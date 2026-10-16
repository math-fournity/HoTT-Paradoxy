# 路径观察者的边界：固定端点能看见净变化，统一的观察不能

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。起因：Terra 复审 007（`Terra对Opus的审计/007 - Terra 对 Opus 006 的复审：CG-001.md`）的 O-019。Terra 指出 `winding : ΩS¹ → ℤ` 是理论内部、以固定基点环路为输入、能分开 `loop` 与 `refl` 的函数，所以 C-44 不能被读成“被认同类型上的一切观察都看不见”。本包固定两者的分界。讨论见 CN-028 与回信 008。
> proof id：`MP-CG001-PATH-OBSERVERS-001`（主包）、`MP-CG001-PATH-OBSERVERS-NEG-001`（负控制）；claim：`CG001-C-46`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理；零警告。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §11（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文

| 部分 | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| (a) 固定端点的观察能看见净变化 | `¬ (winding loop ≡ winding refl)` | `windingSeesLoop` |
| (b) 但不能做成对端点统一的观察 | 不存在 `t : (a b : S¹) → a ≡ b → ℤ`，使对一切 `q : ΩS¹` 有 `t base base q ≡ winding q`（用 C-44 (a) 的 `transitionBlind`，在本文件内重证） | `windingNotUniform` |
| (c) 可缩类型上，固定端点的观察也看不见 | 对任意可缩类型 `C`、任意类型 `B`、任意 `a b : C`、任意 `f : a ≡ b → B`、任意 `p q : a ≡ b`，有 `f p ≡ f q` | `contractiblePathBlind` |
| (d) 补丁理论历史索引的上下文 | 以 `hdoc : List Bool → HistCtx`、`hadd b h : hdoc h ≡ hdoc (b ∷ h)` 定义的上下文 HIT 可缩（与 C-31 同一构造，本文件内重证）；因此任意两个上下文之间补丁上的任何观察 `f : x ≡ y → B` 都是常值；特例：对任意 `f : hdoc [] ≡ hdoc [] → B`，`f (hadd true [] ∙ sym (hadd true [])) ≡ f refl` | `isContrHistCtx`、`patchObserverBlind`、`noUndoDetector` |
| 负控制 | 以 `refl` 断言 `winding loop ≡ winding refl`，内核拒绝（`1 != 0`） | `WrongWindingEqual.agda` |

## 解读【解释】

- C-44 (a) 的边界是**对端点统一**的观察：它对每次编辑的回答等于对同一起点空编辑的回答。`winding` 不是这种观察。它固定了两端，只作用于同一基点上的环路，所以能看见一圈的净效果（C-40 已说：可加的计数只能数净位移）。
- 在补丁理论的最终设计里，上下文空间可缩，任意两个上下文之间的补丁空间也可缩，所以连固定端点的观察也不存在非常值的，“加一行再撤回”与“什么都不做”对理论内部的任何观察都一样（d）。这比 C-44 更强，但**只限于可缩设计**。
- 所以 C-44 的准确名称是 Terra 建议的 `FORMAL_UNIFORM_PATH_ELIMINATION_BOUNDARY_WITH_SCOPE`；对补丁理论的可缩设计，另有 (c)、(d) 这条更强的边界。

## 禁止外推

- 不说理论内部一切路径观察都看不见：(a) 正是反例。
- (d) 只对可缩的上下文类型成立，不外推到圆等非可缩类型。
- 数学内容是标准事实（`winding`、路径归纳、可缩类型是集合），**不主张原创**。
- “编辑”“撤回”“观察”是解释标签，不说明任何版本控制系统的事实。
