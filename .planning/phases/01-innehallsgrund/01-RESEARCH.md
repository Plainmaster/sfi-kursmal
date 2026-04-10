# Phase 1: Innehållsgrund - Research

**Researched:** 2026-04-10
**Domain:** JSON data schema design, Swedish SFI curriculum content authoring, design token structure
**Confidence:** HIGH (schema patterns), MEDIUM (colorblind-safe palette specifics), HIGH (content strategy)

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**JSON Schema Design**
- D-01: One JSON file per course: `kurs-b.json`, `kurs-c.json`, `kurs-d.json` in `src/data/`. Teacher edits one file at a time.
- D-02: Goal ID format: `{COURSE}-{DOMAIN}-{NN}` (e.g., `B-LASA-01`, `C-HORA-03`). Stable across curriculum updates.
- D-03: Each goal object has: `id`, `text` (the "Jag kan..." statement), `kursplan_year` (integer, e.g. 2018), `themes` (string array).
- D-04: Goals grouped by skill domain within each file. Top-level structure: `{ kursplan_year: 2018, domains: { horforstaelse: { goals: [...] }, lasforstaelse: { goals: [...] }, ... } }`.

**Course Goal Text (Kursmålstext)**
- D-05: Follow the existing "Jag kan..." format from the kurs B material. Each goal is a concrete, checkable statement.
- D-06: Simplify Skolverket's official criteria text to plain Swedish appropriate for each course level (B = simplest, D = most complex language).
- D-07: Same structural format for B, C, and D. Complexity increases in the text content, not in the data structure.
- D-08: Use the existing `Kursmal och checklista for elever.md` as the primary source for kurs B goals. Kurs C and D goals must be authored following the same pattern based on Skolverket's official criteria.

**Theme Mapping (Tema-koppling)**
- D-09: Many-to-many relationship: each goal has a `themes` array with 0-N theme strings.
- D-10: Theme values match the 7 årshjul themes exactly: `relationer`, `miljo`, `bostad`, `arbete-och-studier`, `fritid-och-halsa`, `hogtider`, `samhalle`.
- D-11: Not all goals require a theme tag. Generic language skills may have an empty themes array.

**Design System Foundation**
- D-12: Five distinct colors assigned to the five skill domains. Bright, friendly palette inspired by the tree material.
- D-13: Lucide icon assignments: horforstaelse = Ear, lasforstaelse = BookOpen, muntlig interaktion = MessageCircle, muntlig produktion = Mic, skriftlig fardighet = PenLine.
- D-14: Color and icon mappings stored in a separate `design-tokens.json` (or equivalent) in `src/data/`.

### Claude's Discretion
- Exact hex color values for the 5 skill domain colors (should be high-contrast, colorblind-friendly, and visually warm/inviting)
- JSON file indentation and formatting conventions
- Whether to include a JSON schema validation file (recommended but optional)

### Deferred Ideas (OUT OF SCOPE)
None — discussion stayed within phase scope.
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| KURS-01 | Förenklade kursmal i "Jag kan..."-format for kurs B, C och D baserade pa Skolverkets betygskriterier | Content authoring strategy section; existing kurs B material analysis |
| KURS-02 | Kursmal uppdelade i fem fardighetsomraden: horforstaelse, lasforstaelse, muntlig interaktion, muntlig produktion, skriftlig fardighet | JSON schema pattern; domain key names |
| KURS-03 | Visuellt stod med ikoner och fargkodning per fardighetsomrade | Design token schema; color palette recommendation; Lucide icon verification |
| KURS-04 | Kursmal lagrade i separata JSON-datafiler (en per kurs) for enkel uppdatering | File structure pattern; one-file-per-course architecture |
| KURS-05 | JSON-schema med stabil mal-ID och kursplan_year-falt for framtida kursplansandringar | ID stability rules; schema versioning pattern |
| KURS-06 | Koppling mellan kursmal och arshjulets teman | Theme key values from årshjul source; many-to-many mapping pattern |
| DESIGN-05 | Enkel svenska anpassad till respektive kursniva | Language calibration strategy; kurs B test; word-frequency guidance |
</phase_requirements>

---

## Summary

Phase 1 delivers the data foundation that all subsequent phases depend on. The work is divided into three tracks: (1) schema design and file structure, (2) content authoring of simplified "Jag kan..." goals, and (3) design token definitions. Of these, content authoring is the highest-risk and highest-effort track — it requires editorial judgment from the teacher and cannot be fully automated.

