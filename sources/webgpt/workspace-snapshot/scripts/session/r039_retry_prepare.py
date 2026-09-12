#!/usr/bin/env python3
"""Preserve the failed dry-run and create a new immutable checkpoint session.
The initial research SESSION is retained; never overwrite/delete it to satisfy the engine.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
def main():
 p=ROOT/'scripts/session/r039_checkpoint.py';text=p.read_text()
 failure=dict(status='DRY_RUN_REJECTED',error='SESSION_RECORD_REQUIRED',observed_via='container.exec tool response of first r039_checkpoint.py execution',original_script_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),recorded_utc=datetime.now(timezone.utc).isoformat(),state_writes=False,resolution='Create a new checkpoint session instead of overwriting the precommitted research session; preserve both originals and failed payload.')
 f=ROOT/'artifacts/r039/checkpoint/FAILURE.json'
 if f.exists():raise FileExistsError(f)
 f.write_text(json.dumps(failure,ensure_ascii=False,indent=2)+'\n')
 text=text.replace("SID='S-RES-20260911-039-SILENT-STEPS';CID='P-SILENT-STEPS-039';S=P+'sessions/'+SID+'/'", "SID='S-RES-20260911-039-SILENT-STEPS-CHECKPOINT';CID='P-SILENT-STEPS-039';S=P+'sessions/'+SID+'/'\nORIG=P+'sessions/S-RES-20260911-039-SILENT-STEPS/'")
 text=text.replace("OUT=ROOT/'artifacts/r039/checkpoint'", "OUT=ROOT/'artifacts/r039/checkpoint_retry'")
 text=text.replace("session_sources=[S+'REQUEST.md',S+'RESEARCH_DELTA.md','artifacts/r039/COGNITION_STATUS.json','artifacts/r039/START.json']", "session_sources=[ORIG+'REQUEST.md',ORIG+'RESEARCH_DELTA.md',ORIG+'SESSION.md','artifacts/r039/COGNITION_STATUS.json','artifacts/r039/START.json','artifacts/r039/checkpoint/FAILURE.json']\n session=(ROOT/(ORIG+'SESSION.md')).read_text()+'\\n## 原子交接\\n\\n此独立checkpoint Session保留先行研究SESSION原字节；首轮dry-run因未包含新SESSION被拒，未写状态；本次按原引擎新建此不可覆盖记录。\\n'")
 text=text.replace("'source_hashes':{p:sha(ROOT/p) for p in [S+'SESSION.md']+session_sources}","'source_hashes':{**{p:sha(ROOT/p) for p in session_sources},S+'SESSION.md':hashlib.sha256(session.encode()).hexdigest()}")
 text=text.replace("request_path=S+'REQUEST.md'", "request_path=ORIG+'REQUEST.md'")
 text=text.replace("P+'STATE.json':dump(state)}", "P+'STATE.json':dump(state),S+'SESSION.md':session}")
 text=text.replace("'expected_sha256':sha(ROOT/p)}", "'expected_sha256':sha(ROOT/p) if (ROOT/p).exists() else None}")
 out=ROOT/'scripts/session/r039_checkpoint_v2.py'
 if out.exists():raise FileExistsError(out)
 out.write_text(text)
 print('Prepared new session; initial immutable research record and failed script preserved.')
if __name__=='__main__':main()
