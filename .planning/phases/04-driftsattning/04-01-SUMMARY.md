---
phase: 04-driftsattning
plan: 01
status: complete
completed: 2026-04-11
---

## Summary

Deployed the static Astro site to Netlify via GitHub integration.

### What was done
- Created `netlify.toml` with build command (`npm run build`), publish directory (`dist`), and Node 22 pinned
- Fixed Node version: Astro 6 requires Node >= 22.12.0, initial pin of Node 20 caused build failure
- Committed and pushed missing `src/pages/trad.astro` (kunskapsträdet page was untracked, causing 404)
- Pushed all commits to `origin/master` on GitHub
- User connected Netlify to `Plainmaster/sfi-kursmal` via Netlify web UI
- Site is live and all pages accessible (Kurs B, C, D, Min plan, Resurser, Kunskapsträdet)

### Issues encountered
1. **Node version mismatch** — Astro 6 requires Node >= 22, not Node 20. Fixed by updating `netlify.toml` to `NODE_VERSION = "22"`.
2. **Missing page** — `trad.astro` was never committed to git, causing a 404 on `/trad`. Fixed by committing the file.

### Artifacts
- `netlify.toml` — Netlify build configuration
- Site deployed at Netlify `.netlify.app` URL with auto-deploy from GitHub main
