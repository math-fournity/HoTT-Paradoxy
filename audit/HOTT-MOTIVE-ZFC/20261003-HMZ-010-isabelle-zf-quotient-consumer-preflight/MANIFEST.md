# HMZ-010：Isabelle/ZF quotient consumer 预检

> **身份：** `SOURCE_PREFLIGHT / HMZ-009_PAIRING_SOURCE / ACTUAL_PROOF_FORMALIZATION_CONSUMER / F_ROUTE_MISMATCH_AND_EXPLICIT_PAYMENT / ADMISSION_REJECTED_WITH_SCOPE`。

## 预检问题

HMZ-009 已从 HoTT Book 固定一个\(A,R\) quotient 与 Power Set 的建构桥。Isabelle/ZF 的 `EquivClass` 是否提供该任务所需的实际消费者；若提供，它是否在与 Book 同一 **formation route** 上，把尚未付清的 Power Set/quotient 交给后续 operations，还是以 Replacement／`RepFun`、equivalence 和 congruence 前提把交付条件显式化？

本预检只检查一个精确 proof-formalization source，不将 Isabelle/ZF 冒充 bare ZFC object language、一般数学实践或全部 ZFC 的消费者。

## 冻结来源

| ID | 类 | 来源 | 版本／归档状态 | 作用 |
|---|---|---|---|---|
| `HMZ-S-027` | C/D | Lawrence C. Paulson, `ZF/EquivClass.thy`，Isabelle mirror tag `Isabelle2021-1-RC5`，commit `6a65dad3761d436f234dbd752201fe70fffa0200`。 | `originals/HMZ-S-027-Isabelle2021-1-RC5-EquivClass.thy`; SHA-256 `83016841fba6a0b469692ccc5a5b8d65e3953bee1ca6bb348eac9acd51619b76`. | 精确 quotient definition、introduction/elimination、unary/binary quotient operations。 |
| `HMZ-S-011` | C | Paulson, *Isabelle’s Logics: FOL and ZF*, Isabelle2021-1, 2021（HMZ-001 复用）。 | 已归档 PDF hash `2b91b2f89480e8b14201dbc93382df366737d405dbd67c39de6970ecf14cd646`. | `RepFun` 是 functional replacement 的来源解释和规则。 |
| `HMZ-S-026` | A/B | HoTT Book 578b85cc（HMZ-009 复用）。 | 已归档的三文件 source snapshot。 | Power Set-subset quotient route 与 explicit resizing/universe controls。 |

### 版本边界

`HMZ-S-027` 固定为公开 Git mirror 的 `Isabelle2021-1-RC5`；`HMZ-S-011` 是正式 `Isabelle2021-1` manual。两者不是在本预检中被断言为同一 bytes 或同一 release source tree。代码文件自身决定本预检关于 `quotient`、`RepFunI`、`equiv` 与 `respects` 的事实；manual 只作为独立、同系统系的 `RepFun` 解释控制。不得用二者的版本相邻性替代 source identity。

## 最小 `u/F/C/I/O/Done` 卡

```text
u:
  Isabelle/ZF object type i 中的 set A、relation r、class r``{x} 和 quotient A//r.
F:
  quotient_def: A//r == {r``{x} . x ∈ A}; quotientI uses RepFunI.
  The manual identifies RepFun as functional replacement.
C:
  quotientE, Union_quotient, quotient_disj, UN_equiv_class,
  UN_equiv_class_type and the binary-operation lemmas.
I/O/Done:
  Input A, r, a or X, and a unary/binary b; operation form/use A//r;
  observation a quotient membership, an equality of well-defined values, or a
  type-membership conclusion; Done is the stated theorem only after equiv,
  respects/congruent and membership hypotheses are discharged.
```

## 准入裁定

```text
actual consumer: YES, at PROOF_FORMALIZATION layer
same quotient-style output as HMZ-009: YES
same Power Set formation route as HMZ-009: NO
  HMZ-S-027 defines quotient through functional replacement / RepFun, not as
  the Book's Power Set-subset construction.
source payment / guard: YES
  equiv(A,r), respects/congruent, membership and RepFun formation are explicit.
P1 native task / C: PRESENT_AT_PROOF_FORMALIZATION_LAYER
P2 same-object reentry: NOT SUPPLIED
P3 pending admission / unpaid Done: NOT SUPPLIED
H0→Z0: NOT FORMED
SUCCESSOR RUN: ADMISSION_REJECTED_WITH_SCOPE
```

This is a successful **pairing test**, not a failed search: it demonstrates that a source-defined quotient consumer can be found and audited. Its result is a route-split and payment control, not a `Q`.
