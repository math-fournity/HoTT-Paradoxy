#!/usr/bin/env python3
"""Recover *available* historical source bytes into scripts/, without running them.
Nested ZIPs are scanned, duplicate bytes shared, all provenance edges retained.
No absent conversation program is reconstructed and labelled original.
"""
from pathlib import Path, PurePosixPath
from io import BytesIO
import argparse, collections, hashlib, json, stat, unicodedata, zipfile
EXTS={'.py','.sh','.bash','.zsh','.js','.mjs','.cjs','.ts','.tsx','.lean','.agda','.v','.r','.jl','.rb','.pl','.lua','.hs','.c','.h','.cpp','.rs','.go'}
MAX_NESTING=6
MAX_MEMBER=128*1024*1024

def digest(b):return hashlib.sha256(b).hexdigest()
def decoded(info):
    n=info.filename
    if not info.flag_bits & 0x800:
        try:n=n.encode('cp437').decode('utf-8')
        except UnicodeError:pass
    return unicodedata.normalize('NFC',n)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input-dir',type=Path,required=True);ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();root=a.root.resolve()
    target=root/'scripts/recovered';target.mkdir(parents=True,exist_ok=True)
    sources=[];occ=[];payload={};issues=[];excluded=collections.Counter();nested_count=0
    def save(data,origin,member,raw_member):
        h=digest(data);ext=Path(member).suffix.lower()
        key=(h,ext)
        if key not in payload:
            name=Path(member).name
            p=target/h[:20]/name;p.parent.mkdir(parents=True,exist_ok=True)
            if p.exists() and p.read_bytes()!=data:raise ValueError('collision')
            if not p.exists():p.write_bytes(data)
            payload[key]={'path':p.relative_to(root).as_posix(),'sha256':h,'bytes':len(data),'extension':ext}
        occ.append({'source':origin,'member':member,'raw_member':raw_member,'sha256':h,'stored_path':payload[key]['path']})
    def scan_zip(z,origin,depth,chain):
        nonlocal nested_count
        for i in z.infolist():
            n=decoded(i);p=PurePosixPath(n)
            if i.is_dir():continue
            if n.startswith('__MACOSX/') or p.name.startswith('._') or p.name=='.DS_Store':excluded['MacOS metadata']+=1;continue
            if p.is_absolute() or '..' in p.parts or stat.S_ISLNK(i.external_attr>>16):issues.append({'source':origin,'member':n,'reason':'unsafe path/symlink excluded'});continue
            ext=p.suffix.lower()
            if ext not in EXTS and ext!='.zip':continue
            if i.file_size>MAX_MEMBER:issues.append({'source':origin,'member':n,'reason':'member byte bound exceeded'});continue
            try:data=z.read(i)
            except Exception as e:issues.append({'source':origin,'member':n,'reason':str(e)});continue
            if ext in EXTS:save(data,origin,n,i.filename)
            else:
                h=digest(data)
                if h in chain or depth>=MAX_NESTING:issues.append({'source':origin,'member':n,'reason':'archive recursion bound'});continue
                try:
                    with zipfile.ZipFile(BytesIO(data)) as child:
                        nested_count+=1;scan_zip(child,origin+'!/'+n,depth+1,chain|{h})
                except zipfile.BadZipFile:issues.append({'source':origin,'member':n,'reason':'invalid nested archive'})
    archives=sorted(a.input_dir.glob('*.zip'))
    for p in archives:
        data=p.read_bytes();h=digest(data);sources.append({'path':str(p),'bytes':len(data),'sha256':h})
        with zipfile.ZipFile(BytesIO(data)) as z:scan_zip(z,p.name,0,{h})
    # Uploaded standalone source copies, excluding this new workdir and temporary build directory.
    for p in a.input_dir.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in EXTS:continue
        if root in p.parents or 'hott_rev16_build_tools' in p.parts or '.git' in p.parts:continue
        save(p.read_bytes(),'runtime-upload',p.relative_to(a.input_dir).as_posix(),p.relative_to(a.input_dir).as_posix())
    manifest={'schema_version':'hott-code-recovery/v1','scope':'All currently supplied top-level ZIPs, recursively nested ZIP source files, and mounted standalone source files; bytecode and unsaved conversation code excluded','input_archives':sources,'nested_archives_scanned':nested_count,'unique_payloads':list(payload.values()),'source_occurrences':occ,'excluded':dict(excluded),'issues':issues,'code_executed':False,'missing_historical_code':'Original R001 experiment files absent from current supplied inputs; not recreated as originals.'}
    (root/'scripts/RECOVERY_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    by_round=[]
    for row in occ:
        member=row['member']
        if row['source']=='HoTT_quotient_descent_checkpoint_rev15.zip' and member.startswith('.codex/research/hott/sessions/'):
            if member.endswith('.py'):by_round.append(row)
    content='# scripts：研究代码与操作工具\n\n本目录收回当前附件中可取得的脚本/形式化源码，并保存本轮全部可复现操作代码。原路径未删除、原字节未改；回收副本默认仅归档，不自动执行。\n\n## 可运行的本轮工具\n\n- `tools/restore_checkpoint.py`：从明确检查点安全恢复新目录。\n- `tools/recover_code.py`：扫描附件/嵌套包，按内容哈希去重，保留每个来源路径。\n- `session/run_logged.py`：保存实际命令、输出、返回码与时间。\n- `session/establish_git.sh`：只创建新的本地Git基线，不设置remote/push。\n\n## 已恢复的直接历史实验\n\n| 原Session路径 | scripts回收路径 | SHA-256 |\n|---|---|---|\n'
    for r in by_round:content+=f"| `{r['member']}` | `{r['stored_path']}` | `{r['sha256']}` |\n"
    content+=f'\n## 回收边界\n\n扫描 {len(archives)} 个顶层ZIP、{nested_count} 个嵌套ZIP及挂载源码，登记 {len(occ)} 次源码出现，保存 {len(payload)} 份不同内容/语言扩展的副本。逐项路径、来源、哈希见 `RECOVERY_MANIFEST.json`。\n\n没有从聊天摘要伪造缺失脚本。原始R001代码仍不能确认完整恢复；代码片段/伪代码保留在原Markdown/会话里，不自动改装成已运行脚本。此前临时命令若未作为文件或日志进入附件，不能声称已找回。\n\n历史所有恢复代码未经逐份语义/安全审查，不要批量运行。具体复现前先读源码、确认依赖与写入目标。\n'
    (root/'scripts/README.md').write_text(content)
    print(json.dumps({'top_level_archives':len(sources),'nested_archives':nested_count,'source_occurrences':len(occ),'distinct_code_files':len(payload),'distinct_code_bytes':sum(x['bytes'] for x in payload.values()),'issues':issues,'direct_experiments':len(by_round)},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
