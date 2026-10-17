#!/usr/bin/env python3
"""run-serper.py — 罗素解决考古 步骤2 检索底账驱动器（Serper /search + /scholar）.
Key 从 macOS Keychain 读入内存，绝不打印或落盘。原始响应与响应头按 <name>-*.json/.txt 落盘，
账本行追加 ledger.tsv（UTC 时间戳、HTTP 状态、限速头）。"""
import json, subprocess, sys, urllib.request, urllib.error
from datetime import datetime, timezone

USER = subprocess.run(["whoami"], capture_output=True, text=True).stdout.strip()
KEY = subprocess.run(["security", "find-generic-password", "-a", USER, "-s", "codex-search-serper", "-w"],
                     capture_output=True, text=True).stdout.strip()
if not KEY:
    print("FATAL: codex-search-serper key not found in Keychain"); sys.exit(1)

QUERIES = [
    ("q1-a01-web", "search", 'Zermelo 1908 Russell paradox "solved"'),
    ("q1-a02-web", "search", 'Zermelo 1908 Ausschließung Widersprüche Mengenlehre'),
    ("q1-a03-web", "search", 'Zermelo Aussonderung 1908 Antinomie Russell'),
    ("q2-a01-web", "search", 'how does ZFC solve Russell paradox'),
    ("q2-a02-web", "search", 'Enderton "Elements of Set Theory" Russell paradox axiom'),
    ("q3-a01-web", "search", '"unrestricted comprehension" origin of the term'),
    ("q3-a02-web", "search", 'Zermelo 1908 motivation well-ordering theorem not paradox Moore origins'),
    ("q4-a01-web", "search", 'axiom of foundation history Mirimanoff von Neumann Zermelo 1930'),
    ("q1-s01-sch", "scholar", 'Zermelo Untersuchungen Grundlagen Mengenlehre 1908 Antinomien'),
    ("q2-s01-sch", "scholar", 'Russell paradox Zermelo axiomatization response history'),
    ("q3-s01-sch", "scholar", 'Moore origins Zermelo axiomatization set theory 1978'),
    ("q3-s02-sch", "scholar", 'unrestricted comprehension schema terminology history'),
    ("q4-s01-sch", "scholar", 'Zermelo 1930 Grenzzahlen Mengenbereiche Fundierung'),
    ("q4-s02-sch", "scholar", 'von Neumann 1925 Axiomatisierung der Mengenlehre'),
]

def run(name, endpoint, q):
    body = json.dumps({"q": q, "num": 10, "page": 1}).encode()
    req = urllib.request.Request(f"https://google.serper.dev/{endpoint}", data=body,
        headers={"X-API-KEY": KEY, "Content-Type": "application/json"})
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    code, raw, hdrs = 0, "", []
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            code, raw, hdrs = r.status, r.read().decode(errors="replace"), r.getheaders()
    except urllib.error.HTTPError as e:
        code, raw, hdrs = e.code, e.read().decode(errors="replace"), e.headers.items()
    except Exception as e:
        print(f"== {name} TRANSPORT-ERROR {e}"); return
    with open(f"{name}-response.json", "w") as f: f.write(raw)
    with open(f"{name}-headers.txt", "w") as f:
        f.write(f"# fetched {ts} UTC, HTTP {code}\n" + "\n".join(f"{k}: {v}" for k, v in hdrs))
    rl = {k: v for k, v in hdrs if "ratelimit" in k.lower()}
    with open("ledger.tsv", "a") as f:
        f.write(f"{ts}\t{name}\t{endpoint}\t{q}\t{code}\t{json.dumps(rl)}\n")
    print(f"\n== {name} [{endpoint}] {q!r} -> HTTP {code}  rl={rl}")
    try:
        org = json.loads(raw).get("organic", [])
        for i, h in enumerate(org[:6], 1):
            print(f"  {i}. {h.get('title','')[:95]} | {h.get('link','')}")
        if not org: print("  (no organic results) raw[:240]:", raw[:240])
    except Exception as ex:
        print(f"  PARSE-ERROR {ex}; raw[:240]: {raw[:240]}")

for n, ep, q in QUERIES: run(n, ep, q)
print("\nDONE", len(QUERIES), "queries")
