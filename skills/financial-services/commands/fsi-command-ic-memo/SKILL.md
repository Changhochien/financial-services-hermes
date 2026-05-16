---
name: fsi-command-ic-memo
description: Use when financial-services work requires draft an investment committee
  memo.
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
    - ic-memo
    - private-equity
    related_skills: []
---

# FSI Command: /ic-memo

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/ic-memo` from `private-equity`. Invoke it explicitly with `/skill fsi-command-ic-memo` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/ic-memo` or a ic memo financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `ic-memo` skill and draft a structured IC memo synthesizing due diligence findings, financial analysis, and deal terms.

If a company name is provided, use it. Otherwise ask the user for the target and available materials.

## Hermes Invocation
- Explicit: `/skill fsi-command-ic-memo`
- Natural language: “Use the ic-memo command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
