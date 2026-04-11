# Phase 4: Driftsattning - Research

**Researched:** 2026-04-11
**Domain:** Static site deployment (Netlify), teacher update workflow, cross-browser verification
**Confidence:** HIGH

## Summary

Phase 4 deploys a completed static Astro 6 site to Netlify via GitHub integration. The project already has a GitHub remote (`Plainmaster/sfi-kursmal`) and a working `npm run build` pipeline. For static Astro output, no adapter or special configuration is needed -- Netlify auto-detects Astro and uses the `dist/` directory. The main deliverables beyond deployment itself are: (1) a `netlify.toml` for reproducible config, (2) a Swedish-language update guide for the teacher, and (3) manual cross-browser verification on iOS Safari and Android Chrome.

**Primary recommendation:** Use `netlify.toml` in-repo for build config (not dashboard settings). Connect the GitHub repo to Netlify via the web UI. Write the teacher guide as a standalone Markdown file in the repo root.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- D-01: Deploy to Netlify. GitHub repo at `Plainmaster/sfi-kursmal`.
- D-02: Connect Netlify to GitHub for automatic deploys on push to main. Build command: `npm run build`. Publish directory: `dist/`.
- D-03: Use default Netlify subdomain (e.g., `sfi-kursmal.netlify.app`). No custom domain for v1.
- D-04: Teacher updates JSON files via GitHub web editor. No local tools needed.
- D-05: Create Swedish-language guide explaining the update process.
- D-06: Guide covers which files to edit, what fields to change, what NOT to change.
- D-07: Add Netlify adapter or static output config if needed. Astro 6 defaults to static -- correct.
- D-08: Ensure package.json scripts work in Netlify build environment (Node 20 LTS).
- D-09: Manual spot-check on iOS Safari and Android Chrome.
- D-10: Document browser-specific CSS fixes if needed.

### Claude's Discretion
- Whether to use `netlify.toml` config file or Netlify dashboard settings
- Exact structure and format of the teacher update guide
- Whether to add a `_redirects` file or other Netlify-specific files
- Level of detail in the cross-browser test checklist

### Deferred Ideas (OUT OF SCOPE)
- Custom domain setup
- CI/CD pipeline with tests
- Automated cross-browser testing
- PWA/offline support
</user_constraints>

## Standard Stack

No new libraries are needed for this phase. Deployment uses Netlify's platform (no npm packages).

### Existing Stack (verified in repo)
| Technology | Version | Purpose |
|------------|---------|---------|
| Astro | ^6.1.5 | Static site builder |
| Node.js | 24.13.1 (local), target 20 LTS (Netlify) | Build runtime |
| npm | 11.8.0 (local) | Package manager |

### Deployment Platform
| Service | Purpose | Config |
|---------|---------|--------|
| Netlify | Static hosting, auto-deploy | `netlify.toml` in repo root |
| GitHub | Source repo, web editor for teacher | `Plainmaster/sfi-kursmal` |

**No `@astrojs/netlify` adapter needed.** The adapter is only for SSR/on-demand rendering. Static output (the default) deploys without any adapter. [VERIFIED: Astro official docs -- docs.astro.build/en/guides/deploy/netlify/]

## Architecture Patterns

### Deployment Configuration

**Recommendation:** Use `netlify.toml` in the repo (not dashboard settings). This keeps config versioned and reproducible.

```toml
# netlify.toml
[build]
  command = "npm run build"
  publish = "dist"

[build.environment]
  NODE_VERSION = "20"
```

**Why pin Node 20:** The local machine runs Node 24, but Netlify defaults vary. Pinning Node 20 LTS ensures consistent builds. The project uses `^6.1.5` Astro which requires Node 18+. [ASSUMED -- Netlify default Node version varies by account age]

**`site` property in `astro.config.mjs`:** Optional. Only affects sitemap generation and canonical URLs. Since this site has no sitemap and no SEO requirements, it can be omitted for v1. If added later:

```js
export default defineConfig({
  site: 'https://sfi-kursmal.netlify.app',
  // ...existing config
});
```

[VERIFIED: Astro docs -- site property affects sitemaps and canonical URLs only]

### Teacher Update Workflow

The workflow is: teacher edits JSON on GitHub.com -> commit triggers Netlify rebuild -> site updates in ~1 minute.

**File:** Create `UPPDATERA-KURSMAL.md` in repo root (Swedish, clear for non-developer).

