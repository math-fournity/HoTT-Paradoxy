# CE-MAP-001：机器统观八轴映射与同型类归约

状态：`COMPLETE_WITH_SCOPE / CE_MAP_V1_COMPLETE_WITH_SCOPE`  
父目标：`A-HOTT-MACHINE-OVERVIEW-GOAL-002`  
输入截止点：C-243 / STATE revision 149 / machine import `6dafaaba2cfe49032b8219f9c24e42c01bbdb9d124ff9e2ef918803f26785e00`  
证据语义：本文件保存 TaskSpec 与完成判据；机器完成收据在 `audit/ce-map/RECEIPT.json`，不构成开放世界 coverage certificate 或数学结论。

## 1. 目标

把当前 main 中全部具名机器 package、machine-overview cases/evaluations、active/historical research candidates 与已资格化文献 consumer 映射到：

```text
TheoryConstruct
× AbstractionChange
× RealityOrTask
× ConsumerOrContext
× ObservationLayer
× CompletionProperty
× Oracle
× FrameworkOrModel
```

映射必须回答每项“属于哪个 cell、为何、有什么证据、哪些轴未知、能否和其它项保真归约”。它不以关键词命中代替语义登记，也不把没有映射的输入删除。

## 2. 冻结输入分母

第一版从下列 machine-readable/current owners 构造输入清单：

- `HoTT/verification/PROOF_VERSION_CLOSURE.json`：17 个冻结 package、1 个既有 scoped external replay、24 个 later package / 95 个 later claims；
- `HoTT/CLAIM_EVIDENCE_MATRIX.md`：proof/claim 行与禁止外推；
- `.codex/research/hott/STATE.json`：candidate、formal result、literature、consumer 与 lifecycle/evidence；
- main 中已导入的 machine-overview case/evaluation/run manifests；
- `LIT-DENOMINATOR-001`、`LIT-CLASSICS-001`、`LIT-HOTT-COMPUTABILITY-001` 的 current logical documents；
- `全景视野.md` 的 current outcome rows，只作路由与对账，不替代底层 evidence。

任何输入源有重复 ID、未知 schema、stale hash 或未分类 remainder 时，输出必须显式保留并使相应 completeness claim 降级。

## 3. 输出与机器合同

计划实现一个标准库 manager `scripts/audit/build_ce_map.py`，产生：

- `audit/ce-map/CE-MAP.json`：canonical mapping、轴 vocab、provenance、source hashes、class/reduction、unknowns；
- `audit/ce-map/UNCLASSIFIED.json`：所有缺轴/未识别/冲突项，remainder 不能被过滤；
- `audit/ce-map/REPORT.md`：人类可读投影；
- `audit/ce-map/RECEIPT.json`：输入/输出计数、hash、deterministic round-trip 与 coverage scope。

manager 必须支持 `build --write`、`validate`、`query --id`、`list-unclassified`；默认只读，确定性序列化，写入前检查 source snapshot，不能从输出反向改写数学判词。

## 4. 首批新增 cell 与归约类

本轮 C-227–C-243 强制新增：

- `global-capability → local-capability`；
- `fiberwise-fibrant → familywise-fibrant`；
- `external-pointwise → context-uniform-internal`；
- `regular-fibrancy ↔ degenerate-fibrancy + transport`；
- `crisp/global modal restriction`；
- `pointwise-fibrant input restriction`。

2LTT replacement→UIP、LOPS classifier→interval collapse、LOPS internal right-adjoint no-go、ITT regular replacement→False 若满足同一 preservation contract，应归为一个 `UNQUALIFIED_INTERNALISATION` class，而不是重复计作多个独立悖论。归约必须保持 consumer、input domain、context dependence、observation 和 completion；否则只登记 related，不宣称 class coverage。

## 5. 完备性与停止条件

第一版只有在以下条件同时满足时才可称 `CE_MAP_V1_COMPLETE_WITH_SCOPE`：

1. 每个冻结输入 ID 恰有一个 canonical item，input remainder=0；
2. 每项八轴均有值或显式 `UNKNOWN/NOT_APPLICABLE`，不允许空值；
3. 每个 class 有代表、成员、preservation/anti-preservation 字段与证据；
4. `UNCLASSIFIED` 全量保留，报告数量与 JSON 对账；
5. 运行两次 byte-identical，打乱输入顺序后 canonical output 相同；
6. 删除一个已知 input 的负控制使 validator fail；
7. 当前 C-227–C-243 internalisation 家族能被归约且不会吞掉 Gödel/R3/R4、时间、Oracle、现实任务或其它未知轴。

完成 CE-MAP v1 只证明具名输入在冻结 taxonomy 中被登记。它不证明开放世界穷尽、不证明 HoTT 悖论存在，也不允许完成根 Goal。下一 successor 必须从 `UNCLASSIFIED`、未覆盖 cell、holdout 或独立 R3/R4/现实返回口中选择。

## 6. 实现结果（2026-09-15）

manager 与资产已落入 main：

- `scripts/audit/import_machine_overview_ce_map.py` 将外部 dirty worktree 中 169 份具名实物只读冻结到 `audit/imports/machine-overview-ce-map-20260915/`：14 tasks、13 latest cases、15 evaluations、48 runs、18 correspondence reviews；双遍哈希一致，来源 branch/HEAD/dirty 边界均保留；
- `scripts/audit/build_ce_map.py` 实现 `build --write`、`validate`、`query --id`、`list-unclassified`；`audit/ce-map/README.md` 标识四个输出为 machine-managed canonical；
- `CE-MAP.json` 登记 478 个 canonical item：41 proof packages、186 proof claims、143 non-session STATE records，以及 108 个 machine-overview task/case/evaluation/run/review；input remainder=0、duplicate=0、axis-cell remainder=0；
- `UNCLASSIFIED.json` 保留 69 个含显式 `UNKNOWN` 的 item；`NOT_APPLICABLE` 只用于与八轴数学语义无关的治理或覆盖记录；
- `CE-CLASS-UNQUALIFIED-INTERNALISATION-001` 把 C-228/C-229/C-230、C-234/C-235、C-240 归为一个机制 pattern。其 consumer、observation、completion 和 framework 不保持，因此明确标作 `PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE`；
- `CE-CLASS-QUALIFIED-INTERNALISATION-DEFENSE-001` 汇集 identity-R 消融、crisp/global、degenerate+transport 与 empty-context 限制；它是 defense pattern，不冒充单一等价定理；
- 正向/逆序输入、同进程重复和独立进程两次重建均逐字节一致；删除 C-234 或删除一个轴的负控制都使 validator fail；测试 7/7。

验收判词：

```text
CE_MAP_V1_COMPLETE_WITH_SCOPE
/ NAMED_INPUT_REMAINDER_0
/ EXPLICIT_UNKNOWN_REMAINDER_69
/ INTERNALISATION_PATTERN_REDUCED_WITH_ANTI_PRESERVATION
/ OPEN_WORLD_COMPLETENESS_NOT_CLAIMED
/ ROOT_GOAL_NOT_COMPLETE
```

第一 successor 选择 `R3-R4-GODEL-RETURN-001`：已发表 internalisation no-go 具有可执行防线，而 exact HoTT syntax 的 proof predicate、representability、算术解释、fixed point 与 independent sentence 仍未闭合，且用户 Goal 明确要求寻找 HoTT 中的 Gödel 不完备性。Oracle、physical time、ambient R2 与现实任务保留为并行返回口。
