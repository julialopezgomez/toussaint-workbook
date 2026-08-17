# Independent adversarial structural audit — Phase 5 plan 3.6 / Gate B proposal 7

Date: 2026-08-15  
Reviewer role: fresh independent adversarial structural pass  
Scope: C1–C4, C9, STR-01, STR-02, totals/classification/gate order/Gate-A invariance, and validator mutation resistance  
Write boundary: this report is the only review artifact created; all governing artifacts were inspected read-only  
External-source boundary: C5–C8 and other deferred external facts were not verified

## Overall verdict

**STRUCTURAL FAIL.** The five findings that blocked plan 3.5 / proposal 6 are substantively
answered: C1-01, C2-01, C2-02, C4-02 and C9-04 all pass their direct re-checks. The current pair
nevertheless has three fresh structural defects. The status validator prints the withdrawn
“no review ... authorized” state and ignores the ledger boolean that records the opposite; the
plan's purported exact added-hours decomposition omits its declared sixth component; and two
conditional-source resolution rows call the permitted evaluation-only fetch “acquisition,” although
the governing taxonomy makes conditional sources ineligible for acquisition until after that fetch
resolves the blocker.

Gate B and Group A remain unstarted and unapproved. This report approves nothing and authorizes no
next gate or approval request.

## Verdict ledger

| Audit item | Verdict | Basis |
|---|---|---|
| C1 — current revision/status/supersession consistency | **FAIL** | The six prose regions and ledger facts currently agree, and the C1-01 detached-number mutation is caught; however, the validator's passing diagnostic states the opposite review-authorization status, and changing the ledger's `independentReviewRequiredAndAuthorized` fact to false still exits 0 |
| C2 — F0/F8 ownership and hour policy | **FAIL** | C2-01 and C2-02 are fixed, but plan §5.1 says it decomposes +142.0 h “exactly” while listing only five components and omitting the real `f8KeyedRecall: 0.0 h` component that §5.3a says is “not omitted” |
| C3 — disposable Gate-E fixtures | **PASS** | All five pilots remain infrastructure-only scratch artifacts, excluded from content/routing/assessment/totals/commits and deleted or quarantined at exit; P1 has no paused-prototype dependency |
| C4 — Gate-B evaluation/planning-only authority and taxonomy | **FAIL** | C4-02's O1 and scored-conditional wording are corrected, but O5/O6 schedule conditional-source blocker resolution “at acquisition”; plan §9.9 makes those sources ineligible for acquisition and permits only a distinct Gate-D evaluation-only fetch while blocked |
| C9 — assessment IDs, scored-source identity and row status | **PASS** | Current 39-row matrix, 23/7/9 roll-up, ledger membership and D3 row agree; an A1 `SELECT→OPTIONAL` row-only mutation now fails with both intended per-ID diagnostics |
| STR-01 — `OPT-05B` dependencies | **PASS** | KKT/`NUM-03` belongs to `OPT-04B`; `OPT-05B` depends on `OPT-05`, `PROB-02`, `NUM-01` |
| STR-02 — notation migration | **PASS** | Five existing modules are named with direct baseline evidence; the `SYM-02` replacement remains explicitly unresolved for Gate C |
| Totals and route classification | **PASS for current numeric bytes** | 105 modules, 20 blocks, 368.0 h, 347.5 main / 20.5 optional, +36 modules / +142.0 h; the plan's displayed component enumeration still fails C2 as above |
| Gate and prerequisite order | **PASS** | A→B→C→D→E→F→G and F0→F1→F0b→F2…F8 are coherent; all 36 proposed module prerequisites pass semantic order and no main-route module depends on an optional module |
| Gate-A invariance | **PASS** | Approved evidence is byte-identical at its full approved hash, decisions 0005–0007 are clean, both prior audit hashes match their pins, and the baseline commit remains an ancestor of HEAD |
| C5–C8 and deferred external facts | **UNVERIFIED / DEFERRED** | Excluded by instruction; no external page, licence, source payload, version, cadence or appendix title was checked |

## Audited repository state and identities

This audit assessed current worktree bytes. Repository `HEAD` is
`e8e75e5a58964417272df2b70ac5bbbc4bcad363`; the authoritative committed Phase-4
baseline is ancestor `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`.

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

The plan/proposal/ledger/validator/handoff/KIN-02 changes were pre-existing candidate work. The
other dirty paths are user-owned. No existing dirty file was modified by this audit.

Full SHA-256 identities at audit start:

