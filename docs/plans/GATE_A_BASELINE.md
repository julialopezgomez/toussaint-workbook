# Gate A — Verified baseline & concept/depth inventory

**Report revision 2 — 2026-08-14** (supersedes revision 1 of the same date)
**Plan under verification:** [`PHASE5_AUGMENTATION_PLAN.md`](./PHASE5_AUGMENTATION_PLAN.md) rev 2.1
**Status: PASSED, awaiting approval. Gate B NOT started. No module, lab, or source content authored.**

**Benchmark corpus approved 2026-08-14** (Ross et al., Solà, Matrix Cookbook). The **Gate-B production corpus remains unapproved** and is a separate decision — see plan §9.0-pre.

## 0. Evidence provenance — two trees, never conflated

Revision 1 of this report conflated them. This revision does not. **All baseline claims below are from the isolated committed tree.**

| | **A — Committed Phase 4 baseline** | **B — Current worktree** |
|---|---|---|
| Source | `git archive dd2e8717f82dfcb77aff4b8c89aba258997f87fe` → clean dir, `npm ci` from that commit's lockfile | working tree in place |
| State | clean; no uncommitted work | **dirty, 10 changed paths** (user-owned) |
| Dependencies | 403 packages; **no `three`** | includes `three@0.185.1` |
| Build | 100 pages · **20,209 Pagefind words** | 100 pages · **20,218 Pagefind words** |
| `astro check` | 0 errors, 0 warnings, **103 hints** | 0 errors, 0 warnings, **103 hints** |
| Reporter | 13 OK · 13 REPRO · 4 QUEUE · 0 FAIL | 13 OK · 13 REPRO · 4 QUEUE · 0 FAIL |
| Inventory sha256 | `d29a5865…` | `778a910e…` |
| **Role** | **authoritative baseline evidence** | context only; excluded from baseline claims per `REVIEW_PROTOCOL.md:13` |

**The 9-word delta is fully explained**: the uncommitted `RotationViz` paragraph in `KIN-01.mdx`. Tree A reproduces the review's independently-built figure of **20,209 words exactly**, which cross-validates both measurements.

Reproduce tree A:
```
git archive dd2e8717f82dfcb77aff4b8c89aba258997f87fe | tar -x -C <dir>
cd <dir> && npm ci && npm run build
.venv/bin/python scripts/validate/gate_a_baseline.py --tree <dir> --no-write
```

## 1. Artifacts and hashes

| Artifact | sha256 |
|---|---|
| `docs/plans/PHASE5_AUGMENTATION_PLAN.md` (rev 2.1) | `566f58c4887adf3237210d217ac8c934525f4145214d34ba2da4d87dc1ad9bea` |
| `docs/plans/gate-a-concept-depth-inventory.json` | `d29a5865c17af40c520f3dbef18f10ff8326bdc48a1ad63c7353c811e94e9bce` |
| `scripts/validate/gate_a_baseline.py` | `f1bf926bc18301eb9f4d664d8f8bc027b2dc4fa4b6fc4343f4f5a44a1874bced` |

The inventory hash is the **tree-A (committed baseline)** analysis, written into the working repo via `--out`. Its `treePath`/`commit`/`label` fields record that provenance internally.

## 2. Concept/depth inventory — now complete, and renamed

Renamed `gate-a-depth-inventory.json` → **`gate-a-concept-depth-inventory.json`**, and completed. Revision 1 promised a concept/depth inventory and shipped metadata only; that gap is closed.

**Now contains, for all 69 modules:** declared concepts (**308 total**, every module declares ≥1), objectives, a **module depth value on the plan's 0–7 scale** with its evidence basis, and the per-module evidence counts that produced it (exercises by type, display-math blocks, code fences, Python fences, figures, readiness checks, notation entries, source IDs).

**Headline result — the plan's central thesis is now quantified rather than asserted:**

> **All 69 modules sit at depth 4** ("practised by written exercise"). Distribution: `{4: 69}`. **Nothing reaches depth 5** ("implemented in executable code"). No `labs/` tree exists, and the single `code` exercise has no runner.

That is the 4→5 gap the entire augmentation targets, measured across the whole corpus.

**Two limits stated in the artifact itself, not just here:**

