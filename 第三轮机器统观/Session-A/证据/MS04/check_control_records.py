#!/usr/bin/env python3
"""Mechanical record reconciliation only; human semantic reasons remain auditable."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent

def main():
    freeze=json.loads((HERE/'CONTROL-FREEZE.json').read_text())
    for p,h in freeze['files'].items():assert hashlib.sha256((HERE/p).read_bytes()).hexdigest()==h,p
    inputs=json.loads((HERE/'granularity-inputs.json').read_text())['cases']
    oracle=json.loads((HERE/'expected-oracle.json').read_text())['granularity']
    responses=json.loads((HERE/'granularity-review.json').read_text())['responses']
    assert [c['id'] for c in inputs]==[r['id'] for r in responses]
    assert len(set(r['id'] for r in responses))==10
    mismatches=[r['id'] for r in responses if r['decision']!=oracle[r['id']]]
    assert not mismatches and all(r['reason'] and r['evidence'] for r in responses)
    manifest=json.loads((HERE/'INPUT-MANIFEST.json').read_text())
    for r in manifest['sources']:assert hashlib.sha256(Path(r['copy']).read_bytes()).hexdigest()==r['copy_sha256']
    assert hashlib.sha256((HERE/'baseline-relation-table.md').read_bytes()).hexdigest()==manifest['baseline_sha256']
    rr=json.loads((HERE/'RECONSTRUCTION-RECEIPT.json').read_text());assert hashlib.sha256(Path(rr['path']).read_bytes()).hexdigest()==rr['sha256']
    result={'schema':'mo3-method-record-check/v1','status':'RECORDS_MATCH_FROZEN_SCOPE','fixture_count':10,'accepted':sum(r['decision']=='ACCEPT_WITH_SCOPE' for r in responses),'rejected':sum(r['decision']=='REJECT_COVERAGE' for r in responses),'oracle_mismatches':mismatches,'source_and_reconstruction_hashes_match':True,'boundary':'checks identity/completeness/label comparison only; does not certify human semantic judgment, autonomous discovery, HoTT mathematics or future behavior'}
    with (HERE/'record-check.json').open('x') as f:f.write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
