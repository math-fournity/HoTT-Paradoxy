# A1 延伸：合成时间没有先后也没有方向；有向出路的价格（模型）

> HUMAN_EDITED；2026-09-24；Claude（Opus 5.5），会话 6fd0312a（用户指令“把下一步的工作都做了”）。
> proof id：`MP-CG001-TIME-DIRECTION-001`（主包）、`MP-CG001-TIME-DIRECTION-NEG-001`（负控制）；claims：`CG001-C-23`、`CG001-C-24`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §6（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`；解释见 `.claude/思考与发现/CN-019 - 时序在合成空间里无处安放，有向出路只买回了钟.md`。

## 这个包为什么存在

它服务于用户的时间怀疑【原话，KC-000011：“就是看它什么时候，不想让时间、时序参与到Think in HoTT这件事中”】，以及交接文档 §3 的第 4 问。它回答两件事。

第一，如果把时间当作 HoTT 的合成空间，时序能不能住进去？不能。时序不能住在点上：连在一起的两刻之间放不下严格的“先于”。时序也不能住在路上：每条路都可逆，走过去再走回来等于没走。

第二，付费出路“有向类型论”（E06）能买回什么？本包用一个序论模型回答：若运动由不可逆的箭头给出，读数必须顺着箭头的方向，那么钟可以前进；但一个先升后降的温度计读数，在一次有向旅程上不可能出现。若读数类型里只有恒等箭头，读数又被冻结。

数学内容都是标准事实（路径可逆、ℕ 上 ≤ 的反对称），**不主张原创**。模型与 Riehl–Shulman 的单纯类型论（sHoTT）之间的对应是解释，见“禁止外推”。

## 命题全文

记号：`_≤_` 为 cubical 0.9 `Cubical.Data.Nat.Order` 中的 `m ≤ n :≡ Σ[ k ∈ ℕ ] k + m ≡ n`。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-23**（合成时间没有先后也没有方向） | 对任意 `A : Type ℓ` 与 `a b : A`：`Iso (a ≡ b) (b ≡ a)`；对任意 `p : a ≡ b`，`p ∙ sym p ≡ refl`；对任意非自反 `R : A → A → Type ℓ'` 与 `p : a ≡ b`，`¬ R a b`；对任意 `f : A → ℕ`，若 `∀ x y → x ≡ y → f x ≤ f y`，则 `∀ a b → a ≡ b → f a ≡ f b`。 | `Synthetic.{noArrowOfTime, thereAndBackIsStaying, noEarlierAlongPath, pathsFreezeMonotone}` |
| **CG001-C-24**（有向出路的价格，模型） | `¬ (1 ≤ 0)`。对任意 `A`、`Arr : A → A → Type ℓ'`，记 `Monotone f :≡ ∀ x y → Arr x y → f x ≤ f y`：若 `Monotone f`，则 `Arr a b → Arr b a → f a ≡ f b`；并且 `Arr a b → Arr b c → f a ≡ 0 → f b ≡ 1 → ¬ (f c ≡ 0)`。控制：取 `A = ℕ`、`Arr = _≤_`，恒等读数（钟）满足 `Monotone`，且 `¬ (f 0 ≡ f 1)`；不存在满足 `Monotone` 且 `f 0 ≡ 0`、`f 1 ≡ 1`、`f 2 ≡ 0` 的 `f : ℕ → ℕ`（温度计先升后降）。负控制：以 `(0 , refl)` 作 `1 ≤ 0` 的见证应被内核拒绝。 | `one≰zero`、`Directed.{Monotone, roundTripFreezes, noUpThenDown}`、`clockAdvances`、`thermometerNotMonotone`；负控制 `WrongDownStep.agda` |

## 禁止外推

- C-24 是序论模型，不是单纯类型论。与 sHoTT 的对应【来源：Riehl–Shulman，arXiv:1705.07442，Higher Structures 1(1), 2017：Segal 类型之间的函数自动保持恒等与复合】是解释：若 sHoTT 中读数类型带有序的方向结构，读数沿箭头单调；若读数类型是离散的（只有恒等箭头），读数沿箭头不变。实数值读数在 sHoTT 中取哪种结构，本包未核查。
- C-24 的“温度计”只指先升后降的读数；不说有向理论不能表示变化，钟就能前进（`clockAdvances`）。
- C-23 与 C-07、C-15 同源，这里把它们合成一条“合成时间”的陈述；不说 HoTT 中不能讨论时间，时间作为数据（ℕ、ℚ 上的序）完全可用，C-05a、C-17 即是。
