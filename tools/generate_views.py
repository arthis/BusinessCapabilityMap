from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
CAPS_FILE = ROOT / "bcm" / "capabilities.yaml"

OUT_BCM = ROOT / "views" / "bcm-l1l2.mmd"
OUT_HEAT = ROOT / "views" / "bcm-l1l2-heatmap.mmd"
OUT_TRACE = ROOT / "views" / "adr-traceability.md"

def load_caps():
    data = yaml.safe_load(CAPS_FILE.read_text(encoding="utf-8"))
    caps = data["capabilities"]
    by_id = {c["id"]: c for c in caps}
    return caps, by_id

def is_l1(c): return c["level"] == "L1"
def is_l2(c): return c["level"] == "L2"

def mermaid_escape(s: str) -> str:
    # Mermaid can be picky with quotes; keep simple
    return s.replace('"', "'")

def render_bcm_l1l2(caps, by_id):
    l1 = [c for c in caps if is_l1(c)]
    l2 = [c for c in caps if is_l2(c)]

    # subgraphs per L1 (nice for capability map-like view)
    lines = [
        "flowchart LR",
        "%% BCM L1/L2 (auto-generated)",
        "%% Each L1 is a subgraph; L2 are nodes inside",
        ""
    ]

    # Create a stable ordering: by id
    for c1 in sorted(l1, key=lambda x: x["id"]):
        sid = c1["id"].replace(".", "_")
        title = mermaid_escape(c1["name"])
        lines.append(f"subgraph {sid}[\"{c1['id']} — {title}\"]")
        lines.append("direction TB")
        # L2 children
        children = [c for c in l2 if c.get("parent") == c1["id"]]
        for ch in sorted(children, key=lambda x: x["id"]):
            nid = ch["id"].replace(".", "_")
            name = mermaid_escape(ch["name"])
            lines.append(f'{nid}["{ch["id"]} — {name}"]')
        lines.append("end")
        lines.append("")

    return "\n".join(lines)

def render_bcm_heatmap(caps, by_id):
    # Same as bcm-l1l2, but styles based on maturity (1..5)
    l1l2 = [c for c in caps if c["level"] in ("L1", "L2")]

    # Define 5 classes; you can later replace with your color conventions in a Mermaid-compatible renderer.
    # NOTE: Mermaid supports classDef; many renderers accept fill/stroke colors.
    lines = [
        "flowchart LR",
        "%% BCM L1/L2 Heatmap by maturity (auto-generated)",
        ""
        "classDef m1 fill:#f8f9fa,stroke:#adb5bd,color:#212529;",
        "classDef m2 fill:#e9ecef,stroke:#adb5bd,color:#212529;",
        "classDef m3 fill:#dee2e6,stroke:#6c757d,color:#212529;",
        "classDef m4 fill:#ced4da,stroke:#495057,color:#212529;",
        "classDef m5 fill:#adb5bd,stroke:#343a40,color:#212529;",
        ""
    ]

    # Render like the other view
    l1 = [c for c in caps if is_l1(c)]
    l2 = [c for c in caps if is_l2(c)]

    for c1 in sorted(l1, key=lambda x: x["id"]):
        sid = c1["id"].replace(".", "_")
        title = mermaid_escape(c1["name"])
        lines.append(f"subgraph {sid}[\"{c1['id']} — {title}\"]")
        lines.append("direction TB")
        children = [c for c in l2 if c.get("parent") == c1["id"]]
        for ch in sorted(children, key=lambda x: x["id"]):
            nid = ch["id"].replace(".", "_")
            name = mermaid_escape(ch["name"])
            maturity = (ch.get("heatmap", {}) or {}).get("maturity", 1)
            maturity = maturity if maturity in (1,2,3,4,5) else 1
            lines.append(f'{nid}["{ch["id"]} — {name}"]:::m{maturity}')
        lines.append("end\n")

    return "\n".join(lines)

def render_traceability_md(caps):
    # Table capability -> ADRs
    l2 = [c for c in caps if c["level"] == "L2"]
    lines = [
        "# Traçabilité ADR ↔ Capabilities",
        "",
        "## Capabilities (L2) → ADR",
        "",
        "| Capability | Zoning | Maturity | ADRs |",
        "|---|---:|---:|---|",
    ]
    for c in sorted(l2, key=lambda x: x["id"]):
        hm = c.get("heatmap", {}) or {}
        maturity = hm.get("maturity", "")
        adrs = c.get("adrs", []) or []
        adrs_str = "<br/>".join(adrs) if adrs else ""
        lines.append(f"| `{c['id']}` {c['name']} | {c.get('zoning','')} | {maturity} | {adrs_str} |")
    lines.append("")
    lines.append("## Rappel")
    lines.append("- Les ADR de cadre (GOV/MOD/ZON/DOM/MAP) décrivent les règles globales.")
    lines.append("- Les ADR CAP décrivent les arbitrages (split/merge/placement) sur des capacités structurantes ou litigieuses.")
    return "\n".join(lines)

def main():
    (ROOT / "views").mkdir(exist_ok=True)
    caps, by_id = load_caps()

    OUT_BCM.write_text(render_bcm_l1l2(caps, by_id), encoding="utf-8")
    OUT_HEAT.write_text(render_bcm_heatmap(caps, by_id), encoding="utf-8")
    OUT_TRACE.write_text(render_traceability_md(caps), encoding="utf-8")

    print("[OK] Generated:")
    print(f"- {OUT_BCM}")
    print(f"- {OUT_HEAT}")
    print(f"- {OUT_TRACE}")

if __name__ == "__main__":
    main()
