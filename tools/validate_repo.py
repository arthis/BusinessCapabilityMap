import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAPS_FILE = ROOT / "bcm" / "capabilities.yaml"
VOCAB_FILE = ROOT / "bcm" / "vocab.yaml"

def die(msg: str):
    print(f"[ERROR] {msg}")
    sys.exit(1)

def main():
    if not CAPS_FILE.exists():
        die(f"Missing {CAPS_FILE}")
    if not VOCAB_FILE.exists():
        die(f"Missing {VOCAB_FILE}")

    vocab = yaml.safe_load(VOCAB_FILE.read_text(encoding="utf-8"))
    levels = set(vocab["levels"])
    zoning = set(vocab["zoning"])

    data = yaml.safe_load(CAPS_FILE.read_text(encoding="utf-8"))
    caps = data.get("capabilities", [])
    if not caps:
        die("No capabilities found")

    ids = set()
    by_id = {}
    for c in caps:
        cid = c.get("id")
        if not cid:
            die("Capability missing id")
        if cid in ids:
            die(f"Duplicate capability id: {cid}")
        ids.add(cid)
        by_id[cid] = c

        lvl = c.get("level")
        if lvl not in levels:
            die(f"{cid}: invalid level '{lvl}' (allowed: {sorted(levels)})")

        zon = c.get("zoning")
        if zon not in zoning:
            die(f"{cid}: invalid zoning '{zon}' (allowed: {sorted(zoning)})")

        # Parent rules
        if lvl != "L1":
            parent = c.get("parent")
            if not parent:
                die(f"{cid}: level {lvl} must have a parent")
        else:
            if "parent" in c:
                die(f"{cid}: L1 must not have parent")

        # Heatmap checks (optional)
        hm = c.get("heatmap", {})
        if hm:
            if "maturity" in hm:
                m = hm["maturity"]
                allowed = set(vocab["heatmap_scales"]["maturity"])
                if m not in allowed:
                    die(f"{cid}: maturity {m} not in {sorted(allowed)}")

    # Parent existence + level coherence (basic)
    for c in caps:
        lvl = c["level"]
        if lvl == "L1":
            continue
        parent_id = c.get("parent")
        if parent_id not in by_id:
            die(f"{c['id']}: parent not found: {parent_id}")

    print("[OK] Repo validation passed")

if __name__ == "__main__":
    main()
