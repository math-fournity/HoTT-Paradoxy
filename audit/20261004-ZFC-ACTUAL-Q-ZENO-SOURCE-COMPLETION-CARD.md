# ZFC 实际 Q：芝诺 Standard Solution 的来源完成政策卡

> **身份：** `SOURCE_COMPLETION_CARD / ZENO_POLICY_ESTABLISHED_WITH_SCOPE / TASK_CONTRACT_SPLIT / CROSS_CASE_SCOPE_UNOBSERVED`。
>
> **本卡解决的问题：** 区分“标准来源真的有完成政策”与“该政策已经支付用户圆环或 HoTT 的同一任务 bridge”。前者现在有来源；后两者仍没有。

## 1. 冻结来源与可引用内容

| 来源 | 版本／读取边界 | 当前可支持的直接事实 |
|---|---|---|
| [IEP, *Zeno’s Paradoxes*](https://iep.utm.edu/zenos-paradoxes/) | 当前网页，2026-10-04 复核；§2 L180、L184、L289–L290、L309–L315。 | Standard Solution 将级数收敛、actual infinity、连续 physical path 与跑者有限时间到达目标联结；它明确回答“没有最后一步也能完成”并列出必须放弃的直觉。它也明确承认抽象连续统对现实时间／空间的 adequacy 仍受哲学争论。 |
| [SEP, *Supertasks*, Summer 2026](https://plato.stanford.edu/archives/sum2026/entries/spacetime-supertasks/) | 归档版本，§1.1 L46–L54。 | 现代数学给出 Zeno supertask 的解释；在实数标准拓扑下几何级数收敛；“执行最后动作”和“做完每一步”在 finite task 中等价、在 supertask 中不等价。页面把后一义用于 Zeno walk，同时保留对所选拓扑是否恰当的疑问。 |
| [Norton, *Zeno’s Paradoxes of Motion*](https://sites.pitt.edu/~jdnorton/teaching/paradox/chapters/Zeno/Zeno.html) | 当前网页，2026-10-04 复核；L230–L233、L259–L282。 | 明说无限和的定义是现代数学的额外设定；将“完成全部动作、包括最后动作”替换为“完成全部动作”，并以每个 action 的时刻说明完成。 |

这些来源的确切段落与本卡的转述绑定；它们不是 Lean 定理，也没有被改写为用户圆环的过程规格。

## 2. SourceCompletionCard：Zeno 侧已支付到哪里

| 字段 | IEP／SEP／Norton 的来源级内容 | 当前状态 |
|---|---|---|
| `TheoryLayer` | ZFC-supported standard real analysis、classical mechanics、连续时间／位置模型，以及关于 Zeno 的哲学验收叙述。 | `SOURCE_ESTABLISHED_WITH_SCOPE` |
| `I` | 从起点到目标的 runner／Achilles／Dichotomy 路线。 | `SOURCE_ESTABLISHED_WITH_SCOPE` |
| `Op/F` | 连续正速度运动；经过 (1/2,3/4,7/8,\ldots) 等子路径／位置；级数或实数拓扑的极限处理。 | `SOURCE_ESTABLISHED_WITH_SCOPE` |
| `O` | 位置、实数时间、子路径、是否有 final action、是否做完每个 action。 | `SOURCE_ESTABLISHED_WITH_SCOPE` |
| `Done_formal` | 级数收敛到 1、连续模型的 endpoint／目标到达、或所有 Zeno steps 在 limit 中完成。 | `SOURCE_ESTABLISHED_WITH_SCOPE` |
| `Done_source` | 跑者到达目标／在有限时间完成 course；IEP将此作为 Standard Solution 的结论。 | `SOURCE_ESTABLISHED_WITH_SCOPE` |
| `Done_strict` | “完成所有动作且包含最后动作”。Norton与 SEP 都把它列为有限任务直觉，不适用于没有最后 action 的 Zeno supertask。 | `TASK_SWITCH_EXPLICIT` |
| `Bridge / adequacy` | IEP把连续 physical path、实际无穷、calculus 和 scientific fruitfulness作为 Standard Solution 的理由；它没有将这写成一条仅由 ZFC 公理推出的同一任务定理。 | `SOURCE_POLICY_ESTABLISHED_WITH_ASSUMPTIONS` |

因此，来源不是只说“数学对象存在”。它们确实有一个**芝诺侧、源任务范围内**的 policy：在其连续 runner 模型里，采用不要求 final action 的完成概念，并判定跑者到达目标。

## 3. P 的三层区分

```text
P_Zeno-source
  = Standard Solution 对其连续 runner task 的来源级完成政策：
    连续模型／实际无穷／其定义下的步骤完成可以支持“到达目标”。

P_revised
  = Norton／SEP 公开改写 Done；它不是把 Done_strict 偷写成同一谓词。

P_circle/HoTT
  = 将上述政策进一步用于“此前 M 经指定反向过程复原”或
    fixed HoTT Q 的 original completion。
```

`P_Zeno-source` 现在是 `SOURCE_ESTABLISHED_WITH_SCOPE`。`P_revised` 是 `TASK_SWITCH_EXPLICIT`。只有第三项才是 C-359 所需的跨案例 `PolicyScopeWitness`；当前为 `SOURCE_UNOBSERVED`。

这解释了为何“来源明确改写 Done”不能轻率地消灭用户的问题：它支付或改变了 **其自己的 Zeno task**，却没有证明用户圆环的 `OriginDone` 已被保持，也没有给 HoTT 的 completion-reflection 问题提供范围桥。反过来，这也禁止我们把来源的公开 Done 改写描述成已经证实的“隐藏幻觉”。

## 4. 对 C-359 与 C-362 的精确影响

- C-359 的 `ZFCOneUse.gapAdmitsZenoP` 仍然是**条件性因果前提**。来源支持的是 Zeno-side completion policy，不是“它因为正式的 `QMissing` 而接受 P”的历史因果证明。
- C-362 说明：若 `OriginDone` 没有进入 membership-only base theory 的 specification／bridge，base layer 本身不决定它；它不把 IEP 的 runner policy自动运输到圆环或 HoTT。
- C-360 给出 fixed HoTT Q 的 completion-reflection failure；它仍缺少同一任务映射和 source-owned policy scope。
- C-361 给出“几何级数极限不等于有限自然数阶段 endpoint”的严格控制，同时保留闭连续时间 endpoint 正控制；它不能取代来源的 `Done_source`。

## 5. 收尾判词与剩余义务

```text
SOURCE_ZENO_POLICY_ESTABLISHED_WITH_SCOPE
SOURCE_TASK_CONTRACT_SPLIT
SOURCE_CROSS_CASE_POLICY_SCOPE_UNOBSERVED
USER_CIRCLE_ORIGIN_DONE_PARTIAL / USER_DONE_ADJUDICATION_REQUIRED
ACTUAL_Q_POLICY_CONFLICT_WITH_SOURCE_BOUNDARY = NOT_REACHED
```

剩余的不是“再找一篇说 calculus solves Zeno 的文章”，而是两项受限证据：

1. 将用户圆环的 `OriginDone` 固定到足以比较的过程合同，同时不暗加“最后离散步骤”这一用户没有授权的条件；
2. 找到或排除一份来源，它将 `P_Zeno-source` 的完成政策扩张到该 circle contract 和 fixed HoTT Q，给出 `PolicyScopeWitness` 所需的范围理由。

在这两项未支付时，最强且诚实的结论是：ZFC-supported Standard Solution 有一个明示的、局部的完成政策；它没有在当前来源分母中成为一个已证实的 ZFC—圆环—HoTT 统一政策。

## 6. HoTT／类型论方向的邻接时间控制与有界检索

为避免把“当前没有跨案例 scope source”误写成“类型论社区从未正面处理时间或 Zeno”，本轮还核对了 Diezel 与 Goncharov 的 [*Towards Constructive Hybrid Semantics*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol167-fscd2020/LIPIcs.FSCD.2020.24/LIPIcs.FSCD.2020.24.pdf)（FSCD 2020）。其摘要明确将 Zeno behaviour 和连续时间称为 hybrid semantics 的特殊、不可编程特征；它用表示时间域的有序幺半群、cubical Agda 与高阶归纳归纳类型建模，并在第 9 页以 (1/2,1/2+1/4,\ldots) 为 Zeno sequence 的实例。

这是一条重要的 `ADJACENT_TYPE_THEORY_TIME_CONTROL`：它支持“若任务包含 Zeno behaviour，时间／完成结构必须显式进入语义”的研究直觉，同时反驳“类型论社区从未看见时间维度”的宽泛表述。但它不是当前 `QuestioningDelay` HoTT Q，也不是 IEP Standard Solution 的 policy owner：

| T0–T5 门 | 比较结果 |
|---|---|
| T0 theory layer | hybrid semantics / cubical Agda / ordered monoid，不是 bare ZFC 或 Standard Solution。 |
| T1 subject | hybrid program 的潜在发散与最终 value，不是圆环 M/N 或 universe questioning。 |
| T2 formation | directed-sequence completion／quotient 有显式构造。 |
| T3 operation | 迭代、时间索引序列和 completion 被明示建模，未出现当前 P3 的未付使用。 |
| T4 observation | 程序语义和 time-indexed value，不是用户圆环的来源复原观察。 |
| T5 Done | final value／divergence 合同，不是 Standard Solution 到 HoTT 的统一 acceptance policy。 |

因此它的判词是 `SOURCE_LAYER_CONTROL / TRANSPORT_ANTI_ANALOGY`，不是 `PolicyScopeWitness`。

本轮还以四组精确网页检索词检查直接跨案例来源：`"homotopy type theory" "Zeno's paradox"`、`"homotopy type theory" supertask completion`、`"univalent foundations" Zeno completion`、`"type theory" "Zeno" "completion"`。结果包含 Rezk completion、hybrid semantics 和一般 HoTT 资料，却没有一份同时把 **IEP／SEP 的 Standard Solution completion policy** 施用于 **fixed `QuestioningDelay` Q** 的来源。该负结果只支持：

```text
NO_DIRECT_CROSS_CASE_POLICY_SOURCE_WITHIN_DECLARED_QUERY_SET
```

它不证明全体文献中不存在这种来源，也不关闭未来更广的版本固定来源分母。
