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

VERSION = '3.3.0'
SHARD_INDEX_MARKER = '<!-- governance-shard-index:v2'
SHARD_TABLE_START = '<!-- governance-shard-table:start -->'
SHARD_TABLE_END = '<!-- governance-shard-table:end -->'
SHARD_ROW_RE = re.compile(r'^\|\s*`?([A-Za-z0-9._-]+)`?\s*\|\s*\[([^]]+)\]\(([^)]+)\)\s*\|')
SHARD_NAME_RE = re.compile(r'^(?P<shard_id>[0-9]{3}) - (?P<title>.+)\.md$')
H1_RE = re.compile(r'^#\s+(.+?)\s*$', re.MULTILINE)
SHARD_INDEX_KEYS = ('logical_id','mode','shard_root','last_shard','append_target','soft_line_target')
PREFIX = '.codex/research/hott/'
CONFIG = '.codex/cognition/LOAD_SET.json'
STATE = PREFIX + 'STATE.json'
HEAD = '.codex/cognition/HEAD.json'
LOCK = '.codex/cognition/WRITE_LOCK.json'
TXN = '.codex/cognition/TRANSACTION.json'
SKILL = '.codex/skills/hott-paradox-research/SKILL.md'
GOVERNANCE_SKILL = '.codex/skills/hott-local-session-governance/SKILL.md'
ROLES = '.codex/skills/SKILL_ROLES.json'
LEGACY_OPEN_STATUSES = frozenset(('open','active','pending','blocked','in_progress','review_required'))
LIVE_LIFECYCLES = frozenset(('ACTIVE_WORK','CURRENT','OPEN_ISSUE'))
EVIDENCE_REVIEW_STATUSES = frozenset(('UNREVIEWED','REVIEW_REQUIRED','UNKNOWN','NOT_RUN'))
PROFILES = frozenset(('governance','research'))
CLOSURE = '核心认知.md'
DIRECTION = '方向追踪.md'
PANORAMA = '全景视野.md'
QUESTIONS = 'HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md'
CLOSURE_GENERATION_RE = re.compile(r'core-cognition-generation-[0-9]+')
THREE_WAY = (CLOSURE, DIRECTION, PANORAMA)
MUTABLE = ('MEMORY.md', DIRECTION, PANORAMA, PREFIX+'FRONTIER.md', PREFIX+'LESSONS.md', PREFIX+'RESUME.md', STATE)
REQUIRED_BOOT = (
    'AGENTS.md','README.md','MEMORY.md','feature-list.md','rulings.md','.codex/AGENTS.md',
    ROLES,GOVERNANCE_SKILL,'.codex/cognition/PROTOCOL.md',CONFIG,STATE,
)
REQUIRED_RESEARCH = (SKILL,QUESTIONS,PREFIX+'FRONTIER.md',PREFIX+'LESSONS.md',PREFIX+'RESUME.md')
ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_-]{0,100}$')
KC_ID = re.compile(r'^KC-[0-9]{6}$')
KC_RELATIONS = frozenset(('ALIGNED','DEEPENED','CORRECTED','TENSION','DEVIATED','NOT_TOUCHED'))
SESSION_REQUIRED_FILES = ('SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md')

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

