"""Decode actual inline Python file payloads, compare duplicates, and preserve them.
This is archival extraction/AST inspection only; no attached updater is executed.
"""
from pathlib import Path
import json, base64, ast, hashlib, datetime
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'scripts/recovered/HoTT2_json'; OUT=ROOT/'artifacts/r019'
doc=json.loads((ROOT/'HoTT/sources/external-audits/HoTT-2(1).json').read_text())
cs=doc['chunkedPrompt']['chunks']; rows=[]
for i,c in enumerate(cs):
    f=c.get('inlineFile')
    if not f: continue
    data=base64.b64decode(f['data'],validate=True)
    rel=f'scripts/recovered/HoTT2_json/attachment_c{i:03}.py'
    p=ROOT/rel
    if p.exists() and p.read_bytes()!=data: raise RuntimeError('Refusing changed attachment overwrite')
    p.write_bytes(data)
    text=data.decode('utf-8'); ast.parse(text)
    dup=[]
    for part in c.get('parts',[]):
        pd=part.get('inlineData')
        if pd and 'data' in pd: dup.append(base64.b64decode(pd['data'],validate=True)==data)
    eq=[q.relative_to(ROOT).as_posix() for q in SRC.glob('embedded_c*_script_content.py') if q.read_bytes()==data]
    rows.append({'chunk':i,'path':rel,'mime_type':f.get('mimeType'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'parts_byte_matches':dup,'matches_generated_script_content':eq,'python_ast_parse':'PASS','executed':False})
assert len(rows)==2
out={'schema_version':'hott-r019-attachment-inspection/v1','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'attachments':rows,'all_payload_duplicates_match':all(all(x['parts_byte_matches']) for x in rows),'note':'These are real attached Python updater files, not full prior repository, Lean proofs, or commit receipts.'}
(OUT/'ATTACHMENT_AUDIT.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
# Replace redundant base64 export with precise references; raw JSON remains intact.
(OUT/'INLINE_FILE_REFERENCES.json').write_text(json.dumps({'raw_original':'HoTT/sources/external-audits/HoTT-2(1).json','decoded_attachment_index':'artifacts/r019/ATTACHMENT_AUDIT.json','attachment_chunks':[r['chunk'] for r in rows],'raw_bytes_preserved':True},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
