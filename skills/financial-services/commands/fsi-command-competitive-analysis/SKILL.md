---
name: fsi-command-competitive-analysis
description: Use when financial-services work requires create a competitive landscape
  analysis.
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
    - competitive-analysis
    - financial-analysis
    - financial-services
    related_skills: []
---

# FSI Command: /competitive-analysis

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/competitive-analysis` from `financial-analysis`. Invoke it explicitly with `/skill fsi-command-competitive-analysis` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/competitive-analysis` or a competitive analysis financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `competitive-analysis` skill and build a competitive landscape analysis for the specified company or industry.

If a company/industry is provided as an argument, use it. Otherwise ask the user what they want to analyze.

## Hermes Invocation
- Explicit: `/skill fsi-command-competitive-analysis`
- Natural language: “Use the competitive-analysis command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