def parse_shard_index(data, rel):
    """Parse a v2 governance shard index; return None when the file is not one.

    Structural failure raises instead of degrading to a plain document, so a
    broken index can never silently drop the shards it owns.  The full contract
    check lives in scripts/audit/validate_governance_shards.py; this parser only
    enforces what the load path needs to stay fail-closed.
    """
    body=text(data,rel);lines=body.splitlines()
    try:start=next(i for i,line in enumerate(lines) if line.strip()==SHARD_INDEX_MARKER)
    except StopIteration:return None
    meta={};closed=False
    for line in lines[start+1:]:
        stripped=line.strip()
        if stripped=='-->':closed=True;break
        if not stripped or ':' not in stripped:continue
        key,value=stripped.split(':',1);meta[key.strip()]=value.strip()
    if not closed:raise CognitionError('SHARD_INDEX_MARKER_UNTERMINATED: '+rel)
    missing=[k for k in SHARD_INDEX_KEYS if not meta.get(k)]
    if missing:raise CognitionError('SHARD_INDEX_KEYS_MISSING: '+rel+':'+','.join(missing))
    if meta['mode'] not in ('topical','sequential'):raise CognitionError('SHARD_INDEX_MODE_INVALID: '+rel)
    try:table=body.split(SHARD_TABLE_START,1)[1].split(SHARD_TABLE_END,1)[0]
    except IndexError as e:raise CognitionError('SHARD_INDEX_TABLE_MISSING: '+rel) from e
    rows=[]
    for line in table.splitlines():
        match=SHARD_ROW_RE.match(line.strip())
        if not match:continue
        shard_id,title,link=match.group(1),match.group(2).strip(),match.group(3).strip()
        if link.startswith('<') and link.endswith('>'):link=link[1:-1]
        base=PurePosixPath(rel).parent
        normalized=(base/link).as_posix() if str(base)!='.' else link
        rows.append({'shard_id':shard_id,'title':title,'link':link,'path':normalized})
    if not rows:raise CognitionError('SHARD_INDEX_TABLE_EMPTY: '+rel)
    ids=[r['shard_id'] for r in rows];paths=[r['link'] for r in rows]
    if len(set(ids))!=len(ids) or len(set(paths))!=len(paths):
        raise CognitionError('SHARD_INDEX_DUPLICATE: '+rel)
    if meta['last_shard']!=paths[-1]:raise CognitionError('SHARD_INDEX_LAST_SHARD_MISMATCH: '+rel)
    if meta['mode']=='sequential' and meta['append_target']!=meta['last_shard']:
        raise CognitionError('SHARD_INDEX_APPEND_TARGET_MISMATCH: '+rel)
    if meta['mode']=='topical' and meta['append_target']!='-':
        raise CognitionError('SHARD_INDEX_APPEND_TARGET_INVALID: '+rel)
    stem=PurePosixPath(rel).stem
    if meta['shard_root']!=stem:raise CognitionError('SHARD_INDEX_ROOT_MISMATCH: '+rel)
    for row in rows:
        parts=PurePosixPath(row['link']).parts
        if len(parts)!=2 or parts[0]!=stem:raise CognitionError('SHARD_PATH_NOT_DIRECT_CHILD: '+row['path'])
        name=SHARD_NAME_RE.fullmatch(parts[1])
        if name is None or name.group('shard_id')!=row['shard_id'] or name.group('title')!=row['title']:
            raise CognitionError('SHARD_NAME_MISMATCH: '+row['path'])
    return {'logical_id':meta['logical_id'],'mode':meta['mode'],'shard_root':meta['shard_root'],
            'shard_root_rel':(PurePosixPath(rel).parent/meta['shard_root']).as_posix(),
            'last_shard':meta['last_shard'],'append_target':meta['append_target'],
            'soft_line_target':meta['soft_line_target'],'shards':rows}

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

def legacy_is_open(record):
    return isinstance(record,dict) and isinstance(record.get('status'),str) and record['status'].casefold() in LEGACY_OPEN_STATUSES

def lifecycle_of(record,key,state):
    if state.get('schema_version')=='hott-working-state/v2':
        return record.get('lifecycle_status')
    if key in state.get('active',[]):return 'ACTIVE_WORK'
    if record.get('kind')=='session':return 'HISTORICAL'
    if legacy_is_open(record):return 'OPEN_ISSUE'
    if record.get('status') in ('closed','complete'):return 'CLOSED'
    return 'HISTORICAL'

def evidence_of(record):
    value=record.get('evidence_status')
    if isinstance(value,str):return value
    return 'REVIEW_REQUIRED' if record.get('status')=='review_required' else 'VERIFIED_WITH_SCOPE'

def resolution_sources(record,key):
    value=record.get('resolution')
    if value is None:return []
    if not isinstance(value,dict) or not isinstance(value.get('reason'),str) or not value['reason'].strip():
        raise CognitionError('RESOLUTION_REASON_REQUIRED: '+key)
    paths=value.get('evidence')
    if not isinstance(paths,list) or not paths or any(not isinstance(x,str) or not x for x in paths):
        raise CognitionError('RESOLUTION_EVIDENCE_REQUIRED: '+key)
    return paths

def config_paths(config,key):
    value=config.get(key)
    if not isinstance(value,list) or any(not isinstance(x,str) or not x for x in value) or len(set(value))!=len(value):
        raise CognitionError('CONFIG_PATH_LIST_INVALID: '+key)
    return value

