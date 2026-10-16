# CE-MAP v1：HoTT 非现实性悖论机器统观八轴映射

状态：`CE_MAP_V1_COMPLETE_WITH_SCOPE`  
输入快照：`85824aa1d4053e683910c063282162a615331a7ca3cc4b2c1fd5c0962553e3a4`  
冻结截止：STATE revision 149 / C-243 / machine import `6dafaaba2cfe49032b8219f9c24e42c01bbdb9d124ff9e2ef918803f26785e00`

## 这份完成状态表示什么

本次把 478 个具名输入逐一登记到八轴张量。每个轴都有受控值，无法从当前证据确定的值明确写成 `UNKNOWN`，与数学对象无关的记录明确写成 `NOT_APPLICABLE`。输入 remainder 为 0；`UNCLASSIFIED.json` 保留 69 个仍含未知轴的 item。

`CE_MAP_V1_COMPLETE_WITH_SCOPE` 只表示 revision 149 的具名分母已被完整登记。它不表示开放世界已经穷尽，也不表示 HoTT 中已经找到新的矛盾或最终现实相对悖论。

## 输入分母

| 命名空间 | 数量 |
|---|---:|
| `machine_case` | 13 |
| `machine_evaluation` | 15 |
| `machine_review` | 18 |
| `machine_run` | 48 |
| `machine_task` | 14 |
| `proof_claim` | 186 |
| `proof_package` | 41 |
| `state_record` | 143 |

## internalisation 归约结果

| class | 成员数 | 归约强度 | 代表 |
|---|---:|---|---|
| `CE-CLASS-UNQUALIFIED-INTERNALISATION-001` | 6 | `PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE` | proof_claim:C-234 |
| `CE-CLASS-QUALIFIED-INTERNALISATION-DEFENSE-001` | 6 | `RELATED_DEFENSES_NOT_A_SINGLE_EQUIVALENCE` | proof_claim:C-237 |

`CE-CLASS-UNQUALIFIED-INTERNALISATION-001` 把 C-228–C-240 中“取消输入资格后把能力提升到 local/open/context-uniform 使用”的共同机制只计作一个搜索家族。它没有把三个论文结果说成同一个定理：consumer、观察结果、完成性质和 framework 没有保持，因此其状态是 pattern reduction，而不是完整任务保真的双向归约。

crisp/global 限制、identity-R 消融、degenerate fibrancy + transport 与 empty-context extension 被登记为一个 defense pattern。它们都通过显式支付保住来源中的真实任务，但支付内容不同，仍须逐 consumer 检查。

## 未决轴

| 轴 | 含 `UNKNOWN` 的 item 数 |
|---|---:|
| `TheoryConstruct` | 64 |
| `AbstractionChange` | 64 |
| `RealityOrTask` | 64 |
| `ConsumerOrContext` | 64 |
| `ObservationLayer` | 64 |
| `CompletionProperty` | 64 |
| `Oracle` | 69 |
| `FrameworkOrModel` | 64 |

前 25 项如下；全量见 `UNCLASSIFIED.json`：

- `machine_case:MS-TASK-L3-INTERVAL-COMPLETION-001`：Oracle
- `machine_review:RV-MS-TASK-L3-INTERVAL-COMPLETION-001-r1-20260913-SEARCH-L3-SYMBOLIC-001-WV-0001-e5389254`：Oracle
- `machine_run:20260913-M4-LITE-L3-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `machine_run:20260913-M4-LITE-L3-REPLAY-V2`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `machine_run:20260913-SEARCH-L3-SYMBOLIC-001`：Oracle
- `machine_run:20260913-VERIFY-L3-SYMBOLIC-001`：Oracle
- `machine_task:MS-TASK-L3-INTERVAL-COMPLETION-001`：Oracle
- `state_record:A-A-DIRECTION-CANDIDATES-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-AISTUDIO-COVERAGE-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-ASTRA-TRAJECTORY-AUDIT-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-AUDIT-REPORT-TONGGUAN-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-AUTONOMOUS-ROUND2-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-AUTONOMOUS-ROUND3-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-C11-REVIEW-ABSORPTION-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-C11-REVIEW-IMPORT-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-C5-PARADOX-DISTANCE-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-COARSE-CONSUMER-SCAN-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-COQ-MM2-SOURCE-QUALIFICATION-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-E6-TARGETED-SEARCH-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-ERCF3-PREREQUISITE-ASSESSMENT-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-ERCF3-T2-ENCODING-ROUTE-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-ERCF3-T3-ARITH-TAGS-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-ERCF3-T3-BIT-CODING-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-ERCF3-T3-C168-COUNTERCHECK-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel
- `state_record:A-ERCF3-T3-CODING-IMAGE-001`：TheoryConstruct, AbstractionChange, RealityOrTask, ConsumerOrContext, ObservationLayer, CompletionProperty, Oracle, FrameworkOrModel

## 下一机器切片

选择 `R3_R4_GODEL_RETURN_001`，对应 `state_record:A-G-HOTT-SYNTAX-001`。The newly reduced internalisation family has published qualified defenses.  The exact HoTT syntax/representability route remains outside that class, is explicitly required by goal.md, and its CompletionProperty remains FULL_R4_OPEN for a new machine slice.

Oracle、physical time/时空连续性、ambient R2 与现实桥梁仍保留为并行返回口，不被 internalisation class 吞掉。

## 复核入口

```bash
python3 -B scripts/audit/build_ce_map.py validate
python3 -B scripts/audit/build_ce_map.py query --id proof_claim:C-234
python3 -B scripts/audit/build_ce_map.py list-unclassified
python3 -B scripts/audit/test_ce_map.py
```
