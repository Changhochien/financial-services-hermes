---
name: fsi-command-teaser
description: Use when financial-services work requires draft an anonymous one-page
  teaser.
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
    - investment-banking
    - teaser
    related_skills: []
---

# FSI Command: /teaser

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/teaser` from `investment-banking`. Invoke it explicitly with `/skill fsi-command-teaser` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/teaser` or a teaser financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `teaser` skill and create a blind teaser for the specified company.

If a company name is provided, use it. Otherwise ask the user for the company details to anonymize.

## Hermes Invocation
- Explicit: `/skill fsi-command-teaser`
- Natural language: “Use the teaser command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
