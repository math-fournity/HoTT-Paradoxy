<!-- governance-shard:v2
logical_id: CORE_COGNITION_AUDIT_S_RES_20261003_P_DAG_H043_H047_GEMINI_PROOFSEARCH_DIFFERENTIAL
shard_id: 003
index: ../CORE_COGNITION_AUDIT.md
-->

# 选择、偏航与SelfAudit

## 当前判断

用户指定的 Gemini 草稿本身是合理的来源入口，因为它明确把“计算过程”“公式编码”“ZFC”和“UA”放在同一叙述中。实际三刀结果则把它们拆开：external proof search 不是 native task；formula/code 不是 re-entry；loop/halt 不是 admission lifecycle。因此，草稿可用作反幻觉和层次隔离的控制，不可用作 ZFC 候选。

## 运行与理念自审

| 项目 | 实际状态 | 归类 |
|---|---|---|
| 从明显位置而非遍历 | 用户指定的历史声称，冻结 1 张来源卡 | `ALIGNED` |
| 代理公开说明为什么定位／拒绝 | H043/46/47 各有 E0–E7 | `ALIGNED_WITH_SCOPE` |
| P1/P2/P3 的职责分开 | external consumer / re-entry / admission 分别测 | `ALIGNED_DIFFERENTIAL` |
| H044/H045 | exact marker 在采样前 fail | `RUNNER_INPUT_CONTRACT_FAILURE`，非理论失败 |
| 新刀具 | 无独立职责或正负控制 | `NO_P4_CREATED` |

## 后继触发

| 触发 | 可做动作 | 禁止事项 |
|---|---|---|
| 同层 actual consumer source | 冻结 T/u/F/C/I/O/Done card，再跑 P1 | 不将外部 proof search 提升。 |
| 内部 pending/admission source | P3 状态 transition card | 不把 loop 当 admission。 |
| internal evaluation-to-same-object source | P2 re-entry card | 不把 formula code 当 fixed point。 |
| 用户选独立承诺 | 新 blind profile | 不从 H043–47 偷换结论。 |

```text
H043–H047 classification:
  source card = HISTORICAL_AI_DRAFT_BOUNDARY_CONTROL
  H044/H045 = INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT
  H046/H047 = ALIGNED_DIFFERENTIAL_CONTROL_WITH_SCOPE
original idea challenged = none
new tool = none
```
