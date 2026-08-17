# Gate B — Production source selection proposal

**Proposal revision 8 — 2026-08-16.** Proposal revisions 1–4 were each independently reviewed and each **FAILED**; §0.3–§0.6 list what was wrong and where each item is fixed. **Proposal revision 5 was superseded before review** (§0.7). **Proposal revision 6 FAILED the independent structural audit of plan revision 3.5** (`docs/review/planning/PLAN_3_5_STRUCTURAL_AUDIT.md`, SHA-256 `3f3cd468e56ddedb69a29cd0e6d92ab81b7364a8ca63f686a400cc76f1d31a4e`, verdict **STRUCTURAL FAIL**) — §0.8 lists what it got wrong. **Proposal revision 7 FAILED the independent structural audit of plan revision 3.6** (`docs/review/planning/PLAN_3_6_STRUCTURAL_AUDIT.md`, SHA-256 `a42cb26edc93219a0c82c8e5abc84878cb7ded0530528a2d7c518bd84d694b89`, verdict **STRUCTURAL FAIL**) — §0.9 lists what it got wrong.
**Status:** **NOT APPROVED. NOT REVIEWED. NOT READY FOR APPROVAL.** **Proposal revision 8 is the current, corrected pass**, answering every blocking finding of the plan-3.6 structural audit. **Proposal revision 5 was superseded before review** — not on a review verdict, but because a pre-review inspection found three defects (§0.7). **Proposal revision 6 FAILED** the plan-3.5 audit (§0.8). **Proposal revision 7 FAILED** the plan-3.6 audit, on findings C1-02, C2-03 and C4-03 (§0.9). **Correction C2-01 is RESOLVED**: `docs/review/modules/KIN-02.md`'s Phase-5 reconciliation was re-pinned and corrected under the owner's narrow authorization, so **no review-lane blocker remains. A fresh independent structural review is now the required next action and may be requested; no approval may be requested until that review passes**, and none has been requested. Nothing here is approved. No source has been acquired, fetched or added to any manifest. **Gate B has not started and is not approved; Group A is not approved and not started.**

> **A corrected proposal is not a reviewed proposal.** Four consecutive revisions were reported complete and then failed review; a fifth was reported complete and was then found defective before review even began; two more were reported complete and each then failed an independent structural audit. **Seven revisions, none passed.** Everything in §0.5 through §0.9 is a **claim about what that revision changed**, not a finding that the change is correct. Treat this document as material to falsify.

> **Two independent numbering schemes — do not conflate them.** This document has its own
> **proposal revision** number (currently **8**). The plan has its own **plan revision** number
> (currently **3.7**). They are unrelated: proposal revision 8 is pinned to plan revision 3.7, and
> a later proposal revision could still be pinned to plan revision 3.7, or vice versa. Wherever
> this document says "revision" without a qualifier, read the qualifier from the noun it modifies.
> *(Corrected at proposal revision 7 — audit finding C1-01. This note used to name a revision that
> is no longer current as the current one, while the header declared a different number: two live
> statements in one document disagreeing, with the exact numbers recorded in §0.8. `phase5_plan_consistency.py`
> now parses this `number (currently N)` form as a current-revision claim, so the contradiction
> fails the check instead of passing it — the plan-3.6 audit re-ran that mutation and confirmed it.)*

**Pinned to:** `docs/plans/PHASE5_AUGMENTATION_PLAN.md` **plan revision 3.7**, SHA-256
`e298acfac750f378d0557f69233f8f8d0094eaaf0f37fb1d3f8f2de86ea149ea`
**Baseline commit:** `dd2e8717f82dfcb77aff4b8c89aba258997f87fe`
**Authority:** decisions `0005`, `0006`, `0007`; plan §9.2 (rubric), §9.3 (schema), §9.4 (coverage audit), §9.6 (deliverable), §9.7 (foundation needs), §9.8 (approval boundary), §13 (Gate B acceptance).

> **What approving this would do — corrected at proposal revision 5 (audit finding C4-01, CRITICAL).** It would permit **nothing to be fetched, downloaded, pinned, populated, or migrated.** Gate B produces and approves **evaluation and planning records only**: scores, dispositions, coverage records, locator/licence/version findings, notation conflicts, and the **non-executed** `sources.json` v2 draft in §5. **Acquisition, `sources.json` population and `manifest.json` migration are Gate-D implementation work** (plan §9.8, §14.1) that no Gate-B approval advances — **including for Group A**. It also does not authorize any lesson, exercise, solution, cheat sheet, exam, lab, or code (Gate C), any dependency install (Gate D), or any reproduction of source prose or figures.
>
> *Through proposal revision 4 this line read: approval "permits **acquisition, pinning into `sources.json` v2**, and citation at the approved role". That granted ingestion authority the governing boundary withholds, and contradicted §7 O10b's own statement that the migration is Gate-D work.*

---

## 0. Boundaries and what changed

### 0.1 Standing boundaries

1. **The review benchmark corpus is not this corpus.** It is a completeness lens for reviewing existing content (plan §9.0-pre). Four sources appear in both; the role is recorded twice, never merged.
2. **API documentation may never generate a completeness finding** (plan §9.0).
3. **Relevance-scoped completeness governs** (plan §9.0b): every relevant section is logged and disposed; omission is legitimate, silence is not.
4. **No paid tier, subscription, paid account, or API key.** Core labs CPU-first. The RTX 5090 is a **project-validation dependency, never a learner prerequisite** (plan §12.4).
5. **Reuse is separate from citation** (plan §9.8). Most of this corpus is **consultation-and-citation only**.

### 0.2 Verification method

Every Group-A source, and every locator marked **verified 2026-08-15**, was checked in this session by fetching the official page or the PDF itself and reading its table of contents, section numbering, or licence text. Where a claim could not be verified, the row says so and the source stays `CONDITIONAL` **with the specific unverified item named**.

### 0.3 What proposal revision 1 got wrong (fixed in proposal revision 2)

| # | Error in revision 1 | Correction |
|---|---|---|
| 1 | Claimed **Martins & Ning ch.7 covers CMA-ES**. It does not — §§7.1–7.8 are method selection, classification, Nelder–Mead, generalized pattern search, DIRECT, genetic algorithms, particle swarm. A full-text search returns **0 occurrences** of "CMA-ES" or "covariance matrix adaptation" | A1 ch.7 keeps method selection, Nelder–Mead, pattern search and DIRECT/GA/PSO boundaries. **A7 (Hansen) is the sole CMA-ES authority.** A1 ch.4 is retained for Wolfe/BFGS — verified: **§4.3.2 Strong Wolfe Conditions**, and the **curvature condition** appears in §4.4.4 Quasi-Newton Methods |
| 2 | Axler PDF dated **13 July 2026**; called "the only explicitly open-licensed source in this entire proposal" | Corrected to **13 August 2026**. The superlative is removed and false — MuJoCo docs are CC BY 4.0, Drake BSD-3-Clause, Gymnasium MIT, MuJoCo code Apache-2.0 |
| 3 | A5's IFT sections left unpinned, deferred to ingestion | **Pinned now** (§A5) from the v4 PDF. A5 does **not** supply the active-set failure mode; **Barratt (A5b) is added** as the exact authority |
| 4 | DQN treated as a paywall blocker needing an owner decision | Replaced with the **official public DeepMind PDF**, verified. Citation-only: the PDF carries "Macmillan Publishers Limited. All rights reserved ©2015" |
| 5 | SAC locator unresolved between two papers | **ICML 2018 PMLR v80 pp. 1861–1870** is the primary citation, verified. "Algorithms and Applications" added **only if** automatic temperature tuning is taught |
| 6 | Said paid books are "not citable in a public workbook" | **Inaccurate.** Corrected: they are **not eligible as learner-required teaching sources under this project's availability gate** (§9.2 criterion 1). Citing a paid book is fine; requiring learners to buy one is not |
| 7 | Licences left as open items | **Resolved and recorded:** Drake BSD-3-Clause, Gymnasium MIT, MuJoCo Apache-2.0 (code) + CC BY 4.0 (docs), Menagerie **per-model `LICENSE` files** |
| 8 | No numeric §9.2 scores; no `sources.json` v2 draft; incomplete §9.4 coverage matrix; no per-source notation conflicts; claimed "none of these blocks approving this proposal" | **§2 scores all candidates numerically; §5 is the filled schema draft; §6 is the complete coverage-matrix skeleton; §4 is the notation-conflict register.** The "nothing blocks approval" claim is withdrawn — §7 states exactly which items block which source |

### 0.4 What proposal revision 2 got wrong (fixed in proposal revision 3)

| # | Finding | Correction |
|---|---|---|
| 1 | **Proposal-revision and plan-revision numbers were conflated**, and the document was pinned to a plan revision that has since been superseded | Header now separates the two schemes explicitly and pins **plan revision 3.2 / `514249b1…`** |
| 2 | The **`sources.json` v2 draft was not complete** — the 13 migrated PDFs were elided with "...", several selected sources were omitted, no v1→v2 field mapping existed, and `requiresAccount` / conditional metadata were missing | **§5 now enumerates all 13 PDFs with real `source_id`s, page counts and SHA-256 prefixes, every selected and conditional source, an explicit v1→v2 field-mapping table, and `requiresAccount` / `conditional` / `blocker` metadata** |
| 3 | The **coverage skeleton deferred documentation-page rows to Gate C** and lacked the plan-required columns | **§6 now carries all four required columns and enumerates the documentation rows** |
| 4 | Claimed Tedrake was **"33 chapters"** | **Wrong.** Underactuated is 21 chapters **+ appendices A–E**, Robotic Manipulation is 12 chapters: **38 source units** under the one-unit-per-chapter-or-appendix rule now stated in §6.5 |
| 5 | The **scoring contract was broken**: availability folded in account status, and role fit demanded "exactly one role" | Fixed in plan §9.2 and restated in §2; **A1's and C10's scores are revised accordingly** |
| 6 | **`CONDITIONAL` was never defined**, and read as a soft approval | **§2.6 defines it as not approved and not citable** (plan §9.9), with a named blocker and activation condition for **every** conditional source including C9, C10, E4b and Menagerie |
| 7 | The **Barratt claim was overstated** — Assumption 3 was presented as directly being the active-set failure mode | **§3.1 A5b narrowed:** Assumption 3 *is* strict complementarity; the connection to weakly-active constraints and active-set boundaries is an **inference** the workbook must make and label; **Theorem 3.1's separate nonsingular-Jacobian requirement is retained as an independent condition** |
| 8 | **Group-A partial approval scope was not bounded** | **§10.1 states what it would and would not authorize**, mirroring plan §9.10 |

### 0.5 What proposal revision 3 got wrong (fixed in proposal revision 4)

**Revision 3 claimed §5 was "the filled schema draft", §6 "the complete coverage-matrix skeleton", and that every open item was named. The review found all three claims overstated.** Each row below states the defect and the fix. **None of these fixes has been independently verified.**

| # | Finding against proposal revision 3 | Correction in proposal revision 4 |
|---|---|---|
| 1 | **`sources.json` v2 was not executable.** All 13 PDF SHA-256 values were **truncated with `…`**; the retained v1 fields (`relativePath`, `pdfMetadata`, `embeddedToc`, `extraction`) appeared in the §5.1 mapping table but in **no actual entry**; **E9a, E9b and E10 had no entry at all** despite being scored and dispositioned; `cost`, `citationUnits` and module mapping were missing from most entries; `julia-report` was a four-field stub | **§5 is rewritten as a complete, executable draft.** All 13 PDFs carry their **full 64-hex `sha256`** and every retained v1 field. **Every selected and conditional source has an entry, including E9a, E9b and E10.** Every entry carries `cost`, `requiresAccount`, `conditional`, `license`/`licenseNote`, `citationUnits`, `roles`, `reuseStatus` and `modules`. `julia-report` is complete. §5.3 states what the draft does **not** contain |
| 2 | **The coverage matrix was summarized, not materialized.** §6.5 asserted "the matrix reproduces 38 rows" **without writing them**; §6.1–§6.4 carried **two columns**, not the four plan §9.4 requires | **§6 materializes every row.** All four columns — covering module(s) · disposition · reason · notation conflicts introduced — appear on **every** row, and **all 38 Tedrake units are instantiated individually** (§6.5) rather than asserted as a total |
| 3 | **The documentation row total was wrong: 41.** The figure summed only C1–C8 and silently dropped the C9, C10 and C11 rows the same table listed | **56.** 15+8+6+6+2+1+1+2+6+6+3 = **56**, arithmetic shown in §6.7 and machine-checked |
| 4 | **A1, A2 and A3 row counts were wrong.** A1 "13 + 22"; A2 "14" against a 12-row table that merged appendices A–C; A3 "13" against a table merging §3A–3E and ch.5–6 | **A1 = 34, A2 = 14, A3 = 19**, each derived from the enumerated rows in §6.1–§6.3 rather than asserted ahead of them |
| 5 | **The score/status contract was broken.** The band said "≥23 approved · 17–22 conditional", yet **ten sources scoring 26–28 were labelled `CONDITIONAL` or `OPTIONAL`.** `CONDITIONAL` was also used for two different things — a genuine unknown, and mere optionality | **Plan §9.2 now separates eligibility (score) from status (§9.9 taxonomy)**, and §2.6b applies it. **`OPTIONAL` is a third state**: fully evaluated, not proposed by default |
| 6 | **C7 MuJoCo Playground was `CONDITIONAL` on "licence and role unconfirmed" — both were known.** The repository is **Apache-2.0** and the plan already assigns it a `SIM-06` reference role. C11 JAX carried "no blocker beyond ACC-05 being Tier 3", which is not a blocker | **C7 and C11 are `OPTIONAL`**, with licence and role recorded. Neither has a blocker, because neither ever had one. **Optionality is not a blocker** (plan §9.9) |
| 7 | **Blockers requiring a fetch or install had no bounded way to be resolved**, so they could sit open indefinitely or be cleared by assertion | **Plan §9.9.1 defines evaluation-only fetching**: one named blocker, Gate D only, disposable scratch environment, nothing committed, no authoring, a cost ceiling, and a stated `ifUnresolved` outcome. §7 records the ceiling per open item |
| 8 | **CleanRL's SAC file was named `sac.py`.** CleanRL has no such file | **`sac_continuous_action.py`** (§6.8, §5). `dqn.py` and `ppo.py` are unchanged |
| 9 | **§5.2 claimed "exactly three fields" carry `TBD-at-acquisition` and that everything needed is present "for every source"** — both false once E9a/E9b/E10 and the missing fields are counted | **Completeness claims removed and replaced with §5.3's explicit list** of what remains unpinned, which source it affects, and whether it blocks |

**Retained from proposal revision 3 because the review confirmed them, and re-stated here so a later pass does not "correct" them back:** the Barratt Assumption-3 / Theorem-3.1 two-condition reading and the labelled workbook inference (§3.1 A5b); Blondel & Roulet v4's pinned IFT page range and its verified *gap* (§3.1 A5); Martins & Ning ch.7 containing **no** CMA-ES, with Hansen as the sole authority (§0.3 row 1, §3.1 A7); Axler 4e CC BY-NC with the **13 August 2026** PDF date (§3.1 A3); the DQN official DeepMind PDF and its all-rights-reserved terms; the SAC **PMLR v80 pp. 1861–1870** primary locator; and the resolved licences — Drake **BSD-3-Clause**, Gymnasium **MIT**, MuJoCo **Apache-2.0** code + **CC BY 4.0** docs, Menagerie **per-model**.

---

### 0.6 What proposal revision 4 got wrong (fixed in this revision)

**Proposal revision 4 failed an independent STRUCTURAL audit** (`docs/review/planning/PLAN_3_3_STRUCTURAL_AUDIT.md`). Its C1 and C3 items passed; **C2, C4, C9 and a sampled structural item failed.** Only the proposal-side defects are listed here; the plan-side ones are recorded in plan revision 3.4's history row.

| # | Finding against proposal revision 4 | Correction in proposal revision 5 |
|---|---|---|
| 1 | **CRITICAL — C4-01: the proposal granted Gate B source-ingestion authority.** The header said approval "permits **acquisition, pinning into `sources.json` v2**, and citation at the approved role", and §10.1 prohibited a populated `sources.json` only **"beyond the approved Group-A entries"** — affirmatively authorizing population of the Group-A rows. *(This row quotes the wording audit finding C4-01 required removed; both quoted clauses are gone from the normative text.)* Both contradicted §7 O10b's own statement that the `manifest.json` → `sources.json` migration is **Gate-D** work | **Both clauses removed.** The header now states that approval permits **nothing to be fetched, downloaded, pinned, populated or migrated**; §10.1's Group-A exception is **deleted**. Gate B produces **evaluation and planning records only**. Mirrors plan §9.8 / §9.10 as corrected at plan revision 3.4 |
| 2 | The status roll-up in §2.6b claimed every count "is recomputed from the tables above", which was **false** — the validator compared three printed counts with three ledger constants and never parsed membership | **The claim is now true.** `phase5_plan_consistency.py` parses the roll-up's **source-ID membership** and compares it set-for-set against the ledger, so moving a source between `SELECT` and `OPTIONAL` fails even with every count preserved |
| 3 | The coverage matrix was validated by **row count only**, so a duplicated unit replacing a required one passed | **Unit identities are now checked** for uniqueness within each source section and for membership against the 38 required Tedrake units |

**What "at acquisition" means in this document, stated once so it cannot be misread as a Gate-B activity.** Several fields below say a value is "recorded at acquisition" or "pinned at acquisition". **Acquisition is Gate D.** Those phrases describe *when a later gate will fill a field*, never something a Gate-B approval performs or permits. No approval recorded on this document fetches, pins, or populates anything.

**And it is never how a `CONDITIONAL` blocker is resolved** *(new at proposal revision 8, audit finding C4-03)*. The phrase above is correct only for an **unblocked** `SELECT` or `OPTIONAL` field a later Gate D will simply fill — a `gitRef`, an arXiv version suffix. A `CONDITIONAL` source is **ineligible for acquisition while its blocker stands** (plan §9.9), so its blocker cannot be resolved at an event the resolution is itself a precondition for. **The one permitted resolving action is plan §9.9.1's bounded, evaluation-only Gate-D fetch/read/install**, which commits nothing and *is not acquisition*. Every activation condition, resolution ceiling and open-item resolution cell for a conditional source below names that route; `phase5_plan_consistency.py` sweeps §2.6, the §5 draft and §7 and fails on any that does not.

### 0.7 What proposal revision 5 got wrong (fixed in this revision)

**Proposal revision 5 was never independently reviewed.** It was superseded before review, after a direct pre-review inspection of the plan-3.4 / proposal-5 pair found three remaining defects. **That is not a review verdict**, and nothing in revision 5 or revision 6 has been independently confirmed.

| # | Finding against proposal revision 5 | Correction in proposal revision 6 |
|---|---|---|
| 1 | **C9 — the scored-source roll-up did not match the scored matrices.** §2's matrices carried **38** scored rows, while §2.6b published **39** "total scored sources", because **MuJoCo Menagerie appeared in the `CONDITIONAL` roll-up with no scored matrix row at all.** The validator compared the roll-up against ledger constants and the ledger against itself, so a roll-up entry with no scored row was invisible | **Menagerie is scored.** It has a `sources.json` v2 draft entry (§5), a recorded `case-study` role, named modules (`SIM-02`, `SIM-05`) and a per-model licence blocker, so it is a **proposed source that was never scored** — the honest fix is to score it, not to quietly drop it from the roll-up. It is now **`D3`** in §2.4, scored **25/33** against the same eleven criteria, status **`CONDITIONAL`** on the same per-model licence blocker. **§2's scored set and §2.6b's roll-up union are now the same 39 IDs**, and `phase5_plan_consistency.py` enforces set equality, one scored row per roll-up ID, one roll-up status per scored row, and a printed total equal to both cardinalities |
| 2 | **C1 — current-status regression in the plan.** The plan header was correct, but plan §13's Gate B block and §16 still described **proposal revision 4** as the current, unreviewed proposal — a revision that had already **failed** review | **Fixed plan-side at plan revision 3.5** (§13, §16, and a new current-status paragraph in §9.6), and mirrored here. Every current-status statement now derives from one recorded fact set, and the validator **derives and compares** that status across the plan header, plan §9.6, plan §13, plan §16, this document's header, the ledger and the handoff rather than matching a stale-phrase list |
| 3 | **C4 — plan §9.9's taxonomy still contradicted plan §9.8.** The status table answered "Acquirable? **Yes, on approval**" for `SELECT` and "Yes … once opted in" for `OPTIONAL`, while §9.8 bound Gate-B approval to move no bytes and authorize no acquisition | **Fixed at plan revision 3.5.** §9.9's table now separates **Gate-B evaluation status**, **future eligibility for Gate-D acquisition**, and **future eligibility for Gate-C citation/authoring**, and states bindingly that **no Gate-B or Group-A approval authorizes acquisition, fetching, downloading, pinning, `sources.json` population, manifest migration, ingestion, citation in production content, or authoring.** §2's step-2 status table below is realigned to the same three questions |

**Deliberately not addressed at that revision, and still open:** **C5–C8** (external-source claims, §§5–8); the two unfetched papers **E9a/E9b** (§7 O5); and the **Underactuated appendix titles** (§7 O11).

### 0.8 What proposal revision 6 got wrong (fixed in this revision)

**Proposal revision 6 and plan revision 3.5 received an independent STRUCTURAL FAIL**, recorded at `docs/review/planning/PLAN_3_5_STRUCTURAL_AUDIT.md` (SHA-256 `3f3cd468e56ddedb69a29cd0e6d92ab81b7364a8ca63f686a400cc76f1d31a4e`). That audit **passed** C3, STR-01, STR-02, the totals and route classification, the gate and prerequisite order, and Gate-A invariance; it **failed** C1, C2, C4 and C9. Only the proposal-side defects are listed here; the plan-side ones are in plan revision 3.6's history row. **None of these fixes has been independently verified.**

| # | Finding against proposal revision 6 | Correction in proposal revision 7 |
|---|---|---|
| 1 | **HIGH — C1-01: this document contradicted itself about its own revision number.** The header declared **revision 6**, current and unreviewed, while the live numbering note said the **proposal revision** number was "**currently 5**". Neither statement was labelled historical. The status validator exited 0 because its revision-token regex required a digit immediately after "proposal revision" and could not see `number (currently 5)` | **The note now says 7**, and the whole document is at **proposal revision 7**. The validator parses the detached `number (currently N)` form and classifies it as a **current-revision claim**, so a header/note disagreement now fails the derived cross-region comparison rather than slipping through it |
| 2 | **HIGH — C4-02: §7 O1 still granted citation authority at Gate B.** It said approving A1/A4 "**approves citation**, not copying" — current open-item text, not correction history — contradicting plan §9.8/§9.9 and this document's own §9 and header, which reserve production citation for Gate C | **§7 O1 rewritten.** A Gate-B approval **records the `consultation-and-citation-only` classification and the future eligibility that follows, and nothing more.** It approves, performs and authorizes no citation. The `reuseStatus` field is noted as written at **Gate D**, when `sources.json` is populated — not here |
| 3 | **HIGH — C9-04: a scored row's status could disagree with the roll-up undetected.** The validator confirmed each decision cell named exactly one status, then compared the **roll-up lists** with the ledger. It never recorded the status parsed from each row, so changing A1's scored-row decision `SELECT`→`OPTIONAL` — leaving §2.6b and the ledger untouched — exited 0. That falsified §2.6b's own claim that a matrix status disagreeing with the roll-up fails the check | **The claim is now true.** Each scored row's decision is recorded **by source ID** and compared against both the §2.6b bucket and ledger `gateBProposal.statusMembership`, with an exact per-ID diagnostic naming the row status, the roll-up bucket and the ledger bucket. The existing scored-set / roll-up-union checks are unchanged |
| 4 | **MEDIUM — C2-02 (plan-side, mirrored here): the six-component F8 hour check did not exist.** Plan §1 claimed `phase5_plan_consistency.py` checked the six-component `addedHours` enumeration; it recomputed from five and never read `f8KeyedRecall`, `addedHoursComponents` or `published.f8KeyedRecallHours`, so raising the F8 component to 2.0 h passed silently | **Fixed at plan revision 3.6.** All six components are derived and cross-checked, including `hourEstimationMethod.keyedRecallHourPolicy.scheduledLearnerHours`. **The 0.0-hour policy for F8 keyed recall is unchanged**, and the totals it feeds — 142.0 h added, 368.0 h overall — are unchanged |
| 5 | **HIGH — C2-01 (review-lane, now RESOLVED).** `docs/review/modules/KIN-02.md` remained approved/reconciled against plan **2.2** and still assigned keyed recall to F0 | **Resolved under the owner's narrow authorization for that record's Phase-5 reconciliation only** (lines 141–156). It is re-pinned to plan revision 3.6 and its F0/F8 split corrected. No finding, verdict or evidence in that record was altered. **The review-lane blocker is gone; a fresh independent review may now be requested** |

