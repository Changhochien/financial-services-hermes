---
name: fsi-command-dd-checklist
description: Use when financial-services work requires generate a due diligence checklist.
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
    - dd-checklist
    - financial-services
    - private-equity
    related_skills: []
---

# FSI Command: /dd-checklist

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/dd-checklist` from `private-equity`. Invoke it explicitly with `/skill fsi-command-dd-checklist` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/dd-checklist` or a dd checklist financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `dd-checklist` skill and generate a comprehensive, sector-tailored due diligence checklist with status tracking.

If a company name is provided, use it. Otherwise ask the user for the target company and deal details.

## Hermes Invocation
- Explicit: `/skill fsi-command-dd-checklist`
- Natural language: “Use the dd-checklist command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
