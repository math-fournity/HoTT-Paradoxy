<!-- governance-shard:v2
logical_id: S-RES-20261004-ZFC-P-CLOSING-CORE-AUDIT
shard_id: 003
index: ../CORE_COGNITION_AUDIT.md
-->

# 来源、P-DAG与机器证据

## source-first 证据链

1. H091/H093 的 IEP 原典卡：ZFC-with-Choice基础语境、resolution、显式 no-final-step Done 改写。
2. H100/H103：独立 Terra/Max 对 R1/R2/R3 和 H099边界的来源裁决。
3. main@`894e381`：H0 的主分支发现，形式结果、项目解释和用户判定分层。
4. C-83：截断对照的内核结果、路径压平与 `noDecoding`。
5. H104：IEP与截断的结构同形审计。
6. H105：终局措辞仲裁。
7. `MP-ZFC-COMPLETION-SUBSTITUTION-PROFILE-001`：将上述冻结状态作为有限 evidence profile 机器化。

## App Server 证据边界

H100–H105均由外部实验根的 direct App Server wire支持。公开报告只保存节点身份、prompt/output SHA、模型/effort、零工具/零修改/零审批、terminal和source级判词。`session_trajectory.py`树审计确认单 session/turn；raw reason、认证和指令全文仍私有。L1/L2/L4/L5按照H100–H105总报告明确分层，未把node PASS提升为数学真理。

## 机器证明边界

`CompletionSubstitutionProfile.lean`只证明冻结 `EvidenceStatus` fixture 的逻辑分类。它不解析IEP或HoTT原典，不证明来源作者采纳某政策，也不推导现实任务的同一性。run `...-02` 退出0、stderr空、15个打印定理无额外公理；source-manifest绑定proof、claim、TaskCard与capture脚本。

## 候选分支验证增量

本续行独立冻结并核验 `codex/zfc-q-policy-formalization@ea6c338f`。它不是 canonical current
evidence：live source worktree dirty，故只使用 Git object 和 clean detached verification worktree。selected
proof closure 对 C-359–C-365 返回 `SELECTED_PACKAGES_VERSION_CLOSED`；五个 Lean-core modules 的 theorem
均无额外公理，C-361 的 Mathlib control 明示 classic axioms，C-360 的 Cubical Agda positive control exit 0、
negative control 在 `nothing != just 1` 处 exit 42。

它带来的事实不是 actual ZFC Q，而是更窄的形式边界：最小 `=`／`∈` formula theory 对未进入语言的
`originDone` 不变；强 P 与 HoTT B 的 `False` 需要显式 `PolicyScopeWitness`。这正支持现有
R1/R2/R3 收束，且阻止把 completion 名词相似误报为同一任务。完整 B0–B3 见
`audit/20261004-ZFC-ACTUAL-Q-CANDIDATE-VALIDATION-B0-B3.md`。

同日对 IEP、SEP *Supertasks* 与 Norton 原页的复核确认：三者都把 Zeno runner 的完成语义限定在其
own task 中，SEP/Norton尤其显式区分或改写“complete”。这支持 R1/R2 和 `SOURCE_TASK_CONTRACT_SPLIT`，
不支付圆环／HoTT 的 policy scope。
