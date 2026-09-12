#!/usr/bin/env python3
"""Neutral entrypoint to the COMPLETE existing governance runtime, not a second engine.
The recipient needs no Codex integration. Explicit project-relative path map preserves historical storage.
"""
from pathlib import Path
import argparse, importlib.util, json, sys
ROOT=Path(__file__).resolve().parents[2]
def load(root):
 cfg=json.loads((root/'governance/PATHS.json').read_text())
 path=root/cfg['runtime'];spec=importlib.util.spec_from_file_location('hott_legacy_runtime',path)
 m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=ROOT)
 ap.add_argument('command',choices=['plan','read','check','checkpoint','recover','install-entry'])
 ap.add_argument('--snapshot');ap.add_argument('--path');ap.add_argument('--start-line',type=int,default=1);ap.add_argument('--max-bytes',type=int,default=10000)
 ap.add_argument('--payload',type=Path);ap.add_argument('--apply',action='store_true');ap.add_argument('--action',choices=['finish','rollback']);ap.add_argument('--confirm-owner-stopped',action='store_true')
 ap.add_argument('--directory');ap.add_argument('--output',type=Path)
 a=ap.parse_args();root=a.root.resolve();rt=load(root)
 try:
  if a.command=='install-entry':
   if not a.directory:raise ValueError('--directory required')
   from delta_tool import inside
   dest=inside(root,a.directory+'/HOTT_ENTRYPOINT.md')
   if dest.exists():raise FileExistsError(dest)
   dest.parent.mkdir(parents=True,exist_ok=True)
   dest.write_text('# HoTT 项目治理入口（转接文件，不是第二份状态）\n\n项目根：'+str(root)+'\n\n请显式完整读取项目根 AGENTS.md 与 governance/ENTRYPOINT.md，然后按治理计划全文恢复。\n唯一状态和原引擎由 governance/PATHS.json 定位；本文件不授权绕过原协议。\n不要依赖宿主自动发现本文件；需要在该 AI 的项目入口实际配置或由用户明确附给它。\n',encoding='utf-8')
   r={'status':'ENTRY_WRITTEN_NOT_HOST_AUTODISCOVERY_VERIFIED','path':str(dest),'canonical_entry':'governance/ENTRYPOINT.md'}
  elif a.command=='plan':r=rt.plan(root)
  elif a.command=='check':
   p=rt.plan(root)
   if p['snapshot']!=a.snapshot:raise ValueError('STALE_SNAPSHOT_RESTART_ALL')
   r={'status':'SNAPSHOT_UNCHANGED','snapshot':p['snapshot'],'model_cognition':'NOT_CERTIFIED'}
  elif a.command=='read':
   r=rt.read_chunk(root,a.snapshot,a.path,a.start_line,a.max_bytes);body=r.pop('text')
   print('BEGIN_COGNITION_CHUNK\n'+json.dumps(r,ensure_ascii=False)+'\nBEGIN_FULL_TEXT\n'+body+'\nEND_FULL_TEXT\nEND_COGNITION_CHUNK');return
  elif a.command=='checkpoint':
   if not a.payload:raise ValueError('--payload required')
   r=rt.checkpoint(root,a.snapshot,json.loads(a.payload.read_bytes()),apply=a.apply)
  else:r=rt.recover(root,a.action,confirm_owner_stopped=a.confirm_owner_stopped)
  text=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
  if a.output:
   a.output.parent.mkdir(parents=True,exist_ok=True)
   with a.output.open('x',encoding='utf-8') as f:f.write(text)
   print(json.dumps({'status':'RECORDED','path':str(a.output),'command':a.command,'does_not_certify_reading':True},ensure_ascii=False))
  else:print(text,end='')
 except (rt.CognitionError,OSError,ValueError,TypeError,KeyError) as e:
  print(json.dumps({'status':'BLOCKED','error':str(e)},ensure_ascii=False));raise SystemExit(2)
if __name__=='__main__':main()
