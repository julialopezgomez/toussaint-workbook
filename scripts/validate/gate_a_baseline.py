#!/usr/bin/env python3
"""Gate A baseline reporter for the Phase 5 augmentation plan.

WHAT THIS IS
    A *reporter*, not the project's validation suite (that is Gate D work, per
    plan §14.1). It reproduces the current-state claims in
    docs/plans/PHASE5_AUGMENTATION_PLAN.md §2 and emits a concept/depth
    inventory.

SIDE EFFECTS — this script is NOT read-only
    It reads the content tree and WRITES exactly one artifact:
        docs/plans/gate-a-concept-depth-inventory.json
    Nothing else is created or modified. Pass --no-write to suppress it.

RESULT SEMANTICS — a reproduced defect is not a passing validation
    OK     invariant holds (genuine validation success)
    REPRO  a KNOWN, DOCUMENTED defect reproduced exactly as the plan describes.
           This is evidence the baseline is understood. It is NOT success, and
           it is NOT a fix. Each REPRO names the plan section that owns it.
    QUEUE  a measurement that feeds semantic review. NOT a pass/fail judgment
           and never a build failure (see --help notes on QUEUE checks).
    FAIL   an expectation did not reproduce -> the plan's stated baseline is
           wrong, or the tree changed. Exits non-zero.

EXIT CODES
    0  no FAIL
    1  at least one FAIL (unexpected result -- investigate before trusting the plan)
    2  bad invocation

TREE SELECTION — committed baseline vs dirty worktree must not be conflated
    --tree PATH  run against an arbitrary checkout (e.g. an isolated
                 `git archive` of the Phase 4 commit). Defaults to the
                 repository containing this script, i.e. the CURRENT WORKTREE,
                 which may contain uncommitted work.
    The chosen tree, and whether it is dirty, is printed in the header.

Usage:
    .venv/bin/python scripts/validate/gate_a_baseline.py
    .venv/bin/python scripts/validate/gate_a_baseline.py --tree /tmp/baseline-dd2e871 --no-write
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

SCRIPT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

IMPLEMENTED_BLOCK_ORDER = [
    "MATH", "OPT", "PROB", "ODE", "KIN", "DYN", "PLAN", "MANIP",
    "ML", "RL", "SYM", "REV1", "RLEARN", "REV2", "CAP",
]
PROPOSED_BLOCK_ORDER = [
    "MATH", "PROB", "OPT", "ODE", "KIN", "DYN", "PLAN", "MANIP",
    "ML", "RL", "SYM", "REV1", "RLEARN", "REV2", "CAP",
]

# Plan §3 depth scale.
DEPTH_LABELS = {
    0: "absent", 1: "mentioned", 2: "explained conceptually", 3: "mathematically derived",
    4: "practised by written exercise", 5: "implemented in executable code",
    6: "used in simulation", 7: "applied in an integrated robotics task",
}

results: list[tuple[str, str, str, str]] = []  # (id, status, detail, owner)


def record(cid: str, status: str, detail: str, owner: str = "") -> None:
    assert status in {"OK", "REPRO", "QUEUE", "FAIL"}
    results.append((cid, status, detail, owner))


def expect(cid: str, ok: bool, detail: str, owner: str = "", kind: str = "OK") -> None:
    """Assert an expectation; FAIL if it does not hold."""
    record(cid, kind if ok else "FAIL", detail, owner)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tree", default=SCRIPT_ROOT, help="checkout to analyse (default: this worktree)")
    ap.add_argument("--no-write", action="store_true", help="do not write the inventory artifact")
    ap.add_argument("--label", default=None, help="label for this run, recorded in the artifact")
    ap.add_argument("--out", default=None,
                    help="write the inventory here instead of <tree>/docs/plans/. Use this to record "
                         "an isolated committed-baseline analysis inside the working repository.")
    args = ap.parse_args()

    root = os.path.abspath(args.tree)
    if not os.path.isdir(os.path.join(root, "src", "content", "course")):
        print(f"error: {root} is not a workbook checkout", file=sys.stderr)
        return 2

    def p(*parts: str) -> str:
        return os.path.join(root, *parts)

    # ---- provenance header ---------------------------------------------
    try:
        commit = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"],
                                capture_output=True, text=True).stdout.strip() or "n/a (archive)"
        dirty = subprocess.run(["git", "-C", root, "status", "--porcelain"],
                               capture_output=True, text=True).stdout.strip()
    except Exception:
        commit, dirty = "n/a", ""
    tree_kind = "DIRTY WORKTREE" if dirty else "clean tree"
    label = args.label or ("worktree" if dirty else "committed-baseline")

    print(f"tree      : {root}")
    print(f"commit    : {commit}")
    print(f"state     : {tree_kind}" + (f" ({len(dirty.splitlines())} changed paths)" if dirty else ""))
    print(f"label     : {label}")
    print(f"dist/     : {'present' if os.path.isdir(p('dist')) else 'ABSENT (run npm run build)'}\n")

    # ---- load ------------------------------------------------------------
    def frontmatter(path: str) -> str:
        return open(path, encoding="utf-8").read().split("---")[1]

    def scalar(fm: str, key: str) -> str | None:
        m = re.search(rf'^{key}:\s*"?([^"\n]+)"?', fm, re.M)
        return m.group(1).strip() if m else None

    def inline_list(fm: str, key: str) -> list[str]:
        m = re.search(rf"^{key}:\s*\[(.*?)\]", fm, re.M)
        return [x.strip().strip("\"'") for x in m.group(1).split(",") if x.strip()] if m else []

    def block_list(fm: str, key: str) -> list[str]:
        m = re.search(rf"^{key}:\s*\n((?:\s+-\s+.*\n)+)", fm, re.M)
        if not m:
            return []
        return [re.sub(r'^\s*-\s*"?|"?\s*$', "", ln) for ln in m.group(1).rstrip("\n").split("\n")]

    mods: dict[str, dict] = {}
    for f in sorted(glob.glob(p("src/content/course/*/*.mdx"))):
        body = open(f, encoding="utf-8").read()
        fm = body.split("---")[1]
        prose = body.split("---", 2)[2]
        mid = scalar(fm, "id")
        mods[mid] = {
            "file": os.path.relpath(f, root), "body": body, "fm": fm, "prose": prose,
            "block": scalar(fm, "block"), "title": scalar(fm, "title"),
            "tier": int(scalar(fm, "tier")), "hours": float(scalar(fm, "estimatedHours")),
            "prereq": inline_list(fm, "prerequisites"), "next": inline_list(fm, "nextModules"),
            "concepts": block_list(fm, "concepts"), "objectives": block_list(fm, "objectives"),
            "notation": re.findall(
                r'\{\s*symbol:\s*"((?:[^"\\]|\\.)*)"\s*,\s*meaning:\s*"((?:[^"\\]|\\.)*)"\s*\}', fm),
            "sourceIds": re.findall(r'sourceId:\s*"([^"]+)"', fm),
            "readiness": body.count("<ReadinessCheck"),
            "displayMath": prose.count("$$") // 2,
            "codeFences": len(re.findall(r"^```", prose, re.M)) // 2,
            "pyFences": len(re.findall(r"^```(?:python|py)\b", prose, re.M)),
            "figures": prose.count("<SourceFigure") + len(re.findall(r"^!\[", prose, re.M)),
        }

    # moduleId lives on the file wrapper, not the exercise (the Astro loader injects it).
    q: dict[str, dict] = {}
    for f in glob.glob(p("src/content/questions/*.json")):
        data = json.load(open(f, encoding="utf-8"))
        for e in data["exercises"]:
            e.setdefault("moduleId", data["moduleId"])
            q[e["id"]] = e
    s = {e["exerciseId"]: e for f in glob.glob(p("src/content/solutions/*.json"))
         for e in json.load(open(f, encoding="utf-8"))["solutions"]}
    cards = Counter()
    for f in glob.glob(p("src/content/**/*.mdx"), recursive=True):
        for m in re.finditer(r'<ExerciseCard\s+id="([^"]+)"', open(f, encoding="utf-8").read()):
            cards[m.group(1)] += 1
    by_mod: dict[str, list[dict]] = defaultdict(list)
    for e in q.values():
        by_mod[e["moduleId"]].append(e)

    # ---- inventory invariants (OK = genuine success) --------------------
    expect("INV-01", len(mods) == 69, f"69 modules (found {len(mods)})")
    expect("INV-02", len({m['block'] for m in mods.values()}) == 15,
           f"15 blocks (found {len({m['block'] for m in mods.values()})})")
    total_h = sum(m["hours"] for m in mods.values())
    expect("INV-03", abs(total_h - 226.0) < 1e-9, f"226.0 estimated hours (found {total_h})")
    expect("INV-04", len(glob.glob(p("src/content/cheatsheets/*.mdx"))) == 14, "14 cheat sheets")
    expect("INV-05", len(glob.glob(p("src/content/milestones/*.mdx"))) == 8, "8 milestones")
    pages = len(glob.glob(p("dist/**/index.html"), recursive=True))
    if os.path.isdir(p("dist")):
        expect("INV-06", pages == 100, f"100 built pages (found {pages})")
    else:
        record("INV-06", "QUEUE", "dist/ absent - build not measured this run")
    expect("EX-01", len(q) == len(s) == sum(cards.values()) == 361,
           f"361 questions/solutions/cards (found {len(q)}/{len(s)}/{sum(cards.values())})")
    expect("EX-02", not (set(q) ^ set(s)) and not (set(q) ^ set(cards)),
           "question/solution/card sets identical")
    expect("EX-03", all(len(e.get("hints", [])) == 3 for e in q.values()), "exactly 3 hints per exercise")

    # ---- known defects (REPRO = reproduced, NOT fixed) ------------------
    def route(order):
        r = sorted(mods, key=lambda m: (order.index(mods[m]["block"]), m))
        pos = {m: i for i, m in enumerate(r)}
        return [(m, x) for m in r for x in mods[m]["prereq"] if x in pos and pos[x] > pos[m]]

    v_now, v_new = route(IMPLEMENTED_BLOCK_ORDER), route(PROPOSED_BLOCK_ORDER)
    expect("D-01", v_now == [("OPT-06", "PROB-01"), ("OPT-06", "PROB-05")],
           f"forward prereqs under implemented order = {v_now}", "plan §2.5/§7.2", kind="REPRO")
    expect("D-01b", not v_new, "0 forward prereqs under proposed order (PROB before OPT)", "plan §7.2")
    expect("D-01c", not [(m, x) for m, d in mods.items() if d["block"] == "PROB"
                         for x in d["prereq"] if mods[x]["block"] == "OPT"],
           "no PROB module depends on OPT -> reorder safe", "plan §7.2")

    sym = defaultdict(set)
    for mid, d in mods.items():
        for s_, meaning in d["notation"]:
            sym[s_].add((meaning[:80], mid))
    coll = {k: v for k, v in sym.items() if len({m for m, _ in v}) > 1}
    expect("D-02", len(coll) == 6, f"6 notation collisions: {sorted(coll)}", "plan §2.5/§8.2", kind="REPRO")
    s03 = [x for x in mods["SYM-03"]["notation"] if x[0] == "$c(s,a)$"]
    expect("D-02b", bool(s03) and "symbolic state" in s03[0][1],
           "SYM-03 pairs $c(s,a)$ with a symbolic-state meaning", "plan §17.2", kind="REPRO")

    manifest = {x["source_id"] for x in json.load(open(p("data/source-manifest/manifest.json")))}
    used = set().union(*(set(d["sourceIds"]) for d in mods.values()))
    used |= {e["sourceRef"]["sourceId"] for e in q.values() if e.get("sourceRef")}
    expect("D-03", used - manifest == {"julia-report"},
           f"unmanifested sourceIds = {sorted(used - manifest)}", "plan §2.5/§9.3", kind="REPRO")

    if os.path.exists(p("dist/print/index.html")):
        n = open(p("dist/print/index.html"), encoding="utf-8").read().count("exercise-card")
        claims = "exercises aren't included" in open(p("src/pages/print.astro"), encoding="utf-8").read()
        expect("D-04", claims and n == 367,
               f"print.astro claims exercises excluded; dist/print has {n} exercise-cards",
               "plan §2.5/§14.1", kind="REPRO")
    else:
        record("D-04", "QUEUE", "dist/print absent - not measured this run")

    card_src = open(p("src/components/exercise/ExerciseCard.astro"), encoding="utf-8").read()
    at = Counter(e["answerType"] for e in q.values())
    expect("D-05", "q.options" not in card_src,
           f"mcq/multi-select schema-only (ExerciseCard never renders q.options); in use: {dict(at)}",
           "plan §2.2/§14.1", kind="REPRO")
    expect("D-06", at.get("code", 0) == 1 and "'code'" not in card_src,
           "1 'code' exercise, no code branch in ExerciseCard", "plan §2.2/§14.1", kind="REPRO")
    expect("D-07", "data-full-solution" in card_src,
           "full solution embedded in HTML -> lock is UI-only", "plan §2.2/§14.1", kind="REPRO")
    cfg = open(p("src/content.config.ts"), encoding="utf-8").read()
    expect("D-08", "z } from 'astro:content'" in cfg,
           "content.config.ts imports z from 'astro:content' (deprecated) -> 103 ts(6385) hints; "
           "fix: 'astro:schema'", "plan §2.7/§14.2", kind="REPRO")

    ms = {}
    for f in glob.glob(p("src/content/milestones/*.mdx")):
        fm = frontmatter(f)
        ms[scalar(fm, "id")] = {"covers": inline_list(fm, "coversModules"),
                                "remediates": " ".join(re.findall(r"moduleIds:\s*\[([^\]]*)\]", fm))}
    order = {b: i for i, b in enumerate(PROPOSED_BLOCK_ORDER)}
    bad = [(k, c) for k, d in ms.items() if k.split("-")[0] in order
           for c in d["covers"] if c in mods and order[mods[c]["block"]] > order[k.split("-")[0]]]
    expect("MS-01", not bad, f"milestone coversModules ordering violations = {bad or 'none'}")

    pms = {m for m, d in mods.items() if d["block"] in ("PLAN", "MANIP", "SYM")}
    block_cov = set().union(*(set(d["covers"]) for k, d in ms.items() if k != "CUMULATIVE-FINAL"))
    final_cov = set(ms.get("CUMULATIVE-FINAL", {}).get("covers", []))
    expect("MS-02", not (pms & block_cov),
           f"no block milestone covers any of the {len(pms)} PLAN/MANIP/SYM modules; only "
           f"{sorted(pms & final_cov)} appear anywhere (cumulative final only)",
           "plan §17.3", kind="REPRO")
    manip = {m for m, d in mods.items() if d["block"] == "MANIP"}
    expect("MS-03", not (manip & (block_cov | final_cov)),
           f"{sorted(manip)} appear in NO milestone at all", "plan §17.3", kind="REPRO")
    expect("MS-04", "KIN" in " ".join(ms["DYN-EXAM"]["covers"]) and "KIN" not in ms["DYN-EXAM"]["remediates"],
           "DYN-EXAM covers KIN-01/02/03 but its remediationMap has no KIN entry",
           "review KIN02-09 / plan §17.3", kind="REPRO")

    # ---- QUEUE: measurements for semantic review, never gates -----------
    ready_gap = [(m, len(d["prereq"]), d["readiness"]) for m, d in sorted(mods.items())
                 if d["prereq"] and d["readiness"] < len(d["prereq"])]
    record("QUEUE-READINESS", "QUEUE",
           f"{len(ready_gap)}/{len([1 for d in mods.values() if d['prereq']])} modules have fewer "
           f"<ReadinessCheck> widgets than declared prerequisite IDs. NOT a defect count: one check "
           f"may legitimately cover several prerequisites. Review queue for semantic adequacy only.",
           "review COV-G03")
    no_cards = sum(1 for e in q.values() if not e.get("reviewCardIds"))
    record("QUEUE-ANKI-EXPORT", "QUEUE",
           f"{no_cards}/{len(q)} exercises ({100*no_cards//len(q)}%) have no reviewCardIds. Measures "
           f"exercise->Anki EXPORT sparsity only; says nothing about total recall quality (notation "
           f"cards and in-module retrieval prompts are separate surfaces).", "review COV-G04")
    fullnote = sorted(m for m, d in mods.items() if "full note" in d["fm"])
    record("QUEUE-COVERAGE-CLAIM", "QUEUE",
           f"modules asserting 'full note' coverage: {fullnote}. KIN-02 is a confirmed overclaim "
           f"(review); DYN-05 is UNAUDITED - to check, not yet a finding.", "review COV-G02")
    record("QUEUE-NOTATION-EMPTY", "QUEUE",
           f"modules declaring zero notation: {sorted(m for m, d in mods.items() if not d['notation'])}")

    # ---- concept / depth inventory --------------------------------------
    def depth_of(mid: str, d: dict) -> tuple[int, str]:
        ex = by_mod.get(mid, [])
        has_ex = bool(ex)
        derived = d["displayMath"] >= 3 or any(e["answerType"] in ("derivation", "proof") for e in ex)
        # Depth >=5 requires a RUNNABLE artifact. No labs/ tree exists and the single
        # `code` exercise has no runner (D-06), so nothing in this corpus can reach 5.
        runnable = os.path.isdir(p("labs")) and d["pyFences"] > 0
        if runnable:
            return 5, "runnable artifact present"
        if has_ex and derived:
            return 4, (f"{len(ex)} exercises with solutions; {d['displayMath']} display-math blocks; "
                       f"{sum(1 for e in ex if e['answerType'] in ('derivation', 'proof'))} derivation/proof")
        if has_ex:
            return 4, f"{len(ex)} exercises with solutions"
        if derived:
            return 3, f"{d['displayMath']} display-math blocks, no exercises"
        return 2, "prose only"

    inv_modules = {}
    for mid, d in sorted(mods.items()):
        depth, basis = depth_of(mid, d)
        ex = by_mod.get(mid, [])
        inv_modules[mid] = {
            "block": d["block"], "title": d["title"], "tier": d["tier"], "hours": d["hours"],
            "file": d["file"], "prerequisites": d["prereq"], "nextModules": d["next"],
            "objectives": d["objectives"],
            "concepts": [{"name": c, "moduleDepth": depth,
                          "perConceptDepth": None,
                          "perConceptDepthReason":
                              "requires semantic module review (review protocol Gate 6); "
                              "not mechanically derivable"} for c in d["concepts"]],
            "moduleDepth": {
                "value": depth, "label": DEPTH_LABELS[depth], "basis": basis,
                "ceilingNote": "Mechanically-derived CEILING for the module as a whole. Individual "
                               "concepts inside it may sit lower; none can sit higher.",
            },
            "evidence": {
                "exercises": len(ex),
                "exercisesByType": dict(Counter(e["answerType"] for e in ex)),
                "displayMathBlocks": d["displayMath"], "codeFences": d["codeFences"],
                "pythonFences": d["pyFences"], "figures": d["figures"],
                "readinessChecks": d["readiness"], "notationEntries": len(d["notation"]),
                "sourceIds": sorted(set(d["sourceIds"])),
            },
        }

    depth_hist = Counter(v["moduleDepth"]["value"] for v in inv_modules.values())
    expect("DEPTH-01", max(depth_hist) <= 4,
           f"module depth ceiling across all 69 modules = {max(depth_hist)} "
           f"({DEPTH_LABELS[max(depth_hist)]}); distribution {dict(sorted(depth_hist.items()))}. "
           f"Nothing reaches 5 (executable) -- quantifies the plan's core 4->5 thesis.",
           "plan §3", kind="REPRO")

    concepts_total = sum(len(v["concepts"]) for v in inv_modules.values())
    record("DEPTH-02", "OK" if all(mods[m]["concepts"] for m in mods) else "FAIL",
           f"{concepts_total} declared concepts across {len(mods)} modules; "
           f"{sum(1 for m in mods if not mods[m]['concepts'])} modules declare none")

    artifact = {
        "$schema": "gate-a-concept-depth-inventory/1",
        "generatedBy": "scripts/validate/gate_a_baseline.py",
        "treePath": root, "commit": commit, "treeState": tree_kind, "label": label,
        "depthScale": DEPTH_LABELS,
        "scopeAndLimits": {
            "moduleDepth": "COMPLETE for all 69 modules. Mechanically derived from committed "
                           "evidence (exercise counts/types, display math, code fences, presence of "
                           "a labs/ tree). It is a CEILING, not a semantic judgment.",
            "perConceptDepth": "DELIBERATELY NULL. Judging each of the "
                               f"{concepts_total} concepts individually requires reading the module "
                               "against its source; that is the review protocol's job (Gate 6), not "
                               "this reporter's. Nulls are placeholders the review fills in.",
            "conceptSource": "Declared concepts[] frontmatter. Undeclared concepts a module teaches "
                             "in passing are not captured.",
        },
        "summary": {"modules": len(mods), "hours": total_h, "concepts": concepts_total,
                    "moduleDepthHistogram": {str(k): v for k, v in sorted(depth_hist.items())},
                    "exercisesByType": dict(at)},
        "notationCollisions": {k: sorted(v) for k, v in sorted(coll.items())},
        "modules": inv_modules,
    }

    out = os.path.abspath(args.out) if args.out else p("docs/plans/gate-a-concept-depth-inventory.json")
    if not args.no_write:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(artifact, fh, indent=2, ensure_ascii=False)
        digest = hashlib.sha256(open(out, "rb").read()).hexdigest()
    else:
        digest = hashlib.sha256(json.dumps(artifact, indent=2, ensure_ascii=False).encode()).hexdigest()

    # ---- report ----------------------------------------------------------
    w = max(len(c) for c, _, _, _ in results)
    for cid, status, detail, owner in results:
        print(f"{cid:<{w}}  {status:<5}  {detail}" + (f"   [{owner}]" if owner else ""))
    counts = Counter(r[1] for r in results)
    print(f"\n{len(results)} checks: " + ", ".join(f"{counts[k]} {k}" for k in ("OK", "REPRO", "QUEUE", "FAIL") if counts[k]))
    print("  OK    = invariant holds")
    print("  REPRO = known defect reproduced (evidence, NOT success, NOT fixed)")
    print("  QUEUE = measurement for semantic review; never a pass/fail verdict")
    print(f"\ninventory {'written to' if not args.no_write else '(not written; --no-write)'}: {out}")
    print(f"sha256: {digest}")
    if counts["FAIL"]:
        print("\nFAIL — expectations that did not reproduce:", file=sys.stderr)
        for cid, status, detail, _ in results:
            if status == "FAIL":
                print(f"  {cid}: {detail}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
