# Phase 4: Driftsattning - Context

**Gathered:** 2026-04-11
**Status:** Ready for planning
**Mode:** approved (user approved defaults without detailed discussion)

<domain>
## Phase Boundary

Deploy the completed static Astro site to a public URL and verify the end-to-end workflow: teacher updates JSON course goals, triggers a rebuild, and the updated site goes live. Also verify cross-browser compatibility on iOS Safari and Android Chrome.

</domain>

<decisions>
## Implementation Decisions

### Hosting Platform
- **D-01:** Deploy to Netlify. CLAUDE.md recommends Netlify for its drag-and-drop simplicity and auto-detection of Astro projects. GitHub repo already exists at `Plainmaster/sfi-kursmal`.
- **D-02:** Connect Netlify to the GitHub repo for automatic deploys on push to main. Build command: `npm run build`. Publish directory: `dist/`.
- **D-03:** Use the default Netlify subdomain (e.g., `sfi-kursmal.netlify.app`). No custom domain needed for v1.

### Update Workflow for Teacher
- **D-04:** Teacher updates course goals by editing JSON files directly on GitHub (github.com file editor). No local tools needed -- the teacher opens the JSON file, edits text, commits, and Netlify rebuilds automatically.
- **D-05:** Create a brief Swedish-language guide (README or separate doc) explaining the update process step by step with screenshots or clear instructions. Target audience: a teacher with basic computer skills, not a developer.
- **D-06:** The guide should cover: which files to edit (`src/data/kurs-b.json`, `kurs-c.json`, `kurs-d.json`), what fields to change (goal text, theme tags), and what NOT to change (IDs, schema structure).

### Astro Configuration
- **D-07:** Add Netlify adapter or static output config to `astro.config.mjs` if needed. Current config has no output setting -- Astro 6 defaults to static, which is correct.
- **D-08:** Ensure `package.json` scripts work in Netlify's build environment (Node 20 LTS).

### Cross-Browser Verification
- **D-09:** Manual spot-check on iOS Safari and Android Chrome. Verify: tabs switch correctly, checkboxes toggle and persist, "Min plan" works, print stylesheet renders. No automated cross-browser testing infrastructure needed for a static site of this scope.
- **D-10:** Document any browser-specific CSS fixes needed (e.g., iOS Safari viewport units, touch event handling).

### Claude's Discretion
- Whether to use `netlify.toml` config file or Netlify dashboard settings
- Exact structure and format of the teacher update guide
- Whether to add a `_redirects` file or other Netlify-specific files
- Level of detail in the cross-browser test checklist

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project Configuration
- `astro.config.mjs` -- Current Astro config (no output adapter, Tailwind vite plugin)
- `package.json` -- Build scripts, dependencies, Node version requirements
- `CLAUDE.md` -- Technology stack and hosting recommendation (Netlify section)

### Deployment Target
- GitHub repo: `Plainmaster/sfi-kursmal` (origin remote already configured)

### Data Files (teacher update targets)
- `src/data/kurs-b.json` -- Kurs B goals (24 goals, CEFR A1)
- `src/data/kurs-c.json` -- Kurs C goals (25 goals, CEFR A2)
- `src/data/kurs-d.json` -- Kurs D goals (24 goals, CEFR B1)
- `src/data/design-tokens.json` -- Domain colors, icons, labels

### Phase 2-3 Outputs (verify these work after deploy)
- `src/pages/index.astro` -- Main page with tabs, checklist, Min plan
- `src/styles/global.css` -- Tailwind theme and print stylesheet

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- Git repo with remote already configured (`origin` -> GitHub)
- Astro static build pipeline ready (`npm run build`)
- No deployment config files exist yet -- clean slate

### Established Patterns
- Astro 6 static output (default, no SSR)
- Vite-based build via @tailwindcss/vite plugin
- JSON data imported at build time

### Integration Points
- `astro.config.mjs` may need site URL or base path config
- `package.json` may need Node version specification for Netlify
- GitHub repo needs to be pushed with latest commits before Netlify connection

</code_context>

<specifics>
## Specific Ideas

- The teacher is not a developer -- the update workflow must be as simple as possible. GitHub's web editor is the lowest-friction option that still triggers automatic rebuilds.
- The site must work immediately when opened on a phone -- no app install, no login, just a URL.
- The update guide should be in Swedish since that's the working language of the teacher.

</specifics>

<deferred>
## Deferred Ideas

- Custom domain setup (can be added later via Netlify dashboard)
- CI/CD pipeline with tests (overkill for a static site with JSON data)
- Automated cross-browser testing (manual verification sufficient for v1)
- PWA/offline support (v2 -- TILLAG-02)

</deferred>

---

*Phase: 04-driftsattning*
*Context gathered: 2026-04-11*
