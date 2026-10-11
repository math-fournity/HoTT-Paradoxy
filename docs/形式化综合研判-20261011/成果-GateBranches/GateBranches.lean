-- CG-009 / Claude 独立方向：gateG 义务清单 O2 的第一批（andIntro / orIntro 两支）
--
-- 依 `gateG-证明义务清单.md`：归纳不变量取 sequent 层 Q d := Derivable ZFC (translateSeq (fstIdx d))。
-- 本文件完成两条"零件齐、未组装"的支（不依赖失败的 ShCraigElimNegLaw）：
--   * hAnd：p ^⋏ q ∈ s，两条子推导 ⇒ Q (andIntro s p q dp dq)
--   * hOr：p ^⋎ q ∈ s，一条子推导 ⇒ Q (orIntro s p q d)
-- 两条都只用已过核零件：translateSeq_insert、mem_translateSeq_iff、iT_and/iT_or、
-- Derivable.and_m/or_m、fstIdx_andIntro/orIntro、IsUFormula.and/or。
import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.SeqTranslate
import GodelQ.ZFC.SeqTranslateFormula
import GodelQ.ZFC.InternalTranslate

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate

namespace GodelQ.GateBranches

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 归纳不变量（sequent 层，与 `ShCraigElimPredicate.Q` 同形）。 -/
def Q (d : V) : Prop := Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (fstIdx d))

/-- `Q` 的 Σ1 公式（同 `ShCraigElimPredicate.qDef`）。 -/
noncomputable def qDef : 𝚺ᴬ₁.Semisentence 1 := .mkSigma
  “d. ∃ s, !fstIdxDef s d ∧ ∃ t, !translateSeqGraph t s ∧ !(derivable 𝗭𝗙𝗖) t”

/-- `Q` 是 Σ1 谓词（`induction1` 的 `hP` 要求）。 -/
instance q_defined : 𝚺ᴬ₁-Predicate (Q (V := V)) via qDef :=
  .mk fun v => by simp [qDef, Q]

/-- `translateSeq` 保持公式集（用已过核的 `isSemiformula_iT` 重证，不依赖 ShCraigElimBranches）。 -/
lemma isFormulaSet_translateSeq {s : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) :
    IsFormulaSet (L := ℒₛₑₜ) (translateSeq (V := V) s) := by
  intro p hp
  rcases mem_translateSeq_iff.mp hp with ⟨x, hx, rfl⟩
  exact isSemiformula_iT x (hs x hx)

/-- **`hAnd` 支**：`p ^⋏ q ∈ s`，子推导 `⊢ p,s` 与 `⊢ q,s` ⇒ `⊢ s`（翻译后）。 -/
theorem hAnd {s p q dp dq : V}
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hpq : p ^⋏ q ∈ s)
    (hdp : DerivationOf (L := ℒₒᵣ) Sh.craig dp (insert p s))
    (hdq : DerivationOf (L := ℒₒᵣ) Sh.craig dq (insert q s))
    (ihp : Q dp) (ihq : Q dq) : Q (andIntro s p q dp dq) := by
  simp only [Q, fstIdx_andIntro]
  have hpU : IsUFormula ℒₒᵣ p := (IsUFormula.and.mp ((hs (p ^⋏ q) hpq).isUFormula)).1
  have hqU : IsUFormula ℒₒᵣ q := (IsUFormula.and.mp ((hs (p ^⋏ q) hpq).isUFormula)).2
  have hmem : iT (0 : V) (p ^⋏ q) ∈ translateSeq (V := V) s :=
    mem_translateSeq_iff.mpr ⟨p ^⋏ q, hpq, rfl⟩
  rw [iT_and hpU hqU] at hmem
  have hdp' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (iT (0 : V) p) (translateSeq (V := V) s)) := by
    rw [← translateSeq_insert (x := p) (s := s), ← hdp.1]
    exact ihp
  have hdq' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (iT (0 : V) q) (translateSeq (V := V) s)) := by
    rw [← translateSeq_insert (x := q) (s := s), ← hdq.1]
    exact ihq
  exact Derivable.and_m hmem hdp' hdq'

