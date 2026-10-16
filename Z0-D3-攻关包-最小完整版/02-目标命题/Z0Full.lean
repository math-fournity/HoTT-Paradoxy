import GodelQ.ZFC.TranslateRE

/-!
# CG-007 · W8：完整的 Z0 只差一条可导性条件 D3

C-120 的一致性句 `Sh.craig.consistent` 来自 Foundation 用选择挑出的 Σ1 定义，它在 𝗜𝚺₁ 内部与
Con(𝗭𝗙𝗖) 的关系无从推理（见 `godel-q-zfc-z0-translate/REVISIONS.md`）。本文件改用显式的可证性谓词：

* `TrProvable x := Provable 𝗭𝗙𝗖 (iT 0 x)`，“𝗭𝗙𝗖 证明 x 的翻译”，Σ1 公式 `trProv`；
* `zfcTr : Provability 𝗜𝚺₁ Sh`：把它作为 𝗭𝗙𝗖 的算术影子 `Sh` 的可证性谓词。D1 由 Foundation 的
  `internalize_provability` 与 `iT_quote` 得到；D2（`HBL2`）由 `modus_ponens_sentence` 得到；
* `zfcTr_con_iff`：它的一致性句与 Foundation 对 𝗭𝗙𝗖 的一致性句 `𝗭𝗙𝗖.consistent` 在 𝗜𝚺₁ 中可证等价；
* `zfc_z0_full`：在 D3（`zfcTr.HBL3`）下，`𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ`，即 Z0 的完整形式。
  证明用 Foundation 的抽象第二定理 `ProvabilityAbstraction.con_unprovable`；其余条件
  （对角化、`𝗜𝚺₁ ⪯ Sh`、`Sh` 一致）都已具备；
* `zfcTr_D3_standard`：D3 在标准模型 ℕ 中成立（正对照）。

D3 本身（在 𝗜𝚺₁ 中，`zfcTr σ 🡒 zfcTr (zfcTr σ)`）是经翻译的形式化 Σ1 完全性。
它被逐字化成一条等价的“证明的内部翻译”义务，写在 `Z0Blocked.lean` 的
`zfcTr_D3_internalize`（那里以未证标记标出，不进入收据源）；本文件给出它一旦成立
就给出现（`zfc_z0_full_of_D3_internalize`）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.Z0Full

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

section TrProvable

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- “𝗭𝗙𝗖 证明 x 的翻译”。 -/
def TrProvable (x : V) : Prop := Provable 𝗭𝗙𝗖 (iT 0 x)

/-- `TrProvable` 的 Σ1 公式。 -/
noncomputable def trProv : 𝚺ᴬ₁.Semisentence 1 := .mkSigma
  “x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y”

instance trProv_defined : 𝚺ᴬ₁-Predicate (TrProvable : V → Prop) via trProv := .mk fun v ↦ by
  simp [trProv, TrProvable]

lemma trProvable_quote (σ : ArithmeticSentence) :
    TrProvable (⌜σ⌝ : V) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) := by
  have h := iT_quote (V := V) σ
  simp only [Nat.cast_zero] at h
  rw [TrProvable, h]

end TrProvable

lemma models_trProv_iff (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence) :
    V↓[ℒₒᵣ] ⊧ (trProv.val/[⌜σ⌝] : ArithmeticSentence) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) := by
  rw [← trProvable_quote]
  simp [models_iff]

/-- **𝔅Z**：把“𝗭𝗙𝗖 证明它的翻译”作为 `Sh` 的可证性谓词。 -/
noncomputable def zfcTr : Provability 𝗜𝚺₁ Sh where
  prov := trProv.val
  bew_def {σ} h := complete 𝗜𝚺₁ _ fun (V : Type) _ _ ↦
    (models_trProv_iff V σ).mpr (internalize_provability ((Sh_provable_iff σ).mp h))

lemma zfcTr_def (σ : ArithmeticSentence) : zfcTr σ = trProv.val/[⌜σ⌝] := rfl

lemma models_zfcTr_iff (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence) :
    V↓[ℒₒᵣ] ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) := by
  rw [zfcTr_def, models_trProv_iff]

/-- **D2**。 -/
instance zfcTr_HBL2 : zfcTr.HBL2 := ⟨fun {σ τ} ↦ complete 𝗜𝚺₁ _ fun (V : Type) _ _ ↦ by
  rw [Semantics.Imp.models_imply, Semantics.Imp.models_imply, models_zfcTr_iff, models_zfcTr_iff,
    models_zfcTr_iff, LogicalConnective.HomClass.map_imply]
  exact modus_ponens_sentence (T := 𝗭𝗙𝗖)⟩