**Structure recommendation:**
1. How to navigate to the right file on GitHub
2. How to use the pencil (edit) button
3. Which fields are safe to change (goal text in `mal` field, theme tags)
4. Which fields must NOT change (`id`, `domän`, `cefr_niva`, schema structure)
5. How to save (commit) the change
6. How to verify the site updated (visit URL, wait 1-2 minutes)

**Format:** Markdown with numbered steps. No screenshots needed in the file itself -- the steps are simple enough with text ("Klicka pa pennikonen uppe till hoger").

### Netlify-Specific Files

**`_redirects`:** Not needed. The site is a single-page app served from `/index.html`. No routing to handle.

**`_headers`:** Optional. Could add cache headers for static assets, but Netlify handles this well by default for static sites.

**Recommendation:** Skip `_redirects` and `_headers` for v1. The `netlify.toml` is sufficient.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Deploy pipeline | Custom GitHub Actions workflow | Netlify Git integration | Auto-detects Astro, zero config needed |
| Build command config | Dashboard-only settings | `netlify.toml` in repo | Versioned, reproducible, portable |
| Node version pinning | `.nvmrc` or `engines` field only | `NODE_VERSION` in `netlify.toml` | Netlify reads its own env vars first |

## Common Pitfalls

### Pitfall 1: Node Version Mismatch
**What goes wrong:** Build fails on Netlify because default Node version differs from local
**Why it happens:** Netlify's default Node version can be older than what Astro 6 needs (requires 18+)
**How to avoid:** Pin `NODE_VERSION = "20"` in `netlify.toml` `[build.environment]`
**Warning signs:** Build log shows "Unsupported engine" or syntax errors in modern JS

### Pitfall 2: Build Command Not Found
**What goes wrong:** Netlify can't find `npm run build` or `astro` command
**Why it happens:** Missing `npm install` step (Netlify runs it automatically, but custom build commands might skip it)
**How to avoid:** Use `npm run build` as build command (Netlify auto-runs `npm install` before it)
**Warning signs:** "command not found: astro" in build log

### Pitfall 3: iOS Safari localStorage After Clearing History
**What goes wrong:** Students lose their checkbox progress
**Why it happens:** Clearing Safari history also clears localStorage. Additionally, Safari may restrict localStorage for sites flagged as tracking.
**How to avoid:** This is expected browser behavior -- cannot be prevented. The site already handles missing localStorage gracefully (fresh state). Consider mentioning in the guide that clearing browser history resets progress.
**Warning signs:** Student reports "allt forsvann"

### Pitfall 4: iOS Safari Viewport Units
**What goes wrong:** Layout shifts when Safari's address bar shows/hides
**Why it happens:** `100vh` includes the area behind the address bar; `dvh` units shift dynamically
**How to avoid:** This site uses percentage-based and flex layouts (not viewport-height layouts), so this is unlikely to be an issue. Verify during manual testing.
**Warning signs:** Content jumps when scrolling on iOS

### Pitfall 5: Teacher Breaks JSON Syntax
**What goes wrong:** Netlify build fails after teacher edits JSON with a syntax error (missing comma, unclosed quote)
**Why it happens:** JSON is unforgiving -- one missing character breaks the entire file
**How to avoid:** The update guide must warn about this. GitHub's web editor shows basic JSON syntax highlighting but no validation. Recommend the teacher preview the file after editing. Also: Netlify sends email on build failure, which serves as an alert.
**Warning signs:** Netlify build fails, site shows old content

## Code Examples

