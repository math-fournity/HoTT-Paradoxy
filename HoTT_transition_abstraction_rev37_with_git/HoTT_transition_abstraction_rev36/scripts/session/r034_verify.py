#!/usr/bin/env python3
"""Verify preservation, actual outputs and recovery routing, not mathematical truth."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
R=P+'reviews/SELF-REFERENCE-006/'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def runtime():
 s=importlib.util.spec_from_file_location('r034_verify_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
 m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--fresh',action='store_true');a=ap.parse_args()
 state=json.loads((ROOT/(P+'STATE.json')).read_text());base=json.loads((ROOT/'artifacts/r034/checkpoint/STATE_BASE.json').read_text())
 plan=runtime().plan(ROOT);assert state['revision']==plan['revision']==34
 assert all(state['records'][k]==v for k,v in base['records'].items())
 required={R+'PROOF_NOTE.md',R+'PLAN.md',R+'SOURCES.md',R+'CLAIMS.json','MEMORY.md',
 P+'reviews/SELF-REFERENCE-004/PROOF_NOTE.md',P+'reviews/SELF-REFERENCE-005/PROOF_NOTE.md',P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md'}
 assert required<={d['path'] for d in plan['documents']}
 rec=state['records']['P-PATH-CERTIFICATE-034'];assert all(sha(ROOT/p)==h for p,h in rec['source_hashes'].items())
 status=subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True)
 basic={'revision':34,'prior_records_unchanged':len(base['records']),'records':len(state['records']),'documents':len(plan['documents']),
 'snapshot':plan['snapshot'],'old_and_new_routes_present':True,'source_hashes_match':True,
 'git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'worktree_clean':not status.strip(),
 'native_formal':'NOT_RUN','full_business_cognition':'INCOMPLETE_ACTUAL_COMPACTION'}
 if a.fresh:
  assert not status.strip();print(json.dumps(basic,ensure_ascii=False,indent=2));return
 original=json.loads((ROOT/'artifacts/r034/BASE_TRACKED_HASHES.json').read_text())
 allowed={'MEMORY.md',P+'STATE.json',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md','.codex/cognition/HEAD.json',
 'HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md'}
 same=[];changed=[]
 for rel,h in original.items():
  p=ROOT/rel;assert p.is_file(),'Missing old file '+rel
  (same if sha(p)==h else changed).append(rel)
 assert set(changed)<=allowed,repr(set(changed)-allowed)
 for rel in ['HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md',P+'LESSONS.md']:
  assert (ROOT/rel).read_bytes().startswith((ROOT/'artifacts/r034/checkpoint/originals'/rel).read_bytes())
 for name in ['TEST_EXECUTION.json','CONSTRUCTION_EXECUTION.json','WRITE_RECORDS_EXECUTION.json','CHECKPOINT_EXECUTION.json']:
  d=json.loads((ROOT/'artifacts/r034'/name).read_text());assert d['exit_code']==0 and not d['timeout']
 t=json.loads((ROOT/'artifacts/r034/TEST_EXECUTION.json').read_text());assert 'Ran 24 tests' in t['stderr'] and '\nOK' in t['stderr']
 result=json.loads((ROOT/'artifacts/r034/RESULTS.json').read_text())
 assert result['source_output']==1 and result['erased_output']==0
 assert result['erased_value_still_has_fibre_type'] and result['dependent_receipt_rejected']=='computed equality is false'
 assert result['natural_under_target_flip']==[] and result['fixed_input_2_replay_succeeds_under_changed_action']
 assert result['core_source_sha256']==sha(ROOT/'scripts/research/r032_restricted_reflection.py')
 identities=json.loads((ROOT/'artifacts/r034/CODE_IDENTITIES.json').read_text())
 assert all(sha(ROOT/p)==h for p,h in identities['files'].items())
 stale=json.loads((ROOT/'artifacts/r034/checkpoint/STALE.json').read_text());assert stale['error']=='STALE_BASE'
 result=basic|{'status':'PASS_ARCHIVE_ROUTING_AND_RECORDED_OUTPUTS','inherited_files_unchanged':len(same),'changed_inherited_files':changed,
  'old_prefixes_preserved':True,'test_count':24,'stale_write_rejected':True,
  'scope':'File and finite program checks only; not independent HoTT or semantic completeness certification'}
 out=ROOT/'artifacts/r034/VERIFICATION.json'
 if out.exists():raise FileExistsError(out)
 out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'artifacts/r034/REPORT.md').write_text(f'''# R034 实施与交付前验证

状态：PASS_ARCHIVE_ROUTING_AND_RECORDED_OUTPUTS。

数学结果与程序范围分开：完整纸笔Σ回路反证无全宇宙MereMove；24有限证书测试通过，不是HoTT内核。Agda草稿未编译。

原{len(base['records'])}条记录逐值未改，当前{len(state['records'])}条。原{len(same)}份tracked文件保持原字节；仅{len(changed)}项既有治理/专题/索引更新。专题、经验与脚本索引保留旧前缀。新代码先存后跑，实际测试及构造日志exit0。旧快照重试实际返回STALE_BASE。

新R034原始材料与R026/R032/R033已在动态读取集合。核心两文曾完整输出，实际压缩后未完成全动态集合；不认证完整业务门禁。未启动其他AI或远端动作。

本报告在最终Git提交之前产生；最终HEAD、干净工作树、ZIP回读、异目录恢复及bundle克隆结果在外部交付verification中，不虚构未来提交。
''',encoding='utf-8')
 print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