**Deliberately not addressed at proposal revision 7, and still open:** **C5–C8**, **E9a/E9b** (§7 O5) and the **Underactuated appendix titles** (§7 O11), all carried forward unchanged.

### 0.9 What proposal revision 7 got wrong (fixed in this revision)

**Proposal revision 7 and plan revision 3.6 received an independent STRUCTURAL FAIL**, recorded at `docs/review/planning/PLAN_3_6_STRUCTURAL_AUDIT.md` (SHA-256 `a42cb26edc93219a0c82c8e5abc84878cb7ded0530528a2d7c518bd84d694b89`). That audit **confirmed** every one of revision 7's answers — C1-01, C2-01, C2-02, C4-02 and C9-04 all passed their direct re-checks, three of them against re-run isolated mutations — and passed C3, STR-01, STR-02, the totals and route classification, the gate and prerequisite order, and Gate-A invariance. It then found **three fresh defects**. One is plan-side and one is validator-side; both are recorded in plan revision 3.7's history row. Only the proposal-side consequences are listed here. **None of these fixes has been independently verified.**

| # | Finding against proposal revision 7 | Correction in proposal revision 8 |
|---|---|---|
| 1 | **MEDIUM — C4-03: conditional blocker resolution was circularly scheduled "at acquisition".** Plan §9.9 makes a `CONDITIONAL` source **ineligible for acquisition while its blocker stands**, and plan §9.9.1 says in terms that the bounded evaluation-only Gate-D fetch "is not acquisition". §7 **O5** nevertheless resolved `E9a`/`E9b` with a *"One locator-verification fetch at acquisition"* and **O6** resolved `E10` with *"One re-attempt at acquisition"* — *(both phrases are quoted here as the wording audit finding C4-03 required removed; each names an event the blocker itself is a precondition for)* | **Every conditional-source resolution statement now names plan §9.9.1's bounded Gate-D evaluation-only fetch/read.** The audit cited two cells; the sweep covered all of them — §2.6's `C10` and `E9a/E9b` activation conditions, §3.3's `E9a/E9b` locator note, the §5 draft's `lerobot-docs`, `deits-tedrake-iris`, `marcucci-gcs` and `sutton-barto-2e` fields, and §7 O5/O6. `phase5_plan_consistency.py` now sweeps every conditional row in §2.6, the §5 draft and §7 and fails on that phrasing. Plan §9.9.1 states the rule explicitly. **No fetch is authorized by this, and none has occurred** |
| 2 | **HIGH — audit finding C1-02 (validator-side, load-bearing for this document's status block).** The status validator ended every passing run by printing the **withdrawn** "no review or approval request authorized" state — quoted here as the wording that was removed — and — more seriously — the six status regions, this document's header among them, were checked against **assertion labels**, never against the ledger's `currentGateBStatus.facts` booleans. An isolated fixture flipping `independentReviewRequiredAndAuthorized` from `true` to `false` left this header asserting the opposite and still exited 0 | **Fixed at plan revision 3.7.** Each region declares the **facts** it must speak to; the required wording is derived as `factAssertions[fact][current value]`, so a ledger-only fact mutation re-points this header at the opposite assertion and fails. The success line is rendered from the facts. **This document's status claims are now compared against the recorded facts rather than against a label** |
| 3 | **MEDIUM — C2-03 (plan-side, mirrored here).** Plan §5.1 said the +142.0 h "decomposes exactly as" and then listed **five** components, omitting `f8KeyedRecall` at 0.0 h | **Fixed at plan revision 3.7:** the table lists all six, and the validator requires its rows to be the same multiset as the six derived components. **No total this document depends on changed** — 142.0 h added, 368.0 h overall, and the 39-source / 23-7-9 roll-up are all unchanged |

**Also new at this revision, and not a review finding:** a structural audit sitting on disk against the **current** candidate can no longer coexist with a plan, proposal or handoff that calls that candidate unreviewed. That is precisely the state this pass began in — `PLAN_3_6_STRUCTURAL_AUDIT.md` existed while all six status regions still said plan 3.6 / proposal 7 were unreviewed and awaiting a fresh review, in perfect agreement with each other and with the ledger, and all six wrong.

**Deliberately not addressed at this revision, and still open:** **C5–C8**, **E9a/E9b** (§7 O5) and the **Underactuated appendix titles** (§7 O11), carried forward unchanged. **No external source verification was performed at proposal revision 6, 7 or 8** — no page was fetched, no licence re-read, no version re-checked. Every externally-derived claim in this document rests on the verification recorded at earlier revisions, with the unverified items named in §7.

---


## 1. Roles, evaluated separately

| Role | May do | May never do | Admission bar |
|---|---|---|---|
| `theory` | Derivations, theorem statements and conditions, the conceptual spine | Be cited for an API signature | Authority + section-level citability |
| `exercises` | Supply or inspire problems with verifiable answers | — | Answers checkable |
| `api` | Exact signatures, conventions, defaults, version behaviour | Create a completeness finding; supply pedagogy | Official + versioned |
| `implementation` | Be read and compared against | Be vendored without a per-file provenance header | Maintained + readable |
| `citation` | Anchor a specific claim or result to its origin | Be the teaching text | Primary |
| `case-study` | A realistic worked context or dataset | Create a requirement | Public, accountless |

**Binding preference:** a small coherent teaching corpus over a long bibliography; primary/official sources for every factual and API claim; where two candidates fill one role, one is selected and the other is explicitly optional or rejected.

---

## 2. Scored decision matrix (plan §9.2)

Eleven criteria, 0–3 each, **33 points**. Gate criteria: 1 Availability, 2 Cost, 3 Citation granularity, 8 Reproducibility (`api`/`implementation` roles only), 10 Provenance clarity. **Any 0 on a gate criterion disqualifies.**

**The score sets eligibility; the status is a separate decision (plan §9.2, §9.9).** *(Repaired at proposal revision 4.)* Revision 3's header read "≥23 approved · 17–22 conditional · <17 rejected" **as though the band were the status**, and then assigned `CONDITIONAL` or `OPTIONAL` to ten sources scoring 26–28 — all inside the "approved" band. The two steps are now stated separately, and §2.6b applies the result to every scored source.

| Score band | **Eligibility** (step 1) |
|---|---|
| **≥23/33**, no gate-criterion 0 | Eligible at a full role |
| **17–22** | Eligible at a **named, narrowed role only** |
| **<17** | Rejected, with a written reason |
| **Any gate criterion = 0** | Disqualified regardless of total |

**Realigned at proposal revision 6 to plan §9.9's rewritten taxonomy (audit finding C4).** A status answers **what Gate B established**; it is never a permission. The two eligibility columns say what a *later* gate would be free to weigh, and **no Gate-B or Group-A approval authorizes anything in either of them** — acquisition, fetching, downloading, pinning, `sources.json` population, `manifest.json` migration and ingestion are **Gate D**; citation in production content and authoring are **Gate C**.

| Status | **1. Gate-B evaluation status** (step 2, plan §9.9) | **2. Future eligibility for Gate-D acquisition** | **3. Future eligibility for Gate-C citation / authoring** |
|---|---|---|---|
| **`SELECT`** | Proposed for approval at its role. Nothing unknown | **Eligible for consideration at Gate D — not acquired, fetched, pinned, populated, migrated or ingested by any approval recorded here** | **Eligible for consideration at Gate C**, at its approved role |
| **`OPTIONAL`** | **Fully evaluated and approvable. Nothing unknown.** Not proposed by default — it duplicates a selected source's role, or serves a Tier-3/optional artifact. **Opting it in is a Gate C scope decision, not a blocker resolution** | **Not eligible until a Gate-C scope decision opts it in**, and eligible-only even then | **Not eligible until that same Gate-C scope decision opts it in** |
| **`CONDITIONAL`** | **NOT APPROVED, NOT CITABLE.** A fact §9.2 requires is genuinely unknown. Carries exactly one named blocker, an activation condition, and an `ifUnresolved` consequence | **Not eligible at all** while the blocker stands, except for plan §9.9.1's bounded Gate-D evaluation-only fetch/install, which commits and acquires nothing | **Not eligible at all** while the blocker stands |

Criteria: **1** Availability · **2** Cost · **2b** Account-free · **3** Citation granularity · **4** Maintenance · **5** Authority · **6** Notation compatibility · **7** Exercise quality · **8** Reproducibility · **9** Role fit · **10** Provenance clarity.

### 2.1 Group A — Foundation sources (decisions 0006, 0007)

| ID | Source | 1 | 2 | 2b | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | **Total** | **Decision** |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **A1** | Martins & Ning, *Engineering Design Optimization* | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | **30** | **SELECT** |
| | *(A1 role fit is 3 under the repaired criterion 9: `theory` + `exercises` is a coherent role set, not a defect.)* | | | | | | | | | | | | | |
| **A2** | Boyd & Vandenberghe, *Convex Optimization* | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | **30** | **SELECT** |
| **A3** | Axler, *Linear Algebra Done Right* 4e | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | **32** | **SELECT** |
| **A4** | Driscoll & Braun, *Fundamentals of Numerical Computation* | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | **31** | **SELECT** |
| **A5** | Blondel & Roulet, *Elements of Differentiable Programming* | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | **29** | **SELECT** |
| **A5b** | Barratt, *On the Differentiability of the Solution to Convex Optimization Problems* | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 2 | 3 | 3 | **30** | **SELECT** |
| **A6** | Blondel et al., *Efficient and Modular Implicit Differentiation* | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 3 | **29** | **SELECT** (citation) |
| **A7** | Hansen, *The CMA Evolution Strategy: A Tutorial* | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 3 | **29** | **SELECT** |
| **A8** | Larson, Menickelly & Wild, *Derivative-free optimization methods* | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 3 | **29** | **SELECT** |
| A9 | Boyd & Vandenberghe, *VMLS* | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | **29** | **OPTIONAL** — duplicates A4's role |
| A10 | Deisenroth, Faisal & Ong, *Mathematics for ML* | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 2 | 3 | **29** | **OPTIONAL** — duplicates A3; already a benchmark |
| A11 | Petersen & Pedersen, *The Matrix Cookbook* | 3 | 3 | 3 | 2 | 1 | 3 | 2 | 0 | 2 | 1 | 3 | **23** | **OPTIONAL REFERENCE ONLY** — role fit 1: a formula reference, not pedagogy |
| A12 | CVXPY / DCP rules | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 3 | 2 | 3 | **29** | **OPTIONAL, no install** |

*Scoring notes.* A1/A2/A4 score **2 on provenance clarity**: publicly hosted with the publisher's consent, citation expected, **no reuse grant** → consultation/citation-only (plan §9.8). A3 scores 3 (CC BY-NC). A1/A2 score **2 on maintenance** (2022 and 2004 editions, stable rather than updated). A5 scores 2 on notation compatibility (ML-flavoured notation needs mapping to OPT's). A5b/A6/A7/A8/A11/A12 score 1 or 0 on exercise quality — they are references, not problem sets, which is why A1/A2/A3/A4 carry the teaching load.

### 2.2 Group B — Theory (applied)

| ID | Source | 1 | 2 | 2b | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | **Total** | **Decision** |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **B1** | Tedrake, *Underactuated Robotics* | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | **30** | **SELECT** |
| **B2** | Tedrake, *Robotic Manipulation* | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | **30** | **SELECT** |

Both score 2 on notation compatibility — they drive most of §4's conflict register — and 2 on provenance clarity (no explicit prose licence; BSD only on the companion code repo).

### 2.3 Group C — API documentation

| ID | Source | 1 | 2 | 2b | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | **Total** | **Decision** |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **C1** | MuJoCo docs | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | **31** | **SELECT** |
| **C2** | Gymnasium docs | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | **32** | **SELECT** |
| **C3** | PyTorch docs | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 3 | 3 | 3 | **31** | **SELECT** |
| **C4** | NumPy + SciPy docs | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | **32** | **SELECT** |
| **C5** | MuJoCo MJX docs | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 3 | **29** | **SELECT** (optional-extension role) |
| C6 | MuJoCo Warp (MJWarp) | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | **1** | 3 | 3 | **28** | **CONDITIONAL** — install path unconfirmed (§7 O3) |
| C7 | MuJoCo Playground | 3 | 3 | 3 | 2 | 3 | 3 | 2 | 1 | 2 | 2 | **3** | **27** | **OPTIONAL** — licence and role both known; no blocker (§2.6a) |
| C8 | Triton docs | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | **1** | 2 | 3 | **27** | **CONDITIONAL** — ACC-06 (Tier 3) only; capability table unconfirmed (§7 O4) |
| C9 | Drake docs | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 2 | 3 | **28** | **CONDITIONAL** — PLAN-05/06 + CAP-02 only; droppable at Gate D |
| C10 | LeRobot / HF docs | **3** | 3 | **2** | 2 | 3 | 3 | 2 | 1 | 2 | 2 | 3 | **26** | **CONDITIONAL** — see §2.6 |
| C11 | JAX + MJX | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 2 | 3 | **28** | **OPTIONAL** — `ACC-05` (Tier 3) only; no blocker (§2.6a) |

C6 and C8 score **1 on reproducibility** — a gate criterion for `api` roles, but **1 is not 0**, so they are eligible; they are `CONDITIONAL` because a required fact (install path; sm_120 support) is genuinely unknown, not because their artifacts are optional.

**C7 and C11 rescored and reclassified at proposal revision 4.** Revision 3 marked **C7 MuJoCo Playground** `CONDITIONAL` on "licence and role unconfirmed". **Both were already known:** `google-deepmind/mujoco_playground` is **Apache-2.0**, and plan §3.3/§4.4 assign it a **`SIM-06` reference** role. Its provenance-clarity score therefore rises 2 → 3 (total 26 → 27) and its status becomes **`OPTIONAL`**. **C11 JAX/MJX** carried the blocker "none beyond `ACC-05` being Tier 3" — which is not a blocker at all, but the definition of `OPTIONAL`. Neither reclassification is a relaxation: under plan §9.9 an `OPTIONAL` source is still **not proposed by default** and still requires a Gate C scope decision before it is used.

**Scoring corrected at proposal revision 3.** C10 scores **3 on availability**: its documentation is reachable at an official URL with no paywall, and the possibility that a *dataset* is gated is scored at **2b (account-free)**, which is a non-gate preference — not at criterion 1. Revision 2 conflated the two, which is exactly the contract error the review identified. Under the repaired criterion 9, a coherent **role set** scores full marks: A1 (`theory` + `exercises`), C1 (`api` + `implementation`), B1/B2 (`theory` + `exercises`) and A5b (`theory` + `citation`) are not penalized for carrying two roles that genuinely apply.

### 2.4 Group D — Reference implementations and model assets

| ID | Source | 1 | 2 | 2b | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | **Total** | **Decision** |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **D1** | CleanRL | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 3 | 3 | 3 | **31** | **SELECT** — reading source |
| **D2** | Stable-Baselines3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 3 | 2 | 3 | **29** | **SELECT** — role-limited to DRL-06 |
| **D3** | MuJoCo Menagerie (model collection) | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 0 | 2 | 2 | **1** | **25** | **CONDITIONAL** — per-model licences unread (§2.6, §7 O7) |

**D3 is new at proposal revision 6, and it is a correction, not an addition to scope.** *(Audit finding C9.)* Menagerie was already a **proposed source** in every other part of this document — it has a `sources.json` v2 draft entry with a complete conditional block (§5), the recorded role `case-study`, the named modules `SIM-02` and `SIM-05`, a blocker row in §2.6, an open item in §7 (O7), a reuse classification in §8, and a place in the §2.6b `CONDITIONAL` roll-up. **The one thing it did not have was a scored row**, which is why §2's matrices summed to 38 while §2.6b published 39. Scoring it closes that gap under the same eleven-criterion contract as every other source. **The resulting total is again 39; that coincidence is not the reason for the choice** — the alternative, dropping Menagerie from the roll-up, would have removed a source this document proposes, cites in five other places, and gives a full conditional entry to.

*D3 scoring notes, stated so each figure can be falsified.* **1/2/2b = 3**: a public GitHub repository, free, cloneable without an account, at the URL and access date recorded in §5. **3 = 3**: the citation unit is *model directory + that model's own `LICENSE` + git ref*, an exact and stable locator. **4 = 2**: first-party and live at the recorded URL, but its release cadence was **not separately verified**, and **proposal revision 6 performs no external verification** (§0.7); 2 records a maintained-looking first-party repository without asserting an update cadence. This is a *score*, not a second blocker — §9.9 allows exactly one, and D3's is the per-model licences. **5 = 3**: the first-party MuJoCo model collection, indexed from C1's own documentation (§6.7). **6 = 3**: MJCF asset files introduce no mathematical notation, so D3 contributes no row to §4's conflict register. **7 = 0**: a model collection contains no exercises — criterion 7 is **not** a gate criterion (A11 also scores 0). **8 = 2**: pinnable to a 40-hex commit SHA per model, but no ref is pinned and no per-model licence has been read, so a reproducible per-model citation is not yet demonstrable; criterion 8 is a gate criterion for `api`/`implementation` roles only, and D3's role is `case-study`. **9 = 2**: one narrow role serving exactly two modules; it supplies assets, never pedagogy. **10 = 1**, the gate criterion that matters here: the repository-level Apache-2.0 is stated, but the **governing** per-model licences differ and **none has been read**. Terms exist and are stated per model, which is 1 rather than 0 — the same reading that gives E5 a 1. **25/33 with no gate-criterion 0 ⇒ eligible at a full role; status `CONDITIONAL` because a fact §9.2 requires is genuinely unknown.**

**D3 has no §6 coverage rows, and that is deliberate.** Its promised units are *individual models*, and which models will be used cannot be enumerated before each one's own `LICENSE` is read (§7 O7). Enumerating them now would be the aggregate claim §2.6 forbids. The "Menagerie index" row in §6.7 is a **C1 documentation page**, not a D3 unit, and is counted against C1's 15 rows.

### 2.5 Group E — Papers

| ID | Paper | 1 | 2 | 2b | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | **Total** | **Decision** |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **E1** | Schulman et al., PPO | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 3 | **29** | **SELECT** |
| **E2** | Chi et al., Diffusion Policy | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 3 | **29** | **SELECT** |
| **E3** | Ross, Gordon & Bagnell, DAgger | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 3 | **29** | **SELECT** |
| **E4** | Haarnoja et al., SAC (ICML 2018) | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 3 | **29** | **SELECT** |
| **E4b** | Haarnoja et al., *SAC Algorithms and Applications* | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 2 | 3 | **28** | **CONDITIONAL** — add only if automatic temperature tuning is taught |
| **E5** | Mnih et al., DQN (*Nature* 2015) | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | **1** | **27** | **SELECT — citation-only** |
| E8 | Agarwal et al., rliable | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 2 | 3 | **28** | **OPTIONAL** |
| E9a | Deits & Tedrake, IRIS | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 2 | **28** | **CONDITIONAL** — locator unpinned (§7 O5) |
| E9b | Marcucci et al., GCS | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 1 | 2 | 3 | 2 | **28** | **CONDITIONAL** — locator unpinned (§7 O5) |
| E10 | Sutton & Barto 2e | **1** | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 2 | 2 | 2 | **27** | **CONDITIONAL** — official PDF reachability unconfirmed (§7 O6) |

E5 scores **1 on provenance clarity**: the official public PDF is verified, but it is "All rights reserved", so it is citation-only and **never required reading**. That is 1, not 0 — the terms are *stated*, which is what criterion 10 measures. E6 (behavior-cloning origin) and E7 (AlphaZero) are **deferred** and unscored; see §3.3.

### 2.6 `CONDITIONAL` sources — every blocker, activation condition and consequence

**Scope corrected at proposal revision 4.** This table now lists **only sources with a genuine unknown**. C7 and C11 were removed because neither had a blocker (§2.6a); they are `OPTIONAL`, which §2.6b covers. Every blocker below that needs a fetch or an install is resolved under **plan §9.9.1's bounded evaluation-only permission** — Gate D, disposable scratch environment, nothing committed, a cost ceiling, and a stated outcome if the ceiling is hit.

**`CONDITIONAL` is not a soft approval. It means NOT APPROVED and NOT CITABLE** (plan §9.9): the source may not be fetched into the manifest, may not appear in any `sourceId`, and may not be relied on by any module, lab or repair until its named blocker is resolved **and the owner accepts the resolution**. No content may be authored that would need it.

| ID | Source | **Blocker** | **Activation condition** | If never resolved |
|---|---|---|---|---|
| **C6** | MuJoCo Warp (MJWarp) | The install path is unconfirmed — searches did not establish a plain `pip install mujoco-warp`; current guidance is a source/uv install or via Playground | A Gate-D measurement on the 5090 showing a reproducible, documented install **and** a working rollout | `SIM-06`'s optional MJWarp extension is cut. Its **required** CPU vector-env half is unaffected, so the main-route module still ships |
| **C8** | Triton | Exact compute-capability support for sm_120 is unconfirmed; the repo's compatibility table has not been read | A Gate-D measurement: `pip install triton`, a compiled kernel, and a correctness check against eager PyTorch on the 5090 | **`ACC-06` is cut entirely.** It is Tier 3, `cuda-required`, and nothing on the main route depends on it (plan §7.3) |
| **C9** | **Drake** | Two blockers: **(a)** the licence was recorded as unstated on the installation page — now **resolved: BSD-3-Clause** per `RobotLocomotion/drake` `LICENSE.TXT`; **(b) still open —** whether a reproducible pinned install on this host costs less than the plan's stated budget | A Gate-D measurement showing install and version pinning reproducible in **≲ half a day** (plan §16.2's explicit drop criterion) | **Drake is dropped entirely** and the NumPy/SciPy fallback becomes primary for `PLAN-05`, `PLAN-06` and `CAP-02`. Plan §16.2 already rules that this costs the connection to the field's reference GCS implementation but **no concept, derivation or exercise** |
| **C10** | **LeRobot / Hugging Face** | Whether the specific datasets `DRL-08` would use are **ungated**. Ungated public download requires no account; a gated one would need a free account, which §2.10 permits but does not assume | A plan §9.9.1 **Gate-D evaluation-only reachability check** per dataset, confirming the chosen dataset is ungated — or an explicit owner decision to accept a free account for a named gated dataset, recorded as `requiresAccount: true` and surfaced on `/sources` | `DRL-08` is cut or re-scoped to a non-LeRobot dataset. It is **Tier 3**, so nothing on the main route is affected |
| **D3** | MuJoCo Menagerie models *(scored at proposal revision 6 — §2.4)* | **Per-model licences.** The repository is Apache-2.0 but **each model directory carries its own `LICENSE`**, and they differ | **Per model**: before any specific model is used, its own `LICENSE` is read and recorded in `sources.json` against that model. **An aggregate repository-level licence claim is never sufficient** | Only models whose individual licence has been read and recorded may be used. Unread models are simply not used |
| **E4b** | Haarnoja et al., *SAC: Algorithms and Applications* | **Not a defect — a scope question.** It is only needed if `DRL-06` teaches automatic temperature tuning or the later modifications | A Gate-C decision that `DRL-06`'s scope includes automatic temperature tuning | Not added. **E4 (ICML 2018) alone is sufficient** for SAC as `DRL-06` is currently scoped |
| **E9a/E9b** | Deits & Tedrake (IRIS); Marcucci et al. (GCS) | Exact paper versions and stable locators unpinned | A plan §9.9.1 **Gate-D evaluation-only fetch/read** that verifies the version, locator, title and licence, accepted by the owner. **Pinning is a separate, later Gate-D acquisition step that becomes possible only once that blocker is resolved and the status has changed** | B2 ch.6 covers the material; the papers become "further reading" rather than citations |
| **E10** | Sutton & Barto 2e | Official free-PDF reachability unconfirmed — `incompleteideas.net` failed with a self-signed certificate on 2026-08-14 | A plan §9.9.1 **Gate-D evaluation-only fetch** that reaches the official page | DRL cross-references stand on B1, D1 and the existing RL block. **No paywalled substitute is adopted** |

