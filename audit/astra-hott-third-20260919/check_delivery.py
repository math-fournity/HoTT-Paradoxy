#!/usr/bin/env python3
"""Check this audit's own links, sharding, KC coverage and pinned input drift."""
from pathlib import Path
from collections import Counter
import json,re,subprocess,sys
from audit_current import ROOT,OUT,row,sha,save

def main():
    index=ROOT/'Astra对击落HoTT工作的第三次审计.md'
    session=ROOT/'.codex/research/hott/sessions/S-AUD-20260919-ASTRA-HOTT-THIRD'
    files=[index,*sorted(index.with_suffix('').glob('*.md')),OUT/'README.md',OUT/'EXTERNAL-SOURCES.md',
           session/'SESSION.md',session/'CORE_COGNITION_AUDIT.md',*sorted((session/'CORE_COGNITION_AUDIT').glob('*.md'))]
    errors=[];count=0
    for p in files:
        for a,b in re.findall(r'\[[^\]\n]*\]\((?:<([^>]+)>|([^\s)]+))\)',p.read_text()):
            target=a or b
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://',target) or target.startswith('#'):continue
            target=target.split('#')[0];m=re.match(r'^(.*):(\d+)$',target);line=None
            if m:target,line=m.group(1),int(m.group(2))
            q=Path(target);q=q if q.is_absolute() else p.parent/q;count+=1
            if not q.exists():errors.append({'from':str(p.relative_to(ROOT)),'target':target,'error':'MISSING'})
            elif line and (not q.is_file() or line>len(q.read_text().splitlines())):errors.append({'target':target,'error':'LINE_OUT_OF_RANGE'})
    pairs=[]
    for p in sorted((session/'CORE_COGNITION_AUDIT').glob('*.md')):pairs+=re.findall(r'^\| (KC-\d{6}) \| (\w+) \|',p.read_text(),re.M)
    expected=re.findall(r'^### (KC-\d{6})',(ROOT/'核心认知.md').read_text(),re.M)
    r=subprocess.run([sys.executable,'-B','scripts/audit/validate_governance_shards.py',str(index),str(session/'CORE_COGNITION_AUDIT.md')],cwd=ROOT,capture_output=True)
    inputs=json.loads((OUT/'INPUT-BEFORE.json').read_text())['files']+json.loads((OUT/'CONTEXT-SOURCES.json').read_text())
    drift=[x['path'] for x in inputs if sha((ROOT/x['path']).read_bytes())!=x['sha256']]
    evidence=[p for p in sorted(OUT.rglob('*')) if p.is_file() and p.suffix not in ('.agdai','.pyc') and p.name not in ('DELIVERY-CHECK.json','EVIDENCE-MANIFEST.json')]
    save(OUT/'EVIDENCE-MANIFEST.json',{'schema_version':'astra-third-audit-evidence-manifest/v1','files':[row(p) for p in evidence]})
    result={'schema_version':'astra-third-audit-delivery/v1','head_at_check':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
            'report_shards':7,'files':[row(p) for p in files],'links_checked':count,'link_errors':errors,
            'kc_count':len(pairs),'kc_exact_order':[x[0] for x in pairs]==expected,'kc_relations':dict(Counter(x[1] for x in pairs)),
            'shard_exit':r.returncode,'shard_result':(r.stdout+r.stderr).decode(),'input_drift':drift,'evidence_files':len(evidence),
            'limits':'Structural checks do not certify logic, mathematical truth or complete literature coverage.'}
    save(OUT/'DELIVERY-CHECK.json',result);print(json.dumps({k:v for k,v in result.items() if k!='files'},ensure_ascii=False,indent=2))
    return int(bool(errors or drift or r.returncode or not result['kc_exact_order']))

if __name__=='__main__':raise SystemExit(main())
