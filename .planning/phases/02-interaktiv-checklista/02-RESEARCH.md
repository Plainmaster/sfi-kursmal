# Phase 2: Interaktiv checklista - Research

**Researched:** 2026-04-10
**Domain:** Astro 6 static site with Tailwind CSS 4, vanilla JS interactivity, localStorage persistence
**Confidence:** HIGH

## Summary

This phase scaffolds the entire Astro project and builds a single-page interactive checklist where SFI students view course goals grouped by skill domain, toggle checkboxes, and have their progress persisted via localStorage. The tech stack is fully locked by CLAUDE.md and CONTEXT.md decisions: Astro 6, Tailwind CSS 4 (via Vite plugin), @lucide/astro icons, @fontsource/inter typography, and vanilla JavaScript for client-side interactivity.

The project currently has NO Astro scaffold -- only `src/data/` with 4 JSON files from Phase 1. Phase 2 must create the full project structure (package.json, astro.config.mjs, layouts, pages, components, styles) while preserving the existing data files. The interactive features (tab switching, checkbox toggling, save feedback, reset flow) are all client-side vanilla JS with no framework needed.

**Primary recommendation:** Scaffold Astro 6 with `npm create astro@latest`, add Tailwind via `@tailwindcss/vite` Vite plugin (NOT the deprecated `@astrojs/tailwind` integration), build a single `index.astro` page with client-side tab switching, and use a `<script>` tag for all interactivity (localStorage, checkboxes, reset).

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** Scaffold Astro 6 project with Tailwind CSS 4 integration per CLAUDE.md stack recommendation. Install lucide-astro for icons and @fontsource/inter for typography.
- **D-02:** Project root is the current directory. `src/data/` already exists with JSON files from Phase 1.
- **D-03:** Tabs at the TOP of the page, always visible (sticky). Three tabs labeled "Kurs B", "Kurs C", "Kurs D".
- **D-04:** Tab switching uses vanilla JS (no page reload). When switching tabs, scroll to top of content area. Active tab gets a colored underline matching the course.
- **D-05:** Default tab is "Kurs B".
- **D-06:** Tab state is NOT persisted in localStorage.
- **D-07:** Goals grouped by skill domain with colored section headers using design-tokens.json colors/icons.
- **D-08:** Each goal is a checkbox row (not cards). Clean list within each domain section.
- **D-09:** Domain sections expanded by default (no accordion).
- **D-10:** Domain header bars use design-tokens colors as background. White text on colored background.
- **D-11:** Icons always paired with text labels. Icon size at least 24px.
- **D-12:** Inline "Sparat!" text near checkbox that fades after 1.5 seconds on toggle.
- **D-13:** Progress count per domain: "3 av 5 avklarade" below domain header.
- **D-14:** localStorage key format: `sfi-checklist-{course}` (e.g., `sfi-checklist-B`). Value is JSON object mapping goal IDs to boolean.
- **D-15:** Reset button at bottom of each course tab. Labeled "Borja om" with subdued style.
- **D-16:** Two-step confirmation for reset.
- **D-17:** Reset is per-course, not global.
- **D-18:** No browser close warning.
- **D-19:** Mobile-first: 375px viewport as primary. Desktop max-width container, centered.
- **D-20:** Touch targets minimum 44px height for checkboxes and tabs.
- **D-21:** Font size minimum 16px for body text.

### Claude's Discretion
- Exact Tailwind configuration and theme setup
- Astro page structure (single page with client-side tabs vs multi-page)
- Specific animation/transition details for the "Sparat!" indicator
- Whether to use Astro islands or plain script tags for interactivity
- Exact spacing, padding, and margin values

