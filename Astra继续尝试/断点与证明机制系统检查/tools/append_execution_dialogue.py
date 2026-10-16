#!/usr/bin/env python3
"""Append through the user's explicit repair instruction using canonical visible events only."""
import json
from pathlib import Path
from append_marked_puncture import visible_events
from export_visible_dialogue import HOME_DIR, SOURCE, THREAD, READER, command, sha, write_new, jbytes

END = "msg_01a0baec-c22d-7c92-8da8-0457453bc37e"
TITLES = ["指定缺口的答复与方案修订", "外部AI反馈与后续执行准备", "继续尝试与先修复检查点的指令"]

def main():
    basefile=HOME_DIR/"evidence/对话归档清单.json"
    previousfile=HOME_DIR/"evidence/对话归档增量-002.json"
    base=json.loads(basefile.read_text());previous=json.loads(previousfile.read_text())
    oldrows=base["messages"]+previous["messages"]
    events=visible_events();end=next(e["sequence"] for e in events if e["name"]==END)
    start=previous["raw_line_range"][1]+1
    chosen=[e for e in events if start<=e["sequence"]<=end]
    turns=list(dict.fromkeys(e["turn_id"] for e in chosen));assert len(turns)==3
    rows=[];shards=[]
    for sn,(turn,title) in enumerate(zip(turns,TITLES),8):
        rel=Path("对话原文")/(f"{sn:03d} - {title}.md")
        body=(f"<!-- governance-shard:v2\nlogical_id: ASTRA-BREAKPOINT-DIALOGUE\nshard_id: {sn:03d}\nindex: ../对话原文.md\n-->\n\n# {title}\n\n历史可见原文，截止用户明确要求先修复加载与检查点。尚未发送的本轮final不冒充历史。\n\n").encode()
        for e in [e for e in chosen if e["turn_id"]==turn]:
            x=json.loads(command(["inspect","--host","codex","--source",str(SOURCE),e["locator"],"--no-truncate"]))
            assert not x.get("text_truncated") and x["session_id"]==THREAD
            kind="user" if x["role"]=="user" else ("assistant-final" if x["data"]["phase"]=="final_answer" else "assistant-commentary")
            ordinal=len(oldrows)+len(rows)+1;txt=Path("原始消息")/f"{ordinal:03d}-{kind}.txt";data=x["text"].encode()
            body+=f"## 消息 {ordinal:03d}｜{kind}\n\n时间：{x['timestamp']}；消息ID：{x['name']}。\n\n<!-- message-original:{x['name']}:start -->\n".encode()
            a=len(body);body+=data;b=len(body);body+=f"\n<!-- message-original:{x['name']}:end -->\n\n".encode()
            write_new(HOME_DIR/txt,data)
            rows.append({"ordinal":ordinal,"id":x["name"],"role":x["role"],"phase":x.get("data",{}).get("phase"),"turn_id":turn,"timestamp":x["timestamp"],"locator":x["locator"],"utf8_bytes":len(data),"sha256":sha(data),"text_file":str(txt),"shard":str(rel),"shard_byte_range":[a,b]})
        write_new(HOME_DIR/rel,body);shards.append({"number":sn,"title":title,"path":str(rel)})
    allrows=oldrows+rows;bad=[]
    expected=[e["name"] for e in events if base["raw_line_range"][0]<=e["sequence"]<=end]
    assert expected==[r["id"] for r in allrows]
    for x in allrows:
        data=(HOME_DIR/x["text_file"]).read_bytes();a,b=x["shard_byte_range"]
        canonical=json.loads(command(["inspect","--host","codex","--source",str(SOURCE),x["locator"],"--no-truncate"]))
        if sha(data)!=x["sha256"] or (HOME_DIR/x["shard"]).read_bytes()[a:b]!=data or canonical["text"].encode()!=data or canonical.get("text_truncated"):bad.append(x["id"])
    assert not bad
    counts={"user":sum(x["role"]=="user" for x in allrows),"assistant_final":sum(x["phase"]=="final_answer" for x in allrows),"assistant_commentary":sum(x["phase"]=="commentary" for x in allrows)}
    result={"schema_version":"astra-visible-dialogue-increment/v1","previous_manifest":"evidence/对话归档增量-002.json","previous_manifest_sha256":sha(previousfile.read_bytes()),"base_manifest_sha256":sha(basefile.read_bytes()),"raw_line_range":[start,end],"end_user_id":END,"reader":str(READER),"reader_sha256":sha(READER.read_bytes()),"messages":rows,"shards":shards,"cumulative_messages":len(allrows),"counts":counts,"source_is_live":True}
    write_new(HOME_DIR/"evidence/对话归档增量-003.json",jbytes(result))
    write_new(HOME_DIR/"evidence/对话逐字核验-003.json",jbytes({"status":"PASS","messages":len(allrows),"scope_and_order_match":True,"failures":bad,"comparison":"canonical inspect, independent txt and embedded shard bytes; UTF-8 exact"}))
    print(json.dumps({"status":"EXPORTED_AND_VERIFIED","cumulative":len(allrows),"counts":counts,"shards":shards},ensure_ascii=False))

if __name__=="__main__":main()