/-- **`hOr` 支**：`p ^⋎ q ∈ s`，子推导 `⊢ p,q,s` ⇒ `⊢ s`（翻译后）。 -/
theorem hOr {s p q d : V}
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hpq : p ^⋎ q ∈ s)
    (hd : DerivationOf (L := ℒₒᵣ) Sh.craig d (insert p (insert q s)))
    (ih : Q d) : Q (orIntro s p q d) := by
  simp only [Q, fstIdx_orIntro]
  have hpU : IsUFormula ℒₒᵣ p := (IsUFormula.or.mp ((hs (p ^⋎ q) hpq).isUFormula)).1
  have hqU : IsUFormula ℒₒᵣ q := (IsUFormula.or.mp ((hs (p ^⋎ q) hpq).isUFormula)).2
  have hmem : iT (0 : V) (p ^⋎ q) ∈ translateSeq (V := V) s :=
    mem_translateSeq_iff.mpr ⟨p ^⋎ q, hpq, rfl⟩
  rw [iT_or hpU hqU] at hmem
  have hd' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (iT (0 : V) p) (insert (iT (0 : V) q) (translateSeq (V := V) s))) := by
    rw [← translateSeq_insert (x := q) (s := s),
      ← translateSeq_insert (x := p) (s := insert q s), ← hd.1]
    exact ih
  exact Derivable.or_m hmem hd'

