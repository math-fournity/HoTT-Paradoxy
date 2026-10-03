<!-- governance-shard:v2
logical_id: P_FORGE_ATOMIC_LEDGER
shard_id: 005
index: ../20261003-P-FORGE-ATOMIC-LEDGER.md
-->

# A0子session稳定ID补足与重冻结

> **状态：** `A0_REOPENED_BY_MULTI_SESSION_FAMILY_IDENTITY_GAP / A0_CHILD_SESSION_ID_REPAIR_COMPLETE / A0_REFROZEN / C_CANONICAL=125 / C_BRANCH=3 / C_ATOMIC=128 / C_IDENTITY_REMAINDER=0`。

## 1. 触发与范围

在A1已经封存 N01--N23 与 N32 共24张卡之后，准备进入旧账本的`N24 Battle-001`时发现：002将3个独立session
写成一个家族标签，N25/N26/N27也分别把4/8/3个独立session压在一个行名下。虽然003的总计已经按19个session计算，
每个成员却没有stable `atomic_id`，不满足本SOP“每个`D_atomic`成员恰有一张AtomicAuditCard”的合同。

这不是新增执行、重复计数或数学发现。它是 `IDEA_SPEC_INCOMPLETE` 在身份账本上的表现：总数128正确，成员的可审计命名不完整。
本片使家族标签只承担来源路由，将每个可观察session变成一个唯一子ID。N01--N23/N32已封存的卡不受影响；
`C_audit_remainder`的实时值仍由campaign独占，本次refreeze时为 `128 - 24 = 104`。

## 2. 稳定 child atomic ID 映射

### 2.1 F24（legacy N24）：Battle-001

来源：`audit/20261002-P-DAG-BATTLE-001-Terra-Max.md`，SHA-256
`8719c90b38635d79422631eb6c734d9edcedb673052ef9807bae417148967eb7`。

| atomic_id | 角色 | exact session | 原子身份 | A1状态 |
|---|---|---|---|---|
| `N24A` | B-A advocate | `01a0fd1b-039b-77e1-895a-b5ff743ce497` | relation-as-minimal-consumer立场。 | `ATOMIC_AUDIT_COMPLETE` |
| `N24B` | B-B challenger | `01a0fd1b-028d-7442-a124-e3e4a6af5577` | consumer-contract立场。 | `ATOMIC_AUDIT_COMPLETE` |
| `N24C` | B-C independent arbiter | `01a0fd1d-180b-7742-8c04-d83975b92ba1` | 只消费sealed battle pack的裁决。 | `ATOMIC_AUDIT_COMPLETE` |

### 2.2 F25（legacy N25）：SOURCE-001

来源：`audit/20261002-P-DAG-SOURCE-001-Terra-Max.md`，SHA-256
`a7b7f70e08aab6c37fee8244a583a357ff47542e961c9809e6364a6ac744f0b6`。

| atomic_id | 角色 | exact session | 原子身份 | A1状态 |
|---|---|---|---|---|
| `N25A` | S-A formal source tracer | `01a0fd24-e045-7e53-b290-ae608e851408` | Mathlib ZFSet形式化模型source定位。 | `ATOMIC_AUDIT_COMPLETE` |
| `N25B` | S-B math control tracer | `01a0fd24-e017-7330-8f84-cc677ee47132` | HoTT Book跨理论正控制。 | `ATOMIC_AUDIT_COMPLETE` |
| `N25C` | P2-A source-pack mapper | `01a0fd2c-5031-7923-b5a1-b19b5d50c37d` | 对冻结Mathlib card的P2映射。 | `ATOMIC_AUDIT_COMPLETE` |
| `N25D` | P3-A source-pack mapper | `01a0fd2c-4f56-7e10-95e5-08e62223ecb8` | 对冻结Mathlib card的P3映射。 | `ATOMIC_AUDIT_COMPLETE` |

### 2.3 F26（legacy N26）：SOURCE-002 与 BATTLE-002

来源：`audit/20261002-P-DAG-SOURCE-002-与-BATTLE-002-Terra-Max.md`，SHA-256
`2b4ec6660996e0c6b8e610f6faaeec99044b97e5e23590b79f0bb4c49e263beb`。

