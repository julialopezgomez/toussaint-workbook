# Independent structural audit — Phase 5 plan 3.3 / Gate B proposal 4

Date: 2026-08-15  
Reviewer role: independent, adversarial structural pass  
Scope: corrections C1–C4 and C9, validator quality, arithmetic/route regressions, and sampled unaffected sections only  
Write boundary: this report is the only authorized write; all governing artifacts were inspected read-only

## Verdict ledger

| Audit item | Status | Current basis |
|---|---|---|
| C1 — revision, approval, Gate B status, totals, supersession | **PASS** | Independently checked across plan, proposal, ledger, validator, handoff, decisions, repository state, and hashes |
| C2 — F0 excludes keyed-recall production; F8 owns it | **FAIL** | Current plan prose is corrected, but an approved/reconciled KIN-02 record still assigns keyed recall to F0, and F8 recall hours are asserted without a ledger allocation |
| C3 — Gate E fixture is disposable only | **PASS** | P1 is scratch-only, self-created, deleted at exit, uncommitted, and independent of both paused production prototypes |
| C4 — Gate B permits evaluation/planning artifacts only | **FAIL** | Plan §9.8 and the proposal header explicitly authorize acquisition/fetching and `sources.json` pinning at Gate B, contradicting the paper-exercise/no-ingestion boundary |
| C9 — exam/cheat-sheet IDs and validator quality | **FAIL** | The IDs/counts are correct, but multiple count-preserving or internally duplicated defects pass the validator |
| Structural totals, classification, gate order, Gate A invariance, unaffected samples | **FAIL** | Totals, classification, execution order, and Gate A pass; two dependency/notation contradictions remain |
| C5–C8 external-source claims | **UNVERIFIED / DEFERRED** | Deliberately outside this structural pass |

Overall verdict: **STRUCTURAL FAIL**. C2, C4, C9, and the sampled structural-regression item fail;
no approval or production gate may follow from this report.

## Repository state and audited identities

The repository was dirty before this report was created. The current repository `HEAD` is
`e8e75e5a58964417272df2b70ac5bbbc4bcad363`; this is distinct from the authoritative Phase 4
content baseline `dd2e8717f82dfcb77aff4b8c89aba258997f87fe` named by the plan and approved in decision
0005. `git log --oneline` shows `dd2e871…` as an ancestor of `HEAD`, followed by review/agent-quality
documentation commits.

