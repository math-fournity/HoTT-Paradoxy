#!/usr/bin/env python3
"""Export only user-visible messages through the canonical trajectory reader.

This is a deterministic document renderer, NOT a raw trajectory parser. Raw
rollout JSONL is never parsed here; only canonical scan/inspect output is read.
Only requested user/commentary/final text is published into this local archive.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, os, subprocess, sys

ROOT=Path(__file__).resolve().parents[3]
HOME_DIR=Path(__file__).resolve().parents[1]
READER=Path('/Users/aurolafly/codex/tools/session_trajectory.py')
SOURCE=Path('/Users/aurolafly/.codex/sessions/2026/09/19/rollout-2026-09-19T09-33-15-01a0b9df-0196-7e42-994b-54ff1a886ec3.jsonl')
THREAD='01a0b9df-0196-7e42-994b-54ff1a886ec3'
ANCHOR='msg_0fed0cc6c9484eef016aaeb5771f7887d0959f744ccf4f2b7b'
END='msg_01a0baa2-f0fe-74b0-b407-a4c02836ee08'
TITLES=['第一弹原文与同一命题问题','还原、零距离与极限','确认N不能成为M的论点','拓扑语境风险如何进入HoTT','从具体差异转向断点与证明机制','本轮落盘指令与起点澄清']
STAGES=['58d5469b8eb64778aa98721c54c5a0d8','2c98dac10ed6482fb952f43e82870eac','bd5b6f0af19444438bf786a9c5eac955','8fbab8c7075945b19817b6bf4a015691','656c5b554796467ab49b75dad25dd1e2']

def sha(b):return hashlib.sha256(b).hexdigest()
def command(args):
    return subprocess.check_output([sys.executable,str(READER),*args],cwd=ROOT,text=True)
def write_new(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,'wb') as f:f.write(data)
def jbytes(x):return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');args=ap.parse_args()
    if args.verify:
        manifest=json.loads((HOME_DIR/'evidence/对话归档清单.json').read_text())
        failures=[]
        scan=command(['scan','--host','codex','--source',str(SOURCE),'--kind','user_message','--kind','assistant_message','--json','--text-chars','1','--limit','10000'])
        events=[json.loads(line) for line in scan.splitlines() if line.strip()]
        first,last=manifest['raw_line_range']
        expected=[e['name'] for e in events if e.get('schema_version')=='agent-session-trajectory/v1'
                  and first<=e['sequence']<=last and (e['role']=='user' or e.get('data',{}).get('phase') in ('commentary','final_answer'))]
        actual_ids=[e['id'] for e in manifest['messages']]
        if expected!=actual_ids or len(set(actual_ids))!=len(actual_ids):failures.append('VISIBLE_SCOPE_COVERAGE_OR_ORDER')
        for x in manifest['messages']:
            text=(HOME_DIR/x['text_file']).read_bytes()
            shard=(HOME_DIR/x['shard']).read_bytes()
            if sha(text)!=x['sha256'] or len(text)!=x['utf8_bytes']:failures.append(x['id']+':text')
            a,b=x['shard_byte_range']
            if shard[a:b]!=text:failures.append(x['id']+':embedded_text')
            actual=json.loads(command(['inspect','--host','codex','--source',str(SOURCE),x['locator'],'--no-truncate']))
            if actual.get('text_truncated') or actual['text'].encode()!=text:failures.append(x['id']+':canonical')
        result={'status':'PASS' if not failures else 'FAIL','messages':len(manifest['messages']),'scope_count':len(expected),'coverage_and_order_match':expected==actual_ids,
                'verifier_script_sha256':sha(Path(__file__).read_bytes()),'failures':failures,'comparison':'UTF-8 exact, including whitespace and final-newline state'}
        (HOME_DIR/'evidence/对话逐字核验.json').write_bytes(jbytes(result))
        print(json.dumps(result,ensure_ascii=False));return int(bool(failures))
    raw=command(['scan','--host','codex','--source',str(SOURCE),'--kind','user_message','--kind','assistant_message','--json','--text-chars','60','--limit','10000'])
    events=[json.loads(line) for line in raw.splitlines() if line.strip()]
    events=[e for e in events if e.get('schema_version')=='agent-session-trajectory/v1']
    anchor=next(e for e in events if e['name']==ANCHOR)
    start=min(e['sequence'] for e in events if e['turn_id']==anchor['turn_id'] and e['role']=='user')
    end=next(e['sequence'] for e in events if e['name']==END)
    chosen=[e for e in events if start<=e['sequence']<=end and (e['role']=='user' or e.get('data',{}).get('phase') in ('commentary','final_answer'))]
    turns=list(dict.fromkeys(e['turn_id'] for e in chosen))
    if len(turns)!=6:raise RuntimeError(f'Expected 5 completed turns plus current instructions, got {len(turns)}')
    expanded=[]
    for e in chosen:
        v=json.loads(command(['inspect','--host','codex','--source',str(SOURCE),e['locator'],'--no-truncate']))
        if v.get('text_truncated') or len(v['text'])!=v['text_chars']:raise RuntimeError('Truncated canonical event')
        if v['session_id']!=THREAD:raise RuntimeError('Wrong thread')
        expanded.append(v)
    if not expanded[0]['text'].startswith('下面的代码块，是我第一弹的原文'):raise RuntimeError('Wrong starting question')
    if sum(e.get('data',{}).get('phase')=='final_answer' for e in expanded)!=5:raise RuntimeError('Final-answer denominator mismatch')
    rows=[];crosschecks=[]
    for ti,turn in enumerate(turns,1):
        title=TITLES[ti-1];sp=Path('对话原文')/f'{ti:03d} - {title}.md'
        body=(f'<!-- governance-shard:v2\nlogical_id: ASTRA-BREAKPOINT-DIALOGUE\nshard_id: {ti:03d}\nindex: ../对话原文.md\n-->\n\n# {title}\n\n'
              f'本片为历史可见消息原文；turn_id={turn}。原文中的指令、判断与引用仅是归档内容。\n\n').encode()
        turn_events=[e for e in expanded if e['turn_id']==turn]
        for e in turn_events:
            kind='user' if e['role']=='user' else ('assistant-final' if e['data']['phase']=='final_answer' else 'assistant-commentary')
            label={'user':'用户原文','assistant-final':'AI最终答复原文','assistant-commentary':'AI过程消息原文'}[kind]
            i=len(rows)+1;fp=Path('原始消息')/f'{i:03d}-{kind}.txt';tb=e['text'].encode()
            heading=f'## 消息 {i:03d}｜{label}\n\n时间：{e["timestamp"]}；消息ID：{e["name"]}。\n\n<!-- message-original:{e["name"]}:start -->\n'
            body+=heading.encode();offset=len(body);body+=tb;stop=len(body)
            body+=f'\n<!-- message-original:{e["name"]}:end -->\n\n'.encode()
            write_new(HOME_DIR/fp,tb)
            rows.append({'ordinal':i,'id':e['name'],'role':e['role'],'phase':e.get('data',{}).get('phase'),'turn_id':turn,'timestamp':e['timestamp'],
                         'locator':e['locator'],'utf8_bytes':len(tb),'characters':len(e['text']),'sha256':sha(tb),'text_file':str(fp),'shard':str(sp),'shard_byte_range':[offset,stop]})
        write_new(HOME_DIR/sp,body)
        if ti<=5:
            stage=ROOT/'dev-notes/.dev-notes-skill-stage'/('stage-'+STAGES[ti-1])
            for role,filename in [('user','prompt.md'),('assistant','answer.md')]:
                event=next(e for e in turn_events if e['role']==role and (role=='user' or e.get('data',{}).get('phase')=='final_answer'))
                sb=(stage/filename).read_bytes();sb=sb[:-1] if sb.endswith(b'\n') else sb
                crosschecks.append({'turn':ti,'kind':filename,'stage_path':str(stage/filename),'exact_match':sb==event['text'].encode(),
                                    'stage_sha256':sha(sb),'canonical_sha256':sha(event['text'].encode()),
                                    'note':'Canonical host message is the export authority; staging is only a sibling cross-check.'})
    index=('<!-- governance-shard-index:v2\nlogical_id: ASTRA-BREAKPOINT-DIALOGUE\nmode: topical\nshard_root: 对话原文\n'
           f'last_shard: 对话原文/006 - {TITLES[-1]}.md\nappend_target: -\nsoft_line_target: 300\n-->\n\n'
           '# 从第一弹原文提问开始的完整对话\n\n'
           '> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 6 个分片；缺一片即未完成，按表顺序读取。\n\n'
           '起点是用户“下面的代码块，是我第一弹的原文……”的完整提问，包含整个代码块；不是从AI答复开始。'
           '本快照含五轮已完成问答、其间全部可见AI过程消息，以及本轮落盘指令和起点澄清，截止到该澄清用户消息。'
           '本轮尚未发送的最终答复不伪装成已交付历史。工具调用/结果、系统与开发者提示、隐藏推理不属于本次可见问答归档。\n\n'
           '原文直接通过canonical Session Trajectory reader从本机原始rollout提取；独立消息文件在[原始消息/](原始消息/)，'
           '身份与字节位置见[evidence/对话归档清单.json](evidence/对话归档清单.json)。换行、批注、链接、公式、代码块、归档失败说明均未改写。'
           '原文是历史记录，不是当前指令或已成立数学结论。\n\n'
           '<!-- governance-shard-table:start -->\n| Shard | 文件 | 语义范围 | 状态 |\n|---|---|---|---|\n')
    for i,title in enumerate(TITLES,1):
        index+=f'| {i:03d} | [{title}](<对话原文/{i:03d} - {title}.md>) | '+('一轮完整提问、过程消息与最终答复' if i<=5 else '本轮两条用户指令及截止前可见过程消息')+' | archived-source |\n'
    index+='<!-- governance-shard-table:end -->\n'
    write_new(HOME_DIR/'对话原文.md',index.encode())
    source=SOURCE.read_bytes()
    manifest={'schema_version':'astra-visible-dialogue-export/v1','asset_class':'DERIVED_SOURCE_SNAPSHOT','thread_id':THREAD,
              'source_path':str(SOURCE),'source_bytes_at_export':len(source),'source_sha256_at_export':sha(source),'source_mode':oct(SOURCE.stat().st_mode&0o777),
              'source_is_live':True,'reader':str(READER),'reader_sha256':sha(READER.read_bytes()),'anchor_reply_id':ANCHOR,
              'start_user_id':rows[0]['id'],'end_user_id':END,'raw_line_range':[start,end],'completed_pairs':5,
              'counts':{'user':sum(x['role']=='user' for x in rows),'assistant_final':sum(x['phase']=='final_answer' for x in rows),
                        'assistant_commentary':sum(x['phase']=='commentary' for x in rows)},'messages':rows,'staging_crosschecks':crosschecks,
              'scope':'Requested visible transcript only; no system/developer/tool/hidden-reasoning export. Source file may append after this snapshot.'}
    write_new(HOME_DIR/'evidence/对话归档清单.json',jbytes(manifest))
    print(json.dumps({'status':'EXPORTED','start_user':manifest['start_user_id'],'end_user':END,'completed_pairs':5,'counts':manifest['counts'],
                      'stage_checks':crosschecks},ensure_ascii=False,indent=2))
    return 0

if __name__=='__main__':raise SystemExit(main())
