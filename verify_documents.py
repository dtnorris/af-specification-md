"""Check this selected document set offline; this is not a scorer or release gate."""

import hashlib
import json
from pathlib import Path
import re
import sys

INVENTORY_SHA256 = "5ebb0fffcafa165a71bd3afef70e483217074d788d02ff9241ab3cedfd6bf0e6"


def digest(data):
    """Return the SHA-256 of byte input; TypeError propagates for other inputs."""
    return hashlib.sha256(data).hexdigest()


def sections(data):
    """Return heading/body byte identities, including nested bodies and headings.

    Input is UTF-8 Markdown bytes. Each body ends before the next heading of
    equal or lower level. Decode errors propagate; no whitespace is normalized.
    Whole-file hashes additionally cover text preceding the first heading.
    """
    headings = list(re.finditer(rb"^(#{1,6})[ \t]+([^\r\n]+)\r?$", data, re.M))
    result = []
    for position, heading in enumerate(headings):
        level = len(heading[1])
        end = next((entry.start() for entry in headings[position + 1:]
                    if len(entry[1]) <= level), len(data))
        result.append({"level": level, "heading": heading[2].decode("utf-8"),
                       "start": heading.start(), "end": end,
                       "sha256": digest(data[heading.start():end])})
    return result


def verify(root):
    """Verify one explicit root against the pinned inventory; return file count.

    Reject extra/missing files, symlinks, modes, versions, bodies and bytes.
    Raises ValueError or filesystem/JSON errors on corruption. Git administration
    alone is excluded. This verifies preservation, not semantics or rights.
    """
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise ValueError("an explicit real document directory is required")
    inventory_bytes = (root / "documents.json").read_bytes()
    if digest(inventory_bytes) != INVENTORY_SHA256:
        raise ValueError("inventory identity changed")
    inventory = json.loads(inventory_bytes)
    expected = {entry["path"] for entry in inventory["files"]}
    allowed = expected | {"documents.json", "verify_documents.py"}
    actual = set()
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if relative.parts[0] == ".git":
            continue
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"unexpected directory or symlink: {relative}")
        actual.add(str(relative))
    if actual != allowed:
        raise ValueError(f"file inventory differs: {sorted(actual ^ allowed)}")
    for name in allowed:
        if (root / name).stat().st_mode & 0o777 != 0o644:
            raise ValueError(f"mode changed: {name}")
    for entry in inventory["files"]:
        data = (root / entry["path"]).read_bytes()
        if "version_heading" in entry:
            match = re.search(rb"^## Version ([^\s]+).*$", data, re.M)
            if not match or match[1].decode() != entry["version_heading"]:
                raise ValueError(f"incompatible version: {entry['path']}")
        if "sections" in entry and sections(data) != entry["sections"]:
            raise ValueError(f"section body changed: {entry['path']}")
        for collection in ("dimensions", "score_anchors", "prompt_sections"):
            for body in entry.get(collection, []):
                if digest(data[body["start"]:body["end"]]) != body["sha256"]:
                    raise ValueError(f"{collection} body changed: {entry['path']}")
        if len(data) != entry["bytes"] or digest(data) != entry["sha256"]:
            raise ValueError(f"bound bytes changed: {entry['path']}")
    return len(inventory["files"])


if __name__ == "__main__":
    try:
        count = verify(sys.argv[1] if len(sys.argv) == 2 else Path(__file__).parent)
        print(f"PASS: {count} bound files; 19 dimensions, 85 anchors, 10 assessment sections preserved")
    except (OSError, ValueError, KeyError) as error:
        print(f"REFUSED: {error}", file=sys.stderr)
        raise SystemExit(2)
