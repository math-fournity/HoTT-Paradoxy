#!/usr/bin/env python3
"""File, current-owner, dynamic routing and finite-evidence audit (not cognition proof)."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];P='.codex/research/hott/'
C='认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md'
Q='HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md';K='.codex/skills/hott-paradox-research/SKILL.md'
SID='S-GOV-20260911-037-OWNER-ALIGNMENT-FINAL';CID='P-TRANSITION-ABSTRACTION-036'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--fresh',action='store_true');a=ap.parse_args()
 checks=[]
 def ck(name,condition):
  checks.append({'name':name,'passed':bool(condition)})
  if not condition:raise AssertionError(name)
 base=json.loads((ROOT/'artifacts/r036/BASE_TRACKED_HASHES.json').read_text())
 old=json.loads((ROOT/'artifacts/r036/STATE_BASE.json').read_text());state=json.loads((ROOT/(P+'STATE.json')).read_text())
 ck('revision37_after_research36',state['revision']==37 and state['latest_session']==SID)
 ck('resumed_not_paused',state['execution_control']['status']=='RESUMED_BY_USER')
 ck('no_background',state['execution_control']['background_work'] is False)
 ck('all_82_old_records_unchanged',all(state['records'].get(k)==v for k,v in old['records'].items()))
 ck('old_active_preserved',all(x in state['active'] for x in old['active']))
 ck('all_unresolved_preserved',state['unresolved']==old['unresolved'])
 allowed=set(json.loads((ROOT/'artifacts/r036/ALIGNMENT_CHANGES.json').read_text())['changes'])|{'scripts/README.md','MEMORY.md',P+'STATE.json',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md','.codex/cognition/HEAD.json'}
 same=[];changed=[]
 for rel,h in base.items():
  p=ROOT/rel
  if not p.is_file():raise AssertionError('inherited file missing: '+rel)
  (same if sha(p)==h else changed).append(rel)
 ck('only_authorized_old_file_changes',set(changed)<=allowed)
 protected=['.codex/cognition/LOAD_SET.json','.codex/cognition/PROTOCOL.md','.codex/skills/hott-session-governance/SKILL.md','.codex/skills/hott-paradox-research/scripts/cognition_runtime.py','HoTT/THEORY_SCHEMA.md','HoTT/CLAIM_EVIDENCE_MATRIX.md']
 ck('engine_policy_schema_matrix_preserved',all(sha(ROOT/p)==base[p] for p in protected))
 before=(ROOT/('.codex/history/r036-before/'+C)).read_text();after=(ROOT/C).read_text()
 historical=before[before.index('## 十七、'):]
 ck('closure_historical_sections17_to21_exact',historical in after)
 pause=P+'sessions/S-PAUSE-20260911-035-COMPUTATION-BOUNDARY/'
 ck('R035_request_exact_in_closure',(ROOT/(pause+'REQUEST.md')).read_text() in after)
 ck('R035_assessment_exact_in_closure',(ROOT/(pause+'ASSESSMENT.md')).read_text() in after)
 section14=after[after.index('## 十四、'):after.index('## 十五、')]
 ck('stale_no_git_current_verdict_removed','当前环境无.git' not in section14 and '不是新的数学研究轮次' not in section14)
 ck('old_current_v3_removed','三问当前在v3' not in after)
 ck('three_questions_v6','v6（revision36' in (ROOT/Q).read_text())
 ck('business_skill_1_3_4','version: "1.3.4"' in (ROOT/K).read_text())
 for rel in ['AGENTS.md',Q,K,C,'HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md','HoTT/INTRINSIC_TEMPORALITY_OF_HOTT.md']:
  txt=(ROOT/rel).read_text()
  ck('current_lenses_'+rel,'共享界限' in txt and '新增失真' in txt)
 ck('scripts_first_preserved','禁止 inline 代码' in (ROOT/'AGENTS.md').read_text())
 spec=importlib.util.spec_from_file_location('r036_verify_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py');rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
 plan=rt.plan(ROOT);routes={r['path'] for r in plan['documents']}
 for rid in [CID,SID]:
  rec=state['records'][rid];ck('new_record_full_source_route_'+rid,set(rec['full_sources']+[rec['path']])<=routes)
  ck('new_record_source_hashes_'+rid,all(sha(ROOT/p)==h for p,h in rec['source_hashes'].items()))
 for d in ['artifacts/r036/checkpoint','artifacts/r036/final_alignment']:
  ck('real_checkpoint_'+d,json.loads((ROOT/(d+'/COMMIT.json')).read_text())['status']=='CHECKPOINT_COMMITTED')
  ck('stale_rejection_'+d,json.loads((ROOT/(d+'/STALE.json')).read_text())['error']=='STALE_BASE')
 tests=json.loads((ROOT/'artifacts/r036/TEST_EXECUTION.json').read_text());results=json.loads((ROOT/'artifacts/r036/RESULTS.json').read_text())
 ck('28_tests_real_success',tests['exit_code']==0 and not tests['timeout'] and 'Ran 28 tests' in tests['stderr'] and '\nOK\n' in tests['stderr'])
 ck('finite_cycle_lift_certificates',results['source']['all_runs_complete'] and not results['quotient']['all_runs_complete'] and results['finite_obstruction']['compatible_concrete_representatives']==[[0],[1],[]])
 ck('75_finite_partitions',sum(x['Done_preserving_partitions'] for x in results['chain_partition_classification'])==75)
 ck('no_native_certification',results['scope']['native_formal_validation']=='NOT_RUN')
 ck('actual_tool_absence_recorded',all(v is None for v in json.loads((ROOT/'artifacts/r036/START.json').read_text())['tools'].values()))
 ck('no_git_remotes',not git('remote'))
 ck('inherited_history',subprocess.run(['git','merge-base','--is-ancestor','6096f71a2dbbeb842ac8aab74eb7059c60788541','HEAD'],cwd=ROOT).returncode==0)
 if a.fresh:ck('fresh_worktree_clean',not git('status','--porcelain'))
 report={'status':'PASS_FILES_ROUTING_AND_FINITE_EVIDENCE','revision':37,'research_round':'R036','checks':checks,
 'old_records_unchanged':len(old['records']),'record_count':len(state['records']),
 'original_files_unchanged':len(same),'original_files_changed':changed,'runtime_documents':len(plan['documents']),
 'runtime_bytes':plan['total_bytes'],'snapshot':plan['snapshot'],'git_head_at_check':git('rev-parse','HEAD'),
 'git_clean':not git('status','--porcelain'),'full_cognition':'NOT_CERTIFIED','native_formal':'NOT_RUN',
 'claim_scope':'known abstraction mechanism; new finite instance; not HoTT core inconsistency or real software bug'}
 if not a.fresh:
  p=ROOT/'artifacts/r036/VERIFICATION.json'
  if p.exists():raise FileExistsError(p)
  p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
  (ROOT/'artifacts/r036/REPORT.md').write_text(f'''# R036研究／R037最终治理校准：交付说明

当前工作副本继承revision35完整Git，用户授权恢复。研究R036提出三个状态、Done保真的存在关系像，完成纸笔推导和28项有限测试。最终治理37只是修正旧current Verdict及指针，不是第二轮数学成果。

治理已对齐：AGENTS、业务Skill v1.3.4、三问v6、第五闭包当前综合及§22、Z/时间owner、README、feature/ruling、MEMORY/STATE。区分已有计算能力、共享形式界限、特定新增失真。旧原话保留，§17—21整段不变；旧{len(old['records'])}项记录逐值不变。{len(same)}份原文件逐字节不变；仅白名单current/治理文件变化。

数学结果：原a→b→d两步完成；抽象w→w的两步前缀无法提升。不是源程序不可判定，合理may抽象本来允许虚假反例。等级可因子化给保真判据；一般论证与有限测试分开，不认领HoTT内核证明或原创性。

两次checkpoint均实际成功且旧快照写回被拒绝。代码先存scripts后执行。没有Lean/Agda/Rocq，没有新增未编译稿来充数；全文动态集合未全部加载，实际压缩存在，不能认证全业务认知。首次目录移动工具因目标工作目录不存在失败后从/mnt/data正确恢复，无文件覆盖；web固定logic源码读取一次cache miss，规则使用既有固定源码，不报成下载成功。

最终ZIP与bundle的恢复结果在包外delivery_verification，避免自指哈希。文件/路由检查不认证AI永不遗忘、数学原创、物理对应或独立审查。
''',encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
