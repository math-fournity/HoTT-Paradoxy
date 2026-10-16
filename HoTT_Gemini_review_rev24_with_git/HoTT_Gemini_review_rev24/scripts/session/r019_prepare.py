"""Restore supplied baseline and extract the audited conversation without executing its code."""
from pathlib import Path, PurePosixPath
import zipfile, hashlib, json, re, stat, collections, datetime
ROOT=Path(__file__).resolve().parents[2]
ZIP=Path('/mnt/data/HoTT_json_audit_rev18_with_git.zip')
SOURCE=Path('/mnt/data/HoTT-2(1).json')
PREFIX='HoTT_json_audit_rev18/'
def sha(b): return hashlib.sha256(b).hexdigest()
def put(p,b):
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists() and p.read_bytes()!=b: raise RuntimeError(f'Overwrite refused: {p}')
    if not p.exists(): p.write_bytes(b)
with zipfile.ZipFile(ZIP) as z:
    seen=set()
    for info in z.infolist():
        if not info.filename.startswith(PREFIX): raise RuntimeError(info.filename)
        name=info.filename[len(PREFIX):]
        if not name or info.is_dir(): continue
        p=PurePosixPath(name)
        if p.is_absolute() or '..' in p.parts or '\\' in name or stat.S_ISLNK(info.external_attr>>16): raise RuntimeError(name)
        if name in seen: raise RuntimeError('duplicate '+name)
        seen.add(name)
        put(ROOT/name,z.read(info))
input_rel='HoTT/sources/external-audits/HoTT-2(1).json'
put(ROOT/input_rel,SOURCE.read_bytes())
data=json.loads(SOURCE.read_text())
chunks=data['chunkedPrompt']['chunks']
OUT=ROOT/'artifacts/r019'; OUT.mkdir(parents=True,exist_ok=True)
code_dir=ROOT/'scripts/recovered/HoTT2_json';code_dir.mkdir(parents=True,exist_ok=True)
rows=[]; transcript=[];codes=[];results=[];refs=[]
for i,c in enumerate(chunks):
    parts=c.get('parts',[])
    isthought=c.get('isThought',False)
    body=c.get('text')
    if body is None: body=''.join(p.get('text','') for p in parts if not p.get('thought',False))
    row={'chunk':i,'role':c.get('role'),'time':c.get('createTime'),'isThought':isthought,'keys':list(c),'text_chars':len(body or '')}
    if not isthought and body:
        name=f'PUBLIC_c{i:03}.md';put(OUT/'messages'/name,body.encode())
        lines=(body.splitlines())
        row.update(public_file=f'artifacts/r019/messages/{name}',first_line=lines[0] if lines else '',headings=[l for l in lines if l.startswith('#')])
        transcript.extend([f'## CHUNK {i:03} | {c.get("role")} | {c.get("createTime")}', '',body,''])
        for n,m in enumerate(re.finditer(r'```([^\n]*)\n(.*?)\n```',body,re.S)):
            lang=m.group(1).strip().lower(); code=m.group(2)+'\n'
            ext={'python':'.py','lean':'.lean','lean4':'.lean','json':'.json'}.get(lang,'.txt')
            f=f'fence_c{i:03}_{n:02}{ext}';put(code_dir/f,code.encode())
            codes.append({'origin':'public_fence','chunk':i,'ordinal':n,'language':lang,'path':str((code_dir/f).relative_to(ROOT)),'sha256':sha(code.encode()),'bytes':len(code.encode())})
    # executableCode appears both at top level and in parts; de-duplicate within chunk.
    exe=[]
    if c.get('executableCode'): exe.append(c['executableCode'])
    exe += [p['executableCode'] for p in parts if 'executableCode' in p]
    unique={json.dumps(e,sort_keys=True):e for e in exe}
    for n,e in enumerate(unique.values()):
        code=e['code'];lang=e.get('language','');ext='.py' if lang.upper()=='PYTHON' else '.txt'
        f=f'executable_c{i:03}_{n:02}{ext}';put(code_dir/f,code.encode())
        codes.append({'origin':'executableCode','chunk':i,'ordinal':n,'language':lang,'path':str((code_dir/f).relative_to(ROOT)),'sha256':sha(code.encode()),'bytes':len(code.encode())})
        row.setdefault('executable_paths',[]).append(str((code_dir/f).relative_to(ROOT)))
    r=[]
    if 'codeExecutionResult' in c:r.append(c['codeExecutionResult'])
    r += [p['codeExecutionResult'] for p in parts if 'codeExecutionResult' in p]
    for e in {json.dumps(e,sort_keys=True):e for e in r}.values():
        results.append({'chunk':i,**e});row['execution_outcome']=e.get('outcome')
    for k in ['driveDocument','fileData','inlineData','groundingMetadata','webSearchQueries']:
        if k in c:refs.append({'chunk':i,'kind':k,'value':c[k]})
    rows.append(row)
old_path=Path('/mnt/data/HoTT.json')
old=json.loads(old_path.read_text()) if old_path.exists() else None
prefix_raw=0;prefix_public=0
if old:
    for a,b in zip(old['chunkedPrompt']['chunks'],chunks):
        if a!=b:break
        prefix_raw+=1
    for a,b in zip(old['chunkedPrompt']['chunks'],chunks):
        pa={k:a.get(k) for k in ['role','text','executableCode','codeExecutionResult','isThought']}
        pb={k:b.get(k) for k in ['role','text','executableCode','codeExecutionResult','isThought']}
        if pa!=pb:break
        prefix_public+=1
summary={'source':str(SOURCE),'sha256':sha(SOURCE.read_bytes()),'bytes':SOURCE.stat().st_size,'chunk_count':len(chunks),'role_counts':dict(collections.Counter(c.get('role') for c in chunks)), 'thought_chunk_count':sum(bool(c.get('isThought')) for c in chunks),'public_text_count':sum('public_file'in r for r in rows),'code_count':len(codes),'executed_blocks':sum(e['origin']=='executableCode' for e in codes),'result_count':len(results),'old_chunk_count':len(old['chunkedPrompt']['chunks']) if old else None,'identical_raw_prefix_chunks':prefix_raw,'identical_content_prefix_chunks':prefix_public,'old_sha256':sha(old_path.read_bytes()) if old else None,'external_reference_count':len(refs),'raw_is_preserved':True,'opaque_thought_signatures_interpreted':False}
for f,obj in [('INPUT_SUMMARY.json',summary),('CHUNK_INDEX.json',rows),('CODE_INDEX.json',codes),('RECORDED_EXECUTIONS.json',results),('EXTERNAL_REFERENCES.json',refs)]:
    put(OUT/f,(json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode())
put(OUT/'PUBLIC_TRANSCRIPT.md',('\n'.join(transcript)+'\n').encode())
print(json.dumps(summary,ensure_ascii=False,indent=2))
for r in rows:
    if not r['isThought']:print(json.dumps(r,ensure_ascii=False))
