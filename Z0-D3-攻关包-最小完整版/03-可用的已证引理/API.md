# 可直接用的引理（Foundation `1fb01b72`）

> 状态列：**[实测]** = 我在本机 Lean 4.34.0 上 elaborates/编译通过；
> **[读码]** = 只读了源码没跑。其余照实标。
> 所有 Foundation 文件在 `../05-源码/Foundation/` 下有源码（167 个模块全量）。

## A. Foundation 的 D3 家族（这是主武器）

| 名字 | 位置 | 形状 | 状态 |
|---|---|---|---|
| `sigma_one_complete` | `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean:170` | `[T.Δ₁] [𝗣𝗔⁻ ⪯ T] → 𝚺1 σ → V ⊧ σ → Provable T ⌜σ⌝` | **[实测]** |
| `sigma_one_provable_of_models` | 同上 `:162` | `[T.Δ₁] [𝗣𝗔⁻ ⪯ T] → 𝚺1 σ → V ⊧ σ → T.internalize V ⊢ ⌜σ⌝` | **[实测]** |
| `bold_sigma_one_complete` | 同上 `:82` | 沿公式结构归纳的版本（`hBall`/`hExs` 情形） | **[读码]** |
| `provable_internalize` | 同上 `:173` | `Provable T ⌜σ⌝ → Provable T ⌜provabilityPred T σ⌝` | **[实测]** |
| `internalize_provability`（D1） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D1.lean:27` | `T ⊢ φ → Provable T ⌜φ⌝` | **[实测]** |
| `modus_ponens_sentence`（D2） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D2.lean:30` | Provable 层面的 MP | **[读码]** |

注意 `sigma_one_complete` 的 `V` 是**任意的 𝗜𝚺₁ 模型**，`Provable T ⌜σ⌝` 是 V 层的存在量词。
这正是我们需要的方向：从"V 中为真"得到"V 中有编码"，不需要元层 soundness。

## B. Craig 化：把 `Sh.RE` 变成 `Δ₁`（本轮新发现）

| 名字 | 位置 | 形状 | 状态 |
|---|---|---|---|
| `Theory.craigCh` | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean:210` | 两半都用有界量词 `∃ s < x`，Π1 半加唯一性条件 | **[实测]** `inferInstance` 成功 |
| `Theory.IsCraigAxiom.defined` | 同上 `:222` | `𝚫ᴬ₁-Predicate[V] (T.IsCraigAxiom) via T.craigCh` | **[实测]** |
| `(T.craig).Δ₁` | 同上 `:310` | `[T.RE]` ⟹ Δ1 公理表示 | **[实测]** `inferInstance` 成功 |
| `T.craig ⪯ T`, `T ⪯ T.craig` | 同上 `:322/:329` | 需 `[L.DecidableEq]` | **[实测]** 两者都 `inferInstance` |
| `Entailment.Equiv.iff` | `Foundation/Logic/Entailment.lean:146` | `𝓢 ≊ 𝓣 ↔ (∀ φ, 𝓢 ⊢ φ ↔ 𝓣 ⊢ φ)` | **[实测]** |

我用它写成的引理（已编译通过）：

```lean
lemma shCraig_iff (σ : ArithmeticSentence) : Sh.craig ⊢ σ ↔ Sh ⊢ σ := by
  refine ⟨fun h ↦ ?_, fun h ↦ ?_⟩
  · exact Entailment.weakerThan_iff.mp (inferInstance : Sh.craig ⪯ Sh) h
  · exact Entailment.weakerThan_iff.mp (inferInstance : Sh ⪯ Sh.craig) h
```

## C. 语义层桥

| 名字 | 位置 | 形状 | 状态 |
|---|---|---|---|
| `Provability.ext` | `Foundation/FirstOrder/Incompleteness/ProvabilityAbstraction/Basic.lean:72,166` | `T ⊢ σ 🡘 τ → T₀ ⊢ 𝔅 σ 🡘 𝔅 τ` | **[实测]** |
| `Provability.mono'` | 同上 `:165` | `T₀ ⊢ σ 🡒 τ → T₀ ⊢ 𝔅 σ 🡒 𝔅 τ` | **[实测]** |
| `provable_iff_provable` | `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D1.lean:40` | `Provable T (⌜φ⌝ : ℕ) ↔ T ⊢ φ`（**只对 ℕ**） | **[实测]** |
| `tprovable_tquote_iff_provable_quote_sentence` | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean:175` | `T.internalize V ⊢ ⌜σ⌝ ↔ Provable T ⌜σ⌝` | **[实测]** |
| `tprovable_iff_provable` | 同上 `:168` | `T.internalize V ⊢ σ ↔ Provable T σ.val` | **[实测]** |
| `Defined.iff` | `Foundation/FirstOrder/Tarski/HierarchicalDefinability/Basic.lean:135` | `[Defined R φ] → φ.val.Evalb v ↔ R v` | **[实测]** |
| `Defined.shigmaOne_absolute` | `Foundation/FirstOrder/Arithmetic/Definability/Absoluteness.lean:99` | `R v ↔ R' (Nat.cast ∘ v)`（\Δ1 谓词绝对） | **[读码]** |