| Artifact | SHA-256 |
|---|---|
| `docs/plans/PHASE5_AUGMENTATION_PLAN.md` | `f90415eee32837ea01589a55f8eb63274b3c72ed3ef93a311af9e3bb5e41f39b` |
| `docs/plans/GATE_B_SOURCE_SELECTION.md` | `82edfe5c94b3ad6caeb7a137139c0449cc73785907fe1cdd43040ace19e38cc8` |
| `docs/plans/phase5-planning-ledger.json` | `2c9d982d6a08fb5bc19b7975f8b50d82bdf34464791230d91937258d67e350b5` |
| `scripts/validate/phase5_plan_consistency.py` | `86b1d8c693f7f48f4d9a10682bd3f0889d4ca9c87b8f38c17775bbe0d8b28a4b` |
| `docs/plans/GATE_A_BASELINE.md` | `470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4` |
| `docs/review/modules/KIN-02.md` | `4f1eadfe0e3259bb4755146aef8a35acbdaa941efd6189ab23f229e9e276c0b1` |
| `docs/review/planning/PLAN_3_3_STRUCTURAL_AUDIT.md` | `6c6d0164ec296740db2c377259f08afcf1d41d3ffb2d816a229b3ef051b64b7c` |
| `docs/review/planning/PLAN_3_5_STRUCTURAL_AUDIT.md` | `3f3cd468e56ddedb69a29cd0e6d92ab81b7364a8ca63f686a400cc76f1d31a4e` |
| `docs/decisions/0005-gate-a-approved.md` | `2078d528e8add9b01aac12f05cc69fd424f6bdd300791ab0a95d65fe1a4a7dcf` |
| `docs/decisions/0006-math-review-approved.md` | `7d93931650f91332eac8f903f50cb36c1958b8ef254ed682006d041106b83b07` |
| `docs/decisions/0007-opt-review-approved.md` | `b132d889e04f612d9375f1dc9075f195a2d31c88139b8417a716cc6bffe27ad8` |
| `data/source-manifest/manifest.json` | `ef009f1481cd1d5379c20db4feab7156d43443dc38fc58e0046c119e78f36960` |

No Gate-B approval decision exists. Decision 0005 closes Gate A and explicitly withholds production-
corpus and authoring authority. Decisions 0006/0007 approve review findings and planned deltas, not
current coverage, a production corpus or implementation.

## Severity-ranked findings

### 1. HIGH — C1-02: the status validator prints a false state and does not validate the status fact

Current governing prose and ledger facts correctly say that an independent review is required and
authorized, while an approval request is not. Plan `:6,18,1149,1588,1791`, proposal `:4,2030`,
handoff `:23-31`, and ledger `:1619-1624` agree: proposal 7 is current/unreviewed; C2-01 is resolved;
this review may be requested; approval may not.

The validator nevertheless ends a passing run with:

```text
... no review or approval request authorized, None blocked
```

That string is hard-coded at `phase5_plan_consistency.py:447-450`. It directly contradicts the
status transition the revision-3.6 correction register says was withdrawn “everywhere.” It is also
not cosmetic evidence of an otherwise complete derivation: an isolated fixture changed
`currentGateBStatus.facts.independentReviewRequiredAndAuthorized` from `true` to `false`, leaving the
six regions unchanged. The validator still exited 0 and printed the same passing line. Inspection of
`:351-450` confirms that the current revision/failed/superseded sets and each region's `mustAssert`
patterns are checked, but the binding booleans under `facts` are never compared with those expected
assertions. `blockedCorrection` is only interpolated into the success string, which is why the live
`null` becomes “None blocked.”

Thus C1-01's specific detached-number parser is repaired, but the broader claim that current status is
derived from and compared against the ledger's single fact set is false. A future fact transition can
again pass with stale region requirements, and today's passing diagnostic already reports stale
authority.

### 2. MEDIUM — C2-03: the plan's “exact” hour decomposition omits its declared sixth component

Plan §5.1 `:621-630` says “The +142.0 h decomposes exactly as” and lists five components:
120.5 + 9.0 + 9.5 + 1.5 + 1.5. It does not list `f8KeyedRecall: 0.0 h`.

That omission contradicts plan §5.3a `:684-703`, especially `:690` (“a real ledger component ...
not omitted”) and `:701` (“six components, the sixth being `f8KeyedRecall` at 0.0 h”). The ledger is
correct at `:1516-1536`, and the validator now derives all six at `:507-525,610-675`; an isolated
0→2 h F8 drift failed with the intended policy/component diagnostics. The remaining defect is the
human-facing plan table, which still presents the old five-row enumeration as exact.

