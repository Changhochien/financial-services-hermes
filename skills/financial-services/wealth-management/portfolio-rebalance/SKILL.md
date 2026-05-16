---
name: portfolio-rebalance
description: Use when financial-services work requires portfolio Rebalance.
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

# Portfolio Rebalance

description: Analyze portfolio allocation drift and generate rebalancing trade recommendations across accounts. Considers tax implications, transaction costs, and wash sale rules. Triggers on "rebalance", "portfolio drift", "allocation check", "rebalancing trades", or "my portfolio is out of balance".

## Workflow

### Step 1: Current State

For each account, capture:
- Account type (taxable, IRA, Roth, 401k)
- Holdings with current market value
- Cost basis (for taxable accounts)
- Unrealized gains/losses per position

### Step 2: Drift Analysis

Compare current allocation to IPS targets:

| Asset Class | Target % | Current % | Drift | $ Over/Under |
|------------|----------|-----------|-------|-------------|
| US Large Cap Equity | | | | |
| US Small/Mid Cap | | | | |
| International Developed | | | | |
| Emerging Markets | | | | |
| Investment Grade Bonds | | | | |
| High Yield / Credit | | | | |
| TIPS / Inflation Protected | | | | |
| Alternatives | | | | |
| Cash | | | | |

Flag positions exceeding the rebalancing band (typically ±3-5%).

### Step 3: Trade Recommendations

Generate trades to bring allocation back to target:

**Tax-Aware Rebalancing Rules:**
- Prefer rebalancing in tax-advantaged accounts (IRA, Roth) first — no tax consequences
- In taxable accounts, avoid selling positions with large short-term gains
- Harvest losses where possible while rebalancing
- Watch for wash sale rules (30-day window) across all accounts
- Consider directing new contributions to underweight asset classes instead of trading

**Trade List:**

| Account | Action | Security | Shares/$ | Reason | Tax Impact |
|---------|--------|----------|----------|--------|-----------|
| | Buy/Sell | | | Rebalance / TLH | ST gain / LT gain / Loss |

### Step 4: Asset Location Review

Optimize which assets are held in which account types:
- **Tax-deferred (IRA/401k)**: Bonds, REITs, high-turnover funds (highest tax drag)
- **Roth**: Highest expected growth assets (tax-free growth)
- **Taxable**: Tax-efficient equity (index funds, ETFs, munis), tax-loss harvesting candidates

### Step 5: Implementation

- Total trades by account
- Estimated transaction costs
- Estimated tax impact (realized gains/losses)
- Net effect on allocation drift

### Step 6: Output

- Drift analysis table
- Recommended trade list (Excel)
- Tax impact summary
- Before/after allocation comparison

## Important Notes

- Don't rebalance for rebalancing's sake — small drift within bands is fine
- Tax costs can outweigh rebalancing benefits in taxable accounts — calculate the breakeven
- Consider pending cash flows (contributions, withdrawals, RMDs) before trading
- Check for any client-specific restrictions (ESG, concentrated stock, lockups)
- Document rationale for every trade for compliance records
- Wash sale rules apply across accounts — coordinate trades across the household

## Hermes Profile Notes
This skill was packaged from `pi-financial-services` source path `plugins/vertical-plugins/wealth-management/skills/portfolio-rebalance` for the Hermes financial-services profile. Use institutional data connectors first when available, cite sources, and stage outputs for qualified human review.


## Common Pitfalls
1. Do not present drafts as investment, legal, tax, or accounting advice.
2. Do not use web search as the primary source when an institutional MCP/data connector is available.
3. Do not execute transactions, contact clients, post to a ledger, or approve onboarding. Stage outputs for review.


## Verification Checklist
- [ ] Inputs, assumptions, dates, and currencies are explicit.
- [ ] Numbers tie across tables, models, decks, and memos.
- [ ] Sources are cited and institutional data is preferred where available.
- [ ] Output is labeled draft / for human review where appropriate.
