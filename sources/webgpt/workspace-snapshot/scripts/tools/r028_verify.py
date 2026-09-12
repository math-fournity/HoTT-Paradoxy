"""Verify old byte preservation and new routing; this is NOT mathematical certification."""
from pathlib import Path
import ast, hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jt(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def main():
    out=ROOT/'artifacts/r028'
    base=json.loads((out/'RESTORE_BASELINE.json').read_text())
    expected={'MEMORY.md','.codex/research/hott/FRONTIER.md','.codex/research/hott/LESSONS.md',
       '.codex/research/hott/RESUME.md','.codex/research/hott/STATE.json','.codex/cognition/HEAD.json',
       '.codex/research/hott/dialogues/GEMINI-001/DEBATE_LEDGER.json','scripts/README.md'}
    changed=[];missing=[]
    for row in base['files']:
        p=ROOT/row['path']
        if not p.is_file():missing.append(row['path'])
        elif sha(p)!=row['sha256']:changed.append(row['path'])
    assert not missing
    assert set(changed)==expected,(changed,expected)
    syntax=[]
    for p in sorted(ROOT.glob('scripts/**/r028_*.py')):
        ast.parse(p.read_text(),filename=str(p));syntax.append(p.relative_to(ROOT).as_posix())
    incoming=ROOT/'.codex/research/hott/dialogues/GEMINI-001/rounds/008/IN-007.md'
    prov=json.loads((out/'INPUT_PROVENANCE.json').read_text());assert sha(incoming)==prov['peer_sha256']
    for row in prov['code_fragments']:assert sha(ROOT/row['path'])==row['sha256']
    results=json.loads((out/'SCOPE_TEST_RESULTS.json').read_text())
    assert results['groups_passed']==5 and results['model_total']==234 and results['satisfying_total']==20
    assert results['source_sha256']==sha(ROOT/'scripts/research/r028_scope_checks.py')
    assert results['r024_sha256']==sha(ROOT/'scripts/research/r024_diagonal_machine.py')
    assert json.loads((out/'SCOPE_TEST_EXECUTION.json').read_text())['exit_code']==0
    assert json.loads((out/'NATIVE_AVAILABILITY.json').read_text())['native_execution_status']=='NOT_RUN_NO_TOOLCHAIN'
    assert (ROOT/'.codex/research/hott/dialogues/GEMINI-001/TO_GEMINI_007.md').read_bytes()==(ROOT/'.codex/research/hott/dialogues/GEMINI-001/TO_GEMINI_007.txt').read_bytes()
    s=importlib.util.spec_from_file_location('r028_v_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(s);sys.modules[s.name]=rt;s.loader.exec_module(rt)
    p=rt.plan(ROOT)
    summary=json.loads((out/'CHECKPOINT_SUMMARY.json').read_text())
    paths={x['path'] for x in p['documents']}
    assert p['revision']==28 and p['snapshot']==summary['snapshot']
    assert set(summary['required_paths'])<=paths
    oldstate=json.loads((out/'before/.codex/research/hott/STATE.json').read_text())
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    assert set(oldstate['records'])<=set(state['records'])
    ledger=json.loads((ROOT/'.codex/research/hott/dialogues/GEMINI-001/DEBATE_LEDGER.json').read_text())
    assert ledger['next_questions']==[] and not ledger['workflow']['awaiting_peer_to_start_research']
    assert ledger['latest_incoming']=='IN-007' and ledger['latest_outgoing']=='OUT-007'
    assert json.loads((out/'checkpoint/STALE_BASE.json').read_text())['error']=='STALE_BASE'
    result={'status':'PASS_FILE_AND_ROUTING_SCOPE','baseline_files':len(base['files']),
      'unchanged_prior_files':len(base['files'])-len(changed),'changed_prior_files':changed,'missing':missing,
      'old_record_count':len(oldstate['records']),'new_record_count':len(state['records']),
      'new_python_syntax_checked':syntax,'snapshot':p['snapshot'],'revision':28,'documents':len(paths),
      'original_user_and_peer_sources_preserved':True,'r026_r027_and_new_round_in_dynamic_set':True,
      'all_old_records_retained':True,'reply_dependency':False,
      'limits':'File identity/routing, not complete cognitive loading or native theorem certification.'}
    target=out/'VERIFICATION.json'
    if target.exists():raise FileExistsError(target)
    target.write_text(jt(result))
    report='''# R028 实施与验证报告\n\n本轮从revision27完整Git包恢复；第一提交先保全现场与IN-007，之后才做审读和新检查。\n\n## 实际结果\n\n- M01改善了Trap定义/归纳，但全称ReachTrap过强，配合返回保持排除了所有返回状态；不适用于原R024机器。\n- 5组有限检查通过，234个模型及两个原编译实例；一般推断另有纸笔证明，不以样本认证无界命题。\n- M02仍是文档预期。当前未发现原生工具，一次官方发行地址探测DNS失败；不产生伪日志。\n- OUT-007为共同认识的收束信，无新派工编号、不依赖回复继续工作。R026规约探索与旧正反结果持续保存。\n\n## 真实保全\n\n'''
    report+=f"原文件{len(base['files'])}份，其中{len(base['files'])-len(changed)}份逐字节未改；修改的既有文件仅{len(changed)}个治理/索引文件。旧record {len(oldstate['records'])}项全部保留，现有{len(state['records'])}项。新进程plan得到revision28和{len(paths)}份动态文件，并实际包含R026/R027与本轮正文、证据。旧snapshot写回被拒绝。\n\n"
    report+='''所有新代码先scripts落盘再调用。原认知闭包、三问、AGENTS、Skills、Schema、主张矩阵、旧代码/结果/信件原文保持原字节。全量业务认知门禁未认证；本轮为有界来信审计，不将哈希、plan或checkpoint冒充全文理解。\n\n## 交付\n\n完成本地Git提交后，用已保存的package_workspace.py生成带.git的ZIP及bundle，并实际解压/fsck/克隆核对。最终HEAD和交付字节报告放在仓库外，避免让记录自身hash成为自引用。没有远端push或其他AI调用。\n'''
    (out/'REPORT.md').write_text(report)
    print(jt(result))
if __name__=='__main__':main()
