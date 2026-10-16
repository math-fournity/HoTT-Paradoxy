# S-GOV-20260930-COPUS-CORE-GENERATION-9-REGISTRATION

核心认知第 9 代入核，扩展认知修订，方向追踪与全景视野登记芝诺线与罗素线、对 GLM 的审计、归因修正；STATE 登记。

- host: Claude Code（claude.ai/code 云端会话，分支 claude/charming-pasteur-mvzlio）
- model: 不写入仓库产物（会话策略）；模型身份只在会话聊天中查询
- tier: T3
- role: 用户授权的入核与登记；不是研究生成，不是独立审计
- load_receipt: 读取 `.codex/tools/cognition_runtime.py` 全文、PROTOCOL §4A/§5/§7、s154 准备脚本、`核心认知.md` 第 9 代全文（KC-000049–KC-000051 与 48 条旧单元逐字保留已由生成器校验）、方向追踪与全景视野的索引及相关分片、扩展认知 003／005／009 与索引、MEMORY 三片、RESUME 首部；plan snapshot 见 RUNS.json
- authorization: 用户 2026-09-27：入核和登记我现在就授权你，立即完成所有剩余的你可以完成的工作
- parent: 不改变 Goal7 / MO3-COVERAGE-C；本会话不是 integrator 的研究单元

做了什么：

1. 三个来源文件入 `sources/prompts/`（逐字，带哈希；时间为上界，来源文件内写明）；curation v9；生成器新增 `Claude`、`GLM` 平台；`scripts/audit/build_core_cognition.py --write` 生成第 9 代、manifest 与 transition；`verify_core_cognition.py` PASS_WITH_SCOPE。
2. 扩展认知：003／005／009 原位修订（归因修正），新增 010；扩展认知全部 51 个原文块与核心认知逐字一致（准备脚本在写入前逐块比对）。
3. 方向追踪新增 3 行，全景视野新增 4 行并增补“当前未完成”第 18–20 项；MEMORY、RESUME 同步；STATE 登记 1 个核心代记录、2 个候选、1 个跟进项与本 session。
4. 不做的事（及原因）：不改 `.codex/cognition/CORE_COGNITION.schema.json` 与 `.codex/skills/hott-paradox-search-sop/SKILL.md`（框架改动须过用户本机的全局自维护 Gate，见 `G-COPUS-CORE-GEN9-FOLLOWUPS-001`）；不改 KC-000005／020 原话；不推送标签；不处理 `verify_projection_freshness.py` 的既有失败。

|element_usage|本次用途与边界|
|---|---|
|核心认知与原版最高指示|KC-000047–051 与第 9 代全文；归因是正题；不把判定写成定理|
|canonical runtime 与 writer|plan/prepare/checkpoint；单文件兼容审计；只认 canonical result|
|build_core_cognition 与 verify_core_cognition|重建与校验第 9 代；48 旧单元逐字保留|
|projection_edit|索引与全部分片同 payload 原位修改|
|verify_three_way_cognition 与 verify_governance_shards|结构校验；不证明语义|

验证命令与结果见 RUNS.json。无新数学主张；本 session 登记的形式结果属于 Cloud-Opus 审计会话的 46 个运行，它们各自的收据不因本 checkpoint 改变。未 push（标签需用户在本机推送）。