/-- **`hWk` 支**：`fstIdx d ⊆ s` ⇒ 翻译后弱化（`translateSeq_mono` + `Derivable.wk`）。 -/
theorem hWk {s d : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (h : fstIdx d ⊆ s) (ih : Q d) : Q (wkRule s d) := by
  simp only [Q, fstIdx_wkRule]
  exact Derivable.wk (isFormulaSet_translateSeq hs) (translateSeq_mono (V := V) h) ih

/-- **`hVerumIntro` 支**：`^⊤ ∈ s` ⇒ 翻译后 `⊤ ∈ translateSeq s` ⇒ `Derivable.verum`。 -/
theorem hVerumIntro {s : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) (hv : (^⊤ : V) ∈ s) :
    Q (verumIntro s) := by
  simp only [Q, fstIdx_verumIntro]
  apply Derivable.verum
  · exact isFormulaSet_translateSeq hs
  · exact mem_translateSeq_iff.mpr ⟨^⊤, hv, (iT_verum 0).symm⟩

/-- **`hAxL` 支（条件版）**：以"一般内部码的 `iT`/`neg` 相容律"为显式前提。
`p ∈ s ∧ neg p ∈ s` ⇒ 翻译后 `iT p ∈ sᵗ ∧ neg (iT p) ∈ sᵗ` ⇒ `Derivable.axL`。
（前提 `iT_neg` 是 canonical 活跃战线的目标；一旦过核，本支即无条件。） -/
theorem hAxL {s p : V}
    (iT_neg : ∀ (n p' : V), IsSemiformula ℒₒᵣ n p' → iT n (neg ℒₒᵣ p') = neg ℒₛₑₜ (iT n p'))
    (hs : IsFormulaSet (L := ℒₒᵣ) s) (hp : p ∈ s) (hn : neg ℒₒᵣ p ∈ s) :
    Q (axL s p) := by
  simp only [Q, fstIdx_axL]
  have hpU : IsUFormula ℒₒᵣ p := (hs p hp).isUFormula
  have hmem : iT (0 : V) p ∈ translateSeq (V := V) s :=
    mem_translateSeq_iff.mpr ⟨p, hp, rfl⟩
  have hnegmem : neg ℒₛₑₜ (iT (0 : V) p) ∈ translateSeq (V := V) s := by
    have h2 : iT (0 : V) (neg ℒₒᵣ p) ∈ translateSeq (V := V) s :=
      mem_translateSeq_iff.mpr ⟨neg ℒₒᵣ p, hn, rfl⟩
    rwa [iT_neg 0 p (hs p hp)] at h2
  exact ⟨axL (translateSeq (V := V) s) (iT (0 : V) p), by simp,
    Derivation.axL (isFormulaSet_translateSeq hs) hmem hnegmem⟩

/-- **`hCut` 支（条件版）**：同样以 `iT_neg` 为显式前提。 -/
theorem hCut {s p d₁ d₂ : V}
    (iT_neg : ∀ (n p' : V), IsSemiformula ℒₒᵣ n p' → iT n (neg ℒₒᵣ p') = neg ℒₛₑₜ (iT n p'))
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hd₁ : DerivationOf (L := ℒₒᵣ) Sh.craig d₁ (insert p s))
    (hd₂ : DerivationOf (L := ℒₒᵣ) Sh.craig d₂ (insert (neg ℒₒᵣ p) s))
    (ih₁ : Q d₁) (ih₂ : Q d₂) : Q (cutRule s p d₁ d₂) := by
  simp only [Q, fstIdx_cutRule]
  -- p 的公式性：hd₁ 的结论 sequent `insert p s` 是公式集（现成引理）
  have hs' : IsFormulaSet (L := ℒₒᵣ) (insert p s) := hd₁.isFormulaSet
  have hpform : IsSemiformula ℒₒᵣ 0 p := hs' p (by simp)
  have hd₁' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (iT (0 : V) p) (translateSeq (V := V) s)) := by
    rw [← translateSeq_insert (x := p) (s := s), ← hd₁.1]; exact ih₁
  have hd₂' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ (iT (0 : V) p)) (translateSeq (V := V) s)) := by
    rw [← iT_neg 0 p hpform]
    rw [← translateSeq_insert (x := neg ℒₒᵣ p) (s := s), ← hd₂.1]; exact ih₂
  exact Derivable.cut (iT (0 : V) p) hd₁' hd₂'

/-- **`hShift` 支（条件版）**：以"`translateSeq` 与 `setShift` 交换"为显式前提。
`shiftRule` 的结论 sequent 是 `s`，其源是 `setShift s'`（`s = setShift s'`）；
翻译后需 `translateSeq s = setShift (translateSeq s')` 才能接 `Derivable.shift`。 -/
theorem hShift {s d : V}
    (tshift : ∀ s' : V, translateSeq (V := V) (setShift (L := ℒₒᵣ) s') =
      setShift (L := ℒₛₑₜ) (translateSeq (V := V) s'))
    (h : s = setShift (L := ℒₒᵣ) (fstIdx d)) (ih : Q d) : Q (shiftRule s d) := by
  simp only [Q, fstIdx_shiftRule]
  rw [h, tshift (fstIdx d)]
  exact Derivable.shift ih

/-- **`hAll` 支（条件版）**：前提是"**全称规则在翻译下保持**"这一独立义务——
即：若前提 sequent 的翻译可导，则结论 sequent 的翻译可导。
该义务的预期证明路径：`iT` 与 `free`/`setShift` 的相容律 + `Derivable.all_m`。
（本会话不证该相容律——它是 O2 的实质难点；此处只固定接口，使组装可先行。） -/
theorem hAll {s p d : V}
    (hall : ∀ p' : V, IsUFormula ℒₒᵣ p' →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (insert (free (L := ℒₒᵣ) p')
        (setShift (L := ℒₒᵣ) s))) →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s))
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : (^∀ p : V) ∈ s)
    (hd : DerivationOf (L := ℒₒᵣ) Sh.craig d (insert (free (L := ℒₒᵣ) p) (setShift (L := ℒₒᵣ) s)))
    (ih : Q d) : Q (allIntro s p d) := by
  simp only [Q, fstIdx_allIntro]
  have hpU : IsUFormula ℒₒᵣ p := (IsUFormula.all.mp ((hs (^∀ p) hp).isUFormula))
  have ih' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V)
      (insert (free (L := ℒₒᵣ) p) (setShift (L := ℒₒᵣ) s))) := by
    rw [← hd.1]; exact ih
  exact hall p hpU ih'

/-- **`hExs` 支（条件版）**：前提是"**存在规则在翻译下保持**"这一独立义务。
注意 `iVE` 输出是**公式**不是项（`exsIntro` 的项 `t` 经翻译变成值关系公式）——
该义务的形状本身是 O2 最难的实质点。 -/
theorem hExs {s p t d : V}
    (hexs : ∀ p' t' : V, IsUFormula ℒₒᵣ p' →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (insert (substs1 (L := ℒₒᵣ) t' p') s)) →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s))
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : (^∃ p : V) ∈ s)
    (hd : DerivationOf (L := ℒₒᵣ) Sh.craig d (insert (substs1 (L := ℒₒᵣ) t p) s))
    (ih : Q d) : Q (exsIntro s p t d) := by
  simp only [Q, fstIdx_exsIntro]
  have hpU : IsUFormula ℒₒᵣ p := (IsUFormula.ex.mp ((hs (^∃ p) hp).isUFormula))
  have ih' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V)
      (insert (substs1 (L := ℒₒᵣ) t p) s)) := by
    rw [← hd.1]; exact ih
  exact hexs p t hpU ih'

