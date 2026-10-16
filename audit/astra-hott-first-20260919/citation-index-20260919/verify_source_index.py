#!/usr/bin/env python3
"""Freeze/check the sources linked by this one audit report.

Human-edited claim/evidence judgements remain in Markdown. This script checks
identities, paths, line anchors and declared section coverage, not mathematics.
The JSON files it emits are derived audit receipts, not a new canonical registry.
"""
from pathlib import Path
import argparse, hashlib, json, re, subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
REPORT=ROOT/'Astra对击落HoTT工作的第一次审计'
SNAPSHOT=HERE/'SOURCE-SNAPSHOT.json'
LINK=re.compile(r'\[([^\]]+)\]\((<[^>]+>|[^\n]+?)\)')
CLAIM=re.compile(r'^\| (C\d{3}-\d{2}) \|',re.M)
MAP=re.compile(r'<!-- audit-cites: ([^\n]+) -->')

def sha(b): return hashlib.sha256(b).hexdigest()
def write_json(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def git(*args): return subprocess.run(['git',*args],cwd=ROOT,capture_output=True,check=False)
def resolve(p,target):
    target=target.strip('<>')
    if target.startswith(('https://','http://','mailto:','#')): return None,None
    target=target.split('#',1)[0]
    m=re.search(r':(\d+)$',target)
    n=int(m.group(1)) if m else None
    if m: target=target[:m.start()]
    q=Path(target) if target.startswith('/') else p.parent/target
    return q.resolve(),n

def scans():
    paths=sorted((ROOT/'HoTT/formal/dedekind-omega-missile').glob('*.agda'))
    inventory=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p.read_bytes()),'lines':len(p.read_bytes().splitlines())} for p in paths]
    jobs={
      'local-signatures-and-imports':['rg','-n','--glob','*.agda',r'^(module|open import|import|postulate)|^[^[:space:]-].* : ', 'HoTT/formal/dedekind-omega-missile'],
      'formal-packing-consumers':['rg','-n','--glob','*.agda','--glob','*.lagda.md',r'CutGoldForm|Lₚ|Uₚ|DedekindReals|ℝLayerAt|Necessity|sufficiency','HoTT/formal'],
      'process-and-metatheory-candidates':['rg','-n','--glob','*.agda',r'converg|compact|topolog|MereMove|Prov|proof.?code|Gödel|Godel|不可证|三选一|现实|圆环|夹钳|停机|完成','HoTT/formal/dedekind-omega-missile'],
      'primitive-assumptions-options':['rg','-n','--glob','*.agda',r'OPTIONS|^postulate|TERMINATING|NON_TERMINATING|allow-unsolved|no-termination|type-in-type','HoTT/formal/dedekind-omega-missile'],
    }
    rows=[]
    for name,argv in jobs.items():
        r=subprocess.run(argv,cwd=ROOT,capture_output=True,check=False)
        (HERE/(name+'-stdout.txt')).write_bytes(r.stdout)
        (HERE/(name+'-stderr.txt')).write_bytes(r.stderr)
        rows.append({'id':name,'argv':argv,'cwd':str(ROOT),'exit_code':r.returncode,
                     'stdout':name+'-stdout.txt','stderr':name+'-stderr.txt',
                     'stdout_sha256':sha(r.stdout),'stderr_sha256':sha(r.stderr),
                     'scope':'Lexical navigation + explicitly listed files. No hit/finite inventory is not a semantic impossibility proof.'})
    listed=subprocess.check_output(['rg','--files','HoTT/formal','-g','*.agda','-g','*.lagda.md'],cwd=ROOT,text=True).splitlines()
    formal_inventory=[{'path':p,'sha256':sha((ROOT/p).read_bytes())} for p in sorted(listed)]
    diff_args=['diff','--name-only','0dee3a9589ed6b49a63c4fb444e17bc13adb2ad8','8a334e0636620209953a26aba354ffb38bbf7bbf','--','HoTT','核心认知.md','方向追踪.md','方向追踪','全景视野.md','全景视野','扩展认知.md','扩展认知']
    diff=git(*diff_args);(HERE/'baseline-content-diff.txt').write_bytes(diff.stdout)
    write_json(HERE/'SCOPED-SEARCHES.json',{'schema_version':'astra-citation-search/v1','head':git('rev-parse','HEAD').stdout.decode().strip(),'primary_module_inventory':inventory,'module_count':len(inventory),'module_lines':sum(x['lines'] for x in inventory),'formal_search_inventory':formal_inventory,'searches':rows,'baseline_comparison':{'argv':['git',*diff_args],'exit_code':diff.returncode,'stdout_sha256':sha(diff.stdout),'stdout_bytes':len(diff.stdout)}})
    raw='/Users/aurolafly/.zcode/cli/rollout/model-io-sess_0486510b-c8f5-4675-8480-1881bf3325d4.jsonl'
    tree=subprocess.run(['python3','/Users/aurolafly/codex/tools/session_trajectory.py','tree','--host','zcode','--source',raw],capture_output=True,check=True)
    (HERE/'canonical-tree.txt').write_bytes(tree.stdout)
    corpus=ROOT/'AI对话录/ZCode-sess_0486510b-c8f5-4675-8480-1881bf3325d4-用户与AI完整对话.md'
    lines=corpus.read_text().splitlines(); heads=[i for i,x in enumerate(lines) if x.startswith('===== ')]
    entries=[]
    for j,i in enumerate(heads):
        match=re.search(r'jsonl:(.+?) \[([^\]]+)\]',lines[i])
        if not match:continue
        loc,kind=match.groups()
        selected=loc in {f'{n}#/response/text' for n in [27,43,47,50,53,57,61,65,68,71,74,78,107,110,128]} or loc=='72#/request/messages/62'
        if not selected:continue
        stop=heads[j+1] if j+1<len(heads) else len(lines)
        name='user-72.json' if kind=='user_message' else 'assistant-'+loc.split('#')[0]+'.json'
        normalized=ROOT/'private-audit/astra-hott-first-20260919'/name
        x=json.loads(normalized.read_text())
        body='\n'.join(lines[i+1:stop]).strip('\n')
        entries.append({'raw_locator':x['locator'],'readable_source':str(corpus.relative_to(ROOT)),
                        'start_line':i+1,'end_line':stop,'kind':kind,
                        'canonical_text_sha256':sha(x['text'].encode()),
                        'readable_body_matches_canonical':body==x['text'].strip('\n'),
                        'private_normalized_source':str(normalized.relative_to(ROOT))})
    write_json(HERE/'VISIBLE-MESSAGE-LOCATORS.json',{'corpus_sha256':sha(corpus.read_bytes()),'entries':entries,'normalization':'Only separator/newline envelope removed; original message wording retained.'})
    rows=json.loads((HERE.parent/'RESULTS.json').read_text())
    probe_runs={'UA-control':'20260917-MP-DEDEKIND-OMEGA-TA-02','UA-zero':'20260917-MP-DEDEKIND-OMEGA-TA-03','UA-one':'20260917-MP-DEDEKIND-OMEGA-TA-04','AC-zero':'20260917-MP-DEDEKIND-OMEGA-TA-AC-01','AC-one':'20260917-MP-DEDEKIND-OMEGA-TA-AC-02','LEM-zero':'20260918-MP-DEDEKIND-OMEGA-TA-LEM-01','LEM-one':'20260918-MP-DEDEKIND-OMEGA-TA-LEM-02'}
    md=['# 原 run 与本次重放的精确定位','', '> MACHINE_MANAGED_DERIVED；owner: verify_source_index.py。不是新数学 registry。','', '| 检查 | command/exit/hash 收据 | 原始 stdout | 原始 stderr | 历史 primary run | 历史来源清单/环境 |','|---|---|---|---|---|---|']
    for x in rows:
        name=x['label'];p=HERE.parent/'replays'/name
        hist=ROOT/'HoTT/verification/runs'/probe_runs.get(name,name)/'RUN.json'
        h=f'[RUN.json]({hist}:1)' if hist.exists() else '固定 probe，argv 在本轮 receipt'
        md.append(f"| {name} | [receipt.json]({p/'receipt.json'}:1) / exit={x['exit_code']} | [stdout]({p/'stdout.txt'}:1) | [stderr]({p/'stderr.txt'}) | {h} | [source-manifest]({hist.parent/'source-manifest.json'}:1) / [environment]({hist.parent/'environment.txt'}:1) |")
    (HERE/'RUN-LOCATORS.md').write_text('\n'.join(md)+'\n')

