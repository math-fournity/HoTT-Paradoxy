# HMZ-009：HoTT Book 的 Power Set—quotient 建构桥预检

> **身份：** `SOURCE_PREFLIGHT / EXISTING_R_HIGHER_TECHNICAL_BRIDGE / POWERSET_QUOTIENT_BRIDGE / PAIRING_SOURCE_REQUIRED / NOT_A_FULL_DENOMINATOR_RUN`。

## 预检问题

HoTT Book 是否已经提供了此前缺少的、从 HoTT 的 higher/direct-formation 线路到集合论 Power Set 的**精确建构桥**？若有，它是否同时给出了一个 ZFC 侧实际消费者：该消费者在形成、使用和完成标准相同的任务中，未经支付地把仍待形成的对象交给后续操作？

这里的“桥”与“Q”必须分开。桥只说明两个构造在一篇可定位来源中被并列；它不说明 ZFC 不一致、Power Set 有矛盾，或已经有一个模式 P 命中。

## 冻结来源

| ID | 类 | 来源 | 本轮身份 | 实读范围 |
|---|---|---|---|---|
| `HMZ-S-026` | A/B | *Homotopy Type Theory: Univalent Foundations of Mathematics*，Book source commit `578b85cc8d586b1677ec4335148adeb443057d24`。 | 新归档的 HoTT technical/construction bridge；不是新的作者级创立动机。 | `logic.tex:525–555`、`hits.tex:1257–1297`、`setmath.tex:363–455,487–499,1755–1761`。 |
| `HMZ-S-007` | C | Metamath `ax-pow` / `pwex`（在 HMZ-001 已冻结）。 | `REUSED_ZF_FORMATION_CONTROL`。 | Power Set 是 ZF 形成断言、`P(A)` 的 class notation；不含 quotient consumer。 |
| `HMZ-S-010` | C/D | Michael Shulman, *Set Theory for Category Theory*，2008（在 HMZ-001 已冻结）。 | `REUSED_ZFC_AXIOM_LAYER_CONTROL`。 | ZFC 的 Separation/Power Set 分层及其“ordinary constructions”说明；不含本预检所需的同一 quotient consumer。 |

`HMZ-S-026` 的三份原始 \(\LaTeX\) 文件被从本项目已追踪的 upstream snapshot 精确复制到 `originals/`，并逐一哈希。`derived/LOCATORS.md` 是只含 locator 与解释边界的派生阅读索引；不以摘录替代原件。

## 来源所给出的建构桥

`HMZ-S-026` 在同一 Book 版本中同时写出：

1. 当把商视为等价类的集合时，**集合论做法**是把这些等价类视为 \(A\) 的 Power Set 的一个子集（`hits.tex:1257–1277`；`setmath.tex:363–368`）；
2. 该表达的 type-theoretic 仿造使用 \(P:A\to\mathsf{Prop}\)，而等价类构造 \(A\sslash R\) 与 set-quotient \(A/R\) 等价（`hits.tex:1262–1297`；`setmath.tex:419–455`）；
3. 这个 class-style 版本会提升 universe，若要保持同一 universe 必须显式假定 propositional resizing（`hits.tex:1295–1297`；`setmath.tex:363–367`）；
4. Book 还把 external setoid/exact-completion construction 与通过 HIT 在内部取得 well-behaved quotients 区分开（`setmath.tex:487–499`）。

所以，这不是“Power Set”一词的共现：它固定了一个候选共享任务——给定集合 \(A\) 与等价关系 \(R\)，交付等价类所成的 quotient。

## 准入裁定

```text
new primary R_i: NO
new source-grounded construction bridge: YES
ZFC-side u/F: PARTIAL, via the Book's set-theoretic description plus reused
  ZF/ZFC Power Set and Separation sources
same quotient-style mathematical output: SOURCE-REPORTED
independent ZFC actual consumer / exact I/O/Done: NOT SUPPLIED
formation-use reentry / unpaid completion: NOT SUPPLIED
explicit costs/controls: universe lift, propositional resizing, and the
  external-versus-internal construction boundary are SOURCE-REPORTED
H0→Z0: NOT FORMED
SUCCESSOR RUN: PAIRING_SOURCE_REQUIRED
```

本预检不启动完整分母。它保留的下一来源条件很窄：一份版本固定的 ZFC／集合论实践或 formalization 来源，必须以同一 \(A,R\) quotient 任务给出实际 consumer 的输入、操作、观察与 Done；并且该来源必须允许检查 Power Set/Separation/representative/universe 等 payment 是否被省略。仅再次讲解 Power Set、quotient 或 HIT 的材料不足以重开。