Pre-report `git status --short`:

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
?? scripts/validate/phase5_plan_consistency.py
?? src/components/interactive/
?? tmp/
```

Thus the audited plan and handoff are modified relative to `HEAD`, while the audited proposal,
ledger, and Phase 5 validator are untracked. The audit assesses those current worktree bytes; it
does not present them as committed. `docs/plans/GATE_A_BASELINE.md`, decisions 0005–0007, and
`docs/review/**` had no pre-report diff. Existing unrelated changes remain user-owned and untouched.

Full SHA-256 identities of the governing/evidence files audited at the start of the pass:

| Artifact | SHA-256 |
|---|---|
| `docs/plans/PHASE5_AUGMENTATION_PLAN.md` | `edcfdbce55bee89558d6d8362a5b960a1a548b0c5556fef8dfc2b3ad1c02303d` |
| `docs/plans/GATE_B_SOURCE_SELECTION.md` | `f63e0aef2b86ca60badda047abec0e8b76bbf9d974cf7b98152045f6520acb8f` |
| `docs/plans/phase5-planning-ledger.json` | `60cfab6c476b81e1751c8e5fab6589c81ad87a3d89944e2441206b236374aafc` |
| `scripts/validate/phase5_plan_consistency.py` | `e9f991aeaf6544680160b8257782e3df73ed2fc0e43c9acb18487b2d0c3e7a99` |
| `docs/agent/CURRENT_HANDOFF.md` | `9a04c02368bdb34584fbbda7baf5308660a223d08d83ca7f8a5c9fa5f65fd02c` |
| `docs/plans/GATE_A_BASELINE.md` | `470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4` |
| `docs/decisions/0005-gate-a-approved.md` | `2078d528e8add9b01aac12f05cc69fd424f6bdd300791ab0a95d65fe1a4a7dcf` |
| `docs/decisions/0006-math-review-approved.md` | `7d93931650f91332eac8f903f50cb36c1958b8ef254ed682006d041106b83b07` |
| `docs/decisions/0007-opt-review-approved.md` | `b132d889e04f612d9375f1dc9075f195a2d31c88139b8417a716cc6bffe27ad8` |
| `data/source-manifest/manifest.json` | `ef009f1481cd1d5379c20db4feab7156d43443dc38fc58e0046c119e78f36960` |
| `docs/review/REVIEW_INDEX.md` | `021cfd2b62c1a33eabeae92db95e14f5229957819acda5c3aa1a99e91dc938f4` |
| `docs/review/modules/KIN-02.md` | `34a4c108aeec1546875d4d39ab735147d7113db66378c869013dcc30fd3bd259` |
| `docs/review/blocks/MATH.md` | `50e0e5f396f94b8fe59e0d76f63cd19dc5710a191cb0f94e64e65797a6a0c042` |
| `docs/review/blocks/OPT.md` | `38f414282ed1ccc9dd1eb15b99ce86bd957a8f473abd092a8a07bfe3897a7e63` |
| `docs/review/CURRICULUM_COVERAGE.md` | `ce8b27652eb92fb41b2bdf4f66b94d1bcba3692e2c3c023c8948ec34bc154e45` |

Initial required checks, run against those bytes:

- `python3 scripts/validate/agent_context.py`: exit 0, 0 failures, 0 warnings.
- `python3 scripts/validate/review_integrity.py`: exit 0, 0 failures, 0 warnings.
- `python3 scripts/validate/phase5_plan_consistency.py`: exit 0, 0 failures, 0 warnings.

These are baseline observations, not substitutes for the adversarial checks below. The last script
explicitly describes itself as arithmetic/ID integrity rather than pedagogical validation.

## C1 — revision, approval, status, totals, and supersession

Status: **PASS**.

Independent evidence:

- Plan identity/status: `PHASE5_AUGMENTATION_PLAN.md:3-8` declares plan revision 3.3, baseline
  `dd2e871…`, Gate A closed/approved at plan revision 2.1, Gate B **NOT STARTED / NOT APPROVED**,
  proposal revision 4 awaiting its first independent review, and no approval request. Its history at
  `:12-21` scopes revisions 2.2, 3.0, 3.1, and 3.2 as historical/superseded changes and records that
  proposal revisions 1–3 failed.
- Proposal identity/status: `GATE_B_SOURCE_SELECTION.md:3-16` independently separates proposal
  revision 4 from plan revision 3.3, pins the full plan hash above, and says revision 4 is not approved,
  not reviewed, and Gate B has not started. Historical correction tables at `:37-81` scope each old
  claim to proposal revisions 1–3 rather than presenting it as current.
- Proposal approval boundary: `GATE_B_SOURCE_SELECTION.md:1940-1944`, `:1948-1964`, and
  `:1966-1972` say neither full Gate B nor Group A has been approved or requested. A possible future
  Group-A approval is explicitly hypothetical.
- Plan restatements: `PHASE5_AUGMENTATION_PLAN.md:1096-1102` and `:1521-1527` match the header:
  proposal 4 is unreviewed; no source is ingested; Gate B is not started/approved; approval requires
  future explicit owner sign-off.
- Decisions are consistent: decision 0005 `:21-25,47-49` approves Gate A only and leaves Gate B
  unapproved/unbegun; decisions 0006 `:68-76` and 0007 `:67-85` require the later reconciled proposal
  and explicitly do not approve production sources or authoring. No decision 0008 or Gate-B approval
  record exists in `docs/decisions/`.
- Handoff corroboration, not authority: `CURRENT_HANDOFF.md:8-18,24-27,67-77,124-142` matches the
  plan/proposal pins and correctly labels the producer's correction register as claims awaiting this
  review.
- Ledger: `phase5-planning-ledger.json:4-7` identifies plan 3.3/proposal 4 and baseline `dd2e871…`;
  `:1194-1313` defines proposal-4 expectations. Published totals at `:971-1007` are 105 modules,
  20 blocks, 368.0 h, 347.5 h main, 20.5 h optional, +36 modules, and +142.0 h.
- Machine cross-check: the initial Phase 5 validator independently recomputed the 69-module/226.0 h
  baseline from frontmatter; matched committed baseline and worktree per block; matched the 20-row
  plan table and all published totals; verified full plan/proposal/handoff pins; and verified the
  unchanged Gate A hash. Arithmetic derivation and mutation resistance are audited separately below.
- Hash pins are exact: independently computed plan SHA-256 `edcf…303d` equals the proposal and
  handoff pins; independently computed proposal SHA-256 `f63e…b8f` equals the handoff pin.
- Unchanged Gate A evidence: `git diff --exit-code` is clean for `GATE_A_BASELINE.md` and decisions
  0005–0007; the independently computed Gate A hash is the approved `470046…a4`.

Adversarial note: the phrase “Gate B has not started” is a deliberately strict project-status label
despite a proposal existing. That exact convention is required by the audit brief and is used
consistently; no source acquisition, manifest migration, approval decision, Gate-C authoring, or
Gate-D evaluation has occurred. The existing manifest remains the original 13-PDF file.

Findings for C1: none.

## Severity-ranked findings

1. **CRITICAL — C4-01: Gate B is granted source-ingestion authority despite an explicit no-ingestion
   boundary.** Plan `PHASE5_AUGMENTATION_PLAN.md:1123-1133` says Gate-B approval permits acquisition,
   fetching, and recording a source in `sources.json` v2. Proposal `GATE_B_SOURCE_SELECTION.md:19`
   repeats acquisition and pinning as the direct effect of approval. Plan/proposal partial-approval
   tables at plan `:1192-1201` and proposal `:1952-1960` prohibit populated `sources.json` only
   “beyond the approved Group-A entries,” which affirmatively leaves Group-A manifest population
   authorized. This contradicts the governing audit boundary and the same documents' Gate-D-only
   migration/no-ingestion clauses.
2. **HIGH — C2-01: approved KIN-02 reconciliation still assigns keyed-recall production to F0.**
   `docs/review/modules/KIN-02.md:1-4` marks the record `APPROVED / RECONCILED`. Its reconciliation
   table at `:147` says keyed recall becomes a Gate-F0 repair for KIN02-01/03/04, and `:152` says F0
   rewrites KIN02-08 as “direct keyed recall” and names convention targets. That directly contradicts
   plan 3.3 `:376-390`, `:1579-1593`, and `:1790,1798`, which reserve all keying and added recall for
   F8 and allow F0 only to replace the wrong prompt with an unkeyed/correct prompt. Because the
   review record is approved evidence for reviewed scope and is still the live reconciliation record,
   this is not cured merely by labelling its revision-2.2 pin stale.
3. **HIGH — C9-01: planned assessment IDs and their batch ownership are not checked against the
   plan.** Validator `phase5_plan_consistency.py:465-490` reads planned IDs and batch maps only from
   the ledger. It checks count, collision, and presence of a batch key, but never parses plan §5.3/F8
   and never checks that a batch value is `F8`. Disposable mutations replacing `ACC-EXAM` with
   `FAKE-EXAM`, replacing cheat sheet `acc` with `fake-sheet`, and assigning `ACC-EXAM` to `F0` all
   exited 0.
4. **HIGH — C9-02: coverage/status “derivations” accept count-preserving semantic corruption.** The
   coverage check at validator `:741-781` counts five-cell rows but does not check unit uniqueness or
   per-source membership from the proposal. Duplicating `UA ch.1` over `UA ch.2`, then updating the
   handoff's proposal hash, exited 0. The status check at `:782-830` compares row sums and roll-up
   counts to ledger constants but does not parse the roll-up source membership; moving A1 from the
   SELECT list to OPTIONAL without changing the printed counts also exited 0.
5. **MEDIUM — C9-03: existing assessment IDs are derived from filenames, not the actual frontmatter
   IDs.** Validator `:454-463` uses `Path.stem`. Changing `MATH-EXAM.mdx` frontmatter from
   `MATH-EXAM` to `MUTATED-EXAM` exited 0, even though `src/content.config.ts:129-138` defines the
   milestone `id` as content data. Current filenames and frontmatter happen to agree, so the present
   count is right; the claimed validation method is not robust.
6. **MEDIUM — C2-02: F8 recall hours are asserted but not represented or derivable.** Ledger
   `phase5-planning-ledger.json:8-20` says keyed recall is excluded from compact-addition/F0 sizing and
   “is sized separately in [F8].” Yet `published` at `:971-992` has no recall/F8 hour field. Its five
   delta components are 120.5 + 9.0 + 9.5 + 1.5 + 1.5 = 142.0 h, exactly the entire published
   `addedHours`; there is no residual allocation for separately sized recall. The plan repeats the
   unsupported sizing claim at `PHASE5_AUGMENTATION_PLAN.md:65-67`. This makes the required
   ownership of “its hours” unauditable. If recall intentionally adds 0.0 learner hours, the governing
   records need to say that instead of claiming separate F8 sizing.
7. **MEDIUM — STR-01: `OPT-05B` is assigned a KKT-repair dependency that its own specification and
   ledger do not have.** Plan `PHASE5_AUGMENTATION_PLAN.md:532` says both `OPT-04B` and `OPT-05B`
   depend on F0 repairing `OPT-03`'s KKT necessity conditions, and the F0b schedule repeats that
   claim at `:1581`. But `OPT-05B` is derivative-free optimization; its declared prerequisites and
   teaching dependencies at `:530,694-697` are `OPT-05`, `PROB-02`, and `NUM-01`, with no `OPT-03`
   or KKT content. Ledger `phase5-planning-ledger.json:864-875` agrees with that declared edge set.
   The execution order remains safe because F0 precedes all production, but the binding dependency
   statement and batch rationale are false for one of F0b's two modules.
8. **MEDIUM — STR-02: the notation migration omits existing LQR `R`/`Q` uses in `DYN-04`.** Plan
   `PHASE5_AUGMENTATION_PLAN.md:917-918` rules that `R` is a rotation matrix everywhere in DYN and
   that LQR cost matrices become `R_u`/`Q_x`, but the `R_u` row names only `DYN-06`, UAC, and
   `SIM-04`. Existing `src/content/course/DYN/DYN-04.mdx:25,76,80,82,88,120` uses `R` as the LQR
   input-cost matrix and `Q` as the state-cost matrix. The claim at plan `:934` that four renames
   touch four existing modules, and Gate-C's required exact four-module diff at `:1530`, do not
   resolve or even name that existing collision. `DYN-06.mdx:117-125` also uses the LQR notation,
   confirming that this is a cross-module migration rather than a DYN-06-only edit.

## C2 — F0/F8 keyed-recall ownership and hours

Status: **FAIL**.

What is structurally correct in plan revision 3.3:

- The sizing rule at `PHASE5_AUGMENTATION_PLAN.md:65-67` removes keyed recall from compact F0
  additions and assigns it to F8.
- The exclusion table and boundary at `:374-390` assign every keyed-recall addition (MATH, OPT,
  MATH-02B, KIN-02, RLEARN-02) to F8; F0 retains only the correction of KIN02-08's wrong prompt and
  the missing existing `DYN-EXAM` mapping.
- The assessment split at `:653-667`, production schedule at `:1569-1593`, and F8 acceptance rows at
  `:1595-1606` consistently place new recall/keying in F8. `DYN-EXAM` is correctly a persistence
  check in F8, not a second remediation addition.
- The KIN-02 dispositions in the current plan at `:1790` and `:1798` explicitly separate concept and
  wrong-prompt repair at F0 from keying/additional recall at F8; `:1823` keeps only the missing
  remediation-map correction at F0.
- Ledger `:8-20` excludes all keyed-recall additions from F0, and assessment inventory note `:1155`
  correctly describes the `DYN-EXAM` F0-add/F8-persistence split. Decisions 0006 `:44,64,76` and
  0007 `:45,64,86` place whole-block MATH/OPT keyed recall in F8.

Why the item nevertheless fails:

- Finding C2-01 is an active cross-record contradiction in approved evidence, not a historical quote.
- Finding C2-02 leaves the required hour transfer/ownership unrepresented.
- `phase5_plan_consistency.py` contains no semantic F0/F8 ownership check; the handoff itself admits
  this at `CURRENT_HANDOFF.md:41,91-94`. Its passing result therefore supplies no evidence against
  either finding.

## C3 — disposable Gate-E fixture and paused prototypes

Status: **PASS**.

Evidence:

- The plan distinguishes existing user-owned prototypes from Gate-E fixtures. Current-state inventory
  `PHASE5_AUGMENTATION_PLAN.md:121-132` calls `RotationViz` and `GridWorldRL` earlier pilot assets but
  immediately marks both owner-paused and unscheduled; that historical asset description does not make
  either a Gate-E artifact.
- The binding pause rule at `:558-573` says no batch, gate, pilot, budget check, deliverable, acceptance
  criterion, or dependency may rely on either prototype. `RotationViz` has 0 scheduled hours;
  `GridWorldRL` may only be reconsidered by a future owner-approved amendment, while F2 can author a
  fresh visualization or drop it.
- The catalog at `:1209-1229` labels both entries as paused/not scheduled or authorable independently;
  it does not promote either to a Gate-E prerequisite.
- Gate D at `:1535-1544` exercises the performance check on a disposable WebGL fixture and explicitly
  excludes `RotationViz`.
- The Gate-E binding rule at `:1546-1553` excludes every pilot from content collections, route,
  assessment, Anki, lab/module/hour totals, and teaching content, and requires deletion or quarantine
  at gate exit.
- P1 at `:1554-1556` creates its own scratch fixture as its only dependency, does not read/import/
  reactivate `RotationViz`, `GridWorldRL`, or `KIN-01`, and deletes the fixture at exit. P2–P5 are
  likewise throwaway fixtures/notebooks rather than paused production artifacts (`:1557-1563`).
- Gate-E acceptance at `:1564-1567` requires no pilot artifact in a content collection or commit and
  says Gate E ships nothing. The nearby committed `full` outputs are explicitly deferred to F-batches.
- The downstream stabilization entry at `:1634` again uses the disposable fixture and keeps the
  `RotationViz` refactor unscheduled. The documentation trigger at `:1671` is corrected to F-batches,
  not pilot commits.
- Ledger `phase5-planning-ledger.json:1082-1098` records both production prototypes as `PAUSED`, 0.0
  scheduled prototype hours, and non-dependencies. Proposal `GATE_B_SOURCE_SELECTION.md:1954-1961`
  says even a future Group-A approval cannot reactivate them. Handoff `CURRENT_HANDOFF.md:115-121`
  matches this boundary.
- Full repository search found the stale phrases “P1 is blocked on a paused prototype” and “once the
  pilots are committed” only in the ledger's forbidden-stale-claim list and in explicitly labelled
  correction history, never as current instructions. References to older Phase-2/Phase-3 pilots are
  historically scoped and unrelated to Gate E.

Findings for C3: none.

## C4 — Gate-B authorization boundary

Status: **FAIL**.

The intended boundary is present and mostly clear:

- Gate-B deliverables at `PHASE5_AUGMENTATION_PLAN.md:1096-1102` are planning artifacts: scored
  candidates, a coverage matrix, a complete draft schema, notation conflicts, and rejection reasons.
- Bounded install/fetch experiments are explicitly Gate D only; Gate B is called a “paper exercise”
  at `:1170-1186`.
- The roadmap at `:1521-1527` prohibits source ingestion, manifest population, module authoring, and
  notation renames at Gate B. Gate C owns curriculum stubs/specification (`:1529-1533`); Gate D owns
  runtime/lab architecture (`:1535-1544`).
- Proposal `GATE_B_SOURCE_SELECTION.md:423-425` says the embedded `sources.json` is only a draft and
  that migration is Gate D. Proposal `:1940-1942` likewise says Gate B does not execute migration,
  authorize installs, authoring, visibility, deployment, or evaluation-only fetching.
- Module, lesson, exercise, solution, cheat-sheet, exam, figure/visualization, lab, and runtime
  implementation are consistently denied by plan `:1127-1133,1192-1203,1519-1529,1614-1615` and
  proposal `:19,1940-1942,1952-1962`.

The boundary nevertheless fails because the ingestion clauses are current normative text, not
historical quotes:

- Plan `:1123` defines approval as permission to “acquire, pin, and record”; plan `:1129` expressly
  permits fetching and writing a `sources.json` v2 record.
- Proposal `:19` says approval permits acquisition and pinning into `sources.json` v2.
- Plan `:1195` and proposal `:1955` prohibit populated `sources.json` only beyond approved Group-A
  entries, implying that Gate-B/Group-A approval may populate those entries.
- Proposal open-item rows elsewhere correctly call `manifest.json` → `sources.json` migration Gate D
  work (`GATE_B_SOURCE_SELECTION.md:1913`), making the contradiction internal as well as contrary to
  the audit requirement.

Gate B may evaluate sources and produce/approve planning records. Fetching source payloads into the
repository, populating the manifest, pinning acquired repositories/files, or otherwise ingesting them
is implementation and must remain a later gate. Finding C4-01 is therefore gate-blocking.

## C9 — assessment inventories and validator quality

Status: **FAIL** (inventories correct; validator-quality claim false).

### Independent ID/count derivation

The current repository frontmatter, read directly rather than through the ledger, contains exactly
eight milestone IDs:

`CUMULATIVE-FINAL`, `DYN-EXAM`, `MATH-EXAM`, `ML-EXAM`, `OPT-EXAM`, `PROB-EXAM`, `RL-EXAM`,
`RLEARN-EXAM`.

It contains exactly fourteen cheat-sheet IDs:

`cap`, `dyn`, `kin`, `manip`, `math`, `ml`, `neural-networks-backprop`, `ode`, `opt`, `plan`, `prob`,
`rl`, `rlearn`, `sym`.

All current filename stems match those frontmatter IDs. Plan §5.3
(`PHASE5_AUGMENTATION_PLAN.md:648-651`) independently names five planned exams — `PLAN-EXAM`,
`UAC-EXAM`, `SIM-EXAM`, `DRL-EXAM`, `ACC-EXAM` — and five planned sheets — `num`, `uac`, `acc`,
`sim`, `drl`. None collides with the existing sets. Therefore the current claims **8 + 5 = 13
exams** and **14 + 5 = 19 cheat sheets** are correct. The F8 schedule at `:1579-1588` owns all five
new exams and all five new sheets, matching ledger `phase5-planning-ledger.json:1100-1155`.

### Code inspection

Useful derivations genuinely present:

- Baseline module/hours are read from course frontmatter and separately from Git commit `dd2e871…`
  (`phase5_plan_consistency.py:94-130,198-241`).
- Totals are recomputed from enumerated ledger deltas, not from `published` (`:244-338`), and the
  20-row §5.1 table is parsed and checked cell by cell (`:520-564`).
- New-module collision, block order, optional dependency, and module-level prerequisite order checks
  are substantive (`:340-416,492-518`).
- Exact plan/proposal/handoff hashes and the fixed Gate-A hash are checked (`:566-604`).
- PDF migration fields are compared with the actual 13-entry manifest (`:681-723`).

Material gaps are findings C9-01 through C9-03. In addition, the score code initializes `seen` but
never populates or uses it (`:790`), and the parsed per-row `decision` is unreachable/unused because
rows with a length other than 14 are skipped before `cells[14]` could exist (`:794-806`). The printed
claim in proposal `GATE_B_SOURCE_SELECTION.md:241` that every status count is recomputed from the
tables above is therefore false: the validator compares the three printed roll-up counts to the same
three ledger counts.

### Disposable falsification results

All mutations were made in isolated copies under `/private/tmp/phase5-structural-audit.*`; no
governing file was edited.

| Injected defect | Expected | Actual | Result |
|---|---:|---:|---|
| Ledger planned exam `ACC-EXAM` → `FAKE-EXAM`, with its batch key kept internally consistent; plan unchanged | fail | exit 0 | **false negative** |
| Ledger planned sheet `acc` → `fake-sheet`, with batch key changed; plan unchanged | fail | exit 0 | **false negative** |
| Ledger `ACC-EXAM` batch `F8` → `F0` | fail | exit 0 | **false negative** |
| Existing `MATH-EXAM.mdx` frontmatter ID → `MUTATED-EXAM`; filename unchanged | fail | exit 0 | **false negative** |
| Proposal coverage unit `UA ch.2` relabelled as duplicate `UA ch.1`; proposal hash re-pinned | fail | exit 0 | **false negative** |
| A1 moved from SELECT roll-up membership to OPTIONAL; counts retained; proposal hash re-pinned | fail | exit 0 | **false negative** |
| Planned exam changed to existing `MATH-EXAM` | fail | exit 1, collision reported | pass |
| `NUM-01` changed to depend on later `NUM-03` | fail | exit 1, module-order violation reported | pass |
| Plan §5.1 MATH hours 37.5 → 99.5 | fail | exit 1, bad cell and stale pins reported | pass |

The validator is useful but does not justify the handoff's broad statement that it independently
checks ID enumeration, coverage completeness, or score/status consistency in the strong sense those
phrases imply.

## Structural regressions

Status: **FAIL** (arithmetic, route classification, execution order, and Gate A pass; two sampled
dependency/notation assertions fail).

### Independent totals and route classification — PASS

A separate read-only calculation parsed module frontmatter directly from committed tree
`dd2e8717f82dfcb77aff4b8c89aba258997f87fe`, compared the current worktree frontmatter, and applied
the enumerated ledger deltas without importing or calling `phase5_plan_consistency.py`. It derived:

- committed baseline: **69 modules, 15 blocks, 226.0 h**;
- current worktree frontmatter: the same 69 modules, 15 blocks, and 226.0 h;
- 36 new modules = **120.5 h**; 14 foundation additions = **9.0 h**; 15 in-place additions =
  **9.5 h**; two calibration additions = **1.5 h**; two review rescopes = **1.5 h**;
- delta: 120.5 + 9.0 + 9.5 + 1.5 + 1.5 = **142.0 h**;
- result: **105 modules, 20 blocks, 368.0 h**.

The independently derived per-block tuple `(modules, baseline h, delta h, total h)` was:

```text
MATH   8  32.5   5.0  37.5     NUM    3   0.0   8.0   8.0
PROB   6  18.0   0.0  18.0     OPT    8  28.5  10.5  39.0
ODE    3  11.5   1.5  13.0     KIN    3   8.0   1.5   9.5
DYN    7  27.0   2.5  29.5     UAC    5   0.0  16.5  16.5
PLAN   6  12.0   9.0  21.0     MANIP  5   5.5  10.5  16.0
ML     7  23.0   1.0  24.0     ACC    6   0.0  18.5  18.5
RL     7  20.5   1.5  22.0     SYM    4   8.5   0.0   8.5
REV1   1   1.5   0.5   2.0     RLEARN 9  25.5   1.0  26.5
SIM    6   0.0  20.5  20.5     DRL    8   0.0  29.0  29.0
REV2   1   1.0   1.0   2.0     CAP    2   3.0   4.0   7.0
```

Every tuple matches plan `PHASE5_AUGMENTATION_PLAN.md:587-609`. The component decomposition matches
plan `:611-622` and the underlying ledger sections at `phase5-planning-ledger.json:49-954`; it was
not inferred from ledger `published` (`:955-1007`).

Optional hours independently resolve to **20.5 h**:

- existing Tier-3 `ML-07` 2.5 h and `RLEARN-08` 2.0 h, confirmed in current frontmatter at each
  file's `:2,5-6`;
- new optional Tier-3 `UAC-05` 3.0, `MANIP-05` 2.5, `ACC-05` 2.5, `ACC-06` 3.0, and `DRL-08`
  4.0 = 15.0 h, derived from the 36 ledger module rows at `phase5-planning-ledger.json:396-880`;
- optional `OPT-01` and `OPT-03` reference boxes = 1.0 h at ledger `:1067-1080`.

Thus 4.5 + 15.0 + 1.0 = **20.5 optional**, and 368.0 − 20.5 = **347.5 main**. This matches plan
`:624-629`. No new main-route module has an optional new-module prerequisite. Finding C2-02 remains
a separate hour-ownership defect: the 142.0 h decomposition leaves no explicit separately sized F8
recall component.

### Batch/gate order and dependency declarations — FAIL

The required execution order itself is correct: plan `:1571-1581` gives **F0 → F1 → F0b → F2 …
F8**; `NUM-03` belongs to F1 and requires `NUM-01`/`MATH-04` (ledger `:423-436`), while
`OPT-04B` belongs to F0b and requires `NUM-03` (ledger `:847-861`). An independent traversal of all
36 ledger rows found no prerequisite from a later canonical block and no main-route module depending
on an optional new module. The route order itself therefore passes.

The F0b dependency rationale does not. Finding STR-01 records the contradiction between the binding
“both need KKT” claim at plan `:532,1581` and `OPT-05B`'s actual derivative-free prerequisite set at
plan `:530,694-697` and ledger `:864-875`. Because dependency verification is part of this audit
item, the sub-item is **FAIL** despite a safe topological order.

### Gate A invariance — PASS

`git diff --exit-code` is clean for both `docs/plans/GATE_A_BASELINE.md` and decision 0005. The
worktree Gate-A report and `git show HEAD:docs/plans/GATE_A_BASELINE.md` independently hash to the
same full SHA-256, `470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4`.
Decision 0005 `:5-9,21-25` approves and closes Gate A while explicitly withholding source/content
authorization. Its approved baseline evidence remains `dd2e871…`, 69 modules (`:13-18`). No Gate-A
evidence change or reopening was found.

### Three samples outside the C1–C4/C9 correction loci

1. **§8 notation integration — FAIL.** The policy and planned Gate-C exact-diff mechanism are
   structurally sensible at plan `:907-938,1530`, but the actual `R`/`Q` ruling is incomplete and
   self-contradictory. Finding STR-02 gives the exact existing `DYN-04`/`DYN-06` evidence.
2. **§§11–12 runtime/device policy — PASS for structural consistency.** The selected single-site /
   local-lab design and its deployment shape are distinguished at plan `:1296-1328`; the main-route
   CPU requirement, exactly two CUDA-required optional artifacts, and the distinction between learner
   and project-validation dependencies agree at `:1474-1507`. This pass did not test performance,
   hardware, package, or service claims.
3. **§18 later-review amendment mechanism — PASS for structural consistency.** Only an approved
   decision may trigger an amendment (`:1846-1854`); each delta gets exactly one class and a recorded
   consequence (`:1856-1866`); Gate A is never reopened and only an affected class-S source subset
   may reopen at Gate B (`:1892-1899`); implementation remains gated and class S authorizes source
   evaluation, not authoring (`:1901-1908`). This last rule reinforces, rather than cures, C4-01's
   contradictory Gate-B ingestion authority elsewhere.

## Limitations and explicitly deferred work

This pass performs no external source verification. Corrections C5–C8 source/schema/coverage claims
are not accepted as source-truth merely because the structural validator passes. The next source-audit
session must verify those claims, including the two unfetched conditional papers
`deits-tedrake-iris` and `marcucci-gcs`, and the unverified Underactuated appendix titles. Those items
remain **UNVERIFIED**, not failed, in this report.

## Final verification and stop state

The three required validators were rerun after all audit analysis and falsification work:

- `python3 scripts/validate/agent_context.py`: exit 0, **0 failures, 0 warnings**;
- `python3 scripts/validate/review_integrity.py`: exit 0, **0 failures, 0 warnings**;
- `python3 scripts/validate/phase5_plan_consistency.py`: exit 0, **0 failures, 0 warnings**.

The last validator's own closing qualification is material: it validates internal arithmetic and ID
integrity, not pedagogy. Its green result does not override the false negatives demonstrated in C9 or
the cross-document contradictions in C2/C4/STR-01/STR-02.

All 15 audited artifact hashes in the opening table were recomputed after the final validator run and
were byte-for-byte unchanged. Final `git status --short` differs from the recorded pre-report state
only by `?? docs/review/planning/`, which contains this report alone. The governing worktree remains
dirty exactly as separately disclosed above; none of those pre-existing changes was repaired, staged,
discarded, or committed. All disposable falsification copies under
`/private/tmp/phase5-structural-audit.*` were removed.

Final verdict: **STRUCTURAL FAIL**. Gate B and Group A remain **UNAPPROVED and UNSTARTED**. This
report records no approval, performs no implementation, and authorizes none.
