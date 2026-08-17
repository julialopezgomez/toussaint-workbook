# Independent adversarial structural audit — Phase 5 plan 3.5 / Gate B proposal 6

Date: 2026-08-15  
Reviewer role: fresh independent adversarial structural pass  
Scope: C1–C4, C9, STR-01, STR-02, totals/classification/gate order/Gate-A invariance, and validator mutation resistance  
Write boundary: this report is the only repository write; all governing artifacts were inspected read-only  
External-source boundary: no external source verification was performed

## Overall verdict

**STRUCTURAL FAIL.** Current plan/proposal bytes fail C1, C2, and C4. C9 also fails because the
validator still accepts a scored-row status that disagrees with the status roll-up. A second
validator false negative leaves the stated six-component F8 hour check unenforced. Gate B remains
unstarted and unapproved; this report approves nothing and authorizes no next gate.

## Verdict ledger

| Audit item | Verdict | Basis |
|---|---|---|
| C1 — current revision/status/supersession consistency | **FAIL** | Proposal header says revision 6, but its live numbering note says the proposal revision is “currently 5”; the passing status validator does not parse that syntax |
| C2 — F0/F8 ownership, KIN-02 reconciliation, hour policy | **FAIL** | Plan/ledger ownership is corrected, but the approved/reconciled KIN-02 record still assigns keyed recall to F0 and pins plan 2.2; the validator also ignores the sixth F8 hour component |
| C3 — disposable Gate-E fixtures | **PASS** | Every Gate-E pilot is scratch-only, non-content, non-committed, and deleted/quarantined; P1 creates its own fixture and has no paused-prototype dependency |
| C4 — Gate-B evaluation/planning-only authority, including taxonomy wording | **FAIL** | Core boundary prose is corrected, but proposal §7 O1 still says approving A1/A4 “approves citation,” and plan §9.9 says `CONDITIONAL` sources “cannot be scored honestly” although all nine are scored |
| C9 — assessment IDs and validator derivation | **FAIL** | Current IDs and F8 batches are correct and most mutations are caught, but changing a scored row’s decision from `SELECT` to `OPTIONAL` exits 0 |
| STR-01 — `OPT-05B` dependencies | **PASS** | KKT dependency belongs only to `OPT-04B`; `OPT-05B` uses `OPT-05`, `PROB-02`, `NUM-01` |
| STR-02 — notation migration | **PASS** | Five existing modules are named and evidenced; SYM-02 replacement remains explicitly unresolved at Gate C because `σ` is occupied |
| Scored-matrix ID set versus roll-up union | **PASS** for current bytes | 39 scored IDs equal 23 SELECT + 7 OPTIONAL + 9 CONDITIONAL; D3 is now a scored row |
| Scored-row status versus roll-up status | **FAIL** | Current bytes agree, but the validator does not compare each matrix row’s decision with its roll-up bucket |
| Totals and classification | **PASS** for current bytes | 105 modules, 20 blocks, 368.0 h, 347.5 main / 20.5 optional, +36 modules / +142.0 h |
| Gate order and prerequisite order | **PASS** | Gate A→B→C→D→E→F→G and F0→F1→F0b→F2…F8 are coherent; semantic prerequisite mutation is caught |
| Gate-A invariance | **PASS** | Approved evidence is byte-identical at the approved full SHA-256 and relevant decisions are clean |
| C5–C8 external-source claims | **UNVERIFIED / DEFERRED** | Explicitly excluded; no external page, licence, version, or source payload was checked |
| `deits-tedrake-iris`, `marcucci-gcs` | **UNVERIFIED / DEFERRED** | Not fetched; proposal itself records unpinned locators |
| Underactuated appendix titles | **UNVERIFIED / DEFERRED** | Titles were not checked; structural dispositions do not depend on them |

## Audited repository state and identities

The audit assessed the current worktree bytes, not producer claims and not an imagined clean tree.
Repository `HEAD` is `e8e75e5a58964417272df2b70ac5bbbc4bcad363`. The authoritative Phase-4
content baseline is the older ancestor `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`.

The pre-report worktree was dirty:

```text
 M PROJECT_STATE.md
 M data/curriculum/ARCHITECTURE.md
 M data/curriculum/CURRICULUM.md
 M docs/agent/CURRENT_HANDOFF.md
 M docs/plans/PHASE5_AUGMENTATION_PLAN.md
 M package-lock.json
 M package.json
 M src/content/course/KIN/KIN-01.mdx
?? docs/plans/GATE_B_SOURCE_SELECTION.md
?? docs/plans/phase5-planning-ledger.json
?? docs/review/planning/
?? scripts/validate/phase5_plan_consistency.py
?? src/components/interactive/
?? tmp/
```

The modified/untracked planning artifacts are therefore worktree proposals. Gate-A evidence,
decisions 0005–0007, and `docs/review/modules/KIN-02.md` were tracked and clean before this report.
All unrelated dirty paths remain user-owned and untouched. This report adds only
`docs/review/planning/PLAN_3_5_STRUCTURAL_AUDIT.md`.

Full SHA-256 identities at audit start:

| Artifact | SHA-256 |
|---|---|
| `docs/plans/PHASE5_AUGMENTATION_PLAN.md` | `2244799929b8a11ac3357ccdc2003c6f4181261643d0a325a74618c3734b60b5` |
| `docs/plans/GATE_B_SOURCE_SELECTION.md` | `bafa41ee446a9f1733cebf3142916a6d0b8c9f8c8b8cd0f3d72c7eaee38bd89e` |
| `docs/plans/phase5-planning-ledger.json` | `47d341cf0cda8b9df5ea291766a2ad1794aa2201e1e1356b568724f3b3f0a9bf` |
| `scripts/validate/phase5_plan_consistency.py` | `9e141ecde91a68d312fa06cfd24e901c7a9557ffdcce407617a59b7b63c19e` |
| `docs/agent/CURRENT_HANDOFF.md` | `2ce46001814b6bdda7793515936bad44fa444746755f10fe02bd7c6aa035038b` |
| `docs/plans/GATE_A_BASELINE.md` | `470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4` |
| `docs/review/modules/KIN-02.md` | `34a4c108aeec1546875d4d39ab735147d7113db66378c869013dcc30fd3bd259` |
| `docs/review/planning/PLAN_3_3_STRUCTURAL_AUDIT.md` | `6c6d0164ec296740db2c377259f08afcf1d41d3ffb2d816a229b3ef051b64b7c` |
| `docs/decisions/0005-gate-a-approved.md` | `2078d528e8add9b01aac12f05cc69fd424f6bdd300791ab0a95d65fe1a4a7dcf` |
| `docs/decisions/0006-math-review-approved.md` | `7d93931650f91332eac8f903f50cb36c1958b8ef254ed682006d041106b83b07` |
| `docs/decisions/0007-opt-review-approved.md` | `b132d889e04f612d9375f1dc9075f195a2d31c88139b8417a716cc6bffe27ad8` |
| `data/source-manifest/manifest.json` | `ef009f1481cd1d5379c20db4feab7156d43443dc38fc58e0046c119e78f36960` |

Authority derived from repository evidence:

- Decision 0005 `:7-24,41-49` approves Gate A only, closes it, and leaves Gate B unapproved and
  unbegun.
- Decisions 0006 `:60-68,73-75` and 0007 `:59-67,83-86` approve MATH/OPT findings and planned
  deltas; neither approves the production corpus or authoring.
- No Gate-B approval decision exists under `docs/decisions/`.
- Plan revision 3.5 and proposal revision 6 are the current proposed bytes by their headers and
  cross-file SHA pin, but neither is approved.

## Severity-ranked findings

### 1. HIGH — C1-01: live proposal revision contradiction missed by the status validator

`GATE_B_SOURCE_SELECTION.md:3-4` declares **proposal revision 6**, current/unreviewed. The live
numbering note at `:8-10` instead says the proposal revision number is **“currently 5”**, then says
revision 6 is pinned to plan 3.5. This is not labelled historical text.