The JSON schema is fully specified by the locked decisions. The primary planning concern is ensuring goal IDs are stable before any code is written, because localStorage keys in Phase 2 will be keyed directly to these IDs. A curriculum update that renames an ID silently orphans all students' saved checkbox state. ID stability is not a nice-to-have; it is a forward-compatibility requirement.

The existing `Kursmal och checklista for elever.md` file contains partial kurs B source material — specifically the "Min plan" practice checklist items ("Jag ska..."), not the competency goals ("Jag kan..."). The Skolverket criteria text in that file will need to be transformed into concrete, first-person checkable statements. Kurs C and D have no existing simplified material and must be authored from scratch against Skolverket's official betygskriterier.

**Primary recommendation:** Author kurs B content first using the existing material as reference, establish the ID and language-level pattern, then author C and D in the same sitting to guarantee structural consistency.

---

## Standard Stack

This phase produces only data files — no code dependencies are introduced. The stack context is relevant for downstream compatibility only.

### Core Technologies (Phase 1 output consumed by)

| Technology | Version | Purpose | Note |
|------------|---------|---------|------|
| JSON | — | Data format for all three course files and design tokens | No library needed; must be valid JSON (no trailing commas, no comments) |
| Astro 6.x | 6.1.5 | Consumes JSON via `import` at build time (Phase 2) | JSON files must be importable as ES modules — plain JSON only, no JSON5 or JSONC |
| lucide-astro | latest | Renders icons referenced by design-tokens.json | Icon names in design-tokens.json must match lucide-astro export names exactly |

### Files Produced by This Phase

```
src/data/
├── kurs-b.json          # Course B goals — all 5 domains
├── kurs-c.json          # Course C goals — all 5 domains
├── kurs-d.json          # Course D goals — all 5 domains
└── design-tokens.json   # Icon names, hex colors, domain labels
```

**No npm packages are installed in this phase.** Phase 1 is content and schema work only.

---

## Architecture Patterns

### JSON Schema: Per-Course File

Decision D-04 specifies the top-level structure. The full schema is:

```json
{
  "course": "B",
  "kursplan_year": 2018,
  "domains": {
    "horforstaelse": {
      "goals": [
        {
          "id": "B-HORA-01",
          "text": "Jag kan förstå enkla samtal om vanliga ämnen i vardagslivet.",
          "kursplan_year": 2018,
          "themes": ["relationer", "arbete-och-studier"]
        }
      ]
    },
    "lasforstaelse": { "goals": [] },
    "muntlig-interaktion": { "goals": [] },
    "muntlig-produktion": { "goals": [] },
    "skriftlig-fardighet": { "goals": [] }
  }
}
```

[ASSUMED] — Schema based on locked decisions D-01 through D-04; no external source needed.

**Key schema rules:**
- `kursplan_year` appears at BOTH the file root (document-level) and on each goal (goal-level). This allows individual goals to be updated to a new curriculum year without replacing the entire file.
- Domain keys use lowercase Swedish without diacritics and without spaces: `horforstaelse`, `lasforstaelse`, `muntlig-interaktion`, `muntlig-produktion`, `skriftlig-fardighet`. These exact strings will become localStorage key prefixes in Phase 2.
- The `text` field is the displayed "Jag kan..." statement. It must begin with "Jag kan" (not "Du kan", not "Eleven kan").
- `themes` is always an array. Empty array `[]` is valid and means the goal is not theme-tagged.

### ID Stability Rules

[ASSUMED] — Based on localStorage key-stability requirement documented in ARCHITECTURE.md.

Goal IDs (`B-HORA-01`, etc.) must satisfy these constraints:

1. **Immutable once published** — if a goal is revised in text, keep the same ID. Only retire an ID if the competency itself is removed from the curriculum.
2. **Never reuse a retired ID** — if B-HORA-03 is removed in a future curriculum update, the next new goal becomes B-HORA-04, not B-HORA-03.
3. **Sequential within domain** — pad to two digits (`01`, `02`, not `1`, `2`) to keep sort order stable.
4. **Domain abbreviations (locked):**

| Domain | Abbreviation |
|--------|-------------|
| hörförståelse | HORA |
| läsförståelse | LASA |
| muntlig interaktion | MINT |
| muntlig produktion | MPRO |
| skriftlig färdighet | SKRI |

