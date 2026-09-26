# 相同有几层，相干就补几层：机器证明的三个实例（C-70）

> HUMAN_EDITED；2026-09-26；Claude（Opus 5.5），会话 7f138325；目标包 CG-003，完成门 G3。与 C-64、C-66、C-68 同包。
>
> - proof id：`MP-CG001-WILD-SST-LEVELS-001`（`WildSSTP4Levels.agda`，导入 `WildSSTP4.agda`）。
> - 负控制：`MP-CG001-WILD-SST-LEVELS-NEG-001`（`WrongS2Groupoid.agda`）。
> - claim：`CG001-C-70`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §17（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`WildSSTP4Levels.agda`）

- **(a) 集合**：`setsCohereᵢ`，各层都是集合时 `Coh₂ᵢ` 成立。
- **(b) 群胚**：
  - `coh₂IsProp`：各层都是群胚时，`Coh₂ᵢ` 是命题（六边形数据若存在就唯一）；
  - `groupoidsCohere₃`：各层都是群胚时，对任何六边形数据 `Coh₃` 都成立。
- **(c) 圆周上的 flat 形状**（0 维为 S¹ 的点，更高维为 Unit）：
  - `flatS¹-unique`：任意两个六边形数据相等；
  - `flatS¹-coh₃`：每一个都满足 `Coh₃`。

## 与已有结果合成的表

| 各层的类型 | 六边形相干 `Coh₂` | 第二级相干 `Coh₃` |
|---|---|---|
| 集合 | 自动成立（C-64 `setsCohere`；本包 (a)） | 自动成立（集合是群胚，本包 (b)） |
| 群胚（如 S¹） | 是命题，可以失败（C-64 `spin`；C-69） | 自动成立（本包 (b)、(c)） |
| S²（π₂ 非零，不是群胚） | 数据不唯一（C-66 `twoFillings`） | 可以失败（C-68 `notCoh₃`），也可以满足（C-68 `coh₃Trivial`） |

## 这件事说明什么（解释）

- 【解释】要补的相干层数，恰好随“相同”的层数增加：相同只有事实一层（集合），一步就完成；多一层（群胚），要补六边形，然后停止；再多一层（S² 有非平凡的二维相同），第二级也要补，而且可能补不上。
- 【解释】一般的规律是：各层是 t-类型时，补到第 t+1 级相干即可，更高级自动成立；第 t+1 级是命题。这是关于 h-层级的元层论证：在 t-类型中，k 级路径构成 (t−k)-类型。本包只证明 t = 0、1 两个实例，以及 S² 的反例。
- 【解释】为什么不证一般的 t：“第 n 级相干”对变量 n 本身就写不出统一的形式，这正是开放问题所在。能对每个固定的 t 写出，正对应“每一有限层都做得到”。
- 【解释】单价宇宙里的“相同”没有有限的层数上限：宇宙不是集合（C-63），而且单价性还使集合的宇宙也不是集合（C-71）。所以在 HoTT 自己的宇宙上，这个补法停不下来。

## 禁止外推

- 一般的“t+1 规律”没有机器证明，是元层论证。
- 不证明半单纯类型不可定义。
- (b) 需要各层都是群胚这一假设；负控制表明这个假设不能挪到 S² 上去用。

## 负控制

`WrongS2Groupoid.agda` 在 S² 上的 flat 形状中，用圆周的群胚证明代替缺失的 S² 的证明，以此套用 `groupoidsCohere₃`。预期被拒：`S² !=< S¹`。

## 运行

- 主包：`HoTT/verification/runs/20260926-CG001-WILD-SST-LEVELS-01`。
- 负控制：`HoTT/verification/runs/20260926-CG001-WILD-SST-LEVELS-NEG-01`。
