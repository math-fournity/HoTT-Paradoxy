#!/usr/bin/env python3
"""Bounded structure/link/identity check of this audit's own deliverables."""
from pathlib import Path
from collections import Counter
import json, re, subprocess, sys
from audit_repairs import ROOT, OUT, file_row, save, sha

def main():
    session=ROOT/'.codex/research/hott/sessions/S-AUD-20260919-ASTRA-HOTT-SECOND'
    index=ROOT/'Astra对击落HoTT工作的第二次审计.md'
    files=[index,*sorted(index.with_suffix('').glob('*.md')),OUT/'README.md',
           session/'SESSION.md',session/'CORE_COGNITION_AUDIT.md',
           *sorted((session/'CORE_COGNITION_AUDIT').glob('*.md'))]
    errors=[];links=0
    for p in files:
        for a,b in re.findall(r'\[[^\]\n]*\]\((?:<([^>]+)>|([^\s)]+))\)',p.read_text()):
            target=a or b
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://',target) or target.startswith('#'):continue
            target=target.split('#')[0]
            m=re.match(r'^(.*):(\d+)$',target)
            line=None
            if m:target,line=m.group(1),int(m.group(2))
            q=Path(target);q=q if q.is_absolute() else p.parent/q
            links+=1
            if not q.exists():errors.append({'from':str(p.relative_to(ROOT)),'target':target,'error':'missing'})
            elif line is not None and (not q.is_file() or line>len(q.read_text().splitlines())):
                errors.append({'from':str(p.relative_to(ROOT)),'target':target,'error':'line_out_of_range'})
    kcs=[];relations=[]
    for p in sorted((session/'CORE_COGNITION_AUDIT').glob('*.md')):
        for k,rel in re.findall(r'^\| (KC-\d{6}) \| (\w+) \|',p.read_text(),re.M):
            kcs.append(k);relations.append(rel)
    expected=re.findall(r'^### (KC-\d{6})', (ROOT/'核心认知.md').read_text(),re.M)
    r=subprocess.run([sys.executable,'-B','scripts/audit/validate_governance_shards.py',str(index),str(session/'CORE_COGNITION_AUDIT.md')],cwd=ROOT,capture_output=True)
    before=json.loads((OUT/'INPUT-BEFORE.json').read_text())['files']
    drift=[x['path'] for x in before if sha((ROOT/x['path']).read_bytes())!=x['sha256']]
    context=json.loads((OUT/'CONTEXT-SOURCES.json').read_text())
    context_drift=[x['path'] for x in context if sha((ROOT/x['path']).read_bytes())!=x['sha256']]
    evidence_paths=sorted([p for p in OUT.rglob('*') if p.is_file() and p.suffix not in ('.agdai','.pyc') and p.name not in ('DELIVERY-CHECK.json','EVIDENCE-MANIFEST.json')])
    save(OUT/'EVIDENCE-MANIFEST.json',{'schema_version':'astra-second-audit-evidence-manifest/v1','scope':'Derived snapshot, no mathematical certification','files':[file_row(p) for p in evidence_paths]})
    result={'schema_version':'astra-second-audit-delivery-check/v1',
            'head_at_check':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
            'report_shards':7,'files':[file_row(p) for p in files],'checked_links':links,'link_errors':errors,
            'kc_count':len(kcs),'kc_order_and_coverage_match':kcs==expected,'kc_relations':dict(Counter(relations)),
            'shard_validator_exit':r.returncode,'shard_validator_output':(r.stdout+r.stderr).decode(),
            'reviewed_input_drift':drift,'context_source_drift':context_drift,
            'evidence_files':len(evidence_paths),'limits':'Mechanical checks do not prove semantic completeness or mathematical correctness.'}
    save(OUT/'DELIVERY-CHECK.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='files'},ensure_ascii=False,indent=2))
    return int(bool(errors or drift or context_drift or kcs!=expected or r.returncode))

if __name__=='__main__':raise SystemExit(main())
