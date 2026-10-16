"""Package the current peer discussion and declared audit evidence, not a worker job."""
from pathlib import Path
import argparse,hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[2]
def main():
    a=argparse.ArgumentParser();a.add_argument('--output',required=True,type=Path);args=a.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    D='.codex/research/hott/dialogues/GEMINI-001/';R=D+'rounds/008/'
    paths=[D+'TO_GEMINI_007.md',D+'TO_GEMINI_007.txt',D+'TO_GEMINI_006.md']
    paths += [R+x for x in ['IN-007.md','USER_REQUEST.md','ASSESSMENT.md','TECHNICAL_NOTE.md','SOURCES.md']]
    paths += ['scripts/research/r028_scope_checks.py','scripts/research/r028_lean/ScopeAudit.lean',
              'scripts/research/r024_diagonal_machine.py','artifacts/r028/SCOPE_TEST_RESULTS.json',
              'artifacts/r028/SCOPE_TEST_EXECUTION.json','artifacts/r028/NATIVE_AVAILABILITY.json']
    entries={p:(ROOT/p).read_bytes() for p in paths}
    entries['README.md']=('''# GEMINI-001 / OUT-007\n\n可转发TO_GEMINI_007.md或同文txt。它回应IN-007，是同行讨论收束，不是新任务分派。\n本包含实际有限审计和未编译Lean草稿，不能称为HoTT机器证明。原生工具缺失与网络失败单列记录。\n实际独立复现可在解压根运行：python3 -B scripts/research/r028_scope_checks.py --output /tmp/r028-new-results.json\n请使用一个尚未存在的输出路径；原结果不得覆盖。\n下一封回复不是本项目继续工作的条件。本封未通过工具直接发送。\n''').encode()
    rows=[{'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()} for p,b in sorted(entries.items())]
    entries['MANIFEST.json']=(json.dumps({'files':rows,'excludes':['MANIFEST.json'],'scope':'content identity only'},ensure_ascii=False,indent=2)+'\n').encode()
    with zipfile.ZipFile(args.output,'w',zipfile.ZIP_DEFLATED) as z:
        for p,b in sorted(entries.items()):z.writestr(p,b)
    with zipfile.ZipFile(args.output) as z:
        assert z.testzip() is None
        for p,b in entries.items():assert z.read(p)==b
    report={'path':str(args.output),'sha256':hashlib.sha256(args.output.read_bytes()).hexdigest(),
       'bytes':args.output.stat().st_size,'files':len(entries),'status':'PASS_BYTE_SCOPE','sent':False}
    Path(str(args.output)+'.sha256').write_text(report['sha256']+'  '+args.output.name+'\n')
    Path(str(args.output)+'.verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
