#!/usr/bin/env python3
"""Generate a one-time source-entry baseline, never a coverage certificate.

The JSON is derived evidence, not mutable canonical research state. Session C
owns its human-reviewed coverage map and must inspect substantive source bodies.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BOOK = 'HoTT/theory-schema/upstream/book-578b85cc'
CHAPTERS = ['basics','preliminaries','logic','equivalences','induction','hits','hlevels','homotopy','setmath','categories','reals']
SCHEMAS = {'C':'CORE_RULES.md','D':'DERIVED_STRUCTURES.md','S':'SEMANTICS_AND_COHERENCE.md','E':'EXTENSIONS_AND_METATHEORY.md'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();out=a.out.resolve()
    if out.exists():raise SystemExit('OUTPUT_ALREADY_EXISTS')
    hashes={};entries=[];counts={}
    def read(rel):
        p=ROOT/rel;b=p.read_bytes();hashes[rel]=hashlib.sha256(b).hexdigest();return b.decode()
    for prefix,name in SCHEMAS.items():
        rel='HoTT/theory-schema/'+name
        found=[]
        for n,line in enumerate(read(rel).splitlines(),1):
            m=re.match(r'^## ('+prefix+r'\d{2})\s+(.+)$',line)
            if m:found.append({'id':m[1],'title':m[2],'path':rel,'line':n,'status':'NOT_REVIEWED_BY_PREPARER'})
        if not found or len({x['id'] for x in found})!=len(found):raise SystemExit('SCHEMA_ID_DISCOVERY_FAILED:'+rel)
        counts[prefix]=len(found);entries+=found
    sections=[]
    for chapter in CHAPTERS:
        rel=BOOK+'/'+chapter+'.tex';found=[]
        for n,line in enumerate(read(rel).splitlines(),1):
            if re.match(r'^\s*\\section\{',line):found.append({'chapter':chapter,'ordinal_in_file':len(found)+1,'path':rel,'line':n,'raw_heading':line.strip(),'status':'NOT_REVIEWED_BY_PREPARER'})
        if not found:raise SystemExit('CHAPTER_SECTION_DISCOVERY_FAILED:'+rel)
        sections+=found
    appendix=BOOK+'/formal.tex';read(appendix)
    for p in (ROOT/BOOK).iterdir():
        if p.is_file():hashes[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    for rel in ['HoTT/THEORY_SCHEMA.md','HoTT/theory-schema/SOURCES_AND_COVERAGE.md','HoTT/theory-schema/TEMPORAL_AUDIT_MAP.md']:
        read(rel)
    result={'schema_version':'mo3-scope-entry-baseline/v1','asset_role':'ONE_TIME_DERIVED_EVIDENCE_NOT_CANONICAL_COVERAGE','producer':Path(__file__).relative_to(ROOT).as_posix(),'git_head_observed':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'source_sha256':hashes,'schema_entry_counts':counts,'schema_entries':entries,'numbered_book_section_count':len(sections),'book_sections':sections,'appendix_required':appendix,'status':'SOURCE_ENTRIES_DISCOVERED_ONLY','limits':['No source body review certified','Numbered sections omit unnumbered theory content; C must account for it','E entries may contain several named systems; C must expand them','No semantic units, relationships, exclusions, proof validity or parent sufficiency certified']}
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'counts':counts,'book_sections':len(sections),'output':str(out)},ensure_ascii=False))


if __name__=='__main__':main()
