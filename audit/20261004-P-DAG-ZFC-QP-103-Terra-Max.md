# P-DAG H103：SEP 的窄卡 completion-promotion 分类与来源完整性纠正

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / M6_SOURCE_CARD_CONTROL / SOURCE_CARD_COMPLETENESS_FAILURE_REPAIRED / NOT_AN_ACTUAL_SEP_P_INSTANCE / NOT_A_ZFC_VERDICT`。

## 收据

`gpt-5.6-terra / max`、`source-match`、零工具／文件改动／审批；run `H103-SEP-ACTUAL-P-COMPLETION-PROMOTION-20261004` 正常结束。private direct wire 的 L1 冻结输入完整匹配，L2 无工具、L3 未测、L4 Master scoped review、L5 scoped behavior PASS。

## 窄卡确实表达了什么

| P 字段 | SEP §1.1 冻结事实 |
|---|---|
| F | 几何级数在标准实数拓扑下收敛到 1。 |
| D | Achilles 完成每一个 supertask step。 |
| promotionClaim | SEP 明说“从这一视角，Achilles 实际在极限中完成全部步骤”。 |
| verified bridge | 冻结卡未提供 theorem 或逐点 task-preserving proof。 |
| final-action control | SEP 明说 Dichotomy 没有 final action。 |

**worker 的窄卡判词：** 冻结输入中的 F、`Done_everyStep`、promotion 与
`notSupplied` 标签满足该输入自行给定的 P-candidate 形状。这个结果真实地
说明 Terra/Max 按冻结卡完成了 E0--E7 分类；它不等价于完整 SEP 来源没有
payment。

## H083 触发的 Master 纠正

H083 已用同一 SEP §1.1 的更完整来源卡核过关键相邻句：SEP 不只写出
“完成全部步骤”，还明确区分 `Done_finalAction` 与 `Done_everyStep`、否定前者、
肯定后者，并保留“标准拓扑是否合适”的问题。H083 因而已给出
`SOURCE_DONE_DISTINCTION_PAYMENT / SOURCE_TASK_CONTRACT_SPLIT`。

H103 的冻结卡虽然提到该区分，却把“没有一条形式定理”误作“没有来源层面的
payment”。来源可以通过明示自己的 Done 合同支付其限定结论，而不需要把它写成
Lean 定理。故本报告的可用 Master 判词必须改为：

```text
H103_FROZEN_CARD_SHAPE_VALID
SOURCE_CARD_COMPLETENESS_FAILURE_REPAIRED
SEP_FULL_SOURCE = SOURCE_TASK_CONTRACT_SPLIT_CONTROL
NOT_AN_UNPAID_DONE_ORIGIN_LIFT
```

这不是撤销 H103 的运行收据，也不是说 SEP 没有 completion claim；它只撤销把
该运行升级为“SEP 已提供实际未验证 P”的推断。`D_everyStep` 不是用户强原 Done、
final-action completion、圆环复原或一般运动 Done；H103 不证明标准极限无效、
实际 ZFC 缺 Q 或 P→HoTT-B provenance。

## 可推翻条件

若研究发起人将 origin Done 明确定义为 `Done_everyStep`，才可另行审 SEP 的
限定合同是否保留同一任务；在此之前，H103 仅保留为窄卡/来源完整性反控制。