**Note the asymmetry that makes this safe:** every conditional source serves a Tier-3 module, an optional extension, or an artifact with a non-conditional fallback. **No conditional source is load-bearing for the main route**, and none is needed by F0.

**Resolution ceilings (plan §9.9.1).** Every blocker above that requires running something carries a cost ceiling, so none can stay open indefinitely: **C6** and **C8** are bounded by their single Gate-D measurement — one install attempt and one working check each; **C9 Drake** by plan §16.2's explicit **half-day** ceiling. Exceeding a ceiling resolves the blocker as *unresolved* and triggers the `ifUnresolved` column. It never authorizes more time, and it never permits citing the source anyway.

### 2.6a Sources that carry no blocker (`OPTIONAL`) — new at proposal revision 4

These are **fully evaluated**. Nothing about them is unknown, so none is `CONDITIONAL`. They are not proposed by default for the reason given, and each requires a **Gate C scope decision** — not evidence — before it is used.

| ID | Source | Licence | Role | Why not proposed by default |
|---|---|---|---|---|
| **C7** | MuJoCo Playground | **Apache-2.0** (`google-deepmind/mujoco_playground`) | `SIM-06` reference | Duplicates C1/C5 for the one place it would be used; the owner has not committed to the `SIM-06` optional extension |
| **C11** | JAX / MJX | **Apache-2.0** | `ACC-05` (Tier 3) `api` | `ACC-05` is a Tier-3 decision module the owner may simply not build |
| A9 | Boyd & Vandenberghe, *VMLS* | Publisher-permitted web copy, no reuse grant | `theory` | Duplicates **A4**'s role |
| A10 | Deisenroth, Faisal & Ong, *Mathematics for ML* | Publisher-permitted web copy | `theory` | Duplicates **A3**; already an approved review benchmark, recorded separately |
| A11 | Petersen & Pedersen, *The Matrix Cookbook* | Freely distributed reference | reference only | Role fit 1 — a formula reference, not pedagogy. **May verify `MATH-02B`'s identities, may never teach them** |
| A12 | CVXPY / DCP rules | Apache-2.0 | `citation` | Cited for the DCP ruleset only. **No install; no lab depends on it** |
| E8 | Agarwal et al., *rliable* | Preprint + MIT tooling | `citation` | `DRL` evaluation methodology the owner has not committed to |

**None of these is approved by a Group-A approval, and none becomes approved by association** (§10.1).

### 2.6b The three states, applied to every scored source — new at proposal revision 4, **reconciled with §2 at proposal revision 6**

Exactly one status per source, per plan §9.9. This roll-up exists so a reader can check the taxonomy was applied consistently rather than row by row.

| Status | Count | Sources |
|---|---:|---|
| **`SELECT`** | **23** | A1, A2, A3, A4, A5, A5b, A6, A7, A8 · B1, B2 · C1, C2, C3, C4, C5 · D1, D2 · E1, E2, E3, E4, E5 |
| **`OPTIONAL`** | **7** | A9, A10, A11, A12 · C7, C11 · E8 |
| **`CONDITIONAL`** | **9** | C6, C8, C9, C10 · D3 · E4b · E9a, E9b · E10 |
| | **39** | Total scored sources. E6 and E7 are **deferred and unscored** (§3.3) and appear in no row above |

**Corrected at proposal revision 6 (audit finding C9).** Through proposal revision 5 the `CONDITIONAL` list named **Menagerie**, which had **no scored row in §2.1–§2.5**: the matrices held 38 scored rows while this table published 39. Menagerie is now scored as **D3** (§2.4), so the two sets agree. **The total is 39 because 39 sources are scored, not because 39 was the previously printed figure** — the alternative resolution, dropping the entry and publishing 38, was rejected because Menagerie is a source this proposal actually proposes (§5 entry, §2.6 blocker, §7 O7, §8 reuse row).

**Every count in this table is recomputed from the tables above by `scripts/validate/phase5_plan_consistency.py`, not transcribed.** The validator now enforces four things a count comparison alone could not see: **(1)** the set of scored IDs in §2.1–§2.5 **equals** the union of the three roll-up lists; **(2)** every roll-up ID has **exactly one** scored row; **(3)** every scored row appears under **exactly one** status; **(4)** the printed total equals **both** sets' cardinality. A status assigned in §2.1–§2.5 that disagrees with this roll-up, or a `CONDITIONAL` row missing any of blocker / activation condition / consequence, still fails the check.

### 2.7 Rejected, with reasons

| Rejected | Gate failure | Score | Replacement |
|---|---|---|---|
| Nocedal & Wright, *Numerical Optimization* 2e | **Criterion 1 = 0.** No free official copy | disqualified | **A1 ch.4–5** (verified to contain strong Wolfe §4.3.2 and the curvature condition in §4.4.4) + **A2** |
| Trefethen & Bau, *Numerical Linear Algebra* | **Criterion 1 = 0** | disqualified | **A4** |
| Golub & Van Loan, *Matrix Computations* | **Criterion 1 = 0**; also beyond needed depth | disqualified | **A4** |
| Conn, Scheinberg & Vicente; Audet & Hare | **Criterion 1 = 0**; exceed `OPT-05B`'s intuition depth | disqualified | **A8** + **A7** |
| Krantz & Parks, *The Implicit Function Theorem* | **Criterion 1 = 0**; a monograph where one theorem is needed | disqualified | **A5** + **A5b** |
| Fiacco; Bonnans & Shapiro (sensitivity/perturbation analysis) | **Criterion 1 = 0** | disqualified | **A5b**, whose Assumption 3 is exactly the needed condition |
| A general convex-analysis text beyond A2 | Role fit — 0007 scopes `OPT-04` to compact recognition | not scored | **A2** at recognition depth |
| RL-Zoo, SB3-Contrib | Role fit 0 — breadth with no teaching role | not scored | **D2** |
| Tianshou, Acme, rlpyt, Dopamine, torchrl | Role fit 0 — a third implementation source doing D1's job | not scored | **D1** |
| Colab as a lab runtime | Plan §2.10 ruling | not scored | the 5090 / laptop CPU |

**Accuracy note (corrected).** A paid book is **not** "uncitable in a public workbook" — citing one is perfectly legitimate. It is **ineligible as a learner-required teaching source under this project's availability gate** (§9.2 criterion 1: reachable from an official/primary URL, no paywall). If the owner personally owns any of the above, they may still be cited as further reading; they may not be *required*.

---

## 3. Per-source detail

### 3.1 Group A

#### A1 — Martins & Ning, *Engineering Design Optimization* — SELECT (30/33)

`sourceId` `martins-ning-edo` · `theory`, `exercises` · Cambridge University Press, 2022 · `https://mdobook.github.io/` · free PDF at `http://flowlab.groups.et.byu.net/mdobook.pdf` · **642 pages, accessed and read 2026-08-15** · cite by chapter + numbered section · **no reuse licence stated → consultation/citation-only**.

**Verified section mapping** (TOC read directly from the PDF):

| Locator | Serves |
|---|---|
| §4.3 Line Search → **§4.3.1 Sufficient Decrease and Backtracking**, **§4.3.2 Strong Wolfe Conditions**, §4.3.3 Interpolation for Pinpointing | **`OPT-01` repair** — Armijo vs weak vs strong Wolfe, and a line search that can actually enforce the chosen condition |
| §4.4 Search Direction → §4.4.2 Conjugate Gradient, §4.4.3 Newton's Method, **§4.4.4 Quasi-Newton Methods** (contains the **curvature condition**), §4.4.5 Limited-Memory Quasi-Newton | **`OPT-01`/`OPT-02` repairs** — BFGS curvature condition `yᵀs > 0`, linear vs nonlinear CG, Newton assumptions |
| §4.5 Trust-Region Methods | `OPT-01` damping/trust-region limiting behaviour |
| §5.3 Optimality Conditions → §5.3.1 Equality, §5.3.2 Inequality (**constraint qualification** appears here), §5.3.3 Meaning of the Lagrange Multipliers, §5.3.4 Post-Optimality Sensitivities | **`OPT-03` repairs** + the **multiplier-sensitivity optional box** |
| §5.5 Sequential Quadratic Programming → §5.5.1–§5.5.5 incl. **§5.5.3 Merit Functions and Filters** | **`OPT-04` repair** — SQP with the Hessian of the Lagrangian **plus globalization** |
| §5.6 Interior-Point Methods | `OPT-04` barrier/central-path repair (with A2) |
| §7.1 When to Use Gradient-Free Algorithms, §7.2 Classification, **§7.3 Nelder–Mead**, **§7.4 Generalized Pattern Search**, §7.5 DIRECT, §7.6 Genetic Algorithms, §7.7 Particle Swarm | **`OPT-05B`** — method selection, Nelder–Mead, pattern search, and the DIRECT/GA/PSO boundaries. **NOT CMA-ES — see A7** |
| §10.6.2 Efficient Global Optimization | `OPT-06` acquisition/surrogate repair |
| §11.2 LP, §11.3 QP, §11.4 SOCP, **§11.5 Disciplined Convex Optimization**, §11.6 Geometric Programming | **`OPT-04` bridge** — problem-class recognition and DCP composition |

**Uniquely adds:** the only free, single, section-citable authority covering most of the mandatory OPT repair batch in one notation. **Overlap with A2** is deliberate: **A2 governs statements of conditions, A1 governs algorithm descriptions.**

#### A2 — Boyd & Vandenberghe, *Convex Optimization* — SELECT (30/33)

`sourceId` `boyd-convex` · `theory` (production) + already-approved OPT review benchmark (recorded separately) · Cambridge University Press, 2004 · `https://web.stanford.edu/~boyd/cvxbook/` · **accessed 2026-08-15**; the page states copyright is held by CUP, "who have kindly agreed to allow us to keep the book available on the web" · cite by chapter + section + equation · **no reuse grant → consultation/citation-only**.

Serves: `OPT-03` KKT necessity **and Slater's constraint qualification**, stationarity vs Lagrangian minimization, saddle/strong-duality; `OPT-04` convex/quasiconvex language, **convex QP requiring `Q` PSD not PD**, log-barrier domain/limit, central path; `OPT-01` Newton assumptions and the **Newton decrement** optional box; `PLAN-05`/`PLAN-06` conic framing. Section-level dispositions in §6.2.

#### A3 — Axler, *Linear Algebra Done Right* 4e — SELECT (32/33)

`sourceId` `axler-ladr4` · `theory` · Springer UTM, Open Access · `https://linear.axler.net/` · **English PDF dated 13 August 2026, accessed 2026-08-15** · **licence: Creative Commons BY-NC** · cite by numbered section (3F, 7E, 7F) and numbered result.

Serves: ch.1 vector-space axioms → **`MATH-03` missing distributivity axiom**; **§3F Duality** (dual space, dual map) → **`MATH-03` dual space defined without linearity**; §7A–7D positive operators → `MATH-03B` PD/PSD; **§7E SVD** → `MATH-04` symmetric-indefinite SVD/eigen relation; **§7F** (approximation by linear maps with lower-dimensional range) → **`MATH-04` Eckart–Young**, which `MATH-EXAM` Part 3 already assesses.

**Explicit non-coverage:** no conditioning, floating point, QR as an algorithm, Cholesky, or covariance/statistics. That is A4's job.

#### A4 — Driscoll & Braun, *Fundamentals of Numerical Computation* — SELECT (31/33)

`sourceId` `fnc-driscoll-braun` · `theory`, `exercises` · SIAM (print: 2017 MATLAB, 2022 Julia); free online edition with a **Python** code path · `https://fncbook.com/` · **accessed 2026-08-15** · cite by numbered section and theorem · **online edition states no licence → consultation/citation-only**.

**Verified locators:** ch.1 §Problems and conditioning, §Stability; ch.2 LU/pivoting and **Theorem 2.9.3 Cholesky**; ch.3 normal equations and **Theorem 3.3.3 QR**; ch.7 matrix analysis, SVD, dimension reduction. Serves `NUM-03` throughout, plus `OPT-01`/`OPT-02` solve-don't-invert and Gauss–Newton conditioning, and `MATH-03B` projection implemented.

#### A5 — Blondel & Roulet, *The Elements of Differentiable Programming* — SELECT (29/33)

`sourceId` `blondel-roulet-edp` · `theory` · `https://arxiv.org/abs/2403.14606` · **draft version 4, last update 3 August 2026; arXiv:2403.14606v4; 492 pages — verified by reading the PDF 2026-08-15**.

**Sections pinned now** (part III, chapter *Differentiating through optimization*, pp. 285–305 of v4):

| Section | p. | Serves |
|---|---|---|
| Implicit functions — Optimization problems; Nonlinear equations; Application to bilevel optimization | 285–286 | `OPT-04B` framing |
| Envelope theorems — Bertsekas'; Rockafellar's; **Danskin's** | 287–291 | `OPT-04B` context |
| **Implicit function theorem** — Univariate; **Multivariate**; JVP and VJP of implicit functions; Proof | **291–296** | **`OPT-04B` core: the IFT with its conditions** |
| Adjoint state method — Differentiating nonlinear equations; Relation with envelope theorems; two proofs | 297–300 | `OPT-04B` root-system differentiation |
| Inverse function theorem; Summary | 303–305 | Reference |

**Verified gap, and why A5b exists.** This chapter treats the IFT and differentiating nonlinear equations, but **does not supply the KKT-specific active-set-change failure mode** that decision 0007 requires `OPT-04B` to teach. A5 alone is therefore insufficient for that objective.

#### A5b — Barratt, *On the Differentiability of the Solution to Convex Optimization Problems* — SELECT (30/33) — **new in revision 2**

`sourceId` `barratt-diffopt` · `theory`, `citation` · Shane Barratt (Stanford EE) · `https://arxiv.org/abs/1804.05098` · **v3, 11 November 2019, 4 pages — verified by reading the PDF 2026-08-15**.

**What the paper actually states**, verified by direct reading — and stated here at exactly that strength, no further:

| Locator | Content, as written |
|---|---|
| **Assumption 1 (Strong duality)** | Slater's condition holds for the problem |
| **Assumption 2 (Differentiability)** | The `fᵢ` are twice continuously differentiable in `x`; `f` continuously differentiable in `θ` |
| **Assumption 3 (Emptiness of `G`)** | `G = {i \| λ̃ᵢ = 0 and fᵢ(x̃, θ) = 0}` is empty. **This is strict complementarity** — no inequality constraint is simultaneously active and carrying a zero multiplier |
| **Theorem 2.1** | The implicit function theorem, quoted from Dontchev & Rockafellar |
| **Eq. (9)** | The Jacobian `D_z g`, which contains a `diag(λ̃)Df(x̃, θ)` block |
| **Theorem 3.1** | The solution mapping has a continuously differentiable single-valued localization **if Assumptions 1–3 hold *and* `D_z g` is non-singular** |

**Two conditions, not one — and the plan must keep them separate.** Theorem 3.1 requires strict complementarity (Assumption 3) **and, independently, a non-singular KKT Jacobian.** Assumption 3 does not imply non-singularity, and non-singularity does not imply Assumption 3. `OPT-04B` must teach both, and must not present either as a restatement of the other.

**Where the workbook's own inference begins, labelled as such.** Barratt states a *sufficient* condition set for differentiability. He does **not** state that crossing an active-set boundary causes non-differentiability, and this proposal does not claim he does. What the workbook may say, as its **own reasoning from Eq. (9)** and marked `newly-authored`:

> As a multiplier `λ̃ᵢ` approaches zero on a constraint that is active (`fᵢ = 0`), the point approaches the boundary of Assumption 3's admissible set — `G` becomes non-empty in the limit — and the corresponding row of Eq. (9)'s `diag(λ̃)Df` block degenerates. Barratt's *sufficient* conditions therefore stop applying at exactly the configurations where an active set changes, which is why derivatives computed through a solver become unreliable there.

That is an inference about **the theorem ceasing to apply**, which is weaker and more accurate than a claim that the derivative provably fails to exist. `OPT-04B`'s lab demonstrates the failure **empirically** — a finite-difference check that stops agreeing — and the module states plainly that a violated sufficient condition is not a proof of non-differentiability. **If a citable authority for the stronger claim is wanted, that is a separate source need and is not proposed here.**

Four pages, free, primary, and precisely scoped.

#### A6 — Blondel et al., *Efficient and Modular Implicit Differentiation* — SELECT (29/33), citation role

`sourceId` `blondel-implicit-diff` · `citation` · `https://arxiv.org/abs/2105.15183` · **v5, 12 October 2022; NeurIPS 2022 — verified 2026-08-15**. Anchors the "specify optimality conditions `F(x, θ) = 0` and differentiate them" formulation. **Cited, not taught; `OPT-04B` is CPU-first and adopts neither JAX nor JAXopt.**

#### A7 — Hansen, *The CMA Evolution Strategy: A Tutorial* — SELECT (29/33) — **now the sole CMA-ES authority**

`sourceId` `hansen-cmaes-tutorial` · `theory`, `citation` · Nikolaus Hansen, **originator of the method** · `https://arxiv.org/abs/1604.00772` · **v2, 10 March 2023 — verified 2026-08-15**.

Serves `OPT-05B`'s CMA-ES treatment at intuition depth — sampled population, adapted covariance, adapted step size — and the OPT cheat-sheet repair whose decision tree recommends CMA-ES as though `OPT-06` taught it. **Scope guard: intuition only; the update algebra is not derived.** A1 does not cover CMA-ES at all, which is why this source is load-bearing rather than supplementary.

#### A8 — Larson, Menickelly & Wild, *Derivative-free optimization methods* — SELECT (29/33)

`sourceId` `larson-dfo-survey` · `theory` · **Acta Numerica 28 (2019) 287–404**; preprint `https://arxiv.org/abs/1904.11585` **v2, 25 June 2019 — verified 2026-08-15**. Supplies `OPT-05B`'s taxonomy and method boundaries — what keeps the module from drifting into the heuristic catalogue decision 0007 forbids.

#### A9–A12 — optional

A9 VMLS (`https://web.stanford.edu/~boyd/vmls/`, verified 2026-08-15, same posture as A2) — gentler QR/least-squares cross-check; duplicates A4. A10 *Mathematics for ML* — already a MATH benchmark; duplicates A3. A11 *The Matrix Cookbook* — **reference only**; may verify `MATH-02B`'s identities, may never teach them. A12 CVXPY/DCP rules — cite the official DCP ruleset for the `OPT-04` bridge; **no install, no lab depends on it**.

### 3.2 Groups B–D

**B1/B2 — Tedrake ×2.** `https://underactuated.mit.edu/` (Spring 2024, © Russ Tedrake 2024, 21 chapters + appendices A–E, explicit BibTeX, no prose licence, companion repo BSD) and `https://manipulation.mit.edu/` (Fall 2025, © 2020–2025, 12 chapters). Verified 2026-08-14. **Dispositions for all 38 source units — 21 + 5 appendices + 12 — exist in plan §3.3 and are adopted unchanged, and are instantiated row by row in §6.5.** *(Corrected at proposal revision 4: this sentence said "all 33 chapters", the same undercount §6.5 fixes.)* Both are **consultation/citation-only**. Every citation pins edition + chapter anchor + access date; a future edition is a new pinned entry.

**C1–C11 — API docs.** Licences resolved (§7). C1 MuJoCo (`mujoco` 3.11.0, Python 3.14 verified); C2 Gymnasium (1.3.0 verified); C3 PyTorch (torch 2.13.0 local); C4 NumPy/SciPy; C5 MJX; C6 MJWarp (conditional); C7 Playground (**`OPTIONAL`** — Apache-2.0, `SIM-06` reference; no blocker, §2.6a); C8 Triton (conditional; `ACC-06` Tier 3 only); C9 Drake (**PLAN-05/06 + CAP-02 only**, NumPy/SciPy fallback on every Drake lab, **dropped at Gate D if reproducible install exceeds ~half a day**); C10 LeRobot (**DRL-08 Tier 3 only**, ungated datasets default, `requiresAccount: true` recorded per gated dataset, Colab notebooks not adopted); C11 JAX/MJX (**`OPTIONAL`** — Apache-2.0; `ACC-05` Tier 3; no blocker, §2.6a).

**D1 CleanRL** — the **reading** source: single-file implementations a learner can read end to end. The three files this proposal names are **`dqn.py`, `ppo.py` and `sac_continuous_action.py`**. *(Corrected at proposal revision 4: revision 3 named the third file `sac.py`; **CleanRL has no such file** — its continuous-control SAC single-file implementation is `sac_continuous_action.py`.)* **D2 SB3** — the **comparison target in DRL-06 only.** Both: read-and-compare, **no vendoring without a per-file provenance header** naming source, URL, git ref and changes. Both pin an immutable 40-hex `gitRef` at acquisition; a branch name or tag is not an acceptable pin (§5.3).

### 3.3 Group E papers — locators

| ID | Locator | Status |
|---|---|---|
| E1 PPO | **arXiv:1707.06347** | Verified 2026-08-15 |
| E2 Diffusion Policy | **arXiv:2303.04137** (v4 and v5 exist — **pin the version at acquisition**) | Verified 2026-08-15 |
| E3 DAgger | **`https://proceedings.mlr.press/v15/ross11a.html`** — official PMLR | Verified; carried from the approved benchmark record |
| **E4 SAC (primary)** | Haarnoja, Zhou, Abbeel, Levine, *Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL with a Stochastic Actor*, **PMLR v80 (ICML 2018), pp. 1861–1870**, `https://proceedings.mlr.press/v80/haarnoja18b.html`, free PDF | **Verified 2026-08-15.** This is the primary SAC citation |
| E4b SAC *Algorithms and Applications* | arXiv:1812.05905 | **CONDITIONAL — add only if `DRL-06` teaches automatic temperature tuning or the later modifications.** Not added by default |
| **E5 DQN** | Mnih et al., *Human-level control through deep reinforcement learning*, ***Nature* 518, 529–533, 26 February 2015, doi:10.1038/nature14236**; official public PDF **`https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf`** | **Verified 2026-08-15 by reading the PDF: 13 pages, contains both experience replay and the separate target network — the exact mechanism `DRL-03` teaches.** Carries "Macmillan Publishers Limited. All rights reserved ©2015" → **`citation` role only; no reuse of prose or figures; never required reading.** The paywall open item is withdrawn |
| E8 rliable | Agarwal et al. | **OPTIONAL** — locator pinned at acquisition if adopted |
| E9a/E9b IRIS, GCS | Deits & Tedrake; Marcucci et al. | **CONDITIONAL** — **neither paper has been fetched or read.** Titles, authors and venues in §5 are recorded from prior knowledge and are **explicitly flagged unverified in the entries**; they are confirmed by the plan §9.9.1 **Gate-D evaluation-only fetch/read**, as part of the same blocker and before any acquisition is possible. B2 ch.6 covers the material, so nothing depends on them (§7 O5) |
| E10 Sutton & Barto 2e | `http://incompleteideas.net/book/the-book-2nd.html` | **CONDITIONAL** — reachability unconfirmed (§7 O6) |
| E6 behavior-cloning origin | — | **DEFER.** E3 already anchors the compounding-error result; a separate origin citation is bibliography, not teaching |
| E7 AlphaGo / AlphaZero | — | **DEFER.** `RL-06` teaches MCTS/UCT; no module implements AlphaZero; the plan never assigned it a destination |