| atomic_id | 角色 | exact session | 原子身份 | A1状态 |
|---|---|---|---|---|
| `N26A` | S-C Metamath tracer | `01a0fd3d-a12b-7851-9f56-c9aa1469ed62` | ZFC-side proof-system source。 | `ATOMIC_AUDIT_COMPLETE` |
| `N26B` | S-D Isabelle P2 tracer | `01a0fd3d-a0d6-74e3-8105-e6fed4ff0566` | Isabelle/ZF formula source。 | `ATOMIC_AUDIT_COMPLETE` |
| `N26C` | S-E P3 source tracer | `01a0fd3d-a03d-7ca1-95cb-6fc2d0b4f7e4` | Mathlib ZFSet P3 negative source。 | `PENDING` |
| `N26D` | P1-B Isabelle mapper | `01a0fd45-dae0-7a31-ba81-d859daa94586` | Isabelle P1 card。 | `PENDING` |
| `N26E` | P3-B Isabelle mapper | `01a0fd4f-fb3b-7531-873b-500e807149b8` | Isabelle P3 card。 | `PENDING` |
| `N26F` | C-A proof advocate | `01a0fd48-9ab9-73c3-a379-4d2a7a5e8a59` | proof-system consumer立场。 | `PENDING` |
| `N26G` | C-B object challenger | `01a0fd48-9a7c-72a0-b169-9b08ffefd1e5` | target-layer consumer质询。 | `PENDING` |
| `N26H` | C-C layer arbiter | `01a0fd4c-2a1d-7d21-bfec-f3172b85d04c` | layer-integrity裁决。 | `PENDING` |

### 2.4 F27（legacy N27）：SOURCE-003

来源：`audit/20261002-P-DAG-SOURCE-003-TIMEOUT-Terra-Max.md`，SHA-256
`803c8720e74016710268d0fc5fc94376b795f3cdf94d2c35794187288e2585a1`。

| atomic_id | 唯一目标 | exact session | 原子身份 | A1状态 |
|---|---|---|---|---|
| `N27A` | Cantor型数学consumer tracer | `01a0fd5f-0afa-7773-8245-f873a22e49cc` | 无terminal output，Master SIGINT。 | `PENDING` |
| `N27B` | P3 lifecycle/admission tracer | `01a0fd5f-0abc-7ec2-82f1-fe67d40bfff3` | 无terminal output，Master SIGINT。 | `PENDING` |
| `N27C` | Cantor C/I/O/Done审计 | `01a0fd5f-0b21-70f0-8a90-7efa8c9ea504` | 无terminal output，Master SIGINT。 | `PENDING` |

`N28`仍是单一foreground retry（`01a0fd6f-a6d8-7db1-a4a4-7184ff2ac118`），故保持已有ID；其背景尝试无console/final artifact，继续排除。

## 3. 去重、顺序与A1恢复

`N24A--N24C`、`N25A--N25D`、`N26A--N26H`、`N27A--N27C`的UUID彼此不同，也与已登记H节点、N01--N23、N28--N32和branch单位不同。旧`N24--N27`不再是atomic ID，只是历史家族引用。

审计顺序先尊重报告的角色依赖：Battle先双方后arbiter；source tracer先于mapper；source/battle的独立节点按报告表顺序；
SOURCE-003三项都标为并列取消、以表中A/B/C作为稳定tie-break。这样不会伪造不可见的精确墙钟顺序。

修复后：

```text
C_canonical           = 125
C_branch              = 3
C_atomic              = 128
C_identity_remainder  = 0
C_cards                = 24  (由campaign实时记录)
C_audit_remainder     = 104 (由campaign实时记录)
```

下一张A1卡是`N24A`，不是旧家族标签`N24`。每一个child session将有独立AtomicAuditCard和独立Git commit；
父Battle/SOURCE总结只能在A2回接，不可替代三个、四个或八个子卡。

## 4. 重开条件与范围

若发现任何child UUID实际是另一已登记session的重复、某个报告遗漏了独立terminal/pre-sampling动作、或角色与
冻结source不符，A0再次标为`STALE`并只重审受影响家族。此次修复不改变任何ZFC/HoTT数学结论、Power Set站位、
P1/P2/P3字段或已经封存卡的历史事实。
