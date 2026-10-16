# P-DAG-ZFC-SOURCE-031/032：AC／Power Set 的 P3 原子形成与证明上下文控制

> **身份：** `P3_B_DIRECTION_GUARD_CONTROL / INPUT_CONTRACT_FAILURE_PRESERVED / SOURCE_MATCH_RETRY / NOT_A_ZFC_B_OR_MATHEMATICAL_RESULT`。

## 1. H031：采样前的输入合同失败

H031 的 [NodeCard](20261002-P-DAG-ZFC-SOURCE-031-AC-POW-P3-ATOMIC-NODECARD.md) 和 P3 prompt在 commit `b38e9afc` 冻结。其 prompt 开头写作 “You are a P-VALIDATION source mapper for P3.”，而当前 runner 的 `source-match` profile 机械要求精确子串：

```text
You are a P-VALIDATION source mapper.
```

因此 runner 在认证、thread/start、turn/start和模型采样之前拒绝输入：

```text
--prompt-file does not contain the frozen source-match profile
```

H031 的正确身份是：

```text
INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT
```

它不支持任何 AC、P3、B向、Power Set或模型能力判词。历史 NodeCard保持不改；H032只修复该精确 marker，使用新 run ID 和项目根外的新 experiment root。

## 2. H032：同源 P3 复测

H032的 [NodeCard](20261002-P-DAG-ZFC-SOURCE-032-AC-POW-P3-ATOMIC-NODECARD.md) 和
[prompt](20261002-P-DAG-ZFC-SOURCE-032-AC-POW-P3-ATOMIC-PROMPT.md) 在 commit `f735705b` 冻结。唯一功能性变更是将精确 source-match marker放在首句，随后才给 P3 任务说明。

来源仍为 `isabelle-prover/mirror-isabelle/src/ZF/AC.thy`，commit
`5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8`，SHA-256
`8f02e7ec0a2396972a1693572bc046d9906cc430b67b45a072eb1ffbd1e2e126`。它显示 `AC` 的 axiomatization、`AC_Pi_Pow`／`AC_func` 中的 `exE`、以及 `AC_func_Pow` 中的 `bexE`。

Terra/Max的公开 MatchTrace 逐状态给出：

| P3 字段 | source 支持范围 | Master 判词 |
|---|---|---|
| Draft | source没有 f 在公理／证明之前的状态 | `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED` |
| NeedBuild | AC和后继定理只陈述／证明存在式 | `FORMATION_AS_ATOMIC` |
| NeedEval | 没有scheduler、evaluation或observation rule | `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED` |
| Admitted | AC使形式存在结论可在理论中使用 | `AXIOM_ASSUMPTION_ONLY`，非construction admission |
| OperatorUse | `exE`／`bexE`在局部证明上下文引入见证 | `PROOF_CONTEXT_LOCAL_WITNESS_ONLY` |
| BuildDone | theorem证明存在与函数成员性质 | `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED`，不是built/deployed witness |

因此：

```text
P3_FORMATION_AS_ATOMIC_CONTROL
PROOF_CONTEXT_WITNESS_ONLY
CONSTRUCTION_SEMANTICS_NOT_SUPPLIED
NOT_ZFC_B_DIRECTION_LOCATED
```

这不是把“没有运行时构造”说成理论已经安全。它只说明此冻结 source 没有提供 P3 所需的构造状态、资格guard或同一任务现实对照；若未来实际 consumer来源给出这些 transition，B向仍须重新审查。

## 3. H032 运行与TrajectoryReceipt

| 项 | 观察 |
|---|---|
| actor | `gpt-5.6-terra / max`，exact `thread/start` echo |
| environment | `governance-regression-fresh`、read-only、network disabled、`approval=never`、项目根外 experiment root |
| prompt input | PASS，input SHA `9fdca0f4af33fb60ebb2059e0c3acb3d18885d9dffc99538ead651f98925ddc1` |
| terminal | 52.210 seconds；final logical SHA `f88e73021f53aa8266afa221bb21203bdce365f54b385930dfd6678005a6d014` |
| liveness | `RUNNING@1.547s → TERMINAL@52.208s`；`automatic_wall_clock_interrupt=false` |
| tools / approval | command/file-change/approval = 0/0/0；interrupt/cancel/timeout search hits = 0 |
| raw wire | 421 lines，SHA `9f25c0e7bff9c6b176e72e9ed4585a15c2777cae6e25c77808db1da1d12272ba`；terminal locator `wire.jsonl:421` |

`session_trajectory.py`的`catalog → tree → coverage → tool/approval search → terminal inspect`显示：一个completed thread/turn，415 session events、411 turn events。L1=`NOT_TESTED`、L2=`NOT_OBSERVED`、L3=`NOT_TESTED`、L4=`REQUIRES_SEMANTIC_REVIEW`、L5=`REQUIRES_ACCEPTANCE_EVIDENCE`。private bidirectional wire可用而 persisted rollout未提供；没有从终稿或summary推断不可见 reasoning。

## 4. P3 与 B向的边界

H029/H030已经显示 proof system有一条形式支付链。H032进一步确认：

```text
formal axiom / theorem / existential elimination
≠ source-backed construction lifecycle
≠ object-level f constructed
≠ real or computational task completed
```

这正保住用户的 B 向问题，而不提前回答它。要进入 B向，后继必须给同一对象的 `Draft → NeedBuild → NeedEval → BuildDone → Admitted → OperatorUse` 或相称的来源 transition，并说明现实侧对同一 I/O/Done 为什么不能完成。H032没有这些条件，不能成为B向候选。

## 5. 运行合同与SelfAuditCard

```text
H031 classification: RUNNER_OR_EVIDENCE_FAILURE (input-contract preflight; no model sample).
repair: source-match prompts must contain the runner's exact profile marker before role-specific wording.
H032 classification: ALIGNED_P3_NEGATIVE_CONTROL / EXPECTED_CALIBRATION_FAILURE.
original idea challenged: none.
P3 boundary: formal payment and local proof witness do not manufacture construction semantics.
falsifier: a source that explicitly carries pending construction state, admission guard, operator use and BuildDone
            for the same f, plus a same-task realization comparison.
next action: seek that actual consumer source; do not repeat AC proof cards as if they were it.
```
