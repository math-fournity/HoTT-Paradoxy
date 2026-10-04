# ZFC-H0 总闭环候选分支集成交接单

> **身份：** `CANDIDATE_NOT_CURRENT / PARALLEL_WORKTREE_HANDOFF / NO_CANONICAL_OWNER_MUTATION`。

## 1. 固定身份

| 字段 | 值 |
|---|---|
| candidate branch | `codex/zfc-h0-final-proof-closure` |
| candidate HEAD | `42e9b1d7b89814c7f92c36a369daf87e5a9adc56` |
| base | `9ffca5e045a6aac34ed2720c720e9329a914686b` (`dev`) |
| canonical target | `dev` |
| contributor worktree | `/Users/aurolafly/.codex/worktrees/bdfd/HoTT_AI_HANDOFF_20260911` |

该候选不声称已经更新 canonical `dev`。读取时应以 target 的当前 HEAD、目标工作区的 dirty/index
所有权和本候选的 precise commit 为准；不得使用 `ours/theirs` 整块覆盖 current owners。

## 2. 候选范围

本分支完成两类可审计变更：

1. **C-365 证据闭合修复：** recapture native H0 finite trace 的 `-07` primary run，补齐实际
   `UniverseHasNoLevel.agda` transitive input，固定 source manifest，生成 matrix row freeze，并使
   C-365 的选择性 version closure通过；
2. **M1–M5 来源边界：** 记录 GCTT、forcing-ticks、CCHM/CCTT 等 H0Map target 分母；记录
   M2–M5 的 policy/interface/SameFullQ 边界；完成总闭环条件审计。所有结论保持
   source-bound / formal-target-underdefined，未把它们升级为 bare-ZFC inconsistency。

还包括 `ClockedLiftDelayControl.agda` 的**未运行**候选规格。它明确标为 unrun，因为 matching
forcing-ticks compiler 的构建受本机 Xcode toolchain 条件阻断；不能将该文件作为机器证明合入。

## 3. 直接验证

candidate HEAD 上已经执行：

```text
python3 -B scripts/audit/verify_formal_proof_run.py \
  --run-dir HoTT/verification/runs/20261004-MP-ZFC-H0-TRACE-001-07

python3 -B scripts/audit/verify_proof_version_closure.py \
  --evidence-only --proof-id MP-ZFC-H0-TRACE-001

python3 -B scripts/audit/test_proof_dependency_scope.py
python3 -B scripts/audit/test_proof_evidence_links.py
python3 -B scripts/audit/verify_governance_shards.py
python3 -B scripts/audit/verify_pattern_p_tool_history_sources.py --root .
```

它们分别覆盖 C-365 run/source/index、选择性证据闭合、proof dependency/evidence-link regressions、
分片结构和模式 P 历史来源。全局 proof registry 仍有一条与本候选无关的 Coq/Docker historical
integrity gap；Docker daemon 在本次现场不可用，未将它伪称为已修复。

## 4. 集成规则

在干净 integration worktree 中，以 current `dev` 为 target：

1. 先比较 `9ffca5e0..42e9b1d7` 与当前 `dev`，提取仍成立的 formal/run/audit 资产；
2. 对 `MEMORY`、`feature-list`、`audit/README`、总 SOP 原位合并其当前事实，保留 target 上已存在的
   新工作；
3. 复跑 C-365/C-366 的选择性 verifier，并重做 total-closeout requirement audit；
4. 只有 canonical integrator 才可推进 `dev`。若 target 继续变化，重新闭合本交接单的 base/owner 状态。
