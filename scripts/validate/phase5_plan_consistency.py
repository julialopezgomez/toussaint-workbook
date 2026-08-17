#!/usr/bin/env python3
"""Deterministic internal-consistency check for the Phase 5 augmentation plan.

This is a *planning* validator. It touches no application or runtime code and
writes nothing. It exists so that every count published in
`docs/plans/PHASE5_AUGMENTATION_PLAN.md` is re-derivable from evidence rather
than hand-edited.

What it does:

1. Re-derives the committed-baseline module count and hour total directly from
   `src/content/course/**/*.mdx` frontmatter (never from the plan text).
2. Recomputes every published total from the deltas recorded in
   `docs/plans/phase5-planning-ledger.json`.
3. Asserts the ledger's own `published` block matches the recomputation.
4. Asserts every published inventory (labs, static figures, in-block additions)
   matches an explicit enumeration rather than a remembered number.
5. Asserts module and lab IDs are unique, collision-free against the baseline,
   and in ascending intra-block order.
6. Asserts the plan text contains the recomputed headline figures.
7. Asserts no recorded stale claim survives in the plan, the Gate B proposal, or
   the handoff — outside an explicitly-labelled historical correction note.
8. Asserts the plan revision/hash pins agree across the plan, the Gate B
   proposal, and the handoff, and that approved Gate A evidence is unchanged.
9. Asserts exam and cheat-sheet IDs are *enumerated* and match the repository,
   not merely counted.
10. Asserts semantic prerequisite order: every new module's prerequisites
    precede it in the canonical MODULE order, not merely the block order.
11. Asserts the plan's §5.1 per-block table matches the recomputation cell for
    cell, so a hand-edited table cannot drift from the ledger.
12. Asserts the Gate B proposal's `sources.json` v2 draft parses and satisfies
    its own stated schema requirements, that its coverage matrix contains the
    rows it claims, and that its score bands and status assignments agree.
13. Asserts the §2 scored-matrix ID set and the §2.6b status roll-up union are
    the *same set*, with exactly one scored row per roll-up ID, exactly one
    status per scored row, and a printed total equal to both cardinalities.
    (Audit finding C9: `Menagerie` sat in the CONDITIONAL roll-up with no scored
    row, so §2 held 38 rows while §2.6b published 39, and every count agreed.)
14. **Derives** the current Gate-B/proposal status from six regions — the plan
    header, plan §9.6, plan §13's Gate B section, plan §16, the proposal header
    and the handoff — by reading what the prose says about each proposal
    revision number, then compares all six against the ledger's recorded fact
    set and against each other. Labelled historical paragraphs are excluded by
    *region slicing*, not by matching a "Corrected at revision" marker near a
    hit. (Audit finding C1: the plan header was corrected while §13 and §16 went
    on calling the already-failed proposal revision 4 the current unreviewed
    one; a marker-exempted stale-phrase list could not see it. Audit finding
    C1-01: the proposal's numbering note said the revision was "currently 5"
    while its header said 6, and the token regex could not parse that form.)
15. Asserts each scored row's *own* declared status matches its §2.6b roll-up
    bucket and the ledger's `statusMembership`. (Audit finding C9-04: changing
    A1's decision cell from `SELECT` to `OPTIONAL`, leaving roll-up and ledger
    untouched, exited 0.)
16. Derives all **six** `addedHours` components and ties `f8KeyedRecall`,
    `published.f8KeyedRecallHours`, `addedHoursComponents` and the keyed-recall
    hour *policy* to one another. (Audit finding C2-02: the plan claimed this
    check existed; the validator summed five components and never read the F8
    fields, so the F8 component could drift alone.)
17. Derives each status region's required wording from the **value** of the
    ledger fact it is scoped to, via `currentGateBStatus.factAssertions`, and
    renders its own success line from those facts. (Audit finding C1-02: regions
    named assertion labels directly, so the booleans under `facts` were never
    read — flipping `independentReviewRequiredAndAuthorized` to `false` exited 0
    — and the passing diagnostic hard-coded the *withdrawn* authority state.)
18. Asserts the plan's own §5.1 decomposition table enumerates all six
    added-hour components, including the 0.0 h one. (Audit finding C2-03: the
    table said the total decomposed "exactly" and listed five.)
19. Asserts no structural audit on disk targets the **current** candidate while
    the fact set still calls it unreviewed, and that the handoff pins the latest
    audit's hash. (The `PLAN_3_6` audit sat on disk while the plan, proposal and
    handoff all still called plan 3.6 / proposal 7 unreviewed; every region
    agreed with every other, so cross-region comparison could not see it.)
20. Asserts no `CONDITIONAL` source's blocker is scheduled for resolution "at
    acquisition". (Audit finding C4-03: plan §9.9 makes such a source ineligible
    for acquisition *until* the blocker resolves, so the wording is circular; the
    defined route is §9.9.1's Gate-D evaluation-only fetch/read.)

Exit status is non-zero on any failure. `SUMMARY` reports failure and warning
counts. Warnings require judgment; they do not fail the check.

Usage:  python3 scripts/validate/phase5_plan_consistency.py [--verbose]
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
COURSE = REPO / "src" / "content" / "course"
LEDGER = REPO / "docs" / "plans" / "phase5-planning-ledger.json"
PLAN = REPO / "docs" / "plans" / "PHASE5_AUGMENTATION_PLAN.md"
PROPOSAL = REPO / "docs" / "plans" / "GATE_B_SOURCE_SELECTION.md"
GATE_A = REPO / "docs" / "plans" / "GATE_A_BASELINE.md"
HANDOFF = REPO / "docs" / "agent" / "CURRENT_HANDOFF.md"
# Owner-approved Gate A evidence hash. Gate A is closed; this file must not change.
APPROVED_GATE_A_SHA = "470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4"
MILESTONES = REPO / "src" / "content" / "milestones"
CHEATSHEETS = REPO / "src" / "content" / "cheatsheets"

failures: list[str] = []
warnings: list[str] = []


def ok(msg: str) -> None:
    print(f"OK    {msg}")


def fail(msg: str) -> None:
    failures.append(msg)
    print(f"FAIL  {msg}")


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"WARN  {msg}")


def frontmatter(text: str) -> str:
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    return m.group(1)


def field(fm: str, key: str) -> str | None:
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip("\"'") if m else None


def read_baseline_from_worktree() -> tuple[dict[str, dict], list[tuple[str, str, float]]]:
    blocks: dict[str, dict] = collections.defaultdict(lambda: {"modules": 0, "hours": 0.0})
    modules: list[tuple[str, str, float]] = []
    for path in sorted(COURSE.rglob("*.mdx")):
        fm = frontmatter(path.read_text())
        block = path.parent.name
        hours = float(field(fm, "estimatedHours") or 0)
        tier = field(fm, "tier") or "?"
        blocks[block]["modules"] += 1
        blocks[block]["hours"] += hours
        modules.append((field(fm, "id") or path.stem, tier, hours))
    return dict(blocks), modules


def read_baseline_from_commit(commit: str) -> dict[str, dict] | None:
    """Read the same figures from the committed baseline tree, if git is available."""
    try:
        listing = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", commit, "src/content/course/"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout.split()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    blocks: dict[str, dict] = collections.defaultdict(lambda: {"modules": 0, "hours": 0.0})
    for rel in listing:
        if not rel.endswith(".mdx"):
            continue
        text = subprocess.run(
            ["git", "show", f"{commit}:{rel}"], cwd=REPO,
            capture_output=True, text=True, check=True,
        ).stdout
        fm = frontmatter(text)
        blocks[rel.split("/")[3]]["modules"] += 1
        blocks[rel.split("/")[3]]["hours"] += float(field(fm, "estimatedHours") or 0)
    return dict(blocks)


def r1(x: float) -> float:
    """Round to one decimal; every figure in this plan is a multiple of 0.5."""
    return round(x + 0.0, 2)


def id_sort_key(mid: str):
    """Order MATH-02 < MATH-02B < MATH-03, so the 'B' suffix sorts after its base."""
    block, _, num = mid.partition("-")
    digits = "".join(c for c in num if c.isdigit())
    suffix = "".join(c for c in num if c.isalpha())
    return (block, int(digits) if digits else 0, suffix)


def md_rows(text: str) -> list[list[str]]:
    """Every pipe-table data row in `text`, as lists of stripped cells.

    Separator rows (`|---|---|`) are dropped; header rows are kept, because the
    caller knows its own header and it is cheaper to filter there.
    """
    rows = []
    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):
            continue
        rows.append(cells)
    return rows


def jsonc_block(text: str, lang: str = "jsonc") -> object | None:
    """Parse the first fenced ```<lang> block, stripping whole-line // comments."""
    m = re.search(rf"```{lang}\n(.*?)\n```", text, re.S)
    if not m:
        return None
    lines = [ln for ln in m.group(1).split("\n") if not ln.lstrip().startswith("//")]
    try:
        return json.loads("\n".join(lines))
    except json.JSONDecodeError as exc:
        fail(f"Gate B proposal's sources.json draft is not valid JSON: {exc}")
        return None


def frontmatter_id_pairs(folder: Path) -> list[tuple[Path, str]]:
    """(path, declared frontmatter id) for every .mdx in `folder`.

    Falls back to the stem only when a file declares no id at all, which is
    itself reported by the caller rather than silently accepted.
    """
    pairs = []
    for path in sorted(folder.glob("*.mdx")):
        try:
            mid = field(frontmatter(path.read_text()), "id")
        except ValueError:
            mid = None
        pairs.append((path, mid if mid else path.stem))
    return pairs


def frontmatter_ids(folder: Path) -> list[str]:
    return [mid for _, mid in frontmatter_id_pairs(folder)]


def parse_planned_assessments(plan_text: str) -> tuple[list[str], list[str]]:
    """Planned exam and cheat-sheet IDs, read from plan §5.3 itself.

    The ledger must be cross-checked against the plan, not against itself; a
    renamed planned artifact is otherwise invisible to every count-based check.
    """
    m = re.search(r"### 5\.3 Assessment implications\n(.*?)\n(?:###|---)", plan_text, re.S)
    if not m:
        return [], []
    body = m.group(1)
    exams: list[str] = []
    sheets: list[str] = []
    line = re.search(r"\*\*New milestone exams:\s*(\d+)\*\*\s*—(.*)", body)
    if line:
        # The enumeration ends at the first bolded sentence after it; later prose
        # in the same bullet legitimately names existing exams (e.g. DYN-EXAM)
        # and must not be mistaken for a planned one.
        segment = re.split(r"\.\s+\*\*", line.group(2), maxsplit=1)[0]
        exams = re.findall(r"`([A-Z0-9]+-EXAM)`", segment)
        declared = int(line.group(1))
        if len(set(exams)) != declared:
            fail(f"plan §5.3 says {declared} new exams but its own list enumerates "
                 f"{len(set(exams))}: {sorted(set(exams))}")
    line = re.search(r"\*\*New cheat sheets:\s*(\d+)\*\*\s*\(([^)]*)\)", body)
    if line:
        sheets = [s.strip() for s in line.group(2).split(",") if s.strip()]
        declared = int(line.group(1))
        if len(set(sheets)) != declared:
            fail(f"plan §5.3 says {declared} new cheat sheets but its own list enumerates "
                 f"{len(set(sheets))}: {sorted(set(sheets))}")
    # De-duplicate while keeping first-seen order.
    return list(dict.fromkeys(exams)), list(dict.fromkeys(sheets))


def stale_hit_is_exempt(text: str, phrase: str, idx: int, scope: dict) -> bool:
    """True when a stale phrase sits inside a labelled historical correction note.

    A correction register legitimately quotes the wording it removed. Without
    this, the stale check would forbid the very sentences that document the fix.
    """
    ex = scope.get("exemptions", {})
    window = int(ex.get("contextWindow", 400))
    markers = ex.get("markers", [])
    lo = max(0, idx - window)
    hi = min(len(text), idx + len(phrase) + window)
    return any(mk in text[lo:hi] for mk in markers)


# Revision numbers are one or two digits. The trailing \b matters: without it,
# "Proposal revision 6 — 2026-08-15" parses the DATE as a range endpoint and
# expands to every integer from 6 to 2026.
#
# `proposal\s+revisions?` rather than a literal space, and every caller collapses
# whitespace first: a markdown line break falling between "Proposal" and
# "revision 8" made the mention invisible, so revision 8's "is current,
# corrected and unreviewed" landed inside revision *7*'s classifier window and
# the check read a failed revision as the current unreviewed one — the exact C1
# defect class, reintroduced by nothing worse than reflowing a paragraph.
REVISION_MENTION = re.compile(
    r"proposal\s+revisions?\s+(\d{1,2}\b(?:\s*(?:,|and|or|to|–|—|-)\s*\d{1,2}\b)*)", re.I
)

# Audit finding C1-01. The regex above requires a digit immediately after
# "proposal revision", so it could not see the numbering note's detached form —
# "This document has its own proposal revision number (currently 5)" — while the
# header two lines above declared revision 6. Both were live, unlabelled text and
# the check still exited 0. Any phrasing that ties "proposal revision" to a
# "currently <n>" within one clause is a CURRENT-revision claim and is read as one.
# The trailing digit requirement keeps "no review is currently authorized" out.
REVISION_CURRENTLY = re.compile(
    r"proposal\s+revisions?\b[^.|]{0,60}?\bcurrently\s+(\d{1,2})\b", re.I
)

# How far past a revision mention a status word still describes THAT mention. The
# window always stops at the next mention, so an adjacent claim can never bleed
# backwards onto the wrong revision.
CLASSIFIER_WINDOW = 200

CLASSIFIERS = {
    "failed": re.compile(r"\bfail"),
    "unreviewed": re.compile(
        r"unreviewed|not (?:yet )?(?:been )?reviewed|not reviewed|"
        r"awaiting (?:a )?(?:fresh )?(?:independent )?review"
    ),
    "superseded": re.compile(r"supersede"),
    # Deliberately narrow: "C1 current-status regression" must NOT read as a claim
    # that some revision is current.
    "current": re.compile(r"\bis (?:the )?current\b|\bcurrently\b|accompanies"),
}


def expand_revision_expr(expr: str) -> set[int]:
    """'1–4' -> {1,2,3,4}; '1, 2, 3 and 4' -> {1,2,3,4}."""
    out: set[int] = set()
    prev: int | None = None
    pending_range = False
    for tok in re.findall(r"\d+|[–—-]", expr):
        if not tok.isdigit():
            pending_range = True
            continue
        n = int(tok)
        if pending_range and prev is not None:
            out.update(range(min(prev, n), max(prev, n) + 1))
            pending_range = False
        else:
            out.add(n)
        prev = n
    return out


def derive_revision_claims(text: str) -> dict[str, set[int]]:
    """Classify every 'proposal revision N' claim in `text` by its local context.

    This is the C1 check's core. It does not look for known-bad sentences; it reads
    what the prose actually says about each revision number and lets the caller
    compare that against the recorded fact set. A stale-phrase list cannot do this,
    because the next regression will use wording nobody has seen yet.
    """
    # Collapse whitespace before parsing. Markdown wraps prose at arbitrary
    # columns, and a break landing inside a mention or between a mention and its
    # status word must not change what the sentence is read to say.
    flat = re.sub(r"\s+", " ", re.sub(r"\*\*|\*|`", "", text))
    mentions = list(REVISION_MENTION.finditer(flat))
    claims: dict[str, set[int]] = {k: set() for k in CLASSIFIERS}
    claims["mentioned"] = set()
    for i, m in enumerate(mentions):
        nums = expand_revision_expr(m.group(1))
        claims["mentioned"] |= nums
        stop = mentions[i + 1].start() if i + 1 < len(mentions) else len(flat)
        window = flat[m.end():min(stop, m.end() + CLASSIFIER_WINDOW)].lower()
        for name, pat in CLASSIFIERS.items():
            if pat.search(window):
                claims[name] |= nums
    # C1-01: the detached "proposal revision number (currently N)" form.
    for m in REVISION_CURRENTLY.finditer(flat):
        n = int(m.group(1))
        claims["mentioned"].add(n)
        claims["current"].add(n)
    return claims


