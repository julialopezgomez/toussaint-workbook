# Independent adversarial structural audit — Phase 5 plan 3.7 / Gate B proposal 8

Date: 2026-08-16  
Reviewer role: fresh independent adversarial structural pass  
Scope: C1-01, C1-02, C2-01, C2-02, C2-03, C4-02, C4-03, C9-04,
STR-01, STR-02, totals, gate/prerequisite order, Gate-A invariance, audit/handoff
freshness, and validator mutation resistance  
Write boundary: this report is the only review artifact created; the candidate plan,
proposal, ledger, validator, curriculum, sources, decisions and runtime code were read-only  
External-source boundary: C5–C8 and other deferred external facts were not verified

## Overall verdict

**STRUCTURAL FAIL.** Plan 3.7 / proposal 8 closes C1-01 and all three C2 items in
the current bytes, and the 39-source status matrix now survives exhaustive independent
membership mutations. It nevertheless has two HIGH and two MEDIUM structural findings:

1. the C1-02 repair still ignores two of the eight governing status booleans and the
   separate blocked-correction state;
2. C4-02's corrected live wording is not semantically enforced, so restoring Gate-B
   citation authority still exits 0;
3. C4-03 remains live for Menagerie D3, whose conditional blocker resolution is bundled
   with `sources.json` population, and the validator still omits the proposal §3.3 sibling;
4. STR-02 is contradicted by two live proposal rows that call `σ` the already-renamed
   `SYM-02` substitution while the plan and ledger leave that replacement unsettled for
   Gate C.

Gate B and Group A remain unstarted and unapproved. This report approves nothing and
authorizes no approval request, source action, next gate or authoring.

## Verdict ledger

| Audit item | Verdict | Basis |
|---|---|---|
| C1-01 — detached proposal numbering | **PASS** | Header and live numbering note both say proposal 8; isolated `8→5` note mutation failed semantically |
| C1-02 — status facts drive every live region | **FAIL (HIGH)** | Six of eight booleans are enforced; `groupAStarted` and `currentProposalApproved` mutations exit 0, and `blockedCorrection: null→C2-01` also exits 0 |
| C2-01 — F0/F8 ownership | **PASS** | KIN-02 reconciliation, plan and ledger agree; F0 owns content/error correction, F8 owns keying and added recall, F8 adds 0.0 learner hours |
| C2-02 — six-component hour contract | **PASS** | All six components are derived and cross-tied; isolated F8 `0→2` mutation fails semantically |
| C2-03 — human-facing exact decomposition | **PASS** | Plan §5.1 lists all six rows including keyed recall at 0.0 h; removing the zero row's keyed-recall identity fails semantically |
| C4-02 — Gate-B authority boundary | **FAIL (HIGH)** | Current O1 wording is correct, but an isolated mutation restoring “approval approves citation” exits 0 after the proposal hash is re-pinned |
| C4-03 — conditional resolution lifecycle | **FAIL (MEDIUM)** | E9/E10 cited cells are corrected, but D3 still combines its licence read with `sources.json` population; a §3.3-only `at acquisition` regression also exits 0 |
| C9-04 — scored-row/status membership | **PASS** | 39 unique scored rows = 23 SELECT + 7 OPTIONAL + 9 CONDITIONAL; all 39 ledger-membership moves and all 39 row-decision moves fail semantically |
| STR-01 — `OPT-05B` dependencies | **PASS** | `OPT-04B` owns repaired KKT + `NUM-03`; `OPT-05B` consistently depends on `OPT-05`, `PROB-02`, `NUM-01` and not KKT |
| STR-02 — notation migration | **FAIL (MEDIUM)** | Five-module migration is correctly enumerated, but proposal §§4 and 6.6 call `σ` the renamed `SYM-02` substitution, contradicting the plan/ledger's `UNSETTLED` Gate-C decision |
| Totals and route classification | **PASS** | Independent recount: 105 modules, 20 blocks, 368.0 h, 347.5 main / 20.5 optional, +36 modules / +142.0 h |
| Gate and prerequisite order | **PASS** | A→B→C→D→E→F→G; F0→F1→F0b→F2…F8; all 36 proposed prerequisite sets resolve and precede their modules; no main route depends on optional |
| Gate-A invariance | **PASS** | Approved report hash is unchanged; decisions 0005–0007 are clean; baseline commit remains an ancestor of HEAD |
| Audit/handoff freshness at audit start | **PASS** | Three prior audit reports parse, match exact pins, target older candidates, and the handoff pins the latest pre-existing audit; a fully recorded current-audit fixture with `reviewed=false` fails semantically |
| C5–C8 and deferred external facts | **UNVERIFIED / DEFERRED** | No external page, licence, source payload, version, cadence or appendix title was checked |