## D. 本项目包内的引理

| 名字 | 文件 | 形状 | 状态 |
|---|---|---|---|
| `iT_quote` | `GodelQ/ZFC/InternalTranslate.lean:611` | `iT 0 ⌜φ⌝ = ⌜arithTrln.translate φ⌝` | **[实测]** |
| `iVE_quote` | 同文件 | 项级正确性 | **[实测]** |
| `trProvable_quote` | `GodelQ/ZFC/Z0Full.lean:46` | `TrProvable ⌜σ⌝ ↔ Provable 𝗭𝗙𝗂 ⌜σᵗ⌝`（`V : Type*`） | **[实测]** |
| `models_trProv_iff` | `GodelQ/ZFC/Z0Full.lean:54` | `V ⊧ (trProv/[⌜σ⌝]) ↔ Provable 𝗭𝗙𝗂 ⌜σᵗ⌝`（`V : Type`） | **[实测]** |
| `models_zfcTr_iff` | `GodelQ/ZFC/Z0Full.lean:67` | `V ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗂 ⌜σᵗ⌝`（`V : Type`） | **[实测]** |
| `zfcTr_sigma1` | `GodelQ/ZFC/Z0Full.lean:87` | `ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (zfcTr σ)` | **[实测]** |
| `zfcTr_HBL2`（D2） | `GodelQ/ZFC/Z0Full.lean:72` | HBL2 instance | **[实测]** |
| `zfcTr_con_iff` | `GodelQ/ZFC/Z0Full.lean:78` | 一致性句等价 | **[实测]** |
| `zfcTr_D3_standard` | `GodelQ/ZFC/Z0Full.lean:108` | D3 在 ℕ 中的正对照 | **[实测]** |
| `zfc_z0_full_of_D3_internalize` | `GodelQ/ZFC/Z0Full.lean:117` | 阻塞引理 ⟹ 完整形式 | **[实测]** |
| `Sh_provable_iff` | `GodelQ/ZFC/Z0Shadow.lean:45` | `Sh ⊢ σ ↔ 𝗭𝗙́ ⊢ arithTrln.translate σ` | **[实测]** |
| `ISigma1_le_Sh` | `GodelQ/ZFC/Z0PA.lean:28` | `𝗜𝚺₁ ⪯ Sh` instance | **[实测]** |
| `Sh_consistent` | `GodelQ/ZFC/Z0Shadow.lean:49` | `Entailment.Consistent Sh` instance | **[实测]** |
| `Sh_RE` | `GodelQ/ZFC/TranslateRE.lean:52` | `Sh.RE` instance | **[实测]** |

## E. 你**不要**用的（已试过）

| 想法 | 为什么不行 |
|---|---|
| `Sh.Δ₁` 取 `ch := trProv` | `mkDelta trProv (∼trProv)` 要求 `trProv ↔ ¬trProv`，在 trProv 有确定真值的模型中为假。**Π1 那半必须是等价公式，不是否定。** |
| 找"证明长度的界"让 `Provable 𝗭𝗙𝗂` 变有界 | 对 Sh 本身这样的界不存在（否则 Sh 可判定）。CraigTrick 之所以不需要，是因为它从 `T.RE` 出发、证明长度已写进 Craig 公理化。 |
| `provable_D3 (T := Sh)` | 需 `Sh.Δ₁`，循环。**用 `T := Sh.craig`**（见 §B）。 |
| `provable_internalize (T := Sh.craig)` 得目标 | 它给的是 `Sh.craig ⊢ provabilityPred Sh.craig σ`，理论不对，还要翻译回 𝗭𝗙́。 |
