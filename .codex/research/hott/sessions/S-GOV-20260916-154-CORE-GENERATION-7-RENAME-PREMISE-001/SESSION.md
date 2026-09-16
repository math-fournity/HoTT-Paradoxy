# S-GOV-20260916-154-CORE-GENERATION-7-RENAME-PREMISE-001

- 工作单元：用户 2026-09-16 三件事——（1）认识论修正进入核心认知；（2）第四件文档改名；（3）`PREMISE-001` 写入 STATE current queue 并刷新投影。
- 事件 1（已完成，commit `6ab1c68`）：用户 2026-09-16T12:14:00Z 认识论修正原文纳入核心认知 generation-6/43 → generation-7/46；新增 `KC-000044`（理论是对现实的骨架式模仿）、`KC-000045`（数学与 HoTT 必然可映射现实）、`KC-000046`（AI 缺的是用现实理解理论的动作）；43/43 旧单元 `PRESERVED_EXACT`、mapping_count=43、remainder=0；curation v7、transition gen7、`verify_core_cognition.py` PASS_WITH_SCOPE。
- 事件 2（已完成，commit `3990de8`）：`从抽象到悖论——HoTT研究的核心问题意识与思想展开`（索引 + 同名分片目录）按用户要求改名为 `扩展认知`；新增第 008 片《现实对齐：理论是现实的骨架式模仿》；19 个活当前真值文件同步引用（AGENTS/LOAD_SET/PROTOCOL/cognition_runtime `ESSAY` 常量/Skill/rulings/feature-list/合同/validators/RESUME/MEMORY/README）；`verify_governance_shards.py` PASS（456 索引、17 canonical）、`test_three_way_cognition.py` 6/6 OK。剩余旧名引用经全面检查均为不可变历史证据或用户原文逐字引文（`核心认知.md` KC-000038 载体、`扩展认知/006` 逐字引文、essay 索引内的改名说明、audit/imports 与第三方历史快照），不改动。
- 事件 3（本 checkpoint）：`A-PREMISE-001` 登记为 STATE active 记录并写入 `execution_control.next_minimal_verification`；`方向追踪`/`全景视野` 索引 marker 刷到 revision 154 并新增 `DIR-TOP-PREMISE-INVENTORY` / `OUT-TOP-PREMISE-001-REGISTRATION`；`DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` 的下一动作原位改为 PREMISE-001（R4 并行保留）；MEMORY/001 队列与 MEMORY/003 顺序日志同步；RESUME 停止点插入 S154。
- 额外修复（既有漂移，非用户要求但对 canonical 流程强制）：STATE.records 补登 S153 记录——generation-6 的 session 三件存在于磁盘但未被登记，`graph()` 要求 latest_session 必须是已注册 session 记录；登记内容显式标注 canonical checkpoint 收据缺口、不伪造 transaction/result。HEAD.tracked 重建——revision 153 写入后 essay 改名并新增分片 007/008，且 MEMORY/003、RESUME 等哈希过期，`plan()` 报 `HEAD_TRACKING_INCOMPLETE` + `UNCOMMITTED_STATE`；重建保持 revision=153/latest_session=S153 不变，仅恢复派生路由数据。
- 关于 revision 号：用户说「投影刷到 revision 153」，但 153 已被 generation-6 消耗（STATE/HEAD 均为 153、latest_session=S153），canonical checkpoint 只能取 prior+1=154。这是 forced move，在此透明说明。
- 数学状态：不变。PREMISE-001 的 P1/P2 是结构与省略分析，不是数学结论（F-011 不适用）；「某前提非现实」必须经用户 P3/P4 判定再由引擎与原生核验证。无新数学 claim。
- Git：本工作单元路径精确 stage 后本地提交；不 push、不 tag。