def graph(config, state, get, profile='governance', task_ids=(), core_transition=None, path_kind=None, listdir=None):
    if config.get('schema_version')!='cognition-load-set/v3':raise CognitionError('CONFIG_SCHEMA')
    if profile not in PROFILES:raise CognitionError('LOAD_PROFILE_INVALID: '+str(profile))
    trio=config_paths(config,'always_full_three_way')
    boot=config_paths(config,'always_full_boot')
    research=config_paths(config,'research_full')
    query_first=config_paths(config,'query_first')
    task_expand=config_paths(config,'task_expand')
    archive=config_paths(config,'archive_verify_only')
    if trio!=list(THREE_WAY):raise CognitionError('THREE_WAY_ORDER_INVALID')
    if not set(REQUIRED_BOOT)<=set(boot):raise CognitionError('REQUIRED_BOOT_COGNITION_REMOVED')
    if not set(REQUIRED_RESEARCH)<=set(research):raise CognitionError('REQUIRED_RESEARCH_COGNITION_REMOVED')
    categorized=trio+boot+research+query_first+task_expand+archive
    duplicates=sorted({path for path in categorized if categorized.count(path)>1})
    if duplicates:raise CognitionError('LOAD_LAYER_OVERLAP: '+','.join(duplicates))
    if config.get('three_way_order') != list(THREE_WAY):
        raise CognitionError('THREE_WAY_ORDER_INVALID')
    if config.get('dynamic_state')!=STATE:raise CognitionError('STATE_PATH_CHANGED')
    validate_roles(get)
    if state.get('schema_version') not in ('hott-working-state/v1','hott-working-state/v2') or type(state.get('revision')) is not int or state['revision']<1:
        raise CognitionError('STATE_SCHEMA')
    records=state.get('records')
    if not isinstance(records,dict):raise CognitionError('RECORDS_OBJECT_REQUIRED')
    latest=state.get('latest_session')
    if not isinstance(latest,str) or latest not in records or not isinstance(records[latest],dict) or records[latest].get('kind')!='session':
        raise CognitionError('LATEST_SESSION_MISSING')
    for group in ('active','review_due','unresolved'):
        xs=state.get(group)
        if not isinstance(xs,list) or any(not isinstance(x,str) for x in xs) or len(set(xs))!=len(xs):raise CognitionError('SEED_LIST_INVALID: '+group)
    available=[]
    for key,record in records.items():
        if not isinstance(key,str) or not ID.fullmatch(key) or not isinstance(record,dict):
            raise CognitionError('INVALID_RECORD: '+str(key))
        lifecycle=lifecycle_of(record,key,state);evidence=evidence_of(record)
        if lifecycle not in LIVE_LIFECYCLES|{'CLOSED','HISTORICAL','SUPERSEDED'}:
            raise CognitionError('LIFECYCLE_STATUS_INVALID: '+key)
        if state.get('schema_version')=='hott-working-state/v2' and (not isinstance(record.get('evidence_status'),str) or not record['evidence_status']):
            raise CognitionError('EVIDENCE_STATUS_REQUIRED: '+key)
        mode=record.get('path_mode','document')
        if mode not in ('document','scope_locator'):
            raise CognitionError('RECORD_PATH_MODE_INVALID: '+key)
        related=record.get('related_records',[])
        if not isinstance(related,list) or any(not isinstance(x,str) or x not in records for x in related) or len(set(related))!=len(related):
            raise CognitionError('RELATED_RECORDS_INVALID: '+key)
        available.append({'id':key,'kind':record.get('kind'),'path':record.get('path'),'path_mode':mode,
                          'lifecycle_status':lifecycle,'evidence_status':evidence})
    if any(not isinstance(k,str) or k not in records for k in task_ids) or len(set(task_ids))!=len(tuple(task_ids)):
        raise CognitionError('TASK_RECORD_SELECTION_INVALID')
    ordered=[];selection={};visited=set();visiting=set();selected=[];stale=set();logical={}
    def add_raw(p,layer,selected_by,logical_id=None,logical_role=None):
        if not isinstance(p,str):raise CognitionError('PATH_STRING_REQUIRED')
        if p not in ordered:
            ordered.append(p)
            selection[p]={'layer':layer,'selected_by':[selected_by],'logical_id':logical_id,
                          'logical_role':logical_role,'full_load':logical_role is not None}
        else:
            if selected_by not in selection[p]['selected_by']:selection[p]['selected_by'].append(selected_by)
            if logical_id is not None:
                selection[p]['logical_id']=logical_id;selection[p]['logical_role']=logical_role
                selection[p]['full_load']=True

    def add(p,layer,selected_by):
        add_raw(p,layer,selected_by)
        try:data=get(p)
        except CognitionError:return
        index=parse_shard_index(data,p)
        if index is None or index['logical_id'] in logical:return
        logical[index['logical_id']]=index
        if listdir is not None:
            listed={PurePosixPath(row['path']).name for row in index['shards']}
            for name in listdir(index['shard_root_rel']):
                if SHARD_NAME_RE.fullmatch(name) and name not in listed:
                    raise CognitionError('UNLISTED_SHARD: '+index['shard_root_rel']+'/'+name)
        add_raw(p,layer,'shard-index:'+selected_by,index['logical_id'],'index')
        for row in index['shards']:
            heading=H1_RE.search(text(get(row['path']),row['path']))
            if heading is None or heading.group(1).strip()!=row['title']:
                raise CognitionError('SHARD_TITLE_MISMATCH: '+row['path'])
            add_raw(row['path'],layer,'shard:'+index['logical_id'],index['logical_id'],'shard')
    for p in trio:add(p,'always_full_three_way','fixed-trio')
    for p in boot:add(p,'always_full_boot','boot-policy')
    if profile=='research':
        for p in research:add(p,'research_full','profile:research')
    add(records[latest].get('path'),'current_summary','latest-session:'+latest)
    for key in state.get('active',[]):
        if key not in records:raise CognitionError('MISSING_ACTIVE_RECORD: '+key)
        add(records[key].get('path'),'current_record','active:'+key)
    def visit(k):
        if k in visiting:raise CognitionError('DEPENDENCY_CYCLE: '+str(k))
        if k in visited:return
        if not isinstance(k,str) or not ID.fullmatch(k) or k not in records:
            raise CognitionError('MISSING_RECORD: '+str(k))
        record=records[k]
        if not isinstance(record,dict):raise CognitionError('INVALID_RECORD: '+k)
        visiting.add(k)
        primary=record.get('path');mode=record.get('path_mode','document')
        if mode=='document':
            add(primary,'task_expand','task:'+k)
        elif mode=='scope_locator':
            if path_kind is None or path_kind(primary)!='directory':
                raise CognitionError('SCOPE_LOCATOR_NOT_DIRECTORY: '+k)
        deps=record.get('depends_on',[]); sources=record.get('full_sources',[]); hashes=record.get('source_hashes',{})
        if not isinstance(deps,list) or not isinstance(sources,list) or not isinstance(hashes,dict):
            raise CognitionError('INVALID_DEPENDENCIES: '+k)
        if mode=='scope_locator' and not sources and not resolution_sources(record,k):
            raise CognitionError('SCOPE_LOCATOR_EVIDENCE_REQUIRED: '+k)
        for d in deps:visit(d)
        for p in sources:add(p,'task_expand','full-source:'+k)
        for p in resolution_sources(record,k):add(p,'task_expand','resolution:'+k)
        for p,h in hashes.items():
            add(p,'task_expand','source-hash:'+k)
            if not isinstance(h,str) or not re.fullmatch('[0-9a-f]{64}',h):raise CognitionError('INVALID_SOURCE_HASH: '+k)
            if sha(get(p))!=h:stale.add(k)
        if any(d in stale for d in deps):stale.add(k)
        if evidence_of(record) in EVIDENCE_REVIEW_STATUSES:stale.add(k)
        visiting.remove(k);visited.add(k);selected.append(k)
    for k in task_ids:visit(k)
    for p in ordered:text(get(p),p)
    closure_bytes = get(CLOSURE)
    closure_header = '\n'.join(text(closure_bytes, CLOSURE).splitlines()[:12])
    current_core = state.get('current_core')
    if state.get('schema_version') == 'hott-working-state/v2':
        if not isinstance(current_core, dict):
            raise CognitionError('CURRENT_CORE_IDENTITY_MISSING')
        expected_generation = current_core.get('generation')
        if not isinstance(expected_generation, str) or not CLOSURE_GENERATION_RE.fullmatch(expected_generation):
            raise CognitionError('CURRENT_CORE_GENERATION_INVALID')
        if expected_generation not in closure_header:
            if not isinstance(core_transition, dict):
                raise CognitionError('WRONG_CLOSURE_GENERATION')
            target_generation = core_transition.get('to_generation')
            if core_transition.get('from_generation') != expected_generation or target_generation not in closure_header:
                raise CognitionError('CORE_TRANSITION_GENERATION_MISMATCH')
            manifest_path = core_transition.get('manifest')
            transition_path = core_transition.get('transition')
            if not isinstance(manifest_path, str) or not isinstance(transition_path, str):
                raise CognitionError('CORE_TRANSITION_EVIDENCE_PATH_MISSING')
            manifest = obj(get(manifest_path))
            transition = obj(get(transition_path))
            if (manifest.get('generation') != target_generation
                    or manifest.get('core_document_sha256') != sha(closure_bytes)
                    or transition.get('previous', {}).get('generation') != expected_generation
                    or transition.get('current', {}).get('generation') != target_generation
                    or transition.get('current', {}).get('core_sha256') != sha(closure_bytes)
                    or transition.get('mapping_remainder') != 0
                    or transition.get('mapping_count') != transition.get('previous', {}).get('unit_count')):
                raise CognitionError('CORE_TRANSITION_EVIDENCE_INVALID')
    elif not CLOSURE_GENERATION_RE.search(closure_header):
        raise CognitionError('WRONG_CLOSURE_GENERATION')
    for projection, marker in ((DIRECTION, 'integrated-direction-portfolio:v1'), (PANORAMA, 'integrated-outcome-panorama:v1')):
        if marker not in text(get(projection), projection):
            raise CognitionError('PROJECTION_MARKER_MISSING: '+projection)
    return ordered,selection,selected,sorted(stale),available

