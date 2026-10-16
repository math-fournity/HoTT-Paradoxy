#!/usr/bin/env python3
"""Read-only audit inputs; write derived receipts and exact selected source copies here."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
EXT = Path('/Volumes/D/HoTT-machine-overview')

def sha(b):
    return hashlib.sha256(b).hexdigest()

def main():
    inputs = [
        'audit/imports/machine-overview-strategy-20260913/HoTT非现实性悖论机器统观完整方案/001 - 研究目标与完成边界.md',
        'audit/imports/machine-overview-strategy-20260913/HoTT非现实性悖论机器统观完整方案/005 - 六条研究线与首轮实验.md',
        '.codex/research/hott/PREMISE-001/001 - 分母 V1 冻结（A-G 条目、P1 前提与出处）.md',
        '.codex/research/hott/PREMISE-001/003 - P2 逐条登记 C-G 恒等等价与设计决策.md',
        'HoTT/generators/GEN-001/GEN-001-REPORT.md',
        'HoTT/generators/GEN-001/GEN-001-DIVISIBILITY-REPORT.md',
        'HoTT/generators/GEN-001/GEN-001-V2-1-REPORT.md',
        'HoTT/generators/GEN-001/GEN-001-V2-1-ENUMERATION.json',
        'HoTT/generators/PROBE-INTERVAL-I/PROBE-INTERVAL-I-REPORT.md',
        'audit/PREMISE-001-V1信封外遗漏审计-20260916.md',
        'audit/PREMISE-001-STEP6-OMISSION-AUDIT-20260916.md',
        'sources/prompts/Codex-理论经济与针对性悖论策略-用户原文-20260922.md',
    ]
    rows=[]
    for rel in inputs:
        b=(ROOT/rel).read_bytes()
        rows.append(dict(path=rel, sha256=sha(b), bytes=len(b), lines=len(b.splitlines())))
    copies=[]
    for rel in ['machine-overview/registry.json','machine-overview/machine_overview/search.py',
                'machine-overview/machine_overview/v2_cofibration.py',
                'machine-overview/formal/IntervalIForms.agda',
                'machine-overview/formal/IntervalIBoolDiscriminator.agda',
                'machine-overview/formal/IntervalIEqualityAttempt.agda']:
        b=(EXT/rel).read_bytes()
        dest=HERE/'source-samples'/rel
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(b)
        git=subprocess.run(['git','-C',str(EXT),'show','HEAD:'+rel],capture_output=True)
        copies.append(dict(original=str(EXT/rel),snapshot=str(dest.relative_to(ROOT)),sha256=sha(b),
                           matches_head=git.returncode==0 and git.stdout==b))
    runs=[]
    for name in ['VERIFY-GEN001-DIVISIBILITY-WV-0025','20260916-VERIFY-GEN001-WITNESS-RECOVERY-040']:
        base=ROOT/'HoTT/verification/runs'/name
        run=json.loads((base/'RUN.json').read_text())
        hashes={p:sha((base/'generated'/p).read_bytes())==v['sha256'] for p,v in run['generated_sources'].items()}
        assert all(hashes.values()), (name,hashes)
        runs.append(dict(path=str(base.relative_to(ROOT)),status=run['status'],
                         claim_relation=run['claim_relation'],generated_hash_checks=hashes,
                         saved_kernel_runs=[{k:r[k] for k in ('label','exit_code','status') if k in r}
                                            for r in run['kernel_runs']],
                         replayed_in_this_audit=False))
    probes=[]
    for name in ['PROBE-INTERVAL-I-FORMS','PROBE-INTERVAL-I-BOOL-DISC','PROBE-INTERVAL-I-EQ-ATTEMPT']:
        base=EXT/'machine-overview/runs'/name
        run=json.loads((base/'RUN.json').read_text())
        checks={}
        for kernel in run['kernels']:
            for key,item in kernel['artifacts'].items():
                checks[key]=sha((base/item['path']).read_bytes())==item['sha256']
        # An audit records historical integrity failures; it must not rewrite the receipt.
        assert all(checks[k] for k in ('environment','stderr','stdout')),(name,checks)
        command=json.loads((base/'command.json').read_text())
        argv_matches=command['argv']==run['kernels'][0]['command_argv']
        dest=HERE/'probe-receipts'/name
        dest.mkdir(parents=True,exist_ok=True)
        for file in ('RUN.json','stdout.txt','stderr.txt','command.json','environment.txt','source-manifest.json'):
            (dest/file).write_bytes((base/file).read_bytes())
        probes.append(dict(run=name,artifact_hash_checks=checks,command_argv_matches_run=argv_matches,
                           command_expected=run['kernels'][0]['artifacts']['command'],
                           command_actual_sha256=sha((base/'command.json').read_bytes()),
                           integrity_status='COMMAND_BYTES_DRIFT_ARGUMENTS_MATCH' if not checks['command'] and argv_matches else 'CHECKED',
                           exits=[k['exit_code'] for k in run['kernels']],replayed_in_this_audit=False))
    source=(ROOT/inputs[-1]).read_text().splitlines()
    core=(ROOT/'核心认知.md').read_text()
    new=core.split('### KC-000047',1)[1]
    exact={str(n):source[n-1] in new for n in (9,12)}
    assert all(exact.values())
    ev=dict(schema='bounded-source-audit/v1',root=str(ROOT),
            baseline='4e0a7999fe88',external_head=subprocess.check_output(['git','-C',str(EXT),'rev-parse','HEAD'],text=True).strip(),
            inputs=rows,external_source_samples=copies,selected_saved_runs=runs,selected_probe_receipts=probes,
            user_paragraphs_exact_in_new_core=exact,new_math_claims=[],new_kernel_runs=[],
            scope='Selected source and saved receipt audit; not full historical replay or semantic certification.',
            primary_web=[dict(url='https://agda.readthedocs.io/en/v2.8.0/language/cubical.html',
                              sections=['The interval and path types','Partial elements'],access_date='2026-09-23',
                              level='SOURCE_REPORTED_NOT_REPLAYED'),
                         dict(url='https://arxiv.org/abs/1611.02108',version='v1',scope='abstract and theory identity')])
    (HERE/'EVIDENCE.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'inputs':len(rows),'source_copies':len(copies),'runs':len(runs),'probes':probes,
                      'exact_paragraphs':exact,'status':'AUDIT_COMPLETE_WITH_RECORDED_RECEIPT_DRIFT'},ensure_ascii=False))

if __name__=='__main__':
    main()
