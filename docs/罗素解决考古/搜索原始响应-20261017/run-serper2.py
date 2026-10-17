#!/usr/bin/env python3
import json, subprocess, urllib.request, urllib.error
from datetime import datetime, timezone
U = subprocess.run(["whoami"], capture_output=True, text=True).stdout.strip()
K = subprocess.run(["security","find-generic-password","-a",U,"-s","codex-search-serper","-w"],
                   capture_output=True, text=True).stdout.strip()
Q = [
 ("q5-a01-web","search",'Moore 1978 origins Zermelo axiomatization abstract motivation well-ordering'),
 ("q5-a02-web","search",'"Zermelo" 1908 "Russell\'s paradox" Moore "not primarily motivated"'),
 ("q6-a01-web","search",'Kunen set theory 1980 Russell paradox separation avoids textbook'),
 ("q6-a02-web","search",'Jech Set Theory Russell paradox "no universal set" separation'),
 ("q3-a03-web","search",'"naive comprehension" OR "unrestricted comprehension" term coined who first'),
 ("q3-a04-web","search",'Zermelo 1908 "Aussonderung" axiom purpose paradoxes secondary Kanamori'),
 ("q1-a04-web","search",'Zermelo 1908 "beseitigt" OR "verschwinden" Russell Antinomie German text'),
 ("q4-a02-web","search",'Zermelo 1930 "Fundierung" axiom cumulative hierarchy first appeared'),
 ("q3-s03-sch","scholar",'Moore origins Zermelo axiomatization well-ordering paradoxes motivation'),
 ("q1-s02-sch","scholar",'Zermelo 1908 Untersuchungen Russell Antinomie beseitigt'),
]
def run(n,ep,q):
    body = json.dumps({"q":q,"num":10,"page":1}).encode()
    req = urllib.request.Request(f"https://google.serper.dev/{ep}", data=body,
        headers={"X-API-KEY":K,"Content-Type":"application/json"})
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        with urllib.request.urlopen(req, timeout=45) as r: c,raw,h = r.status, r.read().decode(errors="replace"), r.getheaders()
    except urllib.error.HTTPError as e: c,raw,h = e.code, e.read().decode(errors="replace"), e.headers.items()
    except Exception as e: print(f"== {n} ERR {e}"); return
    open(f"{n}-response.json","w").write(raw); open(f"{n}-headers.txt","w").write(f"# {ts} UTC HTTP {c}\n")
    open("ledger.tsv","a").write(f"{ts}\t{n}\t{ep}\t{q}\t{c}\n")
    print(f"\n== {n} [{ep}] {q!r} -> {c}")
    try:
        for i,x in enumerate(json.loads(raw).get("organic",[])[:5],1):
            print(f"  {i}. {x.get('title','')[:88]} | {x.get('link','')}")
        if not json.loads(raw).get("organic"): print("  (0 results)")
    except Exception as ex: print("  parse:", ex)
for n,ep,q in Q: run(n,ep,q)
print("\nROUND2 DONE")
