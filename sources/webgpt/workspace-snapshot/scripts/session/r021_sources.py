"""Save primary-source web pages used to check new claims; no API/AI calls."""
from pathlib import Path
import datetime, hashlib, json, urllib.request
R=Path(__file__).resolve().parents[2];O=R/'artifacts/r021/web'
O.mkdir(parents=True,exist_ok=True)
sources=[
 ('W01','https://raw.githubusercontent.com/HoTT/book/master/logic.tex','logic-master.tex','Unique choice and mere-proposition LEM; master is not automatically the local pin'),
 ('W02','https://lean-lang.org/doc/reference/latest/Definitions/Modifiers/','lean-modifiers.html','noncomputable is a declaration/compilation boundary, not a theorem of algorithmic impossibility'),
 ('W03','https://lean-lang.org/doc/api/Lean/Compiler/ImplementedByAttr.html','lean-implemented-by.html','Alternative compiler implementation is a separate boundary requiring checks'),
 ('W04','https://rocq-prover.org/doc/v9.0/refman/addendum/extraction.html','rocq-9.0.1-extraction.html','Realizing axioms and explicit extraction mappings; not checked as running implementation'),
 ('W05','https://arxiv.org/abs/1607.04156','huber-canonicity.html','Abstract and scope only; no PDF analyzed or theorem reproved')]
rows=[]
for ident,url,name,scope in sources:
    target=O/name
    if target.exists():raise RuntimeError('Refuse overwrite')
    rec={'id':ident,'url':url,'read_scope':scope,'retrieved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Research archival reader'})
        with urllib.request.urlopen(req,timeout=15) as r:b=r.read();resolved=r.geturl();ct=r.headers.get('Content-Type','')
        target.write_bytes(b);rec.update(status='SAVED',path=str(target.relative_to(R)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),resolved_url=resolved,content_type=ct)
    except Exception as exc:rec.update(status='FAILED',error=f'{type(exc).__name__}: {exc}')
    rows.append(rec)
(O/'MANIFEST.json').write_text(json.dumps({'sources':rows,'earlier_web_failures':[{'url':'https://raw.githubusercontent.com/HoTT/book/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex','error':'web cache miss','fallback':'read locally pinned source and separately current master'},{'url':'https://raw.githubusercontent.com/HoTT/book/578b85cc8d586b1677ec4335148adeb443057d24/basics.tex','error':'web cache miss','fallback':'local pinned source'}]},ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'id':x['id'],'status':x['status'],'bytes':x.get('bytes'),'error':x.get('error')} for x in rows],ensure_ascii=False,indent=2))