These abbreviations are not specified in the decisions but must be locked now before IDs are assigned. Using the locked D-02 example `B-LASA-01` (not `B-LAS-01`) implies 4-character domain codes. [ASSUMED — recommend confirming HORA/LASA/MINT/MPRO/SKRI with teacher before assigning all IDs.]

### Design Tokens Schema

```json
{
  "domains": {
    "horforstaelse": {
      "label": "Hörförståelse",
      "label_short": "Höra",
      "icon": "Ear",
      "color_hex": "#F97316",
      "color_name": "orange"
    },
    "lasforstaelse": {
      "label": "Läsförståelse",
      "label_short": "Läsa",
      "icon": "BookOpen",
      "color_hex": "#3B82F6",
      "color_name": "blue"
    },
    "muntlig-interaktion": {
      "label": "Muntlig interaktion",
      "label_short": "Prata",
      "icon": "MessageCircle",
      "color_hex": "#22C55E",
      "color_name": "green"
    },
    "muntlig-produktion": {
      "label": "Muntlig produktion",
      "label_short": "Berätta",
      "icon": "Mic",
      "color_hex": "#A855F7",
      "color_name": "purple"
    },
    "skriftlig-fardighet": {
      "label": "Skriftlig färdighet",
      "label_short": "Skriva",
      "icon": "PenLine",
      "color_hex": "#EF4444",
      "color_name": "red"
    }
  }
}
```

[ASSUMED] — Color values are Claude's discretion per locked decisions. See color rationale below.

**Note on `label_short`:** The display label for SFI students should be the plain verb ("Höra", "Läsa", "Prata", "Berätta", "Skriva"), not the Skolverket term ("Hörförståelse"). Both are stored so the component can choose.

### Recommended File Structure (Phase 1 outputs only)

```
src/
└── data/
    ├── kurs-b.json
    ├── kurs-c.json
    ├── kurs-d.json
    └── design-tokens.json
```

No `src/` directory exists yet — this phase creates the `src/data/` directory and all four files.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| JSON schema validation | Custom validator script | JSON Schema spec (optional) or trust Astro import errors | Astro will throw a build error if the JSON is malformed. A JSON Schema file adds formal validation but is optional for this scope. |
| Icon SVGs | Custom-drawn skill area icons | Lucide icon names already locked (D-13) | Ear, BookOpen, MessageCircle, Mic, PenLine are all in lucide-astro. Zero custom SVG work needed. |
| Color palette generation | Custom palette tool | Use the hex values from design-tokens.json directly | Tailwind 4 consumes CSS custom properties; design tokens flow directly to Tailwind via CSS variables in Phase 2. |

---

## Content Authoring Strategy

This section answers the key question for Phase 1: how to write the simplified "Jag kan..." goals.

### Source Material Inventory

| File | Content | Status for Phase 1 |
|------|---------|-------------------|
| `Kursmal och checklista for elever.md` | Kurs B: Skolverket criteria text (raw) + "Jag ska..." practice checklist items | Use criteria text as source; the "Jag ska..." items are Phase 3 scope |
| `Forvantansdokumentet.md` | Student expectations — language register and tone reference | Use as tone reference; confirms simple imperative Swedish |
| `Arshjul for sfi 2 kurs B, C och D .md` | 7 yearly themes with subtopics | Use to assign `themes` array values to goals |

### What the Existing Kurs B Material Contains

The existing file contains Skolverket's official criteria in third person ("Eleven läser och förstår...") followed by simplified "Du kan..." bullet points for reading and listening. It does NOT contain:
- "Jag kan..." format (file uses "Du kan..." — must be converted to first person)
- Complete coverage of all five skill domains (file shows reading and listening; muntlig interaktion, muntlig produktion, and skriftlig fardighet criteria appear only in official form)
- Any content for kurs C or kurs D

### Authoring Rules for Goal Text

[CITED: Förväntansdokumentet.md — establishes the plain Swedish register the teacher uses with students]

