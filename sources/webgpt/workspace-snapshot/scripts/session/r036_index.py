"""Append the actually saved script and evidence index."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'scripts/README.md'
text=p.read_text()
if '## R036 / R037 ·' in text:raise FileExistsError('already indexed')
p.write_text(text+'''
## R036 / R037 · 认识对齐与有限状态抽象

- `research/r036_transition_abstraction.py`：显式有限迁移图、存在关系商、环证书、相容提升、等级及链分区。不是HoTT内核。
- `tests/test_r036_transition_abstraction.py`：28项实际正反测试；输出在artifacts/r036。
- `session/r036_context.py`：继承基线、完整段落读出与实际工具存在性。收据不认证理解。
- `session/r036_align.py`、`r036_finalize_alignment.py`：当前owner原位修订，保留r036-before/r037-before及旧checkpoint。
- `session/r036_write_research.py`：完整论文、来源、逐项声明与下一步落盘。
- `session/r036_checkpoint.py`：用原治理器恢复研究；最终治理37不计作新数学轮次。
- `session/r036_verify.py`、`r036_deliver.py`：文件/路由和真实Git/ZIP/bundle恢复检查。

所有代码先落盘后调用；不把有限模型结果泛化为HoTT内核证明，全文加载政策未改。
''')
print('R036 index appended')
