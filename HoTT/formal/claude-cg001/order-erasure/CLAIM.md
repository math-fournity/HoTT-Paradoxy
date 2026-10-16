# 补丁律写成路径以后：历史只保留次数，不保留次序

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：Terra 复审 007 §4.2 说，可以保留 HoTT 的路径与群胚律，同时把计数与日志任务交给历史（trace）这一层。本包检验补丁理论自己的历史层在补丁律写成路径之后还保留什么。讨论见 CN-028 与回信 008。
>
> - proof id：`MP-CG001-ORDER-ERASURE-001`（主包）、`MP-CG001-ORDER-ERASURE-NEG-001`（负控制）。
> - claim：`CG001-C-48`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`。源码选项 `--safe --cubical --guardedness`，无公设，不加公理，零警告。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §11（GOAL_LOCAL_INDEX_ONLY）。

## 来源【来源，转述】

Angiuli、Morehouse、Licata、Harper，*Homotopical patch theory*，J. Funct. Program. 26 (2016)，DOI `10.1017/S0956796816000198`，§7.1–§7.2，第 28–30 页（经 sciverse 全文库读）。要点：

- 上下文以布尔列表为索引时，历史记录了补丁执行的确切顺序，因此无法把两个不同顺序的补丁序列认同。
- 要把“补丁可交换”写成路径之间的路径，作者把列表按相邻交换取商，得到多重集 MS，并以 MS 为上下文索引。
- 作者注明：MS 的元素仍保留补丁执行顺序的显式日志，但 MS 中的路径把只差一个置换的日志认同了。

## 命题全文

量词与假设照实写。设 `MS` 是布尔列表按相邻交换取商的高阶归纳类型：
- 构造子 `[]ms`、`_∷ms_`；
- 路径构造子 `ex x y xs : x ∷ms (y ∷ms xs) ≡ y ∷ms (x ∷ms xs)`；
- `fromList : List Bool → MS`。

| 部分 | 命题 | 源码符号 |
|---|---|---|
| (a) 次数经得起取商 | 存在 `size : MS → ℕ`，对一切列表 `xs`，`size (fromList xs) ≡ length xs` | `size`、`sizeIsLength` |
| (b) 次序经不起 | 不存在 `f : MS → Maybe Bool`，使对一切列表 `xs`，`f (fromList xs) ≡ firstOf xs`（`firstOf` 取列表第一项） | `orderErased` |
| (c) 正控制：日志作为数据 | 在列表上 `firstOf` 有定义，且 `¬ (firstOf (true ∷ false ∷ []) ≡ firstOf (false ∷ true ∷ []))`；而在 MS 中 `fromList (true ∷ false ∷ []) ≡ fromList (false ∷ true ∷ [])` | `dataLogKeepsOrder`、`logsIdentified` |
| 负控制 | 在 MS 上按构造子直接定义“第一项”，内核拒绝（`just true` 与 `just false` 须相等） | `WrongFirstEntry.agda` |

## 解读【解释】

Terra 说，计数和日志可以交给历史这一层。补丁理论自己的历史层就是上下文的索引，它在高阶归纳类型之内。一旦把补丁律写成路径，这一层也要跟着被认同。可交换律一加，日志还能数出执行了几次，却说不出哪一个先执行。

要保住带次序的日志，它就得放在路径结构之外，当作普通数据保存（C-41 的列表、Terra 的台账）。

作者的注释与此一致：元素里还有次序，路径却把它认同掉了。这是 KC-000011 所说“思考过程不想让时序参与”的一个补丁理论实例。

## 禁止外推

- 对可交换的补丁，认同不同次序是作者按 Darcs 语义**有意**做的：仓库状态本来就不依赖这些补丁的次序。本包不说这一语义错误。本包只说，写成路径的历史层随之失去了次序，现实的日志（`git log`、`darcs log`）仍然显示次序。
- 本包的 MS 没有作集合截断，结论在截断版本上同样成立，但本包未单独证明。
- 数学内容是标准事实，**不主张原创**。
- “历史”“日志”“先执行”是解释标签。
