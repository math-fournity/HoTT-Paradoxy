#!/usr/bin/env python3
"""Portable, offline, explicit-request-only incremental audit transport.
Exports committed changes; imports only into a NEW isolated clone, never overwrites an active workspace.
Integrity is not authenticity or mathematical validation. Python 3.10+ and Git, no third-party packages.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, tempfile, unicodedata, zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

SCHEMA='hott.audit-delta.v1'
OID=re.compile(r'^[0-9a-f]{40}$')
IDENT=re.compile(r'^[A-Za-z0-9][A-Za-z0-9_-]{0,95}$')
DEFAULT_ROOT=Path(__file__).resolve().parents[2]
MAX_ZIP_BYTES=512*1024*1024
class DeltaError(RuntimeError): pass

def now():return datetime.now(timezone.utc).isoformat()
def encoded(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode('utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()
def put(p:Path,b:bytes):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('xb') as f:f.write(b)
def git(root,*args,input=None,check=True):
    env=os.environ.copy();env['GIT_CONFIG_NOSYSTEM']='1';env['GIT_CONFIG_GLOBAL']=os.devnull
    env['GIT_TERMINAL_PROMPT']='0';env['GIT_NO_REPLACE_OBJECTS']='1'
    cmd=['git','-c','core.hooksPath='+os.devnull,'-c','core.autocrlf=false','-C',str(root),*args]
    p=subprocess.run(cmd,input=input,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
    if check and p.returncode:raise DeltaError(p.stderr.decode('utf-8','replace').strip() or 'git failed')
    return p

def safe_rel(s):
    if not isinstance(s,str) or not s or '\\' in s or '\x00' in s or ':' in s:raise DeltaError('UNSAFE_PATH')
    p=PurePosixPath(s)
    if p.is_absolute() or any(x in ('','.','..') for x in s.split('/')):raise DeltaError('UNSAFE_PATH: '+s)
    if any(x.lower()=='.git' for x in p.parts):raise DeltaError('GIT_ADMIN_PATH_FORBIDDEN')
    return p

def inside(root,rel):
    p=safe_rel(rel);out=root.joinpath(*p.parts)
    for i in (out,*out.parents):
        if i==root.parent:break
        if i.is_symlink():raise DeltaError('SYMLINK_FORBIDDEN')
    return out

def commit(root,ref):
    if not isinstance(ref,str) or not ref or ref.startswith('-') or '\x00' in ref:raise DeltaError('INVALID_REF')
    s=git(root,'rev-parse','--verify','--end-of-options',ref+'^{commit}').stdout.decode().strip()
    if not OID.fullmatch(s):raise DeltaError('Only SHA-1 repositories supported by v1')
    return s

def clean(root):
    if git(root,'status','--porcelain=v1','--untracked-files=all').stdout:raise DeltaError('DIRTY_WORKSPACE: commit research, logs, and round records first')

def tree(root,c):
    rows={};folded={}
    raw=git(root,'ls-tree','-r','-z','--full-tree',c).stdout
    for item in raw.split(b'\0'):
        if not item:continue
        meta,p=item.split(b'\t',1);mode,typ,oid=meta.decode().split();path=p.decode('utf-8')
        safe_rel(path)
        if mode not in ('100644','100755') or typ!='blob':raise DeltaError('UNSUPPORTED_GIT_MODE: '+path)
        norm=unicodedata.normalize('NFC',path).casefold()
        if norm in folded and folded[norm]!=path:raise DeltaError('PORTABILITY_CASE_COLLISION')
        folded[norm]=path;rows[path]={'mode':mode,'git_blob':oid}
    return rows

def blobs(root,oids):
    ids=sorted(set(oids))
    if not ids:return {}
    raw=git(root,'cat-file','--batch',input=('\n'.join(ids)+'\n').encode()).stdout
    pos=0;out={}
    for expected in ids:
        end=raw.index(b'\n',pos);parts=raw[pos:end].decode().split()
        if len(parts)!=3 or parts[0]!=expected or parts[1]!='blob':raise DeltaError('INVALID_BLOB_BATCH')
        n=int(parts[2]);pos=end+1;out[expected]=raw[pos:pos+n];pos+=n+1
    if pos!=len(raw):raise DeltaError('TRAILING_BLOB_DATA')
    return out

def snapshot(root,c):
    t=tree(root,c);bs=blobs(root,[r['git_blob'] for r in t.values()])
    return {p:{**r,'sha256':sha(bs[r['git_blob']]),'bytes':len(bs[r['git_blob']])} for p,r in t.items()}

def changes(a,b):
    return [{'path':p,'operation':'add' if p not in a else 'delete' if p not in b else 'modify','before':a.get(p),'after':b.get(p)} for p in sorted(a.keys()|b.keys()) if a.get(p)!=b.get(p)]

def init_round(root,round_id,request,base):
    if not IDENT.fullmatch(round_id):raise DeltaError('INVALID_ROUND_ID')
    baseid=commit(root,base);folder=inside(root,'exchange/rounds/'+round_id)
    if folder.exists():raise DeltaError('ROUND_ALREADY_EXISTS')
    request=Path(request);data=request.read_bytes()
    folder.mkdir(parents=True)
    put(folder/'REQUEST.md',data)
    put(folder/'ROUND.json',encoded({'schema':'hott.audit-round.v1','round_id':round_id,'base_commit':baseid,'created_at_utc':now(),'request_sha256':sha(data),'status':'IN_PROGRESS','export_is_not_audit_approval':True}))
    for name,text in {
      'RESEARCH_DELTA.md':'# 本轮增量研究记录\n\n## 原任务与上一轮状态\n待填。\n\n## 本轮实际工作（不是计划）\n待填。\n\n## 结论变化／反例／失败\n待填。\n\n## 证据与精确依赖路径\n待填。\n\n## 未运行和仍然未知\n待填。\n\n## 影响的旧结论与下一步\n待填。\n',
      'AUDIT_REQUEST.md':'# 增量审计请求\n\n请审计本轮新增或修改内容；不要把接收文件当作认可。\n\n## 重点问题\n待填。\n\n## 理论配置与机器证据范围\n待填。\n\n## 治理修改\n待填；没有则明确写无。\n',
      'RUNS.json':json.dumps({'schema':'hott.run-ledger.v1','runs':[],'status':'NO_RUNS_RECORDED'},ensure_ascii=False,indent=2)+'\n'
    }.items():put(folder/name,text.encode())
    return {'round_id':round_id,'path':str(folder),'base_commit':baseid,'next':'Complete records; checkpoint governance; commit; export. No jobs were started.'}

def export_delta(root,round_id,base,head,out):
    if not IDENT.fullmatch(round_id):raise DeltaError('INVALID_ROUND_ID')
    clean(root);h=commit(root,head);b=commit(root,base)
    if commit(root,'HEAD')!=h:raise DeltaError('HEAD_MISMATCH')
    if git(root,'merge-base','--is-ancestor',b,h,check=False).returncode:raise DeltaError('BASE_NOT_ANCESTOR')
    if b==h:raise DeltaError('EMPTY_DELTA')
    rd='exchange/rounds/'+round_id
    a=snapshot(root,b);z=snapshot(root,h)
    for name in ['REQUEST.md','ROUND.json','RESEARCH_DELTA.md','AUDIT_REQUEST.md','RUNS.json']:
        if rd+'/'+name not in z:raise DeltaError('MISSING_COMMITTED_ROUND_FILE: '+name)
    roundmeta=json.loads(git(root,'show',h+':'+rd+'/ROUND.json').stdout)
    if roundmeta['base_commit']!=b:raise DeltaError('ROUND_BASE_MISMATCH')
    delta=changes(a,z);out=Path(out).resolve()
    if out.exists():raise DeltaError('OUTPUT_EXISTS')
    try:
        rel=out.relative_to(root).as_posix()
        if not rel.startswith('exchange/outbox/'):raise DeltaError('EXPORT_INSIDE_TRACKED_TREE_FORBIDDEN')
    except ValueError:pass
    members={
       'BASE_SNAPSHOT.json':encoded(a),'HEAD_SNAPSHOT.json':encoded(z),
       'CHANGES.json':encoded(delta),
       'changes.patch':git(root,'diff','--binary','--full-index','--no-ext-diff','--no-renames',b,h,'--').stdout,
       'README.md':('''# HoTT 增量审计包\n\n本包只携带指定基线之后的修改，不是完整项目。必须拥有匹配的完整基线。\n\n先运行受信任基线内的 scripts/handoff/delta_tool.py verify；需要实体审计目录时用 stage，禁止直接覆盖活动工作树。\n不要执行包内新脚本或 Git 钩子；先审查变更。验证只检查完整性和 Git 对应，不认证数学、作者身份或成果。\nCHANGES.json 包含删除清单；改名按删除＋新增处理。审计通过也不自动升级数学结论或自动合并。\n''').encode()
    }
    bs=blobs(root,[r['after']['git_blob'] for r in delta if r['after']])
    for row in delta:
        if row['after']:members['payload/'+row['path']]=bs[row['after']['git_blob']]
    with tempfile.TemporaryDirectory(prefix='hott-delta-') as tmp:
        bundle=Path(tmp)/'commits.bundle'
        git(root,'bundle','create',str(bundle),b+'..HEAD')
        members['commits.bundle']=bundle.read_bytes()
    if sum(map(len,members.values()))>MAX_ZIP_BYTES:raise DeltaError('DELTA_TOO_LARGE: split research rounds or establish a new full baseline')
    manifest={'schema':SCHEMA,'round_id':round_id,'created_at_utc':now(),'base_commit':b,'head_commit':h,
        'base_tree':git(root,'rev-parse',b+'^{tree}').stdout.decode().strip(),
        'head_tree':git(root,'rev-parse',h+'^{tree}').stdout.decode().strip(),
        'members':{p:{'sha256':sha(data),'bytes':len(data)} for p,data in sorted(members.items())},
        'change_count':len(delta),'deletion_count':sum(r['operation']=='delete' for r in delta),
        'review_status':'NOT_AUDITED','full_cognition':'NOT_CERTIFIED_BY_EXPORT','authority':'Only user instruction authorizes sending; no network performed.'}
    members['MANIFEST.json']=encoded(manifest)
    out.parent.mkdir(parents=True,exist_ok=True)
    tmpout=out.with_name(out.name+'.partial')
    if tmpout.exists():raise DeltaError('PARTIAL_OUTPUT_EXISTS')
    try:
        with zipfile.ZipFile(tmpout,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as zipout:
            for name,data in sorted(members.items()):zipout.writestr(name,data)
        os.replace(tmpout,out)
    except Exception:
        # Preserve partial file for investigation rather than silently discarding failed work.
        raise
    receipt={'schema':'hott.delta-export-receipt.v1','zip':str(out),'zip_sha256':sha(out.read_bytes()),'zip_bytes':out.stat().st_size,'base_commit':b,'head_commit':h,'round_id':round_id,'status':'EXPORTED_NOT_AUDITED','changes':len(delta)}
    put(out.with_suffix(out.suffix+'.receipt.json'),encoded(receipt))
    clean(root)
    return receipt

def load_delta(path):
    with zipfile.ZipFile(path) as z:
        infos=z.infolist();names=[i.filename for i in infos]
        if len(names)!=len(set(names)):raise DeltaError('DUPLICATE_ZIP_ENTRY')
        if sum(i.file_size for i in infos)>MAX_ZIP_BYTES:raise DeltaError('UNCOMPRESSED_SIZE_LIMIT')
        norms=set()
        for i in infos:
            safe_rel(i.filename)
            key=unicodedata.normalize('NFC',i.filename).casefold()
            if key in norms:raise DeltaError('PORTABILITY_CASE_COLLISION')
            norms.add(key)
            if i.is_dir() or ((i.external_attr>>16)&0o170000)==0o120000:raise DeltaError('NON_FILE_MEMBER')
        data={name:z.read(name) for name in names}
    if 'MANIFEST.json' not in data:raise DeltaError('MISSING_MANIFEST')
    m=json.loads(data['MANIFEST.json'])
    if m.get('schema')!=SCHEMA:raise DeltaError('UNSUPPORTED_SCHEMA')
    if not IDENT.fullmatch(m.get('round_id','')):raise DeltaError('INVALID_ROUND_ID')
    for k in ['base_commit','head_commit','base_tree','head_tree']:
        if not OID.fullmatch(m.get(k,'')):raise DeltaError('INVALID_GIT_ID')
    if set(data)!=(set(m['members'])|{'MANIFEST.json'}):raise DeltaError('UNEXPECTED_OR_MISSING_MEMBER')
    for p,entry in m['members'].items():
        if len(data[p])!=entry['bytes'] or sha(data[p])!=entry['sha256']:raise DeltaError('CONTENT_HASH_MISMATCH: '+p)
    a=json.loads(data['BASE_SNAPSHOT.json']);b=json.loads(data['HEAD_SNAPSHOT.json']);delta=json.loads(data['CHANGES.json'])
    for t in (a,b):
        for path,r in t.items():
            safe_rel(path)
            if r['mode'] not in ['100644','100755'] or not OID.fullmatch(r['git_blob']):raise DeltaError('INVALID_TREE_ENTRY')
    if changes(a,b)!=delta:raise DeltaError('CHANGE_LIST_MISMATCH')
    expected={'MANIFEST.json','BASE_SNAPSHOT.json','HEAD_SNAPSHOT.json','CHANGES.json','changes.patch','README.md','commits.bundle'}
    expected|={'payload/'+r['path'] for r in delta if r['after']}
    if set(data)!=expected:raise DeltaError('PAYLOAD_PATH_MISMATCH')
    for r in delta:
        if r['after']:
            content=data['payload/'+r['path']]
            if sha(content)!=r['after']['sha256'] or len(content)!=r['after']['bytes']:raise DeltaError('TREE_PAYLOAD_MISMATCH')
    return m,data,a,b,delta

def verify_delta(path,root=None):
    m,data,a,b,delta=load_delta(path)
    if root is not None:
        base=commit(root,m['base_commit'])
        if snapshot(root,base)!=a:raise DeltaError('BASE_CONTENT_MISMATCH')
    return {'status':'INTEGRITY_VERIFIED_NOT_MATH_AUDITED','round_id':m['round_id'],'base_commit':m['base_commit'],'head_commit':m['head_commit'],'changes':len(delta),'base_content_verified':root is not None,'zip_sha256':sha(Path(path).read_bytes())}

def stage_delta(path,base_root,destination):
    clean(base_root);m,data,a,b,delta=load_delta(path)
    if commit(base_root,'HEAD')!=m['base_commit']:raise DeltaError('STALE_BASE: audit source HEAD differs; use a separate exact-base checkout')
    if snapshot(base_root,m['base_commit'])!=a:raise DeltaError('BASE_CONTENT_MISMATCH')
    dest=Path(destination).resolve()
    if dest.exists():raise DeltaError('DESTINATION_EXISTS')
    if dest==base_root or base_root in dest.parents:raise DeltaError('DESTINATION_INSIDE_BASE')
    dest.parent.mkdir(parents=True,exist_ok=True)
    git(base_root,'clone','--no-hardlinks','--no-checkout','--',str(base_root),str(dest))
    with tempfile.TemporaryDirectory(prefix='hott-delta-stage-') as tmp:
        bp=Path(tmp)/'commits.bundle';bp.write_bytes(data['commits.bundle'])
        git(dest,'bundle','verify',str(bp))
        git(dest,'fetch','--no-tags',str(bp),'HEAD')
    head=commit(dest,m['head_commit'])
    if git(dest,'merge-base','--is-ancestor',m['base_commit'],head,check=False).returncode:raise DeltaError('INVALID_ANCESTRY')
    if git(dest,'rev-parse',head+'^{tree}').stdout.decode().strip()!=m['head_tree']:raise DeltaError('HEAD_TREE_MISMATCH')
    if snapshot(dest,head)!=b:raise DeltaError('HEAD_CONTENT_MISMATCH')
    git(dest,'checkout','--detach',head)
    git(dest,'remote','remove','origin')
    for p,r in b.items():
        f=inside(dest,p)
        if not f.is_file() or sha(f.read_bytes())!=r['sha256']:raise DeltaError('CHECKOUT_CONTENT_MISMATCH')
    clean(dest);clean(base_root)
    return {'status':'STAGED_IN_ISOLATED_CLONE_NOT_MERGED','destination':str(dest),'head_commit':head,'source_unchanged':True,'scripts_executed':False,'review_status':'NOT_AUDITED'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=DEFAULT_ROOT)
    sub=ap.add_subparsers(dest='command',required=True)
    i=sub.add_parser('round-init');i.add_argument('--id',required=True);i.add_argument('--request-file',type=Path,required=True);i.add_argument('--base',default='handoff-r040')
    e=sub.add_parser('export');e.add_argument('--round',required=True);e.add_argument('--base');e.add_argument('--head',default='HEAD');e.add_argument('--output',type=Path)
    v=sub.add_parser('verify');v.add_argument('zip',type=Path);v.add_argument('--with-base',action='store_true')
    s=sub.add_parser('stage');s.add_argument('zip',type=Path);s.add_argument('--destination',type=Path,required=True)
    args=ap.parse_args();root=args.root.resolve()
    try:
        if args.command=='round-init':r=init_round(root,args.id,args.request_file,args.base)
        elif args.command=='export':
            rd=json.loads(inside(root,'exchange/rounds/'+args.round+'/ROUND.json').read_text())
            r=export_delta(root,args.round,args.base or rd['base_commit'],args.head,args.output or root/'exchange/outbox'/(args.round+'.zip'))
        elif args.command=='verify':r=verify_delta(args.zip,root if args.with_base else None)
        else:r=stage_delta(args.zip,root,args.destination)
        print(encoded(r).decode(),end='')
    except (DeltaError,OSError,ValueError,KeyError,zipfile.BadZipFile) as ex:
        print(encoded({'status':'FAILED','error':str(ex),'active_workspace_not_imported':True}).decode(),end='');raise SystemExit(2)
if __name__=='__main__':main()
