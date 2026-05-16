---
name: fsi-command-lbo
description: Use when financial-services work requires build an LBO model for a PE
  acquisition.
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
    - financial-analysis
    - financial-services
    - lbo
    related_skills: []
---

# FSI Command: /lbo

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/lbo` from `financial-analysis`. Invoke it explicitly with `/skill fsi-command-lbo` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/lbo` or a lbo financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `lbo-model` skill and build a leveraged buyout model for the specified company or deal.

If a company name is provided as an argument, use it. Otherwise ask the user for the target company and deal parameters.

## Hermes Invocation
- Explicit: `/skill fsi-command-lbo`
- Natural language: “Use the lbo command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
