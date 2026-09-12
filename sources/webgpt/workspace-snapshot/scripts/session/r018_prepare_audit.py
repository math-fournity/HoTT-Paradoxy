"""Restore an immutable supplied baseline and extract public transcript evidence.
All transformations are preserved in this file; never execute opaque transcript data.
"""
from pathlib import Path, PurePosixPath
import hashlib, json, re, shutil, stat, zipfile

ROOT=Path(__file__).resolve().parents[2]
ZIP=Path('/mnt/data/HoTT_workspace_rev17_with_git.zip')
INPUT=Path('/mnt/data/HoTT.json')
OUT=ROOT/'artifacts/r018'
OUT.mkdir(parents=True, exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
rows=[]
with zipfile.ZipFile(ZIP) as z:
    for i in z.infolist():
        p=PurePosixPath(i.filename)
        if p.parts[0] != 'HoTT_workspace_rev17' or '..' in p.parts or p.is_absolute():
            raise ValueError('Unexpected archive path '+str(p))
        r=PurePosixPath(*p.parts[1:])
        if not r.parts: continue
        if stat.S_ISLNK(i.external_attr>>16): raise ValueError('Symlink '+str(p))
        d=ROOT.joinpath(*r.parts)
        if i.is_dir(): d.mkdir(parents=True,exist_ok=True); continue
        b=z.read(i)
        if d.exists() and d.read_bytes()!=b: raise ValueError('Refuse overwrite '+str(d))
        d.parent.mkdir(parents=True,exist_ok=True)
        d.write_bytes(b)
        mode=(i.external_attr>>16)&0o777
        if mode: d.chmod(mode & 0o755)
        rows.append({'path':r.as_posix(),'sha256':sha(b),'bytes':len(b)})
raw=INPUT.read_bytes(); data=json.loads(raw)
arch=ROOT/'HoTT/sources/external-audits/HoTT.json'
arch.parent.mkdir(parents=True,exist_ok=True); arch.write_bytes(raw)
chunks=data['chunkedPrompt']['chunks']
public=[]; codes=[]; embedded_results=[]; suppressed=0; placeholders=[]
for j,c in enumerate(chunks):
    if c.get('isThought'):
        suppressed+=1;continue
    if 'driveDocument' in c:
        placeholders.append({'chunk_index':j,'kind':'driveDocument','content_present':False})
    txt=c.get('text')
    if txt:
        record={'chunk_index':j,'role':c.get('role'),'createTime':c.get('createTime'),'text':txt}
        public.append(record)
        for n,m in enumerate(re.finditer(r'^```(\w+)\n(.*?)^```',txt,re.M|re.S),1):
            lang,body=m.groups(); ext={'lean':'lean','python':'py'}.get(lang,'txt')
            codes.append({'chunk_index':j,'role':c.get('role'),'language':lang,'text':body,'origin':'text_fence','name':f'transcript_c{j:03d}_{n}.{ext}'})
    if 'executableCode' in c:
        e=c['executableCode'];codes.append({'chunk_index':j,'language':e['language'],'text':e['code'],'origin':'executableCode','name':f'transcript_c{j:03d}.py'})
    if 'codeExecutionResult' in c:
        embedded_results.append({'chunk_index':j,**c['codeExecutionResult']})
code_dir=ROOT/'scripts/recovered/HoTT_json';code_dir.mkdir(parents=True,exist_ok=True)
for c in codes:
    b=c.pop('text').encode(); p=code_dir/c['name'];p.write_bytes(b);c.update(path=str(p.relative_to(ROOT)),bytes=len(b),sha256=sha(b))
text='\n\n'.join(f"## Chunk {r['chunk_index']:03d} | {r['role']} | {r['createTime']}\n\n{r['text']}" for r in public)+'\n'
(OUT/'PUBLIC_TRANSCRIPT.md').write_text(text,encoding='utf-8')
manifest={'input_path':str(INPUT),'input_sha256':sha(raw),'input_bytes':len(raw),'chunks':len(chunks),'public_message_count':len(public),'thought_chunks_excluded_from_audit_projection':suppressed,'text_parts_policy':'top-level text only; parts are duplicated streaming content; thoughtSignature preserved in raw only','external_document_references':placeholders,'extracted_code':codes,'embedded_execution_results':embedded_results,'model_runtime_identity':'Not independently verifiable from exported model alias','lean_execution_records_in_export':0}
(OUT/'TRANSCRIPT_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(OUT/'RESTORE_BASELINE.json').write_text(json.dumps({'zip':str(ZIP),'sha256':sha(ZIP.read_bytes()),'files':rows},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in manifest.items() if k not in ('embedded_execution_results',)},ensure_ascii=False,indent=2))
