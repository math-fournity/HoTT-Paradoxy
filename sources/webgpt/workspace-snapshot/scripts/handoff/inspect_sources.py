#!/usr/bin/env python3
"""Audit archive metadata, source location boundaries, and legacy governance plan."""
from pathlib import Path
import hashlib, importlib.util, json, os, zipfile, collections
ROOT=Path(__file__).resolve().parents[2]; PKG=ROOT.parent

def save(n,o):
 p=PKG/'manifests'/n;p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
 src=json.loads((PKG/'manifests/SOURCE_INVENTORY.json').read_text())
 zips=[];flags=[]
 for e in src['entries']:
  if e['kind']!='file':continue
  p=Path(e['source'])
  if p.suffix.lower() in ['.ttf','.otf','.woff','.woff2']:flags.append({'path':str(p),'reason':'font-excluded'})
  if p.suffix.lower()!='.zip':continue
  try:
   with zipfile.ZipFile(p) as z:
    infos=z.infolist();names=[i.filename for i in infos]
    suspicious=[n for n in names if Path(n).suffix.lower() in ['.ttf','.otf','.woff','.woff2','.pem','.p12','.pfx'] or Path(n).name in ['.env','id_rsa','id_ed25519','credentials.json']]
    zips.append({'path':str(p),'entries':len(infos),'expanded_bytes':sum(i.file_size for i in infos),'top_level':sorted(set(n.split('/')[0] for n in names)),'suspicious_names':suspicious,'nested_zip_entries':[n for n in names if n.lower().endswith('.zip')]})
  except Exception as ex: flags.append({'path':str(p),'error':str(ex)})
 save('ARCHIVE_INVENTORY.json',{'archives':zips,'standalone_flags':flags,'metadata_audit_only':True})
 path=ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py'
 spec=importlib.util.spec_from_file_location('legacy_runtime',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 plan=m.plan(ROOT);save('GOVERNANCE_PLAN_BEFORE.json',plan)
 print(json.dumps({'archives':len(zips),'archive_flags':[a for a in zips if a['suspicious_names']],'standalone_flags':flags,'plan_keys':list(plan),'plan_documents':len(plan['documents']),'plan_bytes':sum(d.get('bytes',d.get('byte_count',0)) for d in plan['documents']),'sample_doc':plan['documents'][0],'revision':plan.get('revision'),'review_required_count':len(plan['review_required'])},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
