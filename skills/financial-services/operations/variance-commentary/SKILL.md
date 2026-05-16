---
name: variance-commentary
description: Use when financial-services work requires write flux commentary for every
  P&L and balance-sheet line over threshold — current vs prior period and vs budget,
  with the driver explained from underlying activity. Use for the month-end close
  package and management reporting..
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
    - financial-services
    - fund-admin
    - operations
    related_skills: []
---

# Variance commentary

Given current-period actuals, prior-period actuals, and budget for the same scope, produce a commentary table.

## Threshold

Flag a line for commentary if **either** is true:

- Absolute variance ≥ the firm's materiality threshold (use the provided value; default 5% of the line or a fixed floor, whichever is greater)
- The line is on the "always comment" list (revenue, headcount cost, cash)

## For each flagged line

| Column | Content |
|---|---|
| **Line** | Account or caption |
| **Current / Prior / Budget** | The three values |
| **Δ vs prior** and **Δ vs budget** | Amount and % |
| **Driver** | One sentence explaining the movement from underlying activity — not a restatement of the number |

A driver explains *why*, not *what*: "Cloud spend up $1.2M on incremental GPU reservations for the May launch" — not "Cloud spend increased $1.2M (18%)."

## Sourcing the driver

Look at the activity behind the line (journal-source breakdown, vendor mix, headcount delta, volume × rate) via the internal-gl MCP. If the driver isn't clear from the data, write "driver unclear — flag for controller" rather than inventing one.

## Output

The commentary table plus a short narrative (3–5 sentences) summarizing the period's biggest movers.

## Hermes Profile Notes
This skill was packaged from `pi-financial-services` source path `plugins/vertical-plugins/fund-admin/skills/variance-commentary` for the Hermes financial-services profile. Use institutional data connectors first when available, cite sources, and stage outputs for qualified human review.


## Common Pitfalls
1. Do not present drafts as investment, legal, tax, or accounting advice.
2. Do not use web search as the primary source when an institutional MCP/data connector is available.
3. Do not execute transactions, contact clients, post to a ledger, or approve onboarding. Stage outputs for review.


## Verification Checklist
- [ ] Inputs, assumptions, dates, and currencies are explicit.
- [ ] Numbers tie across tables, models, decks, and memos.
- [ ] Sources are cited and institutional data is preferred where available.
- [ ] Output is labeled draft / for human review where appropriate.
