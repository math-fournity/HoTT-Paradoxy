# 有理点圆：复原那一步不需要任何原则

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。起因：CN-024 把用户圆环的“稠密性”归因收窄为“点的相等不可判定”；本包检验其中一半：有理数同样稠密，但相等可判定，复原所需的那一步能否无原则地完成。讨论见 `.claude/思考与发现/CN-024 - 圆环复原与 Markov 原则：复原撞上一条停机原则.md`。
> proof id：`MP-CG001-RATIONAL-LIFT-001`（主包）、`MP-CG001-RATIONAL-LIFT-NEG-001`（负控制）；claim：`CG001-C-43`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理；零警告。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §9（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`。

## 这个包为什么存在

单位圆去掉点 (−1, 0) 以后，剩下的点 (x, y) 可以用球极投影的参数 t 复原：t 满足 (1 + x)·t = y。要算出 t，就得在只知道“x 不是 −1”的情况下把 1 + x 倒过来。

- 在有理数里，这一步是免费的：有理数的相等可判定，非零即可逆（库定理 `hasInverseℚ`）。本包证明：x ≠ −1 蕴含 1 + x ≠ 0，从而复原参数 t 存在。
- 在 Dedekind 实数里，同一步对应“不等于 0 推出与 0 隔开”（`RealNonzeroApartness`）；Astra 的 C-319、C-322 把它连到固定复原映射的提升与 Markov 原则上（共享矩阵，本会话已重放 C-322、C-324）。

所以，有理数与实数一样稠密，差别只在点的相等是否可判定。这把用户“稠密性”怀疑的落点，收窄到“点由无尽逼近给出、相等不可判定”这一面。

数学内容是标准事实，**不主张原创**。

## 命题全文

记号：`ℚ` 取 cubical 0.9 的 `Cubical.Data.Rationals.MoreRationals.QuoQ`；环结构 `ℚCommRing`（`0r`、`1r`、`_+_`、`_·_`、`-_`）；`hasInverseℚ : (q : ℚ) → ¬ q ≡ 0 → Σ[ p ∈ ℚ ] q · p ≡ 1`（`Cubical.Algebra.Field.Instances.Rationals`）。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-43**（有理点圆的复原参数） | 对任意 `x : ℚ`：`¬ (x ≡ - 1r) → ¬ (1r + x ≡ 0r)`；对任意 `x y : ℚ`：`¬ (x ≡ - 1r) → Σ[ t ∈ ℚ ] (1r + x) · t ≡ y`。负控制：以 `refl` 断言 `0r · 0r ≡ 1r`（缺口处的“逆”），内核拒绝（`0 != 1`）。 | `awayFromGap`、`restoreParameter`；负控制 `WrongGapInverse.agda` |

## 禁止外推

- 只证明复原所需的那一步（由 x ≠ −1 求出参数 t）；没有证明球极投影把 t 映回 (x, y)，也没有证明整个有理点圆的复原是双射。
- 不涉及实数；实数一侧的证据是 Astra 的 C-319、C-322、C-324 与 CN-024 的来源。
- “圆”“缺口”“参数”“复原”是解释标签；不说任何物理事实。
