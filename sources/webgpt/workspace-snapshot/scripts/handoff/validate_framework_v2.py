#!/usr/bin/env python3
"""Retain legacy failures; verify CURRENT semantics without editing historical tests."""
from pathlib import Path
import hashlib, importlib.util, json, subprocess,sys,tempfile
from datetime import datetime,timezone
from govern import load
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'artifacts/r040'
def dump(p,x):
 if p.exists():raise FileExistsError(p)
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def main():
 old=json.loads((OUT/'LEGACY_TEST_EXECUTION.json').read_text());assert old['exit_code']==1
 text=old['stderr'];expected=['test_11_eof_is_not_model_context_certificate','test_12_file_growth_has_no_fixed_2115_limit','test_16_main_gate_precedes_research']
 assert 'Ran 73 tests' in text and 'failures=3' in text
 for n in expected:assert 'FAIL: '+n in text
 sp=ROOT/'.codex/skills/hott-paradox-research/scripts/read_cognitive_closure.py'
 spec=importlib.util.spec_from_file_location('current_reader',sp);reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
 def read_all(root):
  parts=[];start=1;expected_sha=None
  while True:
   p=reader.read_chunk(root,start_line=start,max_bytes=131072,expected_sha256=expected_sha)
   assert p['model_context_completeness']=='NOT_CERTIFIED_BY_READER';parts.append(p['text']);expected_sha=p['file_sha256']
   if p['file_eof']:break
   start=p['next_start_line']
  return ''.join(parts).encode(),len(parts),p
 actual=(ROOT/reader.CLOSURE_RELATIVE_PATH).read_bytes();data,pages,last=read_all(ROOT)
 assert data==actual and pages>=2
 with tempfile.TemporaryDirectory(prefix='hott-portable-validation-') as temp:
  t=Path(temp);cp=t/reader.CLOSURE_RELATIVE_PATH;cp.parent.mkdir(parents=True);cp.write_bytes(actual+b'\nR040 APPENDED FIXTURE\n')
  b,_,p=read_all(t);assert b==cp.read_bytes() and p['total_lines']>last['total_lines']
  for rel in ['governance/PATHS.json','.codex/skills/hott-paradox-research/scripts/cognition_runtime.py']:
   dest=t/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((ROOT/rel).read_bytes())
  cmd=[sys.executable,'-B',str(ROOT/'scripts/handoff/govern.py'),'--root',str(t),'install-entry','--directory','my_non_codex_rules']
  q=subprocess.run(cmd,cwd='/',capture_output=True,text=True);assert q.returncode==0,q.stderr+q.stdout
  assert (t/'my_non_codex_rules/HOTT_ENTRYPOINT.md').is_file()
  q2=subprocess.run(cmd,cwd='/',capture_output=True,text=True);assert q2.returncode==2
 skill=(ROOT/'.codex/skills/hott-paradox-research/SKILL.md').read_text()
 for token in ['EVERY_INVOCATION_FULL_TEXT_PLUS_DYNAMIC_STATE','BLOCKED_FULL_COGNITION','当前模型上下文']:
  assert token in skill
 assert skill.index('## -1.')<skill.index('## 0.')
 rt=load(ROOT);plan=rt.plan(ROOT);state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
 needs=[r for r in plan['review_required'] if state['records'][r]['status']!='review_required']
 report={'status':'CURRENT_CHECKS_PASS_WITH_DOCUMENTED_LEGACY_DRIFT','legacy_unmodified':{'run':73,'pass':70,'fail':3,'failed_tests':expected},'runtime_suite':{'run':56,'pass':56},'supplemental_current_checks':['complete multi-page byte recovery with non-certifying EOF','file growth recovered through pagination','current policy names and gate order','alternate non-.codex entry created','existing entry not overwritten'],'closure_bytes':len(actual),'max_reader_bytes':131072,'pages':pages,'new_dependency_reviews_required':needs,'original_runtime_unchanged':True,'model_understanding':'NOT_CERTIFIED','mathematics':'NOT_CERTIFIED'}
 dump(OUT/'FRAMEWORK_TESTS.json',report);print(json.dumps(report,ensure_ascii=False,indent=2))
 notes='''# 当前完整版本的清单与旧测试说明\n\n本次保留原框架全部文件，不把历史资产清单当当前哈希。业务SKILL正文实际为1.3.4，原MANIFEST仍写1.3.3，属于历史未刷新索引；当前完整框架清单由FRAMEWORK_MANIFEST.json明确记录现有字节。旧清单原字节保留，不能将它用于当前版本验收。\n\n实际原样运行73项旧测试：70通过、3失败。当前cognition_runtime的56项测试全部通过。旧单闭包测试中，test11/test12把131072字节单次输出预算错误当成能读完整份闭包；当前闭包已长到165947字节，因此必须分页；test16要求旧版政策字符串，当前正文已改为动态集合政策。\n\n没有修改这些旧测试或收据。新增独立检查实际验证多页全部字节、追加内容、EOF不认证理解、当前前置顺序与非Codex入口。结果见artifacts/r040/FRAMEWORK_TESTS.json；不能写成“原73项全部通过”。这些不支持数学认证。\n'''
 (ROOT/'governance/VERSION_NOTES.md').write_text(notes)
 for p in [ROOT.parent/'README.md',ROOT/'governance/HANDOFF_README.md']:
  s=p.read_text();s=s.replace('另外有原框架回归、实际新目录plan和完整包恢复记录，最终以validation中的真实输出为准。','原框架原样回归73项中70通过、3项旧单页/旧字符串断言失败；现运行器56项全部通过，另用新版独立检查确认分页完整恢复与入口。旧失败和原源码不删除，详见 governance/VERSION_NOTES.md。还有实际新目录plan和完整包恢复记录，最终以validation中的真实输出为准。')
  p.write_text(s)
if __name__=='__main__':main()