def plan(project_root=None, *, profile='governance', task_ids=(), _allow_busy=False, _allow_core_transition=None):
    root=root_path(project_root)
    if not _allow_busy and (path_of(root,LOCK).exists() or path_of(root,TXN).exists()):
        raise CognitionError('CHECKPOINT_INCOMPLETE_OR_WRITER_ACTIVE')
    head_bytes=read_bytes(root,HEAD);head=obj(head_bytes)
    if head.get('schema_version')!='cognition-head/v1':raise CognitionError('HEAD_SCHEMA')
    cache={}
    def get(rel):
        if rel not in cache:cache[rel]=read_bytes(root,rel)
        return cache[rel]
    def kind(rel):
        p=path_of(root,rel)
        if p.is_file():return 'file'
        if p.is_dir():return 'directory'
        return 'missing'
    def listdir(rel):
        p=path_of(root,rel)
        if not p.is_dir():return []
        return sorted(x.name for x in p.iterdir() if x.is_file())
    state=obj(get(STATE));config=obj(get(CONFIG))
    if head.get('revision')!=state.get('revision') or head.get('latest_session')!=state.get('latest_session'):
        raise CognitionError('HEAD_STATE_MISMATCH')
    tracked=head.get('tracked')
    if not isinstance(tracked,dict) or not set(MUTABLE)<=set(tracked):raise CognitionError('HEAD_TRACKING_INCOMPLETE')
    for rel,h in tracked.items():
        if sha(get(rel))!=h:raise CognitionError('UNCOMMITTED_STATE: '+rel)
    task_ids=tuple(task_ids)
    paths,selection,records,stale,available=graph(config,state,get,profile,task_ids,_allow_core_transition,kind,listdir)
    entries=[]
    for rel in paths:
        b=get(rel);t=text(b,rel)
        entries.append({'path':rel,'sha256':sha(b),'bytes':len(b),'lines':len(t.splitlines(keepends=True)),
                        'layer':selection[rel]['layer'],'selected_by':selection[rel]['selected_by'],
                        'logical_id':selection[rel].get('logical_id'),
                        'logical_role':selection[rel].get('logical_role'),
                        'full_load':bool(selection[rel].get('full_load'))})
    for rel,b in cache.items():
        if read_bytes(root,rel)!=b:raise CognitionError('SNAPSHOT_CHANGED: '+rel)
    if read_bytes(root,HEAD)!=head_bytes:raise CognitionError('HEAD_CHANGED')
    if not _allow_busy and (path_of(root,LOCK).exists() or path_of(root,TXN).exists()):raise CognitionError('WRITER_STARTED')
    signature=sha(dump({'head_sha256':sha(head_bytes),'profile':profile,'task_ids':list(task_ids),'files':entries}))
    query_first_promoted=sorted(set(config.get('query_first',[])) & {x['path'] for x in entries})
    largest=sorted(entries,key=lambda x:(-x['bytes'],x['path']))[:10]
    logical_documents=[]
    for entry in entries:
        if entry['logical_role']!='index':continue
        index=parse_shard_index(get(entry['path']),entry['path'])
        shards=[x for x in entries if x['logical_id']==entry['logical_id'] and x['logical_role']=='shard']
        logical_documents.append({'logical_id':entry['logical_id'],'index':entry['path'],
                                  'mode':index['mode'] if index else None,'shard_count':len(shards),
                                  'shards':[x['path'] for x in shards],
                                  'bytes':entry['bytes']+sum(x['bytes'] for x in shards),
                                  'lines':entry['lines']+sum(x['lines'] for x in shards),
                                  'full_load_required':True})
    return {'schema_version':'cognition-plan/v2','snapshot':signature,'revision':head['revision'],
            'latest_session':state['latest_session'],'profile':profile,'task_ids':list(task_ids),
            'documents':entries,'hydrated_records':records,'available_records':available,
            'automatically_included_historical_sessions':[],
            'review_required':stale,'total_bytes':sum(x['bytes'] for x in entries),
            'total_lines':sum(x['lines'] for x in entries),'model_context':'NOT_CERTIFIED_BY_TOOL',
            'hydration_diagnostics':{'document_count':len(entries),'query_first_promoted':query_first_promoted,
                                     'logical_documents':[{k:d[k] for k in ('logical_id','index','mode','shard_count')} for d in logical_documents],
                                     'largest_documents':[{'path':x['path'],'bytes':x['bytes'],'lines':x['lines']} for x in largest]},
            'logical_documents':logical_documents,
            'policy':'FULL_TRIO_EVERY_SESSION_AND_COMPACTION_PLUS_PROFILED_TASK_HYDRATION',
            'three_way_documents':list(THREE_WAY),
            'query_first_documents':query_first if (query_first:=config.get('query_first')) else [],
            'archive_verify_only_documents':archive if (archive:=config.get('archive_verify_only')) else [],
            'projection_status':config.get('projection_status','UNDECLARED')}

