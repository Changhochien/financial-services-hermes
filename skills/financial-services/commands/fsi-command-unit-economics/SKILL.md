---
name: fsi-command-unit-economics
description: Use when financial-services work requires analyze unit economics (ARR
  cohorts, LTV/CAC, retention).
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
    - private-equity
    - unit-economics
    related_skills: []
---

# FSI Command: /unit-economics

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/unit-economics` from `private-equity`. Invoke it explicitly with `/skill fsi-command-unit-economics` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/unit-economics` or a unit economics financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `unit-economics` skill and analyze customer economics, ARR cohorts, net retention, and revenue quality.

If a company or file is provided, use it. Otherwise ask the user for the target and available data.

## Hermes Invocation
- Explicit: `/skill fsi-command-unit-economics`
- Natural language: “Use the unit-economics command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