/-- **`hAxm` 支（条件版）**：唯一用到 `𝗭𝗙𝗖` 公理的地方，以 **O3 证书桥**为显式前提：
对每个 Craig 公理码 `p`（`p ∈ Sh.craig.Δ₁Class`），V 中存在 `iT 0 p` 的 ZFC 推导编码。
拿到后：`iT p ∈ translateSeq s`（由 `mem_translateSeq_iff`），
而 `Derivable ZFC (insert (iT p) (translateSeq s))` 由单元素 sequent 弱化 + 该证书。 -/
theorem hAxm {s p : V}
    (axmBridge : ∀ p' : V, p' ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT (0 : V) p'))
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hps : p ∈ s) (hpT : p ∈ Sh.craig.Δ₁Class) : Q (axm s p) := by
  simp only [Q, fstIdx_axm]
  -- 从证书桥得 `iT p` 的单元素 sequent 推导，再弱化到目标 sequent
  have hprov : Provable 𝗭𝗙𝗖 (iT (0 : V) p) := axmBridge p hpT
  have hder : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 ({iT (0 : V) p} : V) :=
    ⟨Classical.choose hprov, Classical.choose_spec hprov⟩
  exact Derivable.wk (isFormulaSet_translateSeq hs)
    (by
      intro x hx
      rw [Arithmetic.mem_singleton_iff] at hx
      rw [hx]
      exact mem_translateSeq_iff.mpr ⟨p, hps, rfl⟩)
    hder

/-! ## 条件组装：十支全接 ⇒ 条件版 `ShCraigElim`

把上述十支（4 无条件 + 6 条件）经 `Derivation.induction1` 组装成
**以五条显式义务为前件的完整消去定理**。五条义务：
`iT_neg`（一般码否定相容）、`tshift`（setShift 交换）、`hall`/`hexs`（量词规则保持）、
`axmBridge`（Craig 证书桥）。一旦这五条被证出，`ShCraigElim` 即无条件。 -/