The totals themselves remain correct. This finding is about complete enumeration and future drift:
the plan's principal arithmetic table should expose the same six-component contract it claims.

### 3. MEDIUM — C4-03: conditional blocker resolution is circularly labelled “at acquisition”

Plan §9.9 `:1218-1222` makes a `CONDITIONAL` source ineligible for acquisition while blocked. Its only
exception is §9.9.1's bounded **Gate-D evaluation-only fetch/install**, and plan `:1250` explicitly
states that evaluation fetching “is not acquisition.”

Proposal §7 O5/O6 `:1967-1968` instead resolves E9a/E9b with a locator-verification fetch “**at
acquisition**” and E10 with a re-attempt “**at acquisition**.” On the proposal's own taxonomy, those
sources cannot reach acquisition until the fetch resolves their blocker. The correct action class is
the already-defined Gate-D evaluation-only fetch/read; calling it acquisition collapses the exact
distinction plan §9.9.1 says must not be collapsed.

This does not authorize a Gate-B fetch—the proposal consistently forbids that elsewhere—and C4-02's
O1 correction is sound. It does leave the conditional lifecycle internally circular at the point
where those three blockers would be resolved.

## Confirmed corrections and structural re-checks

### C1-01 — PASS

Proposal `:3-20` consistently names proposal 7 / plan 3.6. Changing only the detached numbering note
from current 7 to current 5, and re-pinning the fixture's proposal hash in its handoff, fails with the
specific proposal-header and cross-region current-revision diagnostics; there are no generic hash
failures.

### C2-01 — PASS

The only KIN-02 diff is inside its Phase-5 reconciliation. Current `KIN-02.md:143-158` pins plan 3.6
and separates ownership coherently:

- F0 teaches/corrects double cover, SLERP sign/antipodal handling, integration/renormalization and the
  unrelated prompt;
- F8 keys that prompt and owns every added recall item;
- F0 adds the missing DYN-exam KIN remediation mapping; F8 persistence-checks it only;
- F8 recall carries 0.0 scheduled learner hours, while KIN-02's +0.5 h covers F0 content.

This agrees with plan `:377-395,684-703,1643-1656,1852-1865`, ledger `:13-38,1516-1536`, and the
whole-block F8 ownership approved in decisions 0006/0007. No finding, verdict or evidence elsewhere
in KIN-02 changed.

### C2-02 — PASS for validator enforcement

The ledger enumerates six components and the validator derives all six. The isolated prior-audit
mutation—F8 component and published F8 figure 0→2, component total 142→144, policy and overall total
left at 0/142—now fails. It produces the intended component-sum and policy/component diagnostics,
plus downstream total/table failures. No F8 field can drift alone under the current validator.

### C3 — PASS

Plan `:568-583` pauses both prototypes and forbids dependencies. Gate E `:1612-1633` binds every
pilot to a scratch artifact excluded from content, route, assessment, Anki, totals and commits, with
deletion/quarantine at exit. P1 creates its own disposable WebGL fixture and explicitly cannot read,
import or reactivate either paused prototype or KIN-01. P2–P5 are likewise throwaway fixtures.

### C4-02 — PASS

Proposal O1 `:1962` now records only the consultation/citation-only classification and future
eligibility; it explicitly authorizes no citation. Plan §9.8–§9.10 and proposal §§2, 8–10 otherwise
consistently reserve citation/authoring for Gate C and acquisition/ingestion/migration for Gate D.
Plan `:1218` now correctly says conditional candidates are still scored, while approval/citation/use
remain blocked.

### C9-04 — PASS

Current matrices contain 39 unique scored IDs, including D3 at proposal `:221-233`. The roll-up at
`:289-302` contains the identical set as 23 SELECT + 7 OPTIONAL + 9 CONDITIONAL; every current row's
declared status matches its roll-up and ledger bucket. Changing only A1's scored-row decision from
`SELECT` to `OPTIONAL`, with the roll-up and ledger unchanged and the fixture hash re-pinned, now
fails with both exact diagnostics:

- row A1 declares OPTIONAL but roll-up lists SELECT;
- row A1 declares OPTIONAL but ledger membership lists SELECT.

D3's eleven current cells sum to 25 and contain no gate-criterion zero. Its maintenance score of 2
remains a judgment resting on explicitly unverified cadence; no external cadence check was performed.

### STR-01 — PASS

Plan `:528-545,722-730,1643-1647` and ledger entries agree: `OPT-04B` follows `OPT-03`, `OPT-04` and
`NUM-03` and consumes the KKT repair; `OPT-05B` follows `OPT-05`, `PROB-02`, `NUM-01` and has no KKT
dependency. This matches decision 0007's distinct IFT/KKT and derivative-free additions.

