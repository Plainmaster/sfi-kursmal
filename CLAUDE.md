<!-- GSD:project-start source:PROJECT.md -->
## Project

**SFI Spår 2 -- Kursmål & Elevmedvetenhet**

En webbsida för SFI spår 2-elever (kurs B, C och D) som gör Skolverkets kursmål begripliga och konkreta. Webbsidan har tre delar: förenklade kursmål med visuellt stöd, elevens egen plan för hur de ska nå målen, och en avprickningslista där eleven kan följa vilka förmågor de utvecklat. Materialet är utformat på enkel svenska med färgglada illustrationer och ikoner, i stil med det befintliga trädmaterialet.

**Core Value:** Eleverna förstår vad de ska lära sig och kan följa sin egen utveckling -- kursmålen blir ett verktyg för eleven, inte bara för läraren.

### Constraints

- **Språknivå**: Texten måste vara begriplig för SFI-elever på respektive kursnivå (B, C, D)
- **Ingen backend**: Statisk webbsida -- ingen server, databas eller inloggning
- **Uppdaterbarhet**: Kursmålen ska ligga i en separat datastruktur (t.ex. JSON) så att de enkelt kan bytas ut
- **Tillgänglighet**: Ska fungera på mobiltelefon (många elever använder mobil som primär enhet)
<!-- GSD:project-end -->

<!-- GSD:stack-start source:research/STACK.md -->
## Technology Stack

