#!/usr/bin/env python3
"""Validate preservation, governance routing and real finite evidence (not cognition)."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];P='.codex/research/hott/'
SID='S-RES-20260911-038-CURRENT-STATE-LIFTING';CID='P-CURRENT-STATE-LIFTING-038'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--fresh',action='store_true');a=ap.parse_args();checks=[]
 def ck(n,c):
  checks.append({'name':n,'passed':bool(c)})
  if not c:raise AssertionError(n)
 base=json.loads((ROOT/'artifacts/r038/BASE_TRACKED_HASHES.json').read_text())
 old=json.loads((ROOT/'artifacts/r038/STATE_BASE.json').read_text());state=json.loads((ROOT/(P+'STATE.json')).read_text())
 ck('state_revision38',state['revision']==38 and state['latest_session']==SID)
 ck('old_85_records_intact',len(old['records'])==85 and all(state['records'].get(k)==v for k,v in old['records'].items()))
 ck('87_records',len(state['records'])==87)
 ck('old_unresolved_intact',state['unresolved']==old['unresolved'])
 ck('old_active_retained',set(old['active'])<=set(state['active']))
 ck('no_background',state['execution_control']['background_work'] is False)
 allowed={'MEMORY.md',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md',P+'STATE.json','.codex/cognition/HEAD.json','scripts/README.md'}
 same=[];changed=[]
 for rel,h in base.items():
  path=ROOT/rel
  if not path.is_file():raise AssertionError('old file missing: '+rel)
  (same if sha(path)==h else changed).append(rel)
 ck('old_files_only_current_governance_changes',set(changed)<=allowed)
 protected=['AGENTS.md','.codex/cognition/LOAD_SET.json','.codex/cognition/PROTOCOL.md','.codex/skills/hott-session-governance/SKILL.md','.codex/skills/hott-paradox-research/SKILL.md','.codex/skills/hott-paradox-research/scripts/cognition_runtime.py',
 '认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md','HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md','HoTT/THEORY_SCHEMA.md','HoTT/CLAIM_EVIDENCE_MATRIX.md','scripts/research/r036_transition_abstraction.py']
 for rel in protected:ck('preserved_'+rel,sha(ROOT/rel)==base[rel])
 sp=importlib.util.spec_from_file_location('r038_verify_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sys.modules[sp.name]=rt;sp.loader.exec_module(rt)
 plan=rt.plan(ROOT);routes={d['path'] for d in plan['documents']}
 for rid in [CID,SID]:
  rec=state['records'][rid]
  ck('full_route_'+rid,set([rec['path']]+rec['full_sources'])<=routes)
  ck('source_hashes_'+rid,all(sha(ROOT/p)==h for p,h in rec['source_hashes'].items()))
 ck('old_R036_still_routed',old['records']['P-TRANSITION-ABSTRACTION-036']['path'] in routes)
 ck('checkpoint_committed',json.loads((ROOT/'artifacts/r038/checkpoint/COMMIT.json').read_text())['status']=='CHECKPOINT_COMMITTED')
 ck('stale_snapshot_rejected',json.loads((ROOT/'artifacts/r038/checkpoint/STALE.json').read_text())['error']=='STALE_BASE')
 test=json.loads((ROOT/'artifacts/r038/TEST_EXECUTION.json').read_text());res=json.loads((ROOT/'artifacts/r038/RESULTS.json').read_text())
 ck('real_28_tests',test['exit_code']==0 and not test['timed_out'] and 'Ran 28 tests' in test['stderr'] and '\nOK\n' in test['stderr'])
 ck('R036_exact_descent_failures',res['bad_R036']['current_lift_failures']==[[0,1],[1,0]])
 ck('positive_acc_checked',res['good_branching']['target_certificate_checked'] is True)
 ck('not_necessary_control',res['not_necessary_for_termination']=={'uniform':False,'source_terminates':True,'target_terminates':True})
 ck('17_finite_prefix_checks',len(res['countdown_horizons'])==17)
 ck('no_native_claim',res['bounds']['general_theorems']=='PAPER_ONLY' and res['bounds']['claims_HoTT_core_error'] is False)
 ck('cognition_not_certified',json.loads((ROOT/'artifacts/r038/COGNITION_STATUS.json').read_text())['status']=='NOT_CERTIFIED_FULL_COGNITION')
 ck('no_remotes',not git('remote'))
 ck('inherited_original_head',subprocess.run(['git','merge-base','--is-ancestor','515da9f6143fb5fd545031fa9648a5a002d75c2b','HEAD'],cwd=ROOT).returncode==0)
 if a.fresh:ck('fresh_git_clean',not git('status','--porcelain'))
 report={'status':'PASS_FILES_ROUTING_AND_FINITE_EVIDENCE','revision':38,'research_round':'R038','checks':checks,
 'old_records':len(old['records']),'record_count':len(state['records']),'original_files_unchanged':len(same),'original_files_changed':changed,
 'planned_documents':len(plan['documents']),'planned_bytes':plan['total_bytes'],'git_head':git('rev-parse','HEAD'),'git_clean':not git('status','--porcelain'),
 'full_cognition':'NOT_CERTIFIED','native_formal':'NOT_RUN'}
 if not a.fresh:
  dest=ROOT/'artifacts/r038/VERIFICATION.json'
  if dest.exists():raise FileExistsError(dest)
  dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
  (ROOT/'artifacts/r038/REPORT.md').write_text(f'''# R038 研究与交接报告\n\n当前revision38；继承revision37完整.git。旧{len(old['records'])}项记录逐值保留，当前{len(state['records'])}项。{len(same)}份旧tracked文件逐字节未变；变化仅{len(changed)}项当前治理/索引。\n\n新结果是后继下降/当前态提升条件、仅截断见证的Acc迁移、有限前缀与无限相容性的区别。28项程序检查通过；17个前缀是有限演示，未用作无界证明。一般HoTT论证是纸笔，未认证内核、原创或物理实例。\n\n原政策/引擎/闭包/三问/Schema/矩阵不变；实际压缩导致418份原动态材料未完整同窗加载，保持NOT_CERTIFIED_FULL。新的433份计划路由不等于已读完。\n\n原checkpoint已提交，旧snapshot测试被拒绝。完整ZIP/bundle及异目录恢复结果在包外HoTT_path_lifting_rev38_delivery_verification.json，避免自身哈希循环。\n\n参考来源两次cache miss与未经本地编译范围保存在SOURCES。首次测试28项全部通过；无伪造失败修复。r038_run收据的source_hashes在结束时对argv文件取哈希，MODEL收据包含输出RESULTS；RESEARCH_MANIFEST另明确记录import的R036源码。\n''')
 print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
