#!/usr/bin/env python3
"""Append a pinned visible-message increment using the canonical reader only.

The first 21 exported texts and their manifest remain immutable. This renderer
adds a separate increment and updates only the navigational archive index.
"""
from pathlib import Path
import argparse,json,os,subprocess,sys
from export_visible_dialogue import ROOT,HOME_DIR,READER,SOURCE,THREAD,command,sha,write_new,jbytes

END='msg_01a0babe-5430-78d3-a0e1-c92cd26fe814'
DELTA=HOME_DIR/'evidence/对话归档增量-002.json'
TITLE='归档交付与指定缺口的新问题'

def visible_events():
    text=command(['scan','--host','codex','--source',str(SOURCE),'--kind','user_message','--kind','assistant_message','--json','--text-chars','1','--limit','10000'])
    return [v for v in map(json.loads,text.splitlines()) if v.get('schema_version')=='agent-session-trajectory/v1'
            and (v['role']=='user' or v.get('data',{}).get('phase') in ('commentary','final_answer'))]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');args=ap.parse_args()
    basefile=HOME_DIR/'evidence/对话归档清单.json';base=json.loads(basefile.read_text());events=visible_events()
    if args.verify:
        delta=json.loads(DELTA.read_text());rows=base['messages']+delta['messages'];bad=[]
        selected=[e['name'] for e in events if base['raw_line_range'][0]<=e['sequence']<=delta['raw_line_range'][1]]
        if selected!=[x['id'] for x in rows]:bad.append('SCOPE_OR_ORDER')
        if sha(basefile.read_bytes())!=delta['previous_manifest_sha256']:bad.append('BASE_MANIFEST_CHANGED')
        for x in rows:
            body=(HOME_DIR/x['text_file']).read_bytes();doc=(HOME_DIR/x['shard']).read_bytes();a,b=x['shard_byte_range']
            native=json.loads(command(['inspect','--host','codex','--source',str(SOURCE),x['locator'],'--no-truncate']))
            if sha(body)!=x['sha256'] or doc[a:b]!=body or native.get('text_truncated') or native['text'].encode()!=body:bad.append(x['id'])
        result={'schema_version':'astra-visible-dialogue-increment-check/v1','messages':len(rows),'scope_count':len(selected),
                'coverage_and_order_match':selected==[x['id'] for x in rows],'status':'PASS' if not bad else 'FAIL','failures':bad,
                'comparison':'Exact UTF-8, including terminal newline; canonical inspect + independent txt + embedded shard bytes.'}
        (HOME_DIR/'evidence/对话逐字核验-002.json').write_bytes(jbytes(result));print(json.dumps(result,ensure_ascii=False));return int(bool(bad))
    end=next(e['sequence'] for e in events if e['name']==END);start=base['raw_line_range'][1]+1
    chosen=[e for e in events if start<=e['sequence']<=end]
    if len(chosen)!=6 or chosen[-1]['role']!='user':raise RuntimeError('Unexpected increment denominator')
    snapshot=HOME_DIR/'evidence/方案v1.0基线';snaprows=[]
    for rel in ['README.md','对话原文.md','系统化后续检查方案.md','系统化后续检查方案/002 - 语义路线与删点表示保真.md',
                '系统化后续检查方案/005 - 程序化候选、覆盖与遗漏检查.md','系统化后续检查方案/006 - 执行次序、证据与停止条件.md','tools/check_delivery.py']:
        p=HOME_DIR/rel;data=p.read_bytes();dst=snapshot/(rel+'.txt');write_new(dst,data)
        snaprows.append({'original_path':rel,'snapshot':str(dst.relative_to(HOME_DIR)),'sha256':sha(data),'bytes':len(data)})
    write_new(HOME_DIR/'evidence/方案修订前基线.json',jbytes(snaprows))
    shard=Path('对话原文')/f'007 - {TITLE}.md'
    body=(f'<!-- governance-shard:v2\nlogical_id: ASTRA-BREAKPOINT-DIALOGUE\nshard_id: 007\nindex: ../对话原文.md\n-->\n\n# {TITLE}\n\n'
          '本片承接初始快照截止点，逐字保存此前归档交付的其余可见消息及本轮新的完整用户提问。当前尚未发送的答复不作为历史final记录。\n\n').encode()
    rows=[]
    for e in chosen:
        x=json.loads(command(['inspect','--host','codex','--source',str(SOURCE),e['locator'],'--no-truncate']))
        if x.get('text_truncated') or x['session_id']!=THREAD:raise RuntimeError('Wrong or truncated event')
        kind='user' if x['role']=='user' else ('assistant-final' if x['data']['phase']=='final_answer' else 'assistant-commentary')
        i=len(base['messages'])+len(rows)+1;p=Path('原始消息')/f'{i:03d}-{kind}.txt';text=x['text'].encode()
        body+=f'## 消息 {i:03d}｜{kind}\n\n时间：{x["timestamp"]}；消息ID：{x["name"]}。\n\n<!-- message-original:{x["name"]}:start -->\n'.encode()
        a=len(body);body+=text;b=len(body);body+=f'\n<!-- message-original:{x["name"]}:end -->\n\n'.encode()
        write_new(HOME_DIR/p,text)
        rows.append({'ordinal':i,'id':x['name'],'role':x['role'],'phase':x.get('data',{}).get('phase'),'turn_id':x['turn_id'],
                     'timestamp':x['timestamp'],'locator':x['locator'],'utf8_bytes':len(text),'characters':len(x['text']),
                     'sha256':sha(text),'text_file':str(p),'shard':str(shard),'shard_byte_range':[a,b]})
    write_new(HOME_DIR/shard,body)
    allrows=base['messages']+rows
    manifest={'schema_version':'astra-visible-dialogue-increment/v1','previous_manifest':'evidence/对话归档清单.json',
              'previous_manifest_sha256':sha(basefile.read_bytes()),'thread_id':THREAD,'end_user_id':END,'raw_line_range':[start,end],
              'messages':rows,'cumulative_messages':len(allrows),'completed_pairs':sum(x['phase']=='final_answer' for x in allrows),
              'counts':{'user':sum(x['role']=='user' for x in allrows),'assistant_final':sum(x['phase']=='final_answer' for x in allrows),
                        'assistant_commentary':sum(x['phase']=='commentary' for x in allrows)}}
    write_new(DELTA,jbytes(manifest))
    index=HOME_DIR/'对话原文.md';old=index.read_text();new=old.replace('last_shard: 对话原文/006 - 本轮落盘指令与起点澄清.md',f'last_shard: {shard}')
    new=new.replace('下方 6 个分片','下方 7 个分片')
    new=new.replace('本快照含五轮已完成问答、其间全部可见AI过程消息，以及本轮落盘指令和起点澄清，截止到该澄清用户消息。','当前归档含六轮已完成问答、其间可见AI过程消息，以及最新的指定缺口与特殊构造方法完整提问，共27条消息。初始21条快照及清单原样保留，新增6条由独立增量清单拥有。')
    new=new.replace('<!-- governance-shard-table:end -->',f'| 007 | [{TITLE}](<{shard}>) | 前轮交付及最新完整提问 | archived-source |\n<!-- governance-shard-table:end -->')
    new+='\n当前增量：[增量清单](evidence/对话归档增量-002.json)；[27条逐字核验](evidence/对话逐字核验-002.json)。原始提问仍是001片完整代码块，不因增量改变起点。\n'
    if new==old:raise RuntimeError('Index not updated')
    index.write_text(new)
    print(json.dumps({'status':'APPENDED','increment_messages':len(rows),'cumulative_messages':len(allrows),'counts':manifest['counts']},ensure_ascii=False))
    return 0
if __name__=='__main__':raise SystemExit(main())
