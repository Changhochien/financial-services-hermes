---
name: fsi-command-ai-readiness
description: Use when financial-services work requires scan the portfolio for the
  highest-leverage AI opportunities.
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
    - ai-readiness
    - command
    - financial-services
    - private-equity
    related_skills: []
---

# FSI Command: /ai-readiness

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/ai-readiness` from `private-equity`. Invoke it explicitly with `/skill fsi-command-ai-readiness` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/ai-readiness` or a ai readiness financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `ai-readiness` skill and scan portfolio companies for AI leverage — per-company go / no-go gate, quick wins ranked by EBITDA impact across the portfolio, and replays that hit multiple companies at once.

If a folder or company list is provided, use it. Otherwise ask which companies to include and for their latest quarterly materials.

## Hermes Invocation
- Explicit: `/skill fsi-command-ai-readiness`
- Natural language: “Use the ai-readiness command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
