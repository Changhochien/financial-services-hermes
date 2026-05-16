---
name: fsi-command-morning-note
description: Use when financial-services work requires draft a morning meeting note.
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
    - morning-note
    related_skills: []
---

# FSI Command: /morning-note

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/morning-note` from `equity-research`. Invoke it explicitly with `/skill fsi-command-morning-note` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/morning-note` or a morning note financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `morning-note` skill and draft a concise morning note covering overnight developments, earnings reactions, and trade ideas across the coverage universe.

## Hermes Invocation
- Explicit: `/skill fsi-command-morning-note`
- Natural language: “Use the morning-note command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
