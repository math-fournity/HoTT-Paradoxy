"""Preserve exact discussion source and named speakers; collect scoped rule excerpts."""
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[2]; O=R/'artifacts/r020'; O.mkdir(parents=True,exist_ok=True)
D=R/'.codex/research/hott/dialogues/GEMINI-001'; D.mkdir(parents=True,exist_ok=True)
src=Path('/mnt/data/Pasted markdown(1).md'); data=src.read_bytes(); text=data.decode('utf-8')
def put(p,b):
    if isinstance(b,str): b=b.encode('utf-8')
    if p.exists() and p.read_bytes()!=b:raise RuntimeError('Refuse overwrite '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def sha(b):return hashlib.sha256(b).hexdigest()
put(D/'000_SOURCE.md',data)
blocks=list(re.finditer(r'^```[^\n]*\n(.*?)^```\s*$',text,re.M|re.S))
assert len(blocks)==5,len(blocks)
names=['001_USER_QUESTION.md','002_QUOTED_GPT_RESPONSE.md','003_USER_REFRAMING.md','004_USER_TO_GEMINI.md','005_GEMINI_ORIGINAL.md']
index=[]
for name,m in zip(names,blocks):
    body=m.group(1); b=body.encode('utf-8'); put(D/name,b)
    index.append({'path':str((D/name).relative_to(R)),'source_start_char':m.start(1),'source_end_char':m.end(1),'source_first_line':text[:m.start(1)].count('\n')+1,'source_last_line':text[:m.end(1)].count('\n'),'bytes':len(b),'sha256':sha(b),'verbatim_slice':True})
assert 'Gemini' in text and '99%' in blocks[-1].group(1)
numbered=''.join(f'{i:04d}: {line}\n' for i,line in enumerate(text.splitlines(),1))
put(O/'SOURCE_NUMBERED.txt',numbered)
put(O/'INPUT_MANIFEST.json',json.dumps({'schema_version':'hott-r020-input/v1','source':str(src),'sha256':sha(data),'bytes':len(data),'lines':len(text.splitlines()),'source_role':'user-supplied relayed exchange, not API-attested model identity','blocks':index,'quoted_rev24_path_available':(R/'.codex/research/hott/candidates/P-RESEARCH-PLAN-001/PLAN.md').is_file(),'full_input_read_in_current_turn':True,'scope':'Current markdown, not rerunning earlier JSON audits'},ensure_ascii=False,indent=2)+'\n')
selections=[('formal.tex',487,555,'contexts'),('formal.tex',984,1009,'axiomatic univalence'),('basics.tex',1628,1636,'function transport'),('basics.tex',1763,1780,'ua and computation'),('logic.tex',598,647,'truncation'),('logic.tex',801,838,'unique choice'),('hits.tex',13,35,'circle constructors'),('hits.tex',108,149,'HIT computation'),('hits.tex',1222,1236,'quotient recursor')]
parts=['# R020 本轮核对的固定书籍规则\n\n原文件未改；以下为精确节选，不冒称全书复核。\n']; ids=[]
for name,a,b,topic in selections:
    p=R/'HoTT/theory-schema/upstream/book-578b85cc'/name; raw=p.read_bytes(); lines=raw.decode().splitlines()
    parts += [f'\n## {topic}\n\n`{p.relative_to(R)}` L{a}—{b}; SHA256 `{sha(raw)}`\n\n```text\n', '\n'.join(f'{i+1}: {lines[i]}' for i in range(a-1,b)),'\n```\n']
    ids.append({'path':str(p.relative_to(R)),'lines':[a,b],'sha256':sha(raw)})
put(O/'SOURCE_EXCERPTS.md',''.join(parts));put(O/'SOURCE_IDENTITIES.json',json.dumps(ids,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_bytes':len(data),'source_lines':len(text.splitlines()),'speaker_blocks':len(index),'source_sha256':sha(data),'output':str(D)},ensure_ascii=False,indent=2))