def collect(freezing=False):
    reports=[ROOT/'Astra对击落HoTT工作的第一次审计.md',*sorted(REPORT.glob('*.md'))]
    claims={};refs=[];errors=[];sections=[];source_paths=set()
    for p in reports:
        text=p.read_text();ids=CLAIM.findall(text)
        for cid in ids:
            if cid in claims: errors.append('DUPLICATE_CLAIM:'+cid)
            line=next(i+1 for i,s in enumerate(text.splitlines()) if s.startswith('| '+cid+' |'))
            claims[cid]={'report':str(p.relative_to(ROOT)),'line':line}
        lines=text.splitlines()
        for i,line in enumerate(lines):
            if re.match(r'^#{2,3} ',line) and '逐项来源索引' not in line and p.parent==REPORT:
                following='\n'.join(lines[i+1:i+4]);m=MAP.search(following)
                sections.append({'report':str(p.relative_to(ROOT)),'heading':line,'claim_ids':m.group(1).split() if m else []})
                if not m: errors.append('SECTION_WITHOUT_SOURCE_MAP:'+str(p.name)+':'+line)
        for label,target in LINK.findall(text):
            q,n=resolve(p,target)
            if q is None: continue
            derived={SNAPSHOT,HERE/'CITATION-CHECK.json',HERE/'SOURCE-LOCATORS.md',HERE/'CLAIM-LOCATORS.md'}
            if not q.exists():
                if freezing and q in derived:continue
                errors.append('MISSING_LINK:'+str(p.name)+':'+target);continue
            if q.is_dir():continue
            if n is not None and n>len(q.read_bytes().splitlines()):errors.append('LINE_OUT_OF_RANGE:'+target)
            refs.append({'report':str(p.relative_to(ROOT)),'label':label,'path':str(q),'line':n})
            if q not in reports and q not in derived:
                source_paths.add(q)
        for line in lines:
            if CLAIM.match(line) and not LINK.search(line):errors.append('CLAIM_WITHOUT_LINK:'+line[:50])
    for section in sections:
        for cid in section['claim_ids']:
            if cid not in claims: errors.append('UNDEFINED_CLAIM:'+cid)
    # Expand the explicit run navigation layer once, so every raw output and
    # historical receipt in that table is hash-pinned, not just its index.
    run_index=HERE/'RUN-LOCATORS.md'
    if run_index.exists():
        for label,target in LINK.findall(run_index.read_text()):
            q,n=resolve(run_index,target)
            if q and q.is_file():source_paths.add(q)
            elif q:errors.append('MISSING_RUN_LINK:'+target)
    search=json.loads((HERE/'SCOPED-SEARCHES.json').read_text())
    for x in search['formal_search_inventory']:source_paths.add(ROOT/x['path'])
    for x in search['searches']:
        if x['exit_code'] not in [0,1]:errors.append('SEARCH_FAILED:'+x['id'])
    trajectory=json.loads((HERE.parent/'TRAJECTORY-SOURCES.json').read_text())
    raw=Path(trajectory['source_path']);source_paths.add(raw)
    if sha(raw.read_bytes())!=trajectory['source_sha256']:errors.append('RAW_TRAJECTORY_IDENTITY_CHANGED')
    reader=Path('/Users/aurolafly/codex/tools/session_trajectory.py');source_paths.add(reader)
    if sha(reader.read_bytes())!=trajectory['reader_sha256']:errors.append('CANONICAL_READER_IDENTITY_CHANGED')
    visible=json.loads((HERE/'VISIBLE-MESSAGE-LOCATORS.json').read_text())
    for x in visible['entries']:
        p=ROOT/x['private_normalized_source'];source_paths.add(p)
        data=json.loads(p.read_text())
        if sha(data['text'].encode())!=x['canonical_text_sha256']:errors.append('CANONICAL_VISIBLE_TEXT_CHANGED:'+str(p))
    source_paths.add(Path(__file__).resolve())
    return reports,claims,refs,errors,sections,source_paths

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--freeze',action='store_true');args=ap.parse_args()
    if args.freeze:scans()
    reports,claims,refs,errors,sections,paths=collect(args.freeze)
    claim_lines=['# 审计结论 ID 定位表','', '> MACHINE_MANAGED_DERIVED；从人工证据行生成，不定义新结论。','', '| 结论 ID | 所属证据行 |','|---|---|']
    for cid,x in sorted(claims.items()):
        claim_lines.append(f"| {cid} | [{x['report']} L{x['line']}](<{ROOT/x['report']}:{x['line']}>) |")
    claim_text='\n'.join(claim_lines)+'\n'
    if args.freeze:(HERE/'CLAIM-LOCATORS.md').write_text(claim_text)
    elif not (HERE/'CLAIM-LOCATORS.md').exists() or (HERE/'CLAIM-LOCATORS.md').read_text()!=claim_text:errors.append('CLAIM_LOCATOR_STALE')
    if args.freeze:
        sources=[]
        for p in sorted(paths):
            b=p.read_bytes();rel=str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p)
            blob=git('rev-parse','HEAD:'+rel) if p.is_relative_to(ROOT) else None
            oid=blob.stdout.decode().strip() if blob and blob.returncode==0 else None
            head_equal=git('show','HEAD:'+rel).stdout==b if oid else None
            sources.append({'path':rel,'bytes':len(b),'lines':len(b.splitlines()),'sha256':sha(b),'head_blob_oid':oid,'matches_head_blob':head_equal,'version_status':'TRACKED_HEAD_MATCH' if head_equal else 'LOCAL_DERIVED_OR_UNTRACKED'})
        write_json(SNAPSHOT,{'schema_version':'astra-source-citation-snapshot/v1','head':git('rev-parse','HEAD').stdout.decode().strip(),'book_upstream_commit':'578b85cc8d586b1677ec4335148adeb443057d24','sources':sources})
        md=['# 审计引用来源的版本与哈希索引','', '> MACHINE_MANAGED_DERIVED；owner: verify_source_index.py。精确来源、字节哈希和 Git blob；不认证正文推理。','', '| 来源 | 行数 | SHA-256 | Git blob / 状态 |','|---|---:|---|---|']
        for x in sources:
            p=ROOT/x['path'] if not x['path'].startswith('/') else Path(x['path'])
            md.append(f"| [{x['path']}](<{p}>) | {x['lines']} | `{x['sha256']}` | `{x['head_blob_oid'] or x['version_status']}` |")
        (HERE/'SOURCE-LOCATORS.md').write_text('\n'.join(md)+'\n')
    if not SNAPSHOT.exists(): errors.append('SNAPSHOT_MISSING')
    else:
        frozen=json.loads(SNAPSHOT.read_text())
        for x in frozen['sources']:
            p=ROOT/x['path'] if not x['path'].startswith('/') else Path(x['path'])
            if not p.exists() or sha(p.read_bytes())!=x['sha256']:errors.append('SOURCE_DRIFT:'+x['path'])
    loc=json.loads((HERE/'VISIBLE-MESSAGE-LOCATORS.json').read_text())
    for x in loc['entries']:
        if not x['readable_body_matches_canonical']:errors.append('TRANSCRIPT_BODY_MISMATCH:'+x['raw_locator'])
    coverage=(ROOT/'HoTT/theory-schema/SOURCES_AND_COVERAGE.md').read_text()
    book_checks=[]
    for name in ['logic.tex','reals.tex']:
        match=re.search(r'\| `'+re.escape(name)+r'` \| (\d+) \| `([0-9a-f]{64})`',coverage)
        source=ROOT/'HoTT/theory-schema/upstream/book-578b85cc'/name
        ok=bool(match and len(source.read_bytes())==int(match.group(1)) and sha(source.read_bytes())==match.group(2))
        book_checks.append({'source':str(source.relative_to(ROOT)),'matches_recorded_upstream_manifest':ok})
        if not ok:errors.append('BOOK_SOURCE_MANIFEST_MISMATCH:'+name)
    result={'status':'PASS_WITH_SCOPE' if not errors else 'FAIL','errors':errors,'claim_count':len(claims),
            'claims_by_report':{p.name:len(CLAIM.findall(p.read_text())) for p in reports if p.parent==REPORT},
            'mapped_section_count':len(sections),'local_reference_count':len(refs),'source_count':len(paths),
            'visible_messages_verified':len(loc['entries']),'book_source_checks':book_checks,'sections':sections,
            'report_hashes':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in reports},
            'scope':'Checks declared citation coverage, source hashes, path/line validity and canonical visible text correspondence. It does not certify semantic entailment, mathematical truth, complete literature coverage or model cognition.'}
    write_json(HERE/'CITATION-CHECK.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in {'sections','report_hashes'}},ensure_ascii=False,indent=2))
    return bool(errors)

if __name__=='__main__':raise SystemExit(main())
