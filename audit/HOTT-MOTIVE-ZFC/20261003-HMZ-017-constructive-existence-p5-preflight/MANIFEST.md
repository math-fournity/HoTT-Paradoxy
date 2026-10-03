# HMZ-017：constructive existence、程序交付与 P5 的预检

> **身份：** `SOURCE_PREFLIGHT / E_SOURCE_CONSTRUCTIVE_DELIVERY_ANTECEDENT / P5_COMPARISON / FULL_RUN_ADMISSION / NOT_A_ZFC_Q_OR_MATH_CLAIM`。

## 预检问题

用户模式 P 强调：理论不能把尚未支付的形成／存在性追问当作已完成输入，且真实消费者的 Done 必须得到实际交付。构造逻辑／类型论文献是否早已以“存在证明给出程序、终止和正确性”表达了这一层？若是，这构成对 user-P 新颖性的什么限制；又为什么它仍不等于找到 ZFC 的 P-qualified Q？

## 冻结来源

| ID | 类 | 来源 | 原件／哈希 | 实读范围 |
|---|---|---|---|---|
| `HMZ-S-031` | E/B/D | Erik Palmgren, *Constructive logic and type theory*, March 2004 Uppsala lecture notes. | `originals/HMZ-S-031-Palmgren-2004-Constructive-Logic-Type-Theory.pdf`; SHA-256 `8e1fc5ac966cf44999e9ad3e011020dbea538ee9b1aafe611b6f4379dc75b083`. | pp. 1–3 and early nonconstructive-proof examples. |

Public source: <https://www2.math.uu.se/~palmgren/tillog/klogik04-01eng.pdf>. The notes articulate constructive logic/type theory, not a theorem that classical ZFC is inconsistent or a claim that every mathematical existence proof must compute.

## Source-reported content

```text
constructive principles:
  proofs are programs; propositions are data types.
existence delivery:
  an existence proof can yield a program constructing the purported object,
  together with verification of termination and correctness.
classical contrast:
  nonconstructive existence proofs may lose algorithmic content.
historical context:
  Russell/unrestricted set formation and foundational crisis are discussed;
  Brouwer’s mental construction is interpreted algorithmically.
```

## P-layer disposition

| Field | Source status |
|---|---|
| existence-to-delivery distinction | `SOURCE_REPORTED` |
| program / termination / correctness contract | `SOURCE_REPORTED` |
| user-P P5 preemptive use of an unpaid \(u\) by a fixed theory consumer | `NOT_SUPPLIED` |
| ZFC consumer promising constructive delivery | `NOT_SUPPLIED` |
| same-task reality/Done comparison | `NOT_SUPPLIED` |

## Admission result

```text
community antecedent to existence/computation/delivery distinction: YES
identity with full user-P P5: NOT ESTABLISHED
ZFC Q: NOT FORMED
SUCCESSOR RUN: FULL_RUN_ADMISSION
```

[HMZ-018](../20261003-HMZ-018-constructive-delivery-p-comparison/MANIFEST.md) has now closed that comparison. Its result is `COMMUNITY_ANTECEDENT_TO_EXISTENCE/DELIVERY / P5_PREEMPTIVE_USE_NOT_ESTABLISHED / NO_ZFC_Q`: the constructive contract cannot be used as a normative premise that ZFC has already violated.
