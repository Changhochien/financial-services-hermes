#!/usr/bin/env python3
"""Validate the Hermes financial-services profile distribution."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:  # PyYAML is bundled with Hermes, but may not be in system python.
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
MAX_DESCRIPTION = 1024


def load_yaml(text: str):
    if yaml is not None:
        return yaml.safe_load(text)
    # Minimal fallback parser for this repo's generated YAML/frontmatter.
    data = {}
    for raw in text.splitlines():
        if not raw or raw.startswith(" ") or raw.startswith("-") or raw.strip().startswith("#"):
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if not key:
            continue
        data[key] = value if value else True
    return data


def parse_frontmatter(text: str):
    if not text.startswith("---"):
        raise ValueError("missing YAML frontmatter")
    m = re.search(r"\n---\s*\n", text[3:])
    if not m:
        raise ValueError("frontmatter not closed")
    yml = text[3:m.start() + 3]
    body = text[m.end() + 3:]
    data = load_yaml(yml) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    if not body.strip():
        raise ValueError("empty skill body")
    return data, body


def main() -> int:
    errors = []

    for required in ["distribution.yaml", "SOUL.md", "README.md", "config.yaml", "mcp.json"]:
        if not (ROOT / required).exists():
            errors.append(f"missing {required}")

    try:
        dist = load_yaml((ROOT / "distribution.yaml").read_text()) or {}
        if dist.get("name") != "financial-services":
            errors.append("distribution.yaml name must be financial-services")
        if not str(dist.get("hermes_requires", "")).startswith(">="):
            errors.append("distribution.yaml hermes_requires should be a >= constraint")
    except Exception as exc:
        errors.append(f"distribution.yaml parse failed: {exc}")

    try:
        mcp = json.loads((ROOT / "mcp.json").read_text())
        if not isinstance(mcp.get("mcpServers"), dict) or not mcp["mcpServers"]:
            errors.append("mcp.json must contain non-empty mcpServers mapping")
    except Exception as exc:
        errors.append(f"mcp.json parse failed: {exc}")

    try:
        cfg_text = (ROOT / "config.yaml").read_text()
        cfg = load_yaml(cfg_text) or {}
        if yaml is not None:
            if not isinstance(cfg.get("mcp_servers"), dict):
                errors.append("config.yaml must contain mcp_servers mapping")
        elif "mcp_servers:" not in cfg_text:
            errors.append("config.yaml must contain mcp_servers mapping")
    except Exception as exc:
        errors.append(f"config.yaml parse failed: {exc}")

    skill_files = sorted((ROOT / "skills").rglob("SKILL.md"))
    if not skill_files:
        errors.append("no SKILL.md files found")

    names = []
    for sf in skill_files:
        try:
            data, _ = parse_frontmatter(sf.read_text(encoding="utf-8"))
            name = str(data.get("name") or "").strip()
            desc = str(data.get("description") or "").strip()
            if not name:
                errors.append(f"{sf}: missing name")
            elif not re.match(r"^[a-z0-9][a-z0-9_-]{0,63}$", name):
                errors.append(f"{sf}: invalid name {name!r}")
            else:
                names.append(name)
            if not desc:
                errors.append(f"{sf}: missing description")
            elif len(desc) > MAX_DESCRIPTION:
                errors.append(f"{sf}: description exceeds {MAX_DESCRIPTION} chars")
            elif not desc.lower().startswith("use when"):
                errors.append(f"{sf}: description should start with 'Use when'")
            for key in ["version", "author", "license", "metadata"]:
                if key not in data:
                    errors.append(f"{sf}: missing {key}")
        except Exception as exc:
            errors.append(f"{sf}: {exc}")

    dupes = [name for name, count in Counter(names).items() if count > 1]
    if dupes:
        errors.append("duplicate skill names: " + ", ".join(sorted(dupes)))

    print(f"Checked {len(skill_files)} skills")
    print(f"Unique skill names: {len(set(names))}")

    if errors:
        print("\nERRORS:")
        for err in errors:
            print(f"- {err}")
        return 1
    print("Validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
