#!/usr/bin/env bash
set -euo pipefail
PROFILE_NAME="${1:-financial-services}"
PROFILE_DIR="$HOME/.hermes/profiles/$PROFILE_NAME"

if [ ! -d "$PROFILE_DIR" ]; then
  echo "Profile directory not found: $PROFILE_DIR" >&2
  echo "Install first: hermes profile install https://github.com/Changhochien/financial-services-hermes --name $PROFILE_NAME --yes" >&2
  exit 1
fi

if [ ! -f "$PROFILE_DIR/.env" ] && [ -f "$PROFILE_DIR/.env.EXAMPLE" ]; then
  cp "$PROFILE_DIR/.env.EXAMPLE" "$PROFILE_DIR/.env"
  echo "Created $PROFILE_DIR/.env from .env.EXAMPLE"
fi

cat <<MSG
MCP setup for profile: $PROFILE_NAME

1. Edit:
   $PROFILE_DIR/.env

2. Add API keys you have (all are optional):
   CAPIQ_API_KEY, DALOOPA_API_KEY, MORNINGSTAR_API_KEY, FACTSET_API_KEY,
   MOODYS_API_KEY, MTNEWSWIRE_API_KEY, AIERA_API_KEY, LSEG_API_KEY,
   PITCHBOOK_API_KEY, CHRONOGRAPH_API_KEY, EGNYTE_API_KEY

3. Edit:
   $PROFILE_DIR/config.yaml

4. Set enabled: true for only the MCP servers you have credentials for.

5. Restart Hermes or run /reload-mcp in a fresh session.
MSG
