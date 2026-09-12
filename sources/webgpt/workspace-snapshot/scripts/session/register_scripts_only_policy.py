#!/usr/bin/env python3
"""Record the user's scripts-first requirement without rewriting unrelated policy."""
from __future__ import annotations
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
USER = '记录到当前工作目录下面的AGENTS.md中：你以后不要写inline的代码，所有代码都应该通过写入scripts目录后进行调用。然后继续下面的工作。'
OLD = '- 今后新写的研究实验、回收/打包/验证/状态更新工具，先保存到根 `scripts/` 再运行。临时探索随后实际采用时也应落为可复用脚本；不能仅留在会话工具单元。'
NEW = '''- **禁止 inline 代码；一切新增代码必须先写入当前项目根 `scripts/`，再通过该文件路径调用。**适用于研究、试算、临时诊断、测试、数据处理、文档更新、加载、checkpoint、回收、验证和打包；不再允许“临时先执行、之后再补存”的例外。
- 不使用 `python -c`、`node -e`、解释器 stdin/heredoc 执行代码、notebook 中直接运行新代码，或在 shell 命令串中临时定义函数/循环/算法。需要几行代码也先创建命名脚本；调用只传参数，不以字符串载荷变相执行未保存代码。
- 写文件所需的文本落盘（例如 here-document 写到 `scripts/example.py`）是保存代码，不是执行；随后以 `python3 -B scripts/example.py` 等明确路径调用。普通已有命令的调用与文件读取（git、cat、sed、ls等）可以直接使用；涉及新算法/控制逻辑时写脚本。工具输出中的示例代码不自动执行。
- 新建工具优先位于 `scripts/research/`、`scripts/tests/`、`scripts/session/`、`scripts/tools/`；研究结果放 `artifacts/` 或相应Session目录，避免把输出误当脚本。历史原代码保持原路径/字节；如需调用历史 `.codex` 工具，通过已保存的 `scripts/` 包装器或使用其已回收并核对哈希的副本。
- 每次调用前确认源码已经落盘；证据保存脚本/输入哈希、实参、工作目录、时间、原始输出和退出状态。失败代码与失败记录同样保留；修订经Git追踪，不删除后伪称首次成功。'''

def main() -> None:
    p = ROOT / 'AGENTS.md'
    before = p.read_text(encoding='utf-8')
    if before.count(OLD) != 1:
        raise RuntimeError('Expected exactly one original policy clause; refusing patch')
    out = ROOT / 'artifacts/r017/policy'
    if out.exists():
        raise RuntimeError('Policy artifacts already exist')
    base = subprocess.run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false','rev-parse','HEAD'],cwd=ROOT,text=True,capture_output=True,check=True).stdout.strip()
    status = subprocess.run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false','status','--porcelain'],cwd=ROOT,text=True,capture_output=True,check=True).stdout
    if any(line[3:] == 'AGENTS.md' for line in status.splitlines()):
        raise RuntimeError('AGENTS already dirty; do not overwrite another change')
    after = before.replace(OLD, NEW, 1)
    out.mkdir(parents=True)
    (out/'AGENTS.before.md').write_bytes(p.read_bytes())
    (out/'USER_REQUEST.txt').write_text(USER+'\n',encoding='utf-8')
    p.write_text(after,encoding='utf-8')
    assert p.read_text(encoding='utf-8') == after
    assert '临时探索随后实际采用时也应落为可复用脚本' not in after
    (out/'AGENTS.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/AGENTS.md',tofile='b/AGENTS.md')),encoding='utf-8')
    result = {'status':'APPLIED','base_git':base,'workspace':str(ROOT),'path':'AGENTS.md',
              'before_sha256':hashlib.sha256(before.encode()).hexdigest(),
              'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
              'user_request':USER,'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'changes':'Replace permissive temporary-code clause with strict scripts-before-execution policy',
              'unrelated_governance_changed':False,'existing_research_changed':False}
    (out/'CHANGE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
