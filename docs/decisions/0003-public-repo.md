# Decision Record 0003 — Public Repository

Date: 2026-08-12

## Decision
User explicitly requested the repository be made public on GitHub, with clear credit to Marc Toussaint and a link to his teaching page in the README. This reverses the original Phase 0 default ("private, local-first," "do not deploy or publish source-derived content unless explicitly approved and rights implications reviewed") specifically for the repository's visibility, not for the site's deployment status (the site remains local-only, no hosted version).

## Rights consideration flagged before proceeding
Two of the six exercises in the ML-03 pilot module are closely adapted from Toussaint's actual exercise text (`lecture-maths` Exercise 4/§2.7.3 and Exercise 5/§2.8.1), with his original numbering preserved, not just "inspired by" his material. This was flagged to the user before pushing. Assessment: sharing this publicly with clear, prominent attribution (which the user explicitly asked for) is normal practice for academic study-note repositories and matches how the workbook's provenance system was already designed (every module/exercise tags source-adapted vs. newly-authored vs. external-sourced). User proceeded with full awareness of this distinction.

## What's actually public vs. excluded
- **Public**: all authored curriculum/architecture docs, the Astro site source code, the ML-03 module content (MDX prose, exercises, solutions/rubrics), scripts, decision records.
- **Never committed, per `.gitignore`**: the source PDFs themselves (`../original notes/`, structurally outside the repo since git was initialized at `workbook/`), and full extracted plain-text transcriptions of them (`data/source-manifest/raw-text/`, `html-text/`).

## README changes
Added a "Credit and source material" section: names Marc Toussaint, TU Berlin, Learning & Intelligent Systems Lab, links `https://www.user.tu-berlin.de/mtoussai/teaching/`, states this is an independent/unofficial/unaffiliated personal project, explains the source-adapted/newly-authored/external-sourced provenance tagging system, and points readers to the original lecture notes rather than treating this workbook as a substitute.

## Status
Repository pushed public to GitHub under the user's account (`julialopezgomez`). No license file was added (not requested, and choosing an OSS license for the code is a separate decision from the content-attribution question addressed here; left for the user to decide later if they want one).