1. **First person singular:** "Jag kan..." — never "Du kan...", never "Eleven kan..."
2. **Concrete and checkable:** The student must be able to answer yes/no. "Jag kan förstå enkla samtal" is checkable. "Jag kan kommunicera" is not.
3. **One competency per statement:** No compound goals with "och" linking two different abilities.
4. **Vocabulary calibration:**
   - Kurs B: CEFR A2 word frequency; avoid abstractions; use cognates where possible; max one clause per sentence.
   - Kurs C: CEFR B1 vocabulary allowed; some subordinate clauses acceptable.
   - Kurs D: CEFR B2 vocabulary allowed; more nuanced distinctions between similar competencies.
5. **No Skolverket jargon in student-facing text:** Replace "interaktion" with "samtal", replace "produktion" with "berätta eller presentera", replace "reception" with "förstå".
6. **Avoid negative constructions:** "Jag kan förstå enkla frågor" not "Jag kan inte förstå svåra frågor".

### Minimum Goal Count per Domain

[ASSUMED] — Based on existing material pattern analysis and checklist usability.

Each domain should have 4-8 goals per course. Fewer than 4 makes the checklist feel empty; more than 8 creates cognitive overload on mobile. The existing kurs B material for reading ("Läsa") has 5 bullet points — use this as the calibration target.

Across 5 domains × 3 courses = 15 domain/course combinations. At 5 goals each = 75 total "Jag kan..." statements to author.

### Five Skill Domains: Authoring Notes

The existing material sometimes merges "muntligt" into a single category. The JSON must keep all five separate per Skolverket's structure (per locked decision noted in CONTEXT.md specifics):

| Domain key | Skolverket label | Plain label for students | What it covers |
|-----------|-----------------|-------------------------|---------------|
| `horforstaelse` | Hörförståelse | Höra | Listening comprehension — understanding spoken Swedish in everyday situations |
| `lasforstaelse` | Läsförståelse | Läsa | Reading comprehension — understanding written Swedish texts |
| `muntlig-interaktion` | Muntlig interaktion | Prata | Two-way conversation — asking and answering, maintaining dialogue |
| `muntlig-produktion` | Muntlig produktion | Berätta | One-way speaking — presenting, narrating, describing without real-time exchange |
| `skriftlig-fardighet` | Skriftlig färdighet | Skriva | Writing — producing written texts for communication |

The distinction between muntlig interaktion and muntlig produktion is the hardest for students to understand. Pair each with a very concrete example in the first goal: interaktion = "Jag kan svara på frågor i ett samtal", produktion = "Jag kan berätta om min dag för klassen".

### Theme Mapping Strategy

The 7 årshjul themes from the source file are:
- `relationer` (familj, vänskap)
- `miljo` (klimat och hållbarhet)
- `bostad`
- `arbete-och-studier` (studieteknik)
- `fritid-och-halsa` (geografi och resa, friskvård/sjukvård, kulturaktiviteter)
- `hogtider` (kultur och traditioner)
- `samhalle` (demokrati, brott och straff, yttrandefrihet, religionsfrihet, ekonomi)

[VERIFIED: Årshjul för sfi 2 kurs B, C och D .md — theme names and subtopics confirmed from source file]

Most listening and reading goals can be tagged to multiple themes. Most grammar-level writing goals (e.g., "Jag kan skriva korta meningar") are theme-generic and get `"themes": []`.

Assign themes conservatively — only tag a goal if that theme genuinely provides a context in which the goal would be practiced. Do not tag every goal to every theme.

---

## Color Palette Recommendation

This is Claude's discretion per locked decisions. The palette must be:
- High-contrast against white backgrounds (WCAG AA minimum: 4.5:1 for text, 3:1 for UI components)
- Colorblind-safe (distinguishable under deuteranopia and protanopia — the two most common forms)
- Warm and inviting, consistent with the tree illustration aesthetic described in CLAUDE.md

[ASSUMED] — Color values selected based on training knowledge of WCAG contrast ratios and colorblind-safe palettes. Should be verified with a contrast checker before final commit.

### Recommended Palette

| Domain | Hex | Color | Contrast on white | Colorblind safe |
|--------|-----|-------|------------------|-----------------|
| hörförståelse | `#D97706` | Amber/orange | 4.7:1 (AA pass) | Distinguishable as yellow-orange under deuteranopia |
| läsförståelse | `#2563EB` | Blue | 5.9:1 (AA pass) | High contrast; appears darker under all CVD types |
| muntlig interaktion | `#16A34A` | Green | 4.5:1 (AA borderline) | Appears as yellow-brown under deuteranopia — **verify** |
| muntlig produktion | `#7C3AED` | Violet/purple | 6.2:1 (AA pass) | Appears as blue-gray under deuteranopia — acceptable |
| skriftlig färdighet | `#DC2626` | Red | 4.5:1 (AA borderline) | Appears as brown/olive under deuteranopia — **verify** |

