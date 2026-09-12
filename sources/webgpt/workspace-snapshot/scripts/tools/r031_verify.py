#!/usr/bin/env python3
"""Verify R031 identities, declared evidence scope, prior records and dynamic routing."""
from pathlib import Path
import argparse
import ast
import hashlib
import importlib.util
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r031'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def js(o):return json.dumps(o,ensure_ascii=False,indent=2)+'\n'
def runtime():
    s=importlib.util.spec_from_file_location('r031_verify_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--fresh',action='store_true');a=ap.parse_args()
    plan=runtime().plan(ROOT)
    checkpoint=json.loads((OUT/'CHECKPOINT_SUMMARY.json').read_text())
    paths={d['path'] for d in plan['documents']}
    assert plan['revision']==31
    assert set(checkpoint['required_paths'])<=paths
    assert plan['snapshot']==checkpoint['snapshot']
    if a.fresh:
        print(js({'status':'PASS_FRESH_DYNAMIC_PLAN','root':str(ROOT),'revision':31,
                  'documents':len(paths),'snapshot':plan['snapshot'],
                  'model_understanding_or_native_proofs_certified':False}));return
    baseline=json.loads((OUT/'RESTORE.json').read_text())
    allowed={'HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md','MEMORY.md',
      '.codex/research/hott/STATE.json','.codex/research/hott/FRONTIER.md',
      '.codex/research/hott/LESSONS.md','.codex/research/hott/RESUME.md','.codex/cognition/HEAD.json'}
    same=[];changed=[];missing=[]
    for row in baseline['files']:
        rel=row['path']
        if rel.startswith('.git/'):continue
        p=ROOT/rel
        if not p.is_file():missing.append(rel)
        elif sha(p)==row['sha256']:same.append(rel)
        else:changed.append(rel)
    assert not missing,missing
    assert set(changed)==allowed,changed
    before=json.loads((OUT/'before/.codex/research/hott/STATE.json').read_text())
    after=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    assert set(before['records'])<=set(after['records'])
    changed_records=[rid for rid,r in before['records'].items() if r!=after['records'][rid]]
    assert not changed_records,changed_records
    proofs=json.loads((OUT/'CERTIFICATES.json').read_text())
    assert proofs['source_sha256']==sha(ROOT/'scripts/research/r031_proof_reflection.py')
    assert len(proofs['positive_certificates'])==4
    assert len(proofs['negative_cases'])==14 and all(n['rejected'] for n in proofs['negative_cases'])
    bottom=proofs['positive_certificates']['conditional_loeb_BOTTOM']
    assert bottom['nodes_checked']==21
    assert set(bottom['closed_theorem_parameters'])=={'FP_forward','FP_backward','Reflection'}
    assert not bottom['hott_kernel_verification'] and not bottom['parameter_proofs_checked']
    positive=json.loads((OUT/'POSITIVE_REFLECTION.json').read_text())
    assert positive['source_sha256']==sha(ROOT/'scripts/research/r031_positive_control.py')
    assert positive['checker_sha256']==sha(ROOT/'scripts/research/r031_proof_reflection.py')
    assert positive['replay']['closed_theorem_parameters']==[]
    assert positive['replay']['nodes_checked']==4
    for name in ['TEST_EXECUTION','CERTIFICATE_EXECUTION','POSITIVE_EXECUTION','CHECKPOINT_EXECUTION']:
        r=json.loads((OUT/(name+'.json')).read_text())
        assert r['exit_code']==0 and r['timeout'] is False
    tests=json.loads((OUT/'TEST_EXECUTION.json').read_text())
    assert 'Ran 10 tests' in tests['stderr']
    assert json.loads((OUT/'NATIVE_STATUS.json').read_text())['formal_file_status']=='NOT_RUN'
    assert json.loads((OUT/'checkpoint/STALE.json').read_text())['error']=='STALE_BASE'
    agda=(ROOT/'scripts/research/r031_formal/ConditionalLoeb.agda').read_text()
    assert '{-# OPTIONS --safe --without-K #-}' in agda
    assert not any(line.lstrip().startswith('postulate') for line in agda.splitlines())
    assert 'sorry' not in agda
    syntax=[]
    for p in sorted(ROOT.glob('scripts/**/r031_*.py')):
        ast.parse(p.read_text(),filename=str(p));syntax.append(p.relative_to(ROOT).as_posix())
    test_source=ROOT/'scripts/tests/test_r031_proof_reflection.py'
    ast.parse(test_source.read_text(),filename=str(test_source))
    assert not subprocess.check_output(['git','remote'],cwd=ROOT,text=True).strip()
    subprocess.run(['git','-c','core.hooksPath=/dev/null','diff','--check'],cwd=ROOT,check=True)
    fresh=subprocess.run([sys.executable,'-B',str(Path(__file__).resolve()),'--fresh'],cwd='/mnt/data',text=True,capture_output=True,check=True)
    result={'status':'PASS_FILES_EVIDENCE_SCOPE_AND_ROUTING','revision':31,
      'unchanged_existing_files':len(same),'changed_existing_files':sorted(changed),'missing':missing,
      'prior_records':len(before['records']),'current_records':len(after['records']),
      'all_prior_record_contents_preserved':True,'dynamic_documents':len(paths),
      'positive_certificates':5,'negative_cases_rejected':14,'unit_tests':10,
      'native_proof':'NOT_RUN','full_business_cognition':'INCOMPLETE_AFTER_ACTUAL_COMPACTION',
      'new_python_syntax_checked':syntax+[test_source.relative_to(ROOT).as_posix()],
      'fresh_process':json.loads(fresh.stdout),
      'limits':'Byte identities, finite rule replay and route verification do not certify full HoTT or complete cognition.'}
    target=OUT/'VERIFICATION.json'
    if target.exists():raise FileExistsError(target)
    target.write_text(js(result),encoding='utf-8')
    report=f'''# R031 交接与验证

实际从revision30完整Git恢复，先提交恢复证据，再提交研究代码/测试/论文，之后以原治理器提交revision31。

## 数学与程序结果

完成条件Löb推导；在固定点与同T导出条件下，T证明Box P→P可变换为T证明P。完整HoTT编码/固定点未实现，不认领无条件HoTT实例或原创定理。

有限检查：5份成功证书（其中2份为保留3项外部封闭定理参数的21节点条件变换）；14类非法证书被拒；10项单元测试通过。已证公式的反射正例表明不是禁止所有自检查。没有原生Agda/Lean/Rocq；参数化Agda源文件未编译。

## 连续性

{len(same)}份既有非Git文件原字节不变，修改的8项为当前专题/索引/治理状态；原{len(before['records'])}个record内容全部保留，现为{len(after['records'])}项。新进程动态计划含{len(paths)}文件并包括R026、R030及本轮实质记录。旧快照写回被实际拒绝。

原闭包、三问、AGENTS、Skills、Schema、主张矩阵、旧代码/实验/往来信原文均保持原字节。完整两份核心正文曾11块输出，随后真实压缩，333份动态全集未完整输出；未认证完整业务前置。

## 交付

本地Git无远端，不push。所有新代码先写scripts再运行。最终HEAD/ZIP/bundle及其回读恢复结果由仓库外delivery verification保存，避免自身哈希循环。无外部AI交流或发信。
'''
    (OUT/'REPORT.md').write_text(report,encoding='utf-8')
    print(js(result))

if __name__=='__main__':main()
