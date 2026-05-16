---
name: fsi-command-analyze-swap-curve
description: Use when financial-services work requires analyze the swap curve with
  government and inflation overlays to identify curve trade opportunities.
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
    - analyze-swap-curve
    - command
    - financial-services
    - lseg
    related_skills: []
---

# FSI Command: /analyze-swap-curve

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/analyze-swap-curve` from `lseg`. Invoke it explicitly with `/skill fsi-command-analyze-swap-curve` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/analyze-swap-curve` or a analyze swap curve financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

# Analyze Swap Curve

> This command uses LSEG swap pricing, interest rate curves, and inflation curve tools. See [CONNECTORS.md](../CONNECTORS.md) for available tools.

Build and analyze the interest rate swap curve, overlay government yields and inflation breakevens, and identify curve trade opportunities.

See the **swap-curve-strategy** skill for domain knowledge on curve analysis and trade construction.

## Workflow

### 1. Gather Input

Ask the user for:
- Currency (required) — e.g., EUR, USD, GBP, CHF, JPY
- Reference rate index (optional) — e.g., ESTR, SOFR, SONIA, TONA
- Valuation date (optional, defaults to today)

### 2. Discover Swap Templates

Call `ir_swap` in list mode with the currency and optional index.

Extract: available template references, index details, conventions.

### 3. Build the Swap Curve

Call `ir_swap` in price mode for standard tenors: 2Y, 5Y, 7Y, 10Y, 20Y, 30Y.

Extract: par swap rate and DV01 at each tenor.

### 4. Overlay the Government Curve

Call `interest_rate_curve` (list then calculate) for the same currency.

Compute swap spread = swap rate minus government yield at each tenor.

### 5. Decompose Real Rates

Call `inflation_curve` (search then calculate) for the currency.

Compute real swap rate = nominal swap rate minus inflation breakeven at each tenor.

### 6. Synthesize Curve Strategy Views

Compute curve metrics: 2s10s slope, 5s30s slope, 2s5s10s butterfly.

Identify opportunities: steepener, flattener, butterfly, or swap spread trades based on current levels vs historical norms.

Present: swap curve table with government overlay, curve metrics, real rate decomposition, and trade recommendations with DV01-neutral ratios.

## Output Format

Lead with curve shape summary and key metrics (2s10s, butterfly). Follow with detailed tables and trade idea section.

## Hermes Invocation
- Explicit: `/skill fsi-command-analyze-swap-curve`
- Natural language: “Use the analyze-swap-curve command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
