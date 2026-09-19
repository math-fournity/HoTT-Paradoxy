<!-- governance-shard-index:v2
logical_id: MEMORY
mode: sequential
shard_root: MEMORY
last_shard: MEMORY/003 - 当前验证状态与顺序日志.md
append_target: MEMORY/003 - 当前验证状态与顺序日志.md
soft_line_target: 300
-->

# 当前工作记忆 — 索引

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 3 个分片；缺一片即未完成，按表顺序读取；300 行只是软目标，不是上限。
> 合同：`docs/quality/长治理文档分片与索引合同.md`。
> 写入规则：当前队列/证据上限/恢复入口在原位片修改；新的逐会话记录追加到 `MEMORY/003 - 当前验证状态与顺序日志.md` 末尾。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [当前执行队列](<MEMORY/001 - 当前执行队列.md>) | 当前执行队列（2026-09-14）；原位更新的当前队列 owner | current |
| 002 | [当前证据上限与恢复入口](<MEMORY/002 - 当前证据上限与恢复入口.md>) | 当前证据上限 + 恢复入口；原位更新的当前边界 owner | current |
| 003 | [当前验证状态与顺序日志](<MEMORY/003 - 当前验证状态与顺序日志.md>) | 当前已验证状态（S023–S141 逐会话记录，append_target） | current |
<!-- governance-shard-table:end -->
