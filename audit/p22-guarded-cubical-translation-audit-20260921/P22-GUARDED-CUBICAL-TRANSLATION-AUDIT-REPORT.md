# P22-GUARDED-CUBICAL-TO-BARE-HOTT-TRANSLATION-AUDIT-001：Guarded Cubical 理论的 source/target 边界

**状态：** `NO_EXPLICIT_GCTT_TO_BARE_HOTT_FORGETFUL_ROUTE_WITHIN_FIXED_SOURCE / DEFENSE_GUARD_AND_LATER_EXPLICIT / PARK_PENDING_CONCRETE_STANDARD_TRANSLATION_TARGET / NO_NEW_HOTT_DEFECT_CLAIM`

## 固定公开来源

审计对象为 Guarded Cubical Type Theory 的 arXiv `1611.09263v2`、Guarded HoTT 项目页和本地 `GuardErasure.agda`。

论文将 GCTT 定义为 GDTT 与 CTT 的组合：later type-former `▷`、`next`、delayed substitutions 与受控 fixed-point unfolding 都是显式的源理论构造。它用 `Str_A = A × ▷ Str_A` 区分 now 可用的 head 和 later 可用的 tail，并将 guarded fixed-point 的类型写为 `(▷ A → A) → A`，明确区别于不受 guard 的 `(A → A) → A`。论文还给出独立的 GCTT 语义和 prototype checker；它不是一份“将 guards 擦除到 bare HoTT 并承诺同一完成”的声明。[论文 HTML](https://arxiv.org/html/1611.09263)，[项目页](https://cs.au.dk/~birke/ghott/index.html)

## P7/Guard-Erasure 对照

| 项 | 固定来源事实 | 判词 |
|---|---|---|
| source input | later/next/delayed substitution/guarded fixed-point 都显式出现 | `NOT_BARE_INPUT` |
| target | 文本构造 GCTT，不是可定位的 bare HoTT forgetful target | `NO_FIXED_BARE_TARGET` |
| claim | 目标是 guarded recursive construction 的 equality/semantics/type-checking | `NO_SAME_DONE_CLAIM` |
| forgetting | 没有在固定来源中找到 stage/availability 被删除后仍保持同一 update law 的实际 route | `NO_ERASURE_ROUTE_FOUND_WITHIN_FIXED_SOURCE` |
| version | arXiv v2 + 项目页；无本项目 checker replay | `SOURCE_INSPECTED_WITH_SCOPE` |

本地 `GuardErasure.agda` 已证明：**若**一个明确的 stage-erasing translation 保留 update law，则会强制 fixed point；对于 Bool negation 没有该 translation，反之有 fixed point 时可构造相应 collapse。这个局部定理不能替代实际 GCTT→bare HoTT route。

## 结论与停放条件

当前没有找到一个版本固定、实际声明的 GCTT/clocked/guarded → bare HoTT forgetful translation，满足“擦除 guard/availability 后仍以同一 Done/observable 消费”的条件。故 Guard-Erasure 的关键桥保持 `PARK_PENDING_CONCRETE_STANDARD_TRANSLATION_TARGET`。

这不是负面研究结果：它准确排除了把一个显式 guarded theory误报为它已经制造了 bare HoTT 的时间擦除。只有出现具体 translation、实际库入口或明确应用承诺时，才重开这条 bridge。

## 波次定位

P22 给用户原始时间方向提供了一个严格分层：一般 GuardErasure lemma 已机器证明；标准 guarded cubical source 显式保留 guards；缺失的是具体 source→bare route，而非一个已证 HoTT 问题。该分支在等候具体 target 时停放，Goal 应从其它独立 ingress 继续，而不是继续同义文献搜索。
