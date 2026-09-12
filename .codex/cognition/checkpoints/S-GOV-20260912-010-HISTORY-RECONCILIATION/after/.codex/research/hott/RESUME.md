# 接续指针

## 当前可恢复入口

1. 读取根 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`。
2. 按固定前三项全文读取 `核心认知.md` → `方向追踪.md` → `全景视野.md`，再读取 `.codex/cognition/LOAD_SET.json` 指定的其余固定文件。
3. 运行 `rtk python3 scripts/audit/verify_core_cognition.py`，确认 generation-2 的 913 KC 和 generation-1 前缀迁移收据。
4. 运行 `rtk python3 scripts/audit/verify_understanding_merge.py` 和 `rtk python3 scripts/audit/verify_cross_source_reconciliation.py`，确认双目录 25/24 文件和 22,226 条 source-row register。
5. 运行 `rtk python3 scripts/audit/verify_three_way_cognition.py`，再用 `cognition_runtime.py plan/read/check` 记录三件套真实 EOF/hash 收据。
6. 按需打开 `audit/cross-source-reconciliation.json` 的具体 locator，优先处理 2,396 条 understanding claim 的句级语义裁决和历史数学主张 review。

## 当前停止点

来源覆盖登记、逐文件 merge receipt 和 core generation-2 已完成并 checkpoint；模型实际上下文、压缩后的保有、数学正确性、aistudio-docs 覆盖和 claim 的人工语义闭合仍不能由当前工具宣称完成。
