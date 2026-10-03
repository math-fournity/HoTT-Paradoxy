# HMZ-001：真实消费者与标准防线

## HMZ-C-001 — Mumford 1965 的 moduli / universal family 控制

| 字段 | 原件所示的任务 |
|---|---|
| 原件 | `HMZ-S-009`，Mumford 1965，PDF physical p. 1 = printed p. 33；p. 2 = printed p. 34；p. 5 = printed p. 37。 |
| 输入 | 非奇异曲线的模问题、曲线族与按同构分类的对象。 |
| 操作 | 构造能够通过参数映射拉回的 universal family，或为 definite model 选取相应对象。 |
| 观察 | 是否存在 universal family；automorphisms 是否存在；是否给出覆盖所需的 particular maps。 |
| Done | 得到明示的 family／mapping data，而非只有 coarse classification。 |
| `C+` 正控制 | Printed p. 33 的脚注：当 `g ≥ 3`，几乎所有曲线没有 automorphisms，并存在 automorphism-free nonsingular curves 的 universal family。 |
| `C−` 标准防线 | Printed p. 37：允许 nontrivial automorphisms 后，只说 open sets cover 不再充分；需要指定 particular maps。 |
| 当前处置 | `DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT`。 |

**为什么它重要。** 它不是对 ZFC 的一般证明，也不是 HoTT 的反例。它是一个真实的数学任务，直接说明
“按同构分类”与“给出可用的 family”不同；而原典没有把第二件事伪装成第一件事已经完成。因此，它排除了把
R-STRUCT 自动升级成 Q 的捷径。

## HMZ-C-002 — HoTT Book 内部 V/ZFC 的兼容控制

| 字段 | 内容 |
|---|---|
| 原件 | `HMZ-S-001`, `setmath.tex:7–27,1755–1760`. |
| 事实范围 | 作者区分 HoTT 的 sets 与 ZF sets，讨论内部累计层级 V，并在 `choice + universe` 条件下陈述 V 是 ZFC 模型。 |
| 对本项目的作用 | 反驳“HoTT 选择 homotopy types 而不是 sets，因此 ZFC 必然不能表达／已经有缺陷”的跳跃。 |
| 不足以推出 | 任何具体 ZFC consumer 已经支付某个存在、过程、来源或完成义务。 |
| 当前处置 | `ANTI_ANALOGY_CONTROL`，仅针对 blanket inference。 |

## HMZ-C-003 — Metamath 的层级控制

| 字段 | 内容 |
|---|---|
| 原件 | `HMZ-S-007`, `ax-ext`, `ax-pow`, `pwex`, `rankpw`, `ax-reg`. |
| 可报告的精确事实 | `ax-ext` 给成员相同推出集合相等的公式；`ax-pow` 给出包含所有子集的集合存在；`pwex` 把 `A∈V` 推至 `P(A)∈V`；`rankpw` 给出 rank successor；`ax-reg` 是 Foundation 形式呈现。 |
| 不可报告的外推 | 运行时 scheduler、构造 admission、真实消费者的 I/O／Done、历史／来源字段、任意谓词的内部 evaluator，或所有形成问题已经解决。 |
| 当前处置 | `SOURCE_LAYER_GUARD`。 |

## HMZ-C-004 — 任务保持测试

任何将 R 卡升级为 Q 卡的未来材料都须通过下列对照：

```text
同一输入是什么？
同一操作是什么？
同一观察量是什么？
同一 Done 是什么？
原来源是否已经提供了选择、标签、映射、证书或截断？
候选是否把“存在对象”偷换成“自然、可计算、可恢复、可执行交付”？
```

若添加了这些条件，结论只能是 `TASK_SWITCH`；若原来源已明确支付，结论是 `SOURCE_PAYMENT`。

## HMZ-C-005 — Shulman 的 ZFC / NBG 大范畴边界与支付

| 字段 | 内容 |
|---|---|
| 原件 | `HMZ-S-010`, pp. 10–14 / derived lines 516–690。 |
| ZFC 内的清晰边界 | 类被理解为由一阶 set-theoretic formula 刻画的集合；ZFC 中没有量化类的语言，因此“任意大范畴”形式的定理不在 ZFC 内部陈述。 |
| `C+` | 对一个固定大范畴可以使用 ZFC 的 formula/class encoding 做许多基本构造。 |
| `C−` | NBG 将 classes 作为新类别引入，并允许 class quantification；其对 set statements 保持 conservative extension 的限定。 |
| Choice payment | 将 finite products 组织为 product functor、构造 inverse equivalence 或 skeleton 的 source examples 明示要求 ordinary/global choice。 |
| 当前处置 | `REPRESENTATION_BOUNDARY + EXPLICIT_LANGUAGE_PAYMENT`，不是 P 或 UR。 |

## HMZ-C-006 — Isabelle/ZF 的实际形式化支付

| 字段 | 内容 |
|---|---|
| 原件 | `HMZ-S-011`, printed pp. 19–27。 |
| 事实 | Manual states that ZF is implemented as an extension of classical FOL; Replacement's scheme is awkward in many provers but Isabelle handles it; axioms' bare existential style is supplemented with named constants/derived syntax for practical reasoning. |
| 近邻任务 | 在 proof assistant 内使用 ZF 的 functions, recursion, inductive definitions and formal developments。 |
| 不可外推 | 这不认证 ZFC 的所有数学实践可执行，也不把 proof checker 的内部 state 解释为 ZFC 的 formation lifecycle。 |
| 当前处置 | `SOURCE_PAYMENT / LAYER_INTEGRITY_CONTROL`。 |
