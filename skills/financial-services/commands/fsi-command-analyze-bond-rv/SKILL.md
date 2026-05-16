---
name: fsi-command-analyze-bond-rv
description: Use when financial-services work requires analyze a bond's relative value
  vs yield curves and credit spreads with scenario stress testing.
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
    - analyze-bond-rv
    - command
    - financial-services
    - lseg
    related_skills: []
---

# FSI Command: /analyze-bond-rv

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/analyze-bond-rv` from `lseg`. Invoke it explicitly with `/skill fsi-command-analyze-bond-rv` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/analyze-bond-rv` or a analyze bond rv financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

# Analyze Bond Relative Value

> This command uses LSEG bond pricing, yield curves, credit curves, and scenario analysis tools. See [CONNECTORS.md](../CONNECTORS.md) for available tools.

Perform relative value analysis on one or more bonds by combining pricing analytics, yield curve context, credit spread decomposition, and rate shock scenarios.

See the **bond-relative-value** skill for domain knowledge on spread frameworks and rich/cheap assessment.

## Workflow

### 1. Gather Bond Identifiers

Ask the user for:
- Bond identifier(s) — ISIN, RIC, or CUSIP (required)
- Optional benchmark bond for comparison
- Valuation date (optional, defaults to today)

### 2. Price the Bond(s)

Call `bond_price` with the identifier(s).

Extract: clean/dirty price, yield, duration, convexity, DV01, currency.

If benchmark provided, price that too.

### 3. Get the Risk-Free Yield Curve

Call `interest_rate_curve` (list then calculate) for the bond's currency.

Interpolate at the bond's maturity to compute G-spread.

### 4. Get the Credit Spread Curve

Call `credit_curve` (search by country/issuerType, then calculate).

Compute residual spread = bond G-spread minus credit curve spread at matching maturity. Positive residual = cheap; negative = rich.

### 5. Run Scenario Analysis

Call `yieldbook_scenario` with parallel rate shifts: -100bp, -50bp, 0bp, +50bp, +100bp.

Extract price change and P&L under each scenario.

### 6. Synthesize the Report

Present: bond summary table, spread decomposition (G-spread, credit spread, residual), scenario P&L table, and rich/cheap assessment.

If benchmark provided, include side-by-side comparison.

## Output Format

Lead with the rich/cheap assessment and supporting evidence. Follow with spread decomposition and scenario tables.

## Hermes Invocation
- Explicit: `/skill fsi-command-analyze-bond-rv`
- Natural language: “Use the analyze-bond-rv command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