Plan `PHASE5_AUGMENTATION_PLAN.md:6,1148,1587,1790`, ledger
`phase5-planning-ledger.json:6,1470-1474`, and handoff `:8-27` otherwise identify proposal 6 as
current, proposal 5 as superseded-before-review, and proposals 1–4 as failed. The proposal's own
two statements therefore disagree.

The validator nevertheless exits 0. Its revision-token regex at
`phase5_plan_consistency.py:257-262` requires `proposal revision` to be followed immediately by a
number. It does not parse `proposal revision number (currently 5)`, even though that sentence lies
inside the proposal-header region described at `:324-330`. This invalidates the claimed all-region
current-status consistency.

### 2. HIGH — C2-01: approved KIN-02 reconciliation still gives keyed recall to F0

The review record is live and approved/reconciled at `docs/review/modules/KIN-02.md:1-5`. Its Phase-5
reconciliation still pins plan revision 2.2 at `:141-143`; `:147` says keyed recall for
KIN02-01/03/04 becomes a Gate-F0 repair; `:152` says F0 rewrites KIN02-08 as direct keyed recall and
names the convention targets.

That conflicts with current plan `PHASE5_AUGMENTATION_PLAN.md:376-390,1851-1864,1644-1655`:

- F0 teaches/fixes the quaternion content and replaces the wrong sigmoid analogy with a correct
  quaternion prompt.
- F8 keys that prompt and owns every added recall item.
- KIN02-09's missing existing DYN-exam remediation mapping is the only F0 assessment item; F8 only
  persistence-checks it.

The decisions support the plan-side split: whole-block MATH/OPT recall is F8 in decisions 0006
`:44,64` and 0007 `:45,64,86`. The contradiction is cross-record and remains blocking.

### 3. HIGH — C4-02: a current proposal row still grants citation authority at Gate B

The main boundary is clear and correct in plan `:1169-1188,1219,1241-1249,1251-1268,1586-1598`
and proposal `:19,140-146,1981-2005`: Gate B evaluates and records planning decisions; it does not
acquire, populate, ingest, cite in production content, or author.

But proposal §7 O1 at `GATE_B_SOURCE_SELECTION.md:1941-1944` says: approving A1/A4
**“approves citation, not copying.”** That is current open-item text, not correction history. It
contradicts plan `:1219` (“no Gate-B approval ... authorizes ... citation in production content”) and
proposal `:19,1983`. A reuse classification may make a source *eligible* for later citation, but Gate
B may not itself approve the citation action under this plan's stated boundary.

The taxonomy also contradicts its own scored contract: plan `:1079-1090` and proposal `:127-146`
require every eligible candidate, including `CONDITIONAL`, to be scored before status assignment;
all nine conditional candidates have scored rows. Plan `:1217` nevertheless says a conditional
source **“cannot be scored honestly.”** The intended meaning appears to be “cannot be approved,” but
the written taxonomy says something the proposal structurally disproves.

### 4. HIGH — C9-04: scored-row decision is not compared with roll-up membership

Current bytes are aligned: proposal `:150-229` has 39 scored rows and `:270-283` rolls up exactly the
same 39 IDs as 23 SELECT, 7 OPTIONAL, 9 CONDITIONAL. D3 is now a scored row at `:202-214`.

However, validator `:1147-1176` only checks that each scored decision cell names exactly one allowed
status. Validator `:1178-1235` compares the **roll-up lists** with ledger membership and compares the
scored-ID set with the roll-up union; it never records the status parsed from each scored row and
never compares that status to its roll-up bucket.

An isolated mutation changed A1's scored-row decision from `SELECT` to `OPTIONAL`, leaving the
ledger and roll-up unchanged and re-pinning the proposal hash in the fixture handoff. The validator
exited 0 with zero warnings. This directly falsifies proposal `:283`'s claim that a matrix status
disagreeing with the roll-up fails the check.

### 5. MEDIUM — C2-02: the stated six-component F8 hour check is not implemented

The current policy itself is explicit and internally consistent:

- plan `:683-702`: F8 keyed recall contributes 0.0 scheduled learner hours;
- ledger `:26-38,1486-1506`: policy, scope, batch F8, and six-component decomposition;
- ledger `:970-990`: published `f8KeyedRecallHours: 0.0`.

