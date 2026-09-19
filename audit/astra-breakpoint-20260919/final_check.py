#!/usr/bin/env python3
"""Final artifact checks, explicitly excluding certification of the open mathematics."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
TOPIC=ROOT/"Astra继续尝试/断点与证明机制系统检查"

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    failures=[];links=0
    docs=[TOPIC/"README.md",TOPIC/"第一轮执行报告.md",*sorted((TOPIC/"第一轮执行报告").glob("*.md")),TOPIC/"系统化后续检查方案.md",*sorted((TOPIC/"系统化后续检查方案").glob("*.md"))]
    for p in docs:
        for a,b in re.findall(r"\]\((?:<([^>]+)>|([^\s)]+))\)",p.read_text()):
            target=unquote(a or b).split("#",1)[0]
            if not target or "://" in target or target.startswith("mailto:"):continue
            links+=1
            if not (p.parent/target).resolve().exists():failures.append("MISSING_LINK:"+str(p)+":"+target)
    runpaths=sorted(list((ROOT/"HoTT/verification/runs").glob("20260919-MP-ASTRA-*/RUN.json"))+list((ROOT/"HoTT/verification/runs").glob("20260919-ASTRA-CLI-*/RUN.json")))
    for p in runpaths:
        r=json.loads(p.read_text())
        fields=r.get("artifacts") or [r[k] for k in ("stdout","stderr","environment","source_manifest")]
        for v in fields:
            f=Path(v["path"]);f=f if f.is_absolute() else p.parent/f
            if not f.exists() or len(f.read_bytes())!=v["bytes"] or sha(f)!=v["sha256"]:failures.append("RUN_ARTIFACT:"+str(f))
    tracking=json.loads((ROOT/".codex/cognition/HEAD.json").read_text())
    drift=[p for p,h in tracking["tracked"].items() if sha(ROOT/p)!=h]
    if drift:failures.append("TRACKING_DRIFT:"+str(drift))
    state=json.loads((ROOT/".codex/research/hott/STATE.json").read_text())
    assert state["revision"]==174
    receipt=json.loads((ROOT/".codex/cognition/checkpoints/S-RES-20260919-ASTRA-BREAKPOINT-01/result.json").read_text())
    assert receipt["status"]=="CHECKPOINT_COMMITTED"
    env=json.loads((OUT/"bounded-envelope.json").read_text());members=env["members"]
    keys={(tuple(x["word"]),tuple(x["function_false_true"])) for x in members}
    assert len(keys)==len(members)==4*sum(2**n for n in range(4))==60
    assert sha(ROOT/"HoTT/formal/astra-breakpoint-check/BoundedConsumers.agda")==env["source_sha256"]
    original=json.loads((TOPIC/"evidence/对话逐字核验-003.json").read_text());assert original["status"]=="PASS" and original["messages"]==44
    payload={"schema":"astra-final-artifact-check/v1","status":"PASS_WITH_SCOPE" if not failures else "FAIL","failures":failures,"links_checked":links,"run_receipts":len(runpaths),"state_revision":state["revision"],"tracked_mismatches":drift,"bounded_members":60,"bounded_remainder":0,"dialogue_messages":44,"not_certified":["global proof delivery gate","geometric restoration bridge","HoTT inconsistency","version closed Git publication","model understanding"]}
    (OUT/"final-artifact-check.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(payload,ensure_ascii=False));return bool(failures)

if __name__=="__main__":raise SystemExit(main())
