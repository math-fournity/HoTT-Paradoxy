"""Bounded independent audit; writes only new audit receipts and temporary copies.

This is an audit reproduction script, not a replacement canonical verifier.
"""
from pathlib import Path
import concurrent.futures, contextlib, datetime, hashlib, importlib.util
import io, json, os, re, shutil, subprocess, sys, tempfile

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
def run(label, argv, cwd=ROOT, env=None):
    p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True)
    (OUT / (label+'.stdout.txt')).write_bytes(p.stdout)
    (OUT / (label+'.stderr.txt')).write_bytes(p.stderr)
    return dict(label=label, argv=list(map(str,argv)), cwd=str(cwd), exit_code=p.returncode,
                stdout_sha256=sha(p.stdout), stderr_sha256=sha(p.stderr))

if __name__ == '__main__':
    report = Path('/Volumes/D/HoTT_AI_HANDOFF_20260911/audit/统观工作技术报告-20260913.md')
    body=report.read_bytes(); (OUT/'report-input.md').write_bytes(body)
    save('input-identity.json', dict(path=str(report),sha256=sha(body),bytes=len(body),
        captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        audit_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()))
    plan=json.loads(subprocess.check_output([sys.executable,'-B','.codex/tools/cognition_runtime.py','plan','--profile','governance'],cwd=ROOT))
    save('load-plan.json',plan)
    verifiers=['verify_governance_shards','verify_three_way_cognition','verify_understanding_merge',
               'verify_fresh_three_way','verify_ledger_retrodiction','verify_proof_version_closure']
    def check(v):
        args=[sys.executable,'-B',str(ROOT/'scripts/audit'/f'{v}.py')]
        if v=='verify_fresh_three_way': args+=['--output',str(OUT/'fresh-generated.json')]
        return run(v,args)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        checks=list(pool.map(check,verifiers))
    save('verifier-results.json',checks)
    print('canonical verifiers:',[(x['label'],x['exit_code']) for x in checks],flush=True)
    reg=json.loads((ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json').read_text())
    matrix=(ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md').read_text().splitlines()
    manifests=[]; claim_ids=[]
    for row in reg['later_packages']:
        d=ROOT/row['run']; receipt=json.loads((d/'RUN.json').read_text())
        manifest=json.loads((d/'source-manifest.json').read_text())
        index=json.loads((d/'index-row-manifest.json').read_text())
        issues=[]
        for f in manifest['files']:
            p=ROOT/f['path']
            if not p.is_file() or sha(p.read_bytes())!=f['sha256']: issues.append('SOURCE:'+f['path'])
        for key in ['stdout','stderr','environment','source_manifest']:
            f=receipt[key]; p=d/f['path']
            if not p.is_file() or sha(p.read_bytes())!=f['sha256']: issues.append('RECEIPT:'+key)
        for f in index['rows']:
            matches=[s for s in matrix if re.match(r'^\|\s*`?'+re.escape(f['id'])+r'`?\s*\|',s)]
            if len(matches)!=1 or sha(matches[0].encode())!=f['line_sha256']: issues.append('ROW:'+f['id'])
        claim_ids+=receipt['claim_ids']
        manifests.append(dict(proof_id=row['proof_id'],claims=receipt['claim_ids'],issues=issues))
    save('manifest-audit.json',dict(packages=manifests,declared_later_count=reg['later_machine_proved_claim_count'],
        receipt_unique_count=len(set(claim_ids)),receipt_claim_ids=claim_ids))
    toolchain=json.loads((ROOT/'HoTT/formal/ercf3-t3/TOOLCHAIN.json').read_text())
    cache=toolchain['runtime_cache']; env=os.environ.copy()
    env.update(XDG_DATA_HOME=cache['xdg_data_home'],XDG_CONFIG_HOME=cache['xdg_config_home'],TMPDIR=cache['tmpdir'])
    binary=toolchain['agda']['local_binary']
    assert sha(Path(binary).read_bytes())==toolchain['agda']['binary_sha256']
    replays=[]
    with tempfile.TemporaryDirectory(prefix='hott-t3-audit-') as temp:
        temp=Path(temp)
        for src in (ROOT/'HoTT/formal/ercf3-t3').glob('*.agda'): shutil.copy2(src,temp/src.name)
        for row in reg['later_packages']:
            if not row['proof_id'].startswith('MP-ERCF3-T3-'): continue
            argv=[binary,'--safe','--no-libraries','--ignore-interfaces','-i',str(temp),str(temp/Path(row['source']).name)]
            replays.append(run(row['proof_id']+'-safe-replay',argv,cwd=temp,env=env))
    save('safe-replay-results.json',replays)
    print('safe kernel replays:',[(x['label'],x['exit_code']) for x in replays],flush=True)
    spec=importlib.util.spec_from_file_location('closure_audit',ROOT/'scripts/audit/verify_proof_version_closure.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    mutations=[]
    # The verifier's module-level ROOT is explicitly redirected to a disposable
    # tree. Git commands remain read-only against the existing worktree index.
    for case in ['matrix-row','invalid-source','missing-stdout']:
        with tempfile.TemporaryDirectory(prefix='hott-verifier-audit-') as temp:
            temp=Path(temp)
            for p in ROOT.iterdir(): (temp/p.name).symlink_to(p,target_is_directory=p.is_dir())
            def materialize(relative):
                dest=temp
                parts=Path(relative).parts
                for part in parts[:-1]:
                    dest=dest/part
                    if dest.is_symlink():
                        original=dest.resolve(); dest.unlink();dest.mkdir()
                        for child in original.iterdir(): (dest/child.name).symlink_to(child,target_is_directory=child.is_dir())
                f=dest/parts[-1]
                if f.is_symlink():
                    original=f.resolve(); f.unlink();shutil.copy2(original,f)
                return f
            if case=='matrix-row':
                f=materialize('HoTT/CLAIM_EVIDENCE_MATRIX.md')
                data=f.read_text(); lines=data.splitlines(keepends=True)
                lines=[s.replace('该编码','AUDIT_CHANGED_CLAIM') if s.startswith('| C-168 |') else s for s in lines]
                f.write_text(''.join(lines))
            elif case=='invalid-source':
                f=materialize('HoTT/formal/ercf3-t3/RepairedSyntax.agda')
                f.write_text(f.read_text()+'\nAUDIT-INVALID : Nat\nAUDIT-INVALID = refl\n')
            else:
                f=materialize('HoTT/verification/runs/20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01/stdout.txt');f.unlink()
            mod.ROOT=temp;mod.REGISTRY=temp/'HoTT/verification/PROOF_VERSION_CLOSURE.json';mod.MATRIX=temp/'HoTT/CLAIM_EVIDENCE_MATRIX.md'
            output=io.StringIO()
            with contextlib.redirect_stdout(output): result=mod.main()
            mutations.append(dict(case=case,exit_code=result,stdout=output.getvalue(),
                original_files_modified=False,verifier_source_sha256=sha(Path(spec.origin).read_bytes())))
    save('verifier-mutation-results.json',mutations)
    print('disposable verifier mutations:',[(x['case'],x['exit_code']) for x in mutations],flush=True)
