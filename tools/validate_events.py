#!/usr/bin/env python3
# validate_bcm_events.py

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"[ERROR] File not found: {path}")
    except Exception as e:
        raise SystemExit(f"[ERROR] Cannot read/parse YAML {path}: {e}")


def build_capability_index(bcm: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    caps = bcm.get("capabilities")
    if not isinstance(caps, list):
        raise SystemExit("[ERROR] BCM file must contain a top-level 'capabilities:' list.")
    idx: Dict[str, Dict[str, Any]] = {}
    for c in caps:
        if not isinstance(c, dict) or "id" not in c:
            continue
        idx[c["id"]] = c
    return idx


def iter_id_paths(obj: Any, path: str = "$") -> List[Tuple[str, str]]:
    """
    Return list of (path, id_value) for any dict key named exactly 'id'.
    """
    found: List[Tuple[str, str]] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}.{k}"
            if k == "id" and isinstance(v, str) and v.startswith("CAP."):
                found.append((p, v))
            found.extend(iter_id_paths(v, p))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            found.extend(iter_id_paths(v, f"{path}[{i}]"))
    return found


def cap_exists(cap_idx: Dict[str, Dict[str, Any]], cap_id: str) -> bool:
    return cap_id in cap_idx


def get_cap(cap_idx: Dict[str, Dict[str, Any]], cap_id: str) -> Dict[str, Any]:
    return cap_idx[cap_id]


def validate_l2_parent(cap_idx: Dict[str, Dict[str, Any]], l2_id: str) -> List[str]:
    errs: List[str] = []
    cap = get_cap(cap_idx, l2_id)
    if cap.get("level") != "L2":
        errs.append(f"{l2_id} is referenced as L2 but its level is {cap.get('level')!r}.")
        return errs
    parent = cap.get("parent")
    if not isinstance(parent, str):
        errs.append(f"{l2_id} is L2 but has no valid 'parent' field.")
        return errs
    if parent not in cap_idx:
        errs.append(f"{l2_id} has parent={parent} but parent does not exist in BCM.")
        return errs
    if cap_idx[parent].get("level") != "L1":
        errs.append(f"{l2_id} has parent={parent} but parent is not L1 (level={cap_idx[parent].get('level')!r}).")
    return errs


def validate_focus_claims_rules(events_doc: Dict[str, Any], cap_idx: Dict[str, Dict[str, Any]], focus_l1: str) -> List[str]:
    errs: List[str] = []
    contracts = events_doc.get("event_contracts") or events_doc.get("event_contracts:")  # defensive
    if not isinstance(contracts, dict):
        return errs  # nothing to validate specifically

    # 1) produced_by_claims.events[].emitted_by_l2.id must be L2 parent==focus_l1
    produced = contracts.get("produced_by_claims") or contracts.get("produced_by")
    if isinstance(produced, dict):
        evts = produced.get("events")
        if isinstance(evts, list):
            for i, e in enumerate(evts):
                if not isinstance(e, dict):
                    continue
                ebl2 = e.get("emitted_by_l2")
                if not isinstance(ebl2, dict) or "id" not in ebl2:
                    continue
                l2_id = ebl2["id"]
                if not cap_exists(cap_idx, l2_id):
                    errs.append(f"$.event_contracts.produced_by_claims.events[{i}].emitted_by_l2.id={l2_id} does not exist in BCM.")
                    continue
                errs.extend([f"Event '{e.get('name', '?')}' emitted_by_l2: {msg}" for msg in validate_l2_parent(cap_idx, l2_id)])
                parent = get_cap(cap_idx, l2_id).get("parent")
                if parent != focus_l1:
                    errs.append(
                        f"Event '{e.get('name','?')}' emitted_by_l2.id={l2_id} has parent={parent}, expected parent={focus_l1}."
                    )

    # 2) subscriptions_handled_by_claims.subscriptions_by_producer_l1[].events[].handled_by_l2[].id must be L2 parent==focus_l1
    subs_root = contracts.get("subscriptions_handled_by_claims") or contracts.get("subscribed_by")
    if isinstance(subs_root, dict):
        subs_by_prod = subs_root.get("subscriptions_by_producer_l1") or subs_root.get("subscriptions")
        if isinstance(subs_by_prod, list):
            for pi, prod in enumerate(subs_by_prod):
                if not isinstance(prod, dict):
                    continue
                prod_events = prod.get("events")
                if not isinstance(prod_events, list):
                    continue
                for ei, ev in enumerate(prod_events):
                    if not isinstance(ev, dict):
                        continue
                    handled = ev.get("handled_by_l2")
                    if not isinstance(handled, list):
                        continue
                    for hi, h in enumerate(handled):
                        if not isinstance(h, dict) or "id" not in h:
                            continue
                        l2_id = h["id"]
                        if not cap_exists(cap_idx, l2_id):
                            errs.append(
                                f"$.event_contracts.subscriptions_handled_by_claims.subscriptions_by_producer_l1[{pi}].events[{ei}].handled_by_l2[{hi}].id={l2_id} does not exist in BCM."
                            )
                            continue
                        errs.extend([f"Subscription event '{ev.get('name','?')}' handled_by_l2: {msg}" for msg in validate_l2_parent(cap_idx, l2_id)])
                        parent = get_cap(cap_idx, l2_id).get("parent")
                        if parent != focus_l1:
                            errs.append(
                                f"Subscription event '{ev.get('name','?')}' handled_by_l2.id={l2_id} has parent={parent}, expected parent={focus_l1}."
                            )

    return errs


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Validate event YAML references against BCM capabilities.yaml (existence + L2 parent tree checks)."
    )
    ap.add_argument("--bcm", required=True, help="Path to BCM capabilities.yaml")
    ap.add_argument("--events", required=True, help="Path to events YAML to validate")
    ap.add_argument("--focus-l1", default="CAP.BSP.005", help="Focus L1 for Sinistres rules (default: CAP.BSP.005)")
    args = ap.parse_args()

    bcm_path = Path(args.bcm)
    events_path = Path(args.events)

    bcm = load_yaml(bcm_path)
    cap_idx = build_capability_index(bcm)

    events_doc = load_yaml(events_path)
    if not isinstance(events_doc, dict):
        print("[ERROR] Events YAML must be a mapping at the root.", file=sys.stderr)
        return 2

    errors: List[str] = []

    # A) global: every referenced 'id: CAP....' must exist
    for p, cap_id in iter_id_paths(events_doc):
        if not cap_exists(cap_idx, cap_id):
            errors.append(f"{p} references unknown capability id '{cap_id}'.")

    # B) if referenced capability is L2, validate parent exists and is L1
    #    (we do this for every referenced CAP id that happens to be L2)
    for p, cap_id in iter_id_paths(events_doc):
        if cap_exists(cap_idx, cap_id) and get_cap(cap_idx, cap_id).get("level") == "L2":
            for msg in validate_l2_parent(cap_idx, cap_id):
                errors.append(f"{p}: {msg}")

    # C) focus rules for Sinistres & Prestations structure
    errors.extend(validate_focus_claims_rules(events_doc, cap_idx, args.focus_l1))

    if errors:
        print(f"[FAIL] {len(errors)} issue(s) found:\n", file=sys.stderr)
        for e in errors:
            print(f" - {e}", file=sys.stderr)
        return 1

    print("[OK] No issues found. Event file is coherent with BCM capabilities and focus tree rules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
