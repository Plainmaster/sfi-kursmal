---
phase: 01-innehallsgrund
reviewed: 2026-04-10T00:00:00Z
depth: standard
files_reviewed: 4
files_reviewed_list:
  - src/data/design-tokens.json
  - src/data/kurs-b.json
  - src/data/kurs-c.json
  - src/data/kurs-d.json
findings:
  critical: 0
  warning: 1
  info: 1
  total: 2
status: issues_found
---

# Phase 1: Code Review Report

**Reviewed:** 2026-04-10
**Depth:** standard
**Files Reviewed:** 4
**Status:** issues_found

## Summary

Reviewed four JSON data files that form the content foundation for the SFI course goals application: one design-tokens file defining domain metadata (colors, icons, labels) and three course-goal files (B, C, D). The data is well-structured with consistent ID conventions and matching domain keys across all files. Two minor issues found -- one encoding inconsistency and one missing data field pattern.

## Warnings

### WR-01: Inconsistent Unicode encoding between course files

**File:** `src/data/kurs-b.json:1-170`
**Issue:** `kurs-b.json` uses JSON Unicode escape sequences for Swedish characters (e.g., `\u00f6` for "o with diaeresis", `\u00e4` for "a with diaeresis"), while `kurs-c.json` and `kurs-d.json` use literal UTF-8 characters (e.g., `forstaa` appears as `f\u00f6rst\u00e5` in B but as `forsta` with proper glyphs in C and D). While both are valid JSON and parse identically, this inconsistency suggests the files were authored with different tools or settings. If a teacher or content editor maintains these files manually (as stated in CLAUDE.md), the escaped form in kurs-b.json is significantly harder to read and edit.
**Fix:** Re-save `kurs-b.json` with a UTF-8 aware editor or run it through a formatter that outputs literal UTF-8 characters, matching the style of `kurs-c.json` and `kurs-d.json`. For example:
```bash
node -e "const fs=require('fs'); const d=JSON.parse(fs.readFileSync('src/data/kurs-b.json','utf8')); fs.writeFileSync('src/data/kurs-b.json', JSON.stringify(d,null,2)+'\n')"
```

## Info

### IN-01: Goal count varies across courses in muntlig-produktion

**File:** `src/data/kurs-b.json:107-133` / `src/data/kurs-c.json:107-139` / `src/data/kurs-d.json:107-133`
**Issue:** The `muntlig-produktion` domain has 4 goals in courses B and D but 5 goals in course C, while all other domains consistently have 5 goals across all three courses. This is likely intentional (reflecting actual curriculum differences), but worth confirming to rule out a missing goal in B or D.
**Fix:** No code change needed if intentional. Verify against Skolverket's official course goals that 4 items is correct for muntlig-produktion in courses B and D.

---

_Reviewed: 2026-04-10_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
