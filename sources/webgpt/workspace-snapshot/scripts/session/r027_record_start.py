"""Record the preservation baseline and literal inbound code before any experiments."""
from pathlib import Path
import re, hashlib, json, datetime
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'.codex/research/hott/dialogues/GEMINI-001/rounds/007'
OUT=ROOT/'artifacts/r027'
def main():
    source=(D/'IN-006.md').read_bytes()
    code=[]
    recdir=ROOT/'scripts/recovered/Gemini_IN006'; recdir.mkdir(parents=True,exist_ok=True)
    for n,match in enumerate(re.finditer(r'```lean\n(.*?)\n```',source.decode(),re.S),1):
        p=recdir/f'snippet_{n:02d}.lean'
        p.write_text(match.group(1)+'\n')
        code.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'VERBATIM_EXTRACTED_NOT_EXECUTED'})
    row={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':'Current user-relayed Gemini text; no provider signature authentication','inbound':'IN-006','responds_to':'OUT-005','source_sha256':hashlib.sha256(source).hexdigest(),'bytes':len(source),'fenced_lean_snippets':code,'continuity':{'inherited_revision':26,'keep_r025_assessment':True,'keep_r026_review_and_specification_exploration':True},'full_business_cognition':'NOT_CERTIFIED; bounded explicit correspondence audit, actual task-specific reads recorded separately','new_native_proof_from_peer':False,'direct_AI_communication':False}
    (D/'PROVENANCE.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
    (OUT/'START_RECORD.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(row,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
