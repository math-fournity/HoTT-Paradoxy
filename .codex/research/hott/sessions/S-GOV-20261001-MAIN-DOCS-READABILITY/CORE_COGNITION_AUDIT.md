<!-- governance-shard-index:v2
logical_id: CORE_COGNITION_AUDIT
mode: topical
shard_root: CORE_COGNITION_AUDIT
last_shard: CORE_COGNITION_AUDIT/002 - 扩展认知逐片回评.md
append_target: -
soft_line_target: 300
-->

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 2 个分片；缺一片即未完成，按表顺序读取；300 行只是软目标，不是上限。

# main 公共叙述文档可读性审计

- session: `S-GOV-20261001-MAIN-DOCS-READABILITY`
- tier/role: `T1-standard` / `GOVERNANCE_ALIGNMENT`
- task: 检查 curated `main` 中面向读者的叙述文档；保留近期人话改写和精确数学证据，只补确有必要的说明。
- core snapshot: `core-cognition-generation-11`, 55 KC, SHA-256 `3cd3326f4bb8578c6e4c4e9e14b1c1b6fa590f9a4c12d64f83e88eb37a5b07f8`.
- source-first: `核心认知.md` 从第 1 行读到 EOF；`扩展认知.md` index 与 11 个 shard 按表顺序读到 EOF。
- outcome: 报告读者层面的解释和未决问题已通俗化；用户原话、形式命题、运行记录、路径和编号保持准确。没有修改 core、STATE、投影、proof sources 或 run receipts；没有新增数学结论。
- touched KC: 15 `ALIGNED`; 40 `NOT_TOUCHED`; 0 `DEEPENED/CORRECTED/TENSION/DEVIATED`.
- touched essay shards: 001, 003, 005, 009, 010, 011; remaining five are explicitly `NOT_TOUCHED`.
- unresolved: original ring-task fidelity, Markov-model transfer, literature novelty, independent review, and A7's uniform-definition question remain open.
- rollback/reopen: prose can be reverted by Git; reopen if the user says the wording changes the task, evidence, attribution, or audience, or if proof/replay state changes.
- state: no STATE revision/checkpoint; release build verifies the document/proof/run closure but does not rerun kernel proofs.

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [核心认知逐项回评](<CORE_COGNITION_AUDIT/001 - 核心认知逐项回评.md>) | 对 core-generation-11 的 55 个 KC 逐条给出本次 relation、评估、证据和复审条件 | current |
| 002 | [扩展认知逐片回评](<CORE_COGNITION_AUDIT/002 - 扩展认知逐片回评.md>) | 对扩展认知 001–011 片逐片记录实际消费、未触及范围和触发条件 | current |
<!-- governance-shard-table:end -->
