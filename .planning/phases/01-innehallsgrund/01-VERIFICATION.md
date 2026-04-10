---
phase: 01-innehallsgrund
verified: 2026-04-10T19:15:00Z
status: human_needed
score: 12/13 must-haves verified
overrides_applied: 0
human_verification:
  - test: "Read kurs B goal texts and confirm language is at CEFR A2 level (simple, concrete, no abstractions)"
    expected: "All 24 goals use vocabulary and sentence structures appropriate for SFI kurs B beginners"
    why_human: "Language level calibration requires native/teacher judgment -- automated tools cannot assess whether Swedish text is appropriately simplified for A2 learners"
  - test: "Read kurs C goal texts and confirm language is at CEFR B1 level (broader topics, some subordinate clauses)"
    expected: "25 goals are noticeably more complex than kurs B but still accessible to intermediate learners"
    why_human: "CEFR level distinction between B and C requires pedagogical judgment"
  - test: "Read kurs D goal texts and confirm language is at CEFR B2 level (argumentation, formal register)"
    expected: "24 goals reflect advanced competencies (structured presentations, formal writing, source comparison)"
    why_human: "CEFR B2 calibration requires teacher confirmation that goals match actual D-level student abilities"
  - test: "Confirm kursplan_year 2018 matches the Skolverket kursplan currently in use for SFI spar 2"
    expected: "Teacher confirms 2018 is correct, or provides the actual year"
    why_human: "External curriculum document verification -- cannot be checked programmatically"
---

# Phase 1: Innehallsgrund Verification Report

**Phase Goal:** Allt kursinnehall finns i stabila JSON-datafiler som lararen kan uppdatera utan att andra koden
**Verified:** 2026-04-10T19:15:00Z
**Status:** human_needed
**Re-verification:** No -- initial verification

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | JSON files for kurs B, C, D contain simplified "Jag kan..." goals for all 5 skill domains | VERIFIED | kurs-b.json: 24 goals, kurs-c.json: 25 goals, kurs-d.json: 24 goals. All goals start with "Jag kan". All 5 domains populated in each file. |
| 2 | Every goal has a stable ID and kursplan_year field | VERIFIED | All 73 IDs match pattern `[BCD]-(HORA\|LASA\|MINT\|MPRO\|SKRI)-\d{2}`. All have `kursplan_year: 2018`. IDs are sequential with no gaps. |
| 3 | Every skill domain has a defined icon and color code | VERIFIED | design-tokens.json contains all 5 domains with icon (Ear, BookOpen, MessageCircle, Mic, PenLine), color_hex, color_name, label, and label_short. |
| 4 | Course goals written in simple Swedish adapted to course level (B, C, D) | ? UNCERTAIN | Goal text uses Swedish diacritics correctly. No "ska" items found. No Skolverket jargon detected. However, CEFR level calibration (A2/B1/B2) requires teacher judgment. |
| 5 | Theme-to-goal mapping uses the 7 canonical arshjul strings | VERIFIED | All theme values validated against canonical set. No diacritics or underscores in theme strings. Conservative assignment (many goals have empty themes array). |
| 6 | design-tokens.json contains all 5 skill domains with icon, color, and label | VERIFIED | 5 domains, each with label, label_short, icon, color_hex, color_name. No missing fields. |
| 7 | kurs-b.json contains "Jag kan..." goals for all 5 skill domains | VERIFIED | 5+5+5+4+5 = 24 goals across all domains. |
| 8 | Every goal has a stable ID in format B-XXXX-NN | VERIFIED | Regex `^B-(HORA\|LASA\|MINT\|MPRO\|SKRI)-\d{2}$` matches all 24 kurs B IDs. |
| 9 | Theme values use only the 7 canonical arshjul strings | VERIFIED | Same as Truth 5 -- validated across all 73 goals. |
| 10 | kurs-c.json contains "Jag kan..." goals for all 5 domains at CEFR B1 level | VERIFIED (structure) | 25 goals, all "Jag kan..." prefix, valid IDs (C-XXXX-NN). Language level needs human check. |
| 11 | kurs-d.json contains "Jag kan..." goals for all 5 domains at CEFR B2 level | VERIFIED (structure) | 24 goals, all "Jag kan..." prefix, valid IDs (D-XXXX-NN). Language level needs human check. |
| 12 | Domain keys in kurs-c.json and kurs-d.json match kurs-b.json exactly | VERIFIED | `JSON.stringify(Object.keys())` identical across all 4 JSON files. |
| 13 | Goal complexity increases from B to C to D while structure stays identical | ? UNCERTAIN | Structure is identical (confirmed). Complexity increase visible in text (B uses "enkla/korta", C uses "aktuella amnen/sammanhangande", D uses "argumentera/formellt"). Requires teacher confirmation. |

**Score:** 12/13 truths verified (1 uncertain -- requires human judgment on language level)

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `src/data/design-tokens.json` | Icon, color, and label mappings for 5 skill domains | VERIFIED | 40 lines, valid JSON, contains "horforstaelse" and all 4 other domains. 5 fields per domain. |
| `src/data/kurs-b.json` | Course B simplified goals across all 5 domains | VERIFIED | 171 lines, valid JSON, contains "Jag kan", 24 goals, course "B", kursplan_year 2018. |
| `src/data/kurs-c.json` | Course C simplified goals across all 5 domains | VERIFIED | 177 lines, valid JSON, contains "Jag kan", 25 goals, course "C", kursplan_year 2018. |
| `src/data/kurs-d.json` | Course D simplified goals across all 5 domains | VERIFIED | 171 lines, valid JSON, contains "Jag kan", 24 goals, course "D", kursplan_year 2018. |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| src/data/kurs-b.json | src/data/design-tokens.json | Matching domain keys | WIRED | Domain keys identical: horforstaelse, lasforstaelse, muntlig-interaktion, muntlig-produktion, skriftlig-fardighet |
| src/data/kurs-c.json | src/data/design-tokens.json | Matching domain keys | WIRED | Domain keys identical across all files |
| src/data/kurs-d.json | src/data/design-tokens.json | Matching domain keys | WIRED | Domain keys identical across all files |

