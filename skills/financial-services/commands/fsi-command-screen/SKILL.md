---
name: fsi-command-screen
description: Use when financial-services work requires run a stock screen or generate
  investment ideas.
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
    - screen
    related_skills: []
---

# FSI Command: /screen

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/screen` from `equity-research`. Invoke it explicitly with `/skill fsi-command-screen` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/screen` or a screen financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `idea-generation` skill and run quantitative screens or thematic sweeps to surface new investment ideas.

If criteria are provided, use them. Otherwise ask the user what they're looking for (long/short, sector, style, theme).

## Hermes Invocation
- Explicit: `/skill fsi-command-screen`
- Natural language: “Use the screen command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