def fact_key(value: object) -> str:
    """The `factAssertions` lookup key for a recorded fact value.

    Booleans become "true"/"false", `null` becomes "null", and a string fact such
    as `resolvedCorrection: "C2-01"` is its own key. Keeping this one function is
    what lets a fact of any shape drive the same derivation.
    """
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return str(value)


def render_status_summary(cfg: dict) -> str:
    """The passing diagnostic, rendered FROM the facts rather than asserted.

    Audit finding C1-02: this line used to hard-code "no review or approval
    request authorized". That sentence was the *withdrawn* state, so every clean
    run reported stale authority — and because nothing read the booleans, the
    string could not go wrong in a way the check would notice.
    """
    f = cfg["facts"]
    parts = [
        f"failed {sorted(cfg['failedProposalRevisions'])}",
        f"revision {cfg['proposalRevision']} current and "
        + ("reviewed" if f["currentProposalReviewed"] else "unreviewed"),
        "Gate B " + ("started" if f["gateBStarted"] else "not started")
        + "/" + ("approved" if f["gateBApproved"] else "unapproved"),
        "Group A " + ("approved" if f["groupAApproved"] else "unapproved"),
        ("independent review required and authorized"
         if f["independentReviewRequiredAndAuthorized"]
         else "no independent review authorized"),
        ("approval request authorized" if f["approvalRequestAuthorized"]
         else "no approval request authorized"),
        (f"{f['resolvedCorrection']} resolved" if f.get("resolvedCorrection")
         else "no correction resolved"),
        (f"{f['blockedCorrection']} blocked" if f.get("blockedCorrection")
         else "nothing blocked"),
    ]
    return ", ".join(parts)


def check_current_status_agreement(ledger: dict, texts: dict[str, str]) -> None:
    """C1: derive current Gate-B/proposal status per region and compare all of them.

    Six locations must agree with the ledger's recorded fact set AND with each other:
    the plan header, plan §9.6, plan §13's Gate B section, plan §16, the proposal
    header, and the handoff. Regions are delimited by anchors, so a labelled
    historical paragraph is excluded by *not being in the region* — never by a
    marker sitting near a hit, which is how the last regression survived.

    Audit finding C1-02. Each region declares the FACTS it must speak to, and the
    wording it must carry is looked up as `factAssertions[fact][value-in-facts]`.
    Before this, regions named assertion labels directly: the booleans under
    `facts` were decorative, so flipping
    `independentReviewRequiredAndAuthorized` to `false` left six regions
    asserting the opposite and the whole check exited 0.
    """
    cfg = ledger.get("currentGateBStatus")
    if not cfg:
        fail("ledger has no currentGateBStatus block; current-status agreement is unchecked")
        return

    current = cfg["proposalRevision"]
    ledger_failed = set(cfg["failedProposalRevisions"])
    ledger_superseded = ledger_failed | set(cfg["supersededUnreviewedProposalRevisions"])
    patterns = cfg["assertionPatterns"]
    facts = cfg["facts"]
    fact_map = cfg.get("factAssertions")

    derived: dict[str, dict[str, set[int]]] = {}
    problems: list[str] = []

    if not fact_map:
        fail("ledger currentGateBStatus has no factAssertions map; region wording would be "
             "compared against labels instead of against the recorded facts (audit finding C1-02)")
        return

    for region in cfg["regions"]:
        name = region["name"]
        text = texts.get(region["path"])
        if text is None:
            problems.append(f"{name}: {region['path']} not found")
            continue
        start = text.find(region["startAnchor"])
        if start == -1:
            problems.append(f"{name}: start anchor {region['startAnchor']!r} not found — "
                            f"the current-status region cannot be located, so it is unchecked")
            continue
        end = text.find(region["endAnchor"], start)
        if end == -1:
            problems.append(f"{name}: end anchor {region['endAnchor']!r} not found after the start")
            continue
        body = text[start:end]

        claims = derive_revision_claims(body)
        derived[name] = claims

        # --- the derived comparisons, per region
        if not claims["failed"] <= ledger_failed:
            problems.append(
                f"{name}: says proposal revision(s) {sorted(claims['failed'] - ledger_failed)} "
                f"failed; the ledger records {sorted(ledger_failed)}")
        if claims["unreviewed"] & ledger_failed:
            problems.append(
                f"{name}: describes FAILED proposal revision(s) "
                f"{sorted(claims['unreviewed'] & ledger_failed)} as unreviewed/awaiting review — "
                f"a failed revision is reviewed, and naming it as the current unreviewed proposal "
                f"is exactly audit finding C1")
        if not claims["current"] <= {current}:
            problems.append(
                f"{name}: names proposal revision(s) {sorted(claims['current'] - {current})} as "
                f"current; the current proposal revision is {current}")
        if not claims["superseded"] <= ledger_superseded:
            problems.append(
                f"{name}: says proposal revision(s) "
                f"{sorted(claims['superseded'] - ledger_superseded)} are superseded; the ledger "
                f"records {sorted(ledger_superseded)}")
        ahead = {n for n in claims["mentioned"] if n > current}
        if ahead:
            problems.append(
                f"{name}: mentions proposal revision(s) {sorted(ahead)}, ahead of the current "
                f"revision {current}")
        if claims["mentioned"] and not (claims["unreviewed"] | claims["current"]) & {current}:
            problems.append(
                f"{name}: classifies revisions but never states that the current proposal "
                f"revision {current} is unreviewed or current")

        # --- the binding facts this region must carry, DERIVED from the ledger
        # C1-02: the required wording comes from the fact's current value, so a
        # ledger-only fact mutation re-points every region at the opposite
        # assertion instead of leaving the booleans unread.
        # Same whitespace collapse as above, and for the same reason: a line
        # break between "NOT" and "ready for approval" defeated the `(?<!not )`
        # lookbehind and turned an affirmation into a contradiction.
        flat = re.sub(r"\s+", " ", re.sub(r"\*\*|\*|`", " ", body)).lower()
        for fact in region["mustAssertFacts"]:
            if fact not in facts:
                problems.append(
                    f"{name}: requires fact {fact!r}, which currentGateBStatus.facts does not "
                    f"record — the region's wording cannot be derived from anything")
                continue
            key = fact_key(facts[fact])
            assertion = fact_map.get(fact, {}).get(key)
            if assertion is None:
                problems.append(
                    f"{name}: fact {fact} = {facts[fact]!r} has no assertion defined in "
                    f"factAssertions[{fact!r}][{key!r}] — an unmapped fact state must never pass "
                    f"unchecked")
                continue
            spec = patterns.get(assertion)
            if spec is None:
                problems.append(
                    f"{name}: fact {fact} = {facts[fact]!r} maps to assertion {assertion!r}, "
                    f"which assertionPatterns does not define")
                continue
            if not any(re.search(p, flat) for p in spec["affirm"]):
                problems.append(
                    f"{name}: does not assert {assertion} — required because the ledger records "
                    f"{fact} = {facts[fact]!r}")
            hit = [p for p in spec["contradict"] if re.search(p, flat)]
            if hit:
                problems.append(
                    f"{name}: contradicts {assertion} (matched {hit[0]!r}) — the ledger records "
                    f"{fact} = {facts[fact]!r}")

    # --- cross-region agreement: the regions must also agree with EACH OTHER, so a
    # matched pair of wrong regions is caught even if the ledger were edited to match.
    for key in ("failed", "unreviewed", "current", "superseded"):
        seen = {n: c[key] for n, c in derived.items() if c["mentioned"]}
        distinct = {frozenset(v) for v in seen.values() if v}
        if len(distinct) > 1:
            problems.append(
                f"regions disagree on which proposal revisions are {key}: "
                + "; ".join(f"{n}={sorted(v)}" for n, v in sorted(seen.items()) if v))

    if problems:
        fail(f"current Gate-B/proposal status disagrees across the plan, proposal, ledger and "
             f"handoff: {problems}")
    else:
        ok(f"current Gate-B/proposal status derived from {len(derived)} regions and consistent "
           f"with the ledger's recorded facts and with each other "
           f"({render_status_summary(cfg)})")