### Data-Flow Trace (Level 4)

Not applicable -- Phase 1 produces data files only. No rendering components exist yet. Data flow will be verified when Phase 2 creates components that consume these files.

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|----------|---------|--------|--------|
| All JSON files are valid and importable | `node -e "require('./src/data/kurs-b.json'); require('./src/data/kurs-c.json'); require('./src/data/kurs-d.json'); require('./src/data/design-tokens.json'); console.log('OK')"` | OK | PASS |
| Domain keys match across all 4 files | Cross-file key comparison | All 4 files have identical domain key arrays | PASS |
| All 73 goals have valid IDs | Regex `^[BCD]-(HORA\|LASA\|MINT\|MPRO\|SKRI)-\d{2}$` | 73/73 match | PASS |
| No "ska" items in goal text | grep for " ska " | 0 matches | PASS |
| All themes from canonical set | Validation against 7-string array | 0 invalid themes | PASS |
| Goal count per domain is 4-8 | Count check | All 15 domain/course combos have 4-5 goals | PASS |
| Total goals in target range 60-120 | Sum | 73 total | PASS |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|------------|-------------|--------|----------|
| KURS-01 | 01-01, 01-02 | Forenklade kursmal i "Jag kan..."-format for B, C, D | SATISFIED | 73 goals all starting with "Jag kan" across 3 courses |
| KURS-02 | 01-01, 01-02 | Kursmal uppdelade i fem fardighetsomraden | SATISFIED | All files have 5 domains: horforstaelse, lasforstaelse, muntlig-interaktion, muntlig-produktion, skriftlig-fardighet |
| KURS-03 | 01-01 | Visuellt stod med ikoner och fargkodning per fardighetsomrade | SATISFIED | design-tokens.json has icon and color_hex for each domain |
| KURS-04 | 01-01, 01-02 | Kursmal lagrade i separata JSON-datafiler (en per kurs) | SATISFIED | Three separate files: kurs-b.json, kurs-c.json, kurs-d.json |
| KURS-05 | 01-01, 01-02 | JSON-schema med stabil mal-ID och kursplan_year-falt | SATISFIED | All goals have stable IDs (B/C/D-XXXX-NN format) and kursplan_year: 2018 |
| KURS-06 | 01-01, 01-02 | Koppling mellan kursmal och arshjulets teman | SATISFIED | themes array on every goal; values from canonical 7-theme set |
| DESIGN-05 | 01-01, 01-02 | Enkel svenska anpassad till respektive kursniva | NEEDS HUMAN | Text appears appropriately leveled but requires teacher confirmation of CEFR calibration |

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| (none) | - | - | - | No anti-patterns detected in any data file |

### Human Verification Required

### 1. CEFR Language Level Calibration (Kurs B = A2)

**Test:** Read through all 24 kurs B goals in `src/data/kurs-b.json` and confirm the vocabulary and sentence structures are appropriate for CEFR A2 / SFI kurs B students.
**Expected:** Simple, concrete statements using everyday vocabulary. No abstractions, no subordinate clauses, max one clause per sentence.
**Why human:** Automated tools cannot assess whether Swedish text is appropriately simplified for A2 learners. This requires native speaker / teacher judgment.

### 2. CEFR Language Level Calibration (Kurs C = B1)

**Test:** Read through all 25 kurs C goals in `src/data/kurs-c.json` and confirm they are noticeably more complex than kurs B but still accessible.
**Expected:** Broader topics (news, workplace, society), some subordinate clauses, opinion expression with reasoning.
**Why human:** CEFR B1 calibration requires pedagogical judgment about what intermediate SFI students can actually understand.

### 3. CEFR Language Level Calibration (Kurs D = B2)

**Test:** Read through all 24 kurs D goals in `src/data/kurs-d.json` and confirm they reflect advanced competencies.
**Expected:** Argumentation, formal register, structured presentations, source comparison, formal writing.
**Why human:** CEFR B2 calibration requires teacher confirmation that goals match actual D-level student abilities.

### 4. kursplan_year Confirmation

**Test:** Check the Skolverket kursplan document currently in use for SFI spar 2 and confirm the year is 2018.
**Expected:** Teacher confirms 2018 is correct, or provides the actual year for correction.
**Why human:** External curriculum document verification cannot be done programmatically.

### Gaps Summary

No structural or technical gaps found. All 4 JSON files exist, are valid, have correct schema, matching domain keys, valid IDs, valid themes, and appropriate goal counts.

The only outstanding item is human verification of linguistic quality -- specifically, whether the "Jag kan..." goal texts are calibrated to the correct CEFR level for each course and whether kursplan_year 2018 is accurate. These are content quality judgments that require teacher expertise.

---

_Verified: 2026-04-10T19:15:00Z_
_Verifier: Claude (gsd-verifier)_
