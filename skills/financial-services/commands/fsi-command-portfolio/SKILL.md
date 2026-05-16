---
name: fsi-command-portfolio
description: Use when financial-services work requires review portfolio company performance.
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
    - portfolio
    - private-equity
    related_skills: []
---

# FSI Command: /portfolio

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/portfolio` from `private-equity`. Invoke it explicitly with `/skill fsi-command-portfolio` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/portfolio` or a portfolio financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `portfolio-monitoring` skill and analyze a portfolio company's performance against plan — KPIs, variances, and red flags.

If a company name or file is provided, use it. Otherwise ask the user for the portfolio company and financial data.

## Hermes Invocation
- Explicit: `/skill fsi-command-portfolio`
- Natural language: “Use the portfolio command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
