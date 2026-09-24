# CG-001 / I1「逐层一致推不出整体相同」正控制包

> HUMAN_EDITED；2026-09-24；Claude（Opus 5.5），CG-001 执行会话 bb204ea1。
> proof id：`MP-CG001-LEVEL-COMPARISON-001`；claim：`CG001-C-09`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不假设 Whitehead 原则。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md`（GOAL_LOCAL_INDEX_ONLY）；共享矩阵行只以草稿写在该目标的 `relay.md`。

## 这个包证明什么、不证明什么

本包检查 I1 候选卡的两条**正控制**，说明现实中那种有限的比较在 HoTT 里可以完成。

- (i) 是 cubical 库的 `WhiteheadsLemma`（库注释：Book 定理 8.8.3）换名重述，不是新证明。
- (ii) `sphereSection` 是本包写的短证明，内容是连通性的标准论证，**不主张原创**。它是“有限个胞腔搭成的形状只需检查有限层”这一 AI 推导的核心一步：填一个胞腔时，只用到有限层的连通性。

不证明：
- Whitehead 原则对一切类型成立或不成立。Book homotopy L2353 报告它不可证，L2363 报告它可相容加回；这些是**来源报告**。
- 有限 CW 复形之间的 Whitehead 定理。它的推导写在 CG-001 工作台 §4.3，身份是猜想（AI 推导），本包只机器检查其中填胞腔的一步。

## 命题全文

记号：
- `isOfHLevel n`：cubical 的 h-层级（0 可缩，1 命题，2 集合，…）。
- `isConnected n A :≡ isContr (hLevelTrunc n A)`：cubical 的连通度，等于 Book 的 (n−2)-连通。
- `S : ℕ₋₁ → Type`：cubical `Cubical.HITs.Sn.Base` 的球面，`S (-1+ 0) = ⊥`，`S (-1+ (suc n)) = Susp (S (-1+ n))`。所以 `S (-1+ n)` 是 (n−1) 维球面，也就是 n 维胞腔的边界。
- `setMap f`：f 在集合截断（连通分支）上的作用。
- `πHom k`：f 在第 k+1 个同伦群上的群同态。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-09** | (i) 对任意 `ℓ`、`A B : Type ℓ`、`n : ℕ`：若 `isOfHLevel n A`、`isOfHLevel n B`，`f : A → B`，`isEquiv (setMap f)`，且对一切 `a : A`、`k : ℕ`，`πHom k (f , refl)`（在基点 a 处）的底层函数是等价，则 `isEquiv f`。(ii) 对任意 `ℓ`、`n : ℕ`、`P : S (-1+ n) → Type ℓ`：若对一切 `x`，`isConnected n (P x)`，则 `∥ ((x : S (-1+ n)) → P x) ∥₁`。 | `finiteLevelComparison`（= 库 `WhiteheadsLemma`）、`sphereSection` |

## 禁止外推

- 不证明 Whitehead 原则对一切类型不可证或可证；不涉及任何非超完备模型。
- (ii) 不是有限 CW 复形的 Whitehead 定理，只是其中填胞腔的一步。
- (i) 的假设对一切 k 量化。n-type 的高阶同伦群平凡，所以实际只需有限层；“高阶同伦群平凡”这一步来自 Book，是来源报告，本包未重放。
- “形状”“逐层比较”“胞腔”是解释标签；对应的现实任务与桥梁见 CG-001 工作台 §4.3。
