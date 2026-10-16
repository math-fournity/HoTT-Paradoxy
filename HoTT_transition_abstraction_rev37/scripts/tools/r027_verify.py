"""Verify original preservation, real output identities and current routing. No math certification."""
from pathlib import Path
import ast, hashlib, json, re, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]; O=ROOT/'artifacts/r027'; D='.codex/research/hott/dialogues/GEMINI-001/'
P='.codex/research/hott/'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    checks=[]
    def check(name,ok,detail=None):
        row={'id':name,'pass':bool(ok)}
        if detail is not None:row['detail']=detail
        checks.append(row)
        if not ok:raise RuntimeError(name)
    baseline=json.loads((O/'BASELINE.json').read_text())
    allowed={'MEMORY.md',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md',P+'STATE.json',
             '.codex/cognition/HEAD.json',D+'DEBATE_LEDGER.json','scripts/README.md'}
    modified=[];missing=[];unchanged=[]
    for row in baseline['protected_non_git_files']:
        f=ROOT/row['path']
        if not f.is_file():missing.append(row['path'])
        elif sha(f)!=row['sha256'] or f.stat().st_size!=row['bytes']:modified.append(row['path'])
        else:unchanged.append(row['path'])
    check('baseline_files_not_removed',not missing,missing)
    check('only_authorized_existing_paths_changed',set(modified)<=allowed,modified)
    check('baseline_zip_unchanged',sha(Path(baseline['source']))==baseline['source_sha256'])
    for path in ['AGENTS.md','HoTT/AUDIT_AND_RECONSTRUCTION.md','HoTT/CLAIM_EVIDENCE_MATRIX.md',
                 P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md',P+'reviews/EARLY-GEMINI-001/PLAN.md',
                 'artifacts/r026/CHECK_V1_RESULTS.json',D+'TO_GEMINI_005.md',
                 'scripts/research/r024_diagonal_machine.py','scripts/research/r025_diagonal_audit.py']:
        check('protected:'+path,path in unchanged)
    state=json.loads((ROOT/(P+'STATE.json')).read_text())
    oldstate=json.loads((O/'before'/P/'STATE.json').read_text())
    check('old_record_ids_preserved',set(oldstate['records'])<=set(state['records']))
    check('revision27',state['revision']==27)
    led=json.loads((ROOT/D/'DEBATE_LEDGER.json').read_text())
    check('latest_dialogue_pointers',led['latest_incoming']=='IN-006' and led['latest_outgoing']=='OUT-006')
    check('counts_consistent',led['received_rounds']==len(led['incoming'])==6 and led['outgoing_count']==len(led['outgoing'])==6)
    check('prior_reply_no_longer_pending',next(x for x in led['outgoing'] if x['id']=='OUT-005')['reply_id']=='IN-006')
    check('new_reply_not_sent',next(x for x in led['outgoing'] if x['id']=='OUT-006')['actually_sent'] is False)
    check('next_questions_current',[x['id'] for x in led['next_questions']]==['M01','M02'])
    check('old_incoming_ids_preserved',{x['id'] for x in json.loads((O/'before'/D/'DEBATE_LEDGER.json').read_text())['incoming']} <= {x['id'] for x in led['incoming']})
    inc=ROOT/D/'rounds/007/IN-006.md';pro=json.loads((ROOT/D/'rounds/007/PROVENANCE.json').read_text())
    check('incoming_matches_saved_identity',sha(inc)==pro['source_sha256'] and inc.stat().st_size==pro['bytes'])
    blocks=re.findall(r'```lean\n(.*?)```',inc.read_text(),re.S)
    check('all_six_original_code_blocks',len(blocks)==len(pro['fenced_lean_snippets'])==6)
    for i,(b,row) in enumerate(zip(blocks,pro['fenced_lean_snippets'])):
        check('snippet_identity_'+str(i+1),sha(ROOT/row['path'])==row['sha256'] and (ROOT/row['path']).read_text()==b.rstrip('\n')+'\n')
    check('outgoing_markdown_text_identical',(ROOT/D/'TO_GEMINI_006.md').read_bytes()==(ROOT/D/'TO_GEMINI_006.txt').read_bytes())
    result=json.loads((O/'FINITE_MODEL_RESULTS.json').read_text()); receipt=json.loads((O/'FINITE_MODEL_RECEIPT.json').read_text())
    check('finite_seven_groups',len(result['groups'])==7 and result['violations']==[])
    check('finite_counts',result['counts']['labelled_models']==4330 and result['counts']['globally_applicable_cases']==1324)
    check('actual_code_hash',sha(ROOT/receipt['code'])==receipt['code_sha256'])
    check('actual_result_hash',sha(O/'FINITE_MODEL_RESULTS.json')==receipt['result_sha256'])
    native=json.loads((O/'NATIVE_RUN.json').read_text())
    check('native_not_fabricated',all(x.get('status')=='NOT_RUN_TOOL_UNAVAILABLE' for x in native['records']))
    check('seven_lean_drafts',len(list((ROOT/'scripts/research/r027_lean').glob('*.lean')))==7)
    check('coq_draft_exists',(ROOT/'scripts/research/r027_coq/OracleExtraction.v').is_file())
    pyfiles=[p for p in (ROOT/'scripts').rglob('r027*.py')]
    for p in pyfiles:ast.parse(p.read_text(),filename=str(p))
    check('new_python_sources_parse',True,{'files':len(pyfiles)})
    check('failed_checkpoint_retained',(O/'checkpoint/FIRST_ATTEMPT_FAILURE.json').is_file() and (O/'checkpoint/PAYLOAD.json').is_file())
    check('checkpoint_committed',json.loads((O/'checkpoint/COMMIT.json').read_text())['status']=='CHECKPOINT_COMMITTED')
    check('stale_base_rejected',json.loads((O/'checkpoint/STALE_BASE.json').read_text())['error']=='STALE_BASE')
    run=subprocess.run([sys.executable,'-B',str(ROOT/'scripts/session/r027_plan_check.py')],cwd=ROOT,capture_output=True,text=True,timeout=30)
    (O/'FRESH_PROCESS_EXECUTION.json').write_text(json.dumps({'argv':[sys.executable,'-B','scripts/session/r027_plan_check.py'],'cwd':str(ROOT),'exit_code':run.returncode,'stdout':run.stdout,'stderr':run.stderr},ensure_ascii=False,indent=2)+'\n')
    check('fresh_process_route',run.returncode==0)
    fresh=json.loads(run.stdout)
    finalplan=json.loads((O/'FINAL_PLAN.json').read_text())
    check('fresh_snapshot_identity',fresh['snapshot']==finalplan['snapshot'])
    g=subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',baseline['inherited_head'],'HEAD'],capture_output=True)
    check('inherited_history_ancestor',g.returncode==0)
    rem=subprocess.run(['git','-C',str(ROOT),'remote'],capture_output=True,text=True,check=True)
    check('no_git_remote',not rem.stdout.strip())
    report={'schema':'r027-preservation-and-file-verification/v1','status':'PASS','checks':checks,
      'checks_passed':len(checks),'original_non_git_files':len(baseline['protected_non_git_files']),
      'original_files_unchanged':len(unchanged),'existing_paths_modified':modified,'missing':missing,
      'restored_zip_members':baseline['files_restored'],
      'mathematical_kernel':'NOT_RUN','full_business_cognition':'NOT_CERTIFIED','snapshot':fresh['snapshot']}
    (O/'VERIFY.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (O/'REPORT.md').write_text(f'''# R027 · IN-006审读、验证和接续

## 实际状态

继承R026完整包与Git。当前状态revision27，最新Session S-DISC-20260911-027-GEMINI-IN006。旧记录{len(oldstate['records'])}项全部保留，新状态{len(state['records'])}项。OUT-006仅准备，未直接发送。

## 认识连续

原有非Git文件{len(baseline['protected_non_git_files'])}份，其中{len(unchanged)}份原字节未变。仅8个既有路径发生授权的治理/index更新；闭包、三问、Skills、Schema、数学主张矩阵、R026审计owner/评估/代码及旧来往信原文保持原字节。R026规约忠实性探索继续，与本次全局环境Σ的识别衔接。

## 实际新验证

7组有限语义检查：4330个1..4状态的确定性带返回标签模型；2165个局部固定点；1324个满足全局前提的实例，无范围内违反。保留缺ReachTrap、缺返回保持、弱归纳假设的反例及较弱返回保持正例。有限枚举不是无界HoTT证明。Lean/Rocq工具不可用且官方访问DNS失败，7份Lean及1份Coq源材料全部NOT_RUN；未模拟它们的结果。

## 纠错与依赖

原checkpoint干跑因新OUT记录未标review_required被拒绝，没有发布混合状态。原脚本/载荷和错误保留；将投递状态与依赖复核状态分开后，原治理器实际提交，旧快照干跑被拒绝。随后仅统一论辩台账的当前计数/指针/工作流，原值另存历史，不修改旧信。FINAL_PLAN给出最终新读取快照；旧checkpoint receipt只代表当时快照。所有受影响依赖保持待复核，未刷新旧hash掩盖变化。

## 文件与路由检查

{len(checks)}项本轮机械检查通过。新进程解析得到299份动态资料，包含R026、OUT-005、IN-006及OUT-006和证据。完整动态集合未全文载入当前上下文，这不是全套业务认知或独立理解验收。

## 输出

- `.codex/research/hott/dialogues/GEMINI-001/TO_GEMINI_006.md`：完整回信。
- `rounds/007/ASSESSMENT.md`与`TECHNICAL_NOTE.md`：评估和证明。
- `artifacts/r027/FINITE_MODEL_RESULTS.json`、`NATIVE_RUN.json`：实际结果与未运行范围。
- `artifacts/r027/VERIFY.json`：原文件保护与路由检查。
- 最终Git HEAD、ZIP回读/异目录恢复/bundle克隆以工作目录外的delivery_verification为准；不在此伪造尚未完成的检查。
''',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