**Warning:** Green and red together are problematic for deuteranopia (red-green color blindness). Muntlig interaktion (green) and skriftlig färdighet (red) will be indistinguishable for approximately 8% of users if color is the only differentiator. This is mitigated by:
1. Each domain also has a distinct icon (Lucide icons locked in D-13)
2. Each domain has a text label (never color alone per REQUIREMENTS DESIGN-04)

[ASSUMED] — Exact contrast ratios estimated from training knowledge. Verify with https://webaim.org/resources/contrastchecker/ before finalizing.

**Simpler alternative if palette is flagged:** Use Tailwind 4's built-in color tokens (amber-600, blue-600, teal-600, violet-600, rose-600) which have been designed as a harmonious, accessible palette. [ASSUMED]

---

## Common Pitfalls

### Pitfall 1: Goal IDs Assigned Ad Hoc
**What goes wrong:** IDs are assigned as goals are written, then renumbered during editing. Phase 2 localStorage keys break for any user who tested Phase 1 data.
**Why it happens:** Content authoring feels separate from schema design, so IDs are treated as metadata to fill in later.
**How to avoid:** Assign IDs before writing goal text. Create the shell structure with numbered ID slots, then fill in text.
**Warning signs:** Any goal with `"id": "TBD"` or sequential gaps (`HORA-01`, `HORA-03` with no `HORA-02`).

### Pitfall 2: "Jag ska..." Mixed Into "Jag kan..." Goals
**What goes wrong:** The existing kurs B material contains both "Jag kan..." (competency = Phase 1) and "Jag ska..." (practice plan = Phase 3) items. If "Jag ska..." items are included in the Phase 1 JSON, Phase 2 will render practice plans as competency checklist items.
**Why it happens:** Both formats appear in the same source document, making them easy to conflate.
**How to avoid:** Filter strictly: include only statements about achieved ability ("Jag kan X"), not practice intent ("Jag ska X varje vecka").
**Warning signs:** Any goal text containing "ska", "varje dag", "varje vecka", or "träna".

### Pitfall 3: Domain Key Mismatch Between JSON Files and Design Tokens
**What goes wrong:** `kurs-b.json` uses `"muntlig_interaktion"` (underscore) but `design-tokens.json` uses `"muntlig-interaktion"` (hyphen). Phase 2 component cannot join the data.
**Why it happens:** JSON keys are typed manually per file without a shared reference.
**How to avoid:** The domain keys are the canonical join key between all files. Write them once in this research document and copy-paste, never retype.
**Canonical domain keys (use exactly):** `horforstaelse`, `lasforstaelse`, `muntlig-interaktion`, `muntlig-produktion`, `skriftlig-fardighet`
**Warning signs:** Any underscore in a domain key name. Any diacritic (ä, ö) in a domain key name.

### Pitfall 4: Themes Array Values Not Matching Årshjul Exactly
**What goes wrong:** A goal has `"themes": ["arbete_och_studier"]` but the canonical value is `"arbete-och-studier"`. Phase 2 theme-filter feature silently returns zero results for that theme.
**Why it happens:** Theme strings are typed by feel, not copied from a reference.
**How to avoid:** The 7 theme values are locked (D-10). Copy from this list only:
`relationer`, `miljo`, `bostad`, `arbete-och-studier`, `fritid-och-halsa`, `hogtider`, `samhalle`
**Warning signs:** Any theme string containing underscores, spaces, Swedish diacritics (miljö → miljo is intentional), or a string not in the list of 7.

### Pitfall 5: kursplan_year Value Not Verified
**What goes wrong:** `kursplan_year` is set to 2018 (an estimate) but the actual Skolverket kursplan in use is a different year. When Skolverket releases new plans in late 2026, the teacher cannot tell whether the JSON was already updated.
**Why it happens:** The year is treated as a cosmetic field.
**How to avoid:** Look up the actual year of the Skolverket kursplan in effect for SFI spår 2. [ASSUMED — 2018 is plausible but should be confirmed by the teacher against the current Skolverket document they use.]

---

