---
name: fsi-command-analyze-option-vol
description: Use when financial-services work requires analyze option volatility with
  vol surface, Greeks, and implied vs realized vol comparison.
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
    - analyze-option-vol
    - command
    - financial-services
    - lseg
    related_skills: []
---

# FSI Command: /analyze-option-vol

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/analyze-option-vol` from `lseg`. Invoke it explicitly with `/skill fsi-command-analyze-option-vol` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/analyze-option-vol` or a analyze option vol financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

# Analyze Option Volatility

> This command uses LSEG volatility surfaces, option pricing, and historical data tools. See [CONNECTORS.md](../CONNECTORS.md) for available tools.

Analyze the volatility environment for an underlying by generating the vol surface, pricing options with full Greeks, and comparing implied vs realized volatility.

See the **option-vol-analysis** skill for domain knowledge on vol surface interpretation and Greeks analysis.

## Workflow

### 1. Gather Input

Ask the user for:
- Underlying asset (required):
  - Equities/indices: RIC format (e.g., "VOD.L@RIC", ".SPX@RIC")
  - Futures: RICROOT format (e.g., "ES@RICROOT", "CL@RICROOT")
  - FX: ISO pair (e.g., "EURUSD", "USDJPY")
- Strike price (optional, defaults to ATM)
- Expiry date or tenor (optional, defaults to 3M)
- Call or Put (optional, defaults to both)

Determine whether this is equity/index or FX to select the correct vol surface tool.

### 2. Generate the Volatility Surface

**For equities/indices/futures:** Call `equity_vol_surface`.

**For FX:** Call `fx_vol_surface`.

Extract: ATM vol at each tenor, 25-delta risk reversal, 25-delta butterfly.

### 3. Discover Option Templates

Call `option_template_list` for the underlying. Identify available types, expiries, and strikes.

### 4. Price the Option

Call `option_value` with the underlying, strike, and expiry.

Extract: premium, delta, gamma, vega, theta, implied vol.

### 5. Compute Realized Volatility

Call `tscc_historical_pricing_summaries` with `interval: "P1D"`, `tenor: "1Y"`.

Compute close-to-close realized vol over 20-day, 60-day, 90-day windows. Compare to matching implied vol tenors.

### 6. Synthesize the Report

Present: vol surface summary table, Greeks table, implied vs realized comparison, vol regime assessment, strategy recommendations.

## Output Format

Lead with the key vol finding (implied rich/cheap vs realized). Follow with the surface summary, option pricing, and detailed comparison.

## Hermes Invocation
- Explicit: `/skill fsi-command-analyze-option-vol`
- Natural language: “Use the analyze-option-vol command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
