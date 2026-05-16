---
name: client-review
description: Use when financial-services work requires client Review Prep.
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
    - wealth-management
    related_skills: []
---

# Client Review Prep

description: Prepare for client review meetings with portfolio performance summary, allocation analysis, talking points, and action items. Pulls together account data into a concise meeting-ready format. Use before quarterly reviews, annual checkups, or ad-hoc client meetings. Triggers on "client review", "meeting prep for [client]", "quarterly review", "prep for [client name]", or "client meeting".

## Workflow

### Step 1: Client Context

Gather or look up:
- **Client name** and household members
- **Account types**: Taxable, IRA, Roth, 401(k), trust, etc.
- **Total AUM** across accounts
- **Investment Policy Statement (IPS)**: Target allocation, risk tolerance, constraints
- **Life stage**: Accumulation, pre-retirement, retirement, legacy
- **Last meeting date** and any outstanding action items

### Step 2: Portfolio Performance

For each account and the household aggregate:

| Metric | QTD | YTD | 1-Year | 3-Year | Since Inception |
|--------|-----|-----|--------|--------|----------------|
| Portfolio return | | | | | |
| Benchmark return | | | | | |
| Alpha | | | | | |

**Performance Attribution:**
- Which asset classes / positions drove returns?
- Top 3 contributors and top 3 detractors
- Any outsized single-position impact?

### Step 3: Allocation Review

Current vs. target allocation:

| Asset Class | Target | Current | Drift | Action |
|------------|--------|---------|-------|--------|
| US Large Cap | | | | |
| US Mid/Small | | | | |
| International Developed | | | | |
| Emerging Markets | | | | |
| Fixed Income | | | | |
| Alternatives | | | | |
| Cash | | | | |

Flag any drift exceeding the IPS rebalancing threshold (typically 3-5%).

### Step 4: Talking Points

Generate a meeting agenda:

1. **Market overview** (2-3 min): Brief macro context and outlook
2. **Portfolio performance** (5 min): How did we do? Why?
3. **Allocation review** (5 min): Any rebalancing needed?
4. **Planning updates** (5-10 min):
   - Life changes? (job, health, family, home, education)
   - Income needs changing?
   - Tax situation updates
   - Estate planning updates
5. **Action items** (5 min): What are we doing before next meeting?

### Step 5: Proactive Recommendations

Based on the review, suggest:
- Rebalancing trades (if drift exceeds thresholds)
- Tax-loss harvesting opportunities
- Cash deployment or withdrawal planning
- Roth conversion opportunities (if applicable)
- Beneficiary updates or estate planning needs
- Insurance review (life, disability, LTC)

### Step 6: Output

- One-page client review summary (Word or PDF)
- Performance table with benchmarks
- Allocation pie chart (current vs. target)
- Recommended action items
- Meeting agenda

## Important Notes

- Know your client before the meeting — review notes from last meeting
- Lead with what the client cares about, not what you want to talk about
- If performance was bad, address it directly — don't hide or spin
- Always end with clear action items and next steps with dates
- Document the meeting notes and any changes to the IPS
- Compliance: ensure all materials are compliant with firm policies and regulatory requirements

## Hermes Profile Notes
This skill was packaged from `pi-financial-services` source path `plugins/vertical-plugins/wealth-management/skills/client-review` for the Hermes financial-services profile. Use institutional data connectors first when available, cite sources, and stage outputs for qualified human review.


## Common Pitfalls
1. Do not present drafts as investment, legal, tax, or accounting advice.
2. Do not use web search as the primary source when an institutional MCP/data connector is available.
3. Do not execute transactions, contact clients, post to a ledger, or approve onboarding. Stage outputs for review.


## Verification Checklist
- [ ] Inputs, assumptions, dates, and currencies are explicit.
- [ ] Numbers tie across tables, models, decks, and memos.
- [ ] Sources are cited and institutional data is preferred where available.
- [ ] Output is labeled draft / for human review where appropriate.