### STR-02 — PASS

Plan `:942-981`, ledger `:1538-1597` and direct baseline inspection agree on five affected existing
modules: `DYN-04`, `DYN-06`, `OPT-05`, `ODE-01`, `SYM-02`. The first four have the cited current
symbol uses. `SYM-02` uses substitution `theta`; its replacement remains explicitly unsettled because
sigma already has six baseline meanings. Gate C, not this review, owns the choice.

## Totals, classification and gate order

Direct ledger sums reproduce:

- 36 new modules / 120.5 h: 31 main-route, 5 optional / 15.0 h;
- foundation 9.0 h; in-place 9.5 h; calibration 1.5 h; rescopes 1.5 h; F8 recall 0.0 h;
- added total 142.0 h; baseline 69 modules / 15 blocks / 226.0 h;
- augmented 105 modules / 20 blocks / 368.0 h;
- optional 15.0 h new + 4.5 h existing Tier-3 + 1.0 h optional boxes = 20.5 h;
- main route 368.0 − 20.5 = 347.5 h;
- 13 exams, 19 cheat sheets, 35 labs, 13 required static figures, 7 in-block additions.

The plan's gate order is A→B→C→D→E→F→G. Gate F is
F0→F1→F0b→F2→F3→F4→F5→F6→F7→F8, so repaired foundations precede `NUM-03`, and `NUM-03` precedes
`OPT-04B`. The validator independently checks all 36 proposed modules against the 105-module
canonical order and reports no optional-as-main dependency.

## Gate-A invariance

`GATE_A_BASELINE.md` hashes to the approved
`470046a5fa4036794c37434295cea67385e985ca9871c06413b964dddc1a45a4`.
`git diff --exit-code` is clean for Gate A and decisions 0005–0007. The prior structural audits are
untracked worktree evidence, so `git diff` cannot establish invariance for them; their directly
recomputed full hashes match the handoff and current plan pins. The baseline commit is an ancestor of
current HEAD. Gate A's own revision-2.1 historical ownership notes remain immutable evidence; the
current plan supersedes their batch details without reopening or rewriting Gate A.

## Disposable mutation matrix

Four independent fixtures were created under
`/private/tmp/phase5-structural-audit-36.lBhaD3/`. Proposal mutations had their dependent full hash
re-pinned in the fixture handoff. The fixture tree was deleted after the runs.

| Mutation | Expected | Actual | Verdict |
|---|---|---|---|
| Proposal numbering note current 7→5 only | C1-01 current-revision mismatch | Exact proposal-header and cross-region diagnostics; no hash failure | **PASS** |
| A1 scored-row decision SELECT→OPTIONAL only | C9-04 row/roll-up/ledger mismatch | Both exact per-ID diagnostics | **PASS** |
| F8 delta/published/component 0→2 and component total 142→144; policy/overall left 0/142 | C2-02 policy/component/sum mismatch | Intended policy and six-component diagnostics, plus downstream total failures | **PASS** |
| Ledger `independentReviewRequiredAndAuthorized: true→false` only | C1 ledger fact versus six regions | Exit 0; stale passing diagnostic unchanged | **FAIL** |

## Validator runs and stop state

Initial current-byte runs:

- `python3 scripts/validate/agent_context.py`: exit 0; 0 failures, 0 warnings.
- `python3 scripts/validate/review_integrity.py`: exit 0; 0 failures, 0 warnings.
- `python3 scripts/validate/phase5_plan_consistency.py`: exit 0; 0 failures, 0 warnings, but the
  success message contains the C1-02 false status described above.

The same three commands were rerun after this report was written with the same exit-0 summaries and
the same C1-02 false success message. The final invariance command for Gate A and decisions 0005–0007
also exited 0.

No Astro check or production build was run: no curriculum or runtime artifact was changed, and those
commands cannot falsify these structural findings. No source was fetched, acquired, installed,
ingested, pinned or externally checked. No approval was requested or recorded. No commit or push was
performed.

`docs/agent/CURRENT_HANDOFF.md` was not updated because its current write-ownership section assigns
that file to Claude and assigns this reviewer only `docs/review/**`; editing it would violate the
explicit lane boundary. The next authorized action is a planning-lane correction pass for C1-02,
C2-03 and C4-03, followed by one fresh independent structural review. No approval request is safe
before a later review passes.

Final verdict: **STRUCTURAL FAIL**.
