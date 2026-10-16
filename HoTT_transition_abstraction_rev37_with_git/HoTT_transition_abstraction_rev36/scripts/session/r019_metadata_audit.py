"""Inspect all exported chunks and attached code; isolate governance fault probes."""
from pathlib import Path
import json, ast, hashlib, difflib, io, contextlib, tempfile, runpy, subprocess, builtins, shutil, datetime
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'artifacts/r019';SRC=ROOT/'scripts/recovered/HoTT2_json'
d=json.loads((ROOT/'HoTT/sources/external-audits/HoTT-2(1).json').read_text());cs=d['chunkedPrompt']['chunks']
records=[];attachments=[];embedded=[];covered=[]
for i,c in enumerate(cs):
    if 'inlineFile' in c: attachments.append({'chunk':i,'inlineFile':c['inlineFile'],'parts_metadata':[list(p.keys()) for p in c.get('parts',[])]})
    if c.get('isThought'):kind='thought_metadata_not_used_as_proof'
    elif 'executableCode' in c:kind='reviewed_source_code'
    elif 'codeExecutionResult' in c:kind='reviewed_recorded_execution'
    elif c.get('text'):kind='reviewed_public_text'
    elif c.get('driveDocument'):kind='external_reference_without_body'
    elif c.get('inlineFile'):kind='inline_file_reference'
    else:kind='other'
    covered.append({'chunk':i,'kind':kind})
for n in sorted(SRC.glob('executable_*.py')):
    text=n.read_text(); tree=ast.parse(text)
    chunk=int(n.stem.split('_')[1][1:]);r={'chunk':chunk,'path':str(n.relative_to(ROOT)),'imports':[],'calls':[],'functions':[],'classes':[]}
    for node in ast.walk(tree):
        if isinstance(node,(ast.Import,ast.ImportFrom)):r['imports'].append(ast.get_source_segment(text,node))
        if isinstance(node,ast.Call):r['calls'].append({'line':node.lineno,'function':ast.unparse(node.func)})
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):r['functions'].append(node.name)
        if isinstance(node,ast.ClassDef):r['classes'].append(node.name)
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Name) and target.id in ['script_content','content'] and isinstance(node.value,ast.Constant) and isinstance(node.value.value,str):
                    b=node.value.value.encode();ext='.py' if target.id=='script_content' else '.md'
                    rel=f'scripts/recovered/HoTT2_json/embedded_c{chunk:03}_{target.id}{ext}'
                    p=ROOT/rel;p.write_bytes(b)
                    embedded.append({'parent_chunk':chunk,'variable':target.id,'path':rel,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
    records.append(r)
    # Stable numbered views of exact code for audit cross-referencing.
    (OUT/'messages'/f'CODE_c{chunk:03}.txt').write_text('\n'.join(f'{j:04} | {l}' for j,l in enumerate(text.splitlines(),1))+'\n')
(OUT/'CODE_AST_AUDIT.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(OUT/'INLINE_FILE_REFERENCES.json').write_text(json.dumps(attachments,ensure_ascii=False,indent=2)+'\n')
(OUT/'EMBEDDED_SOURCE_INDEX.json').write_text(json.dumps(embedded,ensure_ascii=False,indent=2)+'\n')
(OUT/'COVERAGE.json').write_text(json.dumps({'source_chunks':len(cs),'coverage':covered,'basis':'all public text, code and outputs; metadata only for thoughts and opaque signatures; no claim about missing Drive content'},ensure_ascii=False,indent=2)+'\n')
# Test the success print without permitting any actual path write or Git command.
real_open=builtins.open;stdout=io.StringIO();calls=[]
with tempfile.TemporaryDirectory(prefix='governance-fault-probe-') as td:
    tmp=Path(td);(tmp/'认知闭包').mkdir()
    def mapped_open(file,*args,**kwargs):
        name=str(file);prefix='/mnt/data/HoTT_workspace_rev16/'
        if name.startswith(prefix):return real_open(tmp/name[len(prefix):],*args,**kwargs)
        # runpy reads the reviewed script; no other writes allowed
        mode=args[0] if args else kwargs.get('mode','r')
        if any(x in mode for x in ('w','a','x','+')):raise RuntimeError('Unexpected write '+name)
        return real_open(file,*args,**kwargs)
    def failed_git(argv,*args,**kwargs):
        assert argv[0]=='git'
        calls.append({'argv':argv,'declared_cwd':kwargs.get('cwd'),'simulated_returncode':1})
        return subprocess.CompletedProcess(argv,1,'','INJECTED_GIT_FAILURE')
    with patch('builtins.open',mapped_open),patch('subprocess.run',failed_git),contextlib.redirect_stdout(stdout):
        runpy.run_path(str(SRC/'executable_c055_00.py'),run_name='r019_fault_probe')
    produced={p.relative_to(tmp).as_posix():len(p.read_bytes()) for p in tmp.rglob('*') if p.is_file()}
(OUT/'GOVERNANCE_FAULT_PROBE.json').write_text(json.dumps({'scope':'controlled fault injection, not replay of historical Git outcome','all_git_commands_simulated':True,'real_git_executed':False,'original_absolute_paths_redirected_to_temporary_directory':True,'calls':calls,'stdout':stdout.getvalue(),'success_claim_printed_despite_failure':'已提交' in stdout.getvalue(),'temporary_files':produced,'temp_cleaned':True,'original_commit_status':'UNVERIFIED; source ignores return codes, log contains only init and print, no commit hash'},ensure_ascii=False,indent=2)+'\n')
# Compare generated "complete original" to the real requested text; do not alter either.
content=(SRC/'embedded_c055_content.md').read_text()
quoted=content.split('### 1. 用户的完整原文',1)[1].split('### 2.',1)[0]
original=cs[38]['text']
(OUT/'GOVERNANCE_TEXT_FIDELITY.json').write_text(json.dumps({'chunk38_user_chars':len(original),'generated_claimed_verbatim_chars':len(quoted),'exact_user_text_present':original in content,'duplicate_added_word_present':'所有所有' in quoted,'preamble_not_part_of_chunk38':'其实所有的我们已经处理过的那些悖论' in quoted,'note':'Generated record combines prior material, changes wording/formatting, omits opening recording request; not byte-verbatim current user text.'},ensure_ascii=False,indent=2)+'\n')
(OUT/'TOOLCHAIN_STATUS.json').write_text(json.dumps({'observed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'paths':{n:shutil.which(n) for n in ('lean','lake','elan','agda','coqc','git','python3')},'supplied_lean_code_executed':False,'reason':'No local Lean/Agda/Coq executables found; no dependency installation performed. The supplied Lean code remains incomplete and unexecuted.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'covered_chunks':len(covered),'executable_source_blocks':len(records),'embedded_sources':embedded,'inline_files':attachments,'governance_fault_probe_success_printed':'已提交' in stdout.getvalue(),'toolchain':{n:shutil.which(n) for n in ('lean','lake','elan','agda','coqc')}},ensure_ascii=False,indent=2))
