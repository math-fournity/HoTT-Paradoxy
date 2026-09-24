# CG-001 / C1「实数的测量记录」正控制包

> HUMAN_EDITED；2026-09-24；Claude（Opus 5.5），CG-001 执行会话 bb204ea1。
> proof id：`MP-CG001-MEASUREMENT-LOG-001`；claim：`CG001-C-08`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设。可数选择只以显式假设 `ACω` 出现，从不公设。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md`（GOAL_LOCAL_INDEX_ONLY）；共享矩阵行只以草稿写在该目标的 `relay.md`。

## 这个包证明什么、不证明什么

本包只检查 C1 候选卡里的**正控制**：真实的有限测量任务在 HoTT 中可以完成。数学内容是有限选择（cubical 库 `Cubical.Data.FinData.FiniteChoice.choice`）的直接应用，外加两条平凡的对照，**不主张原创**。

cubical 0.9 没有 Book 第 11 章的 HIIT Cauchy 实数 ℝ_c，所以命题对任意类型 `U` 与任意读数关系 `Reads` 泛化。取 `Reads n u q :≡ u ∼_{2⁻ⁿ} rat(q)` 并由阿基米德性质得到“每个精度都有读数”，这一步来自 Book reals（定理 RC-archimedean，L1529–1536），是**来源报告**，未在本包重放。

C1 的关键否定方向（不加可数选择时，整条无穷记录是否取不到）**不在本包内**。它需要反模型；Book 只用模态词说 ℝ_c “may not be a quotient of the set of Cauchy sequences of rationals”（reals L937）。本目标把它登记为猜想 / 来源报告，不作为数学结论交付。

## 命题全文

记号：`ℓ ℓ'` 为任意宇宙层级；`Fin N` 为 cubical 0.9 的 `Cubical.Data.FinData.Base.Fin`，`toℕ` 为其到 ℕ 的映射；`ℚ` 为 `Cubical.Data.Rationals.Base.ℚ`；`∥_∥₁` 为命题截断。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-08** | 对任意 `U : Type ℓ`、`Reads : ℕ → U → ℚ → Type ℓ'`、`u : U`，记 `EachPrecision :≡ (n : ℕ) → ∥ Σ ℚ (Reads n u) ∥₁`、`FiniteLog N :≡ (i : Fin N) → Σ ℚ (Reads (toℕ i) u)`、`InfiniteLog :≡ (n : ℕ) → Σ ℚ (Reads n u)`：(i) `EachPrecision → (N : ℕ) → ∥ FiniteLog N ∥₁`；(ii) `InfiniteLog → (N : ℕ) → FiniteLog N`（截取）；(iii) 记 `ACω ℓ' :≡ (P : ℕ → Type ℓ') → ((n : ℕ) → ∥ P n ∥₁) → ∥ ((n : ℕ) → P n) ∥₁`，则 `ACω ℓ' → EachPrecision → ∥ InfiniteLog ∥₁`；(iv) 对任意 `s : ℕ → ℚ` 与 `r : (n : ℕ) → Reads n u (s n)`，`InfiniteLog` 成立（值为 `λ n → (s n , r n)`），且 `EachPrecision` 成立。 | `EachPrecision`、`FiniteLog`、`InfiniteLog`、`finiteLogAvailable`、`restrict`、`ACω`、`infiniteLogFromChoice`、`carriedApproximationGivesLog`、`carriedApproximationGivesEachPrecision` |

## 禁止外推

- 不证明、也不否定“没有可数选择时 ℝ_c 的无穷测量记录取不到”；(iii) 只说明可数选择足够，不说明它必要。
- 不涉及 Book 的 HIIT 实数本身；到 ℝ_c 的实例化依赖来源报告的阿基米德性质。
- (iv) 是 setoid 式表示的平凡正控制，不说明 setoid 表示与 ℝ_c 等价。
- 不证明任何物理测量事实；“读数”“记录”“精度”是解释标签，对应的现实任务与桥梁见 CG-001 工作台 §4.2。