### netlify.toml (complete)
```toml
# Netlify build configuration for Astro static site
[build]
  command = "npm run build"
  publish = "dist"

[build.environment]
  NODE_VERSION = "20"
```
Source: [Astro deployment guide](https://docs.astro.build/en/guides/deploy/netlify/) [VERIFIED]

### Teacher Update Guide Structure (Swedish)
```markdown
# Uppdatera kursmal

## Steg 1: Oppna filen
1. Ga till github.com/Plainmaster/sfi-kursmal
2. Oppna mappen `src/data/`
3. Klicka pa filen du vill andra (t.ex. `kurs-b.json`)

## Steg 2: Redigera
1. Klicka pa pennikonen (uppe till hoger)
2. Andra texten i faltet "mal" -- det ar meningen eleven ser
3. Andra INTE "id", "doman" eller "cefr_niva"

## Steg 3: Spara
1. Klicka "Commit changes..."
2. Skriv en kort beskrivning (t.ex. "Uppdaterade mal for horforstaelse")
3. Klicka "Commit changes"

## Steg 4: Vanta
Sajten uppdateras automatiskt inom 1-2 minuter.
Besok [URL] for att se andringarna.

## Vanliga misstag
- Glom inte kommatecken mellan malen
- Redigera bara texten inom citattecken ("...")
- Om sajten inte uppdateras -- kontrollera att du inte har nagon skrivfel i JSON-filen
```
[ASSUMED -- guide format is Claude's discretion per CONTEXT.md]

## Cross-Browser Test Checklist

Manual verification items for iOS Safari and Android Chrome:

| Area | What to Check | Expected |
|------|---------------|----------|
| Tabs | Tap B/C/D/Min plan tabs | Switches content without page reload |
| Checkboxes | Toggle checkboxes | Visual feedback, "Sparat" indicator appears |
| Persistence | Check boxes, close browser, reopen | Checked state preserved |
| Min plan | Select training areas | Checkboxes work, state saves |
| Print | Use share > print | Clean layout, no UI chrome |
| Responsive | Portrait and landscape | No horizontal overflow |
| Text | Read goal text | Readable font size, no truncation |
| Reset | Tap reset button | Two-step confirmation works |

[ASSUMED -- checklist depth is Claude's discretion per CONTEXT.md]

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| `@astrojs/netlify` for all deploys | Adapter only for SSR | Astro 5+ | Static sites need zero adapter config |
| Netlify dashboard config only | `netlify.toml` in repo | Long-standing best practice | Reproducible, version-controlled |
| Node 16/18 default on Netlify | Node 20 LTS available | 2024 | Pin in config to avoid surprises |

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Netlify default Node version may not be 20 | Architecture Patterns | Build could fail if default is too old; `netlify.toml` pin mitigates |
| A2 | Teacher guide format (Markdown, Swedish, numbered steps) | Code Examples | Low risk -- format is Claude's discretion |
| A3 | Cross-browser checklist items sufficient | Cross-Browser Test Checklist | Low risk -- manual testing will surface additional issues |

## Open Questions

1. **Netlify account ownership**
   - What we know: The site deploys to Netlify under someone's account
   - What's unclear: Who owns the Netlify account? Teacher? School IT? Developer?
   - Recommendation: Proceed with deployment; account ownership is an organizational decision, not a technical one

2. **GitHub repo access for teacher**
   - What we know: Teacher needs write access to edit JSON files on GitHub
   - What's unclear: Does the teacher already have a GitHub account with write access to `Plainmaster/sfi-kursmal`?
   - Recommendation: The plan should include a step to verify/grant repo access, but this is a manual step outside code scope

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Node.js | Build | Yes | 24.13.1 | Pin Node 20 on Netlify |
| npm | Package install | Yes | 11.8.0 | -- |
| Git | Push to GitHub | Yes | (system) | -- |
| Netlify CLI | Optional deploy | No | -- | Use Netlify web UI (recommended anyway) |
| GitHub repo | Source hosting | Yes | `Plainmaster/sfi-kursmal` | -- |

**Missing dependencies with no fallback:** None

**Missing dependencies with fallback:**
- Netlify CLI not installed -- not needed. Web UI connection is the recommended approach per D-02.

## Sources

### Primary (HIGH confidence)
- [Astro Netlify deployment guide](https://docs.astro.build/en/guides/deploy/netlify/) -- static deploy requires no adapter, `netlify.toml` format verified
- [Netlify Astro framework guide](https://docs.netlify.com/build/frameworks/framework-setup-guides/astro/) -- auto-detection, build settings

### Secondary (MEDIUM confidence)
- [Netlify blog: How to deploy Astro](https://www.netlify.com/blog/how-to-deploy-astro/) -- end-to-end walkthrough
- [WebKit Safari 26 release notes](https://webkit.org/blog/16993/news-from-wwdc25-web-technology-coming-this-fall-in-safari-26-beta/) -- viewport and localStorage behavior

### Tertiary (LOW confidence)
- iOS Safari localStorage clearing behavior -- based on multiple community reports, not official Apple documentation

## Metadata

**Confidence breakdown:**
- Deployment config: HIGH -- verified against official Astro and Netlify docs
- Teacher workflow: HIGH -- GitHub web editor is well-documented, JSON editing is straightforward
- Cross-browser: MEDIUM -- known issues documented but manual testing will be definitive
- Pitfalls: HIGH -- common deployment issues are well-known

**Research date:** 2026-04-11
**Valid until:** 2026-05-11 (stable domain, unlikely to change)
