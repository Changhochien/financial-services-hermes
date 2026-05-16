---
name: fsi-command-sector
description: Use when financial-services work requires create a sector overview report.
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
    - equity-research
    - financial-services
    - sector
    related_skills: []
---

# FSI Command: /sector

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/sector` from `equity-research`. Invoke it explicitly with `/skill fsi-command-sector` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/sector` or a sector financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `sector-overview` skill and create an industry landscape report covering market sizing, competitive dynamics, and investment implications.

If a sector is provided, use it. Otherwise ask the user which industry to cover.

## Hermes Invocation
- Explicit: `/skill fsi-command-sector`
- Natural language: “Use the sector command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
