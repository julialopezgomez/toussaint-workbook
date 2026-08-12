# Toussaint Workbook

Private, local-only study site built from Marc Toussaint's TU Berlin course notes. See `PROJECT_STATE.md` for project status and `CLAUDE.md` for the full technical picture.

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

That's it — steps 2 and 3 only need to be run again if you delete `node_modules/` or `.venv/`.

## Every time you want to study

Open a terminal in this `workbook/` folder and run:

```bash
npm run dev
```

Then open **http://localhost:4321** in your normal browser (Safari, Chrome, etc.) — not by double-clicking any file in Finder.

If a module has a "Check (SymPy)" button (symbolic-answer exercises), also open a **second terminal** in this folder and run:

```bash
npm run grading-server
```

That's optional — everything else on the site works without it; you'll just see a message asking you to start it if you hit a symbolic exercise without it running.

To stop: go back to each terminal and press `Ctrl+C`.

## Your progress

Your answers and progress are saved automatically in your browser (not on disk, not sent anywhere) as you use the site. Use the export/import feature on the site to back up or move your progress between browsers/machines once that feature is built out.

## Troubleshooting

- **Math looks like raw text (`$\sigma(z)$` instead of a rendered formula) / buttons don't do anything** → you're not viewing it through the dev server. Make sure `npm run dev` is running and you opened `http://localhost:4321`, not a local file.
- **"Could not reach the local grading server"** → start it with `npm run grading-server` in a second terminal.
- **Port already in use** → another copy of the server is probably already running; check your terminals, or just reopen `http://localhost:4321` — it may already be up.
