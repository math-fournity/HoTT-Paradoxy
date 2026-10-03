# P-FORGE：校准收敛、来源覆盖与 Power Set station 调整审计

> **身份：** `PROJECT_METHOD_ADJUSTMENT / PRE_RESTART_PREPARATION / NOT_A_THEORY_VERDICT`。

## 1. 触发与裁决范围

研究发起人要求根据当前运行轨迹的独立评价作必要调整，并表示随后会以原来的
`P-FORGE-SOP`恢复。评价中有三项可由当前证据支持的风险：

1. 已知正控制、盲态位置选择、source-surviving Q 和三刀会合被混写时，P 会被误称为“已经写对”；
2. proof assistant / proof-package source 可能被误当成模型语义或实际数学 consumer 的来源分母；
3. Round 内停止重复 guard 不等于有理由无限停留或自动离开 Power Set。

本次调整不接受“既有 HoTT 工作已经机器证明理论矛盾”或“ZFC Q 已被定位”这种超出当前 owner 的判断。
当前可支持的边界保持：`ZFC_Q_LOCATED=NO`，`CAL-3/CAL-4=NOT_REACHED`，没有新的数学 claim。

## 2. 采取的最小修订

| 风险 | 修订 | 为什么是最小修订 |
|---|---|---|
| fixture 成功被误作新发现 | 新增 `PCalibrationConvergenceCard` 与 CAL-0–4。 | 不改变 P1/P2/P3 的职责，只给发现—来源—会合不同证据身份。 |
| proof 层越界成 semantic/practice 层 | 新增 L-A–L-E `SourceLayerCoverageMatrix`；H075明确归L-B。 | 只要求声明来源层和缺口，不虚构一套语义或实践来源。 |
| Round stop 变成隐形换站或无限停留 | 区分`ROUND_STOP_REPEATED_GUARDS`和`STATION_EXIT_REVIEW_PENDING`，冻结S1–S5。 | 仍以原`P-FORGE-SOP`和用户的明显位置原则工作，不自动产生新的理论靶。 |

## 3. H074/H075 是这次修订的反控制

H074 的 deidentified discovery 选中`ClEx(P,a)`与 existential-reflection proof task；H075以固定
`Reflection.thy` source 得到 source theorem Done、guarded global/local relation 与 no P3 lifecycle。
因此该链只能记为`CAL-2_CONTROL_ONLY / L-B / SOURCE_PACKET_DIRECT_PAYMENT`。它正好反驳两种错误提升：

- 不能把盲态选到一个不同 interface 当作 `CAL-3`；
- 不能因为 source 讨论 `Mset`／reflection 而把 L-B 记成 L-C。

详见 [H074/H075 审计](20261003-P-DAG-H074-H075-REFLECTION-STAGE-Terra-Max.md)。

## 4. C01–C10 影响扫描

| ID | 处置 | 事实 |
|---|---|---|
| C01 用户需求／裁定 | `UPDATE` | F-042与新增ruling记录“重启前需分开校准、来源层与station”。 |
| C02 P 方法合同 | `UPDATE` | 013、P-FORGE SOP 001和三刀004新增CAL／layer／station责任。 |
| C03 P-DAG Skill／NodeCard | `UPDATE` | TaskCard/NodeCard以及Skill 1.9.0要求冻结`SourceLayerTarget`、CAL和station impact。 |
| C04 根 AGENTS／TASK_ROUTING | `NO_CHANGE` | 任务仍是既有P-FORGE范围；没有扩展 worker、权限或角色。 |
| C05 current cognition入口 | `UPDATE` | Feature、rulings、MEMORY 001和audit index给出当前恢复动作；顺序日志003保留给已有并行写入者。 |
| C06 验证／证据 | `UPDATE` | H074/H075的source hash、preflight、trajectory、JSON和结构检查进入本单元。 |
| C07 runtime config／权限 | `NO_CHANGE` | 既有隔离的 Terra/Max read-only App Server runs已终态；本次未改配置。 |
| C08 shared runner／认证 | `NO_CHANGE` | 本次只审计既有运行，没有修改runner或认证路径。 |
| C09 Git谱系 | `UPDATE` | 这组限定方法与来源收据以精确路径提交；不tag、不push。 |
| C10 audit／未知项 | `UPDATE` | 新增此审计、H074/H075报告及session；L-C/L-D/L-E和S3保持公开未决。 |

## 5. 当前重启合同

下次 `/goal`仍可完全使用原句：

```text
按照SOP=`P-FORGE-SOP`,继续推进，直至无法推进。
```

`P-FORGE-SOP`现会要求下一张 ForgeIntent 明确它的校准目标、来源层、Round ingress和station影响。
若没有其中任一增量，就停止而不制造新节点。当前 pause 不因本报告被解除；station switch 也需要研究发起人
在S1–S5齐备后作出选择。
