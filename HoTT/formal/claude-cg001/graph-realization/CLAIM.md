# A1 延伸：实现的价格（从“离散状态 + 相邻关系”到 HoTT 空间）

> HUMAN_EDITED；2026-09-24；Claude（Opus 5.5），会话 6fd0312a（用户指令“把下一步的工作都做了”）。
> proof id：`MP-CG001-GRAPH-REALIZATION-001`（主包）、`MP-CG001-GRAPH-REALIZATION-NEG-001`（负控制）；claims：`CG001-C-19`、`CG001-C-20`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §6（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`；解释见 `.claude/思考与发现/CN-017 - 实现的价格：困难恰好出在相邻即相同这一步.md`。

## 这个包为什么存在

它回答交接文档 §3 留给用户的第 3 问：按用户的量子化现实观，运动是一串离散状态；困难是否只来自把运动写成“同一”的那一步？

一个图（状态集 V，相邻关系 E）就是离散运动的骨架：状态彼此不同，相邻关系说明哪一步能走到哪里。HoTT 用“点加路径”造空间的做法（HIT），就是把这个图**实现**出来：每一步都变成一条恒等路径。本包证明这一步的精确价格：实现之后，集合值读数恰好只剩“沿每一步都不变”的那些；相邻状态之间放不下任何严格关系，也放不下任何在对角线上为零的集合值距离。C-05 是这个一般定理在四个位置上的特例。

数学内容是高阶归纳类型递归原理在集合值目标上的标准形态，**不主张原创**。“状态”“一步”“高度”是解释标签，本包不证明任何物理事实，不证明 HoTT 不一致。

## 命题全文

记号：对任意 `V : Type ℓ`、`E : V → V → Type ℓ'`，`Realize V E` 是由点构造子 `vtx : V → Realize V E` 与路径构造子 `edge : (x y : V) → E x y → vtx x ≡ vtx y` 生成的 HIT；`EdgeInvariant V E P :≡ Σ[ f ∈ (V → P) ] ((x y : V) → E x y → f x ≡ f y)`。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-19**（实现的价格） | 对任意 `V`、`E` 与集合 `P`：`Iso (Realize V E → P) (EdgeInvariant V E P)`，正向是限制到 `vtx`，逆向是按构造子延拓。对任意非自反关系 `R` 于 `Realize V E`，以及任意 `x y` 与 `e : E x y`：`¬ R (vtx x) (vtx y)`。对任意 `P`、`d : Realize V E → Realize V E → P`、`o : P`：若 `∀ z → d z z ≡ o`，则对任意 `x y` 与 `e : E x y`，`d (vtx x) (vtx y) ≡ o`。 | `Realize`、`EdgeInvariant`、`Readings.{restrictReading, extendReading, back, price}`、`orderLostAfterRealization`、`distanceLostAfterRealization` |
| **CG001-C-20**（四位置环的实例） | 对四个位置 `Place`、`next`（p0→p1→p2→p3→p0）、`Step x y :≡ (next x ≡ y)`、`height`（0,1,2,1）：`¬ (p0 ≡ p1)`；`Step p0 p1`，且 `¬ (height p0 ≡ height p1)`；`height` 不沿每一步不变；不存在 `g : Realize Place Step → ℕ` 使 `∀ v → g (vtx v) ≡ height v`；任何沿每一步不变的读数在四个位置取同一个值（给出三段相等）。负控制：把每一步送到“起点高度”的定义 `realizedHeight` 应被内核拒绝。 | `Place`、`next`、`Step`、`height`、`statesDistinct`、`heightChangesAlongStep`、`heightNotEdgeInvariant`、`Ring`、`noHeightOnRealizedRing`、`edgeInvariantIsConstant`；负控制 `WrongRealizedHeight.agda` |

## 禁止外推

- C-19 只说集合值读数、非自反关系与集合值两点函数；取值于高阶类型的读数（例如取值于宇宙的族）不受此限，那正是 C-06、C-11 所说“变化只剩预写的改名”的地方。
- C-19 的 `Realize` 只有点和一维路径构造子；对带二维以上构造子的 HIT，本包没有直接陈述（对集合值读数，高维构造子不增加约束，但本包未证明这一点）。
- C-20 只涉及四个位置的环；不说任何物理轨道。
- 本包不说 HoTT 不能表示离散运动：图本身（`V` 加关系 `E`，不做实现）就是 HoTT 中合法的对象，读数在上面可以随意变化（`heightChangesAlongStep`）。本包说的是：一旦用 HIT 把相邻当成相同，价格就是全部沿边变化的读数。