def check_added_hours_plan_table(plan_text: str, derived: dict[str, float],
                                 added_hours: float, contract: dict) -> None:
    """C2-03: the plan's own §5.1 decomposition must enumerate all six components.

    The ledger and the recomputation were already right. The human-facing table
    said the +142.0 h "decomposes exactly as" and then listed five rows, silently
    dropping `f8KeyedRecall` at 0.0 h — the one component plan §5.3a insists is
    "not omitted". A zero-valued component is exactly the one an eyeball check
    never misses *and* a sum check never catches, so it is checked here.
    """
    spec = (contract or {}).get("planTable")
    if not spec:
        fail("addedHoursComponentContract has no planTable block; the plan's own decomposition "
             "table is unchecked (audit finding C2-03)")
        return

    # Slice §5.1 first. The revision history and §5.3a both quote this lead-in
    # when documenting the finding, and a whole-document search would parse the
    # revision-history table instead of the decomposition.
    sec = re.search(r"### 5\.1 Revised block summary\n(.*?)\n###", plan_text, re.S)
    if not sec:
        fail(f"plan §{spec['planSection']} not found; the decomposition table cannot be located")
        return
    body = sec.group(1)

    m = re.search(r"The \+([\d.]+) h decomposes exactly as", body)
    if not m:
        fail(f"plan §{spec['planSection']} lead-in {spec['leadIn']!r} not found; the decomposition "
             f"table cannot be located")
        return
    if abs(float(m.group(1)) - added_hours) > 1e-9:
        fail(f"plan §{spec['planSection']} says +{m.group(1)} h decomposes exactly; recomputation "
             f"gives {added_hours}")

    tail = body[m.end():]
    rows = [r for r in md_rows(tail[:tail.find("\n\n", tail.find("|"))]) if len(r) == 3]
    component_hours: list[float] = []
    total_cell: str | None = None
    zero_labels: list[str] = []
    for cells in rows:
        label = cells[0].strip("* ").strip()
        if label in ("Component", ""):
            continue
        if "Total" in label:
            total_cell = cells[1].strip("* ")
            continue
        try:
            hours = float(cells[1].strip("* "))
        except ValueError:
            fail(f"plan §{spec['planSection']} decomposition row {label!r} has an unparseable "
                 f"hour figure {cells[1]!r}")
            continue
        component_hours.append(hours)
        if abs(hours) < 1e-9:
            zero_labels.append(label)

    problems: list[str] = []
    if len(component_hours) != spec["requiredComponentRows"]:
        problems.append(
            f"the table lists {len(component_hours)} component rows "
            f"{sorted(component_hours)}, but `addedHours` has {spec['requiredComponentRows']} "
            f"derived components {sorted(derived.values())} — a table that claims to decompose "
            f"the total 'exactly' must enumerate every one, including any worth 0.0 h")
    if sorted(component_hours) != sorted(derived.values()):
        problems.append(
            f"the table's component hours {sorted(component_hours)} are not the same multiset as "
            f"the derived components {sorted(derived.values())}")
    if total_cell is None:
        problems.append(f"plan §{spec['planSection']} decomposition table has no Total row")
    elif abs(float(total_cell) - added_hours) > 1e-9:
        problems.append(f"the table's Total row says {total_cell} h; recomputation gives "
                        f"{added_hours} h")
    if spec.get("mustListZeroValuedComponents"):
        expected_zero = [k for k, v in derived.items() if abs(v) < 1e-9]
        if expected_zero and not zero_labels:
            problems.append(
                f"components {expected_zero} are 0.0 h and the table lists no 0.0 h row — this is "
                f"the omission audit finding C2-03 recorded")
        elif expected_zero and not any("recall" in lb.lower() for lb in zero_labels):
            problems.append(
                f"the table's 0.0 h row(s) {zero_labels} do not name keyed recall, so "
                f"{expected_zero} cannot be identified in the plan's own enumeration")

    if problems:
        fail(f"plan §{spec['planSection']} added-hour decomposition table: {problems}")
    else:
        ok(f"plan §{spec['planSection']} decomposition table enumerates all "
           f"{spec['requiredComponentRows']} added-hour components explicitly, including the "
           f"0.0 h keyed-recall component, and totals {added_hours} h")


def check_audit_freshness(ledger: dict, handoff: str) -> None:
    """A new audit of the CURRENT candidate must not coexist with 'unreviewed' prose.

    This is the class of defect that made the handoff stale entering this pass:
    `PLAN_3_6_STRUCTURAL_AUDIT.md` existed on disk while the plan, the proposal
    and the handoff all still said plan 3.6 / proposal 7 were unreviewed and
    awaiting a fresh review. Every C1 region agreed with every other, and with the
    ledger, so no amount of cross-region comparison could see it — the missing
    fact was on the filesystem.

    The audited revisions are parsed out of each report's own title line, so an
    audit that nobody recorded in the ledger still counts against the claim.
    """
    cfg = ledger.get("auditFreshness")
    status = ledger.get("currentGateBStatus", {})
    if not cfg:
        fail("ledger has no auditFreshness block; a fresh audit of the current candidate could "
             "coexist with continuity documents that still call it unreviewed")
        return

    directory = REPO / cfg["directory"]
    on_disk = sorted(directory.glob(cfg["glob"])) if directory.exists() else []
    if not on_disk:
        warn(f"no audit report matches {cfg['directory']}/{cfg['glob']}; freshness check skipped")
        return

    recorded = {a["path"]: a for a in cfg["audits"]}
    title_re = re.compile(cfg["titlePattern"], re.M | re.I)
    verdict_re = re.compile(cfg["verdictPattern"])
    current_plan = str(status.get("planRevision"))
    current_proposal = status.get("proposalRevision")
    reviewed = bool(status.get("facts", {}).get("currentProposalReviewed"))
    failed_revisions = set(status.get("failedProposalRevisions", []))

    problems: list[str] = []
    parsed: list[tuple[str, str, int, str]] = []

    for path in on_disk:
        rel = str(path.relative_to(REPO))
        text = path.read_text()
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        entry = recorded.get(rel)
        if entry is None:
            problems.append(
                f"{rel} is an audit report that the ledger does not record — a review landed and "
                f"the planning lane's own state was never updated")
            continue
        if entry["sha256"] != sha:
            problems.append(f"{rel}: recorded SHA-256 {entry['sha256'][:12]}… != on-disk "
                            f"{sha[:12]}… — review evidence is read-only and must not change")
        tm = title_re.search(text)
        if not tm:
            problems.append(f"{rel}: title line does not name the plan/proposal revision it "
                            f"audits, so its target cannot be derived from the report itself")
            continue
        a_plan, a_proposal = tm.group(1), int(tm.group(2))
        vm = verdict_re.search(text)
        a_verdict = vm.group(1) if vm else None
        parsed.append((rel, a_plan, a_proposal, a_verdict or "<unparseable>"))

        if a_plan != entry["auditedPlanRevision"] or a_proposal != entry["auditedProposalRevision"]:
            problems.append(
                f"{rel}: the report audits plan {a_plan} / proposal {a_proposal}, but the ledger "
                f"records plan {entry['auditedPlanRevision']} / proposal "
                f"{entry['auditedProposalRevision']}")
        if a_verdict is None:
            problems.append(f"{rel}: no parseable final verdict")
        elif a_verdict != entry["verdict"]:
            problems.append(f"{rel}: report verdict {a_verdict!r} != ledger {entry['verdict']!r}")

        # The freshness rule itself.
        if not reviewed and (a_plan == current_plan or a_proposal == current_proposal):
            problems.append(
                f"{rel} audits plan {a_plan} / proposal {a_proposal}, which IS the current "
                f"candidate (plan {current_plan} / proposal {current_proposal}), yet "
                f"currentProposalReviewed is false and every status region therefore calls the "
                f"current candidate unreviewed — a candidate with an audit against it has been "
                f"reviewed, so the continuity documents are stale by construction")
        if a_verdict == "STRUCTURAL FAIL" and a_proposal not in failed_revisions:
            problems.append(
                f"{rel} records a STRUCTURAL FAIL against proposal revision {a_proposal}, which is "
                f"absent from failedProposalRevisions {sorted(failed_revisions)}")

    missing = sorted(set(recorded) - {str(p.relative_to(REPO)) for p in on_disk})
    if missing:
        problems.append(f"ledger records audit report(s) that are not on disk: {missing}")

    if cfg.get("handoffMustPinLatestAuditSha"):
        latest = recorded.get(cfg["latestAudit"])
        if latest is None:
            problems.append(f"latestAudit {cfg['latestAudit']} is not among the recorded audits")
        elif not handoff:
            warn("handoff not found; latest-audit pin check skipped")
        elif latest["sha256"] not in handoff:
            problems.append(
                f"the handoff does not pin the latest audit's SHA-256 {latest['sha256'][:12]}… "
                f"({cfg['latestAudit']}) — a newer audit can then land without the handoff being "
                f"rewritten, which is exactly how it went stale")

    if problems:
        fail(f"audit/handoff freshness: {problems}")
    else:
        ok(f"audit freshness holds: {len(parsed)} structural audit report(s) parsed from their own "
           f"title lines, all recorded at their exact hashes, none targeting the current candidate "
           f"(plan {current_plan} / proposal {current_proposal}), and the handoff pins the latest "
           f"({cfg['latestAudit'].rsplit('/', 1)[-1]})")


