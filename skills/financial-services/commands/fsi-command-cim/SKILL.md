---
name: fsi-command-cim
description: Use when financial-services work requires draft a Confidential Information
  Memorandum.
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
    - cim
    - command
    - financial-services
    - investment-banking
    related_skills: []
---

# FSI Command: /cim

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/cim` from `investment-banking`. Invoke it explicitly with `/skill fsi-command-cim` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/cim` or a cim financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `cim-builder` skill and structure a CIM for the specified company.

If a company name is provided, use it. Otherwise ask the user for the target company and available source materials.

## Hermes Invocation
- Explicit: `/skill fsi-command-cim`
- Natural language: “Use the cim command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
