import GodelQ.ZFC.GodelQZFC

/-!
# CG-006 `godel-q-zfc`：命题对照（`CLAIM.md` §2 的精确形式）

每条 `qual_C*` 把对应命题的各部分写成一个合取，证明只引用包内已过核的定理；随后 `#print axioms`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic

namespace GodelQ.ZFCQual

open GodelQ.ZFCDelta1 GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff GodelQ.ZFCSound GodelQ.ZFCMain

/-- C-95：𝗭𝗙𝗖 有 Foundation 意义下的 Δ1 公理表示；分离、替换两个模式各有 Δ1 识别，𝗕𝗦𝗧 有限。 -/
theorem qual_C95 :
    Nonempty (𝗭𝗙𝗖 : SetTheory).Δ₁ ∧ Nonempty (𝗦𝗘𝗣 : SetTheory).Δ₁ ∧
      Nonempty (𝗥𝗘𝗣𝗟 : SetTheory).Δ₁ ∧ Set.Finite (𝗕𝗦𝗧 : SetTheory) :=
  ⟨⟨ZFC.delta1⟩, ⟨Separation.delta1⟩, ⟨Replacement.delta1⟩, bst_finite⟩

/-- C-96：Rayo 数字公式的编码 `numCode` 由内部原始递归给出且等于真实编码；在 𝗭 的每个模型中
`Num_n(z)` 恰好当 `z = ofNat n`。 -/
theorem qual_C96 :
    (∀ n : ℕ, numCode (n : ℕ) = (⌜numeralF n⌝ : ℕ)) ∧
    (∀ (V : Type) [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭] (n : ℕ) (z : V),
      V ⊧/![z] (numeralF n) ↔ z = ofNat n) :=
  ⟨numCode_quote, fun _ _ _ _ n z ↦ eval_numeralF_iff n z⟩

/-- C-97：对任意 ℒₛₑₜ 公式 Φ，`{n ∣ 𝗭𝗙𝗖 ⊢ ¬∃z (Num_n(z) ∧ Φ(z))}` 可枚举。 -/
theorem qual_C97 (Φ : SetTheorySemisentence 1) :
    REPred (fun n : ℕ ↦ 𝗭𝗙𝗖 ⊢ neverS Φ n) :=
  never_re Φ

/-- C-98：𝗭𝗙𝗖 直接解释 𝗥₀；每个真实 r.e. 事实的数字句被 𝗭𝗙𝗖 证明（只用 Σ1 完全性）。 -/
theorem qual_C98 :
    Nonempty (𝗭𝗙𝗖 ⊳ 𝗥₀) ∧
    (∀ {p : ℕ → Prop}, REPred p → ∀ {a : ℕ}, p a →
      𝗭𝗙𝗖 ⊢ haltsS (arithTrln.translate (codeOfREPred p)) a) :=
  ⟨⟨arithInterp⟩, fun hp _ h ↦ zfc_proves_haltsS hp h⟩

/-- C-99：真实 𝗭𝗙𝗖 的过程观察接口满足四条元性质（`zfcEffective`）；哥德尔 I 的过程形式；
魔鬼交易（𝗭𝗙𝗖 不封闭于 ω 完成规则）。 -/
theorem qual_C99 :
    (∃ d : Process, ¬ Done d ∧
      (∀ k : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, k))) ∧
      𝗭𝗙𝗖 ⊬ neverS ΦH (Encodable.encode d) ∧
      (Done d ↔ 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode d))) ∧
    ¬ zfcEffective.OmegaClosed :=
  ⟨godel_I_process_form_zfc, devils_bargain_zfc⟩