But plan `:700` claims `phase5_plan_consistency.py` checks the six-component enumeration. It does
not. Validator `:480-493` recomputes `added_hours` from only five components; `:553-569` checks only
those five and never reads `f8KeyedRecall`, `addedHoursComponents`, or
`published.f8KeyedRecallHours`.

An isolated fixture changed all three ledger F8 values from 0.0 to 2.0 and changed the component
total from 142.0 to 144.0, leaving the policy text and published overall `addedHours` at 142.0. The
validator exited 0 with zero warnings. Thus the current numbers are arithmetically sound, but the
claimed enforcement and future-drift resistance are false.

## Re-audit details

### C3 — PASS

Plan `PHASE5_AUGMENTATION_PLAN.md:567-589` pauses `RotationViz` and `GridWorldRL` and forbids any
gate/pilot dependency on them. Gate D uses a disposable fixture at `:1600-1609`. Gate E's binding
rule at `:1611-1618` excludes pilot artifacts from content, routing, assessment, Anki, totals, and
commits and requires deletion/quarantine. P1 at `:1619-1622` creates its own scratch fixture, does
not read/import/reactivate either prototype or KIN-01, and deletes the fixture at exit. P2–P5 are
likewise throwaway artifacts at `:1622-1629`. No current dependency on a paused prototype was found.

### STR-01 — PASS

Plan `:527-541` gives `OPT-04B` prerequisites `OPT-03`, `OPT-04`, `NUM-03` and the repaired KKT
condition; `OPT-05B` has `OPT-05`, `PROB-02`, `NUM-01` and explicitly no KKT dependency. Gate-F order
and rationale at `:1638-1646` match. The ledger entries for `OPT-04B` and `OPT-05B` agree. Decision
0007 `:34-38` distinguishes the KKT/IFT module from derivative-free optimization.

### STR-02 — PASS

Plan `:941-980` and ledger `:1508-1547` name five existing-module migrations:

1. `DYN-04`: `R→R_u`, `Q→Q_x` — baseline `:76,80,82,88,120`;
2. `DYN-06`: the same — baseline `:117,121,123,125`;
3. `OPT-05`: `L→L_∇` — baseline `:24,91,93`;
4. `ODE-01`: the quoted `L→L_∇` — baseline `:118`;
5. `SYM-02`: substitution `θ` renamed to an as-yet-unselected symbol — baseline `:21,61,71,87,95,102`.

Plan `:955-976,1594-1598` correctly leaves the SYM-02 replacement for Gate C because `σ` already
has six baseline meanings. No notation rename is authorized by this audit.

### Totals, route classification, and gate order — PASS for current bytes

Independent ledger sums:

- new modules: 36, 120.5 h; 31 main-route and 5 optional, with the optional new modules totalling
  15.0 h;
- foundation additions 9.0 h; in-place additions 9.5 h; calibration repairs 1.5 h; rescopes 1.5 h;
  F8 recall 0.0 h;
- added total: `120.5 + 9.0 + 9.5 + 1.5 + 1.5 + 0.0 = 142.0 h`;
- baseline: 69 modules, 15 blocks, 226.0 h; augmented: 105 modules, 20 blocks, 368.0 h;
- optional: 15.0 h new optional modules + 4.5 h existing Tier-3 modules + 1.0 h optional reference
  boxes = 20.5 h; main route `368.0 − 20.5 = 347.5 h`.

These values match ledger `:970-990`, plan §5.1 `:592-638`, and the validator's independent
frontmatter/table recomputation. The current five planned exams and five planned cheat sheets are
enumerated at plan `:657-675`, ledger assessment inventory, and all ten are assigned F8. Existing
frontmatter IDs are 8 exams and 14 cheat sheets with no filename/id divergence.

The plan's gate order at `:1576-1680` is A→B→C→D→E→F→G; Gate F is
F0→F1→F0b→F2→F3→F4→F5→F6→F7→F8. `NUM-03` is therefore available before `OPT-04B`; no main-route
new module depends on an optional module.

### Gate-A invariance — PASS

