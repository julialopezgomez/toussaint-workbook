# Decision Record 0005 — Gate A approved (Phase 5)

Date: 2026-08-14

## Decision

The owner **approved Gate A of the Phase 5 augmentation plan at revision 2.1**, following an independent review pass.

**Gate A is closed. It is not to be reopened or repeated.**

## What was approved

Approval covers the verified baseline and its evidence, specifically:

- **Isolated committed baseline.** `git archive dd2e8717f82dfcb77aff4b8c89aba258997f87fe` built in a clean directory with `npm ci` from that commit's lockfile: 100 pages, **20,209 Pagefind words**, matching the review's independently produced figure.
- **Separately labelled worktree comparison.** The dirty working tree (100 pages, 20,218 words) is recorded as context only, never as baseline evidence. The 9-word delta is attributed to the uncommitted `RotationViz` paragraph in `KIN-01.mdx`.
- **Concept/depth inventory**, complete for all **69 modules / 308 declared concepts**, with module depth on the plan's 0–7 scale, its evidence basis, and per-concept depth left explicitly `null` (a semantic judgment reserved for the review protocol's Gate 6). Headline finding: **every module sits at depth 4; nothing reaches depth 5.**
- **Reporter status semantics and failure behaviour**: `OK` / `REPRO` / `QUEUE` / `FAIL`, with a reproduced defect never counted as a passing validation, declared write side-effects, and a non-zero exit on unexpected results (verified by synthetic test).
- **Semantic-queue treatment** of the readiness-widget and `reviewCardIds` counts: these are review queues, not automatic failures, and nothing downstream enforces a per-prerequisite or per-exercise ratio.

## Scope limits of this approval

- **This does not approve the Gate B production source corpus.** The review benchmark corpus (Ross, Gordon & Bagnell 2011; Solà 2017; *The Matrix Cookbook*) was approved separately on 2026-08-14 **as the review evidence policy only**. The Gate-B corpus — Tedrake as a *theory* source; MuJoCo/Gymnasium/Drake/PyTorch/Triton/LeRobot as *api* sources; CleanRL/Stable-Baselines3 as *implementation* sources; the PPO/SAC/DQN/DAgger/Diffusion-Policy papers as *citation* sources — **remains unapproved and is a separate decision** (plan §9.0-pre, §9.0).
- **No content authorization.** Approval of a baseline is not permission to author modules, labs, or sources. Per `docs/review/REVIEW_PROTOCOL.md:178`, review findings alone never authorize content or code changes.
- **No defect was fixed.** The 13 reproduced defects remain open and scheduled (F0 repairs; Gate D platform work).

## Editorial corrections applied with this record (plan rev 2.2)

Two non-blocking P3 items in the §1 executive new-block table, both already correct in §5.1 and §17.4:

- UAC: 6 → **5 modules**
- SIM: 5 → **6 modules**

Applied opportunistically as instructed. Gate A was not reopened to make them.

## Artifacts

| Artifact | Revision | sha256 |
|---|---|---|
| `docs/plans/PHASE5_AUGMENTATION_PLAN.md` | 2.2 | `412b807536da6d90b1063ad800aadf5435a6e05eabe6e3cfcd6ea65ac308f2f3` |
| `docs/plans/GATE_A_BASELINE.md` | report rev 2 | approved as-is at plan rev 2.1 |
| `docs/plans/gate-a-concept-depth-inventory.json` | committed-baseline analysis | `d29a5865c17af40c520f3dbef18f10ff8326bdc48a1ad63c7353c811e94e9bce` |
| `scripts/validate/gate_a_baseline.py` | — | `f1bf926bc18301eb9f4d664d8f8bc027b2dc4fa4b6fc4343f4f5a44a1874bced` |

`docs/review/**` is review-owned and was not modified by the planning process. The review subsequently re-pinned its records to plan revision 2.2.

## Next step (not started)

**Gate B — source shortlist and selection.** Requires separate owner approval before any authoring. Not begun; this session stopped here at the owner's instruction.