### Deferred Ideas (OUT OF SCOPE)
- "Min plan" section with "Jag ska..." items (Phase 3)
- Print view via @media print (Phase 3)
- Accordion/collapsible domain sections (v2 -- TILLAG-04)
- Progress indicator visualization like progress bars (v2 -- TILLAG-01)
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| INTER-01 | Avprickningslista dar eleven kryssar av uppnadda formagor per kurs | Checkbox rows per goal within domain sections, JSON data provides goal IDs |
| INTER-02 | Checkbox-state sparas i webblasarens localStorage per kurs | localStorage with key `sfi-checklist-{course}`, JSON object mapping goal IDs to booleans |
| INTER-04 | Synlig "Sparat"-indikator nar eleven kryssar i nagot | Inline "Sparat!" text with CSS fade animation, 1.5s duration |
| INTER-05 | Aterstallningsknapp med tvastegsbekraftelse | Per-course reset button with confirm/cancel UI |
| DESIGN-01 | Mobilforst responsiv design (375px viewport som minimum) | Tailwind CSS 4 mobile-first utilities, min 44px touch targets, 16px body text |
| DESIGN-02 | Flikar/navigation for att vaxla mellan kurs B, C och D utan omladdning | Sticky top tabs with vanilla JS switching, no page reload |
| DESIGN-03 | Fargglad visuell stil inspirerad av tradmaterialet | Design tokens provide 5 domain colors; domain header bars with colored backgrounds |
| DESIGN-04 | Ikoner alltid parade med textbeskrivning | Lucide icons rendered at build time via @lucide/astro, always with text labels |
</phase_requirements>

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| astro | 6.1.5 | Site framework / static output | [VERIFIED: npm registry] Purpose-built for content-driven static sites. Zero JS by default. |
| tailwindcss | 4.2.2 | Utility-first styling | [VERIFIED: npm registry] CSS-first config, mobile-first by default. |
| @tailwindcss/vite | 4.2.2 | Tailwind Vite integration | [VERIFIED: npm registry] Required for Astro 6 + Tailwind 4. Replaces deprecated @astrojs/tailwind. |
| @lucide/astro | 1.8.0 | Icon set | [VERIFIED: npm registry] Replaces deprecated `lucide-astro`. Renders inline SVGs at build time. |
| @fontsource/inter | 5.2.8 | Self-hosted typeface | [VERIFIED: npm registry] Legible at small sizes, self-hosted avoids GDPR concerns. |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| prettier | latest | Code formatting | Development only |
| prettier-plugin-astro | 0.14.1 | Astro file formatting | [VERIFIED: npm registry] Required for .astro file formatting |

### CRITICAL: Package Name Change
`lucide-astro` is deprecated. Use `@lucide/astro` instead. [VERIFIED: npm registry -- `lucide-astro` shows deprecated message pointing to `@lucide/astro`]

