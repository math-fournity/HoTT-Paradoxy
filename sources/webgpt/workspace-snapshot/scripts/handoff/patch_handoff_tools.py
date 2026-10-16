#!/usr/bin/env python3
"""One-time, pre-checkpoint corrections discovered by reading the real runtime contracts."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
p=R/'scripts/handoff/finalize_package.py';s=p.read_text();s=s.replace("r.get('relative_path',r.get('path'))","r.get('relative',r.get('relative_path',r.get('path')))")
p.write_text(s)
p=R/'scripts/handoff/verify_package.py';s=p.read_text().replace('import argparse,hashlib,json,subprocess,sys','import argparse,hashlib,json,subprocess,sys,os')
s=s.replace('capture_output=True,text=True)','capture_output=True,text=True,env={**os.environ, "GIT_OPTIONAL_LOCKS":"0", "GIT_CONFIG_NOSYSTEM":"1", "GIT_CONFIG_GLOBAL":os.devnull, "GIT_NO_REPLACE_OBJECTS":"1"})')
p.write_text(s)
p=R/'governance/WORKFLOW.md';s=p.read_text().replace('先保存不可覆盖 Session 及研究文件，再重新读取当前计划作为**本次写回基线**。','先保存研究正文、源码与实际证据，再重新读取当前计划作为**本次写回基线**。本轮新的 `sessions/<ID>/SESSION.md` 正文放在 checkpoint payload 中，由原子写入一次创建；不要先在目标路径创建同名 SESSION，再要求 checkpoint 覆盖它。其他不可覆盖来源/研究文件可先保存。')
p.write_text(s)
p=R/'exchange/BASELINE.json';d=json.loads(p.read_text());d['baseline_identity_file']='manifests/HANDOFF_IDENTITY.json (relative to package root; from workspace use ../manifests/HANDOFF_IDENTITY.json)';p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=R/'scripts/handoff/checkpoint_handoff.py';s=p.read_text();s=s.replace("'governance/VERSION_NOTES.md','governance/HANDOFF_README.md'","'governance/VERSION_NOTES.md','governance/FRAMEWORK_MANIFEST.json','governance/HANDOFF_README.md'")
p.write_text(s)
print('Patched pre-execution field mapping, read-only Git verification, and atomic SESSION documentation. No old research files changed.')
