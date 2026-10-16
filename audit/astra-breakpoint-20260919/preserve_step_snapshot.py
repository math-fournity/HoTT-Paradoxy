#!/usr/bin/env python3
"""Save an exact candidate commit with a private index; never reset or update main.

The shared main worktree remains the canonical runtime work surface. This ref is
an immutable recovery snapshot, not a second active worktree or current STATE.
"""
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
REF="refs/heads/codex/astra-restoration-snapshot-20260919"

def git(*args,env=None):
    r=subprocess.run(["git",*args],cwd=ROOT,env=env,capture_output=True)
    if r.returncode:raise RuntimeError(r.stderr.decode()+r.stdout.decode())
    return r.stdout

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    assert not subprocess.run(["git","show-ref","--verify","--quiet",REF],cwd=ROOT).returncode==0,"REF_EXISTS"
    base=git("rev-parse","HEAD").decode().strip()
    shared=ROOT/git("rev-parse","--git-path","index").decode().strip()
    shared_before=sha(shared)
    scope=json.loads((OUT/"step-version-scope.json").read_text())
    paths={row["path"] for row in scope["paths"]}
    for folder in [OUT,ROOT/"Astra继续尝试/断点与证明机制系统检查"]:
        paths.update(str(p.relative_to(ROOT)) for p in folder.rglob("*") if p.is_file() and p.suffix in (".agda",".md",".json",".txt",".py",".diff"))
    # The generated private-index review is filled before final staging below.
    paths.discard("audit/astra-breakpoint-20260919/private-snapshot-receipt.json")
    rows={p:sha(ROOT/p) for p in sorted(paths)}
    with tempfile.TemporaryDirectory(prefix="astra-version-index-",dir="/Volumes/D/HoTT-toolchain-cache/tmp") as temp:
        env=os.environ.copy();env["GIT_INDEX_FILE"]=str(Path(temp)/"index")
        git("read-tree",base,env=env)
        git("add","--",*sorted(paths),env=env)
        check=subprocess.run(["git","diff","--cached","--check"],cwd=ROOT,env=env,capture_output=True)
        raw=check.stdout+check.stderr
        flagged=[]
        for line in raw.decode().splitlines():
            m=re.match(r"(.+?):\d+: (?:trailing whitespace|new blank line at EOF)\.",line)
            if m:flagged.append(m.group(1))
        allowed=lambda p: (p.startswith(".codex/cognition/checkpoints/") and ("/before/" in p or "/after/" in p)) or p.startswith("Astra继续尝试/断点与证明机制系统检查/原始消息/") or p.startswith("Astra继续尝试/断点与证明机制系统检查/对话原文/") or p.startswith("Astra继续尝试/断点与证明机制系统检查/evidence/") or p in ("HoTT/formal/astra-breakpoint-check/BoundedConsumers.agda","audit/astra-breakpoint-20260919/tracking-recovery/accepted.diff") or p.startswith("audit/astra-breakpoint-20260919/attempt-sources/")
        unknown=sorted({p for p in flagged if not allowed(p)})
        if unknown:raise RuntimeError("UNCLASSIFIED_WHITESPACE:"+str(unknown))
        (OUT/"private-index-whitespace.txt").write_bytes(raw)
        review={"exit_code":check.returncode,"diagnostics":len(flagged),"unique_paths":len(set(flagged)),"unclassified":unknown,"reason":"Byte-pinned snapshots, original dialogue, captured raw diff and already checked generated source are preserved; whitespace is disclosed, not silently reformatted or scored as a clean diff.","base":base}
        (OUT/"private-index-review.json").write_text(json.dumps(review,ensure_ascii=False,indent=2)+"\n")
        extra=["audit/astra-breakpoint-20260919/private-index-whitespace.txt","audit/astra-breakpoint-20260919/private-index-review.json"]
        git("add","--",*extra,env=env);paths.update(extra)
        for p in extra:rows[p]=sha(ROOT/p)
        assert all(sha(ROOT/p)==h for p,h in rows.items()),"WORKING_SOURCE_DRIFT"
        tree=git("write-tree",env=env).decode().strip()
        commit=git("commit-tree",tree,"-p",base,"-m","BP-GEO-RESTORE-01(step-1): 原生自然恢复与依赖/运行/检查点的独立恢复快照; reflection=revised-in 7900d644",env=env).decode().strip()
        git("update-ref",REF,commit,"0"*40)
    current=git("rev-parse","HEAD").decode().strip()
    shared_after=sha(shared)
    actual={p.decode() for p in git("diff-tree","--no-commit-id","--name-only","-r","-z",commit).split(b"\0") if p}
    assert not actual-paths,"UNEXPECTED_COMMIT_PATH"
    mismatches=[]
    for p,h in rows.items():
        if hashlib.sha256(git("show",commit+":"+p)).hexdigest()!=h:mismatches.append(p)
    assert not mismatches,mismatches
    result={"schema":"astra-private-index-snapshot/v1","status":"CANDIDATE_RECOVERY_SNAPSHOT_VERIFIED","ref":REF,"commit":commit,"tree":tree,"parent":base,"observed_main_after":current,"main_unchanged_during_snapshot":current==base,"shared_index_before":shared_before,"shared_index_after":shared_after,"shared_index_unchanged":shared_before==shared_after,"snapshot_files_verified":len(rows),"changed_paths":len(actual),"scope":"Exact owned working files and their already-canonical checkpoints; no main merge, current-state reallocation, reset, push or tag.","prior_race":"Interleaved shared-index dev-note commit/reset left the planned files uncommitted; 2b0b27a contains only review metadata.","whitespace":review}
    (OUT/"private-snapshot-receipt.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False))

if __name__=="__main__":main()
