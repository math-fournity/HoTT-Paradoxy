#!/usr/bin/env python3
"""Generate FULL-TEXT ordered input volumes from the current governance snapshot.
This creates derived reading files, NOT evidence that an AI read or understood them.
"""
from pathlib import Path
import argparse,hashlib,json,math,socket
from unittest.mock import patch
from govern import load
ROOT=Path(__file__).resolve().parents[2]
TEXT_EXT={'.md','.txt','.py','.sh','.agda','.lean','.tex','.json','.csv','.yaml','.yml','.toml'}

def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def tokenizer():
 try:
  import tiktoken
  def denied(*args,**kw):raise OSError('offline tokenizer lookup only')
  with patch('socket.getaddrinfo',denied),patch('socket.socket.connect',denied):enc=tiktoken.get_encoding('cl100k_base')
  return enc,'cl100k_base (reference only, not the recipient model tokenizer)'
 except Exception:return None,'NOT_AVAILABLE_OFFLINE; no target-token count claimed'

def make_volumes(root,out,label,docs,enc):
 volumes=[];chunks=[];buf=[];used=0;num=1
 def flush():
  nonlocal buf,used,num
  if not buf:return
  name=f'{label}-{num:03d}.md';raw=(''.join(buf)).encode('utf-8');(out/name).write_bytes(raw)
  volumes.append({'path':'volumes/'+name,'bytes':len(raw),'sha256':sha(raw),'reference_tokens':len(enc.encode(raw.decode('utf-8'),disallowed_special=())) if enc else None})
  buf=[];used=0;num+=1
 for d in docs:
  path=root/d['path'];raw=path.read_bytes()
  if sha(raw)!=d['sha256']:raise ValueError('Source changed: '+d['path'])
  text=raw.decode('utf-8');lines=text.splitlines(keepends=True)
  start=1
  while start<=len(lines):
   part=[];size=0;end=start-1
   while end<len(lines):
    line=lines[end];n=len(line.encode('utf-8'))
    if part and size+n>160000:break
    part.append(line);size+=n;end+=1
   body=''.join(part);header=f'\n\n===== SOURCE {d["path"]} | SHA256 {d["sha256"]} | LINES {start}-{end}/{len(lines)} =====\n'
   foot=f'\n===== END SOURCE CHUNK | EOF={str(end==len(lines)).lower()} =====\n'
   item=header+body+foot;itemsize=len(item.encode('utf-8'))
   if buf and used+itemsize>200000:flush()
   volume=f'volumes/{label}-{num:03d}.md';buf.append(item);used+=itemsize
   chunks.append({'source':d['path'],'source_sha256':d['sha256'],'volume':volume,'start_line':start,'end_line':end,'total_lines':len(lines),'body_sha256':sha(body.encode('utf-8')),'body_bytes':size})
   start=end+1
 flush();return volumes,chunks

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=ROOT);ap.add_argument('--destination',type=Path);a=ap.parse_args();root=a.root.resolve();out=a.destination or root.parent/'onboarding'
 if out.exists():raise FileExistsError('Derived target already exists; choose a new target so old snapshot remains')
 (out/'volumes').mkdir(parents=True);rt=load(root);plan=rt.plan(root);enc,tokname=tokenizer()
 core=plan['documents'];corepaths={d['path'] for d in core};hashes={d['sha256'] for d in core}
 supplementary=[];inventory=[];deferred=[]
 for p in sorted(root.rglob('*')):
  if not p.is_file() or p.is_symlink():continue
  rel=p.relative_to(root).as_posix()
  if rel.startswith('.git/'):continue
  raw=p.read_bytes();r={'path':rel,'bytes':len(raw),'sha256':sha(raw),'suffix':p.suffix}
  inventory.append(r)
  if rel in corepaths:continue
  reasons=[]
  if r['sha256'] in hashes:reasons.append('byte-identical content already represented')
  if rel.startswith(('.codex/cognition/checkpoints/','.codex/history/','.codex/verification/','artifacts/','exchange/')):reasons.append('archival transaction, receipt, or separately indexed evidence')
  if p.suffix not in TEXT_EXT:reasons.append('binary or unsupported text format')
  if rel.startswith('HoTT/sources/external-audits/') and p.suffix=='.json':reasons.append('raw forensic transcript incl opaque signatures; public projections loaded separately')
  if len(raw)>600000:reasons.append('large supplementary source; read directly when relevant')
  if not reasons:
   try:raw.decode('utf-8')
   except UnicodeDecodeError:reasons.append('non-UTF8')
  if reasons:deferred.append({**r,'reason':reasons});continue
  hashes.add(r['sha256']);supplementary.append({**r,'lines':len(raw.decode('utf-8').splitlines(keepends=True))})
 # Keep legacy runtime order exactly for mandatory core. Extra material is a separate tier.
 v1,c1=make_volumes(root,out/'volumes','core',core,enc);v2,c2=make_volumes(root,out/'volumes','supplement',supplementary,enc)
 if rt.plan(root)['snapshot']!=plan['snapshot']:raise ValueError('Workspace changed while preparing fulltext')
 data={'schema':'hott.fulltext-reading-plan.v1','snapshot':plan['snapshot'],'revision':plan['revision'],'policy':plan['policy'],'core_documents':core,'supplementary_documents':supplementary,'volumes':v1+v2,'chunks':c1+c2,'tokenizer':tokname,'core_reference_tokens':sum(v['reference_tokens'] or 0 for v in v1) if enc else None,'supplement_reference_tokens':sum(v['reference_tokens'] or 0 for v in v2) if enc else None,'core_original_bytes':sum(d['bytes'] for d in core),'core_lines':sum(d['lines'] for d in core),'supplement_original_bytes':sum(d['bytes'] for d in supplementary),'model_receipt':'NOT_CERTIFIED; the recipient must actually read','no_core_content_summarized_or_omitted':True}
 dump(out/'READING_PLAN.json',data);dump(out/'ALL_WORKSPACE_FILES.json',{'files':inventory});dump(out/'DEFERRED_AND_DUPLICATE_INDEX.json',{'files':deferred,'note':'Not deleted. Not an exception to runtime mandatory core. Explicitly return to these originals when used as evidence.'})
 # Verify each exact source body can be reconstructed from the per-source line slices.
 for d in core+supplementary:
  raw=(root/d['path']).read_bytes();lines=raw.decode('utf-8').splitlines(keepends=True);pieces=[c for c in c1+c2 if c['source']==d['path']]
  recovered=''.join(''.join(lines[c['start_line']-1:c['end_line']]) for c in pieces).encode('utf-8')
  if recovered!=raw:raise ValueError('Full-text coverage mismatch')
 (out/'README.md').write_text(f'''# 完整原文加载导览（revision {plan['revision']}）

先读外层README、项目AGENTS和治理入口。本目录是派生全文，不是新真值源。核心 **{len(core)}份文件、{data['core_original_bytes']:,} UTF-8字节、{len(v1)}卷**，严格按原运行器当前计划顺序；第一份为第五闭包，第二份为三问。各卷按文件名顺序加载，不能只读标题或EOF。每段正文与对应原文件/行范围/哈希绑定，没有摘要替换。

补充 **{len(supplementary)}份不重复文档/源码、{len(v2)}卷**，包括核心之外的理论Schema原始材料、历史治理和研究脚本。其余全部文件有索引，原件未删：大量重复checkpoint、机器清单和原始取证JSON无需默认重复塞进一次窗口，但当本轮实际依赖时必须读回源文件。Archive.zip的大规模原始语料通过archive_store无损恢复，不能假定所有原语料都装入一百万tokens。

参考分词：{tokname}。核心参考tokens={data['core_reference_tokens']}，补充={data['supplement_reference_tokens']}。这不是新模型的精确分词器。留出系统输入和研究输出空间，不能因为号称百万窗口就忽略截断。容量不足必须记录未加载，不能伪造全业务认知通过。无需让当前Astra重新全文分析数学才能做这次保全。

本计划快照 `{plan['snapshot']}`。后续修改任一必读来源后须重新生成到新目录或按govern.py重新读，不使用陈旧卷冒充最新输入。可运行：`python3 -B scripts/handoff/build_onboarding.py --destination <新的派生目录>`。

RECEIVER_ACK.template.md 是接手者真实读取后要填写的记录，不是已经完成的AI验收。
''',encoding='utf-8')
 (out/'RECEIVER_ACK.template.md').write_text('''# 接手确认（模板，尚未执行）

实际AI/会话身份：
实际日期/时区：
项目根、Git HEAD、branch、dirty：
当前治理snapshot与revision：
实际进入上下文的卷/文件及行范围：
未加载/发生截断/来源缺失：
我对原目标、双向范围、ASK及最新认识的理解：
R039及应保留的正反例：
原生工具和已实际运行的验证：
仍待复核的数学与来源：
下一自主动作与理由（不是模板默认启动）：
新Session记录/当前写回状态：

只有真实完成后填写，不预填PASS。没有全文加载则如实标记，不把签字当作原证据。
''',encoding='utf-8')
 print(json.dumps({k:data[k] for k in ['revision','core_original_bytes','core_lines','core_reference_tokens','supplement_reference_tokens','tokenizer']},ensure_ascii=False));print('Core documents',len(core),'volumes',len(v1),'supplementary',len(supplementary),'volumes',len(v2))
if __name__=='__main__':main()
