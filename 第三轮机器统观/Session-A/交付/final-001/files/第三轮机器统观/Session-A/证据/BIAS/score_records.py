#!/usr/bin/env python3
"""Check frozen input identity, response coverage and label agreement only."""
from pathlib import Path
import argparse,hashlib,json

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
    root=Path(__file__).resolve().parent;repo=root.parents[3]
    manifest=json.loads((root/'INPUT-MANIFEST.json').read_text())
    assert manifest['before_responses'] and manifest['blind'] is False
    for row in manifest['rows']:
        p=repo/row['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['path']
    cases=json.loads((root/'CASES.json').read_text())['cases']
    oracle=json.loads((root/'ORACLE.json').read_text())['expected']
    responses=json.loads((root/'RESPONSES.json').read_text())['responses']
    ids=[x['id'] for x in responses];assert len(ids)==len(set(ids)) and set(ids)==set(oracle)=={x['id'] for x in cases}
    errors=[x['id'] for x in responses if x['verdict']!=oracle[x['id']]['verdict']]
    malformed=[x['id'] for x in responses if not x['reason'] or (x['verdict']=='REWRITE' and not x['revised_text']) or (x['verdict']=='KEEP' and x['revised_text'] is not None)]
    result={'case_count':len(cases),'label_agreement':len(cases)-len(errors),'label_disagreements':errors,'malformed_records':malformed,'missed_rewrite_labels':[x['id'] for x in responses if oracle[x['id']]['verdict']=='REWRITE' and x['verdict']!='REWRITE'],'false_rewrite_labels':[x['id'] for x in responses if oracle[x['id']]['verdict']=='KEEP' and x['verdict']!='KEEP'],'semantic_judgment_automated':False,'blind':False,'scope':'Record/label comparison, not independent semantic or future-model certification'}
    with Path(args.out).open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps(result,ensure_ascii=False));return int(bool(errors or malformed))

if __name__=='__main__':main()
