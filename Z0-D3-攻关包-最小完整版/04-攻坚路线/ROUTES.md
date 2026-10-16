# 攻坚路线（三条，附卡点）

## 路线 1（推荐）：句法等价 `keyE` + Foundation 的 `provable_D3`

**思想**：不去翻译任意推导，而是让 `zfcTr` 与 `Sh.craig` 的标准可证性谓词在 𝗜𝚺₁ 中**可证等价**，
然后 Foundation 的 D3 白拿。

**需要的引理**：

```lean
-- [GAP] keyE : 这是全部缺口
lemma keyE (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ zfcTr σ 🡘 provabilityPred Sh.craig σ
```

**怎么证**（`Provability.ext` 的做法是经完备性定理化到语义层）：

```lean
apply complete 𝗜𝚺₁ _
intro V _ _
rw [models_iff]        -- 化成 Realize
simp only [LogicalConnective.iff]
-- 剩：V ⊧ zfcTr σ ↔ V ⊧ provabilityPred Sh.craig σ
--    = Provable 𝗭𝗙𝗂 ⌜σᵗ⌝ ↔ Provable Sh.craig ⌜σ⌝
```

**已经打通的半边**（本机实测，见骨架）：

```lean
-- V ⊧ provabilityPred Sh.craig σ ↔ Provable Sh.craig ⌜σ⌝   [已证]
rw [models_iff]; simp [provabilityPred, (inferInstance : 𝚺ᴬ₁-Predicate (Provable Sh.craig) via
  (provable Sh.craig)).iff]
```

**卡点在哪里**（我诚实标注）：剩下要
`Provable 𝗭𝗙𝗢 ⌜σᵗ⌝ (V) ↔ Provable Sh.craig ⌜σ⌝ (V)`。

- **右→左**：`Provable Sh.craig ⌜σ⌝ → Sh.craig ⊢ σ` 需要 V 层的**推导消去**。
  Foundation 的 `Provable.sound`/`provable_iff_provable` 只对 ℕ。`⌜σ⌝` 是标准数，
  但推导编码 `d` 可能非标准。这是真正的难点所在。
- **左→右**：好办。`Provable 𝗭𝗙𝗂 ⌜σᵗ⌝ → 𝗭𝗙́ ⊢ σᵗ`？同样的问题。
  但反方向可用：`Sh ⊢ σ → 𝗭𝗙́ ⊢ σᵗ → Provable 𝗭𝗙́ ⌜σᵗ⌝`（`internalize_provability`）。

**替代：只证单向**（若 Iff 太难）：

```lean
-- 单向蕴含就够 D3 用
lemma keyE_mp (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ zfcTr σ 🡒 provabilityPred Sh.craig σ
```

配合 `Provability.mono'`（`T₀ ⊢ σ 🡒 τ → T₀ ⊢ 𝔅 σ 🡒 𝔅 τ`）可得 D3 的一个方向；
另一个方向由 D2/一致性推出。若你发现单向也卡，把这个事实写清楚，它就是精确缺口。

**从 keyE 到目标**（已验证的零件都在）：

```lean
have hE := keyE σ
have hD3 := provable_D3 (T := Sh.craig) (σ := σ)        -- Foundation
have := (Provability.ext (𝔅 := Sh.craig.standardProvability) hE).trans ...  -- 组合
```

---

## 路线 2：直接用 `sigma_one_complete (T := Sh.craig)`，绕开句法等价

我已经跑通的 `step1`：

```lean
theorem step1 {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence)
    (h : V↓[ℒₒᵣ] ⊧ zfcTr σ) : Provable Sh.craig (⌜zfcTr σ⌝ : V) :=
  Bootstrapping.Arithmetic.sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 σ) h
```

**它为什么还不够**：它给的是 `Provable Sh.craig`（理论是 `Sh.craig`），
而目标是 `Provable 𝗭𝗙𝗂`（理论是 𝗭𝗙𝗂，语言是 ℒₛₑₜ）。两个理论的推导编码不能直接等同。
要接上，还需要 `Provable Sh.craig ⌜zfcTr σ⌝ → Provable 𝗭𝗙́ ⌜(zfcTr σ)ᵗ⌝`，
也就是跨理论与跨语言的推导搬运——比 route 1 的句法等价更难。

**结论**：route 2 是死路，除非你想形式化解释定理。**不要走。**

---

## 路线 3：形式化语法解释定理（Foundation 里没有，需要从零写）

定义从 𝗜𝚺₁ 推导编码到 𝗭𝗙𝗂 推导编码的可计算函数 F，在 𝗜𝚺₁ 内证其正确性
（对推导结构内归纳），然后 bridge 原形式直接得。

**这是最 general 的路，但工作量显著更大**：要处理 𝗜𝚺₁ 归纳规则的翻译
（ZFC 用 ω 上的归纳模拟）。Foundation 的 `LK/Interpretation.lean:443 of_provability`
是用**完备性定理**语义地证明的，其中没有可搬进 𝗜𝚺₁ 的语法翻译。

只建议在 route 1 被证伪不可行时启用。

---

## 已排除的想法（别重复）

1. `Sh.Δ₁` 取 `ch := trProv`：`ProperOn` 要求 `trProv ↔ ¬trProv`，假。
2. 给 `Provable 𝗭𝗙𝗂 x` 找有界形式 `∃ d < x, ...`：对 Sh 这样的界不存在（否则可判定）。
3. 扩 `provable_internalize` 到 ZFC：ZFC 不是算术理论，`Theory.Δ₁` 都套不上。
4. 在 ZFC 内证 `𝔅(τ)ᵗ ↔ (𝔅τ)ᵗ` 再用 D2：同样需要跨理论的推导搬运。
