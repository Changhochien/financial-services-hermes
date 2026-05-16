---
name: fsi-command-rebalance
description: Use when financial-services work requires analyze drift and generate
  rebalancing trades.
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
    - command
    - financial-services
    - rebalance
    - wealth-management
    related_skills: []
---

# FSI Command: /rebalance

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/rebalance` from `wealth-management`. Invoke it explicitly with `/skill fsi-command-rebalance` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/rebalance` or a rebalance financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `portfolio-rebalance` skill to analyze allocation drift and recommend tax-aware rebalancing trades.

If a client or account is provided, use it. Otherwise ask for the portfolio to analyze.

## Hermes Invocation
- Explicit: `/skill fsi-command-rebalance`
- Natural language: “Use the rebalance command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