/-- C-100：数字句 Σ1 可靠（经 Foundation 的 `Universe` 模型，其 ω 与 ℕ 同构）；𝗭𝗙𝗖 证明“e 停机”
恰好当 e 停机；对角过程的两句都独立；𝗭𝗙𝗖 在 Foundation 意义下不完全。 -/
theorem qual_C100 :
    (∀ {p : ℕ → Prop}, REPred p → ∀ {a : ℕ},
      𝗭𝗙𝗖 ⊢ haltsS (arithTrln.translate (codeOfREPred p)) a → p a) ∧
    (∀ e : Process, zfcEffective.provesHalts e ↔ Done e) ∧
    (∃ d : Process, ¬ Done d ∧
      (∀ k : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, k))) ∧
      𝗭𝗙𝗖 ⊬ neverS ΦH (Encodable.encode d) ∧
      𝗭𝗙𝗖 ⊬ haltsS ΦH (Encodable.encode d) ∧
      (Done d ↔ 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode d))) ∧
    Entailment.Incomplete 𝗭𝗙𝗖 :=
  ⟨fun hp _ h ↦ zfc_haltsS_sound hp h, zfc_provesHalts_iff, godel_I_process_form_zfc_full,
    zfc_incomplete⟩

/-- C-101：哥德尔–芝诺跑者与 𝗭𝗙𝗖 + A = 𝗭𝗙𝗖 + P，落在 𝗭𝗙𝗖 上；以“到达句与永不停机句在 𝗭𝗙𝗖 中
逐个可证等价”为显式参数。 -/
theorem qual_C101 (arr : ℕ → Sentence ℒₛₑₜ) (harr : ∀ a, 𝗭𝗙𝗖 ⊢ arr a 🡘 neverS ΦH a) :
    (∃ d : Process, Arrives d ∧ 𝗭𝗙𝗖 ⊬ arr (Encodable.encode d) ∧
      (∀ n : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (d, n))) ∧
      (∀ n, position d n < 1) ∧ (∃ L, Filter.Tendsto (position d) Filter.atTop (nhds L))) ∧
    ((zfcRunner arr harr).AGeneral ↔ zfcEffective.CompleteForNever) ∧
    (zfcEffective.OmegaClosed → (zfcRunner arr harr).AGeneral) ∧
    ¬ (zfcRunner arr harr).AGeneral :=
  ⟨goedel_zeno_zfc arr harr, zfc_aGeneral_iff_complete arr harr,
    zfc_omegaClosed_imp_aGeneral arr harr, zfc_not_aGeneral arr harr⟩

/-- C-101 的参数可满足：取到达句为“永不停机”句本身。 -/
theorem qual_C101_nonvacuous : ∀ a, 𝗭𝗙𝗖 ⊢ neverS ΦH a 🡘 neverS ΦH a := fun _ ↦ by cl_prover

/-- C-102：算术落地（S1）。对任意 Δ1、扩张 𝗥₀、Σ1 可靠的算术理论 T：哥德尔 I 过程形式（含独立性）
与魔鬼交易。 -/
theorem qual_C102 (T : ArithmeticTheory) [T.Δ₁] [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1] :
    (∃ d : Process, ¬ Done d ∧
      (∀ k : ℕ, T ⊢ ψN/[↑(Encodable.encode (d, k))]) ∧
      T ⊬ ∼φH/[↑(Encodable.encode d)] ∧
      T ⊬ φH/[↑(Encodable.encode d)] ∧
      (Done d ↔ T ⊢ ∼φH/[↑(Encodable.encode d)])) ∧
    ¬ (arithEffective T).OmegaClosed :=
  ⟨godel_I_process_form_arith T, devils_bargain_arith T⟩

/-- C-102 的交叉核对：Foundation 自带的哥德尔第一不完备（经停机问题）对同一 T 成立。 -/
theorem qual_C102_crosscheck (T : ArithmeticTheory) [T.Δ₁] [𝗜𝚺₁ ⪯ T]
    [T.SoundOnHierarchy 𝚺 1] : Entailment.Incomplete T :=
  foundation_crosscheck T

end GodelQ.ZFCQual

#print axioms GodelQ.ZFCQual.qual_C95
#print axioms GodelQ.ZFCQual.qual_C96
#print axioms GodelQ.ZFCQual.qual_C97
#print axioms GodelQ.ZFCQual.qual_C98
#print axioms GodelQ.ZFCQual.qual_C99
#print axioms GodelQ.ZFCQual.qual_C100
#print axioms GodelQ.ZFCQual.qual_C101
#print axioms GodelQ.ZFCQual.qual_C101_nonvacuous
#print axioms GodelQ.ZFCQual.qual_C102
#print axioms GodelQ.ZFCQual.qual_C102_crosscheck
