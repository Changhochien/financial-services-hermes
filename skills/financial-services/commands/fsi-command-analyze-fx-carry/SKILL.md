---
name: fsi-command-analyze-fx-carry
description: Use when financial-services work requires evaluate FX carry trade opportunities
  with spot, forwards, vol surface, and historical context.
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
    - analyze-fx-carry
    - command
    - financial-services
    - lseg
    related_skills: []
---

# FSI Command: /analyze-fx-carry

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/analyze-fx-carry` from `lseg`. Invoke it explicitly with `/skill fsi-command-analyze-fx-carry` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/analyze-fx-carry` or a analyze fx carry financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

# Analyze FX Carry Trade

> This command uses LSEG FX pricing, forward curves, volatility surfaces, and historical data tools. See [CONNECTORS.md](../CONNECTORS.md) for available tools.

Evaluate carry trade opportunities for a currency pair by combining spot rates, forward points, the carry term structure, volatility risk, and historical price context.

See the **fx-carry-trade** skill for domain knowledge on carry frameworks and risk metrics.

## Workflow

### 1. Gather Input

Ask the user for:
- Currency pair (required) — e.g., USDJPY, EURUSD, AUDUSD
- Target tenor (optional, default 3M)
- Valuation date (optional, defaults to today)

### 2. Get the Spot Rate

Call `fx_spot_price` with the currency pair.

Extract: mid/bid/ask rates, bid-ask spread.

### 3. Price the Forward at Target Tenor

Call `fx_forward_price` with the pair and target tenor.

Extract: forward rate, forward points. Compute annualized carry.

### 4. Map the Full Carry Curve

Call `fx_forward_curve` (list then calculate) for the pair.

Present carry profile across tenors (ON through 1Y): forward points, annualized carry, cumulative carry. Identify the sweet-spot tenor.

### 5. Assess Volatility Risk

Call `fx_vol_surface` for the pair.

Extract: ATM vol at target tenor, 25-delta risk reversal, 25-delta butterfly.

Compute carry-to-vol ratio = annualized carry / ATM implied vol.

### 6. Historical Spot Context

Call `tscc_historical_pricing_summaries` for the pair's RIC with `interval: "P1D"`, `tenor: "1Y"`.

Assess: 52-week range, current position in range, trend direction.

### 7. Synthesize the Report

Present: carry-to-vol ratio and overall assessment, spot & forward pricing, carry term structure table, vol surface snapshot, historical context.

## Output Format

Lead with the carry-to-vol ratio and overall assessment (attractive / moderate / unattractive). Follow with detailed supporting data in tables.

## Hermes Invocation
- Explicit: `/skill fsi-command-analyze-fx-carry`
- Natural language: “Use the analyze-fx-carry command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