def check_conditional_resolution_terminology(ledger: dict, proposal: str,
                                             draft: object | None) -> None:
    """C4-03: a CONDITIONAL blocker is never resolved "at acquisition".

    Plan §9.9 makes a conditional source ineligible for acquisition *while the
    blocker stands*, and §9.9.1 says in terms that the bounded evaluation-only
    Gate-D fetch "is not acquisition". Scheduling the resolution "at acquisition"
    therefore puts the cure after the condition it is a precondition for. The
    audit cited §7 O5/O6; the same wording sat in §2.6 and in the §5 draft, so
    every conditional resolution statement is swept here rather than two lines.
    """
    gb = ledger.get("gateBProposal", {})
    cfg = gb.get("conditionalResolutionTerminology")
    if not cfg:
        fail("gateBProposal has no conditionalResolutionTerminology block; conditional blocker "
             "resolution wording is unchecked (audit finding C4-03)")
        return
    if not proposal:
        warn("Gate B proposal not found; conditional-terminology check skipped")
        return

    conditional_ids = gb.get("statusMembership", {}).get("CONDITIONAL", [])
    forbidden = [f.lower() for f in cfg["forbiddenInConditionalResolution"]]
    id_re = re.compile(r"\b(" + "|".join(re.escape(i) for i in conditional_ids) + r")\b")
    problems: list[str] = []

    def scan(where: str, text: str) -> None:
        low = text.lower()
        for phrase in forbidden:
            if phrase in low:
                problems.append(f"{where}: resolves a CONDITIONAL blocker {phrase!r}")

    # §2.6 — the activation-condition cell of every conditional row.
    try:
        sec = proposal[proposal.index("### 2.6 `CONDITIONAL` sources"):
                       proposal.index("### 2.6a")]
    except ValueError:
        problems.append("§2.6 conditional table not found")
        sec = ""
    for cells in md_rows(sec):
        if len(cells) != 5 or cells[0].strip("* ").strip() == "ID":
            continue
        if id_re.search(cells[0]):
            scan(f"§2.6 row {cells[0].strip('* ')} activation condition", cells[3])

    # §5 — the executable draft's own conditional entries.
    if isinstance(draft, dict):
        for entry in draft.get("sources", []):
            if not entry.get("conditional"):
                continue
            sid = entry.get("sourceId", "<no sourceId>")
            for key, value in entry.items():
                if isinstance(value, str) and key in (
                    "activationCondition", "resolutionCeiling",
                    "recordedFromPriorKnowledgeNotFetch",
                ):
                    scan(f"§5 draft {sid}.{key}", value)

    # §7 — the resolution cell of every open item that blocks a conditional source.
    try:
        sec7 = proposal[proposal.index("## 7. Open items"):proposal.index("## 8. Constraint")]
    except ValueError:
        problems.append("§7 open items not found")
        sec7 = ""
    for cells in md_rows(sec7):
        if len(cells) != 5 or cells[0].strip("* ").strip() == "#":
            continue
        if id_re.search(cells[2]):
            scan(f"§7 {cells[0].strip('* ')} resolution", cells[3])
            scan(f"§7 {cells[0].strip('* ')} ceiling", cells[4])

    required = [f.lower() for f in cfg.get("requiredPhraseFragments", [])]
    if required and sec:
        low = sec.lower()
        absent = [f for f in required if f not in low]
        if absent:
            problems.append(
                f"§2.6 never names the defined Gate-D evaluation-only route (missing {absent}), so "
                f"the conditional lifecycle has no stated way to resolve a blocker")

    if problems:
        fail(f"CONDITIONAL blocker resolution terminology (audit finding C4-03): {sorted(problems)}")
    else:
        ok(f"no CONDITIONAL source's blocker resolution is scheduled 'at acquisition' across "
           f"§2.6, the §5 draft and §7 ({len(conditional_ids)} conditional IDs swept); each names "
           f"the plan §9.9.1 Gate-D evaluation-only route instead")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    ledger = json.loads(LEDGER.read_text())
    plan_text = PLAN.read_text()
    declared_rev = ledger["planRevision"]

    # ---------------------------------------------------------------- baseline
    live_blocks, live_modules = read_baseline_from_worktree()
    declared = ledger["baselineBlocks"]

    live_total_modules = sum(b["modules"] for b in live_blocks.values())
    live_total_hours = r1(sum(b["hours"] for b in live_blocks.values()))

    if set(live_blocks) != set(declared):
        fail(f"ledger baseline blocks {sorted(declared)} != repository {sorted(live_blocks)}")
    else:
        mismatched = [
            b for b in declared
            if declared[b]["modules"] != live_blocks[b]["modules"]
            or abs(declared[b]["hours"] - live_blocks[b]["hours"]) > 1e-9
        ]
        if mismatched:
            fail(f"ledger baseline differs from repository frontmatter for: {mismatched}")
        else:
            ok(f"ledger baseline matches repository frontmatter "
               f"({live_total_modules} modules, {live_total_hours} h across {len(live_blocks)} blocks)")

    committed = read_baseline_from_commit(ledger["baselineCommit"])
    if committed is None:
        warn("git unavailable; committed-baseline cross-check skipped (worktree figures used)")
    else:
        c_modules = sum(b["modules"] for b in committed.values())
        c_hours = r1(sum(b["hours"] for b in committed.values()))
        per_block_diff = sorted(
            b for b in set(committed) | set(live_blocks)
            if committed.get(b, {}).get("modules") != live_blocks.get(b, {}).get("modules")
            or abs(committed.get(b, {}).get("hours", -1)
                   - live_blocks.get(b, {}).get("hours", -2)) > 1e-9
        )
        if (c_modules, c_hours) != (live_total_modules, live_total_hours):
            fail(f"committed baseline {ledger['baselineCommit'][:12]} is "
                 f"{c_modules} modules / {c_hours} h but the worktree is "
                 f"{live_total_modules} / {live_total_hours}")
        elif per_block_diff:
            fail(f"committed baseline totals match the worktree but PER-BLOCK figures differ "
                 f"for {per_block_diff} — equal totals can hide compensating errors")
        else:
            ok(f"committed baseline {ledger['baselineCommit'][:12]} agrees with the worktree "
               f"per block and in total ({c_modules} modules, {c_hours} h, "
               f"{len(committed)} blocks)")

    # ------------------------------------------------------------ recomputation
    new_modules = ledger["newModules"]
    new_module_hours = r1(sum(m["hours"] for m in new_modules))

    foundation = ledger["foundationStabilization"]["modules"]
    foundation_hours = r1(sum(m["deltaHours"] for m in foundation))

    calibration_hours = r1(sum(m["deltaHours"] for m in ledger["calibrationRepairs"]["modules"]))
    inplace_hours = r1(sum(m["deltaHours"] for m in ledger["inPlaceAdditions"]["modules"]))
    rescope_hours = r1(sum(m["deltaHours"] for m in ledger["rescopes"]["modules"]))

    # C2-02: the SIXTH component. Through plan revision 3.5 `added_hours` was
    # recomputed from five components while plan §1 claimed the six-component
    # enumeration was checked, so the F8 figure could drift on its own.
    f8_recall_hours = r1(ledger["f8KeyedRecall"]["deltaHours"])

    added_hours = r1(new_module_hours + foundation_hours + calibration_hours
                     + inplace_hours + rescope_hours + f8_recall_hours)
    total_hours = r1(live_total_hours + added_hours)
    total_modules = live_total_modules + len(new_modules)

    # Blocks: baseline blocks plus any block introduced by a new module.
    new_blocks = sorted({m["block"] for m in new_modules} - set(live_blocks))
    total_blocks = len(live_blocks) + len(new_blocks)

    # Route split. Tier 3 modules are optional; tiers 1 and 2 are main route.
    # In addition, some approved in-module additions are themselves optional
    # reference boxes (decision 0007), so their hours are optional even though
    # they sit inside a main-route module.
    optional_new = [m for m in new_modules if m["route"] == "optional"]
    optional_boxes = ledger.get("optionalInModuleAdditions", {}).get("items", [])
    optional_box_hours = r1(sum(b["hours"] for b in optional_boxes))
    optional_hours = r1(sum(m["hours"] for m in optional_new)
                        + sum(m["hours"] for m in ledger["existingTier3Modules"])
                        + optional_box_hours)
    main_hours = r1(total_hours - optional_hours)

    # Every optional reference box must correspond to a real foundation-lane
    # delta, or the split is being asserted rather than derived.
    foundation_ids = {m["id"] for m in foundation}
    orphan_boxes = [b["id"] for b in optional_boxes if b["id"] not in foundation_ids]
    if orphan_boxes:
        fail(f"optional reference boxes name modules absent from the foundation lane: {orphan_boxes}")
    elif optional_boxes:
        ok(f"{len(optional_boxes)} optional reference box(es) worth {optional_box_hours} h "
           f"counted as optional, not main route: {[b['id'] for b in optional_boxes]}")

    # Cross-check the declared existing Tier-3 set against frontmatter.
    live_tier3 = {mid: h for mid, tier, h in live_modules if tier == "3"}
    declared_tier3 = {m["id"]: m["hours"] for m in ledger["existingTier3Modules"]}
    if live_tier3 != declared_tier3:
        fail(f"existing Tier-3 set in the ledger {declared_tier3} != frontmatter {live_tier3}")
    else:
        ok(f"existing Tier-3 modules confirmed from frontmatter: {sorted(live_tier3)}")

    # Per-block augmented totals, derived rather than transcribed.
    aug: dict[str, dict] = {
        b: {"modules": v["modules"], "hours": r1(v["hours"])} for b, v in live_blocks.items()
    }
    for b in new_blocks:
        aug[b] = {"modules": 0, "hours": 0.0}
    for m in new_modules:
        aug[m["block"]]["modules"] += 1
        aug[m["block"]]["hours"] = r1(aug[m["block"]]["hours"] + m["hours"])
    for group in ("foundationStabilization", "calibrationRepairs", "inPlaceAdditions", "rescopes"):
        entries = ledger[group]["modules"]
        for m in entries:
            block = m["id"].split("-")[0]
            aug[block]["hours"] = r1(aug[block]["hours"] + m["deltaHours"])

    if r1(sum(v["hours"] for v in aug.values())) != total_hours:
        fail("per-block augmented hours do not sum to the recomputed total")
    elif sum(v["modules"] for v in aug.values()) != total_modules:
        fail("per-block augmented module counts do not sum to the recomputed total")
    else:
        ok(f"per-block augmented table is internally consistent "
           f"({total_modules} modules, {total_hours} h, {total_blocks} blocks)")

    # --------------------------------------------------- ledger published block
    published = ledger["published"]
    expected = {
        "totalModules": total_modules,
        "newModules": len(new_modules),
        "totalBlocks": total_blocks,
        "newBlocks": len(new_blocks),
        "totalHours": total_hours,
        "addedHours": added_hours,
        "mainRouteHours": main_hours,
        "optionalHours": optional_hours,
        "newModuleHours": new_module_hours,
        "foundationStabilizationHours": foundation_hours,
        "inPlaceAdditionHours": inplace_hours,
        "calibrationRepairHours": calibration_hours,
        "rescopeHours": rescope_hours,
        "f8KeyedRecallHours": f8_recall_hours,
    }
    bad = {k: (published.get(k), v) for k, v in expected.items() if published.get(k) != v}
    if bad:
        for key, (got, want) in bad.items():
            fail(f"ledger published.{key} = {got!r} but recomputation gives {want!r}")
    else:
        ok("every recomputed total matches the ledger's published block")

    # ------------------- C2-02: the SIX added-hour components, derived and tied
    # Plan §1 claimed this check existed from revision 3.4. It did not: the old
    # recomputation used five components and never read `f8KeyedRecall`,
    # `addedHoursComponents`, or `published.f8KeyedRecallHours`, so a fixture that
    # raised the F8 component to 2.0 h — and its component total to 144.0 — while
    # leaving the policy and `published.addedHours` at 0.0/142.0 exited 0.
    derived_components = {
        "newModuleHours": new_module_hours,
        "foundationStabilizationHours": foundation_hours,
        "inPlaceAdditionHours": inplace_hours,
        "calibrationRepairHours": calibration_hours,
        "rescopeHours": rescope_hours,
        "f8KeyedRecallHours": f8_recall_hours,
    }
    contract = ledger.get("addedHoursComponentContract")
    comps = ledger.get("addedHoursComponents")
    policy = ledger.get("hourEstimationMethod", {}).get("keyedRecallHourPolicy")
    hour_problems: list[str] = []
    if not contract:
        hour_problems.append("ledger has no addedHoursComponentContract block")
    if not comps:
        hour_problems.append("ledger has no addedHoursComponents block")
    if not policy:
        hour_problems.append("hourEstimationMethod.keyedRecallHourPolicy is missing")
    if comps and contract:
        named = [c["name"] for c in contract["components"]]
        if sorted(named) != sorted(derived_components):
            hour_problems.append(
                f"addedHoursComponentContract names {sorted(named)}, but the validator derives "
                f"{sorted(derived_components)}")
        for key, derived in derived_components.items():
            if comps.get(key) != derived:
                hour_problems.append(
                    f"addedHoursComponents.{key} = {comps.get(key)!r} but the ledger's own "
                    f"module lists give {derived!r}")
        component_sum = r1(sum(derived_components.values()))
        if comps.get("total") != component_sum:
            hour_problems.append(
                f"addedHoursComponents.total = {comps.get('total')!r} but the six components "
                f"sum to {component_sum!r}")
        if component_sum != published.get("addedHours"):
            hour_problems.append(
                f"the six added-hour components sum to {component_sum!r} but "
                f"published.addedHours = {published.get('addedHours')!r} — the F8 component is the "
                f"one that used to drift alone")
    if policy:
        if policy.get("scheduledLearnerHours") != f8_recall_hours:
            hour_problems.append(
                f"keyedRecallHourPolicy.scheduledLearnerHours = "
                f"{policy.get('scheduledLearnerHours')!r} but f8KeyedRecall.deltaHours = "
                f"{f8_recall_hours!r} — the F8 hour policy and the F8 hour component disagree")
        if policy.get("batch") != ledger["f8KeyedRecall"].get("batch"):
            hour_problems.append(
                f"keyedRecallHourPolicy.batch = {policy.get('batch')!r} but f8KeyedRecall.batch = "
                f"{ledger['f8KeyedRecall'].get('batch')!r}")
        elif policy.get("batch") != "F8":
            hour_problems.append(
                f"keyed recall must be produced in F8 (plan §5.3a); ledger says "
                f"{policy.get('batch')!r}")
    if hour_problems:
        fail(f"F8 / added-hour component contract violated: {hour_problems}")
    else:
        ok(f"all six added-hour components derived and tied together "
           f"({' + '.join(str(derived_components[c['name']]) for c in contract['components'])} "
           f"= {added_hours} h; F8 keyed recall {f8_recall_hours} h matches its policy and "
           f"published figure)")

    # C2-03: and the plan's own table must show the same six.
    check_added_hours_plan_table(plan_text, derived_components, added_hours, contract)

    # ------------------------------------------- assessment / artifact inventory
    live_exams = len(list(MILESTONES.glob("*.mdx")))
    live_sheets = len(list(CHEATSHEETS.glob("*.mdx")))
    if published["totalExams"] != live_exams + published["newExams"]:
        fail(f"totalExams {published['totalExams']} != {live_exams} existing + "
             f"{published['newExams']} new")
    else:
        ok(f"exam inventory consistent ({live_exams} existing + {published['newExams']} new "
           f"= {published['totalExams']})")
    if published["totalCheatSheets"] != live_sheets + published["newCheatSheets"]:
        fail(f"totalCheatSheets {published['totalCheatSheets']} != {live_sheets} existing + "
             f"{published['newCheatSheets']} new")
    else:
        ok(f"cheat-sheet inventory consistent ({live_sheets} existing + "
           f"{published['newCheatSheets']} new = {published['totalCheatSheets']})")

    # ---------------------------------------------------- prerequisite integrity
    known = {mid for mid, _, _ in live_modules} | {m["id"] for m in new_modules}
    dangling = sorted({
        p for m in new_modules for p in m["prerequisites"] if p not in known
    })
    if dangling:
        fail(f"new-module prerequisites reference unknown IDs: {dangling}")
    else:
        ok(f"all new-module prerequisites resolve against the {len(known)}-module ID space")

    order = ledger["canonicalBlockOrder"]
    if set(order) != set(aug):
        fail("canonicalBlockOrder does not cover exactly the augmented block set")
    else:
        pos = {b: i for i, b in enumerate(order)}
        forward = []
        for m in new_modules:
            for p in m["prerequisites"]:
                if pos[p.split("-")[0]] > pos[m["block"]]:
                    forward.append(f"{m['id']} <- {p}")
        if forward:
            fail(f"forward block-level prerequisites among new modules: {forward}")
        else:
            ok("no new module declares a prerequisite from a later block in the canonical order")

        optional_ids = {m["id"] for m in optional_new} | set(declared_tier3)
        bad_opt = [
            f"{m['id']} <- {p}" for m in new_modules if m["route"] == "main"
            for p in m["prerequisites"] if p in optional_ids
        ]
        if bad_opt:
            fail(f"main-route modules depend on optional modules: {bad_opt}")
        else:
            ok("no main-route new module depends on an optional-tier module")

    # -------------------------------------------------- ID uniqueness and order
    new_ids = [m["id"] for m in new_modules]
    dupes = sorted({i for i in new_ids if new_ids.count(i) > 1})
    if dupes:
        fail(f"duplicate new-module IDs in the ledger: {dupes}")
    else:
        ok(f"all {len(new_ids)} new-module IDs are unique")

    baseline_ids = {mid for mid, _, _ in live_modules}
    collisions = sorted(set(new_ids) & baseline_ids)
    if collisions:
        fail(f"new-module IDs collide with existing baseline modules: {collisions}")
    else:
        ok("no new-module ID collides with an existing baseline module ID")

    out_of_order = []
    by_block: dict[str, list[str]] = collections.defaultdict(list)
    for m in new_modules:
        by_block[m["block"]].append(m["id"])
    for block, ids in by_block.items():
        if ids != sorted(ids, key=id_sort_key):
            out_of_order.append(block)
    if out_of_order:
        fail(f"new-module IDs are not in ascending intra-block order for: {sorted(out_of_order)}")
    else:
        ok("new-module IDs are in ascending intra-block order in every block")

    # ------------------------------------------- every published inventory figure
    inventories = {
        "labs": len(ledger["labs"]["carriedFromRevision22"])
                + len(ledger["labs"]["addedAtRevision30"]),
        "requiredStaticFigures": sum(
            len(v) for k, v in ledger["requiredStaticFigures"].items() if k != "description"
        ),
        "inBlockAdditions": len([
            m for m in new_modules if m["block"] in live_blocks
        ]) - len([
            m for m in new_modules
            if m["block"] in live_blocks and m.get("origin", "").endswith("relocated")
        ]),
    }
    for key, derived in inventories.items():
        if published.get(key) != derived:
            fail(f"published.{key} = {published.get(key)!r} but enumeration gives {derived!r}")
    if all(published.get(k) == v for k, v in inventories.items()):
        ok(f"enumerated inventories match published figures "
           f"(labs={inventories['labs']}, staticFigures={inventories['requiredStaticFigures']}, "
           f"inBlockAdditions={inventories['inBlockAdditions']})")

    lab_ids = ledger["labs"]["carriedFromRevision22"] + ledger["labs"]["addedAtRevision30"]
    lab_dupes = sorted({i for i in lab_ids if lab_ids.count(i) > 1})
    if lab_dupes:
        fail(f"duplicate lab IDs: {lab_dupes}")
    else:
        ok(f"all {len(lab_ids)} lab IDs are unique")

    # ------------------------------- exam / cheat-sheet inventories BY ID (new)
    # Counting alone let a wrong ID pass. The ledger now enumerates both sets and
    # the repository is the authority for the "existing" half.
    inv = ledger.get("assessmentInventory")
    if not inv:
        fail("ledger has no assessmentInventory block; exam and cheat-sheet IDs are not enumerated")
    else:
        # C9-03: read the actual frontmatter `id`, never the filename stem. A file
        # whose name and declared id disagree is exactly the defect worth catching,
        # and `Path.stem` is blind to it by construction.
        live_exam_ids = sorted(frontmatter_ids(MILESTONES))
        live_sheet_ids = sorted(frontmatter_ids(CHEATSHEETS))
        for label, declared, live, folder in (
            ("exam", inv["existingExamIds"], live_exam_ids, MILESTONES),
            ("cheat-sheet", inv["existingCheatSheetIds"], live_sheet_ids, CHEATSHEETS),
        ):
            if sorted(declared) != live:
                fail(f"ledger's existing {label} frontmatter IDs {sorted(declared)} != "
                     f"repository {live}")
            else:
                ok(f"existing {label} IDs read from frontmatter and match the ledger ({len(live)})")
            # A stem/id divergence is reported on its own terms so the diagnostic
            # names the real problem rather than a downstream count mismatch.
            drift = sorted(
                f"{path.name} declares id {mid!r}"
                for path, mid in frontmatter_id_pairs(folder) if path.stem != mid
            )
            if drift:
                fail(f"{label} filename/frontmatter-id drift: {drift}")

        # C9-01: planned IDs must be parsed from the PLAN and compared with the
        # ledger. Reading them only from the ledger meant the ledger was checked
        # against itself, so a renamed planned artifact was invisible.
        plan_exams, plan_sheets = parse_planned_assessments(plan_text)
        for label, declared, from_plan in (
            ("exam", inv["newExamIds"], plan_exams),
            ("cheat-sheet", inv["newCheatSheetIds"], plan_sheets),
        ):
            if not from_plan:
                fail(f"could not parse planned {label} IDs from plan §5.3; "
                     f"the ledger cannot be cross-checked")
            elif sorted(declared) != sorted(from_plan):
                only_ledger = sorted(set(declared) - set(from_plan))
                only_plan = sorted(set(from_plan) - set(declared))
                fail(f"planned {label} IDs disagree between the ledger and plan §5.3 — "
                     f"in the ledger only: {only_ledger}; in the plan only: {only_plan}")
            else:
                ok(f"planned {label} IDs parsed from plan §5.3 and match the ledger "
                   f"({sorted(from_plan)})")

        for label, new_ids, live, published_key in (
            ("exam", inv["newExamIds"], live_exam_ids, "newExams"),
            ("cheat-sheet", inv["newCheatSheetIds"], live_sheet_ids, "newCheatSheets"),
        ):
            dupes = sorted({i for i in new_ids if new_ids.count(i) > 1})
            clash = sorted(set(new_ids) & set(live))
            if dupes:
                fail(f"duplicate new {label} IDs: {dupes}")
            elif clash:
                fail(f"new {label} IDs already exist in the repository: {clash}")
            elif len(new_ids) != published[published_key]:
                fail(f"published.{published_key} = {published[published_key]} but "
                     f"{len(new_ids)} new {label} IDs are enumerated")
            else:
                ok(f"new {label} IDs unique and collision-free: {sorted(new_ids)}")

        # C9-01: the batch VALUE must be checked, not merely the presence of a key.
        # Every new exam and cheat sheet is F8 (plan §5.3, §13 Gate F).
        required_batch = inv.get("requiredBatchForNewAssessments", "F8")
        for label, ids, batch in (
            ("exam", inv["newExamIds"], inv["newExamBatch"]),
            ("cheat-sheet", inv["newCheatSheetIds"], inv["newCheatSheetBatch"]),
        ):
            missing = sorted(set(ids) - set(batch))
            wrong = sorted(f"{k}={batch[k]}" for k in ids
                           if k in batch and batch[k] != required_batch)
            if missing:
                fail(f"new {label} IDs with no assigned batch: {missing}")
            if wrong:
                fail(f"new {label}s must be produced in {required_batch} "
                     f"(plan §5.3, §13); found: {wrong}")
        if not any(("no assigned batch" in f or "must be produced in" in f) for f in failures):
            ok(f"every new exam and cheat sheet is assigned to {required_batch}")

    # ------------------------- semantic (module-level) prerequisite order (new)
    # The block-level check above cannot see an intra-block violation such as
    # NUM-01 depending on NUM-03. This orders every module in the canonical
    # route and requires each prerequisite to strictly precede its dependent.
    canonical_pos: dict[str, int] = {}
    all_modules = [mid for mid, _, _ in live_modules] + [m["id"] for m in new_modules]
    block_pos = {b: i for i, b in enumerate(ledger["canonicalBlockOrder"])}
    ordered = sorted(all_modules, key=lambda m: (block_pos.get(m.split("-")[0], 99),
                                                 id_sort_key(m)))
    for i, mid in enumerate(ordered):
        canonical_pos[mid] = i

    semantic_violations = []
    for m in new_modules:
        for pre in m["prerequisites"]:
            if pre not in canonical_pos:
                continue  # dangling is already reported above
            if canonical_pos[pre] >= canonical_pos[m["id"]]:
                semantic_violations.append(
                    f"{m['id']} (pos {canonical_pos[m['id']]}) <- {pre} (pos {canonical_pos[pre]})"
                )
    if semantic_violations:
        fail(f"prerequisites that do not precede their dependent in the canonical "
             f"MODULE order: {semantic_violations}")
    else:
        ok(f"semantic prerequisite order holds for all {len(new_modules)} new modules "
           f"across the {len(ordered)}-module canonical route")

    # ------------------------------- the plan's §5.1 table, checked cell by cell
    # A hand-edited table could previously drift from the ledger undetected: the
    # old check only looked for headline figures anywhere in the document.
    sec = re.search(r"### 5\.1 Revised block summary\n(.*?)\n###", plan_text, re.S)
    if not sec:
        fail("plan §5.1 block-summary table not found")
    else:
        table_rows = [r for r in md_rows(sec.group(1)) if len(r) == 8]
        parsed: dict[str, tuple[int, float]] = {}
        published_total_row = None
        for cells in table_rows:
            name = cells[1].strip("* ").strip()
            if name == "Block":
                continue
            if cells[1].strip().strip("*") == "Total":
                published_total_row = cells
                continue
            if name not in aug:
                continue
            try:
                parsed[name] = (int(cells[3].strip("* ")), float(cells[6].strip("* ")))
            except ValueError:
                fail(f"plan §5.1 row for {name} has an unparseable module count or hour figure")
        missing_rows = sorted(set(aug) - set(parsed))
        if missing_rows:
            fail(f"plan §5.1 table has no row for: {missing_rows}")
        bad_cells = sorted(
            f"{b}: table says {parsed[b][0]} modules / {parsed[b][1]} h, "
            f"recomputation gives {aug[b]['modules']} / {aug[b]['hours']}"
            for b in parsed
            if parsed[b][0] != aug[b]["modules"] or abs(parsed[b][1] - aug[b]["hours"]) > 1e-9
        )
        if bad_cells:
            for b in bad_cells:
                fail(f"plan §5.1 table disagrees with the ledger — {b}")
        if published_total_row is None:
            fail("plan §5.1 table has no Total row")
        elif (published_total_row[3].strip("* ") != str(total_modules)
              or published_total_row[6].strip("* ") != str(total_hours)):
            fail(f"plan §5.1 Total row says {published_total_row[3]} modules / "
                 f"{published_total_row[6]} h; recomputation gives {total_modules} / {total_hours}")
        if not missing_rows and not bad_cells and published_total_row is not None:
            ok(f"plan §5.1 table matches the recomputation cell for cell "
               f"({len(parsed)} block rows + total)")

    # ----------------------------------------- exact revision/hash pin agreement
    plan_sha = hashlib.sha256(PLAN.read_bytes()).hexdigest()
    handoff = HANDOFF.read_text() if HANDOFF.exists() else ""
    proposal = PROPOSAL.read_text() if PROPOSAL.exists() else ""

    if not proposal:
        warn(f"{PROPOSAL.relative_to(REPO)} not found; Gate B pin check skipped")
    else:
        if plan_sha not in proposal:
            fail(f"Gate B proposal does not pin the current plan SHA-256 {plan_sha[:12]}…")
        else:
            ok(f"Gate B proposal pins the current plan SHA-256 {plan_sha[:12]}…")
        if f"revision {declared_rev}" not in proposal:
            fail(f"Gate B proposal does not name plan revision {declared_rev}")
        else:
            ok(f"Gate B proposal names plan revision {declared_rev}")

    if not handoff:
        warn("handoff not found; pin check skipped")
    else:
        if plan_sha not in handoff:
            fail(f"handoff does not pin the current plan SHA-256 {plan_sha[:12]}…")
        else:
            ok(f"handoff pins the current plan SHA-256 {plan_sha[:12]}…")
        if proposal:
            proposal_sha = hashlib.sha256(PROPOSAL.read_bytes()).hexdigest()
            if proposal_sha not in handoff:
                fail(f"handoff does not pin the current Gate B proposal SHA-256 "
                     f"{proposal_sha[:12]}…")
            else:
                ok(f"handoff pins the current Gate B proposal SHA-256 {proposal_sha[:12]}…")

    # Gate A evidence must remain byte-identical to its approved hash.
    if GATE_A.exists():
        gate_a_sha = hashlib.sha256(GATE_A.read_bytes()).hexdigest()
        if gate_a_sha != APPROVED_GATE_A_SHA:
            fail(f"{GATE_A.relative_to(REPO)} has changed: {gate_a_sha[:12]}… != approved "
                 f"{APPROVED_GATE_A_SHA[:12]}… — Gate A evidence is immutable")
        else:
            ok(f"Gate A evidence unchanged at approved SHA-256 {APPROVED_GATE_A_SHA[:12]}…")

    # ------------------------------------------------------------- plan wording
    required = [
        (f"**{total_modules}**", "total module count"),
        (f"**{total_blocks}**", "total block count"),
        (f"**{total_hours}", "total hour figure"),
        (f"**+{len(new_modules)} modules", "new-module count"),
    ]
    for needle, label in required:
        if needle not in plan_text:
            fail(f"plan text does not contain the recomputed {label} ({needle!r})")
    if not failures or all("plan text does not contain" not in f for f in failures):
        ok("plan text contains every recomputed headline figure")

    # ---------------------------------- stale claims, across ALL three documents
    # Previously this scanned the plan only, so an identical stale claim could
    # survive in the proposal or the handoff undetected.
    scope = ledger.get("staleClaimScope", {})
    docs = scope.get("documents", ["docs/plans/PHASE5_AUGMENTATION_PLAN.md"])
    stale_hits: list[str] = []
    for rel in docs:
        path = REPO / rel
        if not path.exists():
            warn(f"{rel} not found; stale-claim scan skipped for it")
            continue
        text = path.read_text()
        for phrase in ledger["staleClaimsThatMustNotAppear"]:
            idx = text.find(phrase)
            while idx != -1:
                if not stale_hit_is_exempt(text, phrase, idx, scope):
                    stale_hits.append(f"{rel}: {phrase!r}")
                    break
                idx = text.find(phrase, idx + 1)
    if stale_hits:
        fail(f"stale claim(s) present outside a labelled correction note: {sorted(set(stale_hits))}")
    else:
        ok(f"none of the {len(ledger['staleClaimsThatMustNotAppear'])} recorded stale claims "
           f"appear unqualified in any of the {len(docs)} continuity documents")

    if f"**Revision {declared_rev}" not in plan_text:
        fail(f"plan header does not declare revision {declared_rev}")
    else:
        ok(f"plan header declares revision {declared_rev}")

    # ------------------------------------------- Gate B proposal, checked (new)
    draft: object | None = None
    gb = ledger.get("gateBProposal")
    if not gb:
        warn("ledger has no gateBProposal block; proposal checks skipped")
    elif not proposal:
        warn("Gate B proposal not found; proposal checks skipped")
    else:
        if f"**Proposal revision {gb['proposalRevision']}" not in proposal:
            fail(f"proposal does not declare proposal revision {gb['proposalRevision']}")
        else:
            ok(f"proposal declares proposal revision {gb['proposalRevision']}")

        # --- 12a. schema completeness of the sources.json v2 draft
        draft = jsonc_block(proposal)
        if draft is None:
            fail("Gate B proposal contains no parseable sources.json v2 draft")
        else:
            entries = draft.get("sources", [])
            if len(entries) != gb["expectedSourceEntries"]:
                fail(f"sources.json draft has {len(entries)} entries; ledger expects "
                     f"{gb['expectedSourceEntries']}")
            problems: list[str] = []
            for e in entries:
                sid = e.get("sourceId", "<no sourceId>")
                for key in gb["sourceEntryRequiredFields"]:
                    if key not in e:
                        problems.append(f"{sid}: missing {key}")
                if not any(k in e for k in gb["sourceEntryLicenseFields"]):
                    problems.append(f"{sid}: no license or licenseNote")
                if e.get("conditional"):
                    for key in gb["conditionalRequiredFields"]:
                        if key not in e:
                            problems.append(f"{sid}: conditional but missing {key}")
            if problems:
                fail(f"sources.json draft entries are incomplete: {sorted(problems)[:12]}"
                     f"{' …' if len(problems) > 12 else ''}")
            elif len(entries) == gb["expectedSourceEntries"]:
                ok(f"sources.json v2 draft is schema-complete ({len(entries)} entries; every "
                   f"conditional entry carries all {len(gb['conditionalRequiredFields'])} "
                   f"consequence fields)")

            # --- 12b. the PDF half must match the real manifest exactly
            man_path = REPO / "data" / "source-manifest" / "manifest.json"
            pdfs = [e for e in entries if e.get("kind") == "pdf"]
            if not man_path.exists():
                warn("manifest.json not found; PDF migration cross-check skipped")
            elif len(pdfs) != gb["expectedPdfEntries"]:
                fail(f"sources.json draft has {len(pdfs)} pdf entries; expected "
                     f"{gb['expectedPdfEntries']}")
            else:
                man = {m["source_id"]: m for m in json.loads(man_path.read_text())}
                pdf_bad = []
                for e in pdfs:
                    src = man.get(e["sourceId"])
                    if src is None:
                        pdf_bad.append(f"{e['sourceId']}: not in manifest.json")
                        continue
                    if e.get("sha256") != src["sha256"]:
                        pdf_bad.append(f"{e['sourceId']}: sha256 truncated or altered")
                    if e.get("pageCount") != src["page_count"]:
                        pdf_bad.append(f"{e['sourceId']}: pageCount differs")
                    if e.get("relativePath") != src["relative_path"]:
                        pdf_bad.append(f"{e['sourceId']}: relativePath dropped or altered")
                    toc = e.get("embeddedToc", {})
                    if toc.get("entryCount") != len(src["embedded_toc"]):
                        pdf_bad.append(f"{e['sourceId']}: embeddedToc entryCount wrong")
                    for v1 in ("pdfMetadata", "extraction"):
                        if v1 not in e:
                            pdf_bad.append(f"{e['sourceId']}: v1 field {v1} not retained")
                if pdf_bad:
                    fail(f"migrated PDF entries disagree with manifest.json: {sorted(pdf_bad)}")
                else:
                    ok(f"all {len(pdfs)} migrated PDF entries carry full 64-hex hashes and every "
                       f"retained v1 field, matching manifest.json")

            # --- 12c. conditional / optional sets agree with the ledger
            draft_cond = sorted(e["sourceId"] for e in entries if e.get("conditional"))
            if draft_cond != sorted(gb["conditionalSourceIds"]):
                fail(f"conditional sources in the draft {draft_cond} != ledger "
                     f"{sorted(gb['conditionalSourceIds'])}")
            else:
                ok(f"the {len(draft_cond)} CONDITIONAL entries match the ledger exactly")
            draft_opt = sorted(e["sourceId"] for e in entries if e.get("optional"))
            if draft_opt != sorted(gb["optionalSourceIdsWithEntries"]):
                fail(f"optional-with-entry sources {draft_opt} != ledger "
                     f"{sorted(gb['optionalSourceIdsWithEntries'])}")
            elif set(draft_cond) & set(draft_opt):
                fail(f"sources marked both conditional and optional: "
                     f"{sorted(set(draft_cond) & set(draft_opt))}")
            else:
                ok("no source is both CONDITIONAL and OPTIONAL; the states are exclusive")

        # --- 12d. coverage-matrix completeness, counted from the document
        cov = gb["coverageMatrix"]
        try:
            sec6 = proposal[proposal.index("## 6. Coverage matrix"):
                            proposal.index("## 7. Open items")]
        except ValueError:
            fail("Gate B proposal §6 coverage matrix not found")
            sec6 = ""
        if sec6:
            headers = {"Unit", "Unit (documentation page)"}
            matrix_rows = [
                r for r in md_rows(sec6)
                if len(r) == len(cov["columns"]) and r[0] not in headers
            ]
            if len(matrix_rows) != cov["totalRows"]:
                fail(f"coverage matrix contains {len(matrix_rows)} four-column rows; "
                     f"ledger expects {cov['totalRows']}")
            else:
                ok(f"coverage matrix materializes all {cov['totalRows']} promised rows with "
                   f"{len(cov['columns'])} columns each")

            # C9-02: a row count cannot see a unit duplicated over another.
            # Uniqueness is scoped PER SOURCE — two different books may each have a
            # "Ch.1 Introduction", and C1/C9 may each document "Python bindings".
            # Duplication only signals a defect within one source's own unit set.
            def unit_key(cell: str) -> str:
                return re.sub(r"[*`_]", "", cell).strip().lower()

            # A row's IDENTITY is its locator, not its whole cell. "UA ch.1 Fully-
            # vs underactuated" and "UA ch.1 The simple pendulum" are the same unit
            # cited twice — which is exactly the count-preserving corruption the row
            # count cannot see — so the trailing title must not make them distinct.
            required_keys = sorted(
                (unit_key(u) for units in cov.get("requiredUnits", {}).values() for u in units),
                key=len, reverse=True,
            )

            def unit_identity(cell: str) -> str:
                k = unit_key(cell)
                for req in required_keys:
                    if k == req or k.startswith(req + " "):
                        return req
                m = re.match(r"^(?:ua|rm)\s+(?:ch\.\s*\d+|appendix\s+[a-e])", k)
                if m:
                    return m.group(0)
                m = re.match(r"^(?:ch\.\s*\d+|§\s*[\w.]+)", k)
                if m:
                    return m.group(0)
                return k

            groups: dict[str, list[str]] = {}
            current = "(preamble)"
            for line in sec6.split("\n"):
                stripped = line.strip()
                if stripped.startswith("#"):
                    current = stripped.lstrip("# ").strip()
                    continue
                if re.match(r"^\*\*C\d+ ", stripped):      # documentation sub-tables
                    current = stripped.strip("*").strip()
                    continue
                if not stripped.startswith("|"):
                    continue
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                if len(cells) != len(cov["columns"]) or cells[0] in headers:
                    continue
                if all(set(c) <= set("-: ") for c in cells):
                    continue
                groups.setdefault(current, []).append(unit_identity(cells[0]))

            dupes_by_group = {
                g: sorted({k for k in ks if ks.count(k) > 1})
                for g, ks in groups.items()
            }
            dupes_by_group = {g: v for g, v in dupes_by_group.items() if v}
            if dupes_by_group:
                fail(f"coverage matrix repeats a unit identity within a single source — a duplicate "
                     f"silently replaces a required unit while the row count stays correct: "
                     f"{dupes_by_group}")
            else:
                ok(f"coverage unit identities are distinct within each of the {len(groups)} "
                   f"source sections ({sum(len(v) for v in groups.values())} rows)")

            # Membership by identity: every unit the ledger requires must appear.
            # Rows carry a title after the locator ("UA ch.2 The simple pendulum"),
            # so a required unit matches as a prefix of the normalized cell.
            all_keys = {k for ks in groups.values() for k in ks}
            missing_units = {}
            for src, units in cov.get("requiredUnits", {}).items():
                absent = [u for u in units if unit_key(u) not in all_keys]
                if absent:
                    missing_units[src] = sorted(absent)
            if missing_units:
                fail(f"coverage matrix is missing required unit(s) by identity: {missing_units}")
            elif cov.get("requiredUnits"):
                total_required = sum(len(v) for v in cov["requiredUnits"].values())
                ok(f"all {total_required} ledger-required coverage units are present by identity "
                   f"across {len(cov['requiredUnits'])} source(s)")
            if sum(cov["perSourceRows"].values()) != cov["totalRows"]:
                fail("ledger's per-source coverage rows do not sum to its own total")
            docs_sum = sum(cov["documentationRowsPerSource"].values())
            if docs_sum != cov["perSourceRows"]["documentation"]:
                fail(f"documentation rows per source sum to {docs_sum}, not "
                     f"{cov['perSourceRows']['documentation']}")
            else:
                ok(f"documentation coverage rows enumerate to {docs_sum} across "
                   f"{len(cov['documentationRowsPerSource'])} sources")
            ted = cov["tedrakeSourceUnits"]
            if (ted["underactuatedChapters"] + ted["underactuatedAppendices"]
                    + ted["manipulationChapters"] != ted["total"]):
                fail("Tedrake source-unit arithmetic does not sum to its declared total")
            elif (cov["perSourceRows"]["B1"] + cov["perSourceRows"]["B2"]) != ted["total"]:
                fail(f"B1+B2 coverage rows {cov['perSourceRows']['B1']}+"
                     f"{cov['perSourceRows']['B2']} != {ted['total']} Tedrake source units")
            else:
                ok(f"all {ted['total']} Tedrake source units are instantiated "
                   f"({ted['underactuatedChapters']} ch + {ted['underactuatedAppendices']} app "
                   f"+ {ted['manipulationChapters']} ch)")

        # --- 12e. score/status consistency across the §2 matrices
        try:
            sec2 = proposal[proposal.index("## 2. Scored decision matrix"):
                            proposal.index("## 3. Per-source detail")]
        except ValueError:
            fail("Gate B proposal §2 scored matrix not found")
            sec2 = ""
        if sec2:
            vocab = gb["statusVocabulary"]
            bands = gb["scoreBands"]
            score_problems: list[str] = []
            scored_ids: list[str] = []
            row_status: dict[str, str] = {}   # C9-04: source ID -> status its own row declares
            for cells in md_rows(sec2):
                # Score rows are: ID | Source | 11 criteria | Total | Decision = 15 cells.
                if len(cells) != 15:
                    continue
                sid = cells[0].strip("* ").strip()
                if not sid or sid == "ID":
                    continue
                try:
                    scores = [int(c.strip("* ")) for c in cells[2:13]]
                    total = int(cells[13].strip("* "))
                except ValueError:
                    continue
                scored_ids.append(sid)
                decision = cells[14]
                # C9-04: record WHICH status the row declares, not merely that it
                # declares one. Without this, changing A1's decision cell from
                # SELECT to OPTIONAL left the roll-up and the ledger untouched and
                # the whole check exited 0.
                declared = [s for s in vocab if s in decision]
                if len(declared) == 1:
                    row_status[sid] = declared[0]
                if sum(scores) != total:
                    score_problems.append(f"{sid}: scores sum to {sum(scores)}, row says {total}")
                if total > bands["maxScore"]:
                    score_problems.append(f"{sid}: total {total} exceeds {bands['maxScore']}")
                if total < bands["eligibleNarrowedRoleFloor"]:
                    score_problems.append(
                        f"{sid}: total {total} is below the {bands['eligibleNarrowedRoleFloor']} "
                        f"eligibility floor but is not recorded as rejected")
                # The decision cell must name exactly one status from the vocabulary.
                named = [s for s in vocab if s in decision]
                if len(named) != 1:
                    score_problems.append(
                        f"{sid}: decision cell names {len(named)} statuses {named}, expected exactly 1")
            dupe_scored = sorted({i for i in scored_ids if scored_ids.count(i) > 1})
            if dupe_scored:
                score_problems.append(f"duplicate scored source IDs in §2: {dupe_scored}")

            # C9-02: compare MEMBERSHIP, not just printed counts. Moving a source
            # between SELECT and OPTIONAL preserves every count and must still fail.
            membership = gb.get("statusMembership", {})
            rollup: dict[str, list[str]] = {}
            for status in vocab:
                row = re.search(
                    rf"\|\s*\*\*`{status}`\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|([^|]*)\|", proposal)
                if not row:
                    score_problems.append(f"{status}: no row in the §2.6b roll-up")
                    continue
                printed_count = int(row.group(1))
                ids = [i.strip() for i in re.split(r"[,·]", row.group(2)) if i.strip()]
                rollup[status] = ids
                if printed_count != gb["statusCounts"][status]:
                    score_problems.append(
                        f"{status}: roll-up count {printed_count}, ledger {gb['statusCounts'][status]}")
                if len(ids) != printed_count:
                    score_problems.append(
                        f"{status}: roll-up prints {printed_count} but lists {len(ids)} IDs")
                if status in membership and sorted(ids) != sorted(membership[status]):
                    only_doc = sorted(set(ids) - set(membership[status]))
                    only_ledger = sorted(set(membership[status]) - set(ids))
                    score_problems.append(
                        f"{status} MEMBERSHIP differs from the ledger — in the proposal only: "
                        f"{only_doc}; in the ledger only: {only_ledger}")
            # A source must appear in exactly one status list.
            all_listed = [i for ids in rollup.values() for i in ids]
            multi = sorted({i for i in all_listed if all_listed.count(i) > 1})
            if multi:
                score_problems.append(f"source(s) listed under more than one status: {multi}")

            # C9 (proposal revision 6): the scored MATRIX and the §2.6b ROLL-UP must be
            # the same set. Every previous check compared printed counts with ledger
            # constants and the ledger with itself, so `Menagerie` could sit in the
            # CONDITIONAL roll-up with no scored row at all: 38 scored rows, 39 printed.
            scored_set = set(scored_ids)
            rollup_set = set(all_listed)
            only_rollup = sorted(rollup_set - scored_set)
            only_scored = sorted(scored_set - rollup_set)
            if only_rollup:
                score_problems.append(
                    f"roll-up ID(s) with NO scored row in §2.1–§2.5: {only_rollup} — a status was "
                    f"assigned to a source that was never scored")
            if only_scored:
                score_problems.append(
                    f"scored row(s) absent from every §2.6b status list: {only_scored} — a scored "
                    f"source carries no status")
            # Exactly one scored row per roll-up ID, and exactly one status per scored row.
            wrong_row_count = sorted(
                f"{i}×{scored_ids.count(i)}" for i in rollup_set if scored_ids.count(i) != 1)
            if wrong_row_count:
                score_problems.append(
                    f"roll-up ID(s) without exactly one scored row: {wrong_row_count}")
            wrong_status_count = sorted(
                f"{i}×{all_listed.count(i)}" for i in scored_set if all_listed.count(i) != 1)
            if wrong_status_count:
                score_problems.append(
                    f"scored row(s) not in exactly one roll-up status: {wrong_status_count}")

            # C9-04: each scored row's OWN declared status must match its roll-up
            # bucket and the ledger. The set checks above compare membership as
            # sets; they cannot see a row whose decision cell says something the
            # roll-up contradicts, because the roll-up alone decided the bucket.
            id_to_bucket = {i: status for status, ids in rollup.items() for i in ids}
            for sid in sorted(row_status):
                declared = row_status[sid]
                bucket = id_to_bucket.get(sid)
                if bucket is not None and bucket != declared:
                    score_problems.append(
                        f"scored row {sid} declares {declared} but the §2.6b roll-up lists it "
                        f"under {bucket}")
                led_bucket = next(
                    (s for s in vocab if sid in membership.get(s, [])), None)
                if led_bucket is not None and led_bucket != declared:
                    score_problems.append(
                        f"scored row {sid} declares {declared} but ledger statusMembership puts "
                        f"it under {led_bucket}")

            # The printed total must equal BOTH cardinalities, not just the ledger's.
            total_row = re.search(
                r"\|\s*\|\s*\*\*(\d+)\*\*\s*\|\s*Total scored sources", proposal)
            if not total_row:
                score_problems.append("§2.6b has no parseable 'Total scored sources' row")
            else:
                printed_total = int(total_row.group(1))
                if not (printed_total == len(scored_set) == len(rollup_set)):
                    score_problems.append(
                        f"§2.6b prints {printed_total} total scored sources, but §2 has "
                        f"{len(scored_set)} scored rows and the roll-up lists {len(rollup_set)} IDs")
                elif printed_total != gb["statusCounts"]["totalScored"]:
                    score_problems.append(
                        f"§2.6b printed total {printed_total} != ledger totalScored "
                        f"{gb['statusCounts']['totalScored']}")

            if score_problems:
                fail(f"score/status contract violations: {sorted(score_problems)}")
            else:
                ok(f"score/status contract holds: {len(scored_ids)} scored rows each sum to their "
                   f"total and name exactly one status; every row's declared status matches its "
                   f"§2.6b bucket and the ledger; the scored set and the roll-up union are the "
                   f"SAME {len(scored_set)} IDs, one scored row and one status each, and the "
                   f"printed total agrees with both "
                   f"({', '.join(f'{k} {gb['statusCounts'][k]}' for k in vocab)})")
            if sum(gb["statusCounts"][k] for k in vocab) != gb["statusCounts"]["totalScored"]:
                fail("ledger status counts do not sum to totalScored")

    # ------------------------- current Gate-B / proposal status, DERIVED (new)
    check_current_status_agreement(ledger, {
        "docs/plans/PHASE5_AUGMENTATION_PLAN.md": plan_text,
        "docs/plans/GATE_B_SOURCE_SELECTION.md": proposal,
        "docs/agent/CURRENT_HANDOFF.md": handoff,
    })

    # The six regions above can only agree with each other and with the ledger.
    # These two read state the ledger does not own: the review directory, and the
    # proposal's conditional lifecycle.
    check_audit_freshness(ledger, handoff)
    check_conditional_resolution_terminology(ledger, proposal, draft)

    if args.verbose:
        print("\n--- recomputed augmented architecture ---")
        for b in order:
            v = aug[b]
            print(f"  {b:<7} {v['modules']:>3} modules  {v['hours']:>6.1f} h")
        print(f"  {'TOTAL':<7} {total_modules:>3} modules  {total_hours:>6.1f} h "
              f"({main_hours} main / {optional_hours} optional)")

    print(f"SUMMARY {len(failures)} failure(s), {len(warnings)} warning(s). "
          f"This validates internal arithmetic and ID integrity, not pedagogy.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
