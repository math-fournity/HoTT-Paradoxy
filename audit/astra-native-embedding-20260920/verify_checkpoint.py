#!/usr/bin/env python3
"""Read the real canonical checkpoint and verify its current managed bytes."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-NATIVE-EMBEDDING';rel='.codex/cognition/checkpoints/'+SID+'/result.json'
raw=(ROOT/rel).read_bytes();result=json.loads(raw);assert result['status']=='CHECKPOINT_COMMITTED' and result['revision']==201
state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text());assert state['revision']==201 and state['latest_session']==SID
head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in head['tracked'].items())
p=subprocess.run(['python3','-B','scripts/audit/verify_three_way_cognition.py'],cwd=ROOT,capture_output=True)
(OUT/'three-way.stdout.txt').write_bytes(p.stdout);(OUT/'three-way.stderr.txt').write_bytes(p.stderr);assert p.returncode==0,p.stdout.decode()+p.stderr.decode()
receipt={'canonical_result':rel,'canonical_result_sha256':hashlib.sha256(raw).hexdigest(),'canonical_status':result['status'],'revision':201,'latest_session':SID,'tracked_hashes_match':len(head['tracked']),'three_way_exit':p.returncode,'full_motion_task':'OPEN','parent_goal':'OPEN','legacy_kc_bundle_gap':'G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001'}
(OUT/'POST-CHECKPOINT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