## Code Examples

### Complete Goal Object (correct format)

```json
{
  "id": "B-HORA-01",
  "text": "Jag kan förstå enkla samtal om vanliga ämnen i vardagslivet.",
  "kursplan_year": 2018,
  "themes": ["relationer", "arbete-och-studier"]
}
```

### Goal Object: Generic Language Skill (no themes)

```json
{
  "id": "B-SKRI-01",
  "text": "Jag kan skriva korta och enkla meningar.",
  "kursplan_year": 2018,
  "themes": []
}
```

### Complete kurs-b.json Skeleton (fill in goal text)

```json
{
  "course": "B",
  "kursplan_year": 2018,
  "domains": {
    "horforstaelse": {
      "goals": [
        { "id": "B-HORA-01", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-HORA-02", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-HORA-03", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-HORA-04", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-HORA-05", "text": "...", "kursplan_year": 2018, "themes": [] }
      ]
    },
    "lasforstaelse": {
      "goals": [
        { "id": "B-LASA-01", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-LASA-02", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-LASA-03", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-LASA-04", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-LASA-05", "text": "...", "kursplan_year": 2018, "themes": [] }
      ]
    },
    "muntlig-interaktion": {
      "goals": [
        { "id": "B-MINT-01", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-MINT-02", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-MINT-03", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-MINT-04", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-MINT-05", "text": "...", "kursplan_year": 2018, "themes": [] }
      ]
    },
    "muntlig-produktion": {
      "goals": [
        { "id": "B-MPRO-01", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-MPRO-02", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-MPRO-03", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-MPRO-04", "text": "...", "kursplan_year": 2018, "themes": [] }
      ]
    },
    "skriftlig-fardighet": {
      "goals": [
        { "id": "B-SKRI-01", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-SKRI-02", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-SKRI-03", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-SKRI-04", "text": "...", "kursplan_year": 2018, "themes": [] },
        { "id": "B-SKRI-05", "text": "...", "kursplan_year": 2018, "themes": [] }
      ]
    }
  }
}
```

### design-tokens.json (complete file)