/-- **一致性句的等价**：`zfcTr` 的一致性句与 Foundation 对 𝗭𝗙𝗖 的一致性句在 𝗜𝚺₁ 中可证等价。 -/
theorem zfcTr_con_iff : 𝗜𝚺₁ ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  complete 𝗜𝚺₁ _ fun (V : Type) _ _ ↦ by
    have h1 : V↓[ℒₒᵣ] ⊧ zfcTr.con ↔ ¬ Provable 𝗭𝗙𝗖 (⌜(⊥ : Sentence ℒₛₑₜ)⌝ : V) := by
      rw [Provability.con, Semantics.Not.models_not, models_zfcTr_iff, LogicalConnective.HomClass.map_bot]
    have h2 : V↓[ℒₒᵣ] ⊧ (𝗭𝗙𝗖.consistent : ArithmeticSentence) ↔
        ¬ Provable 𝗭𝗙𝗖 (⌜(⊥ : Sentence ℒₛₑₜ)⌝ : V) := by
      simp [models_iff, Theory.Consistent]
    have e := h1.trans h2.symm
    simpa using e

/-- `zfcTr σ` 是 𝚺₁ 句（`trProv` 由 `mkSigma` 给出，代入保持层级）。 -/
theorem zfcTr_sigma1 (σ : ArithmeticSentence) : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (zfcTr σ) := by
  rw [zfcTr_def]
  exact trProv.sigma_prop.rew (ω := _)

instance zfcTr_HBL [zfcTr.HBL3] : zfcTr.HBL := ⟨⟩

/-- **完整的 Z0（影子一侧）**：在 D3 下，`Sh` 证明不了 Foundation 对 𝗭𝗙𝗖 的一致性句。 -/
theorem sh_z0_full [zfcTr.HBL3] : Sh ⊬ (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  intro h
  have e : Sh ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent : ArithmeticSentence) := WeakerThan.pbl zfcTr_con_iff
  have hc : Sh ⊢ zfcTr.con := by cl_prover [e, h]
  exact con_unprovable (𝔅 := zfcTr) hc

/-- **完整的 Z0**：在 D3 下，𝗭𝗙𝗖 证明不了“𝗭𝗙𝗖 一致”（Foundation 的一致性句经翻译）。 -/
theorem zfc_z0_full [zfcTr.HBL3] :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  fun h ↦ sh_z0_full ((Sh_provable_iff _).mpr h)

/-- **正对照**：D3 在标准模型 ℕ 中成立。 -/
theorem zfcTr_D3_standard (σ : ArithmeticSentence) :
    ℕ↓[ℒₒᵣ] ⊧ (zfcTr σ 🡒 zfcTr (zfcTr σ)) := by
  rw [Semantics.Imp.models_imply, models_zfcTr_iff, models_zfcTr_iff, provable_iff_provable,
    provable_iff_provable]
  intro h
  exact (Sh_provable_iff _).mp (WeakerThan.pbl (zfcTr.D1 ((Sh_provable_iff σ).mpr h)))

/-- **正结果**：一旦 `Z0Blocked.lean` 中的阻塞引理成立，Z0 的完整形式 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ`
立即随之成立（本定理无未证标记，只以待证引理为显式前提）。 -/
theorem zfc_z0_full_of_D3_internalize
    (h : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence),
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  have h3 : zfcTr.HBL3 := by
    refine ⟨fun {σ} ↦ ?_⟩
    apply complete 𝗜𝚺₁ _
    intro V hV1 hV2
    apply Semantics.Imp.models_imply.mpr
    intro hp
    -- `V ⊧ zfcTr σ` 即 `Provable 𝗭𝗙𝗖 ⌜translate σ⌝`（`models_zfcTr_iff`）。
    -- D3 要 `V ⊧ zfcTr (zfcTr σ)`，即 `Provable 𝗭𝗙𝗖 ⌜translate (zfcTr σ)⌝`。
    -- 唯一缺的一步：`Provable 𝗭𝗙𝗖 ⌜translate σ⌝ → Provable 𝗭𝗙𝗖 ⌜translate (zfcTr σ)⌝`，
    -- 也就是“𝗭𝗙𝗖 证明 τ 的翻译 ⟹ 𝗭𝗙𝗖 证明 τ 的可证性句的翻译”。
    have hout : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr σ)⌝ : V) :=
      @h V _ _ σ (models_zfcTr_iff V σ |>.mp hp)
    exact (models_zfcTr_iff V (zfcTr σ)).mpr hout
  exact zfc_z0_full

end GodelQ.Z0Full

#print axioms GodelQ.Z0Full.zfcTr
#print axioms GodelQ.Z0Full.zfcTr_HBL2
#print axioms GodelQ.Z0Full.zfcTr_con_iff
#print axioms GodelQ.Z0Full.sh_z0_full
#print axioms GodelQ.Z0Full.zfc_z0_full
#print axioms GodelQ.Z0Full.zfcTr_D3_standard
#print axioms GodelQ.Z0Full.zfcTr_sigma1
#print axioms GodelQ.Z0Full.zfc_z0_full_of_D3_internalize