- **Module depth is a mechanically-derived ceiling**, not a semantic judgment. Individual concepts inside a module may sit lower; none can sit higher.
- **Per-concept depth is deliberately `null`**, each with a machine-readable reason. Judging 308 concepts individually means reading each module against its source — that is the review protocol's Gate 6, not this reporter's job. Emitting invented per-concept numbers would be exactly the overclaim this pass exists to remove.

## 3. Reporter honesty

| Correction | What changed |
|---|---|
| Claimed read-only, but wrote | Docstring now leads with **"SIDE EFFECTS — this script is NOT read-only"**, names the one artifact it writes, and adds `--no-write` |
| FAIL exited 0 | **Exits 1 on any FAIL** (verified by synthetic test: deleting `SYM-04.mdx` from a throwaway copy → 4 FAIL, exit 1). `2` for bad invocation |
| Defects counted as PASS | Four statuses replace two. **`REPRO`** = a known defect reproduced — evidence the baseline is understood, explicitly **not** success and **not** a fix; each names the plan section that owns it. **`OK`** = a genuine invariant. Summary line prints all four with their meanings |
| Baseline vs worktree conflated | `--tree` selects the checkout; header prints path, commit, dirty/clean, changed-path count |

Tree A totals: **13 OK, 13 REPRO, 4 QUEUE, 0 FAIL**. Thirteen of thirty are reproduced defects — the corpus is well-understood, not healthy.

## 4. QUEUE checks — review queues, not failures

Reclassified per your instruction; the plan's §15 rules were softened to match, so nothing downstream enforces a ratio.

| Queue | Measurement | What it does **not** mean |
|---|---|---|
| `QUEUE-READINESS` | 32/67 modules with prerequisites have fewer `<ReadinessCheck>` widgets than prerequisite IDs | **Not a defect count.** One well-chosen check can cover several prerequisites. §15 now reports modules whose prerequisites are not *named* in their readiness section and queues them for semantic reading — it does **not** require one widget per prerequisite |
| `QUEUE-ANKI-EXPORT` | 322/361 exercises (89%) have no `reviewCardIds` | Measures **exercise→Anki export sparsity only**. Notation cards (208 exported) and in-module retrieval prompts are separate surfaces; this number alone never establishes weak recall |
| `QUEUE-COVERAGE-CLAIM` | 2 modules claim "full note": `KIN-02`, `DYN-05` | `KIN-02` is a review-confirmed overclaim. **`DYN-05` is unaudited — to check, not a finding** |
| `QUEUE-NOTATION-EMPTY` | 5 modules declare zero notation | Observation for the notation registry (§8) |

## 5. Baseline confirmed (tree A)

69 modules / 15 blocks · **226.0 h exactly** · 361 questions = 361 solutions = 361 `<ExerciseCard>` refs, three-way with zero orphans · exactly 3 hints on every exercise · 14 cheat sheets · 8 milestones · 100 pages · no cycles, no dangling prerequisite targets.

## 6. Defects reproduced (tree A) — 13

`D-01` OPT-06 forward prerequisite (2 violations) · `D-01b`/`D-01c` the PROB-before-OPT fix verified to give **0** violations with no PROB→OPT edge · `D-02` 6 notation collisions · `D-02b` SYM-03 symbol/meaning mismatch · `D-03` unmanifested `julia-report` · `D-04` print page claims exercises excluded, ships **367** · `D-05` mcq/multi-select schema-only · `D-06` `code` type has no runner · `D-07` solution lock UI-only · `D-08` 103 `ts(6385)` hints · `MS-02` no block milestone covers any of the 10 PLAN/MANIP/SYM modules · `MS-03` MANIP in **no** milestone at all · `MS-04` DYN-EXAM claims KIN coverage with no KIN remediation entry · `DEPTH-01` depth ceiling 4.

All are **pre-existing at the committed baseline** — none introduced by the uncommitted work.

## 7. Corrections carried into plan rev 2.1

**Calibration reconciliation, resolved:**

