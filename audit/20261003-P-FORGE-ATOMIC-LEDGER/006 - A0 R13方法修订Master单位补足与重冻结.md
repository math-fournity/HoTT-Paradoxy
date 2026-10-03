<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_LEDGER
shard_id: 006
index: ../20261003-P-FORGE-ATOMIC-LEDGER.md
-->

# A0 R13方法修订Master单位补足与重冻结

> **状态：** `A0_REOPENED_BY_R13_MASTER_DECISION_GAP / A0_REFROZEN / C_CANONICAL=127 / C_BRANCH=3 / C_ATOMIC=130 / C_IDENTITY_REMAINDER=0 / N33_COMPLETE_N34_PENDING_A1`。

## 1. 触发：R13的两个方法决定不能只留在粗粒度父卡

R13的原汇总明确以两次 Git 方法修订为审计对象：`f51a205a` 的 CAL／来源层／station 合同，和`47ea9deb` 的
P/Q共同涌现／`QConvergenceLink`合同。它们各自改变了 P/Q 的准入、分类或停止语义。按照
`P-FORGE-ATOMIC-AUDIT-SOP` 对 `NON_H_MASTER_DECISION` 的定义，二者都是实际的 Master 工作单位：即使没有
worker session，也不能只以R13的粗粒度叙述代替其原子审计。

此前005的128成员没有登记它们。该遗漏不改变任何已经封存卡的事实，也不产生理论结论；它使“128已覆盖全部
R01--R13锻打单位”的说法失效，故A0定点重开。

## 2. 新增单位、身份与去重

| atomic_id | unit_kind / parent | raw identity | 改变的P/Q责任 | 分母判词 | A1状态 |
|---|---|---|---|---|---|
| `N33` | `NON_H_MASTER_DECISION / R13` | Git commit `f51a205a4c87a84a0b6a87e41f3c3eb98519d82d`，`research: tighten P calibration and station controls`，2026-10-03 02:33:16 -0400。 | 引入CAL-0..4、L-A..L-E、S1..S5，分开control、来源层、station与Theory-Q。 | `UNIQUE_MASTER_DECISION(1)` | `ATOMIC_AUDIT_COMPLETE` |
| `N34` | `NON_H_MASTER_DECISION / R13` | Git commit `47ea9deb8e1059ade41bdc6639e9e5cbaf3a72f2`，`research: bind P forging to Q convergence`，2026-10-03 02:54:44 -0400。 | 为ForgeIntent／TaskCard／SelfAudit加入Target-Q、Candidate-Q、Control-Q、状态前后、可证伪Q增量与`TOOL_ONLY_DRIFT`边界。 | `UNIQUE_MASTER_DECISION(1)` | `PENDING_A1` |

两个 commit 有不同OID、时间、直接 source、修改集合和P/Q效果，不能互相去重，也不等同于后来的 R13 audit report。
`108a7895` 等对这两项修订的验证／叙述提交只记录或审计既有决定，没有再次改变P/Q准入，故为
`MATERIAL_REPORT / OUT_OF_SCOPE_WITH_REASON`。跨分支`B001--B003`也与此无关。

## 3. 更新后的分母

```text
previous canonical D_atomic      = 125
new Master decisions             = 2  (N33, N34)
current canonical D_atomic       = 127
branch candidate executions      = 3
current D_atomic                 = 130
C_identity_remainder             = 0
completed AtomicAuditCards       = 129
C_audit_remainder                = 1
```

`N33,N34`按可核Git时间位于R12之后、R13粗单元之前；它们的精确父级是R13。A1必须先分别审计其`AS_RUN`、
当前合同反事实、QConvergenceLink、固定保护对象、消费证据、反证条件和重开条件。只有两张卡封存后，才可恢复A2并
书写R13父级回接。

## 4. 分母范围与重开条件

此次补足只修正“改变P/Q准入的非H Master decision”遗漏，不将每个审计、文档、README或Git提交一概纳入。一个新
Git动作只有实际改变P/Q准入、来源边界、候选资格、停止语义或审计路线，且不是对既有决定的纯记录时，才可能按
`NON_H_MASTER_DECISION`进入分母。

若发现另外一项这样的唯一Master decision、N33/N34只是纯文字复述、或二者与既有D_atomic身份相同，A0再次标为
`STALE`并重审受影响集合。否则本片的130单位分母为当前声明范围内的冻结分母；`ZFC_Q_LOCATED=NO`不变。