## Audited repository state and identities

Stage 1 was performed before substantive work: `CURRENT_HANDOFF.md` was read and
compared with the live worktree and newest audit, `git status --short` and relevant diffs
were inspected, and `agent_context.py` passed with zero failures and zero warnings.

The audit assessed current worktree bytes at repository `HEAD`
`e8e75e5a58964417272df2b70ac5bbbc4bcad363`; committed Phase-4 baseline
`dd2e8717f82dfcb77aff4b8c89aba258997f87fe` remains its ancestor.

The pre-report worktree was dirty:

```text
 M PROJECT_STATE.md
 M data/curriculum/ARCHITECTURE.md
 M data/curriculum/CURRICULUM.md
 M docs/agent/CURRENT_HANDOFF.md
 M docs/plans/PHASE5_AUGMENTATION_PLAN.md
 M docs/review/modules/KIN-02.md
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

The plan/proposal/ledger/validator/handoff/KIN-02 and prior audit files were pre-existing
candidate/review work. Other dirty paths are user-owned. No existing dirty file was
modified during the evidence pass.

Full SHA-256 identities at audit start:

| Artifact | SHA-256 |
|---|---|
| `docs/plans/PHASE5_AUGMENTATION_PLAN.md` | `e298acfac750f378d0557f69233f8f8d0094eaaf0f37fb1d3f8f2de86ea149ea` |
| `docs/plans/GATE_B_SOURCE_SELECTION.md` | `f79edcb28bda7ab86603831cd532b5ea16b3acec013b9a4c9a40e5aafc8e190e` |
| `docs/plans/phase5-planning-ledger.json` | `dfe8210fb0f28b27bc4ee6b7716a3980559ab4dc34d17f4e66853f466d58dae3` |
| `scripts/validate/phase5_plan_consistency.py` | `00eef4acc1a317bd15ccd5948824f456f6369dc2f98e9f707cf7f1fbe6cd9f9a` |
| `docs/plans/GATE_A_BASELINE.md` | `470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4` |
| `docs/review/modules/KIN-02.md` | `4f1eadfe0e3259bb4755146aef8a35acbdaa941efd6189ab23f229e9e276c0b1` |
| `docs/review/planning/PLAN_3_3_STRUCTURAL_AUDIT.md` | `6c6d0164ec296740db2c377259f08afcf1d41d3ffb2d816a229b3ef051b64b7c` |
| `docs/review/planning/PLAN_3_5_STRUCTURAL_AUDIT.md` | `3f3cd468e56ddedb69a29cd0e6d92ab81b7364a8ca63f686a400cc76f1d31a4e` |
| `docs/review/planning/PLAN_3_6_STRUCTURAL_AUDIT.md` | `a42cb26edc93219a0c82c8e5abc84878cb7ded0530528a2d7c518bd84d694b89` |
| `docs/decisions/0005-gate-a-approved.md` | `2078d528e8add9b01aac12f05cc69fd424f6bdd300791ab0a95d65fe1a4a7dcf` |
| `docs/decisions/0006-math-review-approved.md` | `7d93931650f91332eac8f903f50cb36c1958b8ef254ed682006d041106b83b07` |
| `docs/decisions/0007-opt-review-approved.md` | `b132d889e04f612d9375f1dc9075f195a2d31c88139b8417a716cc6bffe27ad8` |
| `data/source-manifest/manifest.json` | `ef009f1481cd1d5379c20db4feab7156d43443dc38fc58e0046c119e78f36960` |

No Gate-B approval decision exists. Decision 0005 closes Gate A but explicitly withholds
production-corpus and authoring authority. Decisions 0006/0007 approve review findings and
planned deltas, not current coverage, corpus selection or implementation.

## Severity-ranked findings

### 1. HIGH — C1-02 remains incomplete: three recorded status fields are not binding

The ledger calls `currentGateBStatus.facts` the single recorded fact set. It contains eight
booleans at ledger `:1651-1659`, including `groupAStarted: false` and
`currentProposalApproved: false`, plus the paired correction fields
`resolvedCorrection: "C2-01"` and `blockedCorrection: null` at `:1660-1661`.

The six region definitions require only six booleans and `resolvedCorrection`
(`:1664-1751`). Neither `groupAStarted` nor `currentProposalApproved` appears in
`mustAssertFacts` or `factAssertions`. `blockedCorrection` is printed by
`render_status_summary()` (`phase5_plan_consistency.py:414-417`) but is likewise not
compared with any region or with `resolvedCorrection`.

Independent ledger-only mutations produced:

| Mutation | Exit | Result |
|---|---:|---|
| `groupAStarted: false→true` | 0 | **MISSED**; prose still says Group A not started |
| `currentProposalApproved: false→true` | 0 | **MISSED**; prose still says current proposal not approved/unreviewed |
| `blockedCorrection: null→"C2-01"` | 0 | **MISSED**; success line reports C2-01 both resolved and blocked |

The other six booleans each failed semantically when flipped, and
`resolvedCorrection: "C2-01"→null` failed. That partial success does not satisfy the
binding claim or the requested each-boolean mutation requirement. The validator can still
accept impossible gate states, so this is authority-bearing and HIGH.

### 2. HIGH — C4-02's live correction has no semantic regression guard

Proposal §7 O1 currently says a Gate-B approval records the consultation/citation-only
classification and future eligibility but does not approve or authorize citation
(`GATE_B_SOURCE_SELECTION.md:1978`). That live sentence agrees with plan §§9.8–9.10.

An isolated fixture changed only that live O1 authority clause to say a Gate-B approval
“approves citation, not copying.” The proposal's full hash was recomputed and re-pinned in
the fixture handoff, eliminating checksum noise. `phase5_plan_consistency.py` exited 0 with
zero failures and warnings.

This is the exact semantic authority regression C4-02 closed. A historical stale-phrase
list is not a substitute for deriving the action boundary from the current row. Because the
validator permits Gate B to regain Gate-C citation authority silently, C4-02 is not
structurally closed.

### 3. MEDIUM — C4-03 remains live for D3 and §3.3 is still outside the sweep

The governing lifecycle says a conditional source cannot be fetched into the manifest,
appear in a `sourceId`, or be relied on until its blocker resolves and the owner accepts the
resolution (proposal `:270-272`; plan `:1222-1256`). The only blocker-resolving read/fetch
while conditional is the bounded §9.9.1 Gate-D evaluation-only action; `sources.json`
population is later acquisition.

D3 does not preserve that sequence:

- §2.6 says the per-model `LICENSE` is read **and recorded in `sources.json`** before the
  model is used (`GATE_B_SOURCE_SELECTION.md:280`);
- the §5 draft repeats “read and record ... before ... used” in `activationCondition`
  (`:1288-1291`), without evaluation-only status or owner acceptance;
- §7 O7 again says “Read and record the licence per model used” (`:1985`).

Thus the action that resolves the blocker is still bundled with manifest/schema population,
an acquisition step the source is ineligible for until after resolution and acceptance.

The validator's claimed exhaustive sweep is also false. It scans §2.6, three selected §5
fields and §7 (`phase5_plan_consistency.py:796-833`); it does not scan §3.3. Its positive
requirement merely checks that `evaluation-only` and `9.9.1` occur somewhere in §2.6
(`:835-842`), not once per conditional resolution. A §3.3-only mutation restoring “read at
acquisition” exited 0. The cited E9/E10 cells are fixed, but the sibling lifecycle is not.

### 4. MEDIUM — STR-02 has a live `SYM-02` replacement contradiction

Plan §8.2 leaves `SYM-02`'s substitution replacement explicitly unsettled because `σ` already
has six baseline meanings, and requires Gate C to choose a genuinely free symbol
(`PHASE5_AUGMENTATION_PLAN.md:960`). The five-module migration table repeats that unsettled
state at `:973-981`. The ledger records `theta->UNSETTLED` and the same Gate-C requirement
(`phase5-planning-ledger.json:1613-1632`).

Two current proposal regions state the opposite:

- the notation-conflict table says `σ` is the **renamed SYM-02 substitution**
  (`GATE_B_SOURCE_SELECTION.md:490`);
- the A7 coverage row repeats that collision (`:1802`).

These are live planning inputs to Gate C, not labelled history. They prematurely select the
symbol the authoritative plan deliberately leaves unresolved and make the proposed notation
bridge self-contradictory.

## Confirmed closures and structural re-checks

### C1-01 — PASS

Proposal header, plan pin and the detached note at proposal `:9` all name proposal 8 / plan
3.7. Changing only the detached note from 8 to 5, then re-pinning the changed proposal hash,
failed with current-revision diagnostics and no hash failure.

### C2-01 — PASS

`KIN-02.md:141-160` now separates the batches coherently: F0 teaches/corrects quaternion
content and replaces the unrelated prompt; F8 keys that prompt and owns every added recall
item; F0 adds the missing DYN-exam remediation mapping; F8 persistence-checks it only; F8
adds 0.0 scheduled learner hours. This agrees with plan §§4.0.1a, 5.3a, 13 and 17.2.

The review record still pins superseded plan 3.6. The handoff correctly classifies that as a
review-lane pin-staleness item, not a substantive reopening of C2-01; this audit had no
authority to re-pin it.

### C2-02 and C2-03 — PASS

Independent derivation reproduced the six components:

```text
120.5 + 9.0 + 9.5 + 1.5 + 1.5 + 0.0 = 142.0 h
```

The ledger component map, published figures, policy and batch agree. Plan §5.1 now lists all
six rows and a 142.0 total. An isolated F8 component-only `0→2` mutation failed, as did a
plan-table mutation that preserved the 0.0 row but removed its keyed-recall identity, with all
dependent hashes re-pinned.

### C9-04 — PASS

Direct parsing found 39 unique scored rows, each with eleven score cells summing to its row
total and exactly one status. The union is exactly 23 SELECT + 7 OPTIONAL + 9 CONDITIONAL.

Two exhaustive mutation sets were run:

- each of the 39 ledger membership entries was independently moved to a different bucket;
- each of the 39 scored-row decision cells was independently changed to a different status,
  with the proposal hash re-pinned each time.

All 78 mutations failed semantically with row/membership diagnostics and no generic hash
failure.

### STR-01 — PASS

Plan §§4.6b, 6 and 13 plus the ledger agree:

- `OPT-04B` prerequisites: `OPT-03`, `OPT-04`, `NUM-03`; it consumes repaired KKT;
- `OPT-05B` prerequisites: `OPT-05`, `PROB-02`, `NUM-01`; it does not consume KKT;
- F0→F1→F0b places repaired KKT and `NUM-03` before `OPT-04B`.

No live sibling assigns the KKT repair to `OPT-05B`; occurrences of the old sentence are
explicitly scoped historical correction notes or stale-claim fixtures.

## Totals, classification and gate order

An independent parser, not the project validator, reproduced the current baseline as 69
modules / 226.0 h / 15 blocks and the proposed delta as 36 modules / 120.5 h (31 main,
105.5 h; 5 optional, 15.0 h). Adding foundation 9.0, in-place 9.5, calibration 1.5,
rescope 1.5 and recall 0.0 gives +142.0 h and 105 modules / 20 blocks / 368.0 h.
Existing Tier-3 modules plus optional boxes bring optional study to 20.5 h; main route is
347.5 h. Published inventories remain 13 exams, 19 cheat sheets, 35 labs, 13 required static
figures and 7 in-block additions.

The roadmap headings are A→B→C→D→E→F→G. Gate F explicitly orders
F0→F1→F0b→F2→F3→F4→F5→F6→F7→F8. All 36 proposed modules have resolvable,
preceding prerequisites under the canonical 105-module route, and no main-route proposed
module depends on an optional module.

## Gate-A invariance

`GATE_A_BASELINE.md` remains byte-identical at approved SHA-256
`470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4`.
`git diff --exit-code` is clean for Gate A and decisions 0005–0007. Prior audit hashes match
their handoff/ledger pins. The baseline commit is an ancestor of current HEAD. Nothing in
the candidate or this audit reopens Gate A.

## Disposable mutation matrix

Ninety-seven isolated mutations ran in one disposable repository copy under
`/private/tmp/phase5-structural-audit-37.*`. The fixture was restored from original bytes
before each mutation. Changed plan/proposal hashes and downstream pins were recomputed inside
the fixture, so no expected failure depended on a generic checksum mismatch. The fixture was
deleted after the run.

| Mutation family | Required semantic failures | Actual | Verdict |
|---|---:|---:|---|
| Every governing status boolean, flipped independently | 8/8 | **6/8** | **FAIL** — `groupAStarted`, `currentProposalApproved` missed |
| Correction state fields, changed independently | 2/2 | **1/2** | **FAIL** — `blockedCorrection` missed |
| Every ledger source membership, moved independently | 39/39 | **39/39** | **PASS** |
| Every scored-row decision, changed independently | 39/39 | **39/39** | **PASS** |
| Targeted closure/freshness mutations | 9/9 | **7/9** | **FAIL** — C4-02 O1 and C4-03 §3.3 missed |

The targeted closure set comprised C1-01; C2-02; C2-03; C4-02; C4-03 separately in §2.6,
§3.3, §5 and §7; and a fully recorded/pinned audit of the current candidate while
`currentProposalReviewed=false`. All except C4-02 O1 and C4-03 §3.3 failed semantically.

## Validator runs and freshness transition

Initial current-byte runs before this report existed:

- `python3 scripts/validate/agent_context.py`: exit 0; 0 failures, 0 warnings.
- `python3 scripts/validate/review_integrity.py`: exit 0; 0 failures, 0 warnings.
- `python3 scripts/validate/phase5_plan_consistency.py`: exit 0; 0 failures, 0 warnings.

The Phase-5 validator's clean result is not dispositive because the mutations and live sibling
search above demonstrate its false negatives.

At audit start, audit/handoff freshness passed: all three prior reports were present at their
exact recorded hashes, none targeted plan 3.7 / proposal 8, and the handoff pinned the latest
pre-existing report. The isolated fixture that added and fully recorded a current-candidate
audit while leaving `currentProposalReviewed=false` failed semantically, so that core
freshness transition is enforced.

Publishing this report necessarily changes the live state: plan 3.7 / proposal 8 has now been
reviewed and failed. Per the owner's no-candidate-correction boundary, this audit does not edit
the ledger/plan/proposal to absorb that transition. The handoff is updated only to record this
FAIL and the next safe action. Until the planning lane records this report and advances the
candidate status, `phase5_plan_consistency.py` is expected to fail its audit-freshness check;
that is the correct stop state, not a reason for this reviewer to edit planning-owned files.

No Astro check or production build was run: no curriculum or runtime artifact was changed,
and those commands cannot falsify these structural findings. No source was fetched, acquired,
installed, ingested, pinned or externally checked. No approval was requested or recorded. No
commit or push was performed.

The next safe action is a planning-lane correction pass for the four findings above, including
semantic mutation coverage for every status fact and every current authority/lifecycle region,
followed by one fresh independent structural review. No approval request is safe before a later
review passes.

Final verdict: **STRUCTURAL FAIL**.
