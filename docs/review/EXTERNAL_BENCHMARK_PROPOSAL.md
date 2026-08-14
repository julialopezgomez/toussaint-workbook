# External benchmark corpus proposal

Status: **approved by the owner on 2026-08-14 for the review process**
Purpose: detect important gaps that are absent from both the workbook and its declared notes, without turning review into an unlimited literature survey.

Approval authorizes these sources as a controlled completeness lens, not as an instruction to add every topic they contain. Existing Toussaint sources remain the primary fidelity target; this corpus is a second lens for breadth, conventions, and modern practice. Living sources must be cited with an access date/version.

## Selection rules

The corpus should remain small, public or freely readable where possible, pedagogically strong, and stable enough to cite by chapter/section. Prefer author/course/publisher pages, original papers for theorem claims, runnable examples that do not require payment, and sources whose notation can be mapped cleanly to the workbook. A benchmark may expose a gap; it does not automatically dictate a new module.

## Proposed core corpus

| Blocks | Full citation / link | Why authoritative | What it benchmarks | Layer | Free? | Scope limitation |
|---|---|---|---|---|---|---|
| MATH | Deisenroth, Faisal & Ong, [*Mathematics for Machine Learning*](https://mml-book.github.io/); Petersen & Pedersen, [*The Matrix Cookbook*](https://www2.imm.dtu.dk/pubdb/pubs/3274-full.html), 2012 | Author-hosted university text and DTU technical reference | Broad math objectives; matrix identities/derivatives and shape conventions | Foundations/reference | Yes | The Cookbook is a formula reference, not a pedagogy model. |
| OPT | Boyd & Vandenberghe, [*Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/), Cambridge UP, 2004 | Canonical author-hosted graduate text | Convexity, duality, KKT, canonical problem classes, numerical framing | Foundations | Yes | Does not benchmark black-box/Bayesian optimization broadly. |
| PROB | Pishro-Nik, [*Introduction to Probability, Statistics, and Random Processes*](https://www.probabilitycourse.com/) | University-authored open textbook with exercises | Probability foundations, random variables, conditioning, expectation, limit concepts | Foundations | Yes | VI and information geometry need specialist sources. |
| ODE | MIT OpenCourseWare, [18.03SC Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/) | Official MIT course with notes, problems, and solutions | ODE objectives, qualitative behavior, linear systems, numerical context | Foundations | Yes | Broader than the robotics-oriented minimum. |
| KIN, DYN, PLAN | Lynch & Park, [*Modern Robotics: Mechanics, Planning, and Control*](https://hades.mech.northwestern.edu/index.php/Modern_Robotics), Cambridge UP, 2017 | Canonical robotics text, official free preprint and software | Rigid motions, kinematics, dynamics, planning, control, conventions | Foundations/practice | Yes | Not quaternion-centered. |
| KIN | Joan Solà, [“Quaternion Kinematics for the Error-State Kalman Filter”](https://arxiv.org/abs/1711.02508), 2017 | Widely used specialist technical reference with explicit conventions and derivations | Double cover, conventions, derivatives, integration, geometric intuition | Foundations/advanced | Yes | Estimation treatment is beyond Tier 1 scope. |
| DYN, ODE, OPT, PLAN, RL | Russ Tedrake, [*Underactuated Robotics*](https://underactuated.csail.mit.edu/), living MIT notes | Official advanced MIT course notes with computational examples | Nonlinear dynamics/control, stability, trajectory optimization, model systems, labs | Modern practice/research | Yes | Living source: record access date/version; breadth overlaps many blocks. |
| MANIP, PLAN, RLEARN | Russ Tedrake, [*Robotic Manipulation*](https://manipulation.csail.mit.edu/), living MIT notes | Official MIT manipulation course and runnable examples | Contact-rich manipulation, perception, planning, optimization, learning | Modern practice/research | Yes | Living and deliberately selective. |
| PLAN | Steven M. LaValle, [*Planning Algorithms*](https://lavalle.pl/planning/), Cambridge UP, 2006 | Canonical author-hosted planning textbook | Configuration spaces, sampling planning, nonholonomic planning, completeness | Foundations | Yes | Far broader than workbook scope; use mapped chapters only. |
| ML | Zhang et al., [*Dive into Deep Learning*](https://en.d2l.ai/) | Maintained open interactive book with executable implementations | Modern NN objectives, training workflow, CPU/GPU practice | Foundations/modern practice | Yes | Framework APIs change; benchmark concepts, not transient syntax. |
| RL, RLEARN | Sutton & Barto, [*Reinforcement Learning: An Introduction*, 2nd ed.](http://incompleteideas.net/book/the-book-2nd.html), 2018; UC Berkeley, [CS 285 Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/) | Canonical author resource plus leading official graduate course | RL foundations; current deep-RL algorithms and implementation expectations | Foundations/modern practice | Yes | Record CS 285 offering/date; course content evolves. |
| SYM | Ghallab, Nau & Traverso, [*Automated Planning: Theory and Practice* resource page](https://www.cs.umd.edu/~nau/planning.html), 2004 | Author-hosted materials for a canonical planning text | Representations, search, heuristics, and planning systems | Foundations | Partial | Do not require access to a paid text; use public slides/resources only. |
| CAP | MIT Robotic Manipulation, [“Motion Planning”](https://manipulation.mit.edu/trajectories.html); Drake, [Graph of Convex Sets API](https://drake.mit.edu/doxygen_cxx/classdrake_1_1geometry_1_1_optimization_1_1_graph_of_convex_sets.html) | Primary course exposition plus official software documentation | GCS concepts, formulation boundaries, implementation terminology | Modern practice/research | Yes | API details are version-sensitive. |
| REV1, REV2 | No separate source | Cumulative reviews should inherit approved constituent-block evidence | Retention, integration, and transfer | Synthesis | N/A | Adding a source would distort their assessment role. |

## Module-specific primary checks for calibration

These are narrower than the core corpus and should be approved with it:

| Module | Candidate | Exact question it answers |
|---|---|---|
| `MATH-02B` | The Matrix Cookbook | Are determinant, inverse, Woodbury, trace, and matrix-derivative identities sufficiently complete and conventionally stated? |
| `KIN-02` | Solà quaternion reference | Does the lesson teach the double cover, sign choice, composition conventions, interpolation edge cases, and quaternion integration needed for competent use? |
| `RLEARN-02` | [Ross, Gordon & Bagnell, A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://proceedings.mlr.press/v15/ross11a.html) | Are the behavior-cloning and DAgger bounds stated with the right assumptions and conclusions? |
| `RLEARN-02` | Current CS 285 imitation-learning material | Are objectives and exercises representative of a modern introductory imitation-learning treatment? |

## Controlled use of recent surveys

A recent survey can serve as a **recency sentinel**, not as a source of truth or a requirement to include every named method. Proposed sentinel: [Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes](https://arxiv.org/abs/2404.18201). It may nominate topics for checking against primary sources; it cannot by itself create an `UNPLANNED_GAP`.

## Explicit exclusions from the benchmark

- paid accounts, paid APIs, or paywalled material required for core learning;
- anonymous tutorials and SEO summaries;
- framework documentation as the sole source for conceptual claims;
- leaderboards or “state of the art” lists without stable pedagogical value;
- importing every topic found in a broad graduate textbook;
- treating one source's notation as a reason to rewrite the workbook globally.

## Approval questions

Before external review begins, the owner should answer:

- [x] Approve this corpus as-is.
- [x] Approve living-course sources provided every finding records an access date/version.
- [x] Approve the three module-specific checks above.
- [x] Approve one recent survey only as a recency sentinel.
- [x] No source removed, replaced, or demoted at approval time.
- [x] External gaps must be important to the workbook's stated robotics/ML goals, not merely interesting.

External findings may now be finalized when directly supported by this corpus and the relevance-scoped completeness rule. Verified omissions from a module's own declared source never depended on benchmark approval.
