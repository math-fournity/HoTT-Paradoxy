#!/usr/bin/env python3
import json, subprocess, urllib.request
from datetime import datetime, timezone
U = subprocess.run(["whoami"], capture_output=True, text=True).stdout.strip()
K = subprocess.run(["security","find-generic-password","-a",U,"-s","codex-search-exa","-w"],
                   capture_output=True, text=True).stdout.strip()
Q = [
 ("e1","Zermelo 1908 axiomatization motivation well-ordering theorem versus paradoxes Moore"),
 ("e2","who first called it the Russell-Zermelo paradox independent discovery 1902"),
 ("e3","ZFC solves Russell paradox textbooks claim critical history of the narrative"),
 ("e4","Zermelo 1908 Aussonderung axiom what it actually proves no universal set"),
 ("e5","axiom of foundation 1930 Zermelo cumulative hierarchy Mirimanoff 1917 von Neumann 1925"),
]
def run(n,q):
    body = json.dumps({"query":q,"type":"auto","numResults":8}).encode()
    req = urllib.request.Request("https://api.exa.ai/search", data=body,
        headers={"x-api-key":K,"Content-Type":"application/json"})
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        with urllib.request.urlopen(req, timeout=60) as r: raw, code = r.read().decode(errors="replace"), r.status
    except Exception as e:
        print(f"== {n} ERROR {e}"); return
    open(f"{n}-exa.json","w").write(raw)
    open("ledger-exa.tsv","a").write(f"{ts}\t{n}\t{q}\t{code}\n")
    print(f"\n== {n} [{code}] {q}")
    try:
        for i,h in enumerate(json.loads(raw).get("results",[])[:6],1):
            print(f"  {i}. {h.get('title','')[:90]} | {h.get('url','')}")
    except Exception as ex: print("  parse:", ex, raw[:200])
for n,q in Q: run(n,q)
print("\nDONE")
