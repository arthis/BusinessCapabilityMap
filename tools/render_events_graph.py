#!/usr/bin/env python3
# render_events_graph.py
#
# Build a capability hierarchy graph (L1/L2) + events produced/consumed from events.yaml
# Output: Graphviz DOT (+ optional SVG if 'dot' command exists)
#
# NEW: --focus-l2 to focus the graph on a single L2 capability

import argparse
import shutil
from pathlib import Path
from typing import Any, Dict, List, Tuple, Set

import yaml


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def build_cap_index(capabilities: List[dict]) -> Dict[str, dict]:
    idx = {}
    for c in capabilities:
        if isinstance(c, dict) and "id" in c:
            idx[c["id"]] = c
    return idx


def find_l1_l2_tree(cap_idx: Dict[str, dict]) -> Tuple[Dict[str, dict], Dict[str, List[dict]]]:
    """Return (l1_by_id, l2_by_parent_l1id)."""
    l1 = {}
    l2_by_parent = {}
    for cid, c in cap_idx.items():
        if c.get("level") == "L1":
            l1[cid] = c
    for cid, c in cap_idx.items():
        if c.get("level") == "L2":
            parent = c.get("parent")
            if isinstance(parent, str):
                l2_by_parent.setdefault(parent, []).append(c)
    return l1, l2_by_parent


def sanitize_id(s: str) -> str:
    return s.replace(".", "_").replace("-", "_").replace(" ", "_")


def dot_escape(label: str) -> str:
    return str(label).replace('"', '\\"')


def extract_events(events_doc: dict) -> List[dict]:
    """
    Extract produced events:
      event_contracts:
        produced_by_claims / produced_by:
          events: [...]
    Supports consumed_by or consumed_by_strict_bcm as consumers container.
    """
    contracts = events_doc.get("event_contracts", {})
    produced = contracts.get("produced_by_claims") or contracts.get("produced_by") or {}
    evts = produced.get("events", [])
    normalized = []
    for e in evts:
        if not isinstance(e, dict) or "name" not in e:
            continue
        emitted_by_l2 = e.get("emitted_by_l2") or {}
        consumed_by = e.get("consumed_by") or e.get("consumed_by_strict_bcm") or {}
        normalized.append(
            {
                "name": e["name"],
                "definition": e.get("definition", ""),
                "emitted_by_l2": {"id": emitted_by_l2.get("id"), "name": emitted_by_l2.get("name")},
                "consumed_by": {
                    "l1": consumed_by.get("l1", []) if isinstance(consumed_by.get("l1", []), list) else [],
                    "l2": consumed_by.get("l2", []) if isinstance(consumed_by.get("l2", []), list) else [],
                },
            }
        )
    return normalized


def extract_subscriptions(events_doc: dict) -> List[dict]:
    """
    Extract subscriptions (events produced elsewhere but consumed by claims side):
      event_contracts:
        subscriptions_handled_by_claims / subscribed_by:
          subscriptions_by_producer_l1 / subscriptions: [...]
    """
    contracts = events_doc.get("event_contracts", {})
    subs_root = contracts.get("subscriptions_handled_by_claims") or contracts.get("subscribed_by") or {}
    subs_list = subs_root.get("subscriptions_by_producer_l1") or subs_root.get("subscriptions") or []
    normalized = []
    for producer_block in subs_list:
        if not isinstance(producer_block, dict):
            continue
        producer = (
            producer_block.get("producer_l1")
            or producer_block.get("producer_capability")
            or producer_block.get("producer")
            or {}
        )
        prod_id = producer.get("id")
        prod_name = producer.get("name")
        events = producer_block.get("events", [])
        for e in events:
            if not isinstance(e, dict) or "name" not in e:
                continue
            handled = e.get("handled_by_l2") or []
            normalized.append(
                {
                    "producer_l1": {"id": prod_id, "name": prod_name},
                    "event": {"name": e["name"], "definition": e.get("definition", "")},
                    "handled_by_l2": handled,
                }
            )
    return normalized


def cap_name(cap_idx: Dict[str, dict], cap_id: str) -> str:
    c = cap_idx.get(cap_id) or {}
    return c.get("name") or cap_id


def is_l2(cap_idx: Dict[str, dict], cap_id: str) -> bool:
    return (cap_idx.get(cap_id) or {}).get("level") == "L2"


def l2_parent(cap_idx: Dict[str, dict], l2_id: str) -> str | None:
    c = cap_idx.get(l2_id) or {}
    parent = c.get("parent")
    return parent if isinstance(parent, str) else None


