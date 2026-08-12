// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// remark-math + rehype-katex do two jobs at once here:
// 1. Render $...$ / $$...$$ math to KaTeX HTML at build time for MDX prose.
// 2. Just as important: remark-math intercepts math BEFORE the MDX/JSX parser sees it,
//    which is required — raw LaTeX like \dfrac{a}{b} contains literal { } that the MDX
//    JSX parser otherwise tries to interpret as embedded JS expressions and fails on.
// Set via markdown.processor (not mdx({remarkPlugins,...}), which is deprecated in this
// Astro version) — @astrojs/mdx inherits this configured processor automatically.
// Exercise prompts/hints/solutions live in JSON content collections (not MDX), so they
// don't go through this pipeline at all — those are rendered with client-side KaTeX
// auto-render instead (see BaseLayout.astro), since there's no MDX/JSX parsing step to
// protect them from in the first place.
export default defineConfig({
  markdown: {
    processor: unified({
      remarkPlugins: [remarkMath],
      rehypePlugins: [rehypeKatex],
    }),
  },
  integrations: [mdx()],
});