---

## 4. Per-source notation conflicts (plan §9.6, §8)

Every source that introduces a symbol conflict, and the §8 ruling that resolves it. **This is the input Gate C's `notation.json` consumes.**

| Source | Symbol | Source's meaning | Workbook's meaning | Ruling (§8.2) |
|---|---|---|---|---|
| **B1** Tedrake UA | `x` | state `x = [q; q̇]` | optimization variable (OPT); state (DYN) | Adopt `x` = state in DYN/UAC/SIM; OPT keeps `x` = decision variable, scoped, with a bridge box at `UAC-04` |
| **B1** | `R` | LQR input-cost matrix | rotation matrix (KIN); reward (RL) | **Three-way collision.** `R` = rotation matrix in KIN/DYN/PLAN/MANIP/SIM; LQR input cost **renamed `R_u`**; reward stays `r`/`R(s,a)` in RL/DRL |
| **B1** | `Q` | LQR state cost | Q-function (RL) | LQR state cost **renamed `Q_x`** |
| **B1** | `V` | Lyapunov function **and** cost-to-go | value function | **Deliberate unification**, `UAC-03`'s teaching point; one bridge box |
| **B1** | `J` | cost functional | Jacobian (KIN-03, MATH-02) | `J` = Jacobian; cost functional is `L`/`ℓ` running, `J_c` total; bridge box at `UAC-04` |
| **B2** Tedrake Manip | `C`, `C_free` | configuration space | `X`, `X_fea` (PLAN-01) | Keep `X`/`X_fea`; bridge box in `PLAN-05` |
| **C1** MuJoCo | `qpos`, `qvel`, `ctrl` | generalized coords, velocities, controls | `q`, `q̇`, `u` | Map in `SIM-01`; **mandatory bridge box on `dim(qpos) ≠ dim(qvel)` with quaternion joints** |
| **A1** Martins & Ning | `f`, `g`, `h`, `x` | objective, inequality, equality, design variables | `f`, `g`, `h`, `x` in OPT | **No conflict** — matches OPT's existing convention |
| **A1** | `α` | line-search step length | step size (OPT-01) / learning rate (RL-03) | **No new conflict**; folds into the existing unified `α` registry entry |
| **A2** Boyd | `λ`, `ν` | inequality and equality multipliers | `λ` used for both in `OPT-03`; also eigenvalue in MATH | **New ruling needed:** adopt Boyd's `λ`/`ν` split in `OPT-03`/`OPT-04B` (it is what the KKT system needs); eigenvalue `λ` stays scoped to MATH with a bridge box |
| **A2** | `t` | barrier/central-path parameter | time (DYN/ODE) | Scope `t` = barrier parameter **inside `OPT-04` only**; bridge box, since `μ` is also common |
| **A3** Axler | `V`, `W` | vector spaces | value function (RL); Lyapunov (UAC) | Scope: `V`, `W` as vector spaces **inside MATH only**; no cross-block use |
| **A3** | `T` | a linear map | transpose superscript; time horizon | Workbook keeps matrix notation `A`; **do not import Axler's operator `T`** |
| **A4** FNC | `κ(A)` | condition number | unused | **No conflict — adopt as-is.** Becomes the canonical condition-number symbol in `NUM-03` |
| **A5/A5b** | `θ` | problem parameters being differentiated w.r.t. | rotation angle (KIN); policy parameters (ML/RL) | **Existing collision.** `θ` = parameter is consistent with ML/RL usage; bridge box in `OPT-04B` noting KIN's rotation-angle `θ` is unrelated |
| **A5b** | `z = (x, λ, ν)` | primal–dual triple | — | New, no conflict; adopt in `OPT-04B` |
| **A7** Hansen | `σ`, `C`, `m` | step size, covariance, distribution mean | `σ` is the **renamed SYM-02 substitution** (§8.2); `C` is Tedrake's `C_free`; `m` is a dimension | **Three collisions, all scoped.** Confine Hansen's `σ`/`C`/`m` to `OPT-05B` with one bridge box; do not export them |
| **D1** CleanRL | `obs`, `done`, `truncated` | Gymnasium API names | — | No conflict; API-level, matches C2 |
| **E1/E4** | `π_θ`, `α` (SAC temperature) | policy; entropy temperature | `α` = step size/learning rate | **Collision.** SAC's temperature is written `α_ent` in `DRL-06`, with a bridge box noting the papers write `α` |

**Rule applied throughout (§8.3):** translate to canonical when the symbol is central and crosses ≥2 blocks; retain source notation locally with a bridge box when the learner will read the source directly. **A7's symbols are the clearest "retain locally" case** — a learner reading Hansen must see Hansen's notation.

---

## 5. Proposed `sources.json` v2 draft (plan §9.3)

**This is a DRAFT. It is not written to disk, not executed, and creates no manifest entry.** The migration it describes is **Gate D** work (§9). Publishing it here is what lets Gate B be decided on complete data instead of on a promise.

**Rewritten at proposal revision 4.** Revision 3's draft was reviewed and found **not executable**: every PDF `sha256` was truncated with `…`; the v1 fields `relativePath`, `pdfMetadata`, `embeddedToc` and `extraction` appeared in the mapping table but in no entry; **E9a, E9b and E10 had no entry at all**; `cost`, `citationUnits` and module mapping were missing from most entries; and `julia-report` was a four-field stub. All of that is fixed below.

**What "complete" means here, stated so it can be falsified:**

| Requirement | How to check it |
|---|---|
| Every PDF carries its **full 64-hex** `sha256` | Compare each against `data/source-manifest/manifest.json`. No truncated hash appears in any entry below |
| Every v1 field has a destination **in an actual entry** | `relativePath`, `pdfMetadata`, `embeddedToc`, `extraction` are present on all 13 |
| **Every** `SELECT` and `CONDITIONAL` source has an entry | **48 entries total = 13 migrated PDFs + 35 new.** The 35 are: all **23 `SELECT`** + all **9 `CONDITIONAL`** (§2.6b) + the **2 `OPTIONAL`** sources that already carry a scoped role and licence (C7, C11) + `julia-report`. The five `OPTIONAL` sources with no assigned module (A9–A12, E8) are deliberately excluded — see §5.2 |
| Every entry carries the decision fields | `cost`, `requiresAccount`, `conditional`, `license` **or** `licenseNote`, `citationUnits`, `roles`, `reuseStatus`, `modules` |
| Every `conditional: true` entry carries **all four** consequence fields | `blocker`, `activationCondition`, `resolutionCeiling`, `ifUnresolved` |
| Every version-like identifier is **immutable or explicitly policy-bound** | Each carries an `*Immutable` boolean; where `false`, a `*PinPolicy` states the exact form required and §5.3 lists it |

`scripts/validate/phase5_plan_consistency.py` parses this block and fails on any violation of the six rows above, so "complete" is machine-checked rather than asserted.

