// Inline Lucide icons into composition HTML.
// Usage: node tools/build.mjs <srcDir> <outDir>
// In sources, write <i data-i="icon-name" class="optional classes"></i>; it becomes the Lucide SVG.
import { readFileSync, writeFileSync, readdirSync, mkdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const iconsDir = join(here, "..", "node_modules", "lucide-static", "icons");
const [srcDir, outDir] = process.argv.slice(2);
if (!srcDir || !outDir) throw new Error("usage: build.mjs <srcDir> <outDir>");

const cache = new Map();
function icon(name, cls) {
  if (!cache.has(name)) {
    const raw = readFileSync(join(iconsDir, `${name}.svg`), "utf8");
    const inner = raw.replace(/<!--[\s\S]*?-->/g, "").replace(/^[\s\S]*?<svg[^>]*>/, "").replace(/<\/svg>\s*$/, "");
    cache.set(name, inner.replace(/\s+/g, " ").trim());
  }
  const c = ["lucide", `lucide-${name}`, cls].filter(Boolean).join(" ");
  return `<svg class="${c}" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${cache.get(name)}</svg>`;
}

mkdirSync(outDir, { recursive: true });
let total = 0;
for (const f of readdirSync(srcDir).filter((n) => n.endsWith(".html"))) {
  let html = readFileSync(join(srcDir, f), "utf8");
  let n = 0;
  html = html.replace(/<i data-i="([a-z0-9-]+)"(?: class="([^"]*)")?><\/i>/g, (_, name, cls) => {
    n++;
    return icon(name, cls);
  });
  if (/data-i="/.test(html)) throw new Error(`${f}: unmatched icon placeholder left`);
  writeFileSync(join(outDir, f), html);
  total += n;
  console.log(`${f}: ${n} icons`);
}
console.log(`done, ${total} icons`);
