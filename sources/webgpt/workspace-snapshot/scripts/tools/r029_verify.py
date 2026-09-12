#!/usr/bin/env python3
"""Verify persistence/protection only; not a mathematics or cognition validator."""
import hashlib, importlib.util, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def sha(x):return hashlib.sha256(x).hexdigest()
def main():
    baseline=json.loads((ROOT/'artifacts/r029/BASELINE.json').read_text())
    mutable={'AGENTS.md','HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md',
             'MEMORY.md','.codex/research/hott/FRONTIER.md','.codex/research/hott/LESSONS.md',
             '.codex/research/hott/RESUME.md','.codex/research/hott/STATE.json','.codex/cognition/HEAD.json'}
    changed=[];unchanged=0
    for row in baseline['files']:
        p=ROOT/row['path']
        if not p.is_file():raise AssertionError('Deleted original '+row['path'])
        if sha(p.read_bytes())!=row['sha256']:changed.append(row['path'])
        else:unchanged+=1
    assert set(changed)<=mutable,(changed,mutable)
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    prior=json.loads((ROOT/'artifacts/r029/before/AGENTS.md').read_text()) if False else None
    assert state['revision']==29
    assert len(state['records'])==71
    spec=importlib.util.spec_from_file_location('r029_verify_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    plan=rt.plan(ROOT)
    required=json.loads((ROOT/'artifacts/r029/CHECKPOINT_SUMMARY.json').read_text())['required_dynamic_paths']
    paths={d['path'] for d in plan['documents']}
    assert set(required)<=paths
    assert subprocess.run(['git','merge-base','--is-ancestor','ce5e8f3aed974ef11a252bafeb67b3d8df16bea2','HEAD'],cwd=ROOT).returncode==0
    u=(ROOT/'.codex/research/hott/reviews/SELF-REFERENCE-001/USER_MESSAGE_LATEST.md').read_text()
    assert '本来我觉得，找个悖论是很简单的事，尤其是自指型的，为什么你们找起来这么慢呢？' in u
    assert 'HoTT难道可以越过对其自身的自指吗？我不相信。' in u
    result={'status':'PASS_DOCUMENT_STATE_SCOPE','revision':29,'baseline_files':len(baseline['files']),
      'unchanged_original_files':unchanged,'changed_original_paths':changed,'deleted_original_files':[],
      'old_record_count':68,'new_record_count':71,'prior_history_retained':True,
      'all_required_dynamic_paths_present':True,'new_math_experiments':0,'native_proof':'NOT_RUN',
      'limits':'Hash/route checks do not certify understanding, theorem truth, or full research workflow.'}
    out=ROOT/'artifacts/r029/VERIFICATION.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    report='''# R029 交接报告\n\n当前工作为用户两问的直接解释、Gemini观点评估及授权吸收。当前revision29，继承revision28 Git，无重新初始化、无远端。\n\n实际完成：原消息保全；原自指专题回读与§8更新；同域全域忠实且覆盖自身反向项的评价器不相容的完整短证明；AGENTS调度纠偏；原checkpoint提交、过期快照拒绝、新依赖动态可读。\n\n未完成/未声称：没有原生HoTT机器证明，没有全理论规范性/一致性或物理崩溃证明，没有完整业务动态认知验收，没有新的Gemini发信或回复，没有新数学实验计数。\n\n代码先写scripts后执行。旧第五闭包、三问、Skills、Schema、主张矩阵、旧研究与结果保持原字节；原自指专题修改前备份见before。完整Git保留全部旧记录。\n\n直接入口：\n- `.codex/research/hott/reviews/SELF-REFERENCE-001/ASSESSMENT.md`\n- `.codex/research/hott/reviews/SELF-REFERENCE-001/PROOF_NOTE.md`\n- `HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md`\n- `MEMORY.md`\n\n有限文件校验见VERIFICATION.json；最终Git/ZIP/bundle与异目录恢复检查写在工作目录外的delivery_verification.json，避免污染已提交工作树。\n'''
    (ROOT/'artifacts/r029/REPORT.md').write_text(report)
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
