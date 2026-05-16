# Hermes Financial Services Profile Distribution

This repository is a clean Hermes Agent profile distribution. It is generated from `Changhochien/pi-financial-services` and designed to install with:

```bash
hermes profile install https://github.com/Changhochien/financial-services-hermes --name financial-services --yes
```

Do not add user data, credentials, sessions, memories, logs, workspaces, or local-only files to this repo. Profile user data is created on the installing machine and preserved by Hermes update semantics.

Key files:
- `distribution.yaml` — Hermes profile distribution manifest
- `SOUL.md` — financial-services system prompt/persona
- `skills/financial-services/` — domain, command, partner, and named-agent workflow skills
- `config.yaml` — optional MCP server definitions, disabled by default
- `mcp.json` — original MCP server manifest for reference/distribution convention
- `scripts/check.py` — validation script
