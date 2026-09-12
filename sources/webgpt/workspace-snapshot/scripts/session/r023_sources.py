"""Pin read sources and current governance plan for a bounded reply assessment."""
from __future__ import annotations
import hashlib, importlib.util, json, shutil, sys, urllib.request
from pathlib import Path
from datetime import datetime, timezone
R=Path(__file__).resolve().parents[2]
O=R/'artifacts/r023'
D=R/'.codex/research/hott/dialogues/GEMINI-001/rounds/004'

def save(p:Path, data:bytes) -> None:
    if p.exists(): raise FileExistsError(str(p))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)

def js(obj): return (json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode()

def main():
    incoming=(D/'IN-003.md').read_bytes()
    save(D/'USER_REQUEST.md', ('这是它的回复，你打算如何吸收和回复？`` ` ``'+incoming.decode().rstrip('\n')+'``\n').encode())
    save(D/'PROVENANCE.json',js({'schema_version':'hott-incoming/v1','incoming':'IN-003',
        'origin':'Current user message quoting Gemini; manual full transcription, not provider-export bytes',
        'encoding':'UTF-8 LF; one terminal newline added','body_sha256':hashlib.sha256(incoming).hexdigest(),
        'body_bytes':len(incoming),'unicode_replacement_object_chars':incoming.decode().count('\ufffc'),
        'role':'Third incoming opinion, reply to OUT-002','no_direct_contact':True,
        'user_text_vs_peer_text':'USER_REQUEST.md preserves wrapper; IN-003.md isolates quoted peer body'}))
    engine=R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py'
    spec=importlib.util.spec_from_file_location('r023_runtime_sources',engine)
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    plan=rt.plan(R);save(O/'ENTRY_PLAN.json',js(plan))
    sources=[
      ('cubical-s1-base','https://raw.githubusercontent.com/agda/cubical/master/Cubical/HITs/S1/Base.agda','scripts/recovered/r023/cubical-s1-base.agda'),
      ('cubical-equality-s1','https://raw.githubusercontent.com/agda/cubical/master/Cubical/Data/Equality/S1.agda','scripts/recovered/r023/cubical-equality-s1.agda'),
      ('lean-validation','https://lean-lang.org/doc/reference/latest/ValidatingProofs/','artifacts/r023/sources/lean-validation.html'),
      ('lean-decide','https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/','artifacts/r023/sources/lean-tactics.html')]
    records=[]
    for name,url,rel in sources:
        item={'id':name,'url':url,'path':rel,'at_utc':datetime.now(timezone.utc).isoformat(),'executed':False}
        try:
            request=urllib.request.Request(url,headers={'User-Agent':'HoTT-research-source-check/1.0'})
            with urllib.request.urlopen(request,timeout=20) as response:
                data=response.read(12*1024*1024);item['resolved_url']=response.url
            save(R/rel,data);item.update(status='FETCHED',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        except Exception as exc:
            item.update(status='FETCH_FAILED',error=f'{type(exc).__name__}: {exc}')
        records.append(item)
    local='HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex'
    data=(R/local).read_bytes();lines=data.decode().splitlines()
    excerpts=['# R023 circle source excerpts\n\nLocal pinned upstream snapshot; not recompiled.\n']
    for lo,hi in [(323,349),(423,456),(497,538),(576,645)]:
        excerpts.append(f'\n## {local}:{lo}-{hi}\n\n```tex\n'+ '\n'.join(f'{i+1}: {lines[i]}' for i in range(lo-1,hi))+'\n```\n')
    save(O/'SOURCE_EXCERPTS.md',''.join(excerpts).encode())
    save(O/'SOURCE_REGISTRY.json',js({'remote':records,'local':{'path':local,'sha256':hashlib.sha256(data).hexdigest(),
        'read_ranges':[[323,349],[423,456],[497,538],[576,645]]},
        'toolchain':{x:shutil.which(x) for x in ('agda','lean','coqc','rocq')},
        'proof_assistant_run':False,'scope':'Source inspection only; no remote source executed'}))
    save(O/'READ_SCOPE.json',js({'task':'Bounded IN-003 evaluation and OUT-003 drafting, not autonomous business execution',
        'read':'AGENTS, governance/business skills, protocol, MEMORY, OUT-002, IN-003, RP-B01 PLAN, exact circle excerpts; remote selected rules',
        'full_dynamic_cognition':'NOT_CLAIMED','mandatory_policy_changed':False,
        'plan_documents':len(plan['documents']),'plan_total_bytes':plan.get('total_bytes'),
        'native_math_verification':'NOT_RUN','prior_parity_and_circle_discussion':'Checked with exact primary definitions, not an assumed old theorem'}))
    print(json.dumps({'revision':plan['revision'],'documents':len(plan['documents']),'remote':[(x['id'],x['status']) for x in records],
        'source_read_scope':'bounded; no full business cognition claim'},ensure_ascii=False))

if __name__=='__main__':main()