Gate-A evidence hashes to the approved
`470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4`. `git diff --exit-code` is
clean for `GATE_A_BASELINE.md` and decisions 0005–0007. Decision 0005 `:7-24` closes Gate A and
preserves the separate dirty-worktree comparison. Baseline commit
`dd2e8717f82dfcb77aff4b8c89aba258997f87fe` is an ancestor of current HEAD. Nothing in this audit
reopens or repeats Gate A.

## Disposable mutation matrix

Fixtures were independent copies under `/private/tmp/phase5-structural-audit-35.Y1OZoE/`. For every
plan/proposal mutation, dependent full hashes were re-pinned in the fixture proposal/handoff before
running the validator. No result below is a generic plan/proposal hash mismatch.

| Mutation | Expected semantic result | Actual result | Verdict |
|---|---|---|---|
| Current Gate-B section calls failed proposal 4 the current unreviewed proposal | C1 current/failed/cross-region diagnostic | Exact C1 semantic failure; 0 hash failures | **PASS** |
| Plan §5.3 `ACC-EXAM→FAKE-EXAM` | planned-ID disagreement | Exact ledger-only / plan-only ID diagnostic | **PASS** |
| Ledger `ACC-EXAM` batch `F8→F0` | wrong F8 batch | `new exams must be produced in F8 ... ACC-EXAM=F0` | **PASS** |
| `MATH-EXAM.mdx` frontmatter ID diverges from filename | frontmatter and filename drift | Both explicit semantic diagnostics | **PASS** |
| Coverage `UA ch.2→UA ch.1` with row count preserved | duplicate plus missing required unit | Exact duplicate `ua ch.1` and missing `UA ch.2` diagnostics | **PASS** |
| Swap A1/A9 between SELECT/OPTIONAL roll-up lists with counts preserved | roll-up membership drift | Exact SELECT and OPTIONAL membership differences | **PASS** |
| Change A1 scored-row decision SELECT→OPTIONAL only | matrix-row status versus roll-up mismatch | Exit 0, 0 warnings | **FAIL** |
| Add unscored `Z9` to roll-up; keep roll-up/ledger counts internally consistent | roll-up-only ID | Exact `NO scored row`, `Z9×0`, and 39-vs-40 diagnostics | **PASS** |
| Omit scored A1 from every roll-up; keep roll-up/ledger counts internally consistent | scored-only ID | Exact `absent from every ... status list`, `A1×0`, and 39-vs-38 diagnostics | **PASS** |
| `NUM-01` depends on later `NUM-03` | semantic prerequisite violation | Exact canonical positions `NUM-01 (8) <- NUM-03 (10)` | **PASS** |
| Plan §5.1 NUM hours `8.0→8.5` | cell-level table mismatch | Exact NUM 8.5-vs-8.0 diagnostic | **PASS** |
| F8 recall component/published/component-total `0→2`, `142→144` while policy/overall stay 0/142 | six-component hour inconsistency | Exit 0, 0 warnings | **FAIL** |

The fixture tree was isolated from the repository and contained no governing-file write.

## Validator runs

Initial runs against the audited bytes:

- `python3 scripts/validate/agent_context.py`: exit 0; 0 failures, 0 warnings.
- `python3 scripts/validate/review_integrity.py`: exit 0; 0 failures, 0 warnings.
- `python3 scripts/validate/phase5_plan_consistency.py`: exit 0; 0 failures, 0 warnings.

Those clean summaries are not semantic approval. In particular, the live proposal-5 status phrase,
scored-row status mutation, and F8-hour mutation demonstrate three false negatives.

Final runs after this report was written are recorded as exit 0 with 0 failures and 0 warnings for
the same three validators. No curriculum build was run because no curriculum/runtime artifact was
changed and a build cannot falsify these structural findings.

## Deferred work and stop state

- C5–C8, all external source facts/scores, `deits-tedrake-iris`, `marcucci-gcs`, and Underactuated
  appendix titles remain **UNVERIFIED**.
- No source was fetched, acquired, pinned, ingested, or externally checked.
- No governing file was repaired; no approval was recorded or requested; Gate B was not begun.
- No commit or push was performed.

Final verdict: **STRUCTURAL FAIL**.
