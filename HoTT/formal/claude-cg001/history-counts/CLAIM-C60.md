# C-54 与同伦补丁理论原始 `MS` 的对应：作者的 `MS` 不是集合，截断后才等于计数（C-60，Cubical Agda）

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：Terra 复审 013 §2.2 第 3 条：C-54 用的是 cubical 库中带集合截断的 `FMSet`，没有本地证明它就是 HPT（Angiuli–Morehouse–Licata–Harper，JFP 2016，§7）的 `MS`；论文的“isomorphic”是强来源支持，但不是本地的精确定义重放。
>
> **回源**：论文第 7 节脚注 7 指向作者的 Agda 代码 `dlicata335/hott-agda`，分支 `homotopical-patch-theory-paper`，文件 `programming/PatchWithHistories.agda`（2026-09-25 以浏览器只读查看，未下载）。其 `module HistoryHIT` 里：
> - `MS` 的点构造子只有两个：空历史 `[]ms`、前置一个布尔值 `_::ms_`；
> - 路径构造子只有一个，由 postulate 给出：`Ex : (x y : Bool) (xs : MS) → (x ::ms (y ::ms xs)) == (y ::ms (x ::ms xs))`；
> - 消去子 `MS-ind` 只有这三种情形，另 postulate 其对 `Ex` 的 β 规则；
> - 全文件只有三处 postulate（`Ex`、`MS-ind/βEx`、补丁理论 `R` 本身），没有集合截断，也没有更高的构造子。
>
> 论文 §7.1 正文中的定义块不在我可用的解析文本里（该处只有“defined as the following quotient higher inductive type:”一句），所以本包按作者代码逐构造子重建。
>
> - proof id：`MP-CG001-HPT-MULTISET-001`（主包）、`MP-CG001-HPT-MULTISET-NEG-001`（负控制）。
> - claim：`CG001-C-60`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9（`HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`），`--safe --cubical --guardedness`，无公设。`HistoryCounts.agda`（C-54）作为依赖进入源码清单。
> - 标签：`FORMAL_FIDELITY_CORRECTION_WITH_SCOPE`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §14（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`HPTMultisetFidelity.agda`）

`MS` 在这里是 cubical 高阶归纳类型，构造子与作者代码一一对应：`[]ms`、`_∷ms_`、`Ex`。

- **(a) `MS` 不是集合**：`loopIsNotRefl`：环 `Ex true true []` 不等于 `refl`；`msIsNotASet`。证法：族 `Code` 沿以 `true` 开头的交换运输为交换前两项、沿以 `false` 开头的交换运输为恒等（`ua`），沿该环运输会移动 `(true, false, tt)`。
- **(b) `MS` 不等价于 ℕ × ℕ**：`msIsNotCounts`，因为 ℕ × ℕ 是集合。所以 JFP §7.2 “Nat × Nat 表示实际上与 MS 同构”一句，对作者定义的 `MS` 只在集合截断（路径连通分支）的层面成立。
- **(c) 截断后等于计数**：`msTruncIsFMSet : ∥ MS ∥₂ ≃ FMSet Bool`，`msTruncIsCounts : ∥ MS ∥₂ ≃ ℕ × ℕ`（接 C-54）。C-54 是关于 `∥ MS ∥₂` 的定理。
- **(d) 没有“第一项”**：`noFirstEntryMS`：没有函数 `MS → Maybe Bool` 对每个历史返回其第一项。这对任意函数成立，不只对集合层的函数，因为 `Ex` 本身是路径。
- **(e) 集合值的观察经由计数**：`factorsThroughCountsMS`：到集合的函数 `g` 满足 `g m ≡ ĝ (build (counts (toFMS m)))`，其中 `ĝ` 为 `g` 在截断上的延拓。
- **(f) 交换再换回不是“什么也没做”**：`exchangeBackIsNotRefl`：`Ex true false [] ∙ Ex false true []` 不等于 `refl`。
- **负控制**（`WrongFirstEntryMS.agda`）：按构造子逐项定义“第一项”，在 `Ex x y xs` 一格填常值 `just x`，被拒：`y != x of type Bool … the terms just y and just x must be equal, since firstEntry (Ex x y xs i1) could reduce to either`。

## 解读【解释】

- **对 012 的更正**：012 §3.2 写“C-54 把它（作者的同构）证了出来”。这读过了头。作者的 `MS` 没有截断，不是集合，不等价于 ℕ × ℕ；C-54 证的是它的集合截断。论文的“isomorphic”在路径连通分支的层面成立。
- **O-026 的结论不受影响，而且在精确类型上重新成立**：在作者自己的 `MS` 上，没有任何函数读得出第一项（(d)）；到集合的观察都经由计数（(e)）。
- **新看到的一层**：作者的 `MS` 比计数多出的东西在路径里。交换是自由的路径，换过去再换回来不等于不动（(f)），环 `Ex x x xs` 也非平凡（(a)）。点忘掉的次序，以“两种写法之间走过哪些交换”的形式留在上一层；集合截断把这一层也抹掉。这与 CN-007 所说的“历史上移了一层”同形。它说的是写法之间的交换历史，不是补丁的应用历史。
- 这支持 Terra 的三层表述（写法与显式日志、由 `Ex` 给出的置换路径、集合层观察经由计数），并给中间一层补上了一个精确事实：在作者的定义里，置换路径不满足任何律。

## 禁止外推

- 重建依据作者代码（HoTT-Agda 风格：postulate 路径与 β 规则），本包是 cubical 的同构造子翻译，没有机器证明两个证明系统之间的翻译保真。
- 论文正文 §7.1 的定义块未能读到；若论文正文另加了截断，(b) 的结论只针对作者代码中的 `MS`。
- (f) 只说明这一个环非平凡，不计算 `MS` 的基本群。
- 数学内容标准，**不主张原创**。
