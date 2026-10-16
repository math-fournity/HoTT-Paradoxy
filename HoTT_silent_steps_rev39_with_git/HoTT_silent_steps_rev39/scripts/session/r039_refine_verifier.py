#!/usr/bin/env python3
"""Preserve verification v1 and replace its tautological session test with a Git comparison."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
source = ROOT / 'scripts/session/r039_verify.py'
target = ROOT / 'scripts/session/r039_verify_v2.py'
old = " ck('research_session_not_overwritten',sha(ROOT/(P+'sessions/S-RES-20260911-039-SILENT-STEPS/SESSION.md'))==sha(ROOT/(P+'sessions/S-RES-20260911-039-SILENT-STEPS/SESSION.md')))"
new = """ original_session_path=P+'sessions/S-RES-20260911-039-SILENT-STEPS/SESSION.md'
 original_session_bytes=subprocess.check_output(['git','show','1eeafb5a1ae9a9dfa01dc52f518c553073ffbb03:'+original_session_path],cwd=ROOT)
 ck('research_session_matches_first_research_commit',sha(ROOT/original_session_path)==hashlib.sha256(original_session_bytes).hexdigest())"""
text = source.read_text()
if text.count(old) != 1:
    raise ValueError('Expected exactly one v1 tautological check')
if target.exists():
    raise FileExistsError(target)
text = text.replace(old, new)
text = text.replace("'artifacts/r039/VERIFICATION.json'", "'artifacts/r039/VERIFICATION_V2.json'")
text = text.replace("'artifacts/r039/REPORT.md'", "'artifacts/r039/REPORT_FINAL.md'")
text = text.replace("# R039 研究及交付报告", "# R039 研究及交付报告（验证器 v2）")
text = text.replace("文件与Git恢复报告在包外", "验证器v1的研究Session保护断言错误地将文件与自身比较；v2已改为与首次研究提交1eeafb5中的真实blob比较。v1源码、结果及修正脚本均保留；只采用v2作为最终检查。\n\n文件与Git恢复报告在包外")
target.write_text(text)
log = {
    'finding': 'The v1 research_session_not_overwritten assertion compared a file hash to itself.',
    'correction': 'v2 compares the current file to the blob in the original research commit 1eeafb5a1ae9a9dfa01dc52f518c553073ffbb03.',
    'scope': 'Verification infrastructure correction; no research source or mathematical conclusion changed.',
    'v1_preserved': True,
    'v1_script_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'v2_script_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
}
(ROOT / 'artifacts/r039/VERIFIER_CORRECTION.json').write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(log, ensure_ascii=False, indent=2))
