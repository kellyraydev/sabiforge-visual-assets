#!/usr/bin/env python3
"""Decode library/encoded/**/*.b64 into real image files, then remove the encoded copies."""

import base64
import shutil
from pathlib import Path

root = Path(__file__).resolve().parents[1]
encoded = root / "library" / "encoded"
if not encoded.exists():
    raise SystemExit(0)

for path in sorted(encoded.rglob("*.b64")):
    rel = path.relative_to(encoded)
    dest = root / "library" / Path(str(rel)[:-4])
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(base64.b64decode("".join(path.read_text().split())))

shutil.rmtree(encoded)
workflow = root / ".github" / "workflows" / "materialize-assets.yml"
if workflow.exists():
    workflow.unlink()
workflows = root / ".github" / "workflows"
if workflows.exists() and not any(workflows.iterdir()):
    workflows.rmdir()
github_dir = root / ".github"
if github_dir.exists() and not any(github_dir.iterdir()):
    github_dir.rmdir()
