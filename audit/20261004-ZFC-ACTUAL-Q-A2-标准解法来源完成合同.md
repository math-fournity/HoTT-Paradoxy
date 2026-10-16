# A2：ZFC 支撑的芝诺标准解法之完成合同来源卡

> **身份：** `SOURCE_COMPLETION_CARD / ACTUAL_Q_CONVERGENCE_INPUT / NOT_A_KERNEL_THEOREM`。
>
> **任务：** 冻结 IEP 与 Norton 对芝诺 Dichotomy／标准解法的 `C/I/O/Done`，判断它们能否填入 C-359 所需的 `P = formalDone → originDone`，以及它们是否反而提供一张“完成合同被改写”的来源卡。
>
> **采集日期：** 2026-10-04；公开网页的直接读取定位保留为 URL 和行号。网页文字是外部来源，以下分类是本项目的来源解释，不是 Lean 对历史文本的证明。

## 1. 冻结来源与直接可见内容

| ID | 来源／版本 | 直接可见的关键内容 | 本卡只承认的范围 |
|---|---|---|---|
| `IEP-ZENO-20261004` | [Internet Encyclopedia of Philosophy, *Zeno’s Paradoxes*](https://iep.utm.edu/zenos-paradoxes/) | 第 112–126 行：多数观点把带 Choice 的 ZF 视为实分析基础，并把该框架称为对芝诺的间接解答；第 174、180、184 行：标准解法以几何级数、微积分和连续时间处理 Dichotomy，且回答“旅行是否需要最后一步”为“不需要”。 | 这是一个 `ZFC-supported continuum / standard-solution` 来源卡，支持“标准解法被称为解答”与“其 Done 不要求最后一步”。不证明 bare ZFC 语法推出任何运动结论。 |
| `NORTON-ZENO-20261004` | [John D. Norton, *Zeno’s Paradoxes of Motion*](https://sites.pitt.edu/~jdnorton/teaching/paradox/chapters/Zeno/Zeno.html) | 第 226–233 行：无穷和为 1 的读法包含现代数学的额外定义；第 259–276 行：严格完成包含最后动作，缩减完成只要求做完所有动作，解法靠删除前一要求；第 282–286 行：给每个指定动作分配一个时间。 | 这是明确的 `Done_strict → Done_revised` 来源卡：它不是默默假设 bridge，而是明说删去最后动作条件。 |
| `SEP-ZENO-20261004` | [Stanford Encyclopedia of Philosophy, *Zeno’s Paradoxes*](https://plato.stanford.edu/entries/paradox-zeno/) | 第 243–248 行：received view 的目标不仅是数学不受威胁，也要求数学正确描述真实对象、时空和运动；该适用性是可争论且取决于物理现实的。 | 防止把“数学内部计算通过”直接写成“物理过程已经被同一任务解决”。 |

## 2. 来源级 `C/I/O/Done` 卡

| 字段 | `IEP-ZENO-20261004` | `NORTON-ZENO-20261004` | 证据状态 |
|---|---|---|---|
| 理论层 `T` | ZFC with Choice 支撑的标准实分析、微积分与连续物理模型 | 几何级数、连续时间与动作序列的哲学分析 | `SOURCE_ESTABLISHED` |
| 输入 `I` | Dichotomy runner、无穷半程序列、连续时空／速度模型 | runner 的无限动作序列或相应 partial sums | `SOURCE_ESTABLISHED` |
| 形式模型 `M` | 级数收敛、连续 path、微积分与点事件 | partial sums、连续时刻、逐个动作时间分配 | `SOURCE_ESTABLISHED` |
| `Done_formal` | 目标在有限时间被达到；系列之和为 1；不要求最后一步 | 每个指定动作都有发生时间；所有动作完成 | `SOURCE_ESTABLISHED` |
| 严格过程 Done | “完成全部动作，包括最后一个”这一有限任务式条件 | 同左，Norton 明确称它为 stricter notion | `SOURCE_ESTABLISHED` |
| `OriginDone` 是否被同一来源证明 | IEP 称标准解法为解答，但同时拒绝“需要最后一步”的直觉 | Norton 明示解法删除“包括最后动作”要求 | `SOURCE_REFUTED` 对“严格 Done 已由桥保持”的读法 |
| `Bridge : Done_formal → Done_strict` | 未给出 | 未给出；Norton 的写法反而说明 strict 条件被删去 | `SOURCE_REFUTED` 对本卡的 strict bridge |
| 来源判词 | 可称为标准／间接解答，但完成条件为不需要最后一步 | `revisedResolved`：删去最后动作要求后，矛盾不再推出 | `SOURCE_ESTABLISHED` |

## 3. 本卡的形式化输入

本项目将以下两个完成谓词分开，而不以自然语言“完成”合并它们：

```text
StrictCompletion  = 做完全部指定动作，并且有最后动作。
RevisedCompletion = 每个指定动作都已做完；不要求不存在的最后动作。
```

这不是对所有 Zeno 解读的唯一形式化。它是 Norton 在该版本页面中明确给出的收紧／缩减合同，并用来测试当前来源是否能支付 C-359 的强 P。

允许进入机器化的来源认证前提是：

```text
NORTON_CLASSIFIED_AS_REVISED_RESOLUTION
IEP_CLASSIFIED_AS_STANDARD_RESOLUTION_WITH_NO_LAST_STEP
NO_SOURCE_BRIDGE_FROM_REVISED_TO_STRICT_IN_THIS_DENOMINATOR
```

它们是 `SOURCE_CERTIFIED_PREMISES`，不被 Lean、Agda 或本卡文字本身升级成历史真理。

## 4. A2 的判词

```text
SOURCE_TASK_CONTRACT_DIVERGENCE_ESTABLISHED_WITH_SCOPE
P_STRICT_SOURCE_ADMISSION_REFUTED_WITH_SCOPE
ACTUAL_POLICY_OWNER_FOR_HOTT_SIDE = SOURCE_UNOBSERVED
```

这一判词有两层：

1. 对固定 IEP/Norton 分母，来源确实显示一种 ZFC 支撑连续统标准解法在**改写完成合同**后取得“解答”判词；因此它是用户所说 P 的较准确来源级形状，命名为 `ResolutionByRevision`。
2. 同一来源**没有**支付 `RevisedCompletion → StrictCompletion`。因此它不能充当 C-359 中更强 `formalDone → originDone` 的来源实例，也不能单靠“解答”一词填入 `A ↔ P` 或 `SameFullQ`。

它不能支持：

- bare ZFC 内部矛盾；
- “所有数学家”采取同一政策；
- 原用户圆环任务已经被本卡完全冻结；
- HoTT Q 与 Zeno 已是同一完整实际 Q；
- 历史来源自身承认其解法不合理。

## 5. 对收尾路线的影响

这张卡使 A2 不再开放搜索。对这一来源分母，强 P 的直接来源支付已经失败；可以继续的是更准确的收敛问题：

```text
一个基础性解答政策是否可以把 RevisedCompletion 称为原问题的 resolution，
却不提供 RevisedCompletion 与 OriginDone 的同一任务支付？
```

后续 C-362／C-363 只能机器证明该**完成合同发散形状**及它与 HoTT coarse-completion 控制的共同抽象结构；它们不得把“共同形状”冒充 `SameFullQ`。
