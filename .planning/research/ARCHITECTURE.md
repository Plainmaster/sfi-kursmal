# Architecture Patterns

**Project:** SFI Spår 2 -- Kursmål & Elevmedvetenhet
**Researched:** 2026-04-10
**Confidence:** HIGH (patterns are well-established; no exotic dependencies)

---

## Recommended Architecture

A three-layer static site: static data files (JSON) → rendering layer (vanilla HTML/CSS/JS) → client-side state (localStorage). No build step required. No framework required. Deploy anywhere as a folder of files.

```
┌──────────────────────────────────────────────────────┐
│                    Browser                           │
│                                                      │
│  ┌──────────────┐   fetch()   ┌──────────────────┐  │
│  │   JS App     │ ──────────> │  JSON Data Files │  │
│  │  (renderer)  │             │  (course goals)  │  │
│  └──────┬───────┘             └──────────────────┘  │
│         │ reads/writes                               │
│  ┌──────▼───────┐                                    │
│  │ localStorage │  (checkbox state, per course)      │
│  └──────────────┘                                    │
│         │ renders into                               │
│  ┌──────▼───────┐                                    │
│  │     DOM      │  (HTML views: B / C / D)           │
│  └──────────────┘                                    │
└──────────────────────────────────────────────────────┘
```

---

## Component Boundaries

| Component | Responsibility | Communicates With |
|-----------|---------------|-------------------|
| `data/goals-b.json` | Course B goals, 5 skill areas, simplified text | Read by JS renderer |
| `data/goals-c.json` | Course C goals | Read by JS renderer |
| `data/goals-d.json` | Course D goals | Read by JS renderer |
| `js/renderer.js` | Loads JSON, builds DOM for the active course view | Reads JSON, writes DOM |
| `js/state.js` | Reads and writes checkbox state to localStorage | Called by renderer and event handlers |
| `js/nav.js` | Handles course tab switching (B / C / D) | Triggers renderer |
| `css/styles.css` | Visual design, color coding per course, responsive layout | Consumed by HTML |
| `index.html` | Shell: nav tabs, course containers, script/style links | Entry point |
| `assets/` | Icons, illustrations (tree-style images) | Referenced by CSS and HTML |

**Boundary rule:** JSON files contain only data (no HTML, no logic). JS files contain only behavior (no hardcoded goal text). HTML/CSS files contain only structure and style (no goal text, no logic).

---

## Data Flow

```
1. User opens index.html
       │
       ▼
2. index.html loads styles.css + renderer.js
       │
       ▼
3. renderer.js fetches data/goals-b.json (default course B)
       │
       ▼
4. renderer.js builds DOM: course sections, skill areas, checkboxes
       │
       ▼
5. state.js reads localStorage → restores any previously checked boxes
       │
       ▼
6. User ticks a checkbox
       │
       ▼
7. Event handler → state.js writes updated state to localStorage
       │
       ▼
8. User switches to course C tab
       │
       ▼
9. nav.js fires → renderer.js fetches goals-c.json → rebuilds view
       │
       ▼
10. state.js reads localStorage for course C → restores state
```

**State key design:** Store checkbox state namespaced by course to prevent collisions:

```
localStorage key: "sfi_state_b"  →  { "horforstaelse_1": true, "lasforstaelse_3": true, ... }
localStorage key: "sfi_state_c"  →  { ... }
localStorage key: "sfi_state_d"  →  { ... }
```

---

## JSON Data Schema (per course file)

```json
{
  "course": "B",
  "skill_areas": [
    {
      "id": "horforstaelse",
      "label": "Hörförståelse",
      "icon": "ear",
      "color": "#4CAF50",
      "goals": [
        {
          "id": "horforstaelse_1",
          "text": "Jag kan förstå enkla samtal om vardagliga ämnen.",
          "plan_item": true,
          "checklist_item": true
        }
      ]
    }
  ]
}
```

**Schema decisions:**
- `id` must be stable across updates — it is the key used in localStorage. If Skolverket updates curriculum, add new IDs, do not reuse old ones. Old checkbox state becomes orphaned silently (no crash).
- `plan_item` and `checklist_item` flags allow the same data file to drive both the "Min plan" section and the "Avprickning" section without duplicating data.
- `color` and `icon` live in the data file so that the visual coding for a skill area can be updated without touching CSS.

---

## Patterns to Follow

### Pattern 1: Data/Render Separation
**What:** Goal text lives exclusively in JSON files. JS renders it into HTML at runtime. HTML template is goal-agnostic.
**When:** Always — this is the core updateability mechanism.
**Why:** When Skolverket publishes new kursplaner in 2026, the teacher edits only the JSON files. No HTML, no JS changes needed.

### Pattern 2: Namespaced localStorage Keys
**What:** Prefix all storage keys with `sfi_state_{course}_{id}`.
**When:** Any write to localStorage.
**Why:** Prevents key collisions across courses and future features. Makes it trivial to reset one course's state without affecting others.