def read_chunk(project_root, snapshot, path, start_line=1, max_bytes=10000, *, profile='governance', task_ids=()):
    root=root_path(project_root);p=plan(root,profile=profile,task_ids=task_ids)
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
    if plan(root,profile=profile,task_ids=task_ids)['snapshot']!=snapshot:raise CognitionError('SNAPSHOT_CHANGED_RESTART_ALL')
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

def query_record(project_root,record_id):
    root=root_path(project_root);base=plan(root)
    state=obj(read_bytes(root,STATE));records=state.get('records',{})
    if not isinstance(record_id,str) or not ID.fullmatch(record_id) or record_id not in records:
        raise CognitionError('RECORD_NOT_FOUND: '+str(record_id))
    record=records[record_id]
    return {'schema_version':'cognition-record-query/v1','record_id':record_id,
            'lifecycle_status':lifecycle_of(record,record_id,state),'evidence_status':evidence_of(record),
            'record':record,'base_snapshot':base['snapshot'],
            'hydrate_with':{'profile':'research','task_ids':[record_id]},
            'model_context':'NOT_CERTIFIED_BY_TOOL'}

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

def mutable_shard_paths(root):
    """Shard paths owned by MUTABLE logical documents (index plus ordered shards)."""
    owned={}
    for rel in MUTABLE:
        try:data=read_bytes(root,rel)
        except CognitionError:continue
        index=parse_shard_index(data,rel)
        if index is None:continue
        for row in index['shards']:owned[row['path']]=index['logical_id']
    return owned