set_option maxHeartbeats 800000 in
/-- **条件版 ShCraigElim**：五条显式义务 ⇒ 对 V 内任意 Sh.craig 推导的消去。 -/
theorem shCraigElim_of_obligations
    (iT_neg : ∀ (n p : V), IsSemiformula ℒₒᵣ n p → iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p))
    (tshift : ∀ s' : V, translateSeq (V := V) (setShift (L := ℒₒᵣ) s') =
      setShift (L := ℒₛₑₜ) (translateSeq (V := V) s'))
    (hall : ∀ s' p' : V, IsUFormula ℒₒᵣ p' →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (insert (free (L := ℒₒᵣ) p')
        (setShift (L := ℒₒᵣ) s'))) →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s'))
    (hexs : ∀ s' p' t' : V, IsUFormula ℒₒᵣ p' →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (insert (substs1 (L := ℒₒᵣ) t' p') s')) →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s'))
    (axmBridge : ∀ p' : V, p' ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT (0 : V) p'))
    (d : V) (hd : Derivation (V := V) (L := ℒₒᵣ) Sh.craig d) :
    Q d := by
  apply Derivation.induction1 (T := Sh.craig) 𝚺 (hP := q_defined.to_definable) hd
  · intro s hs p hp hn; exact hAxL iT_neg hs hp hn
  · intro s hs hv; exact hVerumIntro hs hv
  · intro s hs p q dp dq hpq hdp hdq ihp ihq; exact hAnd hs hpq hdp hdq ihp ihq
  · intro s hs p q d hpq hd ih; exact hOr hs hpq hd ih
  · intro s hs p d hp hd ih; exact hAll (fun p' hU h => hall s p' hU h) hs hp hd ih
  · intro s hs p t d hp ht hd ih; exact hExs (fun p' t' hU h => hexs s p' t' hU h) hs hp hd ih
  · intro s hs d h hd ih; exact hWk hs h ih
  · intro s hs d h hd ih; exact hShift tshift h ih
  · intro s hs p d₁ d₂ h₁ h₂ ih₁ ih₂; exact hCut iT_neg hs h₁ h₂ ih₁ ih₂
  · intro s hs p hps hpT; exact hAxm axmBridge hs hps hpT

/-- **条件版单句消去**：五条义务 ⇒ `elim@G`（只对结论句 `zfcTr G` 的那一条）。
注意结论句固定但**推导 d 仍任意**——这正是本定理要 `hd : Derivation Sh.craig d` 的原因。 -/
theorem elim_at_godel_of_obligations
    (iT_neg : ∀ (n p : V), IsSemiformula ℒₒᵣ n p → iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p))
    (tshift : ∀ s' : V, translateSeq (V := V) (setShift (L := ℒₒᵣ) s') =
      setShift (L := ℒₛₑₜ) (translateSeq (V := V) s'))
    (hall : ∀ s' p' : V, IsUFormula ℒₒᵣ p' →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (insert (free (L := ℒₒᵣ) p')
        (setShift (L := ℒₒᵣ) s'))) →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s'))
    (hexs : ∀ s' p' t' : V, IsUFormula ℒₒᵣ p' →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (insert (substs1 (L := ℒₒᵣ) t' p') s')) →
      Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s'))
    (axmBridge : ∀ p' : V, p' ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT (0 : V) p'))
    (d : V) (hd : Derivation (V := V) (L := ℒₒᵣ) Sh.craig d)
    (hconcl : fstIdx d = ({⌜zfcTr (gödel zfcTr)⌝} : V)) :
    Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) ({⌜zfcTr (gödel zfcTr)⌝} : V)) := by
  have hQ := shCraigElim_of_obligations iT_neg tshift hall hexs axmBridge d hd
  rwa [Q, hconcl] at hQ

/-- **义务归约：`tshift` ⇐ 元素级 `iT`/`shift` 相容律**（本会话探针证实）。
`translateSeq (setShift s) = setShift (translateSeq s)` 由成员级论证给出，
只需元素律 `iT 0 (shift x) = shift (iT 0 x)`。 -/
theorem tshift_of_ishift
    (ishift : ∀ x : V, iT (0 : V) (shift (L := ℒₒᵣ) x) = shift (L := ℒₛₑₜ) (iT (0 : V) x))
    (s : V) :
    translateSeq (V := V) (setShift (L := ℒₒᵣ) s) = setShift (L := ℒₛₑₜ) (translateSeq (V := V) s) := by
  apply Arithmetic.mem_ext; intro y
  rw [mem_translateSeq_iff, mem_setShift_iff]
  constructor
  · rintro ⟨x, hx, rfl⟩
    rw [mem_setShift_iff] at hx
    rcases hx with ⟨x', hx', rfl⟩
    exact ⟨iT (0 : V) x', mem_translateSeq_iff.mpr ⟨x', hx', rfl⟩, by rw [ishift]⟩
  · rintro ⟨y', hy', rfl⟩
    rw [mem_translateSeq_iff] at hy'
    rcases hy' with ⟨x', hx', rfl⟩
    exact ⟨shift (L := ℒₒᵣ) x', mem_setShift_iff.mpr ⟨x', hx', rfl⟩, by rw [ishift]⟩

end GodelQ.GateBranches

#print axioms GodelQ.GateBranches.hAnd
#print axioms GodelQ.GateBranches.hOr
#print axioms GodelQ.GateBranches.hWk
#print axioms GodelQ.GateBranches.hVerumIntro
#print axioms GodelQ.GateBranches.hAxL
#print axioms GodelQ.GateBranches.hCut
#print axioms GodelQ.GateBranches.hShift
#print axioms GodelQ.GateBranches.hAll
#print axioms GodelQ.GateBranches.hExs
#print axioms GodelQ.GateBranches.hAxm
#print axioms GodelQ.GateBranches.shCraigElim_of_obligations
#print axioms GodelQ.GateBranches.elim_at_godel_of_obligations
