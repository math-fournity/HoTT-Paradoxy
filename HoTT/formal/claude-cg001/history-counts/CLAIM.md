# 历史索引就是它的计数：JFP §7.2 同一段里的两句话（C-54）

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：Terra 复审 009 的 O-026 说，C-48 的摘要“历史只保留次数、不保留次序”错误，理由是 JFP 2016 §7.2 明说 MS 的元素保存了应用次序的显式日志。回源核对（经 sciverse 全文，第 30 页，偏移约 84312）：同一段里，作者**先**说 replay 算出的 Nat × Nat 表示“实际上与 MS 同构”，**再**说 MS 的元素保存显式日志、而 MS 中的路径认同只差置换的日志，最后说 Nat × Nat 表示“根本不保存”这种日志。本包把这两句话都证出来，并说明它们各自在哪一层成立。讨论见 CN-030 与回信 012。
>
> - proof id：`MP-CG001-HISTORY-COUNTS-001`（主包）、`MP-CG001-HISTORY-COUNTS-NEG-001`（负控制）。
> - claim：`CG001-C-54`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9（`HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`），`--safe --cubical --guardedness`，无公设，不加公理，零警告。多重集用 cubical 库的 `FMSet`：带交换律 `comm`，并做集合截断，即商高阶归纳类型。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §13（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文

- **(a) 历史索引等价于计数**：
  - `historyIsCounts : FMSet Bool ≃ ℕ × ℕ`，映射是 `counts`（`true` 与 `false` 各出现几次），逆映射是 `build`（先放全部 `true`，再放全部 `false`）；
  - 由单价性，`historyIsCountsPath : FMSet Bool ≡ ℕ × ℕ`。
  - 证明用到库中的计数外延性 `FMScountExt.Thm`：各元素计数相等的两个多重集相等。
- **(b) 一切观察都经由计数**：`factorsThroughCounts`：对任意类型 `X` 与任意函数 `g : FMSet Bool → X`，都有 `g xs ≡ g (build (counts xs))`。
- **(c) 没有“第一项”**：`noFirstEntry`：不存在 `f : FMSet Bool → Maybe Bool`，使得对每个列表 `xs`，`f (fromList xs) ≡ firstOf xs`。这是 C-48 (b) 在集合截断版本上的对应。
- **(d) 两种写法，一个元素**：
  - `presentationsAreOneElement : trueFirst ≡ falseFirst`（由 `comm`）；
  - `presentationsHaveTheSameCounts`（`refl`）；
  - `canonicalPresentation : build (counts falseFirst) ≡ trueFirst`（`refl`，即计数后按规范写法重建）。
- **负控制**：`WrongPresentationsDefinitional.agda` 以 `refl` 断言两种写法相同，被拒：`true != false`。内核在定义层面把两种写法分开。

## 解读【解释】

- JFP 那一段的两句话都对，但在不同的层：
  - **类型层**：MS 等价于、从而（单价性）等于 ℕ × ℕ，一切函数都只看计数（(a)(b)）。在这一层，历史只保留次数。
  - **写法层**：两种写法是两个不同的项，内核在定义层面分得开（负控制）；作者所说的“显式日志”就在这里。按 (b)，没有任何函数能读出它。这与期刊版 §10 的说法一致：命题相等而计算不同的项，理论内部没有谓词能区分。
- 所以对 O-026 的精确答复是：
  - “历史层**在类型内部**只保留次数”成立（本包 (a)(b)），作者自己也说了同构；
  - “历史层在任何意义上都不保存次序”不成立，写法层保存次序；
  - “凡进入认同结构的都失去时间”是由三个例子外推的口号，撤回。
- C-48 用的多重集没有做集合截断，所以不等价于 ℕ × ℕ；但 C-48 (b) 的“没有第一项”对它照样成立。本包补上 JFP 所用的截断版本。

## 禁止外推

- 不涉及任何版本控制系统的实际日志，也不涉及现实中的时间次序记录。
- 不说补丁理论的交换语义错误：对可交换的补丁，认同不同次序是作者按 Darcs 语义有意为之。
- 数学内容是标准事实（有限多重集与计数），**不主张原创**；“同构于 Nat × Nat”是 JFP 作者的原话，本包只是把它机器证明出来。
