"""Save targeted read identity and source excerpts, not a full-cognition certificate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, importlib.util, json, sys
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'artifacts/r024'
engine=ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py'
spec=importlib.util.spec_from_file_location('r024_read_runtime',engine)
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
p=rt.plan(ROOT)
(OUT/'ENTRY_PLAN.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
parts=[]; identities=[]
base='HoTT/theory-schema/upstream/book-578b85cc/'
for name,start,end in [('hits.tex',110,153),('formal.tex',978,1010),('basics.tex',1624,1645),('basics.tex',1760,1785),('homotopy.tex',320,352),('homotopy.tex',420,461),('logic.tex',800,842)]:
    rel=base+name; data=(ROOT/rel).read_bytes();lines=data.decode().splitlines()
    identities.append({'path':rel,'sha256':hashlib.sha256(data).hexdigest(),'line_start':start,'line_end':end})
    parts.append(f'## {rel}:{start}-{end}\n\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in range(start-1,min(end,len(lines)))))
(OUT/'SOURCE_EXCERPTS.md').write_text('# R024 targeted original-rule excerpts\n\n'+'\n\n'.join(parts)+'\n')
body=ROOT/'.codex/research/hott/dialogues/GEMINI-001/rounds/005/IN-004.md'
provenance={'id':'IN-004','received_date':'2026-09-11','via':'Current user-pasted message',
 'bytes':body.stat().st_size,'sha256':hashlib.sha256(body.read_bytes()).hexdigest(),
 'capture':'Manual full transcription of visible quoted body, UTF-8 LF; no independent platform-export byte comparison',
 'header_original':'致 OUT-002','responds_to_inferred':'OUT-003',
 'binding_evidence':'J01-J05 identifiers and explicit wording match OUT-003, not OUT-002 H01-H06; original header unedited.',
 'identity_authenticated':False,'direct_model_contact':False}
(body.parent/'PROVENANCE.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
read_scope={'task':'Bounded incoming-response review with targeted implementation checks',
 'runtime_utc':datetime.now(timezone.utc).isoformat(),'plan_revision':p['revision'],'plan_documents':len(p['documents']),
 'governance_entries_read':['AGENTS.md','.codex/skills/hott-session-governance/SKILL.md','.codex/skills/hott-paradox-research/SKILL.md','MEMORY.md','.codex/cognition/LOAD_SET.json','.codex/cognition/PROTOCOL.md'],
 'actual_argument_sources':identities,
 'full_business_cognition':'NOT_CLAIMED; all mandatory dynamic documents not loaded; no policy change',
 'new_native_hott_theorem':'NOT_RUN','source_review':'Local pinned source and official web pages are separate evidence channels'}
(OUT/'READ_SCOPE.json').write_text(json.dumps(read_scope,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'revision':p['revision'],'documents':len(p['documents']),'incoming_bytes':body.stat().st_size,'source_sections':len(identities),'full_business_cognition':'NOT_CLAIMED'},ensure_ascii=False))
