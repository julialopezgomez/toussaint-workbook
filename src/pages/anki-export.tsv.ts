import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const prerender = true;

// Anki's native LaTeX tags differ from KaTeX's $...$/$$...$$ delimiters.
function toAnkiLatex(text: string): string {
  return text
    .replace(/\$\$(.+?)\$\$/gs, (_m, inner) => `[$$]${inner}[/$$]`)
    .replace(/\$(.+?)\$/gs, (_m, inner) => `[$]${inner}[/$]`);
}

// TSV fields can't contain literal tabs/newlines.
function cleanField(text: string): string {
  return text.replace(/\t/g, ' ').replace(/\r?\n/g, ' ').trim();
}

export const GET: APIRoute = async () => {
  const modules = await getCollection('course');
  const questions = await getCollection('questions');
  const solutions = await getCollection('solutions');
  const solutionByExerciseId = new Map(solutions.map((s) => [s.data.exerciseId, s.data]));

  const rows: string[] = ['Front\tBack\tTags'];

  // Notation cards: every module's symbol -> meaning pair, universal coverage.
  for (const m of modules) {
    for (const n of m.data.notation) {
      const front = cleanField(toAnkiLatex(n.symbol));
      const back = `${cleanField(toAnkiLatex(n.meaning))} (${m.data.id})`;
      rows.push(`${front}\t${back}\tnotation::${m.data.block}`);
    }
  }

  // Exercise recall cards: only exercises explicitly flagged with reviewCardIds
  // (a curated subset, not every exercise -- most exercises' full derivations
  // don't compress well into a flashcard back).
  for (const q of questions) {
    if (!q.data.reviewCardIds || q.data.reviewCardIds.length === 0) continue;
    const sol = solutionByExerciseId.get(q.data.id);
    if (!sol) continue;
    const front = cleanField(toAnkiLatex(q.data.prompt));
    const back = cleanField(toAnkiLatex(sol.fullSolution));
    rows.push(`${front}\t${back}\texercise::${q.data.moduleId}`);
  }

  const tsv = rows.join('\n') + '\n';
  return new Response(tsv, {
    headers: {
      'Content-Type': 'text/tab-separated-values; charset=utf-8',
      'Content-Disposition': 'attachment; filename="toussaint-workbook-anki-export.tsv"',
    },
  });
};
