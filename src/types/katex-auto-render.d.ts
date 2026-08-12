declare module 'katex/contrib/auto-render' {
  import type { KatexOptions } from 'katex';
  interface AutoRenderOptions extends KatexOptions {
    delimiters?: { left: string; right: string; display: boolean }[];
  }
  export default function renderMathInElement(elem: HTMLElement, options?: AutoRenderOptions): void;
}
