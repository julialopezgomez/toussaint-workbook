# Toussaint Workbook

A personal, self-paced study workbook built from Marc Toussaint's TU Berlin course notes: sequenced, prioritized, and interleaved with exercises for one specific PhD research direction (long-horizon robotics planning). See `PROJECT_STATE.md` for project status and `CLAUDE.md` for the full technical picture.

> **Marc Toussaint**, Professor, Learning & Intelligent Systems Lab, TU Berlin
> Teaching materials: <https://www.user.tu-berlin.de/mtoussai/teaching/>

The site itself runs entirely locally (see setup below): this repository is public so the code and notes are backed up and shareable, but there's no hosted/deployed version.

## Setup Instructions

### First-time setup (only needed once per machine)

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

### Every time you want to study

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

## Editing content

Everything on the site is plain text files under `src/content/`; there's no CMS or admin panel, you edit files directly and the dev server (`npm run dev`) hot-reloads. Nothing here needs the source PDFs: `original notes/` is read-only and never touched by editing workflows.

Each module `{ID}` (e.g. `RL-04`) is three files:
- `src/content/course/{BLOCK}/{ID}.mdx` — the lesson prose (frontmatter + Markdown/JSX body)
- `src/content/questions/{ID}.json` — that module's exercises (prompts, hints, metadata)
- `src/content/solutions/{ID}.json` — matching rubrics/solutions, one entry per exercise

**Fix a typo or edit explanatory text**: open the `.mdx` file and edit the Markdown directly. Save, the dev server picks it up immediately.

**Edit or add math**: inline math is `$...$`, display math is `$$...$$`, both on a single line for anything short. For a multi-line block (e.g. `\begin{aligned}...\end{aligned}` spanning several lines), the closing `$` **must be alone on its own line** — this is a real gotcha (`remark-math` silently fails to parse it otherwise, and it renders as raw red LaTeX text instead of a build error, so it can hide indefinitely if you don't happen to view that page). Always check `document.querySelectorAll('.katex-error')` is empty on any page you touch, or run the sweep command below.

**Add a figure/image**: put the image file under `public/figures/{source-id}/{descriptive-name}.png`, then in the `.mdx`:
```mdx
import SourceFigure from '../../../components/SourceFigure.astro';

<SourceFigure
  src="/figures/lecture-robotics/fig3-example.png"
  alt="Short accessible description"
  caption="What the figure shows."
  source="lecture-robotics"
  page="42"
/>
```
For a figure that's your own diagram (not reproduced from a source PDF), just use a plain Markdown image `![alt](/figures/.../my-diagram.png)` instead, no `source`/`page` attribution needed.

**Add a link to an external site**: plain Markdown, `[link text](https://example.com)`, works anywhere in the `.mdx` prose.

**Add or edit an exercise**: add an entry to that module's `questions/{ID}.json` (`hints` must be exactly 3 strings, `id` must be `{ID}-ex{N}-{subpart}` and unique site-wide) and a matching entry (same `exerciseId`) to `solutions/{ID}.json`. Then, in the `.mdx`, add `<ExerciseCard id="{that-exercise-id}" />` at the point in the prose where it should appear. **This last step is easy to forget and nothing catches it automatically**: an exercise can exist fully-authored in both JSON files and simply never render on the page if the `<ExerciseCard>` tag is missing or misspelled. Always run the cross-reference check below after adding an exercise.

**Add a whole new module**: create the three files above with a new `{ID}` following the existing `{BLOCK}-{NN}` pattern (or `{BLOCK}-00` for a foundational module ahead of `-01`, see `MATH-00`/`RLEARN-00` for precedent). Required frontmatter fields are in `src/content.config.ts`; copy an existing module's frontmatter as a template rather than writing it from scratch. If it's genuinely a new block (not just a new module in an existing one), add it to `BLOCKS` in `src/lib/curriculum/blocks.ts` (id, title, one-line rationale) so it appears in the right place on the homepage, `/curriculum`, and the breadcrumbs — everything else (module lists, concept/notation/source indexes, prev/next navigation) is generated automatically from the content collection, no other file needs updating.

**Validate before trusting a change**, especially after adding an exercise or a multi-line math block:
```bash
npx astro check && npm run build
```
Then check nothing silently broke (both are quick, zero-dependency scripts):
```bash
# 0 matches expected: catches multi-line-math rendering failures
grep -rl katex-error dist/course dist/index.html

# every JSON exercise should have a matching <ExerciseCard>, and vice versa
python3 -c "
import json, re, glob
mdx = glob.glob('src/content/course/**/*.mdx', recursive=True)
cards = set()
for f in mdx: cards |= set(re.findall(r'<ExerciseCard\s+id=\"([^\"]+)\"', open(f).read()))
qids = set()
for f in glob.glob('src/content/questions/*.json'):
    qids |= set(e['id'] for e in json.load(open(f))['exercises'])
print('missing cards:', qids - cards or 'none')
print('orphan cards:', cards - qids or 'none')
"
```

## Credit and source material

The mathematical content, notation, structure, and several exercises in this workbook are derived from the publicly available lecture notes of:

> **Marc Toussaint**, Professor, Learning & Intelligent Systems Lab, TU Berlin
> Teaching materials: <https://www.user.tu-berlin.de/mtoussai/teaching/>

This is an **independent, unofficial personal study project**, not an official course resource, and it is not affiliated with or endorsed by Prof. Toussaint or TU Berlin. Every piece of content in this workbook is tagged with its provenance, visible right on the page:

- **Source-adapted**: exercises or explanations directly adapted from Toussaint's lecture notes, with his original section/exercise numbering preserved wherever possible (e.g. "adapted from `lecture-maths`, Exercise 5 / §2.8.1"). These are the closest to his original material, paraphrased/restructured rather than quoted at length.
- **Newly authored**: exercises, worked examples, and explanations written for this workbook, not present in the source material.
- **External-sourced**: content drawn from other cited references (e.g. Sutton & Barto, Lynch & Park), cited separately. The one capstone module (`CAP-01`) also cites the workbook owner's own PhD Year-1 report as an external source, since the capstone is explicitly a synthesis/application exercise connecting the taught material to the owner's own research, not new taught content from Toussaint's lectures.

The original source PDFs themselves are **not included in this repository** (see `.gitignore`), nor is any full extracted transcription of them, precisely because they're Prof. Toussaint's copyrighted teaching material. Only paraphrased/adapted derivative content with clear attribution is published here.

If you're a student encountering this: go read Prof. Toussaint's actual lecture notes at the link above first, this workbook is a personal supplement, not a substitute.


## Troubleshooting

- **Math looks like raw text (`$\sigma(z)$` instead of a rendered formula) / buttons don't do anything**: you're not viewing it through the dev server. Make sure `npm run dev` is running and you opened `http://localhost:4321`, not a local file.
- **"Could not reach the local grading server"**: start it with `npm run grading-server` in a second terminal.
- **Port already in use**: another copy of the server is probably already running; check your terminals, or just reopen `http://localhost:4321`, it may already be up.
