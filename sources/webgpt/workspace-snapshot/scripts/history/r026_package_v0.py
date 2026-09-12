"""Validate, commit locally, and package R026 including inherited Git history.
No remote writes. All outputs have their actual hashes checked. File checks
are not formal mathematical proofs or independent cognition acceptance.
"""
from __future__ import annotations
import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r026'
REVIEW='.codex/research/hott/reviews/EARLY-GEMINI-001/'
BASE='0d7ef5e48c67ee3586606dc45fb9f4ef4a30a685'
DEST=ROOT.parent
FULL=DEST/'HoTT_early_reassessment_rev26_with_git.zip'
BUNDLE=DEST/'HoTT_early_reassessment_rev26.bundle'
SMALL=DEST/'HoTT_early_Gemini_review_R026.zip'
RECEIPT=DEST/'HoTT_early_reassessment_rev26_delivery_verification.json'
CHECKS=[]
LOG=[]

def sha(data):return hashlib.sha256(data).hexdigest()
def serial(obj):return json.dumps(obj,ensure_ascii=False,indent=2)+'\n'
def put(path,obj):
    path=Path(path)
    if path.exists():raise FileExistsError(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(obj if isinstance(obj,str) else serial(obj),encoding='utf-8')
def cmd(args,cwd=ROOT,timeout=60):
    args=[str(x) for x in args]
    start=datetime.now(timezone.utc).isoformat()
    p=subprocess.run(args,cwd=cwd,text=True,capture_output=True,timeout=timeout)
    LOG.append({'argv':args,'cwd':str(cwd),'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),
        'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    if p.returncode:raise RuntimeError(f'{args[0]} failed with {p.returncode}: {p.stderr}')
    return p.stdout.strip()
def git(*args,cwd=ROOT):
    return cmd(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd=cwd)
def check(name,condition,detail=None):
    CHECKS.append({'id':name,'status':'PASS' if condition else 'FAIL','detail':detail})
    if not condition:raise AssertionError(name)
def rows(text):
    return {line.split('|')[1].strip():[v.strip() for v in line.split('|')]
            for line in text.splitlines() if line.startswith('| C-')}

def main():
    for p in [FULL,BUNDLE,SMALL,RECEIPT]:
        if p.exists():raise FileExistsError(p)
    check('inherited_head',git('rev-parse','HEAD')==BASE)
    check('branch_main',git('branch','--show-current')=='main')
    check('no_remote',not git('remote'))
    original=(ROOT/(REVIEW+'ORIGINAL.md')).read_bytes()
    supplied=(DEST/'Pasted markdown(2).md').read_bytes()
    check('original_verbatim_bytes',original==supplied,{'bytes':len(original),'lines':len(original.splitlines()),'sha256':sha(original)})
    provenance=json.loads((ROOT/(REVIEW+'PROVENANCE.json')).read_text())
    # Read actual metadata without assuming a field alias proves a signature.
    check('provenance_present',bool(provenance) and 'Gemini' in (ROOT/(REVIEW+'PROVENANCE.json')).read_text())
    current=ROOT/'scripts/research/r026_early_ideas_checks.py'
    prior=ROOT/'scripts/history/r026_early_ideas_checks_v0.py'
    v0=json.loads((OUT/'CHECK_RESULTS.json').read_text())
    v1=json.loads((OUT/'CHECK_V1_RESULTS.json').read_text())
    check('executed_final_source_hash',sha(current.read_bytes())==v1['script_sha256'])
    check('executed_v0_preserved',sha(prior.read_bytes())==v0['script_sha256'])
    check('six_check_groups',v1['status']=='PASS_WITH_DECLARED_SCOPE' and v1['check_groups']==6)
    rc=v1['checks']['linear_resources']
    check('two_linear_derivations',len(rc['accepted_derivations'])==2)
    check('eight_invalid_objects_rejected',len(rc['negative_controls'])==8 and all(rc['negative_controls'].values()))
    check('ordinary_reference_duplication_positive',rc['contraction_without_linearity']=='ACCEPTED')
    check('independent_tokens_vs_alias',rc['two_distinct_tokens']==['p','q'] and rc['one_token_two_redemptions']==[True,False])
    check('native_scope_explicit',v1['native_hott_kernel']=='NOT_RUN' and v1['native_proof_assistant']=='NOT_AVAILABLE')
    for receipt in ['CHECK_EXECUTION.json','CHECK_V1_EXECUTION.json','WRITE_RECORDS_EXECUTION.json','CHECKPOINT_EXECUTION.json']:
        check('successful_'+receipt,json.loads((OUT/receipt).read_text())['exit_code']==0)
    check('search_unknown_not_refutation',v1['checks']['discovery_and_statement']['negative_search']=='NO_WITNESS_WITHIN_BUDGET')
    old_matrix=(OUT/'before/HoTT/CLAIM_EVIDENCE_MATRIX.md').read_text()
    new_matrix=(ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md').read_text()
    old_rows,new_rows=rows(old_matrix),rows(new_matrix)
    check('matrix_claim_ids_unchanged',old_rows.keys()==new_rows.keys())
    changed_rows=[]
    for key,old in old_rows.items():
        new=new_rows[key]
        if old!=new:
            changed_rows.append(key)
            check('matrix_only_evidence_'+key,len(old)==len(new) and all(a==b for i,(a,b) in enumerate(zip(old,new)) if i!=4))
    check('matrix_only_existing_12_16',set(changed_rows)=={f'C-{i:02}' for i in range(12,17)})
    cp=json.loads((OUT/'CHECKPOINT_SUMMARY.json').read_text())
    check('checkpoint26',cp['status']=='CHECKPOINT_COMMITTED' and cp['revision']==26)
    check('cognition_not_overclaimed',cp['full_business_cognition']=='NOT_CLAIMED')
    check('stale_write_rejected',json.loads((OUT/'checkpoint/STALE_BASE.json').read_text())['error']=='STALE_BASE')
    fresh=json.loads(cmd([sys.executable,'-B',ROOT/'scripts/session/r026_plan_check.py']))
    check('fresh_process_routing',fresh['revision']==26 and fresh['required_paths_present'])
    put(OUT/'FRESH_ROUTE.json',fresh)
    allowed={'MEMORY.md','scripts/README.md','HoTT/AUDIT_AND_RECONSTRUCTION.md','HoTT/CLAIM_EVIDENCE_MATRIX.md',
        '.codex/cognition/HEAD.json',*['.codex/research/hott/'+n for n in ['STATE.json','FRONTIER.md','LESSONS.md','RESUME.md']]}
    restore=json.loads((OUT/'RESTORE.json').read_text())
    changes=[];illegal=[];count=0
    for entry in restore['files']:
        path=entry['path']
        if path.startswith('.git/'):continue
        count+=1
        f=ROOT/path
        if not f.is_file() or sha(f.read_bytes())!=entry['sha256']:
            changes.append(path)
            if path not in allowed:illegal.append(path)
    check('protected_files_unchanged',not illegal,{'checked':count,'changed':changes,'violations':illegal})
    check('source_zip_unchanged',sha(Path(restore['archive']).read_bytes())==restore['archive_sha256'])
    for p in ROOT.glob('scripts/**/r026_*.py'):ast.parse(p.read_text(),filename=str(p))
    check('new_scripts_parse',True)
    for p in list(OUT.rglob('*.json'))+list((ROOT/REVIEW).glob('*.json')):json.loads(p.read_text())
    check('new_json_parse',True)
    check('no_symlinks',not any(p.is_symlink() for p in ROOT.rglob('*')))
    put(OUT/'REPORT.md','''# R026 · 早期Gemini思路回收、窄机器检查与文档更新

用户要求审视旧稿对未来的帮助，不以旧稿必须正确为前提。本轮明确：最终判决不成立，但资源使用、答案发现、规约形成三项责任可以保留；规约忠实性与版本变化值得恢复为探索位，不新增万能ASK门禁或三个已证悖论。

原稿497行、32478字节完整保全，历史撰写日期未验证。本轮不是IN-006，不改变现有来信/回信台账。旧主张C-12—C-16已记录类似缺口；本轮只补证据与解释，不升级数学标签。

六组新检查成功，包括两份线性正推导、八种无效输入拒绝、三个目标驱动证明合成和语境/规约变化的反例。检查器是明确的小语法片段，不是HoTT内核；有理数计算不证明物理本体；有限搜索失败不等于不存在证明。V0和原结果保留，增强版本V1单独记录。没有Lean/Agda/Rocq/Coq工具，未安装或运行原生证明。

更新：HoTT/AUDIT_AND_RECONSTRUCTION §3.5—3.7，矩阵C-12—C-16证据字段，scripts索引，最新MEMORY/FRONTIER/LESSONS/RESUME与STATE。第五闭包、三问、AGENTS、Skills、Schema和旧数学/实验保持原字节。

通过原checkpoint由25到26；新进程计划含本轮原文、评估、纸笔、代码与结果；旧快照写回被拒。完整动态正文集合未全文加载，本轮只认证用户明确要求的有界材料审读与维护。新Session可读取记录，但不声称已通过独立理解验收。

本地Git继承rev25历史，不push、不联络其他AI。完整ZIP包含.git并逐字节回读；异目录与bundle恢复结果及最终HEAD见外部delivery_verification。文件校验不是数学证明。
''')
    put(OUT/'FILE_CHECKS.json',{'scope':'FILE_AND_ROUTE_CHECKS_NOT_MATHEMATICAL_CERTIFICATION','checks':CHECKS.copy()})
    put(OUT/'PRECOMMIT_COMMANDS.json',LOG.copy())
    git('add','--all')
    git('commit','-m','Reassess early Gemini essay, check linear resources and specification fidelity, save R026')
    head=git('rev-parse','HEAD')
    check('clean_worktree_after_commit',not git('status','--porcelain'))
    git('fsck','--full')
    git('bundle','create',BUNDLE,'--all')
    git('bundle','verify',BUNDLE)
    check('git_integrity_and_bundle_verified',True)
    files=[p for p in sorted(ROOT.rglob('*')) if p.is_file()]
    with zipfile.ZipFile(FULL,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:z.write(p,ROOT.name+'/'+p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(FULL) as z:
        check('zip_crc',z.testzip() is None)
        check('zip_all_bytes',all(z.read(ROOT.name+'/'+p.relative_to(ROOT).as_posix())==p.read_bytes() for p in files))
    packet={}
    for p in (ROOT/REVIEW).iterdir():
        if p.is_file():packet[p.name]=p
    for rel in ['scripts/research/r026_early_ideas_checks.py','scripts/history/r026_early_ideas_checks_v0.py',
        'scripts/session/run_logged.py','artifacts/r026/CHECK_V1_RESULTS.json','artifacts/r026/CHECK_V1_EXECUTION.json',
        'artifacts/r026/CHECK_RESULTS.json','artifacts/r026/CHECK_EXECUTION.json','artifacts/r026/ENVIRONMENT.json',
        'artifacts/r026/REPORT.md']:
        packet[rel]=ROOT/rel
    manifest=[]
    with zipfile.ZipFile(SMALL,'w',zipfile.ZIP_DEFLATED) as z:
        for name,p in packet.items():
            b=p.read_bytes();z.writestr(name,b);manifest.append({'path':name,'bytes':len(b),'sha256':sha(b)})
        z.writestr('MANIFEST.json',serial({'files':manifest,'scope':'Old essay, explicit local reanalysis, and finite checks; not native HoTT proof.'}))
    with zipfile.ZipFile(SMALL) as z:
        check('small_packet_hashes',z.testzip() is None and all(sha(z.read(x['path']))==x['sha256'] for x in manifest))
    with tempfile.TemporaryDirectory(prefix='hott-r026-restore-') as temp:
        target=Path(temp)
        with zipfile.ZipFile(FULL) as z:
            for info in z.infolist():
                rel=PurePosixPath(info.filename)
                if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe archive path')
                if (info.external_attr>>16)&0o170000==0o120000:raise ValueError('Symlink in archive')
            z.extractall(target)
            for info in z.infolist():
                if not info.is_dir():
                    (target/info.filename).chmod(0o755 if (info.external_attr>>16)&0o111 else 0o644)
        restored=target/ROOT.name
        check('restored_same_head',git('rev-parse','HEAD',cwd=restored)==head)
        check('restored_clean',not git('status','--porcelain',cwd=restored))
        reloaded=json.loads(cmd([sys.executable,'-B',restored/'scripts/session/r026_plan_check.py'],cwd=target))
        check('relocated_same_routing',reloaded['snapshot']==fresh['snapshot'] and reloaded['required_paths_present'])
        clone=target/'bundle-clone'
        cmd(['git','-c','core.hooksPath=/dev/null','clone',BUNDLE,clone],cwd=target)
        check('bundle_same_head',git('rev-parse','HEAD',cwd=clone)==head)
        check('bundle_clean',not git('status','--porcelain',cwd=clone))
    outputs=[]
    for p in [FULL,BUNDLE,SMALL]:
        h=sha(p.read_bytes());put(str(p)+'.sha256',h+'  '+p.name+'\n')
        outputs.append({'path':str(p),'bytes':p.stat().st_size,'sha256':h})
    receipt={'status':'VERIFIED_FILES_AND_GIT','revision':26,'workspace':str(ROOT),'head':head,'inherited_head':BASE,
        'outputs':outputs,'checks':CHECKS,'passed':len(CHECKS),'commands':LOG,'workspace_files':len(files),
        'mathematical_check_groups':6,'invalid_linear_inputs_rejected':8,'native_hott_kernel':'NOT_RUN',
        'full_business_cognition':'NOT_CLAIMED','independent_audit':'NOT_RUN','old_canonical_claim_statuses_unchanged':True,
        'source_readback':'Byte identical to attached markdown','new_gemini_reply':'NONE_NOT_IN006'}
    put(RECEIPT,receipt)
    print(serial({k:receipt[k] for k in ['revision','head','passed','outputs','native_hott_kernel']}))

if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=ROOT.parent/'HoTT_early_reassessment_rev26_packaging_failure.json'
        if not failure.exists():
            failure.write_text(serial({'error':str(exc),'type':type(exc).__name__,'checks':CHECKS,'commands':LOG}),encoding='utf-8')
        raise
