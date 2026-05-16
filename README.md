# Hermes Financial Services Profile

Installable Hermes Agent profile distribution for financial-services workflows: investment banking, equity research, private equity, wealth management, fund administration, accounting operations, KYC, GL reconciliation, institutional modeling, and partner-data workflows.

## One-command install

```bash
hermes profile install https://github.com/Changhochien/pi-financial-services-hermes --name financial-services --yes
```

Start Hermes with the profile:

```bash
hermes -p financial-services
```

Or make it your default profile:

```bash
hermes profile use financial-services
```

## What is included

- 66 domain and partner skills converted from `pi-financial-services`
- 47 command-style Hermes skills converted from Cowork slash commands (`/skill fsi-command-dcf`, `/skill fsi-command-comps`, etc.)
- 10 named-agent workflow skills (`pitch-agent`, `market-researcher`, `earnings-reviewer`, etc.)
- Financial-services `SOUL.md` with data-source priority, compliance guardrails, and output quality standards
- `mcp.json` plus `config.yaml` entries for institutional data MCP servers
- Validation scripts and reference docs

## Common invocations

```text
/skill pitch-agent
/skill market-researcher
/skill earnings-reviewer
/skill model-builder
/skill gl-reconciler
/skill fsi-command-dcf
/skill fsi-command-comps
/skill fsi-command-earnings
/skill fsi-command-ic-memo
```

Natural language works too:

```text
Build a DCF for AAPL using the financial-services profile.
Prepare a market-research briefing for GLP-1 supply chain beneficiaries.
Use the pitch-agent workflow to draft a sponsor sell-side pitch outline.
Run a GL reconciliation workflow on this workbook and stage breaks for review.
```

## MCP / institutional data setup

The profile installs with MCP servers listed but disabled by default so it works on machines without paid data subscriptions. To enable data connectors:

1. Copy the generated profile env example:
   ```bash
   cp ~/.hermes/profiles/financial-services/.env.EXAMPLE ~/.hermes/profiles/financial-services/.env
   ```
2. Fill in the API keys you have.
3. Edit `~/.hermes/profiles/financial-services/config.yaml` and set `enabled: true` for the MCP servers you want.
4. Restart Hermes or run `/reload-mcp` in a fresh session.

## Update

```bash
hermes profile update financial-services --yes
```

Hermes preserves user-owned profile data on update: `.env`, memories, sessions, logs, plans, workspace, auth, and local customizations.

## Validate this repo

```bash
python3 scripts/check.py
```

## Safety note

This profile drafts financial-services work product for human review. It does not provide investment, legal, tax, accounting, fiduciary, or compliance advice and must not be used to execute trades, move money, post ledgers, approve onboarding, or contact clients without qualified human authorization.
