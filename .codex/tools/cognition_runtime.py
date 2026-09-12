#!/usr/bin/env python3
"""File-based full cognition loading and optimistic checkpointing.

Standard library only. plan/read/check are read-only. checkpoint defaults to a
no-write preview; --apply and current user authorization are required to write.
No network, subprocess, model invocation, or mathematical verification occurs.
A coverage result concerns emitted file ranges, never the model's understanding.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import uuid

VERSION = '2.1.0'
PREFIX = '.codex/research/hott/'
CONFIG = '.codex/cognition/LOAD_SET.json'
STATE = PREFIX + 'STATE.json'
HEAD = '.codex/cognition/HEAD.json'
LOCK = '.codex/cognition/WRITE_LOCK.json'
TXN = '.codex/cognition/TRANSACTION.json'
SKILL = '.codex/skills/hott-paradox-research/SKILL.md'
GOVERNANCE_SKILL = '.codex/skills/hott-local-session-governance/SKILL.md'
ROLES = '.codex/skills/SKILL_ROLES.json'
OPEN_STATUSES = frozenset(('open','active','pending','blocked','in_progress','review_required'))
CLOSURE = '核心认知.md'
DIRECTION = '方向追踪.md'
PANORAMA = '全景视野.md'
QUESTIONS = 'HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md'
CLOSURE_ID = 'core-cognition-generation-1'
THREE_WAY = (CLOSURE, DIRECTION, PANORAMA)
MUTABLE = ('MEMORY.md', DIRECTION, PANORAMA, PREFIX+'FRONTIER.md', PREFIX+'LESSONS.md', PREFIX+'RESUME.md', STATE)
REQUIRED = (CLOSURE, QUESTIONS, 'AGENTS.md', 'README.md', 'MEMORY.md', 'feature-list.md', 'rulings.md',
            '核心认知.manifest.json', SKILL, GOVERNANCE_SKILL, ROLES, CONFIG, STATE,
            '.codex/skills/hott-paradox-research/references/top-level-repo-adaptation.md',
            '.codex/AGENTS.md', '.codex/cognition/PROTOCOL.md', '.codex/cognition/CORE_COGNITION.schema.json',
            '.codex/cognition/SOURCE_MANIFEST.schema.json', '.codex/verification/README.md',
            PREFIX+'FRONTIER.md', PREFIX+'LESSONS.md', PREFIX+'RESUME.md', '理解章节/README.md',
            '理解章节/C0-当前整合审计与证据边界-20260912.md', '理解章节/A0-总目标.md', '理解章节/A11-开放问题与悬空接头.md', '理解章节/B0-工作史总览.md',
            '理解章节/B1-本地GPT工作史.md', '理解章节/B2-网页GPT工作史-I.md', '理解章节/B3-网页GPT工作史-II.md',
            '理解章节/B4-Gemini工作史.md', '理解章节/B5-成果总账.md', 'audit/governance-impact.md',
            'audit/coverage-summary.json', 'audit/README.md', 'audit/LEDGER_SCHEMA.md', 'audit/ledger-summary.json', 'audit/verification-report.json',
            'audit/external-validation-20260912.json',
            'sources/SOURCE_MANIFEST.json', 'sources/README.md', '.codex/tools/cognition_runtime.py', 'scripts/audit/README.md',
            'scripts/audit/verify_core_cognition.py', 'scripts/audit/verify_history_ledgers.py', DIRECTION, PANORAMA,
            'scripts/audit/verify_three_way_cognition.py')
ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_-]{0,100}$')

class CognitionError(RuntimeError):
    pass

def stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def dump(obj) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2)+'\n').encode('utf-8')

def root_path(value=None) -> Path:
    if value is None:
        script = Path(__file__).resolve()
        if script.parent.name == 'tools' and script.parent.parent.name == '.codex':
            value = script.parents[2]
        elif script.parts[-5:-1] == ('.codex','skills','hott-paradox-research','scripts'):
            value = script.parents[4]
        else:
            raise CognitionError('ROOT_UNRESOLVED: use --project-root')
    p=Path(value)
    if p.is_symlink(): raise CognitionError('ROOT_SYMLINK')
    return p.resolve()

def path_of(root: Path, rel: str) -> Path:
    if not isinstance(rel,str) or not rel or '\\' in rel or '\x00' in rel:
        raise CognitionError('UNSAFE_PATH')
    p=PurePosixPath(rel)
    if p.is_absolute() or any(x in ('','..','.') for x in rel.split('/')):
        raise CognitionError('UNSAFE_PATH: '+rel)
    cursor=root
    for part in p.parts:
        cursor=cursor/part
        if cursor.is_symlink(): raise CognitionError('SYMLINK_FORBIDDEN: '+rel)
    try: cursor.resolve().relative_to(root)
    except ValueError as e: raise CognitionError('PATH_ESCAPE: '+rel) from e
    return cursor

def read_bytes(root, rel):
    p=path_of(root,rel)
    try:
        before=p.stat();data=p.read_bytes();after=p.stat()
    except OSError as e: raise CognitionError('MISSING_OR_UNREADABLE: '+rel) from e
    if (before.st_ino,before.st_size,before.st_mtime_ns)!=(after.st_ino,after.st_size,after.st_mtime_ns):
        raise CognitionError('CHANGED_DURING_READ: '+rel)
    return data

def obj(data):
    try:
        out=json.loads(data)
    except (ValueError,UnicodeError) as e:raise CognitionError('INVALID_JSON') from e
    if not isinstance(out,dict):raise CognitionError('JSON_OBJECT_REQUIRED')
    return out

def text(data, name):
    try:t=data.decode('utf-8')
    except UnicodeError as e:raise CognitionError('NOT_UTF8: '+name) from e
    if not t.strip():raise CognitionError('EMPTY_REQUIRED_FILE: '+name)
    return t

def validate_roles(get):
    roles=obj(get(ROLES))
    expected={'governance':('hott-local-session-governance',GOVERNANCE_SKILL),
              'business':('hott-paradox-research',SKILL)}
    if roles.get('schema_version') not in ('hott-skill-roles/v1', 'hott-skill-roles/v2') or not isinstance(roles.get('roles'),dict) or set(roles['roles'])!=set(expected):
        raise CognitionError('SKILL_ROLE_REGISTRY_INVALID')
    for role,(name,path) in expected.items():
        record=roles['roles'][role]
        if not isinstance(record,dict) or record.get('name')!=name or record.get('path')!=path:
            raise CognitionError('SKILL_ROLE_IDENTITY_MISMATCH: '+role)
        source=text(get(path),path)
        front=re.match(r'\A---\n(.*?)\n---\n',source,re.S)
        if not front or not re.search(r'^name: '+re.escape(name)+r'$',front[1],re.M):
            raise CognitionError('SKILL_FRONTMATTER_NAME_MISMATCH: '+role)

def is_open(record):
    return isinstance(record,dict) and isinstance(record.get('status'),str) and record['status'].casefold() in OPEN_STATUSES

def resolution_sources(record,key):
    value=record.get('resolution')
    if value is None:return []
    if not isinstance(value,dict) or not isinstance(value.get('reason'),str) or not value['reason'].strip():
        raise CognitionError('RESOLUTION_REASON_REQUIRED: '+key)
    paths=value.get('evidence')
    if not isinstance(paths,list) or not paths or any(not isinstance(x,str) or not x for x in paths):
        raise CognitionError('RESOLUTION_EVIDENCE_REQUIRED: '+key)
    return paths

def graph(config, state, get):
    if config.get('schema_version') not in ('cognition-load-set/v1', 'cognition-load-set/v2'):raise CognitionError('CONFIG_SCHEMA')
    fixed=config.get('fixed_full_text')
    if not isinstance(fixed,list) or any(not isinstance(x,str) for x in fixed) or len(set(fixed))!=len(fixed):raise CognitionError('FIXED_LIST_INVALID')
    if fixed[:3]!=list(THREE_WAY) or not set(REQUIRED)<=set(fixed):
        raise CognitionError('REQUIRED_COGNITION_REMOVED_OR_REORDERED')
    if config.get('three_way_order') != list(THREE_WAY):
        raise CognitionError('THREE_WAY_ORDER_INVALID')
    if config.get('dynamic_state')!=STATE:raise CognitionError('STATE_PATH_CHANGED')
    validate_roles(get)
    if state.get('schema_version')!='hott-working-state/v1' or type(state.get('revision')) is not int or state['revision']<1:
        raise CognitionError('STATE_SCHEMA')
    records=state.get('records')
    if not isinstance(records,dict):raise CognitionError('RECORDS_OBJECT_REQUIRED')
    seeds=[]
    latest=state.get('latest_session')
    if not isinstance(latest,str) or latest not in records or not isinstance(records[latest],dict) or records[latest].get('kind')!='session':
        raise CognitionError('LATEST_SESSION_MISSING')
    seeds.append(latest)
    for group in ('active','review_due','unresolved'):
        xs=state.get(group)
        if not isinstance(xs,list) or any(not isinstance(x,str) for x in xs) or len(set(xs))!=len(xs):raise CognitionError('SEED_LIST_INVALID: '+group)
        seeds.extend(xs)
    # Open records cannot disappear merely by omission from manually maintained seed lists.
    for key,record in records.items():
        if not isinstance(key,str) or not ID.fullmatch(key) or not isinstance(record,dict):
            raise CognitionError('INVALID_RECORD: '+str(key))
        if is_open(record):seeds.append(key)
    ordered=list(fixed);visited=set();visiting=set();selected=[];stale=set()
    def add(p):
        if not isinstance(p,str):raise CognitionError('PATH_STRING_REQUIRED')
        if p not in ordered:ordered.append(p)
    def visit(k):
        if k in visiting:raise CognitionError('DEPENDENCY_CYCLE: '+str(k))
        if k in visited:return
        if not isinstance(k,str) or not ID.fullmatch(k) or k not in records:
            raise CognitionError('MISSING_RECORD: '+str(k))
        record=records[k]
        if not isinstance(record,dict):raise CognitionError('INVALID_RECORD: '+k)
        visiting.add(k);add(record.get('path'))
        deps=record.get('depends_on',[]); sources=record.get('full_sources',[]); hashes=record.get('source_hashes',{})
        if not isinstance(deps,list) or not isinstance(sources,list) or not isinstance(hashes,dict):
            raise CognitionError('INVALID_DEPENDENCIES: '+k)
        for d in deps:visit(d)
        for p in sources:add(p)
        for p in resolution_sources(record,k):add(p)
        for p,h in hashes.items():
            add(p)
            if not isinstance(h,str) or not re.fullmatch('[0-9a-f]{64}',h):raise CognitionError('INVALID_SOURCE_HASH: '+k)
            if sha(get(p))!=h:stale.add(k)
        if any(d in stale for d in deps):stale.add(k)
        if record.get('status')=='review_required':stale.add(k)
        visiting.remove(k);visited.add(k);selected.append(k)
    for k in seeds:visit(k)
    # Directly declared dependencies are complete textual sources, not summaries.
    for p in ordered:text(get(p),p)
    if CLOSURE_ID not in '\n'.join(text(get(CLOSURE),CLOSURE).splitlines()[:12]):
        raise CognitionError('WRONG_CLOSURE_ID')
    for projection, marker in ((DIRECTION, 'integrated-direction-portfolio:v1'), (PANORAMA, 'integrated-outcome-panorama:v1')):
        if marker not in text(get(projection), projection):
            raise CognitionError('PROJECTION_MARKER_MISSING: '+projection)
    return ordered,selected,sorted(stale)

def plan(project_root=None, *, _allow_busy=False):
    root=root_path(project_root)
    if not _allow_busy and (path_of(root,LOCK).exists() or path_of(root,TXN).exists()):
        raise CognitionError('CHECKPOINT_INCOMPLETE_OR_WRITER_ACTIVE')
    head_bytes=read_bytes(root,HEAD);head=obj(head_bytes)
    if head.get('schema_version')!='cognition-head/v1':raise CognitionError('HEAD_SCHEMA')
    cache={}
    def get(rel):
        if rel not in cache:cache[rel]=read_bytes(root,rel)
        return cache[rel]
    state=obj(get(STATE));config=obj(get(CONFIG))
    if head.get('revision')!=state.get('revision') or head.get('latest_session')!=state.get('latest_session'):
        raise CognitionError('HEAD_STATE_MISMATCH')
    tracked=head.get('tracked')
    if not isinstance(tracked,dict) or not set(MUTABLE)<=set(tracked):raise CognitionError('HEAD_TRACKING_INCOMPLETE')
    for rel,h in tracked.items():
        if sha(get(rel))!=h:raise CognitionError('UNCOMMITTED_STATE: '+rel)
    paths,records,stale=graph(config,state,get)
    entries=[]
    for rel in paths:
        b=get(rel);t=text(b,rel)
        entries.append({'path':rel,'sha256':sha(b),'bytes':len(b),'lines':len(t.splitlines(keepends=True))})
    for rel,b in cache.items():
        if read_bytes(root,rel)!=b:raise CognitionError('SNAPSHOT_CHANGED: '+rel)
    if read_bytes(root,HEAD)!=head_bytes:raise CognitionError('HEAD_CHANGED')
    if not _allow_busy and (path_of(root,LOCK).exists() or path_of(root,TXN).exists()):raise CognitionError('WRITER_STARTED')
    signature=sha(dump({'head_sha256':sha(head_bytes),'files':entries}))
    return {'schema_version':'cognition-plan/v1','snapshot':signature,'revision':head['revision'],
            'latest_session':state['latest_session'],'documents':entries,'dynamic_records':records,
            'automatically_included_open_records':[k for k,r in state['records'].items() if is_open(r)],
            'review_required':stale,'total_bytes':sum(x['bytes'] for x in entries),
            'total_lines':sum(x['lines'] for x in entries),'model_context':'NOT_CERTIFIED_BY_TOOL',
            'policy':'NEW_FULL_READ_EVERY_INVOCATION_AND_AFTER_COMPACTION',
            'three_way_documents':list(THREE_WAY),
            'projection_status':config.get('projection_status','UNDECLARED')}

def read_chunk(project_root, snapshot, path, start_line=1, max_bytes=10000):
    root=root_path(project_root);p=plan(root)
    if snapshot!=p['snapshot']:raise CognitionError('STALE_SNAPSHOT_RESTART_ALL')
    entry=next((x for x in p['documents'] if x['path']==path),None)
    if entry is None:raise CognitionError('PATH_NOT_IN_CURRENT_LOAD_SET')
    if type(start_line) is not int or start_line<1 or type(max_bytes) is not int or max_bytes<1 or max_bytes>262144:
        raise CognitionError('INVALID_RANGE_OR_BUDGET')
    b=read_bytes(root,path)
    if sha(b)!=entry['sha256']:raise CognitionError('FILE_CHANGED')
    ls=text(b,path).splitlines(keepends=True)
    if start_line>len(ls):raise CognitionError('START_PAST_EOF')
    i=start_line-1;used=0;out=[]
    while i<len(ls):
        size=len(ls[i].encode('utf-8'))
        if used+size>max_bytes:
            if not out:raise CognitionError('LINE_TOO_LARGE_INCREASE_BUDGET')
            break
        out.append(ls[i]);used+=size;i+=1
    if plan(root)['snapshot']!=snapshot:raise CognitionError('SNAPSHOT_CHANGED_RESTART_ALL')
    body=''.join(out)
    return {'snapshot':snapshot,'path':path,'file_sha256':entry['sha256'],'start_line':start_line,
            'end_line':i,'total_lines':len(ls),'next_start_line':None if i==len(ls) else i+1,
            'chunk_sha256':sha(body.encode()),'text':body,'model_context':'NOT_CERTIFIED_BY_TOOL'}

def check_coverage(p, chunks):
    """Check supplied emitted ranges only; cannot certify the model read them."""
    by={x['path']:[] for x in p['documents']}
    for c in chunks:
        if c.get('snapshot')!=p['snapshot'] or c.get('path') not in by:raise CognitionError('COVERAGE_SNAPSHOT_OR_PATH')
        by[c['path']].append(c)
    for f in p['documents']:
        cursor=1;acc=[]
        for c in by[f['path']]:
            if c.get('file_sha256')!=f['sha256'] or c.get('start_line')!=cursor or c.get('end_line',0)<cursor:
                raise CognitionError('COVERAGE_GAP_OR_ORDER: '+f['path'])
            body=c.get('text','')
            if not isinstance(body,str) or len(body.splitlines(keepends=True))!=c['end_line']-cursor+1 or sha(body.encode())!=c.get('chunk_sha256'):
                raise CognitionError('COVERAGE_BODY_MISMATCH')
            acc.append(body);cursor=c['end_line']+1
        if cursor!=f['lines']+1 or sha(''.join(acc).encode())!=f['sha256']:
            raise CognitionError('COVERAGE_INCOMPLETE: '+f['path'])
    return {'status':'FULL_EMITTED_BYTES_MATCH','documents':len(by),'model_context':'NOT_CERTIFIED_BY_TOOL'}

def atomic(path: Path, data: bytes):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name('.'+path.name+'.tmp-'+uuid.uuid4().hex)
    try:
        with temp.open('xb') as f:f.write(data);f.flush();os.fsync(f.fileno())
        os.replace(temp,path)
        try:
            fd=os.open(path.parent,os.O_RDONLY);os.fsync(fd);os.close(fd)
        except OSError:pass
    finally:
        if temp.exists():temp.unlink()

def allowed_write(rel,sid):
    if rel in MUTABLE:return True
    if re.fullmatch(re.escape(PREFIX)+r'candidates/[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+',rel):return True
    if re.fullmatch(re.escape(PREFIX)+'sessions/'+re.escape(sid)+r'/[A-Za-z0-9_.-]+',rel):return True
    return False

def prepare(root, snapshot, payload, *, busy=False):
    p=plan(root,_allow_busy=busy)
    if snapshot!=p['snapshot']:raise CognitionError('STALE_BASE')
    if payload.get('schema_version')!='cognition-checkpoint/v1':raise CognitionError('PAYLOAD_SCHEMA')
    sid=payload.get('session_id')
    if not isinstance(sid,str) or not ID.fullmatch(sid):raise CognitionError('INVALID_SESSION_ID')
    if not isinstance(payload.get('authorization'),str) or not payload['authorization'].strip():raise CognitionError('AUTHORIZATION_STATEMENT_REQUIRED')
    if not isinstance(payload.get('files'),list):raise CognitionError('FILES_LIST_REQUIRED')
    changes={};old={}
    for row in payload['files']:
        if not isinstance(row,dict) or 'expected_sha256' not in row:raise CognitionError('EXPECTED_FILE_BASE_REQUIRED')
        rel=row.get('path');target=path_of(root,rel)
        if not allowed_write(rel,sid):raise CognitionError('WRITE_OUTSIDE_AUTHORIZED_STATE: '+str(rel))
        if rel in changes:raise CognitionError('DUPLICATE_WRITE')
        if not isinstance(row.get('text'),str):raise CognitionError('UTF8_TEXT_REQUIRED')
        before=read_bytes(root,rel) if target.exists() else None
        if (sha(before) if before is not None else None)!=row.get('expected_sha256'):raise CognitionError('FILE_BASE_MISMATCH: '+rel)
        if rel.startswith(PREFIX+'sessions/') and before is not None:raise CognitionError('SESSION_IMMUTABLE')
        changes[rel]=row['text'].encode();old[rel]=before
    if not set(MUTABLE)<=set(changes):raise CognitionError('INCOMPLETE_CHECKPOINT_STATE')
    session_path=PREFIX+'sessions/'+sid+'/SESSION.md'
    if session_path not in changes:raise CognitionError('SESSION_RECORD_REQUIRED')
    get=lambda rel: changes[rel] if rel in changes else read_bytes(root,rel)
    state=obj(get(STATE)); prior=obj(read_bytes(root,STATE))
    if state.get('revision')!=prior['revision']+1 or state.get('latest_session')!=sid:
        raise CognitionError('REVISION_OR_LATEST_SESSION_INVALID')
    if state.get('records',{}).get(sid,{}).get('path')!=session_path:raise CognitionError('SESSION_ROUTE_INVALID')
    _,_,stale=graph(obj(get(CONFIG)),state,get)
    for k in stale:
        if state['records'][k].get('status')!='review_required':raise CognitionError('DEPENDENCY_REVIEW_REQUIRED: '+k)
    # Removing old records would silently delete historical routing.
    if not set(prior['records'])<=set(state['records']):raise CognitionError('OLD_RECORD_ROUTING_REMOVED')
    for k,rec in prior['records'].items():
        new=state['records'][k]
        if not isinstance(new,dict) or new.get('path')!=rec.get('path') or new.get('kind')!=rec.get('kind'):
            raise CognitionError('RECORD_IDENTITY_CHANGED: '+k)
        if is_open(rec) and not is_open(new):
            if not resolution_sources(new,k):raise CognitionError('RESOLUTION_REQUIRED_TO_CLOSE: '+k)
            for evidence_path in resolution_sources(new,k):text(get(evidence_path),evidence_path)
        if rec.get('source_hashes')!=new.get('source_hashes') and not str(new.get('revalidation','')).strip():
            raise CognitionError('REVALIDATION_EXPLANATION_REQUIRED: '+k)
    head={'schema_version':'cognition-head/v1','revision':state['revision'],'latest_session':sid,
          'updated_at_utc':stamp(),'tracked':{x:sha(changes[x]) for x in MUTABLE}}
    changes[HEAD]=dump(head);old[HEAD]=read_bytes(root,HEAD)
    return p,sid,changes,old

def checkpoint(project_root,snapshot,payload,*,apply=False,_fail_after=None):
    root=root_path(project_root)
    p,sid,changes,old=prepare(root,snapshot,payload)
    if not apply:return {'status':'DRY_RUN','revision':p['revision']+1,'paths':list(changes),'writes':False}
    lock=path_of(root,LOCK)
    try:
        with lock.open('xb') as f:f.write(dump({'session_id':sid,'created_at_utc':stamp(),'pid':os.getpid()}));f.flush();os.fsync(f.fileno())
    except FileExistsError as e:raise CognitionError('WRITER_LOCKED') from e
    published=False
    try:
        p,sid,changes,old=prepare(root,snapshot,payload,busy=True)
        if path_of(root,TXN).exists():raise CognitionError('TRANSACTION_EXISTS')
        transaction_root='.codex/cognition/checkpoints/'+sid
        if path_of(root,transaction_root).exists():raise CognitionError('CHECKPOINT_ID_EXISTS')
        rows=[]
        for rel,b in changes.items():
            after=transaction_root+'/after/'+rel;atomic(path_of(root,after),b)
            before=transaction_root+'/before/'+rel if old[rel] is not None else None
            if before:atomic(path_of(root,before),old[rel])
            rows.append({'path':rel,'old_sha256':sha(old[rel]) if old[rel] is not None else None,'new_sha256':sha(b),
                         'before_copy':before,'after_copy':after})
        journal={'schema_version':'cognition-transaction/v1','session_id':sid,'base_snapshot':snapshot,
                 'rows':rows,'created_at_utc':stamp(),'authorization':payload['authorization']}
        atomic(path_of(root,transaction_root+'/transaction.json'),dump(journal))
        atomic(path_of(root,TXN),dump(journal));published=True
        for n,row in enumerate(rows,1):
            atomic(path_of(root,row['path']),changes[row['path']])
            if _fail_after==n:raise CognitionError('INJECTED_INTERRUPTION')
        for row in rows:
            if sha(read_bytes(root,row['path']))!=row['new_sha256']:raise CognitionError('POSTWRITE_MISMATCH')
        result={'status':'CHECKPOINT_COMMITTED','session_id':sid,'revision':p['revision']+1,'paths':list(changes),
                'model_understanding':'NOT_CERTIFIED','mathematics':'NOT_CERTIFIED','completed_at_utc':stamp()}
        atomic(path_of(root,transaction_root+'/result.json'),dump(result))
        path_of(root,TXN).unlink();published=False
        return result
    finally:
        if not published and lock.exists():
            if obj(lock.read_bytes()).get('session_id')==sid:lock.unlink()

def recover(project_root,action,*,confirm_owner_stopped=False):
    root=root_path(project_root)
    if not confirm_owner_stopped:raise CognitionError('EXPLICIT_OWNER_STOP_CONFIRMATION_REQUIRED')
    if action not in ('finish','rollback'):raise CognitionError('INVALID_RECOVERY_ACTION')
    journal=obj(read_bytes(root,TXN));sid=journal.get('session_id')
    lock=obj(read_bytes(root,LOCK))
    if journal.get('schema_version')!='cognition-transaction/v1' or not isinstance(sid,str) or not ID.fullmatch(sid):
        raise CognitionError('INVALID_RECOVERY_JOURNAL')
    if lock.get('session_id')!=sid:raise CognitionError('LOCK_OWNER_MISMATCH')
    rows=journal.get('rows',[])
    if not isinstance(rows,list) or not rows:raise CognitionError('TRANSACTION_EMPTY')
    base='.codex/cognition/checkpoints/'+sid
    if read_bytes(root,TXN)!=read_bytes(root,base+'/transaction.json'):
        raise CognitionError('RECOVERY_JOURNAL_MISMATCH')
    seen=set()
    for row in rows:
        if not isinstance(row,dict):raise CognitionError('RECOVERY_ROW_INVALID')
        rel=row.get('path')
        if not isinstance(rel,str) or rel in seen or (rel!=HEAD and not allowed_write(rel,sid)):
            raise CognitionError('RECOVERY_PATH_REJECTED')
        path_of(root,rel);seen.add(rel)
        old=row.get('old_sha256');new=row.get('new_sha256')
        if not isinstance(new,str) or not re.fullmatch('[0-9a-f]{64}',new) or (old is not None and (not isinstance(old,str) or not re.fullmatch('[0-9a-f]{64}',old))):
            raise CognitionError('RECOVERY_HASH_INVALID')
        expected_before=base+'/before/'+rel if old is not None else None
        if row.get('before_copy')!=expected_before or row.get('after_copy')!=base+'/after/'+rel:
            raise CognitionError('RECOVERY_BACKUP_PATH_INVALID')
    if not set(MUTABLE)<=seen or HEAD not in seen or rows[-1]['path']!=HEAD:
        raise CognitionError('RECOVERY_STATE_INCOMPLETE_OR_HEAD_NOT_LAST')
    # Refuse if anyone has written content not part of this transaction.
    for row in rows:
        p=path_of(root,row['path']);now=sha(read_bytes(root,row['path'])) if p.exists() else None
        if now not in (row['old_sha256'],row['new_sha256']):raise CognitionError('THIRD_PARTY_WRITE_RECOVERY_REFUSED')
        for key,hkey in [('before_copy','old_sha256'),('after_copy','new_sha256')]:
            if row[key] and sha(read_bytes(root,row[key]))!=row[hkey]:raise CognitionError('RECOVERY_BACKUP_CORRUPT')
    sequence=rows if action=='finish' else list(reversed(rows))
    for row in sequence:
        source=row['after_copy'] if action=='finish' else row['before_copy'];target=path_of(root,row['path'])
        if source:atomic(target,read_bytes(root,source))
        elif target.exists():target.unlink()
    res={'status':'RECOVERED_'+action.upper(),'session_id':sid,'timestamp':stamp(),'model_understanding':'NOT_CERTIFIED'}
    atomic(path_of(root,'.codex/cognition/checkpoints/'+sid+'/recovery.json'),dump(res))
    plan(root,_allow_busy=True)
    path_of(root,TXN).unlink();path_of(root,LOCK).unlink()
    plan(root)
    return res

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--project-root',type=Path)
    sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('plan')
    p=sub.add_parser('read');p.add_argument('--snapshot',required=True);p.add_argument('--path',required=True);p.add_argument('--start-line',type=int,default=1);p.add_argument('--max-bytes',type=int,default=10000)
    p=sub.add_parser('check');p.add_argument('--snapshot',required=True)
    p=sub.add_parser('checkpoint');p.add_argument('--snapshot',required=True);p.add_argument('--payload',type=Path,required=True);p.add_argument('--apply',action='store_true')
    p=sub.add_parser('recover');p.add_argument('--action',choices=['finish','rollback'],required=True);p.add_argument('--confirm-owner-stopped',action='store_true')
    a=ap.parse_args()
    try:
        if a.command=='plan':r=plan(a.project_root);r['invocation_nonce']=uuid.uuid4().hex
        elif a.command=='read':
            r=read_chunk(a.project_root,a.snapshot,a.path,a.start_line,a.max_bytes);body=r.pop('text')
            print('BEGIN_COGNITION_CHUNK');print(json.dumps(r,ensure_ascii=False));print('BEGIN_FULL_TEXT');sys.stdout.write(body)
            if not body.endswith('\n'):print()
            print('END_FULL_TEXT\nEND_COGNITION_CHUNK');return 0
        elif a.command=='check':
            r=plan(a.project_root)
            if r['snapshot']!=a.snapshot:raise CognitionError('STALE_SNAPSHOT_RESTART_ALL')
            r={'status':'SNAPSHOT_UNCHANGED','model_context':'NOT_CERTIFIED_BY_TOOL','snapshot':a.snapshot}
        elif a.command=='checkpoint':r=checkpoint(a.project_root,a.snapshot,obj(a.payload.read_bytes()),apply=a.apply)
        else:r=recover(a.project_root,a.action,confirm_owner_stopped=a.confirm_owner_stopped)
        print(json.dumps(r,ensure_ascii=False,indent=2));return 0
    except (CognitionError,OSError,ValueError,TypeError,KeyError) as e:
        print(json.dumps({'status':'BLOCKED','error':str(e)},ensure_ascii=False),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