### Pattern 3: Progressive Enhancement
**What:** Core content (goal text) is visible even with JS disabled or slow. Interactivity (checkboxes) layers on top.
**When:** HTML is rendered by the server/static host before JS executes.
**Why:** Students on slow mobile connections see content immediately. Many SFI students use older Android phones on weak connections.
**Implementation:** Render goal text in `<noscript>`-safe HTML or server-side via a static site generator pre-render step if needed (optional optimization).

### Pattern 4: Single-File-Per-Course View
**What:** Each course (B, C, D) is a self-contained section in the DOM, hidden/shown via CSS class.
**When:** Tab switching.
**Why:** Avoids full page reload on tab switch, which would reset scroll position and feel sluggish. Simpler than a router.

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Goal Text in HTML
**What:** Writing course goal text directly in index.html.
**Why bad:** Every Skolverket curriculum update requires editing HTML. Risk of breaking layout. Not maintainable by a non-developer.
**Instead:** All goal text in JSON files. HTML only contains the structural skeleton.

### Anti-Pattern 2: Single Monolithic JSON File
**What:** One `goals.json` with all three courses.
**Why bad:** When updating course B goals, you must touch the same file that stores C and D goals. Merge risk. Also loads all data even when user only visits one course.
**Instead:** Separate file per course (`goals-b.json`, `goals-c.json`, `goals-d.json`). Load on demand.

### Anti-Pattern 3: Storing State as a Single Flat String
**What:** `localStorage.setItem("checkboxes", "1,0,1,0,1,...")`.
**Why bad:** Adding or removing goals in a future curriculum update shifts all indices. Old stored state maps to wrong goals.
**Instead:** Store as an object keyed by stable goal IDs (see schema above).

### Anti-Pattern 4: Framework Overhead for This Scope
**What:** Reaching for React, Vue, or a bundler (webpack/vite) for a site of this complexity.
**Why bad:** Adds build tooling, increases maintenance surface, makes it harder for a non-developer teacher to update the JSON. Overkill for ~30 interactive checkboxes per course.
**Instead:** Vanilla JS. No build step. The file is editable in VS Code or Notepad. Deployable by dragging a folder to a web server or GitHub Pages.

---

## File Structure

```
/
├── index.html               # Shell with tab nav and course containers
├── css/
│   └── styles.css           # All visual styling, responsive, course colors
├── js/
│   ├── renderer.js          # Fetches JSON, builds DOM
│   ├── state.js             # localStorage read/write
│   └── nav.js               # Tab switching logic
├── data/
│   ├── goals-b.json         # Course B goals (the only file to edit for B curriculum)
│   ├── goals-c.json         # Course C goals
│   └── goals-d.json         # Course D goals
└── assets/
    ├── icons/               # SVG icons per skill area
    └── illustrations/       # Tree-style images, course illustrations
```

---

## Scalability Considerations

| Concern | Current scope | If extended later |
|---------|--------------|-------------------|
| State storage | localStorage (~5MB, plenty for checkbox booleans) | Still fine for 100s of goals |
| Curriculum update | Edit JSON file only | Same — no code changes |
| New course (e.g. A) | Add `goals-a.json` + new tab in HTML | Minimal change |
| Print support | CSS `@media print` to produce a printable checklist | CSS-only change |
| Teacher export | Not in scope; if needed, JSON.stringify state to clipboard | JS-only addition |
| Offline use | Service Worker can cache all assets for offline access | Add `sw.js`, register in index.html |

---

## Suggested Build Order (phase dependencies)

1. **JSON data schema + data files** — everything else depends on this. Define IDs now; changing them later invalidates localStorage state for all users.
2. **HTML skeleton** — course tabs, structural containers. No styling yet.
3. **Core renderer** — fetch JSON, render goal list into DOM. Validates data schema.
4. **CSS visual design** — color coding, icons, responsive layout, course-specific colors.
5. **State module (localStorage)** — checkbox persistence. Depends on stable IDs from step 1 and DOM structure from step 3.
6. **Tab navigation** — course switching, show/hide logic. Depends on renderer and state.
7. **Assets** — icons and illustrations. Can be added at any point after step 4.
8. **Print stylesheet** (optional) — CSS-only, independent.

**Critical dependency:** Steps 1 and 3 must be stable before step 5. If goal IDs change after localStorage is in use, stored state is silently orphaned. Decide ID naming convention before writing any JS.

---

## Sources

- [MDN Client-side storage](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Client-side_storage) — localStorage API, 5MB limit, JSON serialization pattern (HIGH confidence)
- [State Management in Vanilla JS: 2026 Trends](https://medium.com/@chirag.dave/state-management-in-vanilla-js-2026-trends-f9baed7599de) — namespaced keys, batched DOM updates (MEDIUM confidence)
- [Making Your SPA Remember State with localStorage](https://dev.to/linou518/making-your-spa-remember-state-with-localstorage-3-patterns-and-their-pitfalls-30jo) — patterns and pitfalls (MEDIUM confidence)
- [EdX course_structure JSON format](https://edx.readthedocs.io/projects/devdata/en/latest/internal_data_formats/course_structure.html) — educational JSON schema precedent (MEDIUM confidence, different scale)