def main() -> int:
    ap = argparse.ArgumentParser(description="Render events.yaml + capabilities.yaml as a Graphviz graph (DOT + SVG).")
    ap.add_argument("--bcm", required=True, help="Path to capabilities.yaml")
    ap.add_argument("--events", required=True, help="Path to events.yaml")
    ap.add_argument("--out", default="events_graph", help="Output base name without extension (default: events_graph)")
    ap.add_argument("--focus-l1", default=None, help="Optional focus L1 (e.g. CAP.BSP.005)")
    ap.add_argument("--focus-l2", default=None, help="Optional focus L2 (e.g. CAP.BSP.DSP.000)")
    args = ap.parse_args()

    bcm_path = Path(args.bcm)
    events_path = Path(args.events)
    out_base = Path(args.out)

    bcm = load_yaml(bcm_path)
    events_doc = load_yaml(events_path)

    caps = bcm.get("capabilities", [])
    if not isinstance(caps, list):
        raise SystemExit("[ERROR] capabilities.yaml must contain a top-level 'capabilities:' list")

    cap_idx = build_cap_index(caps)
    l1_by_id, l2_by_parent = find_l1_l2_tree(cap_idx)

    produced_events_all = extract_events(events_doc)
    subscriptions_all = extract_subscriptions(events_doc)

    focus_l1 = args.focus_l1
    focus_l2 = args.focus_l2

    # ---- NEW: Focus logic ----
    # If focus_l2 is provided, validate it exists and is L2
    focus_l2_parent_l1 = None
    if focus_l2:
        if focus_l2 not in cap_idx:
            raise SystemExit(f"[ERROR] focus L2 not found in BCM: {focus_l2}")
        if not is_l2(cap_idx, focus_l2):
            raise SystemExit(f"[ERROR] focus capability is not L2: {focus_l2} (level={cap_idx[focus_l2].get('level')})")
        focus_l2_parent_l1 = l2_parent(cap_idx, focus_l2)

    # If both focus_l1 and focus_l2 are provided, ensure consistency
    if focus_l1 and focus_l2 and focus_l2_parent_l1 and focus_l2_parent_l1 != focus_l1:
        raise SystemExit(
            f"[ERROR] focus-l2 parent mismatch: {focus_l2} parent={focus_l2_parent_l1} but focus-l1={focus_l1}"
        )

    # Filter events/subscriptions depending on focus
    produced_events = produced_events_all
    subscriptions = subscriptions_all

    if focus_l2:
        # Keep only produced events emitted by that L2
        produced_events = [
            e for e in produced_events_all
            if isinstance(e.get("emitted_by_l2", {}).get("id"), str) and e["emitted_by_l2"]["id"] == focus_l2
        ]
        # Keep only subscription events handled by that L2
        subs_filtered = []
        for s in subscriptions_all:
            handled = s.get("handled_by_l2") or []
            if any(isinstance(h, dict) and h.get("id") == focus_l2 for h in handled):
                subs_filtered.append(s)
        subscriptions = subs_filtered

        # If focus_l1 not specified, set it automatically to parent L1 to keep the cluster context
        if not focus_l1 and focus_l2_parent_l1:
            focus_l1 = focus_l2_parent_l1

    # If focus_l1 is provided (and no focus_l2), you may want to restrict to only that L1 tree + related L1s.
    # We keep a "contextual" view: show focus L1 tree plus other L1/L2 linked by event edges.
    # (No extra filtering needed beyond relevant-node selection.)

    # ---- Collect relevant capability IDs to show ----
    relevant_l1_ids: Set[str] = set()
    relevant_l2_ids: Set[str] = set()

    # Always include focus L1 tree, if any
    if focus_l1 and focus_l1 in l1_by_id:
        relevant_l1_ids.add(focus_l1)
        for l2 in l2_by_parent.get(focus_l1, []):
            relevant_l2_ids.add(l2["id"])

    # If focusing a single L2, include only that L2 (and not all L2s under the parent L1)
    if focus_l2:
        relevant_l2_ids = {focus_l2}
        if focus_l2_parent_l1:
            relevant_l1_ids.add(focus_l2_parent_l1)

    # From produced events: emitter L2 and consumers L1/L2
    for e in produced_events:
        emitter_l2 = e.get("emitted_by_l2", {}).get("id")
        if isinstance(emitter_l2, str):
            relevant_l2_ids.add(emitter_l2)
            parent = l2_parent(cap_idx, emitter_l2)
            if isinstance(parent, str):
                relevant_l1_ids.add(parent)

        for c in e["consumed_by"]["l1"]:
            if isinstance(c, dict) and isinstance(c.get("id"), str):
                relevant_l1_ids.add(c["id"])
        for c in e["consumed_by"]["l2"]:
            if isinstance(c, dict) and isinstance(c.get("id"), str):
                relevant_l2_ids.add(c["id"])
                parent = l2_parent(cap_idx, c["id"])
                if isinstance(parent, str):
                    relevant_l1_ids.add(parent)

    # From subscriptions: producer L1 + handled_by L2
    for s in subscriptions:
        prod_id = s["producer_l1"].get("id")
        if isinstance(prod_id, str):
            relevant_l1_ids.add(prod_id)
        for h in s.get("handled_by_l2", []):
            if isinstance(h, dict) and isinstance(h.get("id"), str):
                relevant_l2_ids.add(h["id"])
                parent = l2_parent(cap_idx, h["id"])
                if isinstance(parent, str):
                    relevant_l1_ids.add(parent)

    # ---- Build DOT ----
    dot_lines: List[str] = []
    dot_lines.append("digraph EventsBCM {")
    dot_lines.append('  graph [rankdir="LR", compound=true, fontsize=10];')
    dot_lines.append('  node  [fontsize=10];')
    dot_lines.append('  edge  [fontsize=9];')

    # L1 clusters
    for l1_id in sorted(relevant_l1_ids):
        l1_cap = cap_idx.get(l1_id)
        if not l1_cap:
            continue
        l1_label = f"{cap_name(cap_idx, l1_id)}\\n({l1_id})"
        cluster_name = f"cluster_{sanitize_id(l1_id)}"
        dot_lines.append(f'  subgraph {cluster_name} {{')
        dot_lines.append('    style="rounded";')
        dot_lines.append(f'    label="{dot_escape(l1_label)}";')

        l1_node = sanitize_id(l1_id)
        dot_lines.append(f'    "{l1_node}" [shape="box", penwidth=2];')

        # L2 nodes under this L1
        for l2 in sorted(l2_by_parent.get(l1_id, []), key=lambda x: x.get("id", "")):
            l2_id = l2.get("id")
            if not isinstance(l2_id, str):
                continue
            if l2_id not in relevant_l2_ids:
                continue
            l2_node = sanitize_id(l2_id)
            l2_label = f"{l2.get('name', l2_id)}\\n({l2_id})"
            dot_lines.append(f'    "{l2_node}" [shape="box", label="{dot_escape(l2_label)}"];')
            dot_lines.append(f'    "{l1_node}" -> "{l2_node}" [style="dashed", arrowhead="none"];')

        dot_lines.append("  }")

    # Produced event nodes + edges
    for e in produced_events:
        ev_name = e["name"]
        ev_node = sanitize_id(f"EVT_{ev_name}")
        dot_lines.append(f'  "{ev_node}" [shape="ellipse", label="{dot_escape(ev_name)}"];')

        emitter_l2 = e.get("emitted_by_l2", {}).get("id")
        if isinstance(emitter_l2, str):
            emitter_node = sanitize_id(emitter_l2)
            dot_lines.append(f'  "{emitter_node}" -> "{ev_node}" [label="produit"];')

        for c in e["consumed_by"]["l1"]:
            if not (isinstance(c, dict) and isinstance(c.get("id"), str)):
                continue
            c_node = sanitize_id(c["id"])
            dot_lines.append(f'  "{ev_node}" -> "{c_node}" [label="consommé"];')

        for c in e["consumed_by"]["l2"]:
            if not (isinstance(c, dict) and isinstance(c.get("id"), str)):
                continue
            c_node = sanitize_id(c["id"])
            dot_lines.append(f'  "{ev_node}" -> "{c_node}" [label="consommé"];')

    # Subscription event nodes + edges
    for s in subscriptions:
        ev_name = s["event"]["name"]
        ev_node = sanitize_id(f"SUB_{ev_name}")
        dot_lines.append(f'  "{ev_node}" [shape="ellipse", label="{dot_escape(ev_name)}\\n(subscription)"];')

        prod_id = s["producer_l1"].get("id")
        if isinstance(prod_id, str):
            prod_node = sanitize_id(prod_id)
            dot_lines.append(f'  "{prod_node}" -> "{ev_node}" [label="produit"];')

        # If focus_l2 is set, draw only edges to that L2 (avoid clutter)
        for h in s.get("handled_by_l2", []):
            if not (isinstance(h, dict) and isinstance(h.get("id"), str)):
                continue
            if focus_l2 and h["id"] != focus_l2:
                continue
            h_node = sanitize_id(h["id"])
            dot_lines.append(f'  "{ev_node}" -> "{h_node}" [label="consommé"];')

    dot_lines.append("}")

    dot_path = out_base.with_suffix(".dot")
    dot_path.write_text("\n".join(dot_lines), encoding="utf-8")
    print(f"[OK] DOT generated: {dot_path}")

    # Render SVG if graphviz installed
    if shutil.which("dot"):
        import subprocess

        svg_path = out_base.with_suffix(".svg")
        subprocess.run(["dot", "-Tsvg", str(dot_path), "-o", str(svg_path)], check=True)
        print(f"[OK] SVG rendered: {svg_path}")
    else:
        print("[WARN] Graphviz 'dot' command not found. Install Graphviz to render SVG/PNG, or use the .dot file manually.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
