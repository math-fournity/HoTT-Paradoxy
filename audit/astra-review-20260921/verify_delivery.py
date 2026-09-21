#!/usr/bin/env python3
"""Verify the frozen archive, copied run evidence, document links and exact Git bytes."""
from pathlib import Path
import argparse,hashlib,json,re,subprocess,tarfile,urllib.parse
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
REVIEW=ROOT/'HoTT/review/four-stage-redo-v1';REPORT=ROOT/'Astra继续尝试/断点与证明机制系统检查/第三十二轮执行报告.md'
def sha(b):return hashlib.sha256(b).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--committed',action='store_true');args=ap.parse_args()
build=json.loads((OUT/'BUILD.json').read_text());archive=Path(build['archive']);assert sha(archive.read_bytes())==build['archive_sha256']
with tarfile.open(archive,'r:gz') as t:
    members=t.getmembers();assert len(members)==build['file_count']
    names=[m.name for m in members];assert len(set(names))==len(names)
    raw=t.extractfile('four-stage-review/MANIFEST.json').read();assert sha(raw)==build['manifest_sha256'];manifest=json.loads(raw)
    for row in manifest['files']:
        b=t.extractfile('four-stage-review/'+row['path']).read();assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['path']
    for p in REVIEW.rglob('*'):
        if p.is_file() and p.suffix in ('.md','.py'):assert t.extractfile('four-stage-review/'+p.relative_to(REVIEW).as_posix()).read()==p.read_bytes()
for row in manifest['source_rows']:assert sha((ROOT/row['path']).read_bytes())==row['sha256']
v=json.loads((OUT/'REPLAY-VERIFICATION.json').read_text());run=ROOT/v['run'];receipt=json.loads((run/'RUN.json').read_text())
assert sha((run/'RUN.json').read_bytes())==v['run_sha256'] and receipt['status']=='SCOPED_RELOCATION_PASS'
for row in receipt['files']:assert (run/row['path']).stat().st_size==row['bytes'] and sha((run/row['path']).read_bytes())==row['sha256']
assert {r['id'] for r in receipt['cases']}=={c['id'] for c in manifest['cases']}
for case in manifest['cases']:
    r=json.loads((run/case['id']/'RUN.json').read_text());assert r['exit_code']==case['expected_exit'] and r['status']=='RELOCATION_REPLAY_PASS_WITH_SCOPE'
    assert r['input_files_unchanged'] and r['ignore_interfaces'] and r['interface_cache_initially_empty'] and not r['observed_path_escapes'] and r['fresh_primitive_hashes_matched']==36
    assert r['bundle_manifest_sha256']==build['manifest_sha256'] and r['compiler_sha256']==manifest['agda']['binary_sha256']
    assert r['expected_diagnostic_matched'] and (case['expected_exit']!=0 or r['original_dependency_graph_equal'])
docs=[REPORT,*sorted(REPORT.with_suffix('').glob('*.md')),*sorted(REVIEW.glob('*.md'))]
links=[]
for p in docs:
    for match in re.finditer(r'\[[^\]]+\]\((?:<([^>]+)>|([^\)]+))\)',p.read_text()):
        target=match.group(1) or match.group(2)
        if target.startswith(('http:','https:','#')):continue
        target=urllib.parse.unquote(target.split('#')[0]);target=re.sub(r':\d+$','',target)
        q=Path(target) if target.startswith('/') else p.parent/target
        assert q.exists(),(p,target);links.append({'source':p.relative_to(ROOT).as_posix(),'target':target})
post=json.loads((OUT/'POST-CHECKPOINT.json').read_text());canonical=ROOT/post['canonical_result'];assert sha(canonical.read_bytes())==post['canonical_result_sha256']
assert json.loads(canonical.read_text())['status']=='CHECKPOINT_COMMITTED'
version=None;checked=0
if args.committed:
    version=json.loads((OUT/'VERSION.json').read_text());commit=version['source_commit']
    for path in json.loads((OUT/'version-paths.json').read_text())['paths']:
        # This derived receipt records the verification and exact commit below;
        # it is not an input and cannot include its own future hash/commit.
        if path==(OUT/'DELIVERY.json').relative_to(ROOT).as_posix():continue
        p=ROOT/path
        stored=subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)
        assert stored==p.read_bytes(),path;checked+=1
result={'status':'SCOPED_REVIEW_DELIVERY_PASS','archive_sha256':build['archive_sha256'],'archive_bytes':archive.stat().st_size,'bundle_payload_files_checked':len(manifest['files']),'local_sources_unchanged':len(manifest['source_rows']),'replay_cases':len(receipt['cases']),'positive_graphs_equal':5,'exact_type_rejections':4,'integrity_control_status':json.loads((OUT/'INTEGRITY-CONTROLS.json').read_text())['status'],'local_links_checked':len(links),'canonical_revision':206,'version':version,'committed_paths_checked':checked,'excluded_from_source_commit_byte_comparison':['audit/astra-review-20260921/DELIVERY.json (derived verification output, not an input)'],'scope':'One fixed macOS arm64 environment, five proof entries/four fixed error controls. No new math claim, no all-platform/whole-repo/publication/peer-review or complete parent-goal certification.'}
(OUT/'DELIVERY.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
