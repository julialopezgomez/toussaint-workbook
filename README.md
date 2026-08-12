# Toussaint Workbook

A personal, self-paced study workbook built from Marc Toussaint's TU Berlin course notes: sequenced, prioritized, and interleaved with exercises for one specific PhD research direction (long-horizon robotics planning). See `PROJECT_STATE.md` for project status and `CLAUDE.md` for the full technical picture.

The site itself runs entirely locally (see setup below): this repository is public so the code and notes are backed up and shareable, but there's no hosted/deployed version.

## Credit and source material

The mathematical content, notation, structure, and several exercises in this workbook are derived from the publicly available lecture notes of:

> **Marc Toussaint**, Professor, Learning & Intelligent Systems Lab, TU Berlin
> Teaching materials: <https://www.user.tu-berlin.de/mtoussai/teaching/>

This is an **independent, unofficial personal study project**, not an official course resource, and it is not affiliated with or endorsed by Prof. Toussaint or TU Berlin. Every piece of content in this workbook is tagged with its provenance, visible right on the page:

- **Source-adapted**: exercises or explanations directly adapted from Toussaint's lecture notes, with his original section/exercise numbering preserved wherever possible (e.g. "adapted from `lecture-maths`, Exercise 5 / §2.8.1"). These are the closest to his original material, paraphrased/restructured rather than quoted at length.
- **Newly authored**: exercises, worked examples, and explanations written for this workbook, not present in the source material.
- **External-sourced**: content drawn from other cited references (e.g. Sutton & Barto, Lynch & Park), cited separately.

The original source PDFs themselves are **not included in this repository** (see `.gitignore`), nor is any full extracted transcription of them, precisely because they're Prof. Toussaint's copyrighted teaching material. Only paraphrased/adapted derivative content with clear attribution is published here.

If you're a student encountering this: go read Prof. Toussaint's actual lecture notes at the link above first, this workbook is a personal supplement, not a substitute.

## First-time setup (only needed once per machine)

1. Install [Node.js](https://nodejs.org) (v22+) and Python 3 if you don't already have them.
2. Open a terminal in this `workbook/` folder and run:
   ```bash
   npm install
   ```
3. Set up the Python environment (used for PDF extraction and the symbolic-grading server):
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install --upgrade pip pymupdf beautifulsoup4 lxml numpy sympy flask torch
   ```

That's it: steps 2 and 3 only need to be run again if you delete `node_modules/` or `.venv/`.

## Every time you want to study

Open a terminal in this `workbook/` folder and run:

```bash
npm run dev
```

Then open **http://localhost:4321** in your normal browser (Safari, Chrome, etc.), not by double-clicking any file in Finder.

If a module has a "Check (SymPy)" button (symbolic-answer exercises), also open a **second terminal** in this folder and run:

```bash
npm run grading-server
```

That's optional: everything else on the site works without it, you'll just see a message asking you to start it if you hit a symbolic exercise without it running.

To stop: go back to each terminal and press `Ctrl+C`.

## Your progress

Your answers and check results are saved automatically in your browser's local storage (IndexedDB) as you use the site, not on disk and not sent anywhere (this site has no server or database). Use the "Export my progress" / "Import progress" buttons on the homepage to back up your progress or move it to another browser or machine.

## Troubleshooting

- **Math looks like raw text (`$\sigma(z)$` instead of a rendered formula) / buttons don't do anything**: you're not viewing it through the dev server. Make sure `npm run dev` is running and you opened `http://localhost:4321`, not a local file.
- **"Could not reach the local grading server"**: start it with `npm run grading-server` in a second terminal.
- **Port already in use**: another copy of the server is probably already running; check your terminals, or just reopen `http://localhost:4321`, it may already be up.