```jsonc
{
  "schemaVersion": 2,
  "generatedBy": "Gate B proposal revision 8 — DRAFT ONLY. Not written to disk, not executed.",
  "sources": [

    // ===================================================================
    // 13 existing Toussaint PDFs, migrated from manifest.json v1.
    // sha256 values are the FULL 64-hex digests copied byte-for-byte from
    // manifest.json — never truncated. Every v1 field has a destination
    // here (see 5.1); none is dropped.
    // ===================================================================

    {
      "sourceId": "lecture-maths",
      "kind": "pdf",
      "filename": "Lecture-Maths.pdf",
      "relativePath": "original notes/Lecture-Maths.pdf",
      "sha256": "e1bb6ef04cb3b88172bc8f73914c5a7289217841bf476d5f2c00417793eb6301",
      "pageCount": 104,
      "pdfMetadata": {
        "title": "Maths for Intelligent Systems", "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20260421143921+02'00'", "modDate": "D:20260421143921+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[lecture-maths].embedded_toc",
                       "entryCount": 145 },
      "extraction": {
        "avgCharsPerPage": 1802.6, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/lecture-maths.md"
      },
      "roles": ["theory", "exercises"],
      "modules": ["MATH-00..MATH-05"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "lecture-optimization",
      "kind": "pdf",
      "filename": "Lecture-Optimization.pdf",
      "relativePath": "original notes/Lecture-Optimization.pdf",
      "sha256": "f0e811311d81c46eef3614ae71a8919d8dd92883a8cc2ef01b7cbdfe3d8de877",
      "pageCount": 128,
      "pdfMetadata": {
        "title": "Introduction to Optimization", "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.18",
        "creationDate": "D:20230207132329+01'00'", "modDate": "D:20230207132329+01'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[lecture-optimization].embedded_toc",
                       "entryCount": 156 },
      "extraction": {
        "avgCharsPerPage": 1222.9, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/lecture-optimization.md"
      },
      "roles": ["theory", "exercises"],
      "modules": ["OPT-01..OPT-06"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "lecture-ai",
      "kind": "pdf",
      "filename": "Lecture-AI.pdf",
      "relativePath": "original notes/Lecture-AI.pdf",
      "sha256": "be696efe2d8b4822c1da9f0e6a90446e08572e2118d1ac978ee3f2b9ba14dd2f",
      "pageCount": 219,
      "pdfMetadata": {
        "title": "Introduction to Artificial Intelligence", "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20260714154944+02'00'", "modDate": "D:20260714154944+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[lecture-ai].embedded_toc",
                       "entryCount": 246 },
      "extraction": {
        "avgCharsPerPage": 1255.0, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/lecture-ai.md"
      },
      "roles": ["theory", "exercises"],
      "modules": ["PROB-01..PROB-06", "PLAN-01..PLAN-04", "SYM-01..SYM-04"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "lecture-machinelearning",
      "kind": "pdf",
      "filename": "Lecture-MachineLearning.pdf",
      "relativePath": "original notes/Lecture-MachineLearning.pdf",
      "sha256": "be4b7df89376e6427babafe0bcc1f1877c1a8bab16f9750651627d95e595268d",
      "pageCount": 139,
      "pdfMetadata": {
        "title": "Introduction to Machine Learning", "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.16",
        "creationDate": "D:20190711202433+02'00'", "modDate": "D:20190711202433+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[lecture-machinelearning].embedded_toc",
                       "entryCount": 40 },
      "extraction": {
        "avgCharsPerPage": 1159.1, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/lecture-machinelearning.md"
      },
      "roles": ["theory", "exercises"],
      "modules": ["ML-01..ML-07"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "lecture-robotics",
      "kind": "pdf",
      "filename": "Lecture-Robotics.pdf",
      "relativePath": "original notes/Lecture-Robotics.pdf",
      "sha256": "f36e0a2bda971a8ec424b6da170af616a1f28a565fbf570fe4f1858d4b75affb",
      "pageCount": 201,
      "pdfMetadata": {
        "title": "Introduction to Robotics", "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.14",
        "creationDate": "D:20161027081845+02'00'", "modDate": "D:20161027081845+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[lecture-robotics].embedded_toc",
                       "entryCount": 49 },
      "extraction": {
        "avgCharsPerPage": 907.5, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/lecture-robotics.md"
      },
      "roles": ["theory", "exercises"],
      "modules": ["KIN-01..KIN-03", "DYN-01..DYN-07", "MANIP-01..MANIP-02"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "lecture-robotlearning",
      "kind": "pdf",
      "filename": "Lecture-RobotLearning.pdf",
      "relativePath": "original notes/Lecture-RobotLearning.pdf",
      "sha256": "0a84aff2726465e29abfde98d6884c6950238b5c70a90009b8d9f5a0c9b5f4d8",
      "pageCount": 137,
      "pdfMetadata": {
        "title": "Robot Learning", "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20250725112918+02'00'", "modDate": "D:20250725112918+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[lecture-robotlearning].embedded_toc",
                       "entryCount": 133 },
      "extraction": {
        "avgCharsPerPage": 1485.4, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/lecture-robotlearning.md"
      },
      "roles": ["theory", "exercises"],
      "modules": ["RL-01..RL-07", "RLEARN-01..RLEARN-09"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "energy",
      "kind": "pdf",
      "filename": "energy.pdf",
      "relativePath": "original notes/energy.pdf",
      "sha256": "83c3aaa4feb79860aece2bbb98f040c3c2d5329674bfeb0729bb5558f51f5b16",
      "pageCount": 3,
      "pdfMetadata": {
        "title": null, "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20260512151431+02'00'", "modDate": "D:20260512151431+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[energy].embedded_toc",
                       "entryCount": 3 },
      "extraction": {
        "avgCharsPerPage": 2430.3, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/energy.md"
      },
      "roles": ["theory"],
      "modules": ["DYN-02"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "entropy",
      "kind": "pdf",
      "filename": "entropy.pdf",
      "relativePath": "original notes/entropy.pdf",
      "sha256": "c94853eede8126dc73ab51b08ac158992bade5e33f16cef9a737ef29deccd30d",
      "pageCount": 2,
      "pdfMetadata": {
        "title": null, "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20260512151431+02'00'", "modDate": "D:20260512151431+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[entropy].embedded_toc",
                       "entryCount": 3 },
      "extraction": {
        "avgCharsPerPage": 3041.5, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/entropy.md"
      },
      "roles": ["theory"],
      "modules": ["PROB-05"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "gaussians",
      "kind": "pdf",
      "filename": "gaussians.pdf",
      "relativePath": "original notes/gaussians.pdf",
      "sha256": "1492c456aed273fb696682ebc6a72dfed72f6ff0d8ecb77adc8a40fcfc975032",
      "pageCount": 4,
      "pdfMetadata": {
        "title": null, "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20260512151432+02'00'", "modDate": "D:20260512151432+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[gaussians].embedded_toc",
                       "entryCount": 15 },
      "extraction": {
        "avgCharsPerPage": 1199.0, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/gaussians.md"
      },
      "roles": ["theory"],
      "modules": ["PROB-03", "ML-05"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "quaternions",
      "kind": "pdf",
      "filename": "quaternions.pdf",
      "relativePath": "original notes/quaternions.pdf",
      "sha256": "adba17bbe0e58feb32cd3821403890e52a2636fb60f0542e42582e85d2722fb3",
      "pageCount": 5,
      "pdfMetadata": {
        "title": null, "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20260512151432+02'00'", "modDate": "D:20260512151432+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[quaternions].embedded_toc",
                       "entryCount": 7 },
      "extraction": {
        "avgCharsPerPage": 2719.4, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/quaternions.md"
      },
      "roles": ["theory"],
      "modules": ["KIN-02"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "robotkin",
      "kind": "pdf",
      "filename": "robotKin.pdf",
      "relativePath": "original notes/robotKin.pdf",
      "sha256": "c4e1651b2e1a322aa88a56a6f603483e6929912ff63ab28f7fdc010602b4bb21",
      "pageCount": 5,
      "pdfMetadata": {
        "title": null, "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20260512151433+02'00'", "modDate": "D:20260512151433+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[robotkin].embedded_toc",
                       "entryCount": 7 },
      "extraction": {
        "avgCharsPerPage": 3643.6, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/robotkin.md"
      },
      "roles": ["theory"],
      "modules": ["KIN-01", "KIN-03"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "splines",
      "kind": "pdf",
      "filename": "splines.pdf",
      "relativePath": "original notes/splines.pdf",
      "sha256": "4350576fcccb8da001f774c0f11b988ce0cddb4982e82c03938e8750462dfd15",
      "pageCount": 7,
      "pdfMetadata": {
        "title": null, "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20260512151433+02'00'", "modDate": "D:20260512151433+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[splines].embedded_toc",
                       "entryCount": 10 },
      "extraction": {
        "avgCharsPerPage": 2482.3, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/splines.md"
      },
      "roles": ["theory"],
      "modules": ["DYN-05"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },

    {
      "sourceId": "svd",
      "kind": "pdf",
      "filename": "svd.pdf",
      "relativePath": "original notes/svd.pdf",
      "sha256": "45e55b7393313a6b09712039458c542e567f02832416a3acfd76eb46552fd854",
      "pageCount": 2,
      "pdfMetadata": {
        "title": null, "author": "Marc Toussaint",
        "subject": null, "producer": "pdfTeX-1.40.25",
        "creationDate": "D:20260512151434+02'00'", "modDate": "D:20260512151434+02'00'"
      },
      "embeddedToc": { "$copyVerbatimFrom": "manifest.json[svd].embedded_toc",
                       "entryCount": 0 },
      "extraction": {
        "avgCharsPerPage": 1756.5, "lowTextPageCount": 0,
        "lowTextPages": [], "likelyScannedOrImagePages": false,
        "rawTextFile": "data/source-manifest/raw-text/svd.md"
      },
      "roles": ["theory"],
      "modules": ["MATH-04"],
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Author-hosted teaching notes, publicly available. No reuse grant stated.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "page range",
      "migratedFrom": "manifest.json v1 — sourceId, sha256, pageCount, relativePath, pdfMetadata, embeddedToc and extraction all carried unchanged"
    },
    // ===================================================================
    // GROUP A — foundation sources (decisions 0006, 0007).  All SELECT.
    // ===================================================================

    {
      "sourceId": "martins-ning-edo", "kind": "web-book",
      "title": "Engineering Design Optimization",
      "authors": ["Joaquim R. R. A. Martins", "Andrew Ning"],
      "publisher": "Cambridge University Press", "edition": "2022", "editionImmutable": true,
      "url": "https://mdobook.github.io/",
      "pdfUrl": "http://flowlab.groups.et.byu.net/mdobook.pdf",
      "accessedAt": "2026-08-15", "pageCount": 642,
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "No content licence stated; free PDF offered by the authors alongside the CUP edition.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "chapter + numbered section",
      "roles": ["theory", "exercises"],
      "modules": ["OPT-01", "OPT-02", "OPT-03", "OPT-04", "OPT-04B", "OPT-05B", "OPT-06", "NUM-03"],
      "anchors": [
        { "id": "s4.3.2", "label": "4.3.2 Strong Wolfe Conditions" },
        { "id": "s4.4.4", "label": "4.4.4 Quasi-Newton Methods (curvature condition)" },
        { "id": "s5.3",   "label": "5.3 Optimality Conditions (constraint qualification)" },
        { "id": "s5.5",   "label": "5.5 Sequential Quadratic Programming" },
        { "id": "s7.3",   "label": "7.3 Nelder-Mead Algorithm" },
        { "id": "s7.4",   "label": "7.4 Generalized Pattern Search" },
        { "id": "s10.6.2","label": "10.6.2 Efficient Global Optimization" },
        { "id": "s11.5",  "label": "11.5 Disciplined Convex Optimization" }
      ],
      "note": "Chapter 7 contains NO CMA-ES; full-text search returns 0 hits. hansen-cmaes-tutorial is the sole CMA-ES authority.",
      "notationConflicts": [] },

    {
      "sourceId": "boyd-convex", "kind": "web-book",
      "title": "Convex Optimization",
      "authors": ["Stephen Boyd", "Lieven Vandenberghe"],
      "publisher": "Cambridge University Press", "edition": "2004", "editionImmutable": true,
      "url": "https://web.stanford.edu/~boyd/cvxbook/", "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Copyright held by Cambridge University Press, who permit the authors to keep the book on the web.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "chapter + section + equation",
      "roles": ["theory"],
      "modules": ["OPT-01", "OPT-03", "OPT-04", "OPT-04B", "PLAN-05", "PLAN-06"],
      "alsoReviewBenchmark": true,
      "notationConflicts": ["lambda-nu-multipliers", "t-barrier-parameter"] },

    {
      "sourceId": "axler-ladr4", "kind": "web-book",
      "title": "Linear Algebra Done Right", "authors": ["Sheldon Axler"],
      "publisher": "Springer (Undergraduate Texts in Mathematics)",
      "edition": "fourth edition", "editionImmutable": true,
      "url": "https://linear.axler.net/", "pdfVersion": "English PDF dated 2026-08-13",
      "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "license": "CC BY-NC", "reuseStatus": "open-licence",
      "citationUnits": "numbered section + numbered result",
      "roles": ["theory"],
      "modules": ["MATH-03", "MATH-03B", "MATH-04"],
      "anchors": [
        { "id": "1",  "label": "Chapter 1 Vector Spaces (axiom list)" },
        { "id": "3F", "label": "3F Duality" },
        { "id": "7C", "label": "7C Positive Operators" },
        { "id": "7E", "label": "7E Singular Value Decomposition" },
        { "id": "7F", "label": "7F Consequences of the SVD (low-rank approximation)" }
      ],
      "notationConflicts": ["V-W-vector-spaces", "T-linear-map"] },

    {
      "sourceId": "fnc-driscoll-braun", "kind": "web-book",
      "title": "Fundamentals of Numerical Computation",
      "authors": ["Tobin A. Driscoll", "Richard J. Braun"],
      "publisher": "SIAM (print editions 2017 MATLAB, 2022 Julia)",
      "edition": "free online edition, Python code path", "editionImmutable": false,
      "editionPinPolicy": "The online edition is living. Pin the accessed build date with every citation; re-verify each cited theorem number on any future access.",
      "url": "https://fncbook.com/", "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "Print editions SIAM copyright; the free online edition states no licence.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "numbered section + numbered theorem",
      "roles": ["theory", "exercises"],
      "modules": ["NUM-03", "OPT-01", "OPT-02", "MATH-03B"],
      "anchors": [
        { "id": "ch1-conditioning", "label": "Ch.1 Problems and conditioning; Stability" },
        { "id": "thm2.9.3", "label": "Theorem 2.9.3 Cholesky factorization" },
        { "id": "thm3.3.3", "label": "Theorem 3.3.3 QR factorization" },
        { "id": "ch7", "label": "Ch.7 Matrix analysis (SVD, dimension reduction)" }
      ],
      "notationConflicts": [] },

    {
      "sourceId": "blondel-roulet-edp", "kind": "preprint",
      "title": "The Elements of Differentiable Programming",
      "authors": ["Mathieu Blondel", "Vincent Roulet"],
      "arxivId": "2403.14606", "version": "v4", "versionImmutable": true,
      "url": "https://arxiv.org/abs/2403.14606v4",
      "versionDate": "2026-08-03", "pageCount": 492, "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "arXiv preprint; no reuse licence identified on the abstract page.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "part + chapter + section + page",
      "roles": ["theory"],
      "modules": ["OPT-04B"],
      "anchors": [
        { "id": "implicit-functions", "label": "Implicit functions (pp. 285-286)" },
        { "id": "envelope", "label": "Envelope theorems, incl. Danskin (pp. 287-291)" },
        { "id": "ift", "label": "Implicit function theorem: univariate, multivariate, JVP/VJP, proof (pp. 291-296)" },
        { "id": "adjoint", "label": "Adjoint state method (pp. 297-300)" },
        { "id": "inverse-fn", "label": "Inverse function theorem; Summary (pp. 303-305)" }
      ],
      "note": "Living draft, pinned at v4. Does NOT cover the KKT active-set-change failure mode; barratt-diffopt is the authority for that.",
      "notationConflicts": ["theta-parameter"] },

    {
      "sourceId": "barratt-diffopt", "kind": "preprint",
      "title": "On the Differentiability of the Solution to Convex Optimization Problems",
      "authors": ["Shane Barratt"],
      "arxivId": "1804.05098", "version": "v3", "versionImmutable": true,
      "url": "https://arxiv.org/abs/1804.05098v3",
      "versionDate": "2019-11-11", "pageCount": 4, "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "arXiv preprint; no reuse licence identified on the abstract page.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "numbered assumption / theorem / equation",
      "roles": ["theory", "citation"],
      "modules": ["OPT-04B"],
      "anchors": [
        { "id": "asm1", "label": "Assumption 1 (Strong duality / Slater)" },
        { "id": "asm2", "label": "Assumption 2 (Differentiability)" },
        { "id": "asm3", "label": "Assumption 3 (Emptiness of G = strict complementarity)" },
        { "id": "thm2.1", "label": "Theorem 2.1 (IFT, quoted from Dontchev & Rockafellar)" },
        { "id": "eq9",  "label": "Eq. (9) Jacobian D_z g" },
        { "id": "thm3.1", "label": "Theorem 3.1 (requires Assumptions 1-3 AND non-singular D_z g)" }
      ],
      "usagePolicy": "Theorem 3.1's two conditions are INDEPENDENT and must be taught as two. The active-set-boundary connection is the workbook's own inference and is tagged newly-authored, never source-adapted.",
      "notationConflicts": ["z-primal-dual-triple", "theta-parameter"] },

    {
      "sourceId": "blondel-implicit-diff", "kind": "preprint",
      "title": "Efficient and Modular Implicit Differentiation",
      "authors": ["Mathieu Blondel", "Quentin Berthet", "Marco Cuturi", "Roy Frostig",
                  "Stephan Hoyer", "Felipe Llinares-Lopez", "Fabian Pedregosa", "Jean-Philippe Vert"],
      "arxivId": "2105.15183", "version": "v5", "versionImmutable": true,
      "url": "https://arxiv.org/abs/2105.15183v5", "versionDate": "2022-10-12",
      "venue": "NeurIPS 2022", "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "arXiv preprint; no reuse licence identified on the abstract page.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "section", "roles": ["citation"],
      "modules": ["OPT-04B"],
      "usagePolicy": "Cited for the optimality-condition formulation. JAX/JAXopt are NOT adopted.",
      "notationConflicts": [] },

    {
      "sourceId": "hansen-cmaes-tutorial", "kind": "preprint",
      "title": "The CMA Evolution Strategy: A Tutorial", "authors": ["Nikolaus Hansen"],
      "arxivId": "1604.00772", "version": "v2", "versionImmutable": true,
      "url": "https://arxiv.org/abs/1604.00772v2", "versionDate": "2023-03-10",
      "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "arXiv preprint; no reuse licence identified on the abstract page.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "section", "roles": ["theory", "citation"],
      "modules": ["OPT-05B"],
      "note": "SOLE CMA-ES authority. martins-ning-edo ch.7 does not cover CMA-ES.",
      "usagePolicy": "Intuition depth only per decision 0007: sampling, covariance adaptation, step-size control. The update algebra is NOT derived.",
      "notationConflicts": ["sigma-step-size", "C-covariance", "m-mean"] },

    {
      "sourceId": "larson-dfo-survey", "kind": "journal-article",
      "title": "Derivative-free optimization methods",
      "authors": ["Jeffrey Larson", "Matt Menickelly", "Stefan M. Wild"],
      "venue": "Acta Numerica 28 (2019) 287-404",
      "arxivId": "1904.11585", "version": "v2", "versionImmutable": true,
      "url": "https://arxiv.org/abs/1904.11585v2", "versionDate": "2019-06-25",
      "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "arXiv preprint of an Acta Numerica article; no reuse licence identified.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "section", "roles": ["theory"],
      "modules": ["OPT-05B"] },

    // ===================================================================
    // GROUP B — applied theory.  Both SELECT.
    // ===================================================================

    {
      "sourceId": "tedrake-underactuated", "kind": "web-book",
      "title": "Underactuated Robotics: Algorithms for Walking, Running, Swimming, Flying, and Manipulation",
      "authors": ["Russ Tedrake"], "publisher": "MIT (course notes for 6.832)",
      "url": "https://underactuated.mit.edu/",
      "edition": "Spring 2024", "editionImmutable": true,
      "structure": { "chapters": 21, "appendices": 5, "sourceUnits": 26 },
      "accessedAt": "2026-08-14", "copyright": "(c) Russ Tedrake, 2024",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "No explicit content licence; citation requested with the author's own BibTeX. Companion repo RussTedrake/underactuated is BSD.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "chapter + section anchor + edition",
      "roles": ["theory", "exercises"],
      "modules": ["UAC-01", "UAC-02", "UAC-03", "UAC-04", "UAC-05", "MANIP-03", "MANIP-05", "DRL-01", "SIM-04"],
      "anchors": [{ "id": "ch9", "label": "Ch. 9 Lyapunov Analysis",
                    "url": "https://underactuated.mit.edu/lyapunov.html" }],
      "usagePolicy": "A future edition is a NEW pinned entry, never an in-place update of this one.",
      "notationConflicts": ["x-state", "R-lqr-input-cost", "Q-lqr-state-cost", "V-lyapunov", "J-cost-functional"] },

    {
      "sourceId": "tedrake-manipulation", "kind": "web-book",
      "title": "Robotic Manipulation: Perception, Planning, and Control",
      "authors": ["Russ Tedrake"], "url": "https://manipulation.mit.edu/",
      "edition": "Fall 2025", "editionImmutable": true,
      "structure": { "chapters": 12, "appendices": 0, "sourceUnits": 12 },
      "accessedAt": "2026-08-14", "copyright": "(c) Russ Tedrake, 2020-2025",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "No explicit content licence; citation requested.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "chapter + section anchor + edition",
      "roles": ["theory", "exercises"],
      "modules": ["PLAN-05", "PLAN-06", "MANIP-04", "SIM-01", "SIM-04", "SIM-05"],
      "usagePolicy": "A future edition is a NEW pinned entry.",
      "notationConflicts": ["C-free-configuration-space"] },

    // ===================================================================
    // GROUP C — API documentation.
    // ===================================================================

    {
      "sourceId": "mujoco-docs", "kind": "documentation",
      "url": "https://mujoco.readthedocs.io/en/stable/",
      "packageVersion": "3.11.0", "packageVersionImmutable": true,
      "accessedAt": "2026-08-14", "maintainer": "Google DeepMind",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "license": "Apache-2.0 (code); CC BY 4.0 (documentation in doc/)",
      "reuseStatus": "open-licence", "roles": ["api", "implementation"],
      "citationUnits": "documentation page + anchor + package version",
      "modules": ["SIM-01", "SIM-02", "SIM-03", "SIM-04", "SIM-05", "MANIP-03", "MANIP-04", "DRL-06", "DRL-07"],
      "notationConflicts": ["qpos-qvel-ctrl"] },

    {
      "sourceId": "gymnasium-docs", "kind": "documentation",
      "url": "https://gymnasium.farama.org/",
      "packageVersion": "1.3.0", "packageVersionImmutable": true,
      "accessedAt": "2026-08-14", "maintainer": "Farama Foundation",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "license": "MIT", "reuseStatus": "open-licence", "roles": ["api"],
      "citationUnits": "documentation page + anchor + package version",
      "modules": ["SIM-03", "SIM-06", "DRL-01", "DRL-02", "DRL-03", "DRL-04", "DRL-05", "DRL-06", "DRL-07"] },

    {
      "sourceId": "pytorch-docs", "kind": "documentation",
      "url": "https://pytorch.org/docs/",
      "packageVersion": "2.13.0", "packageVersionImmutable": true,
      "accessedAt": "2026-08-14", "maintainer": "PyTorch Foundation",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "license": "BSD-3-Clause (code)", "reuseStatus": "open-licence", "roles": ["api"],
      "citationUnits": "documentation page + anchor + package version",
      "modules": ["NUM-02", "ACC-01", "ACC-02", "ACC-03", "ACC-04", "ML-01", "DRL-02", "DRL-03"] },

    {
      "sourceId": "numpy-scipy-docs", "kind": "documentation",
      "url": "https://numpy.org/doc/", "secondaryUrl": "https://docs.scipy.org/doc/scipy/",
      "packageVersion": null, "packageVersionImmutable": false,
      "packageVersionPinPolicy": "Pinned to the exact numpy and scipy versions the Gate-D `core` dependency layer resolves, recorded as two explicit version strings. Unpinned here because that layer does not exist yet; the documentation SOURCE is pinned by URL and this does not affect any Gate B decision (5.3, item 3).",
      "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "license": "BSD-3-Clause", "reuseStatus": "open-licence", "roles": ["api"],
      "citationUnits": "documentation page + anchor + package version",
      "modules": ["NUM-01", "NUM-02", "NUM-03", "OPT-04B", "OPT-05B"] },

    {
      "sourceId": "mjx-docs", "kind": "documentation",
      "url": "https://mujoco.readthedocs.io/en/stable/mjx.html",
      "packageVersion": "3.11.0", "packageVersionImmutable": true,
      "accessedAt": "2026-08-14",
      "maintainer": "Google DeepMind",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "license": "Apache-2.0 (code); CC BY 4.0 (docs)",
      "reuseStatus": "open-licence", "roles": ["api"],
      "citationUnits": "documentation page + anchor + package version",
      "scopeRestriction": "SIM-06 optional CUDA extension and ACC-05 only.",
      "modules": ["SIM-06", "ACC-05"] },

    {
      "sourceId": "mjwarp-docs", "kind": "documentation",
      "url": "https://mujoco.readthedocs.io/en/latest/mjwarp/",
      "repository": "https://github.com/google-deepmind/mujoco_warp",
      "gitRef": null, "gitRefImmutable": false,
      "gitRefPinPolicy": "A 40-hex commit SHA, recorded only if and when the blocker below is resolved.",
      "accessedAt": "2026-08-14", "maintainer": "NVIDIA + Google DeepMind",
      "cost": "free", "requiresAccount": false,
      "license": "Apache-2.0", "reuseStatus": "open-licence", "roles": ["api"],
      "citationUnits": "documentation page + anchor + git ref",
      "modules": ["SIM-06"],
      "conditional": true,
      "blocker": "Install path unconfirmed; no plain `pip install mujoco-warp` established.",
      "activationCondition": "Gate-D evaluation-only measurement on the 5090 under plan 9.9.1: one reproducible documented install plus one working rollout.",
      "resolutionCeiling": "One install attempt and one rollout check. Exceeding it resolves the blocker as UNRESOLVED.",
      "ifUnresolved": "SIM-06's optional MJWarp extension is cut; its required CPU vector-env half is unaffected and the main-route module still ships." },

    {
      "sourceId": "mujoco-playground", "kind": "documentation",
      "url": "https://github.com/google-deepmind/mujoco_playground", "accessedAt": "2026-08-14",
      "gitRef": null, "gitRefImmutable": false,
      "gitRefPinPolicy": "A 40-hex commit SHA, recorded if the owner opts this source in at Gate C.",
      "maintainer": "Google DeepMind",
      "cost": "free", "requiresAccount": false,
      "license": "Apache-2.0", "reuseStatus": "open-licence", "roles": ["api"],
      "citationUnits": "repository path + git ref",
      "scopeRestriction": "SIM-06 reference only.",
      "modules": ["SIM-06"],
      "conditional": false,
      "optional": true,
      "optionalReason": "Fully evaluated: licence Apache-2.0 and role both known, so there is NO blocker (plan 9.9). Not proposed by default because it duplicates mujoco-docs/mjx-docs at the one place it would be used, and the owner has not committed to the SIM-06 optional extension. Opting it in is a Gate C scope decision.",
      "correctedAtProposalRevision4": "Revision 3 marked this CONDITIONAL on 'licence and role unconfirmed'. Both were known. Optionality is not a blocker." },

    {
      "sourceId": "triton-docs", "kind": "documentation",
      "url": "https://triton-lang.org/", "accessedAt": "2026-08-14",
      "packageVersion": null, "packageVersionImmutable": false,
      "packageVersionPinPolicy": "Exact triton version, recorded only if the blocker below is resolved.",
      "cost": "free", "requiresAccount": false,
      "license": "MIT", "reuseStatus": "open-licence", "roles": ["api"],
      "citationUnits": "documentation page + anchor + package version",
      "scopeRestriction": "ACC-06 only - Tier 3, cuda-required. Nothing main-route may depend on it.",
      "modules": ["ACC-06"],
      "conditional": true,
      "blocker": "Exact compute-capability support for sm_120 is unconfirmed; the repository's compatibility table has not been read.",
      "activationCondition": "Gate-D evaluation-only measurement under plan 9.9.1: install, compile one kernel, check correctness against eager PyTorch on the 5090.",
      "resolutionCeiling": "One install and one kernel-correctness check.",
      "ifUnresolved": "ACC-06 is cut entirely. It is Tier 3 and nothing on the main route depends on it." },

    {
      "sourceId": "drake-docs", "kind": "documentation",
      "url": "https://drake.mit.edu/", "accessedAt": "2026-08-14",
      "packageVersion": null, "packageVersionImmutable": false,
      "packageVersionPinPolicy": "Exact pinned Drake release, recorded only if the blocker below is resolved.",
      "maintainer": "Toyota Research Institute / MIT (RobotLocomotion)",
      "cost": "free", "requiresAccount": false,
      "license": "BSD-3-Clause", "reuseStatus": "open-licence", "roles": ["api"],
      "citationUnits": "documentation page + C++/Python API symbol + release",
      "scopeRestriction": "PLAN-05, PLAN-06, CAP-02 only. Every Drake lab keeps a NumPy/SciPy fallback.",
      "modules": ["PLAN-05", "PLAN-06", "CAP-02"],
      "conditional": true,
      "blocker": "Whether a reproducible pinned install on this host costs less than the plan's stated budget. (The LICENCE blocker is RESOLVED: BSD-3-Clause per RobotLocomotion/drake LICENSE.TXT.)",
      "activationCondition": "Gate-D evaluation-only measurement under plan 9.9.1 showing install and version pinning reproducible within plan 16.2's half-day ceiling.",
      "resolutionCeiling": "Half a day (plan 16.2's explicit drop criterion).",
      "ifUnresolved": "Drake is dropped entirely; the NumPy/SciPy fallback becomes primary. Per plan 16.2 this costs the connection to the field's reference GCS implementation but NO concept, derivation or exercise." },

    {
      "sourceId": "lerobot-docs", "kind": "documentation",
      "url": "https://huggingface.co/docs/lerobot", "accessedAt": "2026-08-14",
      "packageVersion": null, "packageVersionImmutable": false,
      "packageVersionPinPolicy": "Exact lerobot release, recorded only if the blocker below is resolved.",
      "maintainer": "Hugging Face",
      "cost": "free",
      "requiresAccount": false,
      "requiresAccountNote": "Documentation and ungated public datasets need no account. A GATED dataset would need a free HF account: permitted by plan 2.10, NOT assumed, and recorded per dataset as requiresAccount: true with a visible note on /sources.",
      "license": "Apache-2.0 (library)",
      "reuseStatus": "open-licence", "roles": ["api", "case-study"],
      "citationUnits": "documentation page + anchor; datasets by dataset id + revision",
      "scopeRestriction": "DRL-08 only - Tier 3.",
      "modules": ["DRL-08"],
      "conditional": true,
      "blocker": "Whether the specific datasets DRL-08 would use are ungated.",
      "activationCondition": "Per-dataset Gate-D evaluation-only reachability check under plan 9.9.1 confirming ungated status, or an explicit owner decision accepting a free account for one NAMED gated dataset. Never scheduled for acquisition time: a CONDITIONAL source is ineligible for acquisition until this blocker resolves (plan 9.9, 9.9.1).",
      "resolutionCeiling": "One reachability check per candidate dataset.",
      "ifUnresolved": "DRL-08 is cut or re-scoped to a non-LeRobot dataset. Tier 3, no main-route consequence." },

    {
      "sourceId": "jax-docs", "kind": "documentation",
      "url": "https://docs.jax.dev/", "accessedAt": "2026-08-15",
      "packageVersion": null, "packageVersionImmutable": false,
      "packageVersionPinPolicy": "Exact jax version, recorded if the owner opts ACC-05 in at Gate C.",
      "cost": "free", "requiresAccount": false,
      "license": "Apache-2.0", "reuseStatus": "open-licence", "roles": ["api"],
      "citationUnits": "documentation page + anchor + package version",
      "scopeRestriction": "ACC-05 only - Tier 3 decision module.",
      "modules": ["ACC-05"],
      "conditional": false,
      "optional": true,
      "optionalReason": "Fully evaluated: licence Apache-2.0 and role both known, so there is NO blocker. Not proposed by default because ACC-05 is a Tier-3 module the owner may not build. Opting it in is a Gate C scope decision.",
      "correctedAtProposalRevision4": "Revision 3 listed the blocker as 'none beyond ACC-05 being Tier 3', which is the definition of OPTIONAL, not a blocker." },

    {
      "sourceId": "mujoco-menagerie", "kind": "model-collection",
      "scoredAs": "D3",
      "url": "https://github.com/google-deepmind/mujoco_menagerie", "accessedAt": "2026-08-15",
      "gitRef": null, "gitRefImmutable": false,
      "gitRefPinPolicy": "A 40-hex commit SHA, recorded per model actually used.",
      "cost": "free", "requiresAccount": false,
      "license": "Apache-2.0 for repository content; INDIVIDUAL MODELS CARRY THEIR OWN LICENCES",
      "reuseStatus": "per-item-licence",
      "citationUnits": "model directory + that model's own LICENSE + git ref",
      "roles": ["case-study"],
      "modules": ["SIM-02", "SIM-05"],
      "usagePolicy": "Each model directory has its own LICENSE file. Record the licence PER MODEL used. NEVER make an aggregate licence claim.",
      "conditional": true,
      "blocker": "Per-model licences differ and none has been read.",
      "activationCondition": "PER MODEL: read and record that model's own LICENSE before that model is used.",
      "resolutionCeiling": "One LICENSE read per model. Resolution is per model and never generalizes to the collection.",
      "ifUnresolved": "Only models whose individual licence has been read and recorded may be used. Unread models are simply not used." },

    // ===================================================================
    // GROUP D — reference implementations.
    // ===================================================================

    {
      "sourceId": "cleanrl", "kind": "reference-implementation",
      "url": "https://github.com/vwxyzjn/cleanrl",
      "gitRef": null, "gitRefImmutable": false,
      "gitRefPinPolicy": "A 40-hex commit SHA recorded at acquisition. A branch name or tag is NOT acceptable as the pin; the repository URL is what Gate B decides (5.3, item 1).",
      "accessedAt": "2026-08-14",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "license": "MIT", "reuseStatus": "open-licence",
      "roles": ["implementation"],
      "citationUnits": "file + line range + git ref",
      "files": ["dqn.py", "ppo.py", "sac_continuous_action.py"],
      "filesNote": "CleanRL has NO file named sac.py. The continuous-control SAC single-file implementation is sac_continuous_action.py. Proposal revision 3 named sac.py; corrected at revision 4.",
      "modules": ["DRL-03", "DRL-05", "DRL-06"],
      "usagePolicy": "read-and-compare; do NOT vendor code without a per-file provenance header naming source, URL, git ref and what was changed." },

    {
      "sourceId": "stable-baselines3", "kind": "reference-implementation",
      "url": "https://github.com/DLR-RM/stable-baselines3",
      "gitRef": null, "gitRefImmutable": false,
      "gitRefPinPolicy": "A 40-hex commit SHA recorded at acquisition.",
      "accessedAt": "2026-08-14",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "license": "MIT", "reuseStatus": "open-licence",
      "roles": ["implementation"],
      "citationUnits": "file + line range + git ref",
      "files": ["stable_baselines3/sac/sac.py"],
      "scopeRestriction": "Comparison target in DRL-06 only.",
      "modules": ["DRL-06"],
      "usagePolicy": "read-and-compare; no vendoring without a per-file provenance header." },

    // ===================================================================
    // GROUP E — papers.  Citation role throughout.
    // ===================================================================

    {
      "sourceId": "schulman-ppo", "kind": "preprint",
      "title": "Proximal Policy Optimization Algorithms",
      "authors": ["John Schulman", "Filip Wolski", "Prafulla Dhariwal", "Alec Radford", "Oleg Klimov"],
      "arxivId": "1707.06347", "version": null, "versionImmutable": false,
      "versionPinPolicy": "An explicit arXiv version suffix (e.g. v2) recorded at acquisition and cited as https://arxiv.org/abs/1707.06347vN. The PAPER is pinned immutably by its arXiv ID, which is verified; only the version suffix is open (5.3, item 2).",
      "url": "https://arxiv.org/abs/1707.06347",
      "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "arXiv preprint; no reuse licence identified.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "section + equation", "roles": ["citation"],
      "modules": ["DRL-05"],
      "notationConflicts": ["pi-theta-policy"] },

    {
      "sourceId": "chi-diffusion-policy", "kind": "preprint",
      "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
      "authors": ["Cheng Chi", "Siyuan Feng", "Yilun Du", "Zhenjia Xu", "Eric Cousineau",
                  "Benjamin Burchfiel", "Shuran Song"],
      "arxivId": "2303.04137", "version": null, "versionImmutable": false,
      "versionPinPolicy": "An explicit arXiv version suffix recorded at acquisition; v4 and v5 both exist. The PAPER is pinned by its verified arXiv ID (5.3, item 2).",
      "url": "https://arxiv.org/abs/2303.04137",
      "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "arXiv preprint; no reuse licence identified.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "section", "roles": ["citation"],
      "modules": ["DRL-08"] },

    {
      "sourceId": "ross-dagger", "kind": "conference-paper",
      "title": "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning",
      "authors": ["Stephane Ross", "Geoffrey J. Gordon", "J. Andrew Bagnell"],
      "venue": "AISTATS 2011, PMLR v15", "venueImmutable": true,
      "url": "https://proceedings.mlr.press/v15/ross11a.html", "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "PMLR proceedings page; copyright retained by the authors.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "theorem + assumption", "roles": ["citation"],
      "modules": ["RLEARN-02", "DRL-07"],
      "alsoReviewBenchmark": true,
      "usagePolicy": "Anchors RLEARN-02's mandatory RLN02-02 repair: the theorem's ASSUMPTIONS must be stated, not just its name." },

    {
      "sourceId": "haarnoja-sac", "kind": "conference-paper",
      "title": "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor",
      "authors": ["Tuomas Haarnoja", "Aurick Zhou", "Pieter Abbeel", "Sergey Levine"],
      "venue": "ICML 2018, PMLR v80, pp. 1861-1870", "venueImmutable": true,
      "url": "https://proceedings.mlr.press/v80/haarnoja18b.html",
      "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false, "conditional": false,
      "licenseNote": "PMLR proceedings page; copyright retained by the authors.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "section + equation", "roles": ["citation"],
      "modules": ["DRL-06"],
      "note": "PRIMARY SAC citation. Sufficient on its own for DRL-06 as currently scoped.",
      "notationConflicts": ["alpha-entropy-temperature"] },

    {
      "sourceId": "haarnoja-sac-apps", "kind": "preprint",
      "title": "Soft Actor-Critic Algorithms and Applications",
      "authors": ["Tuomas Haarnoja", "Aurick Zhou", "Kristian Hartikainen", "George Tucker",
                  "Sehoon Ha", "Jie Tan", "Vikash Kumar", "Henry Zhu", "Abhishek Gupta",
                  "Pieter Abbeel", "Sergey Levine"],
      "arxivId": "1812.05905", "version": null, "versionImmutable": false,
      "versionPinPolicy": "Version suffix recorded only if the blocker below resolves.",
      "url": "https://arxiv.org/abs/1812.05905", "accessedAt": "2026-08-15",
      "cost": "free", "requiresAccount": false,
      "licenseNote": "arXiv preprint; no reuse licence identified.",
      "reuseStatus": "consultation-and-citation-only",
      "citationUnits": "section + equation", "roles": ["citation"],
      "modules": ["DRL-06"],
      "conditional": true,
      "blocker": "A SCOPE question, not a defect: this paper is needed only if DRL-06 teaches automatic entropy-temperature tuning or the later modifications.",
      "activationCondition": "A Gate-C decision that DRL-06's scope includes automatic temperature tuning.",
      "resolutionCeiling": "None applicable - resolved by a scope decision, not by measurement.",
      "ifUnresolved": "Not added. haarnoja-sac (ICML 2018) alone is sufficient for SAC as DRL-06 is currently scoped." },

    {
      "sourceId": "mnih-dqn", "kind": "journal-article",
      "title": "Human-level control through deep reinforcement learning",
      "authors": ["Volodymyr Mnih", "Koray Kavukcuoglu", "David Silver", "Andrei A. Rusu",
                  "Joel Veness", "Marc G. Bellemare", "Alex Graves", "Martin Riedmiller",
                  "Andreas K. Fidjeland", "Georg Ostrovski", "et al."],
      "venue": "Nature 518, 529-533", "venueImmutable": true,
      "publicationDate": "2015-02-26", "doi": "10.1038/nature14236",
      "url": "https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf",
      "accessedAt": "2026-08-15", "pageCount": 13,
      "cost": "free", "requiresAccount": false, "conditional": false,
      "copyright": "Macmillan Publishers Limited. All rights reserved (c)2015",
      "license": "All rights reserved",
      "reuseStatus": "all-rights-reserved",
      "citationUnits": "section + figure number", "roles": ["citation"],
      "modules": ["DRL-03"],
      "usagePolicy": "CITATION ONLY. No reuse of prose or figures. NEVER required reading. The mechanism is taught from cleanrl dqn.py plus newly-authored exposition." },

    {
      "sourceId": "deits-tedrake-iris", "kind": "conference-paper",
      "title": "Computing Large Convex Regions of Obstacle-Free Space through Semidefinite Programming",
      "authors": ["Robin Deits", "Russ Tedrake"],
      "venue": "Workshop on the Algorithmic Foundations of Robotics (WAFR) 2014",
      "venueImmutable": false,
      "url": null,
      "urlPinPolicy": "A stable official URL (publisher DOI or the authors' MIT-hosted PDF) recorded at acquisition - which this source can only reach after its blocker is resolved under plan 9.9.1.",
      "accessedAt": null,
      "cost": "free", "requiresAccount": false,
      "licenseNote": "Not yet read; licence unknown pending the locator.",
      "reuseStatus": "unknown-pending-licence-read",
      "citationUnits": "section + algorithm", "roles": ["citation"],
      "modules": ["PLAN-05"],
      "recordedFromPriorKnowledgeNotFetch": "Title, authors and venue are recorded from prior knowledge and are NOT verified. They must be confirmed against the official record by the plan 9.9.1 Gate-D evaluation-only fetch/read, together with the URL. This is part of the blocker below, not separate from it, and it precedes any acquisition rather than happening at one.",
      "conditional": true,
      "blocker": "The exact paper version and a stable official locator are unpinned; the source has not been fetched or read.",
      "activationCondition": "An official URL and version verified, plus a licence read, by the plan 9.9.1 Gate-D evaluation-only fetch/read, and accepted by the owner. Pinning into sources.json is a separate later Gate-D acquisition step that becomes possible only once this blocker is resolved.",
      "resolutionCeiling": "One locator-verification fetch under plan 9.9.1.",
      "ifUnresolved": "tedrake-manipulation ch.6 covers the IRIS material and PLAN-05 stands on it. This paper becomes 'further reading', never a citation." },

    {
      "sourceId": "marcucci-gcs", "kind": "journal-article",
      "title": "Motion Planning around Obstacles with Convex Optimization",
      "authors": ["Tobia Marcucci", "Mark Petersen", "David von Wrangel", "Russ Tedrake"],
      "venue": "Science Robotics (version to be pinned)", "venueImmutable": false,
      "url": null,
      "urlPinPolicy": "A stable official URL or DOI recorded at acquisition - which this source can only reach after its blocker is resolved under plan 9.9.1 - or an arXiv preprint version if that is what is adopted.",
      "accessedAt": null,
      "cost": "free", "requiresAccount": false,
      "licenseNote": "Not yet read; licence unknown pending the locator.",
      "reuseStatus": "unknown-pending-licence-read",
      "citationUnits": "section + formulation", "roles": ["citation"],
      "modules": ["PLAN-06"],
      "recordedFromPriorKnowledgeNotFetch": "Title, authors and venue are recorded from prior knowledge and are NOT verified. They must be confirmed against the official record by the plan 9.9.1 Gate-D evaluation-only fetch/read, together with the URL. This is part of the blocker below, not separate from it, and it precedes any acquisition rather than happening at one.",
      "conditional": true,
      "blocker": "The exact paper version and a stable official locator are unpinned; the source has not been fetched or read.",
      "activationCondition": "An official URL and version verified, plus a licence read, by the plan 9.9.1 Gate-D evaluation-only fetch/read, and accepted by the owner. Pinning into sources.json is a separate later Gate-D acquisition step that becomes possible only once this blocker is resolved.",
      "resolutionCeiling": "One locator-verification fetch under plan 9.9.1.",
      "ifUnresolved": "tedrake-manipulation ch.6 covers the GCS material and PLAN-06 stands on it. This paper becomes 'further reading', never a citation." },

    {
      "sourceId": "sutton-barto-2e", "kind": "web-book",
      "title": "Reinforcement Learning: An Introduction",
      "authors": ["Richard S. Sutton", "Andrew G. Barto"],
      "publisher": "MIT Press", "edition": "second edition, 2018", "editionImmutable": true,
      "url": "http://incompleteideas.net/book/the-book-2nd.html",
      "accessedAt": null,
      "cost": "free",
      "requiresAccount": false,
      "licenseNote": "Author-hosted free PDF of a MIT Press book; terms not read because the page could not be reached.",
      "reuseStatus": "unknown-pending-licence-read",
      "citationUnits": "chapter + numbered section", "roles": ["citation"],
      "modules": ["DRL-01", "DRL-02", "DRL-03"],
      "conditional": true,
      "blocker": "Official free-PDF reachability is unconfirmed: incompleteideas.net failed with a self-signed certificate on 2026-08-14.",
      "activationCondition": "A successful plan 9.9.1 Gate-D evaluation-only fetch from the official page, followed by a licence read.",
      "resolutionCeiling": "One Gate-D evaluation-only re-attempt under plan 9.9.1.",
      "ifUnresolved": "DRL cross-references stand on tedrake-underactuated, cleanrl and the existing RL block. NO paywalled substitute is adopted, and no purchase is proposed." },

    // ===================================================================
    // PERSONAL — closes the julia-report hole (plan 2.5, 15).
    // ===================================================================

    {
      "sourceId": "julia-report", "kind": "personal-document",
      "title": "CDT-D2AIR Year-1 Final Scientific Report",
      "authors": ["Julia Lopez Gomez"],
      "institution": "CDT-D2AIR",
      "documentDate": null,
      "documentDatePinPolicy": "The report's own date, recorded from the document when it is located.",
      "url": null,
      "locationPolicy": "Owner-held document. It is NOT fetched, NOT copied into the repository, and NOT committed; the entry exists so the three exercises that already reference this sourceId resolve.",
      "accessedAt": null,
      "cost": "free", "requiresAccount": false, "conditional": false,
      "license": "Owner-owned", "reuseStatus": "owner-owned",
      "citationUnits": "section",
      "roles": ["case-study"],
      "modules": ["CAP-01", "CAP-02"],
      "referencedByExerciseCount": 3,
      "note": "Fixes the currently-unmanifested sourceId found on 3 exercises (plan 2.5). Creating this entry is Gate-D migration work, not a Gate-B source approval: the owner's own document needs no external approval."
    }
  ]
}
```