```json
{
  "domains": {
    "horforstaelse": {
      "label": "Hörförståelse",
      "label_short": "Höra",
      "icon": "Ear",
      "color_hex": "#D97706",
      "color_name": "amber"
    },
    "lasforstaelse": {
      "label": "Läsförståelse",
      "label_short": "Läsa",
      "icon": "BookOpen",
      "color_hex": "#2563EB",
      "color_name": "blue"
    },
    "muntlig-interaktion": {
      "label": "Muntlig interaktion",
      "label_short": "Prata",
      "icon": "MessageCircle",
      "color_hex": "#16A34A",
      "color_name": "green"
    },
    "muntlig-produktion": {
      "label": "Muntlig produktion",
      "label_short": "Berätta",
      "icon": "Mic",
      "color_hex": "#7C3AED",
      "color_name": "violet"
    },
    "skriftlig-fardighet": {
      "label": "Skriftlig färdighet",
      "label_short": "Skriva",
      "icon": "PenLine",
      "color_hex": "#DC2626",
      "color_name": "red"
    }
  }
}
```

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Domain abbreviations HORA/LASA/MINT/MPRO/SKRI are used in ID format | ID Stability Rules | IDs assigned with wrong abbreviations must be renamed before Phase 2 begins |
| A2 | kursplan_year 2018 is the correct year for the current Skolverket SFI kursplan | Content Authoring Strategy / Code Examples | Misleading provenance; teachers using this to track curriculum versions will see wrong year |
| A3 | Color hex values in design-tokens.json meet WCAG AA 4.5:1 contrast | Color Palette Recommendation | Accessibility failure; potential WCAG non-compliance |
| A4 | Green (#16A34A) and red (#DC2626) are sufficiently distinguishable under deuteranopia given that icons also differentiate domains | Color Palette Recommendation | 8% of male users cannot distinguish these domains by color; icons must carry the full differentiating load |
| A5 | 4-8 goals per domain is the right range for usability | Content Authoring Strategy | Too few = feels incomplete; too many = cognitive overload on mobile |
| A6 | `label_short` plain verbs (Höra/Läsa/Prata/Berätta/Skriva) are appropriate student-facing labels | Design Tokens Schema | "Berätta" may not be the most intuitive label for muntlig produktion — teacher should review |

---

## Open Questions

1. **Domain abbreviation confirmation (A1)**
   - What we know: D-02 specifies format `{COURSE}-{DOMAIN}-{NN}` with example `B-LASA-01`
   - What's unclear: Whether the other four abbreviations (HORA/MINT/MPRO/SKRI) are teacher-preferred or Claude's choice
   - Recommendation: Confirm with teacher before authoring any IDs. Once goals are authored and IDs committed, changing abbreviations is a breaking change.

2. **Correct kursplan_year value (A2)**
   - What we know: Field exists to track curriculum provenance
   - What's unclear: Whether the Skolverket kursplan currently in effect for SFI spår 2 was issued in 2018 or another year
   - Recommendation: Teacher checks the Skolverket kursplan document header. Use that year. If unsure, use `null` rather than an incorrect value.

3. **Number of goals per domain**
   - What we know: Existing kurs B reading material has ~5 items
   - What's unclear: Whether the teacher wants a comprehensive list (8+ goals) or a focused short list (4-5)
   - Recommendation: Start with 5 per domain for kurs B, review with teacher, then scale C and D accordingly.

---

## Environment Availability

Step 2.6: SKIPPED — Phase 1 produces only JSON data files. No external tools, CLI utilities, runtimes, or services are required. Files can be created with any text editor.

---

## Project Constraints (from CLAUDE.md)

Directives that apply to Phase 1 specifically:

| Directive | Application to Phase 1 |
|-----------|----------------------|
| No backend, no server, no database | JSON files are static — no backend access pattern needed |
| Kursmal i separata JSON-datafiler med stabil mal-ID och kursplan_year | Directly implemented in this phase |
| JSON-schema maste vara stabilt innan localStorage-kod skrivs | Phase 1 must be complete and IDs locked before Phase 2 begins |
| Innehallet ar det hogsta riskarbetet — blockerar allt UI | Content authoring is the primary deliverable; schema scaffolding is secondary |
| No TypeScript strict mode for data files | JSON files only — no TypeScript involved in this phase |
| No analytics or tracking scripts | Not relevant to Phase 1 |
| Mobile-first (375px viewport minimum) | Not directly applicable to Phase 1; design token colors/icons flow into mobile layout in Phase 2 |
| Ikoner alltid parade med textbeskrivning | Enforced in design-tokens.json by including both `label` and `label_short` alongside every icon name |

---

## Sources

### Primary (HIGH confidence)
- `Kursmal och checklista for elever.md` (project source file) — kurs B criteria text and simplified statements
- `Arshjul for sfi 2 kurs B, C och D .md` (project source file) — 7 theme names and subtopics (verified exact strings)
- `Forvantansdokumentet.md` (project source file) — tone and language register reference
- `.planning/phases/01-innehallsgrund/01-CONTEXT.md` — all locked decisions (D-01 through D-14)
- `.planning/REQUIREMENTS.md` — KURS-01 through KURS-06 and DESIGN-05 requirements
- `.planning/research/ARCHITECTURE.md` — ID stability rules and localStorage key design
- `.planning/research/PITFALLS.md` — Pitfall 1 (content in HTML), Pitfall 3 (language level), Pitfall 9 (color-only differentiation)

### Secondary (MEDIUM confidence)
- ARCHITECTURE.md: JSON schema shape and domain key naming conventions (project research, internally consistent)
- PITFALLS.md: Skolverket curriculum risk timing (cited Skolverket sources, MEDIUM because timing is external)

### Tertiary (LOW confidence — marked [ASSUMED] in document)
- Color hex values and WCAG contrast estimates — training knowledge, verify with webaim.org before finalizing
- kursplan_year value 2018 — training knowledge, must be confirmed against actual Skolverket document

---

## Metadata

**Confidence breakdown:**
- JSON schema: HIGH — all decisions locked by CONTEXT.md; schema shape confirmed against ARCHITECTURE.md
- Domain key naming: HIGH — locked decisions plus consistency requirement with localStorage keys
- Content authoring strategy: HIGH — sourced from existing project materials
- Color palette: MEDIUM — Claude's discretion; exact contrast ratios unverified
- kursplan_year value: LOW — assumed; must be confirmed by teacher

**Research date:** 2026-04-10
**Valid until:** 2026-05-10 (stable domain; main volatility is Skolverket curriculum timeline, which is external)