## Recommended Stack
### Core Technologies
| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Astro | 6.x (current: 6.1.5) | Site framework / static output | Purpose-built for content-driven static sites. Zero JS by default — pages ship as plain HTML. Built-in support for loading JSON data files and generating pages from them. Islands architecture means checklist interactivity is added only where needed, not globally. Content Collections API gives the JSON-to-page pipeline the project requires. |
| Tailwind CSS | 4.2.x | Utility-first styling | Fastest way to produce colorful, responsive, consistent UI without writing custom CSS files. v4 is CSS-first (no JS config), ships with modern color palettes, and is 100x faster on incremental builds. Mobile-first by default — critical given students use phones as primary devices. |
| Vanilla JavaScript | Browser native | Checkbox persistence via localStorage | No framework needed for this feature. A ~30-line script saves checked state per course (B/C/D) as JSON strings in localStorage. Survives page refresh. No install, no bundle overhead. Appropriate complexity level for a no-backend site. |
| JSON (data files) | — | Course goal data storage | Flat JSON files in `src/data/` store the simplified course goals for B, C, and D. When Skolverket updates curricula, only the JSON changes — no template code touched. Astro reads them at build time via `import`. |
### Supporting Libraries
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| lucide-astro | latest (^0.x) | Icon set | 1500+ MIT-licensed SVG icons. Official Astro integration renders icons as inline SVGs at build time — zero runtime cost, tree-shakable. Best fit for skill-domain icons (ear, eye, mouth, pen) and UI affordances. |
| @fontsource/inter | 5.x | Self-hosted typeface | Inter is highly legible at small sizes — important for low-literacy readers on mobile. Self-hosted via fontsource avoids Google Fonts privacy/GDPR concerns and works offline. |
### Development Tools
| Tool | Version | Purpose | Why |
|------|---------|---------|-----|
| Node.js | 20 LTS | Build runtime | Astro requires Node 18+. Node 20 LTS is the stable long-term support release. |
| Vite | bundled with Astro 6 | Dev server / bundler | Astro 6 ships Vite internally. No separate Vite install needed; it is the dev/build engine. |
| Prettier + prettier-plugin-astro | latest | Code formatting | Astro files (`.astro`) need the dedicated prettier plugin. Keeps templates consistent when content editors touch files. |
## Installation
# Scaffold project (interactive)
# Tailwind CSS integration (Astro official)
# Icons
# Self-hosted font
# Prettier + Astro formatter
## Alternatives Considered
| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Framework | Astro 6 | Next.js 15 | Next.js is React-first and server-oriented. This site has no backend. The React mental model adds unnecessary complexity for a teacher who may maintain the content files. |
| Framework | Astro 6 | Plain HTML + Vite | Viable for a tiny site, but Astro's component model, layout system, and JSON import pipeline save significant boilerplate as soon as there are three courses (B/C/D) each with five skill domains. |
| Framework | Astro 6 | Eleventy (11ty) | Eleventy is excellent for Markdown-heavy docs sites. This project needs visual component flexibility (colorful cards, progress indicators) that Astro's component model handles more naturally. |
| CSS | Tailwind 4 | Plain CSS | Plain CSS is fine but requires inventing and maintaining a design system from scratch. Tailwind gives consistent spacing, responsive breakpoints, and color tokens out of the box. |
| CSS | Tailwind 4 | Bootstrap 5 | Bootstrap's opinionated component classes make it harder to achieve a custom, colorful visual style. Tailwind composes better with custom illustrated layouts. |
| Icons | lucide-astro | Heroicons | Heroicons has ~300 icons; Lucide has 1500+. The skill-domain icons (listening, reading, speaking, writing) are more likely to exist in Lucide's larger set. |
| Icons | lucide-astro | Custom SVGs | Custom SVGs are the right call if the tree illustration style must be matched exactly. Lucide covers standard UI icons; use custom SVGs for the tree/nature illustrations specifically. |
| Persistence | localStorage (vanilla JS) | No persistence | Without persistence, students lose their checked items on every visit. localStorage requires zero backend and is universally supported. |
| Persistence | localStorage (vanilla JS) | IndexedDB | IndexedDB is overkill for checkbox state. localStorage holds ~5 MB and stores the entire checklist state as a single JSON string trivially. |
| Hosting | Netlify | Vercel | Both are equivalent for static Astro. Netlify is slightly simpler for non-developer maintainers (drag-and-drop deploy option, no Git required). Vercel is fine if Git workflow is already in place. |
| Hosting | Netlify | GitHub Pages | GitHub Pages works but requires a GitHub Actions workflow for Astro builds. Netlify auto-detects Astro and handles build config with zero setup. |
## What NOT to Use
| Technology | Reason |
|------------|--------|
| React / Vue / Svelte as primary framework | Adds a client-side JS runtime for content that is essentially static. Increases bundle size, complexity, and maintenance burden. Use Astro's component model instead. |
| A CMS (Contentful, Sanity, Strapi) | Heavy infrastructure for what is fundamentally a JSON file that a teacher edits once per curriculum cycle. JSON in the repo is the right scope. |
| TypeScript strict mode for data files | Adds friction when the teacher edits JSON. Keep data files as plain `.json`. TypeScript strict mode is fine for component code but should not touch data files. |
| CSS-in-JS (styled-components, Emotion) | No React, so no reason. Tailwind + Astro scoped `<style>` handles all styling needs. |
| Service Workers / PWA | Out of scope. The site works offline in practice because it is a static HTML file, but implementing a full PWA service worker adds complexity with no stated requirement. |
| Any analytics or tracking scripts | SFI students may include minors or vulnerable adults. No tracking unless explicitly required by school IT policy. |
## Sources
- [Astro GitHub Releases — v6.1.5 current](https://github.com/withastro/astro/releases)
- [Astro 6 Beta announcement](https://astro.build/blog/astro-6-beta/)
- [Building a Static Website from JSON Data with Astro](https://dev.solita.fi/2024/12/02/building-static-websites-with-astro.html)
- [Tailwind CSS v4.0 release](https://tailwindcss.com/blog/tailwindcss-v4)
- [Tailwind CSS v4.2 — InfoQ](https://www.infoq.com/news/2026/04/tailwind-css-4-2-webpack/)
- [Lucide for Astro — official guide](https://lucide.dev/guide/packages/lucide-astro)
- [Astro Icon integrations](https://astro.build/integrations/?search=icon)
- [Netlify vs Vercel vs GitHub Pages comparison](https://startupik.com/github-pages-vs-netlify-vs-vercel-which-platform-wins/)
- [localStorage checkbox persistence — Go Make Things](https://gomakethings.com/checking-of-completed-items-with-vanilla-javascript/)
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, or `.github/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