### 5.1 v1 → v2 field mapping (complete)

Every v1 field has a defined destination **and appears in every one of the 13 migrated entries above** — that is the part revision 3 asserted and did not deliver. **No v1 data is dropped**, and the 13 PDF entries keep their `source_id` and `sha256` so existing citations continue to resolve.

| v1 field (`manifest.json`) | v2 field (`sources.json`) | Transform |
|---|---|---|
| `source_id` | `sourceId` | Renamed to camelCase; **value unchanged** — this is what keeps existing `sourceRef`s valid |
| `filename` | `filename` | Unchanged; meaningful only for `kind: "pdf"` |
| `relative_path` | `relativePath` | Renamed; **present on all 13 entries above** |
| `sha256` | `sha256` | **Unchanged, byte-for-byte, full 64 hex characters.** The integrity guarantee is the point of the migration |
| `page_count` | `pageCount` | Renamed; PDFs only |
| `pdf_metadata` | `pdfMetadata` | Renamed; keys camelCased, **values verbatim**; present on all 13 |
| `embedded_toc` | `embeddedToc` | Renamed; **copied verbatim.** The draft carries `$copyVerbatimFrom` plus the measured `entryCount` rather than reprinting all 814 TOC rows inside a proposal — the validator checks each `entryCount` against `manifest.json`, so the assertion is falsifiable rather than elided |
| `extraction` | `extraction` | Renamed; keys camelCased, **values verbatim and fully inlined** on all 13 |
| — | **`kind`** | **New, required.** All 13 existing entries become `"pdf"`. New values: `web-book`, `documentation`, `preprint`, `journal-article`, `conference-paper`, `reference-implementation`, `model-collection`, `personal-document` |
| — | **`roles`** | **New, required.** Array from theory / exercises / api / implementation / citation / case-study |
| — | **`reuseStatus`** | **New, required** (plan §9.8): `open-licence`, `consultation-and-citation-only`, `all-rights-reserved`, `per-item-licence`, `owner-owned`, `unknown-pending-licence-read` |
| — | **`accessedAt`** | **New; required for every non-PDF kind that has actually been accessed.** `null` where the source has deliberately not been fetched — which is only ever true of a `CONDITIONAL` entry |
| — | **`cost`** | **New, required.** `"free"` for every source in this proposal. No paid tier, subscription or API key appears anywhere |
| — | **`license` / `licenseNote`** | **New; one or the other required.** `license` where terms are stated; `licenseNote` where they are inferable but not formally granted |
| — | **`citationUnits`** | **New, required.** What a locator means for this source |
| — | **`modules`** | **New, required.** The modules this source may serve. Narrower than `scopeRestriction`, which is a hard limit; `modules` is the mapping Gate C consumes |
| — | `anchors[]` | New, optional; stable named locators |
| — | `notationConflicts[]` | New; keys into §4's register, consumed by Gate C's `notation.json` |
| — | **`requiresAccount`** | **New, required.** `false` for every source in this proposal. Only a later, named gated LeRobot dataset could set it `true`, recorded per dataset |
| — | **`conditional`** | **New, required.** `true` marks a source that is **not approved** (§2.6) |
| — | **`blocker` / `activationCondition` / `resolutionCeiling` / `ifUnresolved`** | **New; all four required whenever `conditional: true`.** A conditional entry missing any of them is malformed. `resolutionCeiling` is new at revision 4 and implements plan §9.9.1 |
| — | **`optional` / `optionalReason`** | **New at revision 4.** Marks a fully-evaluated source that is not proposed by default (§2.6a). **Distinct from `conditional`** — an `optional` source has no blocker |
| — | `*Immutable` / `*PinPolicy` | **New at revision 4.** Every version, edition, git ref or venue field carries a boolean saying whether it is immutable; where it is not, the paired policy field states the exact form the pin must take |
| — | `scopeRestriction` | New, optional; a hard limit on which modules a narrowly justified source may serve |
| — | `usagePolicy` | New, optional; e.g. read-and-compare, no vendoring without a provenance header |
| `externalSources` free text *(module frontmatter, not the manifest)* | structured entries | **Deprecated and migrated.** This closes the `julia-report` hole — three exercises reference a `sourceId` that resolves nowhere today |
| `sources[].pages` *(module frontmatter)* | **`sources[].locator`** | Free string interpreted per `kind`: `"p14-16"` PDF · `"ch9 §9.3"` web book · `"Theorem 3.3.3"` numbered book · `"Assumption 3"` short paper · `"§4.3.2"` sectioned book · `"XMLreference#actuator"` docs · `"ppo.py L120-160"` implementations |

**Migration acceptance (Gate D):** all 13 `source_id`s resolve after migration; all 13 `sha256` values are unchanged and full-length; all 13 `embeddedToc` entry counts match `manifest.json`; every `kind`, `roles`, `reuseStatus`, `cost`, `requiresAccount`, `citationUnits`, `modules` and `conditional` field is populated; every `conditional: true` entry has all four consequence fields; every non-immutable version field has a pin policy; and `julia-report` resolves.

### 5.2 What this draft deliberately does not contain

**Stated as a boundary, not as a gap.** None of the following is missing data — each is excluded on purpose:

- **No `OPTIONAL` source that has no assigned module** — A9, A10, A11, A12 and E8 are scored in §2 and described in §2.6a, but they get no `sources.json` entry until the owner opts one in at Gate C. Writing entries for sources nobody has committed to would misrepresent the corpus.
- **No extracted text of any kind.** No `raw-text/`, no `html-text/`, no quoted prose (plan §9.8).
- **No `locator` values on modules.** Which module cites which page is a Gate C assignment.
- **The 13 `embeddedToc` arrays are referenced, not reprinted** — see §5.1.

### 5.3 Every field that is not yet pinned, what it affects, and whether it blocks

**Revision 3 claimed "exactly three fields" carried a `TBD-at-acquisition` marker and that everything needed was present "for every source". Both claims were false** once E9a/E9b/E10 and the missing decision fields are counted. The claims are withdrawn. This is the complete list.

| # | Field | Sources | Why it is not pinned now | **Does it block a Gate B decision?** |
|---|---|---|---|---|
| 1 | `gitRef` | `cleanrl`, `stable-baselines3`, `mjwarp-docs`, `mujoco-playground`, `mujoco-menagerie` | A commit SHA does not exist until the repository is cloned. Cloning is Gate D | **No.** The *repository*, its licence and its role are pinned, and those are what Gate B decides |
| 2 | `version` (arXiv suffix) | `schulman-ppo`, `chi-diffusion-policy`, `haarnoja-sac-apps` | Multiple arXiv versions exist and the choice is made when the PDF is fetched | **No.** Each paper is pinned immutably by its verified arXiv ID. *(Contrast A5, A5b, A6, A7, A8, which **are** version-pinned because their versions were read.)* |
| 3 | `packageVersion` | `numpy-scipy-docs`, `triton-docs`, `drake-docs`, `lerobot-docs`, `jax-docs` | Resolved by the Gate-D dependency layer, which does not exist | **No.** The documentation source is pinned by URL |
| 4 | `url`, `accessedAt`, title/author/venue | `deits-tedrake-iris`, `marcucci-gcs` | **These sources have not been fetched or read.** Their recorded metadata is prior knowledge, explicitly flagged as unverified in the entry | **They block *those two sources*, which is exactly why both are `CONDITIONAL`** (§2.6, O5). They block nothing else: `tedrake-manipulation` ch.6 covers the material |
| 5 | `accessedAt`, licence terms | `sutton-barto-2e` | The official page failed with a self-signed certificate on 2026-08-14 | **Blocks that source only** (§2.6, O6). It is `CONDITIONAL` and DRL stands on B1/D1 without it |
| 6 | `documentDate` | `julia-report` | The owner's own document has not been located in this session | **No.** It is owner-owned and needs no external approval; the entry exists to close a dangling `sourceId` |
| 7 | Per-model `LICENSE` | `mujoco-menagerie` (**D3**) | Each model directory carries its own licence and none has been read | **Blocks each model individually** (§2.6, O7). No aggregate claim is ever made |

**The honest summary, replacing revision 3's overclaim:** every field needed to decide **Group A** — the subset a partial approval would cover — is present and verified. **Five sources (`mjwarp-docs`, `triton-docs`, `drake-docs`, `lerobot-docs`, plus `mujoco-menagerie` per model) and four papers (`deits-tedrake-iris`, `marcucci-gcs`, `sutton-barto-2e`, `haarnoja-sac-apps`) carry named blockers and are `CONDITIONAL` precisely because they are not fully decidable today.** That is the taxonomy working, not a hole in the proposal.

---

## 6. Coverage matrix (plan §9.4)

Plan §9.4 requires a `SOURCE_COVERAGE.md` matrix with **one row per source unit** and four columns: **covering module(s) · disposition · reason · notation conflicts introduced.**

**Materialized at proposal revision 4.** Revision 3 called this a "skeleton", carried **two** columns in §6.1–§6.4, and asserted totals it never wrote out — most visibly §6.5's claim that "the matrix reproduces 38 rows" with no 38 rows anywhere. **Every row below is now written, with all four columns.** Dispositions: **teach here** · **route → {module}** · **optional reference** · **intentionally omit** · **reference-only** (documentation) · **REUSE / EXTEND / SKIP / Tier-4 stub** (Tedrake, per plan §3.3).

**Unit rule, stated so the row count is checkable.** One row per **chapter or appendix** for books; per **numbered section** where a chapter splits across dispositions — in which case the section rows **replace** the chapter row rather than adding to it, so nothing is double-counted; per **documentation page**; per **file** for reference implementations; per **claim** for papers.

| Source | Unit | **Rows** | Changed at revision 4? |
|---|---|---:|---|
| A1 Martins & Ning | chapter (9 whole) + section (25, inside ch.4/5/7/11) | **34** | **Yes** — revision 3 said "13 + 22" |
| A2 Boyd & Vandenberghe | chapter (11) + appendix (3) | **14** | **Yes** — count was right, the table had 12 rows |
| A3 Axler | chapter (7 whole) + section (§3A–3F, §7A–7F) | **19** | **Yes** — revision 3 said 13 |
| A4 Driscoll & Braun | chapter | **13** | No |
| A5 Blondel & Roulet | section (6) + one whole-book omission row | **7** | No |
| A5b Barratt | numbered assumption / theorem / equation | **6** | No |
| A6 · A7 · A8 | section | **3 · 5 · 6** | No |
| **B1 Underactuated** | **chapter (21) + appendix A–E (5)** | **26** | **Yes** — instantiated individually |
| **B2 Robotic Manipulation** | **chapter (12)** | **12** | **Yes** — instantiated individually |
| C1–C11 documentation | page | **56** | **Yes** — revision 3 said 41 |
| D1 · D2 | file | **3 · 1** | **Yes** — `sac.py` → `sac_continuous_action.py` |
| E1–E5, E4b, E9a, E9b, E10 | claim | **15** | **Yes** — E4b and E10 had no rows at all |
| | **Total** | **220** | |

**Arithmetic:** 34 + 14 + 19 + 13 + 7 + 6 + 3 + 5 + 6 + 26 + 12 + 56 + 3 + 1 + 15 = **220**. `scripts/validate/phase5_plan_consistency.py` counts the rows actually present in §6.1–§6.8 and fails if any subtotal or the total disagrees, so the count is derived from the enumeration rather than asserted ahead of it.

### 6.1 A1 — Martins & Ning — **34 rows** (9 whole chapters + 25 section rows)

