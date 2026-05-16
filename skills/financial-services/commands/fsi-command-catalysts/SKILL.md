---
name: fsi-command-catalysts
description: Use when financial-services work requires view or update the catalyst
  calendar.
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
    - catalysts
    - command
    - equity-research
    - financial-services
    related_skills: []
---

# FSI Command: /catalysts

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/catalysts` from `equity-research`. Invoke it explicitly with `/skill fsi-command-catalysts` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/catalysts` or a catalysts financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `catalyst-calendar` skill to build or review upcoming catalysts across the coverage universe.

If a timeframe is provided, use it. Otherwise default to the next 2 weeks.

## Hermes Invocation
- Explicit: `/skill fsi-command-catalysts`
- Natural language: “Use the catalysts command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
