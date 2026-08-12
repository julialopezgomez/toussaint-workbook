import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import type { Loader } from 'astro/loaders';
import fs from 'node:fs/promises';
import path from 'node:path';

const sourceRef = z.object({
  sourceId: z.string(),
  pages: z.string(),
  role: z.enum(['primary', 'supplementary', 'cross-reference']),
});

const course = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/course' }),
  schema: z.object({
    id: z.string(),
    block: z.string(),
    title: z.string(),
    tier: z.union([z.literal(1), z.literal(2), z.literal(3), z.literal(4)]),
    estimatedHours: z.number(),
    prerequisites: z.array(z.string()).default([]),
    objectives: z.array(z.string()),
    sources: z.array(sourceRef),
    externalSources: z.array(z.object({ citation: z.string(), note: z.string() })).optional(),
    concepts: z.array(z.string()),
    notation: z.array(z.object({ symbol: z.string(), meaning: z.string() })).default([]),
    cheatsheetLinks: z.array(z.string()).default([]),
    obsidianLinks: z
      .array(z.object({ path: z.string(), confidence: z.literal('high'), note: z.string() }))
      .optional(),
    nextModules: z.array(z.string()).default([]),
  }),
});

/**
 * Each file in src/content/questions/ and src/content/solutions/ holds ONE JSON array
 * (one file per module), not one entry per file — so the built-in `file()` loader
 * (which expects one collection entry per file) doesn't fit. This custom loader reads
 * every *.json file in `dir`, applies `extract` to pull the array of raw entries out of
 * each file's parsed JSON, and stores each array element as its own collection entry.
 */
function multiEntryJsonLoader(name: string, dir: string, extract: (fileData: unknown) => Record<string, unknown>[]): Loader {
  return {
    name,
    load: async ({ store, parseData, logger }) => {
      store.clear();
      const dirNames = await fs.readdir(dir);
      const files = dirNames.filter((f) => f.endsWith('.json')).map((f) => path.join(dir, f));
      for (const filePath of files) {
        const raw = await fs.readFile(filePath, 'utf-8');
        const fileData = JSON.parse(raw);
        const entries = extract(fileData);
        for (const entry of entries) {
          const id = String(entry.id);
          const data = await parseData({ id, data: entry });
          store.set({ id, data, filePath: path.relative(process.cwd(), filePath) });
        }
      }
      logger.info(`${name}: loaded entries from ${files.length} file(s) in ${dir}`);
    },
  };
}

const questions = defineCollection({
  loader: multiEntryJsonLoader('questions-loader', './src/content/questions', (fileData) => {
    const data = fileData as { moduleId: string; exercises: Record<string, unknown>[] };
    return data.exercises.map((e) => ({ ...e, moduleId: data.moduleId }));
  }),
  schema: z.object({
    id: z.string(),
    moduleId: z.string(),
    objective: z.string(),
    provenance: z.enum(['source-adapted', 'newly-authored', 'external-adapted']),
    sourceRef: z.object({ sourceId: z.string(), page: z.number(), originalNumber: z.string() }).optional(),
    difficulty: z.enum(['foundation', 'core', 'challenge']),
    estimatedMinutes: z.number(),
    prerequisites: z.array(z.string()).default([]),
    answerType: z.enum([
      'mcq',
      'multi-select',
      'short-text',
      'numeric',
      'symbolic',
      'derivation',
      'proof',
      'code',
      'diagram',
    ]),
    prompt: z.string(),
    options: z.array(z.string()).optional(),
    hints: z.tuple([z.string(), z.string(), z.string()]),
    reviewCardIds: z.array(z.string()).optional(),
  }),
});

const solutions = defineCollection({
  loader: multiEntryJsonLoader('solutions-loader', './src/content/solutions', (fileData) => {
    const data = fileData as { solutions: Record<string, unknown>[] };
    return data.solutions.map((s) => ({ ...s, id: s.exerciseId }));
  }),
  schema: z.object({
    id: z.string(),
    exerciseId: z.string(),
    checkMode: z.enum(['deterministic', 'symbolic', 'rubric']),
    deterministic: z
      .object({ expected: z.union([z.string(), z.number()]), tolerance: z.number().optional(), unit: z.string().optional() })
      .optional(),
    symbolic: z.object({ expectedExpr: z.string(), variables: z.array(z.string()).default([]), equivalenceNotes: z.string().optional() }).optional(),
    rubric: z
      .object({
        criteria: z.array(z.object({ points: z.number(), description: z.string() })),
        commonErrors: z.array(z.string()),
      })
      .optional(),
    fullSolution: z.string(),
  }),
});

const cheatsheets = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/cheatsheets' }),
  schema: z.object({
    id: z.string(),
    title: z.string(),
    relatedModules: z.array(z.string()).default([]),
  }),
});

export const collections = { course, questions, solutions, cheatsheets };
