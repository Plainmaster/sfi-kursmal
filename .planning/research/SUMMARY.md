# Project Research Summary

**Project:** SFI Spar 2 -- Kursmal & Elevmedvetenhet
**Domain:** Static educational self-assessment website for adult language learners (SFI spar 2, kurs B/C/D)
**Researched:** 2026-04-10
**Confidence:** HIGH

## Executive Summary

This project is a no-backend static website that makes Skolverket course goals comprehensible and actionable for adult immigrants learning Swedish. The audience -- SFI spar 2 students -- has low digital literacy, uses mobile phones as the primary device, and spans dozens of linguistic and cultural backgrounds. The research consensus is unambiguous: the highest-value investment is content, not technology. Simplified course goals written in plain Swedish, calibrated per course level, is the core deliverable.

The technology stack is deliberately minimal -- Astro 6 for static site generation with JSON data files, Tailwind CSS for responsive styling, and vanilla JavaScript for localStorage-backed checkbox persistence. There is no backend, no login, no server.

The key architectural insight is strict data/render separation. All course goal text lives in three JSON files (one per course), which Astro reads at build time to generate static HTML. This design directly addresses the most critical project risk: Skolverket is actively revising the SFI curriculum, with new kursplaner potentially arriving in late 2026. When that update arrives, the teacher edits one JSON file per course -- no code changes required.

The primary risks are not technical. Language calibration is the highest-risk work: every UI string and every goal statement must pass a "kurs B test" -- would a student at the lowest level understand this?

## Key Findings

### Recommended Stack

| Technology | Purpose | Rationale |
|------------|---------|-----------|
| Astro 6.x | Site framework / static output | Zero-JS by default; built-in JSON import; islands for checkbox interactivity only |
| Tailwind CSS 4.2.x | Utility-first styling | Mobile-first, CSS-first, consistent design tokens |
| Vanilla JS | localStorage checkbox persistence | ~30-line solution; no build overhead; maintainable by a non-developer |
| JSON data files (`src/data/`) | Course goal storage | Single source of truth; curriculum updates = edit JSON only |
| lucide-astro | Icons | 1500+ MIT SVGs; rendered inline at build time; zero runtime cost |
| Netlify | Hosting | Auto-detects Astro; drag-and-drop deploy for non-developer maintainer |

**What NOT to use:** React/Vue/Svelte (runtime overhead), any CMS (overkill), analytics/tracking (privacy risk for vulnerable population).

### Expected Features

**Must ship:**
- Simplified course goals for kurs B, C, D in JSON format
- Competency checklist with localStorage persistence per course
- Mobile-first responsive layout (375px viewport)
- Icon + color coding per skill area with visible text labels
- Simple Swedish calibrated to each course level
- Print stylesheet for classroom use

**Ship in MVP iteration:**
- "Min plan" practice selection checklist
- Reset button with two-step confirmation

**Anti-features to exclude:** user accounts, teacher dashboard, grading/scoring, notifications, multilingual UI, gamification.

### Architecture Approach

Three-layer static site: JSON data files -> Astro rendering (build time) -> client-side localStorage state.

Key patterns:
1. **Data/render separation** -- all course goal text in JSON only; HTML templates are goal-agnostic
2. **Namespaced localStorage keys** -- `sfi_state_b/c/d` keyed by stable goal IDs
3. **Single parameterized course component** -- one component renders all three courses from data
4. **Progressive enhancement** -- goal text visible without JS; checkboxes layer on top

### Critical Pitfalls

| Pitfall | Severity | Prevention |
|---------|----------|------------|
| Course goal text baked into HTML | Critical | JSON data layer before any HTML |
| No persistence strategy | Critical | localStorage save on every change; visible "Sparat" indicator |
| Language too difficult for students | Critical | Every UI string through "kurs B test"; teacher reviews |
| Icons without text labels | Moderate | Icon + visible label rule from day one |
| Copy-paste course B/C/D divergence | Moderate | Single parameterized component |
| Skolverket curriculum update (late 2026) | External risk | JSON data layer + `kursplan_year` field |

## Implications for Roadmap

### Phase 1: Content and Data Foundation
**Rationale:** Content is the riskiest work and blocks all UI. JSON schema must be stable before any localStorage code exists.
**Delivers:** JSON schema with locked goal IDs, simplified course goals for kurs B/C/D, UI string glossary, design system (color/icon/typography).
**Addresses pitfalls:** Content in HTML, wrong language register, icon-only, color-only.

### Phase 2: Core Checklist Product (MVP)
**Rationale:** Once schema and content exist, build the complete interactive checklist.
**Delivers:** Astro project, parameterized course component, checklist with localStorage, tab navigation (B/C/D), mobile-first layout, print stylesheet, "Sparat" indicator, reset button.
**Addresses pitfalls:** No persistence, scroll-heavy, copy-paste divergence, no print, small touch targets.

### Phase 3: "Min Plan" and Polish
**Rationale:** "Min plan" builds on stable checklist infrastructure.
**Delivers:** Min plan practice selection, visual progress indicators (validate demand first), accessibility audit.

### Phase 4: Deployment and Curriculum-Readiness
**Rationale:** Deploy and verify the curriculum update workflow end-to-end.
**Delivers:** Netlify deployment, curriculum update playbook, `kursplan_year` field.

### Phase Ordering Rationale

The hard dependency chain is: stable goal IDs -> localStorage keys -> checklist component -> "Min plan" -> deployment. Skipping Phase 1 and starting with code is the single biggest project risk.

### Research Flags

- Phase 1: No additional research needed. Content work is the constraint.
- Phase 2: Standard, well-documented patterns.
- Phase 3: One targeted question -- does showing percentage completion motivate or create anxiety in low-confidence adult learners?
- Phase 4: Standard for deployment.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Astro 6 + Tailwind 4 + vanilla JS confirmed against current releases |
| Features | HIGH | Low-literacy UX research is strong |
| Architecture | HIGH | Well-established patterns; data/render separation well-validated |
| Pitfalls | HIGH | Sourced from NNGroup, Skolverket, MDN, accessibility research |
| Content | NOT RESEARCHED | Actual goal text must come from the teacher |

**Overall: HIGH -- with one significant gap: the content itself.**

### Gaps to Address

1. **Course goal text** -- JSON data files will be empty until simplified "Jag kan..." statements are written for all five skill areas across kurs B, C, D.
2. **Existing material integration** -- Review existing drafts (Min plan, tree illustrations) before writing new content.
3. **Progress indicator UX** -- Validate whether adult SFI learners respond positively to progress bars before Phase 3.

---
*Research completed: 2026-04-10*
*Ready for roadmap: yes*