- **KIN02-06 re-routed.** Rev 2.0 proposed routing quaternion↔matrix conversion and vector application to KIN-01. **I checked KIN-01: it contains neither** — its only quaternion content is a forward pointer to KIN-02 (`KIN-01.mdx:80`) plus the Rodrigues/angular-velocity appendix. Routing to a module that lacks the material is precisely the silent-omission failure §9.0b forbids. **Now taught compactly in KIN-02** (one formula each).
  *Open sub-item for F0:* KIN-01 cites `quaternions` p3-4 for that appendix while the review places it on p5 of a 5-page note. One is off by a page. Flagged for a page check during the repair rather than guessed at here.
- **KIN02-08 owned.** The sigmoid-analogy retrieval prompt is an explicit **F0 repair**: rewrite prompt 3 as direct keyed recall, plus keyed recall for `q ~ −q`, inverse/product order, exp/log domains, normalization, SLERP sign choice, frame convention. Card *volume* stays an F8 question; the prompt rewrite does not.
- **RLN02-04 split into three dispositions.** (a) feature/constraint learning → **routed to RLEARN-07**, which genuinely develops it; (b) DTW → **optional reference**, passes all six §9.0b conditions; (c) VAE motion-planning example → **intentionally out of scope, with a condition**: the substitution is sound, but it must be *stated*, because that example links VAEs to sampling distributions for planning — adjacent to PLAN-05/ACC-04. RLEARN-02 records the omission and cross-references PLAN-05.
- **F8 acceptance criteria added** — six measurable exit conditions (≥3 answered recall items per repaired module; ≥3 exported cards; cheat sheet must contain every identity group the module claims incl. Woodbury; named exam items; three named static figures). Notably: **an interactive may not close a figure finding** — static figures are the acceptance bar.

**Stale revision-1 text removed:** "seven new modules inside existing blocks" → five (+2 relocated); UAC 6→5; SIM 5→6; repairs F1→**F0**; "32 new modules" → 33 in Gate C and §14; every description of ACC-05 as the main-route vector-environment module with a required CPU half → **SIM-06**.

## 8. What explicitly did NOT happen

- No module, exercise, solution, cheat sheet, or milestone created or edited. `package.json` untouched.
- **No defect fixed.** All 13 are reproduced and scheduled (F0 repairs, Gate D platform work).
- `docs/review/**` **not modified** — read-only, per your instruction that the review process owns those records. Reconciliation lives in plan §17, which references them.
- The uncommitted worktree (`three`, `RotationViz`, `GridWorldRL`, three modified planning docs) untouched.
- **Gate B not started.** No source added to any manifest. Benchmark approval does not authorize authoring against the production corpus.

## 9. Review-record synchronisation (read, not written)

`docs/review/**` was updated by the review process at 21:13–21:16, **after** I read it at ~21:05 and **after** rev 2.0 was pinned. I re-read the updated records; I did not modify them.

- **`REVIEW_INDEX.md` pins plan revision 2.0 at sha256 `2747ef91cb9be457a69cb26564ffc8b6ab6147a7c1b7010d728850c4e460f902`.** This report supersedes that with **rev 2.1 = `566f58c4887adf3237210d217ac8c934525f4145214d34ba2da4d87dc1ad9bea`**, so the review will need to re-pin.
- The review's own Gate A status lists exactly the four corrections you gave me (dirty-tree isolation, missing concept/depth classifications, residual revision-1 references, mechanical counts as queues). **All four are addressed in this revision.**
- **Independent agreement on KIN02-06:** `KIN-02.md:150` now records "committed `KIN-01` teaches rotation matrices/Rodrigues but not quaternion↔matrix conversion or quaternion vector application. A route to material that is not there is not coverage." I reached the same conclusion by checking `KIN-01` directly, before re-reading that line. Two independent paths, same verdict.
- **Open items the updated records list are now closed in rev 2.1:** the VAE motion-planning example has an explicit disposition (§17.2, RLN02-04c); F8 acceptance criteria name the required diagrams, keyed-recall targets, and generative-policy assessment, and quantify M02B-06/07.

No disposition in rev 2.1 contradicts the updated records.

## 10. Recommended next step

Approve corrected Gate A. The next decision is the **Gate-B production corpus** (`sources.json` v2) — Tedrake as a theory source, the tooling docs as API sources, CleanRL/SB3 as implementation sources, the algorithm papers as citation sources — which is separate from the now-approved benchmark.