def allowed_write(rel,sid,root=None,proposed=None):
    if rel in MUTABLE:return True
    if re.fullmatch(re.escape(PREFIX)+r'candidates/[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+',rel):return True
    if re.fullmatch(re.escape(PREFIX)+'sessions/'+re.escape(sid)+r'/[A-Za-z0-9_.-]+',rel):return True
    if proposed and rel in proposed:return True
    if root is not None and rel in mutable_shard_paths(root):return True
    return False

def validate_session_bundle(get, sid, state):
    """Require session evidence before a checkpoint can become durable.

    This validates structure and exact KC coverage only.  It cannot infer or
    certify the semantic quality of an assessment.
    """
    base=PREFIX+'sessions/'+sid+'/'
    required={name:base+name for name in SESSION_REQUIRED_FILES}
    session=text(get(required['SESSION.md']),required['SESSION.md'])
    if sid not in session:raise CognitionError('SESSION_ID_NOT_IN_RECORD')
    runs=obj(get(required['RUNS.json']))
    if runs.get('session_id')!=sid or not isinstance(runs.get('schema_version'),str) or not runs['schema_version']:
        raise CognitionError('SESSION_RUNS_IDENTITY_INVALID')
    audit=text(get(required['CORE_COGNITION_AUDIT.md']),required['CORE_COGNITION_AUDIT.md'])
    if sid not in audit:raise CognitionError('KC_AUDIT_SESSION_ID_MISMATCH')
    current_core=state.get('current_core',{})
    generation=current_core.get('generation');expected_count=current_core.get('kc_count')
    if not isinstance(generation,str) or generation not in audit or type(expected_count) is not int or expected_count<1:
        raise CognitionError('KC_AUDIT_CORE_IDENTITY_INVALID')
    rows=[]
    for line in audit.splitlines():
        if not line.startswith('| `KC-'):continue
        cells=[cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(cells)<5:raise CognitionError('KC_AUDIT_ROW_INVALID')
        kc=cells[0].strip('` ');relation=cells[2].strip('` ')
        if not KC_ID.fullmatch(kc) or relation not in KC_RELATIONS:
            raise CognitionError('KC_AUDIT_ROW_INVALID')
        if not cells[3] or not cells[4]:raise CognitionError('KC_AUDIT_EVIDENCE_REQUIRED: '+kc)
        rows.append(kc)
    expected=[f'KC-{n:06d}' for n in range(1,expected_count+1)]
    if rows!=expected:raise CognitionError('KC_AUDIT_COVERAGE_OR_ORDER_INVALID')
    for field in ('core_change','direction_change','panorama_change','update_decision','cross_conflicts','unresolved'):
        if not re.search(r'(?mi)^[-*]?\s*'+re.escape(field)+r'\s*:',audit):
            raise CognitionError('KC_AUDIT_THREE_WAY_FIELD_MISSING: '+field)

def prepare(root, snapshot, payload, *, busy=False):
    root=root_path(root)
    profile=payload.get('load_profile','governance')
    task_ids=payload.get('task_ids',[])
    if not isinstance(task_ids,list):raise CognitionError('CHECKPOINT_TASK_IDS_INVALID')
    core_transition=payload.get('core_transition')
    p=plan(root,profile=profile,task_ids=task_ids,_allow_busy=busy,_allow_core_transition=core_transition)
    if snapshot!=p['snapshot']:raise CognitionError('STALE_BASE')
    if payload.get('schema_version')!='cognition-checkpoint/v1':raise CognitionError('PAYLOAD_SCHEMA')
    sid=payload.get('session_id')
    if not isinstance(sid,str) or not ID.fullmatch(sid):raise CognitionError('INVALID_SESSION_ID')
    if not isinstance(payload.get('authorization'),str) or not payload['authorization'].strip():raise CognitionError('AUTHORIZATION_STATEMENT_REQUIRED')
    if not isinstance(payload.get('files'),list):raise CognitionError('FILES_LIST_REQUIRED')
    proposed={}
    for row in payload['files']:
        if not isinstance(row,dict):continue
        index_rel=row.get('path')
        if index_rel not in MUTABLE or not isinstance(row.get('text'),str):continue
        proposed_index=parse_shard_index(row['text'].encode('utf-8'),index_rel)
        if proposed_index is None:continue
        for shard_row in proposed_index['shards']:proposed[shard_row['path']]=proposed_index['logical_id']
    changes={};old={}
    for row in payload['files']:
        if not isinstance(row,dict) or 'expected_sha256' not in row:raise CognitionError('EXPECTED_FILE_BASE_REQUIRED')
        rel=row.get('path');target=path_of(root,rel)
        if not allowed_write(rel,sid,root,proposed):raise CognitionError('WRITE_OUTSIDE_AUTHORIZED_STATE: '+str(rel))
        if rel in changes:raise CognitionError('DUPLICATE_WRITE')
        if not isinstance(row.get('text'),str):raise CognitionError('UTF8_TEXT_REQUIRED')
        before=read_bytes(root,rel) if target.exists() else None
        if (sha(before) if before is not None else None)!=row.get('expected_sha256'):raise CognitionError('FILE_BASE_MISMATCH: '+rel)
        if rel.startswith(PREFIX+'sessions/') and before is not None:raise CognitionError('SESSION_IMMUTABLE')
        changes[rel]=row['text'].encode();old[rel]=before
    if not set(MUTABLE)<=set(changes):raise CognitionError('INCOMPLETE_CHECKPOINT_STATE')
    session_path=PREFIX+'sessions/'+sid+'/SESSION.md'
    if session_path not in changes:raise CognitionError('SESSION_RECORD_REQUIRED')
    for name in SESSION_REQUIRED_FILES:
        if PREFIX+'sessions/'+sid+'/'+name not in changes:
            raise CognitionError('SESSION_EVIDENCE_REQUIRED: '+name)
    get=lambda rel: changes[rel] if rel in changes else read_bytes(root,rel)
    state=obj(get(STATE)); prior=obj(read_bytes(root,STATE))
    if state.get('revision')!=prior['revision']+1 or state.get('latest_session')!=sid:
        raise CognitionError('REVISION_OR_LATEST_SESSION_INVALID')
    if prior.get('schema_version')=='hott-working-state/v1' and state.get('schema_version')=='hott-working-state/v2':
        migration=state.get('schema_migration')
        if not isinstance(migration,dict) or migration.get('from')!='hott-working-state/v1' or migration.get('to')!='hott-working-state/v2':
            raise CognitionError('STATE_SCHEMA_MIGRATION_RECEIPT_REQUIRED')
        if not isinstance(migration.get('rollback_ref'),str) or not migration['rollback_ref']:
            raise CognitionError('STATE_SCHEMA_MIGRATION_ROLLBACK_REQUIRED')
        receipt=migration.get('receipt')
        if not isinstance(receipt,str):raise CognitionError('STATE_SCHEMA_MIGRATION_PATH_REQUIRED')
        text(get(receipt),receipt)
    elif state.get('schema_version')!=prior.get('schema_version'):
        raise CognitionError('STATE_SCHEMA_TRANSITION_INVALID')
    if state.get('records',{}).get(sid,{}).get('path')!=session_path:raise CognitionError('SESSION_ROUTE_INVALID')
    validate_session_bundle(get,sid,state)
    def kind(rel):
        if rel in changes:return 'file'
        p=path_of(root,rel)
        if p.is_file():return 'file'
        if p.is_dir():return 'directory'
        return 'missing'
    def listdir(rel):
        names=set()
        p=path_of(root,rel)
        if p.is_dir():names|={x.name for x in p.iterdir() if x.is_file()}
        prefix=rel+'/'
        for candidate in changes:
            if candidate.startswith(prefix) and '/' not in candidate[len(prefix):]:
                names.add(candidate[len(prefix):])
        return sorted(names)
    _,_,_,stale,_=graph(obj(get(CONFIG)),state,get,profile,tuple(task_ids),core_transition,path_kind=kind,listdir=listdir)
    for k in stale:
        if evidence_of(state['records'][k])!='REVIEW_REQUIRED':raise CognitionError('DEPENDENCY_REVIEW_REQUIRED: '+k)
    # Removing old records would silently delete historical routing.
    if not set(prior['records'])<=set(state['records']):raise CognitionError('OLD_RECORD_ROUTING_REMOVED')
    for k,rec in prior['records'].items():
        new=state['records'][k]
        if not isinstance(new,dict) or new.get('path')!=rec.get('path') or new.get('kind')!=rec.get('kind'):
            raise CognitionError('RECORD_IDENTITY_CHANGED: '+k)
        old_live=lifecycle_of(rec,k,prior) in LIVE_LIFECYCLES
        new_live=lifecycle_of(new,k,state) in LIVE_LIFECYCLES
        if (legacy_is_open(rec) and not legacy_is_open(new)) or (old_live and not new_live):
            if not resolution_sources(new,k):raise CognitionError('RESOLUTION_REQUIRED_TO_CLOSE: '+k)
            for evidence_path in resolution_sources(new,k):text(get(evidence_path),evidence_path)
        if rec.get('source_hashes')!=new.get('source_hashes') and not str(new.get('revalidation','')).strip():
            raise CognitionError('REVALIDATION_EXPLANATION_REQUIRED: '+k)
        if rec.get('depends_on',[])!=new.get('depends_on',[]) and new.get('depends_on'):
            if new.get('dependency_semantics')!='verification_staleness':
                raise CognitionError('DEPENDENCY_SEMANTICS_REQUIRED: '+k)
    for k,new in state['records'].items():
        if k not in prior['records'] and new.get('depends_on') and new.get('dependency_semantics')!='verification_staleness':
            raise CognitionError('DEPENDENCY_SEMANTICS_REQUIRED: '+k)
    tracked={x:sha(changes[x]) for x in MUTABLE}
    for rel in MUTABLE:
        index=parse_shard_index(changes[rel],rel)
        if index is None:continue
        for row in index['shards']:
            shard=row['path']
            if shard not in changes:raise CognitionError('SHARD_NOT_IN_CHECKPOINT: '+shard)
            tracked[shard]=sha(changes[shard])
    head={'schema_version':'cognition-head/v1','revision':state['revision'],'latest_session':sid,
          'updated_at_utc':stamp(),'tracked':tracked}
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
        if not isinstance(rel,str) or rel in seen or (rel!=HEAD and not allowed_write(rel,sid,root)):
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
    p=sub.add_parser('plan');p.add_argument('--profile',choices=sorted(PROFILES),default='governance');p.add_argument('--task',action='append',default=[])
    p=sub.add_parser('read');p.add_argument('--snapshot',required=True);p.add_argument('--path',required=True);p.add_argument('--start-line',type=int,default=1);p.add_argument('--max-bytes',type=int,default=10000);p.add_argument('--profile',choices=sorted(PROFILES),default='governance');p.add_argument('--task',action='append',default=[])
    p=sub.add_parser('check');p.add_argument('--snapshot',required=True);p.add_argument('--profile',choices=sorted(PROFILES),default='governance');p.add_argument('--task',action='append',default=[])
    p=sub.add_parser('query');p.add_argument('--record',required=True)
    p=sub.add_parser('checkpoint');p.add_argument('--snapshot',required=True);p.add_argument('--payload',type=Path,required=True);p.add_argument('--apply',action='store_true')
    p=sub.add_parser('recover');p.add_argument('--action',choices=['finish','rollback'],required=True);p.add_argument('--confirm-owner-stopped',action='store_true')
    a=ap.parse_args()
    try:
        if a.command=='plan':r=plan(a.project_root,profile=a.profile,task_ids=a.task);r['invocation_nonce']=uuid.uuid4().hex
        elif a.command=='read':
            r=read_chunk(a.project_root,a.snapshot,a.path,a.start_line,a.max_bytes,profile=a.profile,task_ids=a.task);body=r.pop('text')
            print('BEGIN_COGNITION_CHUNK');print(json.dumps(r,ensure_ascii=False));print('BEGIN_FULL_TEXT');sys.stdout.write(body)
            if not body.endswith('\n'):print()
            print('END_FULL_TEXT\nEND_COGNITION_CHUNK');return 0
        elif a.command=='check':
            r=plan(a.project_root,profile=a.profile,task_ids=a.task)
            if r['snapshot']!=a.snapshot:raise CognitionError('STALE_SNAPSHOT_RESTART_ALL')
            r={'status':'SNAPSHOT_UNCHANGED','model_context':'NOT_CERTIFIED_BY_TOOL','snapshot':a.snapshot}
        elif a.command=='query':r=query_record(a.project_root,a.record)
        elif a.command=='checkpoint':r=checkpoint(a.project_root,a.snapshot,obj(a.payload.read_bytes()),apply=a.apply)
        else:r=recover(a.project_root,a.action,confirm_owner_stopped=a.confirm_owner_stopped)
        print(json.dumps(r,ensure_ascii=False,indent=2));return 0
    except (CognitionError,OSError,ValueError,TypeError,KeyError) as e:
        print(json.dumps({'status':'BLOCKED','error':str(e)},ensure_ascii=False),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