**Unit rule applied:** chapters 4, 5, 7 and 11 split across dispositions, so each is represented by its **section** rows *instead of* a chapter row — never both, so nothing is double-counted. *(Revision 3 published "13 + 22"; the enumerated rows below give 34.)*

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Ch.1 Introduction | `OPT-01` | optional reference | Framing only; OPT-01 already opens the block | — |
| Ch.2 A Short History of Optimization | — | **intentionally omit** | No objective, dependent module, or research use (§9.0b all six conditions pass) | — |
| Ch.3 Numerical Models and Solvers | `NUM-03` | route → `NUM-03` | Conditioning/numerical-error framing belongs to the NUM block, not OPT | `κ(A)` — see A4 row |
| §4.1 Fundamentals | `OPT-01` | **teach here → `OPT-01` repair** | Descent-sign and normalization repairs (0007 §1) need the source's own statement | `α` step length — folds into the existing unified `α` entry |
| §4.2 Two Approaches to Optimization | `OPT-01` | optional reference | Line-search vs trust-region framing; one sentence in OPT-01 | — |
| §4.3 Line Search (§4.3.1 Sufficient Decrease/Backtracking; **§4.3.2 Strong Wolfe**; §4.3.3 Interpolation) | `OPT-01` | **teach here → `OPT-01` repair** | **Verified locator.** The Wolfe-terminology repair (0007 §1) requires Armijo vs weak vs strong Wolfe distinguished by an authority | `α` step length |
| §4.4 Search Direction (§4.4.2 CG; §4.4.3 Newton; **§4.4.4 Quasi-Newton — curvature condition**; §4.4.5 L-BFGS) | `OPT-01`, `OPT-02` | **teach here → `OPT-01`/`OPT-02` repairs** | **Verified locator.** Supplies BFGS `yᵀs > 0`, linear-vs-nonlinear CG, and Newton assumptions — three mandatory F0-b conditions | — |
| §4.5 Trust-Region Methods | `OPT-01` | **teach here → `OPT-01` repair** | The damping/trust-region limiting-behaviour repair (0007 §1) | — |
| §4.6 Summary | — | **intentionally omit** | Chapter recap; adds nothing the rows above do not | — |
| §5.1–§5.2 Constrained problem statement and setup | `OPT-03` | optional reference | OPT-03 already states the problem form | — |
| §5.3 Optimality Conditions (§5.3.1 Equality; **§5.3.2 Inequality — constraint qualification**; §5.3.3 Meaning of the Multipliers; §5.3.4 Post-Optimality Sensitivities) | `OPT-03` | **teach here → `OPT-03` repair** + the multiplier-sensitivity optional box | **The single most load-bearing row in Group A.** F0-b's KKT constraint-qualification repair cannot be accepted without a source locator (plan §4.0.3 A3) | `λ`/`ν` split — adopt Boyd's; see A2 |
| §5.4 Penalty Methods | `OPT-03` | optional reference | Context for barrier/interior-point; not separately taught | — |
| §5.5 Sequential Quadratic Programming (§5.5.1–§5.5.5, incl. **§5.5.3 Merit Functions and Filters**) | `OPT-04` | **teach here → `OPT-04` repair** | **Verified locator.** Supplies SQP with the Hessian *of the Lagrangian* plus globalization — the exact error `OPT-EXAM` Part 1 repeats | — |
| §5.6 Interior-Point Methods | `OPT-04` | **teach here → `OPT-04` repair** (with A2) | Barrier domain/limit and central-path repair; A1 gives the algorithm, A2 the conditions | `t` barrier parameter — scoped to OPT-04 |
| §5.7 Constraint Aggregation | — | optional reference | Named, not developed | — |
| Ch.6 Computing Derivatives | `OPT-04B` | route → `OPT-04B` | Finite differences are already in `MATH-02`/`NUM-01`; the AD framing belongs with the IFT | `θ` parameter — see A5 |
| §7.1 When to Use Gradient-Free Algorithms | `OPT-05B` | **teach here → `OPT-05B`** | Method selection is the module's opening objective | — |
| §7.2 Classification | `OPT-05B` | **teach here → `OPT-05B`** | Supplies the taxonomy that keeps the module out of a heuristic catalogue (0007 scope guard) | — |
| **§7.3 Nelder–Mead** | `OPT-05B` | **teach here → `OPT-05B`** | **Verified locator.** One of the two direct-search methods 0007 approves at intuition depth | — |
| **§7.4 Generalized Pattern Search** | `OPT-05B` | **teach here → `OPT-05B`** | **Verified locator.** The second approved direct-search method | — |
| §7.5 DIRECT | `OPT-05B` | **boundary only — named, not developed** | 0007 forbids the heuristic inventory; the boundary must still be visible | — |
| §7.6 Genetic Algorithms | `OPT-05B` | **boundary only — named, not developed** | As above | — |
| §7.7 Particle Swarm | `OPT-05B` | **boundary only — named, not developed** | As above. **CMA-ES is absent from this entire chapter — verified by full-text search returning 0 hits — and comes from A7** | — |
| Ch.8 Discrete Optimization | `OPT-04`, `PLAN-06` | route → `OPT-04` bridge (branch-and-bound intuition) and `PLAN-06` (MIQP) | Full treatment **intentionally omitted**: the bridge needs recognition depth only | — |
| Ch.9 Multiobjective Optimization | — | **intentionally omit** | No module, dependent, or research need | — |
| Ch.10 Surrogate-Based Optimization (incl. **§10.6.2 Efficient Global Optimization**) | `OPT-06` | route → `OPT-06` | Supplies the acquisition/surrogate repair and the min/max convention fix | — |
| §11.1 Convex problem framing | `OPT-04` | optional reference | A2 governs the definitions; A1 gives the engineering framing | — |
| §11.2 Linear Programming | `OPT-04` | **teach here → `OPT-04` bridge** | LP relaxation and lower bounds are a direct `PLAN-05`/`PLAN-06` prerequisite | — |
| §11.3 Quadratic Programming | `OPT-04` | **teach here → `OPT-04` bridge`** | QP recognition; pairs with A2's `Q` PSD-not-PD repair | — |
| §11.4 Second-Order Cone Programming | `OPT-04` | **teach here → `OPT-04` bridge** | SOCP recognition at the depth 0007 scopes | — |
| **§11.5 Disciplined Convex Optimization** | `OPT-04` | **teach here → `OPT-04` bridge** | **Verified locator.** DCP-style composition is what makes problem-class recognition mechanical | — |
| §11.6 Geometric Programming | — | optional reference | Outside the scoped recognition set | — |
| Ch.12 Optimization Under Uncertainty | — | optional reference | Adjacent to the owner's reachability work; a plan §18 candidate, not current scope | — |
| Ch.13 Multidisciplinary Design Optimization | — | **intentionally omit** | The book's own specialism, outside scope | — |

### 6.2 A2 — Boyd & Vandenberghe — **14 rows** (11 chapters + appendices A, B, C)

*(Revision 3 published 14 against a table that merged appendices A–C into one row, so only 12 rows existed. Under the one-row-per-unit rule the three appendices are three rows, and the table now contains the 14 it claimed.)*

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Ch.1 Introduction | `OPT-04` | optional reference | Framing only | — |
| Ch.2 Convex sets | `OPT-04`, `PLAN-05` | **teach here → `OPT-04`** (compact) and **`PLAN-05`** (polytopes, H/V-representation) | Polytope representation is a direct prerequisite of the owner's convex-decomposition research | — |
| Ch.3 Convex functions | `OPT-04` | **teach here → `OPT-04` repair** | Repairs the false convex/quasiconvex hierarchy (0007 §3) | — |
| Ch.4 Convex optimization problems | `OPT-04` | **teach here → `OPT-04` bridge** | LP/QP/SOCP/SDP recognition, and **convex QP requires `Q` PSD, not PD** — a mandatory F0-b condition | — |
| Ch.5 Duality | `OPT-03`, `OPT-04B` | **teach here → `OPT-03` repair** | **KKT necessity with Slater's condition**, stationarity vs Lagrangian minimization, saddle/strong duality; supplies the multiplier-sensitivity box | `λ`/`ν` inequality/equality multipliers — **new ruling**: adopt Boyd's split in `OPT-03`/`OPT-04B`; eigenvalue `λ` stays scoped to MATH |
| Ch.6 Approximation and fitting | `MATH-03B`, `NUM-03` | route → `MATH-03B`/`NUM-03` | Least-squares framing already lives there; A4 owns the numerics | — |
| Ch.7 Statistical estimation | — | **intentionally omit** | PROB and ML own estimation; §9.0b condition 2 passes — no dependent needs it here | — |
| Ch.8 Geometric problems | `PLAN-05` | optional reference → `PLAN-05` | Max-volume inscribed ellipsoid sits behind IRIS; useful context, not required | — |
| Ch.9 Unconstrained minimization | `OPT-01` | **teach here → `OPT-01` repair** | Newton's assumptions, including the strictly-convex-quadratic one-step condition; supplies the **Newton-decrement optional box** | — |
| Ch.10 Equality constrained minimization | `OPT-04B` | route → `OPT-04B` | The KKT linear system is what `OPT-04B` differentiates through | `z = (x, λ, ν)` primal–dual triple — see A5b |
| Ch.11 Interior-point methods | `OPT-04` | **teach here → `OPT-04` repair** | Barrier domain/limit/smoothness and the central path — a mandatory F0-b condition | `t` barrier parameter — **scope to `OPT-04` only**; bridge box, since `μ` is also common and `t` is time in DYN/ODE |
| Appendix A Mathematical background | — | optional reference | Reference for learners who need it; nothing is taught from it | — |
| Appendix B Problems involving two quadratic functions | — | optional reference | Outside scope | — |
| Appendix C Numerical linear algebra background | `NUM-03` | optional reference → `NUM-03` | A4 is the numerical-linear-algebra authority; this is a cross-check only | — |

### 6.3 A3 — Axler, *Linear Algebra Done Right* 4e — **19 rows** (7 whole chapters + §3A–3F + §7A–7F)

*(Revision 3 published 13 against a table that merged §3A–3E into one row and chapters 5–6 into another. Axler 4e uses lettered sections; chapters 3 and 7 split across dispositions, so each is represented by its six section rows.)*

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Ch.1 Vector spaces | `MATH-03` | **teach here → `MATH-03` repair** | The module's axiom list is incomplete (0006); the axioms must come from an authority | `V`, `W` as vector spaces — **scope to MATH only**, no cross-block use |
| Ch.2 Finite-dimensional vector spaces | `MATH-03` | optional reference | Basis/dimension already taught adequately | — |
| §3A Vector space of linear maps | `MATH-03` | optional reference | Already covered | `T` linear map — **do not import**; the workbook keeps matrix notation `A` |
| §3B Null spaces and ranges | `MATH-03`, `MATH-04` | optional reference | Rank–nullity already taught; A4 owns *numerical* rank | — |
| §3C Matrices | `MATH-03` | optional reference | Already covered | — |
| §3D Invertibility and isomorphisms | `MATH-03` | optional reference | Already covered | — |
| §3E Products and quotients | — | **intentionally omit** | No objective, dependent, or research need | — |
| **§3F Duality** | `MATH-03` | **teach here → `MATH-03` repair** | **Verified locator.** The module defines the dual space *without linearity* (0006); this section is the authority for the correct definition and the dual map | — |
| Ch.4 Polynomials | — | **intentionally omit** | Outside applied scope | — |
| Ch.5 Eigenvalues and eigenvectors | `MATH-04` | route → `MATH-04` | Already taught; A3 is the citable authority for the statements | — |
| Ch.6 Inner product spaces | `MATH-03B` | route → `MATH-03B` | Metrics and orthogonality already taught | — |
| §7A Self-adjoint and normal operators | `MATH-03B`, `MATH-04` | optional reference | Context for the spectral theorem | — |
| §7B Spectral theorem | `MATH-04` | route → `MATH-04` | Already taught; cited for the statement | — |
| **§7C Positive operators** | `MATH-03B` | **teach here → `MATH-03B` repair** | The PD/PSD repair (0006 mandatory repair 1) needs a source locator | — |
| §7D Isometries | — | optional reference | Adjacent to KIN's rotation material but not required | — |
| **§7E Singular value decomposition** | `MATH-04` | **teach here → `MATH-04` repair** | **Verified locator.** Repairs the symmetric-indefinite SVD/eigen relation (0006) | — |
| **§7F Consequences of the SVD** | `MATH-04` | **teach here → `MATH-04` addition** (Eckart–Young) | **Verified locator.** `MATH-EXAM` Part 3 already assesses best low-rank approximation *before it is taught* (§5.3); this addition makes the exam valid | — |
| Ch.8 Operators on complex vector spaces (Jordan form) | — | **intentionally omit** | Outside applied scope | — |
| Ch.9 Multilinear algebra and determinants | `MATH-03` | **intentionally omit**, with one pointer | Omitted as a topic, **but** `MATH-03`'s `M03-07` `k`-form convention note cites the alternating-tensor distinction this chapter draws | `k`-form convention — note only, no symbol imported |

### 6.4 A4 — Driscoll & Braun — **13 rows** (13 chapters)

*Omissions 9–13 are large and deliberate: FNC is a full numerical-methods course and the workbook needs its linear-algebra and conditioning half. Each omission is recorded, not silent (§9.0b).*

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Ch.1 Introduction (conditioning; stability) | `NUM-03` | **teach here → `NUM-03`** | The conditioning/stability material Toussaint §3.8 does not cover anywhere (0006) | `κ(A)` condition number — **no conflict; adopt as-is** and make it canonical in `NUM-03` |
| Ch.2 Linear systems (LU, pivoting, **Thm 2.9.3 Cholesky**) | `NUM-03`, `OPT-01`, `OPT-02` | **teach here → `NUM-03`**; route → `OPT-01`/`OPT-02` | **Verified locator.** Supplies solve-don't-invert, the destination of `MATH-02B`'s `M02B-04` finding | — |
| Ch.3 Overdetermined systems (normal equations, **Thm 3.3.3 QR**) | `NUM-03`, `MATH-03B`, `OPT-02` | **teach here → `NUM-03`**; route → `MATH-03B`, `OPT-02` | **Verified locator.** QR is the stable route for the least-squares bridge `MATH-03B` adds | — |
| Ch.4 Roots of nonlinear equations | `OPT-01`, `OPT-04B` | route → `OPT-01`, `OPT-04B` | Newton on root systems is what `OPT-04B` differentiates through | — |
| Ch.5 Piecewise interpolation | `DYN-05` | route → `DYN-05` | Already taught there (splines) | — |
| Ch.6 Initial-value problems for ODEs | `ODE-03`, `SIM-01` | route → `ODE-03`, `SIM-01` | Integrator accuracy/stability is `SIM-01`'s subject | — |
| Ch.7 Matrix analysis (SVD, dimension reduction) | `NUM-03` | **teach here → `NUM-03`** | **Numerical rank** — the concept 0006 requires and no existing module teaches | — |
| Ch.8 Krylov methods | `OPT-02` | optional reference → `OPT-02` | A plan §18 candidate; nothing currently depends on it | — |
| Ch.9 Global function approximation | — | **intentionally omit** | FNC is a full numerical-methods course; this half is out of scope | — |
| Ch.10 Boundary-value problems | — | **intentionally omit** | As above | — |
| Ch.11 Diffusion equations | — | **intentionally omit** | As above | — |
| Ch.12 Advection equations | — | **intentionally omit** | As above | — |
| Ch.13 Two-dimensional problems | — | **intentionally omit** | As above | — |

### 6.5 B1/B2 — Tedrake — **38 source units** (26 + 12)

**Corrected and instantiated at proposal revision 4.** Proposal revisions 2 and 3 both said **"33 chapters"**, which silently dropped **Underactuated's appendices A–E**. Under the unit rule the correct figure is **21 + 5 + 12 = 38**. Revision 3 identified the error and published the number **38 — but still did not write the 38 rows**, and its own heading still read "(33 chapters)". Both are fixed: the count is 38 and all 38 rows are below.

**Dispositions are adopted from plan §3.3 without change** — that section already records a decision for every chapter. What §3.3 does *not* do is carry the four matrix columns or separate the units it merges (ch.4–5, appendices A–E, Manipulation ch.1–2 and ch.9–10), which is why the rows are restated here rather than cross-referenced.

#### 6.5.1 B1 — *Underactuated Robotics* (Spring 2024) — **26 rows** (21 chapters + appendices A–E)

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| UA ch.1 Fully- vs underactuated | `UAC-01` | **ADD → `UAC-01`** | Absent from the workbook; this is the block's founding distinction | `x` state — adopt in DYN/UAC/SIM; OPT keeps `x` = decision variable, bridge box at `UAC-04` |
| UA ch.2 The simple pendulum | `ODE-01`, `ODE-02`, `DYN-01` | **REUSE as running example** | Already taught; **do not re-derive the equations of motion** | `x` state |
| UA ch.3 Acrobot, cart-pole, quadrotor | `UAC-02` | **ADD → `UAC-02`** | Absent; the canonical underactuated systems the block reasons about | `x` state |
| UA ch.4 Simple models of walking | `MANIP-05` | **OPTIONAL → `MANIP-05`** (Tier 3) | `MANIP-02` covers the compass gait conceptually and gains a cross-reference, not a rewrite | — |
| UA ch.5 Walking, running and other legged locomotion | `MANIP-05` | **OPTIONAL → `MANIP-05`** (Tier 3) | As above. *Revision 3 merged chapters 4 and 5 into one row; the unit rule requires two* | — |
| UA ch.6 Stochasticity and uncertainty | `PROB-*`, `RL-01` | **SKIP**, cross-reference | PROB and RL-01 already cover it at the needed depth | — |
| UA ch.7 Dynamic programming | `RL-01`, `RL-02`, `DYN-04`, `DRL-01` | **SKIP theory**; only the continuous-state value-iteration-on-a-grid **lab** is new → `DRL-01` | `RL-01`/`RL-02` teach DP *with* the contraction proof; only the executable part is missing | `V` value function — see the deliberate `V` unification below |
| UA ch.8 Linear quadratic regulators | `DYN-04`, `DYN-06` | **SKIP theory**; add a lab to `DYN-04` | LQR theory is taught; the implementation is not | `R` → **`R_u`**, `Q` → **`Q_x`** — three-way `R` collision with rotation matrix and reward |
| UA ch.9 Lyapunov analysis | `UAC-03` | **EXTEND → `UAC-03`** | `DYN-06` gives definitions plus energy and LQR examples; ROA, Lyapunov **synthesis**, and the V-as-value-function unification are absent | `V` Lyapunov **and** cost-to-go — **deliberate unification**, `UAC-03`'s teaching point, one bridge box |
| UA ch.10 Trajectory optimization | `UAC-04` | **EXTEND → `UAC-04`** | `DYN-04` gives the discrete-time *formulation*; transcription, constraint handling and warm starts are absent. `DYN-04` is re-scoped to "formulation", `UAC-04` to "how you actually solve it" | `J` cost functional vs Jacobian — `J` stays the Jacobian; bridge box at `UAC-04` |
| UA ch.11 Policy search | `RL-04`, `RLEARN-03` | **SKIP theory** → DRL implements | Theory already taught; DRL owns the implementation | — |
| UA ch.12 Motion planning as search | `PLAN-02` | **SKIP** | `PLAN-02` covers sampling-based planning from Toussaint | — |
| UA ch.13 Robust and stochastic control | — | **Tier-4 reference stub** | Absent, and no module or research dependency needs it (§9.0b) | — |
| UA ch.14 Feedback motion planning | `UAC-05` | **OPTIONAL → `UAC-05`** (Tier 3) | Absent; a coherent optional branch off `UAC-03` | — |
| UA ch.15 Output feedback (aka pixels-to-torques) | — | **Tier-4 reference stub** | Absent; no dependent | — |
| UA ch.16 Algorithms for limit cycles | `MANIP-05` | **OPTIONAL → `MANIP-05`** (Tier 3) | Relocated from `UAC-06` at §17.4 to fix a forward prerequisite on `MANIP-02` | — |
| UA ch.17 Planning and control through contact | `MANIP-03` | **ADD, main route → `MANIP-03`** | `MANIP-01` covers static force closure only; contact dynamics and complementarity are absent and `CAP-02` depends on them | — |
| UA ch.18 System identification | `RLEARN-01` | **SKIP**, cross-reference | Covered | — |
| UA ch.19 State estimation | existing Tier-4 SLAM branch | **stays Tier 4** | Perception is outside the owner's research scope | — |
| UA ch.20 Model-free policy search | `RL-04` | **SKIP** | Covered | — |
| UA ch.21 Imitation learning | `RLEARN-02`, `DRL-07` | **SKIP theory** → `DRL-07` implements | `RLEARN-02` teaches it (and is being repaired at F0); DRL owns the implementation | — |
| UA Appendix A | `SIM-04` | **setup material only → `SIM-04`** | Plan §3.3 dispositions the appendices as Drake/multibody/optimization support material. **The exact appendix titles are not verified** — see §7 O11; the *disposition* does not depend on the title | — |
| UA Appendix B | `SIM-04` | **setup material only → `SIM-04`** | As above | — |
| UA Appendix C | `SIM-04`, `OPT-*` | **reference → OPT block** | The optimization appendix duplicates the OPT block; carried as reference only | — |
| UA Appendix D | `SIM-04` | **reference** | As above; title unverified (§7 O11) | — |
| UA Appendix E | `SIM-04` | **reference** | As above; title unverified (§7 O11). *Revision 3 collapsed all five appendices into one row and then reported 33 units instead of 38* | — |

#### 6.5.2 B2 — *Robotic Manipulation* (Fall 2025) — **12 rows** (12 chapters)

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| RM ch.1 Introduction | `SIM-01` | **setup material → `SIM-01`** | Framing for what a simulator computes | — |
| RM ch.2 Let's get you a robot | `SIM-04` | **setup material → `SIM-04`** | Model/robot setup. *Revision 3 merged chapters 1 and 2* | — |
| RM ch.3 Basic pick and place | `KIN-03`, `SIM-05` | **REUSE `KIN-03` maths**; add the pick-and-place **task** to `SIM-05` | The kinematics are taught; the executable task is not | — |
| RM ch.4 Geometric pose estimation | — | **Tier 4** | Perception, outside the owner's research scope | — |
| RM ch.5 Bin picking | `SIM-05` | **OPTIONAL** grasp-sampling lab in `SIM-05` | A natural optional extension; nothing depends on it | — |
| RM ch.6 Motion planning | `PLAN-05`, `PLAN-06` | **overlap resolved**: this is the source for **`PLAN-05`/`PLAN-06`** | Tedrake's IRIS/GCS content is the theory source; classical PRM/RRT stays Toussaint-sourced in `PLAN-01`…`PLAN-04`. **This row is why E9a/E9b are not load-bearing** | `C`, `C_free` configuration space vs the workbook's `X`, `X_fea` — **keep `X`/`X_fea`**, bridge box in `PLAN-05` |
| RM ch.7 Mobile manipulation | — | **SKIP** | No module, dependent, or research need | — |
| RM ch.8 Manipulator control | `MANIP-04` | **EXTEND → `MANIP-04`** | `DYN-03` covers operational space; force/impedance/hybrid control is absent | — |
| RM ch.9 Object detection and segmentation | — | **Tier-4 stub** | Perception, out of scope | — |
| RM ch.10 Deep perception for manipulation | — | **Tier-4 stub** | As above. *Revision 3 merged chapters 9 and 10* | — |
| RM ch.11 Reinforcement learning | `RL-*`, `RLEARN-*`, `DRL-*` | **SKIP**, cross-reference | Three blocks already own it | — |
| RM ch.12 Soft robots and tactile sensing | — | **SKIP** | No module, dependent, or research need | — |

### 6.6 A5, A5b, A6, A7, A8 — section rows

#### 6.6.1 A5 — Blondel & Roulet — **7 rows**

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Implicit functions — optimization problems; nonlinear equations; bilevel | `OPT-04B` | **teach here → `OPT-04B`** | The framing the module opens with (pp. 285–286) | `θ` parameters |
| Envelope theorems — Bertsekas; Rockafellar; **Danskin** | `OPT-04B` | optional reference | Context, not a required objective (pp. 287–291) | — |
| **Implicit function theorem** — univariate; multivariate; JVP/VJP; proof | `OPT-04B` | **teach here → `OPT-04B` core** | **Verified locator, pp. 291–296.** The IFT's conditions must come from an authority, not from a plan (§9.7) | `θ` parameters — collides with KIN's rotation angle; bridge box in `OPT-04B` |
| Adjoint state method — differentiating nonlinear equations; relation to envelope theorems; two proofs | `OPT-04B` | **teach here → `OPT-04B`** | Root-system differentiation (pp. 297–300) | — |
| Inverse function theorem | `OPT-04B` | optional reference | Completeness for the chapter (pp. 303–305) | — |
| Chapter summary | — | **intentionally omit** | Recap | — |
| **The remaining ~470 pages** — autodiff internals, probabilistic learning, network architectures | — | **intentionally omit** (one whole-book row) | Outside `OPT-04B`'s scope entirely. Recorded as one explicit row so the omission is not silent (§9.0b) | — |

#### 6.6.2 A5b — Barratt — **6 rows** (a 4-page paper; no omissions)

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Assumption 1 (Strong duality / Slater) | `OPT-04B` | **teach here** | One of Theorem 3.1's three assumptions | — |
| Assumption 2 (Differentiability) | `OPT-04B` | **teach here** | As above | — |
| **Assumption 3 (Emptiness of `G`)** | `OPT-04B` | **teach here** | **This *is* strict complementarity** — stated at exactly that strength and no further | — |
| Theorem 2.1 (IFT, quoted from Dontchev & Rockafellar) | `OPT-04B` | route → A5's IFT rows | A5 is the teaching source for the IFT itself | — |
| Eq. (9) — the Jacobian `D_z g` | `OPT-04B` | **teach here** | The `diag(λ̃)Df` block is what the workbook's own labelled inference reasons from | `z = (x, λ, ν)` primal–dual triple — new, no conflict, adopt in `OPT-04B` |
| **Theorem 3.1** | `OPT-04B` | **teach here — as TWO independent conditions** | Requires Assumptions 1–3 **and, separately, a non-singular `D_z g`**. Neither implies the other, and `OPT-04B` must not present either as a restatement of the other | — |

#### 6.6.3 A6 — Blondel et al., implicit differentiation — **3 rows** (citation role)

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| The implicit-differentiation framework | `OPT-04B` | **route/citation → `OPT-04B`** | Anchors the "specify optimality conditions `F(x, θ) = 0` and differentiate them" formulation | — |
| Optimality-condition mappings | `OPT-04B` | **route/citation → `OPT-04B`** | The catalogue of mappings, cited not taught | — |
| Experiments and the JAXopt library treatment | — | **intentionally omit** | `OPT-04B` is CPU-first and adopts neither JAX nor JAXopt | — |

#### 6.6.4 A7 — Hansen, CMA-ES tutorial — **5 rows** (sole CMA-ES authority)

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Sampling from the search distribution | `OPT-05B` | **teach here — intuition depth** | The first of the three ideas 0007 scopes | `σ` step size — collides with the renamed SYM-02 substitution; **confine to `OPT-05B`** |
| Covariance matrix adaptation | `OPT-05B` | **teach here — intuition depth** | The method's defining idea | `C` covariance — collides with Tedrake's `C_free`; confine to `OPT-05B` |
| Step-size control | `OPT-05B` | **teach here — intuition depth** | The third scoped idea | `m` distribution mean — collides with `m` as a dimension; confine to `OPT-05B` |
| Strategy parameters and recommended settings | — | **intentionally omit** | 0007's scope guard forbids the parameter tables | — |
| The full algorithm listing and update algebra | — | **intentionally omit** | 0007 scopes `OPT-05B` to intuition; the algebra is not derived. **One bridge box retains Hansen's own notation**, since a learner reading Hansen must see Hansen's symbols (§8.3) | — |

#### 6.6.5 A8 — Larson, Menickelly & Wild — **6 rows**

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Taxonomy of derivative-free methods | `OPT-05B` | **teach here** | What keeps the module from drifting into a heuristic catalogue | — |
| Deterministic model-based methods | `OPT-05B` | optional reference | Named as a family; not developed | — |
| Direct-search methods | `OPT-05B` | **teach here** | Pairs with A1 §7.3/§7.4 | — |
| Randomized methods | `OPT-05B` | **teach here** | Where CMA-ES sits in the taxonomy; A7 supplies the method itself | — |
| Methods for constrained problems | `OPT-05B` | optional reference | Recorded, not taught | — |
| Benchmarking and evaluation budgets | `OPT-05B` | **teach here** | The module's title promises an *evaluation budget*; this is its authority | — |

### 6.7 C1–C11 — documentation page rows — **56 rows**

**Materialized at proposal revision 4.** Revision 3 listed per-source subtotals and then published **41** as the total — the figure summed only C1 through C8 and silently dropped the 6 + 6 + 3 rows of C9, C10 and C11 that the same table listed. The arithmetic is now shown and every row is written out.

> **15 + 8 + 6 + 6 + 2 + 1 + 1 + 2 + 6 + 6 + 3 = 56.**

Every documentation row carries the `api` role and the standing disposition **`reference-only`**, and under plan §9.0 **no documentation row may ever be marked as a completeness gap**. The *reason* column therefore reads the same on most rows by design — that uniformity is the rule being applied, not a filler.

**C1 MuJoCo (15)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Overview | SIM-01 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Computation | SIM-01 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Modeling | SIM-02 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| XML reference | SIM-02 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Programming | SIM-02, SIM-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Simulation | SIM-01 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Bodies, joints, degrees of freedom | SIM-02 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | **`qpos`/`qvel`/`ctrl`** → `q`/`q̇`/`u`; **mandatory bridge box on `dim(qpos) ≠ dim(qvel)` with quaternion joints** |
| Actuators | SIM-02, SIM-04 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | `ctrl` → `u` |
| Sensors | SIM-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Contacts | MANIP-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Solver | SIM-01, MANIP-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Visualization | SIM-01 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Python bindings | SIM-01…SIM-05 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Menagerie index | SIM-02, SIM-05 | reference-only | As above, **and** every model used carries its own licence (§2.6) | — |
| FAQ | SIM-01 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |

**C2 Gymnasium (8)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Env API | SIM-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| `reset` / `step` | SIM-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Spaces | SIM-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Wrappers | SIM-03, DRL-02 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| **Vector environments** | SIM-06 | reference-only | As above. **This is `SIM-06`'s required CPU half** — the part that ships whether or not MJWarp resolves | — |
| Seeding and reproducibility | NUM-01, SIM-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Termination vs truncation | SIM-03, DRL-01 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | `done` / `truncated` — API-level, no workbook conflict |
| MuJoCo environments | SIM-05, DRL-06 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |

**C3 PyTorch (6)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Tensors | NUM-02, ACC-02 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| **MPS backend** | ACC-02 | reference-only | As above. Anchors the `mps-optional` device tier | — |
| **CUDA semantics** | ACC-02, ACC-04 | reference-only | As above. Anchors the `cuda-optional` device tier | — |
| `torch.profiler` | ACC-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| autograd | ML-01, OPT-04B | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| `torch.compile` | ACC-04 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |

**C4 NumPy + SciPy (6)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Broadcasting | NUM-02 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| `numpy.linalg` | NUM-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| **`scipy.linalg`** (QR, Cholesky, `cond`) | NUM-03 | reference-only | As above. The executable counterpart of A4's Thm 2.9.3 and Thm 3.3.3 | `κ(A)` — matches A4 |
| `scipy.optimize.minimize` | OPT-05B | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| `scipy.optimize` least-squares | OPT-02, NUM-03 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| `random` / `Generator` seeding | NUM-01 | reference-only | As above. Anchors the seeding policy in plan §11.9 | — |

**C5 MJX (2)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| MJX overview | SIM-06 | reference-only | API reference; **cannot generate a completeness finding** (plan §9.0) | — |
| Documented limitations | SIM-06 | reference-only | As above — and the limitations are why `SIM-06`'s MJX half is an *optional extension* | — |

**C6 MJWarp — CONDITIONAL (1)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| MJWarp overview | SIM-06 | reference-only, **not citable while `CONDITIONAL`** | Install path unconfirmed (§7 O3). The row exists so the disposition is settled if the blocker clears | — |

**C7 MuJoCo Playground — OPTIONAL (1)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Repository README | SIM-06 | reference-only, **not proposed by default** | Apache-2.0 and role both known, so no blocker (§2.6a). Requires a Gate C scope decision | — |

**C8 Triton — CONDITIONAL (2)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Getting started | ACC-06 | reference-only, **not citable while `CONDITIONAL`** | sm_120 support unconfirmed (§7 O4). ACC-06 is Tier 3 | — |
| Kernel tutorials | ACC-06 | reference-only, **not citable while `CONDITIONAL`** | As above | — |

**C9 Drake — CONDITIONAL (6)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| Installation | PLAN-05, PLAN-06, CAP-02 | reference-only, **not citable while `CONDITIONAL`** | Install-cost blocker (§7 O2b). **Licence resolved: BSD-3-Clause** | — |
| `MathematicalProgram` | PLAN-05, PLAN-06 | reference-only, **not citable while `CONDITIONAL`** | As above; NumPy/SciPy fallback on every Drake lab | — |
| `GraphOfConvexSets` | PLAN-06 | reference-only, **not citable while `CONDITIONAL`** | As above | — |
| IRIS | PLAN-05 | reference-only, **not citable while `CONDITIONAL`** | As above | — |
| `MultibodyPlant` | CAP-02 | reference-only, **not citable while `CONDITIONAL`** | As above | — |
| Python bindings | PLAN-05, PLAN-06, CAP-02 | reference-only, **not citable while `CONDITIONAL`** | As above | — |

**C10 LeRobot — CONDITIONAL (6)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| `LeRobotDataset` | DRL-08 | reference-only, **not citable while `CONDITIONAL`** | Dataset-gating blocker (§7 O10a). DRL-08 is Tier 3 | — |
| Dataset hub | DRL-08 | reference-only, **not citable while `CONDITIONAL`** | **This is where the gating question is answered, per dataset** | — |
| Policies | DRL-08 | reference-only, **not citable while `CONDITIONAL`** | As above | — |
| Training | DRL-08 | reference-only, **not citable while `CONDITIONAL`** | As above | — |
| Evaluation | DRL-08 | reference-only, **not citable while `CONDITIONAL`** | As above | — |
| Simulation | DRL-08 | reference-only, **not citable while `CONDITIONAL`** | As above | — |

**C11 JAX — OPTIONAL (3)**

| Unit (documentation page) | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| `jit` | ACC-05 | reference-only, **not proposed by default** | Apache-2.0 and role both known, so no blocker (§2.6a). ACC-05 is Tier 3 | — |
| `vmap` | ACC-05 | reference-only, **not proposed by default** | As above | — |
| `grad` | ACC-05 | reference-only, **not proposed by default** | As above | — |

**Documentation rows: 56.**

**Which module cites which page is fixed at Gate C**, when labs are specified — that is *assignment within an already-approved set*, not approval data. The rows, their roles, and their dispositions are settled here.

### 6.8 D1/D2 and E1–E10 — implementation and paper rows — **19 rows**

**Unit rule:** one row per **file** for reference implementations, one row per **claim** for papers.

| Unit | Covering module(s) | Disposition | Reason | Notation conflicts introduced |
|---|---|---|---|---|
| **D1 CleanRL `dqn.py`** | DRL-03 | **reference implementation, read-and-compare** | Single-file and readable end to end; the mechanism `E5` describes is *taught* from here, not from the paper | `obs`/`done`/`truncated` — API-level, matches C2 |
| **D1 CleanRL `ppo.py`** | DRL-05 | **reference implementation, read-and-compare** | As above | — |
| **D1 CleanRL `sac_continuous_action.py`** | DRL-06 | **reference implementation, read-and-compare** | As above. **Corrected at proposal revision 4: revision 3 named this file `sac.py`, which does not exist in CleanRL.** The continuous-control SAC single-file implementation is `sac_continuous_action.py` | `α` entropy temperature → **`α_ent`** |
| **D2 SB3** — the SAC implementation only | DRL-06 | **comparison target** | A second, structurally different implementation to compare against D1. Role-limited to `DRL-06` | — |
| E1 PPO — the clipped surrogate objective | DRL-05 | citation | Anchors the objective `DRL-05` derives | `π_θ` policy |
| E1 PPO — generalized advantage estimation | DRL-05 | citation | Anchors GAE | — |
| E2 Diffusion Policy — action diffusion | DRL-08 (Tier 3) | citation | Anchors the mechanism | — |
| E2 Diffusion Policy — receding-horizon action chunking | DRL-08 (Tier 3) | citation | Also anchors `RLEARN-02`'s history/action-chunk notation repair (RLN02-05) | — |
| E3 DAgger — the no-regret reduction | RLEARN-02, DRL-07 | citation | Anchors the result `RLEARN-02` names | — |
| **E3 DAgger — the theorem's assumptions** | RLEARN-02 | citation → **`RLEARN-02`'s mandatory RLN02-02 repair** | `RLEARN-02:79` labels this a theorem and states **no conditions**. This row is the authority for the repair | — |
| E4 SAC — the maximum-entropy objective | DRL-06 | citation | Primary SAC citation, PMLR v80 pp. 1861–1870 | `α` entropy temperature → **`α_ent`** |
| E4 SAC — the stochastic actor | DRL-06 | citation | As above | — |
| **E4b SAC A&A — automatic temperature tuning** *(CONDITIONAL)* | DRL-06 | citation, **not citable while `CONDITIONAL`** | **Added at proposal revision 4** — revision 3 scored E4b but gave it no matrix row. Needed **only if** `DRL-06`'s scope includes automatic temperature tuning (a Gate C decision, §2.6) | — |
| E5 DQN — experience replay | DRL-03 | citation. **Citation-only, never required reading** | All rights reserved; the mechanism is taught from `dqn.py` plus newly-authored exposition | — |
| E5 DQN — the separate target network | DRL-03 | citation. **Citation-only, never required reading** | As above | — |
| **E9a IRIS — the alternation between ellipsoid and separating hyperplanes** *(CONDITIONAL)* | PLAN-05 | citation, **not citable while `CONDITIONAL`** | Locator unpinned and the paper unread (§7 O5). **B2 ch.6 covers the material**, so this blocks nothing | — |
| **E9b GCS — the convex-relaxation formulation** *(CONDITIONAL)* | PLAN-06 | citation, **not citable while `CONDITIONAL`** | As above (§7 O5). **B2 ch.6 covers the material** | — |
| **E10 Sutton & Barto — TD and Q-learning cross-reference** *(CONDITIONAL)* | DRL-01, DRL-03 | route → the existing RL block; **not citable while `CONDITIONAL`** | **Added at proposal revision 4** — revision 3 scored E10 but gave it no matrix row. Official PDF reachability unconfirmed (§7 O6) | — |
| **E10 Sutton & Barto — policy-gradient cross-reference** *(CONDITIONAL)* | DRL-02, DRL-05 | route → the existing RL block; **not citable while `CONDITIONAL`** | As above. **If never resolved, DRL stands on B1, D1 and the existing RL block, and no paywalled substitute is adopted** | — |

**E6 (behaviour-cloning origin) and E7 (AlphaZero) have no rows: both are deferred and unscored** (§3.3), so they promise nothing for the matrix to contain.

---

## 7. Open items — what each one blocks

**Corrected at proposal revision 1's review: revision 1 claimed none of these blocked approval. Several do.** Each row names the source it blocks and nothing more, and — **new at proposal revision 4** — each row that needs a fetch or an install carries the **bounded resolution ceiling** plan §9.9.1 requires, so no item can stay open indefinitely or be cleared by assertion.

| # | Item | **Blocks** | Resolution | **Ceiling (plan §9.9.1)** |
|---|---|---|---|---|
| **O1** | **A1 and A4 state no reuse licence** | **Nothing — resolved by classification.** Both are classified `consultation-and-citation-only` (plan §9.8). A Gate-B approval **records that classification and the resulting future eligibility, and nothing more**: it does not approve, perform or authorize any citation, and copying is excluded outright *(corrected at proposal revision 7, audit finding C4-02: this cell said approving them "approves citation, not copying", which granted at Gate B an action plan §9.8 and §9.9 reserve for Gate C)* | Classification recorded as a finding here; the `reuseStatus` field is written when `sources.json` is populated at **Gate D** | n/a — no fetch needed |
| **O2** | A5 is a living draft at v4 | **Nothing** — v4, its arXiv version suffix and its page ranges are pinned | Re-pin on any future version | n/a |
| **O2b** | **Drake install cost unconfirmed** | **C9 only.** C9 stays `CONDITIONAL`. *(The Drake **licence** blocker is resolved: BSD-3-Clause.)* | Gate-D evaluation-only measurement: reproducible pinned install | **Half a day** (plan §16.2's explicit drop criterion). Exceeding it drops Drake |
| **O3** | **MJWarp install path unconfirmed** | **C6 only.** C6 stays `CONDITIONAL` | Gate-D evaluation-only measurement on the 5090 | **One install attempt + one rollout check.** `SIM-06`'s required half is CPU-only, so the module ships regardless |
| **O4** | **Triton compute-capability table unconfirmed** | **C8 only.** C8 stays `CONDITIONAL` | Gate-D evaluation-only measurement | **One install + one kernel-correctness check.** `ACC-06` is Tier 3 |
| **O5** | **IRIS and GCS papers unfetched — versions, locators, titles and licences all unverified** | **E9a/E9b only.** Both stay `CONDITIONAL` | One plan §9.9.1 **Gate-D evaluation-only locator-verification fetch/read**, then a licence read *(corrected at proposal revision 8, audit finding C4-03: this cell scheduled the resolution at an event `CONDITIONAL` status makes unreachable until the resolution happens)* | **One fetch each.** B2 ch.6 covers the material meanwhile |
| **O6** | **Sutton & Barto official PDF unreachable** (self-signed certificate, 2026-08-14) | **E10 only.** E10 stays `CONDITIONAL` | One plan §9.9.1 **Gate-D evaluation-only re-attempt** against the official page *(corrected at proposal revision 8, audit finding C4-03, on the same ground as O5)* | **One re-attempt.** If it fails, DRL stands on B1, D1 and the existing RL block. **No paywalled substitute is adopted** |
| **O7** | **D3 Menagerie per-model licences** | **Individual models only**, never the collection | Read and record the licence **per model used** | **One `LICENSE` read per model.** Resolution never generalizes |
| **O8** | **A1 is a single point of failure** for Wolfe/BFGS/SQP at teaching depth | **Nothing today** — A1 is verified live and free | Recorded risk | n/a. If it vanished: A2 covers the convex-side conditions and the rest would need newly authored exposition |
| **O9** | E4b (SAC *Algorithms and Applications*) | **Nothing** — not proposed by default | A Gate-C scope decision, not evidence | n/a — resolved by a decision, not a measurement |
| **O10a** | **LeRobot dataset gating unconfirmed** | **C10 only.** C10 stays `CONDITIONAL` | Per-dataset confirmation of ungated status, or an explicit owner decision naming one gated dataset | **One reachability check per candidate dataset.** `DRL-08` is Tier 3 |
| **O10b** | `manifest.json` → `sources.json` v2 migration; the `julia-report` hole | **Nothing at Gate B** | Gate-D platform work; §5 is the draft it implements | n/a |
| **O11** | **Underactuated appendix titles unverified** *(new at proposal revision 4)* | **Nothing.** Plan §3.3 dispositions all five appendices to `SIM-04` setup material and reference; **the disposition does not depend on the title** | Read the appendix titles at acquisition and record them | **One page read.** Recorded here rather than left silent (§9.0b) |

**Resolved and no longer open:** Drake **licence** (BSD-3-Clause), Gymnasium licence (**MIT**), MuJoCo licence (**Apache-2.0** code + **CC BY 4.0** docs), **MuJoCo Playground licence (Apache-2.0) and role (`SIM-06` reference)** — *newly resolved at proposal revision 4, which is why C7 is no longer `CONDITIONAL`* — **JAX licence (Apache-2.0) and the absence of any JAX blocker**, the DQN locator (**official public DeepMind PDF**), the SAC locator (**PMLR v80 pp. 1861–1870**), and A5's IFT sections (**pinned, pp. 291–296**).

**Two things this table deliberately does not do.** It does not bundle unrelated unknowns into a general caveat — each row names one source. And it does not treat *optionality* as an open item: A9–A12, C7, C11 and E8 are fully evaluated and appear here only where a genuine unknown exists, which for C7 and C11 is nowhere (§2.6a).

---

## 8. Constraint compliance

| Constraint | Status |
|---|---|
| No paid API key, subscription, or paid account | **Satisfied.** Every selected source is free at an official URL, including E5 via the official public DeepMind PDF. **No paywalled source is required reading** |
| No account required | **Satisfied** for all of Groups A, B, D, E. Sole exception path: C10 LeRobot gated datasets — ungated is the default, a free account is acceptable per gated dataset only, recorded `requiresAccount: true` and surfaced on `/sources` |
| Core labs CPU-first | **Satisfied and strengthened.** `NUM-03`, `OPT-04B` and `OPT-05B` are **CPU-only with no GPU path**. Group A adds **zero** GPU, hardware or account requirements |
| GPU explicitly optional or advanced-justified | **Satisfied.** GPU enters only via C5–C8 and C11 — all serving Tier-3 modules or optional extensions of main-route modules |
| **RTX 5090** | **Not a learner prerequisite** — the course completes on the laptop alone. **It is a current project-validation dependency** (plan §12.4): Gate-D measurements, Gate-E's P5 spike, the third CI configuration, and committed `full`-config outputs |
| Citation granularity | **Satisfied.** Every selected source cites to chapter/section/theorem/assumption/anchor/version |
| Maintenance | Living sources pin edition/version/gitRef + access date; stable published works (A2, A5b, A7, A8, E1–E5) satisfy it by publication |
| **Reuse** | **Satisfied by explicit classification** (plan §9.8): open-licence (A3, C1–C5, **C7**, C8, C9, C10, **C11**, D1, D2), consultation/citation-only (A1, A2, A4, A5, A5b, A6, A7, A8, B1, B2, Toussaint's 13 PDFs, E1–E4, E4b), all-rights-reserved (E5), per-item (**D3** Menagerie), owner-owned (`julia-report`), **unknown-pending-licence-read (E9a, E9b, E10 — which is precisely why all three are `CONDITIONAL` and none is citable)** |
| **Status taxonomy applied** | **Satisfied.** Every scored source carries exactly one of `SELECT` / `OPTIONAL` / `CONDITIONAL` (§2.6b), and every `CONDITIONAL` carries a blocker, an activation condition, a **resolution ceiling** and an `ifUnresolved` consequence. **No source is `CONDITIONAL` merely because its artifact is optional** |
| **Coverage matrix materialized** | **Satisfied.** 220 rows, four columns each, subtotals and total machine-checked (§6) |
| **Schema draft executable** | **Satisfied.** 48 entries; full 64-hex hashes; all v1 fields retained; every conditional entry complete (§5) |

---

## 9. What Gate B does not decide

It does not authorize authoring (Gate C), installs (Gate D), visibility or deployment, **or any reproduction of source prose or figures**. It does not resolve PROB or any unreviewed block — a later approved review reopens Gate B **for the affected subset only** (plan §18). **It does not acquire, fetch, download, pin or populate anything** *(sharpened at proposal revision 5, audit finding C4-01)*: it does not execute the `sources.json` v2 migration — §5 is a draft written to no file, and Gate D implements it — and **no approval recorded here populates a `sources.json` entry, Group A included**. **It does not authorize the evaluation-only fetching of plan §9.9.1 either** — that is a Gate D permission, bounded per blocker, and it never makes a source citable on its own.

---

## 10. Approval shapes

### 10.1 What a Group-A-first partial approval would and would not authorize

Mirrors plan §9.10 and is binding. **A partial approval is narrow by construction, and its boundaries are stated here so they cannot be widened by implication.**

> **Corrected at proposal revision 5 (audit finding C4-01).** The right-hand column previously prohibited a populated `sources.json` only **"beyond the approved Group-A entries"**, which affirmatively authorized populating the Group-A rows. **The exception is deleted. A Group-A approval populates nothing.**

| It **would** authorize | It would **not** authorize |
|---|---|
| **Selection** of A1, A2, A3, A4, A5, A5b, A6, A7, A8 at their approved roles, **recorded in this document** | Any source outside Group A — Tedrake, all tool documentation, CleanRL, SB3 and every paper stay unapproved |
| Recording their **locators** — chapter, section, theorem, assumption, equation, version, access date — **as findings in this proposal** | **Acquisition, fetching, extraction or ingestion of any source, Group A included.** **No populated `sources.json` — not one entry, not even a Group-A entry.** No `raw-text/`, no `html-text/`, no `manifest.json` change. Acquisition and migration are **Gate D** (plan §9.8) |
| Recording their **roles**, **provenance**, and **reuse status** (plan §9.8) | **Any authoring, including F0 repairs** — no lesson, exercise, solution, cheat sheet, exam, figure or lab |
| Nothing further | **Gate C**, which owns the curriculum decision |
| | **Gate D** runtime, dependency, install or platform work |
| | **Reactivating `RotationViz` or `GridWorldRL`** (plan §4.7a) |
| | **Any `CONDITIONAL` source** (§2.6) — none is in Group A, and none becomes approved by association |

**Stated plainly: approving Group A settles *what the project will cite and where*. It does not start the work.** F0 authoring additionally requires the owner to approve the reconciled plan, and Gate C still owns the curriculum. A partial approval read as "F0 may begin" would skip two gates.

**Why Group A first is nonetheless the right shape:** F0 is the first authoring batch and depends only on Group A; the applied corpus is not needed until batch F3. Approving Group A removes the longest-lead blocker without committing to anything else.

### 10.2 Owner approval — **not requested at this revision**

**No approval prompt accompanies proposal revision 8.** Four consecutive revisions were reported complete and then failed review; the fifth was superseded before review when a pre-review inspection found three further defects (§0.7); the sixth failed an independent **structural** audit (§0.8); the seventh failed the next one (§0.9). **The review-lane blocker C2-01 is now RESOLVED** — `docs/review/modules/KIN-02.md`'s Phase-5 reconciliation was re-pinned and its F0/F8 split corrected, under the owner's narrow authorization for that section alone; that record now pins the superseded plan revision 3.6 and is the review lane's to re-pin, which is a pin-staleness item and not a reopening of C2-01. **One thing therefore remains before any approval request: an independent structural review of plan revision 3.7 / proposal revision 8 must pass. That review is now the required next action and may be requested. It has not happened, so no approval may be requested yet.**

When a review eventually does pass, the prompt's decision groups map to §2 (scores and eligibility), §2.6/§2.6a/§2.6b (the three statuses, every blocker, and the sources that have none), §5 (schema draft, v1→v2 mapping, and §5.3's list of what is not pinned), §6 (the 220-row coverage matrix), §7 (what each open item blocks and its ceiling), §8 (constraints), and §10.1 (partial-approval scope). **Every one of those is a planning record. None of them acquires a source.**

**Recommended shape, unchanged and still only a recommendation:** Group-A-first partial approval, bounded by plan §9.10 and §10.1 above. It is recommended *in principle*; it is not on the table until the review passes.
