#!/usr/bin/env python3
"""Verify preservation and dynamic recovery; never certify mathematical truth from hashes."""
from pathlib import Path
import argparse,hashlib,json,subprocess
from r039_context import ROOT,runtime,dump
P='.codex/research/hott/';CID='P-SILENT-STEPS-039';SID='S-RES-20260911-039-SILENT-STEPS-CHECKPOINT'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--fresh',action='store_true');a=ap.parse_args();checks=[]
 def ck(name,value):
  checks.append({'name':name,'passed':bool(value)})
  if not value:raise AssertionError(name)
 old=json.loads((ROOT/'artifacts/r039/STATE_BASE.json').read_text());state=json.loads((ROOT/(P+'STATE.json')).read_text());baseline=json.loads((ROOT/'artifacts/r039/BASE_TRACKED_HASHES.json').read_text())
 ck('revision39',state['revision']==39 and state['latest_session']==SID)
 ck('all_87_old_records_preserved',len(old['records'])==87 and all(state['records'].get(k)==v for k,v in old['records'].items()))
 ck('89_current_records',len(state['records'])==89)
 ck('old_unresolved_preserved',state['unresolved']==old['unresolved'])
 ck('old_active_retained',set(old['active'])<=set(state['active']))
 changed=[];same=[]
 for p,h in baseline.items():
  if not (ROOT/p).is_file():raise AssertionError('Deleted old file: '+p)
  (same if sha(ROOT/p)==h else changed).append(p)
 allowed={'MEMORY.md',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md',P+'STATE.json','.codex/cognition/HEAD.json','scripts/README.md'}
 ck('changes_only_current_governance_and_index',set(changed)<=allowed)
 protected=['AGENTS.md','.codex/cognition/LOAD_SET.json','.codex/cognition/PROTOCOL.md','.codex/skills/hott-session-governance/SKILL.md','.codex/skills/hott-paradox-research/SKILL.md','.codex/skills/hott-paradox-research/scripts/cognition_runtime.py','认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md','HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md','HoTT/THEORY_SCHEMA.md','HoTT/CLAIM_EVIDENCE_MATRIX.md','scripts/research/r038_current_lift.py']
 for p in protected:ck('protected_'+p,sha(ROOT/p)==baseline[p])
 plan=runtime().plan(ROOT);routed={d['path'] for d in plan['documents']}
 for rid in [CID,SID]:
  record=state['records'][rid]
  ck('route_'+rid,set([record['path']]+record['full_sources'])<=routed)
  ck('hash_'+rid,all(sha(ROOT/p)==h for p,h in record['source_hashes'].items()))
 ck('R038_still_routed',old['records']['P-CURRENT-STATE-LIFTING-038']['path'] in routed)
 t=json.loads((ROOT/'artifacts/r039/TEST_EXECUTION.json').read_text());res=json.loads((ROOT/'artifacts/r039/RESULTS.json').read_text())
 ck('31_tests_actually_passed',t['exit_code']==0 and not t['timeout'] and 'Ran 31 tests' in t['stderr'] and '\nOK\n' in t['stderr'])
 ck('weak_bisim_may_must_gap',res['nondeterminism']['fast_retry_weak'] and res['nondeterminism']['must']['fast'] and not res['nondeterminism']['must']['retry'])
 ck('bad_relation_nontransitivity',res['delay']['bad_spin_ret0'] and res['delay']['bad_spin_ret1'] and not res['delay']['bad_ret0_ret1'])
 ck('positive_delay_guard',res['delay']['good_rejects_spin_ret0'] and res['delay']['good_identifies_finite_delay'])
 ck('not_native_or_core_error',res['native_kernel']=='NOT_RUN' and res['HoTT_core_error'] is False)
 ck('original_failed_dry_run_preserved',json.loads((ROOT/'artifacts/r039/checkpoint/FAILURE.json').read_text())['error']=='SESSION_RECORD_REQUIRED')
 ck('successful_retry_committed',json.loads((ROOT/'artifacts/r039/checkpoint_retry/COMMIT.json').read_text())['status']=='CHECKPOINT_COMMITTED')
 ck('stale_snapshot_rejected',json.loads((ROOT/'artifacts/r039/checkpoint_retry/STALE.json').read_text())['error']=='STALE_BASE')
 original_session_path=P+'sessions/S-RES-20260911-039-SILENT-STEPS/SESSION.md'
 original_session_bytes=subprocess.check_output(['git','show','1eeafb5a1ae9a9dfa01dc52f518c553073ffbb03:'+original_session_path],cwd=ROOT)
 ck('research_session_matches_first_research_commit',sha(ROOT/original_session_path)==hashlib.sha256(original_session_bytes).hexdigest())
 manifest=json.loads((ROOT/'artifacts/r039/RESEARCH_MANIFEST.json').read_text());ck('research_manifest_hashes',all(sha(ROOT/p)==h for p,h in manifest.items()))
 ck('cognition_honestly_incomplete',json.loads((ROOT/'artifacts/r039/COGNITION_STATUS.json').read_text())['status']=='BLOCKED_FULL_COGNITION')
 ck('all_download_failures_recorded',all(x['status']=='FAILED' for x in json.loads((ROOT/'artifacts/r039/sources/FETCH_RECEIPT.json').read_text())))
 ck('no_remote',not git('remote'));ck('no_background',state['execution_control']['background_work'] is False)
 ck('inherited_base_head',subprocess.run(['git','merge-base','--is-ancestor','149767b70bd102fa4b16b28922bf7bb3dd64682c','HEAD'],cwd=ROOT).returncode==0)
 if a.fresh:ck('fresh_clean_worktree',not git('status','--porcelain'))
 report=dict(status='PASS_FILE_ROUTING_AND_FINITE_EVIDENCE',revision=39,checks=checks,original_files_unchanged=len(same),original_files_changed=changed,old_records=len(old['records']),current_records=len(state['records']),planned_documents=len(plan['documents']),planned_bytes=plan['total_bytes'],git_head=git('rev-parse','HEAD'),full_cognition='NOT_CERTIFIED',native='NOT_RUN')
 if not a.fresh:
  out=ROOT/'artifacts/r039/VERIFICATION_V2.json'
  if out.exists():raise FileExistsError(out)
  out.write_text(dump(report))
  (ROOT/'artifacts/r039/REPORT_FINAL.md').write_text(f'''# R039 研究及交付报告（验证器 v2）\n\n当前revision39；继承revision38完整Git。原87项记录逐值保留，当前89项；{len(same)}份旧tracked文件保持字节，变化仅{len(changed)}项当前治理/索引。\n\n31项测试实际通过；144个有限确定性Delay图为局部交叉检查，不提供全HoTT证明。结果区分may/must、Bad最大单边关系与正确Delay保护；物理桥梁为MODEL_ONLY。\n\n首次checkpoint dry-run漏列SESSION被原引擎拒绝。原先已提交的研究Session不可覆盖，因此新建独立checkpoint Session；原脚本、载荷、错误与修正版保留。成功提交后旧快照实际被拒绝。\n\n433份原全文集合未加载完，BLOCKED_FULL_COGNITION；不虚构压缩、不更改政策、不认证全部Skill。web读源成功；容器下载三份源均DNS失败，未伪造本地原件或本地native输出。\n\n验证器v1的研究Session保护断言错误地将文件与自身比较；v2已改为与首次研究提交1eeafb5中的真实blob比较。v1源码、结果及修正脚本均保留；只采用v2作为最终检查。

文件与Git恢复报告在包外HoTT_silent_steps_rev39_delivery_verification.json，避免自哈希循环。\n''')
 print(dump(report))
if __name__=='__main__':main()
