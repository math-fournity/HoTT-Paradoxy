# 接续指针

## 当前可恢复入口

1. 读取根 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`。
2. 按固定前三项全文读取 `核心认知.md` → `方向追踪.md` → `全景视野.md`，再读取 `.codex/cognition/LOAD_SET.json` 指定的其余固定文件。
3. 执行 `rtk python3 scripts/audit/verify_core_cognition.py`，确认 core generation-1 未被改写。
4. 执行 `rtk python3 scripts/audit/verify_three_way_cognition.py`，确认三件套顺序、revision 和方向↔成果引用闭合。
5. 继续生成四类 historical ledger；完成后再修订 `理解章节/` 的 owner 和冲突表。

## 当前停止点

当前已由 session 003/004 完成 repo 初始化、交接治理和 runtime checkpoint；本轮 session 005 增加三件套初始投影和治理框架比较，不是新的 HoTT 数学研究轮次。没有完成四类 ledger、方向/成果全量语义映射、理解章节冲突复核和 fresh governance 验证前，不应写“全部历史已审计”或“博士论文级交接已完成”。