### CRITICAL: Tailwind Integration Change
Do NOT use `@astrojs/tailwind` (the old Astro integration). Tailwind CSS v4 uses `@tailwindcss/vite` as a Vite plugin directly. [CITED: https://tailwindcss.com/docs/installation/framework-guides/astro]

**Installation:**
```bash
# Scaffold Astro (use --template minimal, answer prompts non-interactively)
npm create astro@latest . -- --template minimal --no-install

# Install dependencies
npm install astro tailwindcss @tailwindcss/vite @lucide/astro @fontsource/inter

# Dev dependencies
npm install -D prettier prettier-plugin-astro
```

Note: `npm create astro@latest` is interactive. For automated execution, use `--template minimal` and handle the existing directory. The planner should account for this being potentially interactive and provide fallback manual setup.

## Architecture Patterns

### Recommended Project Structure
```
/
├── src/
│   ├── data/                    # EXISTING -- Phase 1 JSON files
│   │   ├── design-tokens.json
│   │   ├── kurs-b.json
│   │   ├── kurs-c.json
│   │   └── kurs-d.json
│   ├── components/
│   │   ├── TabNav.astro         # Course tab navigation (B, C, D)
│   │   ├── CoursePanel.astro    # All domains + goals for one course
│   │   ├── DomainSection.astro  # One skill domain header + goal list
│   │   ├── GoalCheckbox.astro   # Single checkbox row
│   │   └── ResetButton.astro    # Reset with two-step confirmation
│   ├── layouts/
│   │   └── BaseLayout.astro     # HTML head, font import, global CSS
│   ├── styles/
│   │   └── global.css           # @import "tailwindcss" + custom @theme
│   └── pages/
│       └── index.astro          # Single page -- imports all components
├── public/                      # Static assets (favicon etc.)
├── astro.config.mjs
├── package.json
└── .prettierrc
```

### Pattern 1: Single Page with Client-Side Tabs (RECOMMENDED)
**What:** One `index.astro` page renders all three course panels. Vanilla JS shows/hides panels based on active tab.
**When to use:** This project -- all content is known at build time, tab switching must be instant.
**Why not multi-page:** Multi-page would cause full page reloads, losing scroll position and violating DESIGN-02.

```astro
<!-- Source: Architecture recommendation based on project constraints -->
---
import kursB from '../data/kurs-b.json';
import kursC from '../data/kurs-c.json';
import kursD from '../data/kurs-d.json';
import tokens from '../data/design-tokens.json';
---

<!-- All three panels rendered at build time, JS toggles visibility -->
<div id="panel-B" class="course-panel">...</div>
<div id="panel-C" class="course-panel hidden">...</div>
<div id="panel-D" class="course-panel hidden">...</div>
```

### Pattern 2: Vanilla JS in Astro via `<script>` Tags
**What:** Astro ships `<script>` tags as bundled JS. No island/framework needed for this level of interactivity.
**When to use:** When interactivity is DOM manipulation (show/hide, toggle classes, read/write localStorage) -- no complex state management needed. [CITED: Astro docs -- scripts are bundled by Vite]

```astro
<!-- In index.astro or a component -->
<script>
  // This runs in the browser. Astro bundles it via Vite.
  const panels = document.querySelectorAll('.course-panel');
  const tabs = document.querySelectorAll('.course-tab');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const course = tab.dataset.course;
      panels.forEach(p => p.classList.toggle('hidden', p.id !== `panel-${course}`));
      tabs.forEach(t => t.classList.toggle('active', t === tab));
    });
  });
</script>
```

### Pattern 3: localStorage Persistence Pattern
**What:** Save checkbox state as JSON object per course. Load on page init, save on every toggle.

```javascript
// Key format per D-14
const STORAGE_KEY = (course) => `sfi-checklist-${course}`;

function loadState(course) {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY(course))) || {};
  } catch {
    return {};
  }
}

function saveGoal(course, goalId, checked) {
  const state = loadState(course);
  state[goalId] = checked;
  localStorage.setItem(STORAGE_KEY(course), JSON.stringify(state));
}

function resetCourse(course) {
  localStorage.removeItem(STORAGE_KEY(course));
}
```

### Pattern 4: Astro Component with Dynamic Lucide Icons
**What:** Since icon names come from design-tokens.json, and Astro components run at build time, you can use a mapping approach.

```astro
---
// In DomainSection.astro
import { Ear, BookOpen, MessageCircle, Mic, PenLine } from '@lucide/astro';

const iconMap = { Ear, BookOpen, MessageCircle, Mic, PenLine };
const IconComponent = iconMap[domain.icon];
---

{IconComponent && <IconComponent size={24} class="text-white" />}
```
[ASSUMED: This dynamic icon mapping pattern should work in Astro since components are resolved at build time. Astro supports dynamic component rendering.]

### Pattern 5: Tailwind CSS v4 Custom Theme via @theme
**What:** Define custom colors from design-tokens in CSS using Tailwind v4's @theme directive.

```css
/* src/styles/global.css */
@import "tailwindcss";

@theme {
  --color-domain-hora: #D97706;
  --color-domain-lasa: #2563EB;
  --color-domain-prata: #16A34A;
  --color-domain-beratta: #7C3AED;
  --color-domain-skriva: #DC2626;
}
```
[CITED: https://tailwindcss.com/docs/installation/framework-guides/astro -- Tailwind v4 CSS-first config]

Then use as `bg-domain-hora`, `text-domain-lasa` etc. in templates.

### Anti-Patterns to Avoid
- **Using @astrojs/tailwind integration:** Deprecated for Tailwind v4. Use @tailwindcss/vite directly. [VERIFIED: npm search + Tailwind docs]
- **Using React/Vue for tabs:** Adds runtime JS framework for what is simple show/hide logic. Vanilla JS is correct here per CLAUDE.md.
- **Storing full goal text in localStorage:** Only store goal IDs mapped to booleans. Text comes from JSON at build time.
- **Using `<style>` scoped blocks with @apply in Astro components:** Tailwind v4 requires `@reference` to use @apply inside scoped styles. Prefer utility classes directly or use global.css.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Icons | Custom SVG sprite system | @lucide/astro | All 5 needed icons (Ear, BookOpen, MessageCircle, Mic, PenLine) verified to exist in Lucide |
| Responsive grid | Custom media queries | Tailwind responsive utilities | `sm:`, `md:`, `lg:` prefixes handle all breakpoints |
| Color system | Manual hex values in templates | Tailwind @theme custom properties | Single source of truth, used as utility classes |
| Font loading | Manual @font-face rules | @fontsource/inter | Handles font formats, weights, and loading strategy |

## Common Pitfalls

### Pitfall 1: Astro Scaffold Overwrites Existing src/data/
**What goes wrong:** `npm create astro@latest` may create a fresh `src/` directory, potentially conflicting with existing `src/data/` files.
**Why it happens:** The scaffold assumes an empty directory.
**How to avoid:** Back up `src/data/` before scaffolding, or scaffold into a temp directory and merge. Alternatively, manually create the project structure (package.json, astro.config.mjs) without the scaffold command.
**Warning signs:** Missing JSON files after scaffold.

### Pitfall 2: @astrojs/tailwind vs @tailwindcss/vite Confusion
**What goes wrong:** Using the old `@astrojs/tailwind` integration with Tailwind v4 causes build errors or missing styles.
**Why it happens:** Many tutorials and even Astro's own integration page still reference the old integration.
**How to avoid:** Use `@tailwindcss/vite` as a Vite plugin in `astro.config.mjs`, NOT as an Astro integration. [CITED: https://tailwindcss.com/docs/installation/framework-guides/astro]
**Warning signs:** `@astrojs/tailwind` in config, tailwind.config.js file present (v4 doesn't need one).

### Pitfall 3: Scoped Styles and Tailwind v4
**What goes wrong:** Using `@apply` inside Astro component `<style>` blocks fails because Tailwind v4 requires `@reference` for separate stylesheets.
**Why it happens:** Tailwind v4 changed how theme variables are scoped.
**How to avoid:** Use utility classes directly in HTML (the Tailwind way). If @apply is needed in a component, add `@reference "../styles/global.css"` at the top of the style block.
**Warning signs:** "Unknown at rule @apply" errors, missing utility classes in scoped styles.

### Pitfall 4: iOS Safari Zoom on Input Focus
**What goes wrong:** iOS Safari zooms in when a user taps a form element with font-size below 16px.
**Why it happens:** Safari "helps" by zooming to make small text readable.
**How to avoid:** D-21 already addresses this -- ensure minimum 16px font size. Also set `<meta name="viewport" content="width=device-width, initial-scale=1">` in the layout head. Do NOT add `maximum-scale=1` as it breaks accessibility.
**Warning signs:** Page zooms unexpectedly on mobile when tapping checkboxes.

### Pitfall 5: localStorage Quota or Disabled
**What goes wrong:** localStorage throws an error when storage is full or disabled (private browsing on some older browsers).
**Why it happens:** Private browsing modes on older Safari had localStorage disabled.
**How to avoid:** Wrap all localStorage calls in try/catch. The site should work without persistence -- checkboxes still toggle, just don't persist.
**Warning signs:** Uncaught exceptions in console, checkboxes not saving.

### Pitfall 6: Checkbox Touch Target Too Small
**What goes wrong:** Default browser checkboxes are ~16px, far below the 44px WCAG requirement (D-20).
**Why it happens:** Browser default checkbox styling is tiny.
**How to avoid:** Style checkboxes with Tailwind's `w-6 h-6` (24px) minimum, and ensure the clickable label area extends the touch target to 44px via padding on the label/row.
**Warning signs:** Difficult to tap checkboxes on mobile.

## Code Examples

### Astro Config for Tailwind v4
```javascript
// astro.config.mjs
// Source: https://tailwindcss.com/docs/installation/framework-guides/astro
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
  },
});
```

### Global CSS with Custom Theme
```css
/* src/styles/global.css */
/* Source: Tailwind v4 @theme directive */
@import "tailwindcss";
@import "@fontsource/inter/latin-400.css";
@import "@fontsource/inter/latin-600.css";
@import "@fontsource/inter/latin-700.css";

@theme {
  --font-sans: "Inter", sans-serif;
  --color-domain-hora: #D97706;
  --color-domain-lasa: #2563EB;
  --color-domain-prata: #16A34A;
  --color-domain-beratta: #7C3AED;
  --color-domain-skriva: #DC2626;
}
```

### Base Layout
```astro
<!-- src/layouts/BaseLayout.astro -->
---
import "../styles/global.css";
---
<!doctype html>
<html lang="sv">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SFI Spar 2 -- Kursmal</title>
  </head>
  <body class="font-sans bg-gray-50 text-gray-900">
    <slot />
  </body>
</html>
```

### "Sparat!" Fade Animation (CSS only)
```css
/* In global.css */
@keyframes fade-out {
  0% { opacity: 1; }
  70% { opacity: 1; }
  100% { opacity: 0; }
}

.saved-indicator {
  animation: fade-out 1.5s ease-out forwards;
}
```

### Two-Step Reset Confirmation Pattern
```javascript
// Vanilla JS pattern for D-15, D-16
function initReset(course) {
  const btn = document.querySelector(`[data-reset="${course}"]`);
  const confirm = document.querySelector(`[data-confirm="${course}"]`);

  btn.addEventListener('click', () => {
    btn.classList.add('hidden');
    confirm.classList.remove('hidden');
  });

  confirm.querySelector('.cancel').addEventListener('click', () => {
    confirm.classList.add('hidden');
    btn.classList.remove('hidden');
  });

  confirm.querySelector('.confirm').addEventListener('click', () => {
    localStorage.removeItem(`sfi-checklist-${course}`);
    // Uncheck all checkboxes in this course panel
    document.querySelectorAll(`#panel-${course} input[type="checkbox"]`)
      .forEach(cb => { cb.checked = false; });
    // Reset progress counts
    updateAllProgressCounts(course);
    confirm.classList.add('hidden');
    btn.classList.remove('hidden');
  });
}
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| @astrojs/tailwind integration | @tailwindcss/vite plugin | Tailwind v4 (Jan 2025) | Config goes in astro.config.mjs vite.plugins, not integrations |
| tailwind.config.js | CSS @theme directive | Tailwind v4 (Jan 2025) | Theme customization in global.css, no JS config file |
| `lucide-astro` package | `@lucide/astro` scoped package | 2025 | Old package deprecated, use scoped name |

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Dynamic icon component mapping via iconMap works in Astro build-time rendering | Architecture Patterns - Pattern 4 | LOW -- if it fails, use explicit conditionals instead |
| A2 | @fontsource/inter imports work inside Tailwind v4 @import chain | Code Examples - Global CSS | LOW -- if not, import in BaseLayout.astro frontmatter instead |
| A3 | `npm create astro@latest . -- --template minimal` works for in-place scaffold | Standard Stack - Installation | MEDIUM -- may need manual project setup if interactive prompts block automation |

## Open Questions

1. **Astro scaffold in non-empty directory**
   - What we know: `src/data/` already exists with 4 files. `npm create astro@latest .` may conflict.
   - What's unclear: Whether the minimal template creates a `src/data/` directory or leaves it alone.
   - Recommendation: The planner should include a step to back up `src/data/`, scaffold, then restore. Or skip the scaffold entirely and manually create package.json + astro.config.mjs.

2. **Course-specific tab colors**
   - What we know: D-04 says "Active tab gets a colored underline matching the course." Design tokens define domain colors, not course colors.
   - What's unclear: What color each course tab should use (no course-level colors defined).
   - Recommendation: Use a neutral accent (e.g., blue-600) for all tabs, or pick one domain color per course. This is within Claude's discretion.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Node.js | Astro build | Yes | v24.13.1 | -- |
| npm | Package management | Yes | 11.8.0 | -- |

**Missing dependencies:** None. All required tools are available.

## Project Constraints (from CLAUDE.md)

- **No backend:** Static site only -- no server, database, or login
- **No React/Vue/Svelte:** Use Astro component model + vanilla JS
- **No CMS:** JSON files in repo are the data source
- **No analytics/tracking:** Privacy-sensitive audience
- **No Service Workers/PWA:** Out of scope
- **No CSS-in-JS:** Use Tailwind + Astro scoped styles
- **Data files stay as plain JSON:** No TypeScript strict mode on data files
- **Mobile-first:** Many students use phone as primary device
- **JSON data in src/data/:** Separate from template code for easy updates

## Sources

### Primary (HIGH confidence)
- [npm registry] -- astro 6.1.5, tailwindcss 4.2.2, @tailwindcss/vite 4.2.2, @lucide/astro 1.8.0, @fontsource/inter 5.2.8, prettier-plugin-astro 0.14.1
- [Tailwind CSS official Astro guide](https://tailwindcss.com/docs/installation/framework-guides/astro) -- setup steps, @tailwindcss/vite config
- [Lucide icons](https://lucide.dev/icons/) -- verified Ear, BookOpen, MessageCircle, Mic, PenLine icons exist

### Secondary (MEDIUM confidence)
- [Tailkits Astro + Tailwind v4 guide](https://tailkits.com/blog/astro-tailwind-setup/) -- confirmed @astrojs/tailwind is deprecated for v4
- [Lucide Astro guide](https://lucide.dev/guide/packages/lucide-astro) -- import pattern for @lucide/astro

### Tertiary (LOW confidence)
- None -- all claims verified against npm registry or official docs

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- all versions verified against npm registry
- Architecture: HIGH -- patterns derived from locked decisions + official docs
- Pitfalls: HIGH -- based on verified Tailwind v4 migration changes and known localStorage behaviors

**Research date:** 2026-04-10
**Valid until:** 2026-05-10 (stable stack, 30-day validity)
