# R2 跨内核 TaskSpec correspondence

本文件解释 `R2-TASKSPEC.json` 的证据强度。它不是第四份数学证明，也不声称 Coq 与 Agda 的语法树在某一 kernel 内相等。

## 已由 kernel 分别证明的链

### Coq 8.15.2

`C-214`–`C-218` 在同一个 kernel 中完成：

```text
upstream relational MM2 termination
  ↔ finite functional source observation
  ↔ finite explicit-target observation

MM2_HALTING ⪯ PC_HALTING
MM2_HALTING_undec ⇒ PC_HALTING_undec
```

`undecidable` 保持上游定义：`decidable P → enumerable(complement SBTM_HALT)`。

### Cubical Agda 2.8.0 / Cubical v0.9

`C-209`–`C-213` 对本地源与项目目标完成：

```text
functional MM2 lookup/step/run/finalAt
  = compiled ProgramCode lookup/step/run/finalAt

MM2Halts ↔ CodeHalts(compileMM2)
```

## 四模型 correspondence

| 维度 | Coq source | Coq target | Agda source | Agda target | 裁决 |
|---|---|---|---|---|---|
| state | `(pc,(a,b))` | 同左 | `cfg pc a b` | 同左 | 字段双射，源码级固定 |
| first source label | 1 | 1 | 1 | 1 | 一致 |
| halt sentinel | source label 0 无指令 | target index 0=`halt` | source label 0=`nothing` | target index 0=`halt` | 观察等价；表示不同 |
| outside table | 无关系后继 | default halt | `nothing`/final | default halt | 观察等价 |
| INC | counter+1，pc+1 | 显式 next=pc+1 | counter+1，pc+1 | 显式 next=pc+1 | 两 kernel 内全称证明 |
| DEC zero | pc+1 | onZero=pc+1 | pc+1 | onZero=pc+1 | 两 kernel 内全称证明 |
| DEC successor | decrement，jump j | onSuc=j | decrement，jump j | onSuc=j | 两 kernel 内全称证明 |
| bounded run | 从关系闭包恢复步数 | `pc_run` | `mm2Run` | `runFor` | 各 kernel 内闭合 |
| halting witness | 普通 `exists` | 普通 `exists` | propositional truncation | propositional truncation | 只要求 mere finite existence；逻辑表示不相同 |

## 机器 correspondence verifier 的意义

`scripts/audit/verify_r2_cross_kernel_correspondence.py`：

1. 验证 TaskSpec schema 与所有 source anchors；
2. 验证三个 proof/run/claim 身份和冻结索引行；
3. 调用 Agda 与 Coq 的静态 run verifier；
4. 对指令、jump、label、零／后继计数器的有限控制域执行独立可执行模型比较；
5. 产出确定性的 correspondence receipt。

有限控制域只用于发现字段交换、分支反转和哨兵错误；全称数学强度来自 C-209–C-218，而不是有限枚举。

## 当前可交付判词

```text
DUAL_KERNEL_SCOPED_CORRESPONDENCE
/ SAME_KERNEL_COQ_TOTAL_REDUCTION
/ AGDA_LOCAL_HALTING_EQUIVALENCE
/ SYNTHETIC_UNDECIDABILITY_ONLY
/ CROSS_KERNEL_DEFINITIONAL_IDENTITY_NOT_CLAIMED
```

这足以说明 R2 的编码、编译和 synthetic reduction 没有只由一个 kernel 的偶然实现支撑；它仍不足以完成 `goal.md`，也不足以把 synthetic implication 写成无条件 no-decider。

