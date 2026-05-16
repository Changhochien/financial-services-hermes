---
name: clean-data-xls
description: Use when financial-services work requires clean up messy spreadsheet
  data — trim whitespace, fix inconsistent casing, convert numbers-stored-as-text,
  standardize dates, remove duplicates, and flag mixed-type columns. Use when data
  is messy, inconsistent, or needs prep before analysis. Triggers on "clean this data",
  "clean up this sheet", "normalize this data", "fix formatting", "dedupe", "standardize
  this column", "this data is messy"..
version: 0.1.0
author: Changhochien
license: MIT
platforms:
- linux
- macos
- windows
metadata:
  hermes:
    tags:
    - financial-analysis
    - financial-services
    - modeling
    related_skills: []
---

# Clean Data

Clean messy data in the active sheet or a specified range.

## Environment

- **If running inside Excel (Office Add-in / Office JS):** Use Office JS directly (`Excel.run(async (context) => {...})`). Read via `range.values`, write helper-column formulas via `range.formulas = [["=TRIM(A2)"]]`. The in-place vs helper-column decision still applies.
- **If operating on a standalone .xlsx file:** Use Python/openpyxl.

## Workflow

### Step 1: Scope

- If a range is given (e.g. `A1:F200`), use it
- Otherwise use the full used range of the active sheet
- Profile each column: detect its dominant type (text / number / date) and identify outliers

### Step 2: Detect issues

| Issue | What to look for |
|---|---|
| Whitespace | leading/trailing spaces, double spaces |
| Casing | inconsistent casing in categorical columns (`usa` / `USA` / `Usa`) |
| Number-as-text | numeric values stored as text; stray `$`, `,`, `%` in number cells |
| Dates | mixed formats in the same column (`3/8/26`, `2026-03-08`, `March 8 2026`) |
| Duplicates | exact-duplicate rows and near-duplicates (case/whitespace differences) |
| Blanks | empty cells in otherwise-populated columns |
| Mixed types | a column that's 98% numbers but has 3 text entries |
| Encoding | mojibake (`Ã©`, `â€™`), non-printing characters |
| Errors | `#REF!`, `#N/A`, `#VALUE!`, `#DIV/0!` |

### Step 3: Propose fixes

Show a summary table before changing anything:

| Column | Issue | Count | Proposed Fix |
|---|---|---|---|

### Step 4: Apply

- **Prefer formulas over hardcoded cleaned values** — where the cleaned output can be expressed as a formula (e.g. `=TRIM(A2)`, `=VALUE(SUBSTITUTE(B2,"$",""))`, `=UPPER(C2)`, `=DATEVALUE(D2)`), write the formula in an adjacent helper column rather than computing the result in Python and overwriting the original. This keeps the transformation transparent and auditable.
- Only overwrite in place with computed values when the user explicitly asks for it, or when no sensible formula equivalent exists (e.g. encoding/mojibake repair)
- For destructive operations (removing duplicates, filling blanks, overwriting originals), confirm with the user first
- After each category of fix (whitespace → casing → number conversion → dates → dedup), show the user a sample of what changed and get confirmation before moving to the next category
- Report a before/after summary of what changed

## Hermes Profile Notes
This skill was packaged from `pi-financial-services` source path `plugins/vertical-plugins/financial-analysis/skills/clean-data-xls` for the Hermes financial-services profile. Use institutional data connectors first when available, cite sources, and stage outputs for qualified human review.


## Common Pitfalls
1. Do not present drafts as investment, legal, tax, or accounting advice.
2. Do not use web search as the primary source when an institutional MCP/data connector is available.
3. Do not execute transactions, contact clients, post to a ledger, or approve onboarding. Stage outputs for review.


## Verification Checklist
- [ ] Inputs, assumptions, dates, and currencies are explicit.
- [ ] Numbers tie across tables, models, decks, and memos.
- [ ] Sources are cited and institutional data is preferred where available.
- [ ] Output is labeled draft / for human review where appropriate.
