#!/usr/bin/env python3
"""Check archive byte identity separately from this design's structural coverage."""
from pathlib import Path
from collections import Counter
import hashlib,json,re,subprocess,sys

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
SESSION=ROOT/'.codex/research/hott/sessions/S-DES-20260919-ASTRA-MARKED-PUNCTURE'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def main():
    m=json.loads((BASE/'evidence/对话归档清单.json').read_text())
    delta=json.loads((BASE/'evidence/对话归档增量-002.json').read_text())
    all_messages=m['messages']+delta['messages']
    users=[x for x in m['messages'] if x['role']=='user'][:5]
    diffs=[]
    for x,c in zip(users,[z for z in m['staging_crosschecks'] if z['kind']=='prompt.md']):
        a=(BASE/x['text_file']).read_bytes();b=Path(c['stage_path']).read_bytes();b=b[:-1] if b.endswith(b'\n') else b
        diffs.append({'turn':c['turn'],'exact_match':a==b,'same_after_outer_whitespace_removal':a.strip()==b.strip(),
                      'canonical_leading_lf':len(a)-len(a.lstrip(b'\n')),'canonical_trailing_lf':len(a)-len(a.rstrip(b'\n')),
                      'stage_leading_lf':len(b)-len(b.lstrip(b'\n')),'stage_trailing_lf':len(b)-len(b.rstrip(b'\n'))})
    save(BASE/'evidence/暂存差异核对.json',{'authority':'Canonical Host text; no trimming applied to exported originals','rows':diffs})
    identity=json.loads((ROOT/'audit/astra-hott-first-20260919/FOUR-SET-IDENTITY.json').read_text())
    cognition=[{'path':x['path'],'sha256':sha((ROOT/x['path']).read_bytes()),'matches_prior':sha((ROOT/x['path']).read_bytes())==x['sha256']} for x in identity]
    save(BASE/'evidence/四件套复认-002.json',cognition)
    files=[BASE/'README.md',BASE/'依据与归档核对.md',BASE/'对话原文.md',BASE/'系统化后续检查方案.md',ROOT/'Astra继续尝试/README.md']
    files+=sorted((BASE/'系统化后续检查方案').glob('*.md'))
    if SESSION.exists():files += [SESSION/'CORE_COGNITION_AUDIT.md',*sorted((SESSION/'CORE_COGNITION_AUDIT').glob('*.md'))]
    errors=[];links=0
    for p in files:
        for a,b in re.findall(r'\[[^\]\n]*\]\((?:<([^>]+)>|([^\s)]+))\)',p.read_text()):
            t=a or b
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://',t) or t.startswith('#'):continue
            t=t.split('#')[0];t=re.sub(r':\d+$','',t);q=Path(t);q=q if q.is_absolute() else p.parent/q;links+=1
            if not q.exists():errors.append({'from':str(p.relative_to(ROOT)),'target':t})
    indexes=[BASE/'对话原文.md',BASE/'系统化后续检查方案.md']
    if SESSION.exists():indexes.append(SESSION/'CORE_COGNITION_AUDIT.md')
    r=subprocess.run([sys.executable,'-B','scripts/audit/validate_governance_shards.py',*map(str,indexes)],cwd=ROOT,capture_output=True)
    roster=(BASE/'系统化后续检查方案/005 - 程序化候选、覆盖与遗漏检查.md').read_text()
    cases=re.findall(r'^\| (BP-C\d{2}) \|',roster,re.M)
    unit_text=(BASE/'系统化后续检查方案/006 - 执行次序、证据与停止条件.md').read_text()
    units=re.findall(r'^\| (BP-U\d{2}) \|',unit_text,re.M)
    pairs=[]
    if SESSION.exists():
        for p in sorted((SESSION/'CORE_COGNITION_AUDIT').glob('*.md')):pairs+=re.findall(r'^\| (KC-\d{6}) \| (\w+) \|',p.read_text(),re.M)
    expected=re.findall(r'^### (KC-\d{6})',(ROOT/'核心认知.md').read_text(),re.M)
    result={'schema_version':'astra-breakpoint-design-delivery/v1.1','archive_messages':len(all_messages),'completed_pairs':delta['completed_pairs'],
            'archive_counts':delta['counts'],'readable_archive_shards':7,'design_shards':7,'links_checked':links,'link_errors':errors,
            'cases_exact':cases==[f'BP-C{i:02d}' for i in range(1,15)],'units_exact':units==[f'BP-U{i:02d}' for i in range(7)],
            'kc_count':len(pairs),'kc_order_match':[x[0] for x in pairs]==expected,'kc_relations':dict(Counter(x[1] for x in pairs)),
            'shard_validator_exit':r.returncode,'shard_result':(r.stdout+r.stderr).decode(),'cognition_unchanged':all(x['matches_prior'] for x in cognition),
            'mathematical_runs':0,'limits':'Archive exactness and design structure, not mathematical truth or complete search coverage.'}
    save(BASE/'evidence/交付检查-002.json',result)
    paths=[*files,*sorted((BASE/'对话原文').glob('*.md')),*sorted((BASE/'原始消息').glob('*.txt')),*sorted((BASE/'tools').glob('*.py'))]
    save(BASE/'evidence/交付文件清单-002.json',[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in paths])
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return int(bool(errors or r.returncode or not result['cases_exact'] or not result['units_exact'] or not result['cognition_unchanged'] or not result['kc_order_match']))
if __name__=='__main__':raise SystemExit(main())
