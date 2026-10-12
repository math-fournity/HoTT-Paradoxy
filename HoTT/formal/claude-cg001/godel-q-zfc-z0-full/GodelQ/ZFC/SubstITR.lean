import GodelQ.ZFC.ITSubsts1

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.ITSubsts1

set_option maxHeartbeats 4000000

/-!
# CG-007 · W8 第二层（十七·附二）：`subst` 穿过原子翻译 `iTR`

公式层桥 `iT_substs1` 的**原子支**所需。`iTR n R v` 是

```
qqAlls (imp (conjunct 2 n 0 (iVE n v.[0]) ⋏ (conjunct 2 n 1 (iVE n v.[1]) ⋏ ⊤))
          (subst ?[^#0,^#1] (cRel R))) 2
```

先推两层 `qqAlls`（`subst_qqAlls_two`），拆 `imp`（`subst_imp`），
最内层的 `subst (qVec (qVec w)) (subst ?[^#0,^#1] (cRel R))` 用
`substs_substs` 并成**一次**代换，向量 `termSubstVec 2 (qVec (qVec w)) ?[^#0,^#1]`。

四个 `conjunct` **不在本引理内做**——那是 `ve2` 支已走过的路
（`subst_conjunct` ×4 + 归纳假设），留给调用方按需展开。
-/

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `subst` 穿过 `iTR`：照 `subst_ve2` 的形状。
`iTR n R v = qqAlls (imp (conjunct 2 n 0 (iVE n v.[0]) ⋏ (conjunct 2 n 1 (iVE n v.[1]) ⋏ ⊤))
                        (subst ?[^#0,^#1] (cRel R))) 2` -/
lemma subst_iTR {n R v m w : V} (h0 : IsSemiformula ℒₛₑₜ (n + 1) (iVE n v.[0]))
    (h1 : IsSemiformula ℒₛₑₜ (n + 1) (iVE n v.[1]))
    (hw : IsSemitermVec ℒₛₑₜ (2 + n) m (qVec ℒₛₑₜ (qVec ℒₛₑₜ w))) :
    subst ℒₛₑₜ w (iTR n 2 R v) =
      qqAlls (imp ℒₛₑₜ
        (subst ℒₛₑₜ (qVec ℒₛₑₜ (qVec ℒₛₑₜ w))
            (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤)))
        (subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 2 (qVec ℒₛₑₜ (qVec ℒₛₑₜ w)) (?[^#0, ^#1] : V))
          (cRel R))) 2 := by
  have hA : IsSemiformula ℒₛₑₜ (2 + n)
      (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤)) :=
    IsSemiformula.and.mpr ⟨isSemiformula_conjunct h0 (zero_lt_two_add n),
      IsSemiformula.and.mpr ⟨isSemiformula_conjunct h1 (one_lt_two_add n),
        IsSemiformula.verum⟩⟩
  have hv2 : IsSemitermVec ℒₛₑₜ 2 2 (?[^#0, ^#1] : V) := by
    rw [show (?[^#0, ^#1] : V) = ((^#0 : V) ∷ ((^#1 : V) ∷ (0 : V))) from rfl]
    rw [show (2 : V) = 1 + 1 by norm_num, IsSemitermVec.cons_iff]
    exact ⟨IsSemiterm.bvar.mpr (by norm_num), by simp⟩
  have hF : IsSemiformula ℒₛₑₜ (2 + n) (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) :=
    isSemiformula_mono (IsSemiformula.subst (isSemiformula_cRel R) hv2) (by
      have h := le_add_self (a := (2 : V)) (b := n)
      rwa [show n + 2 = 2 + n by ring] at h)
  have hw2 : IsSemitermVec ℒₛₑₜ (2 + n) m (qVec ℒₛₑₜ (qVec ℒₛₑₜ w)) := hw
  have hmono : IsSemitermVec ℒₛₑₜ 2 (2 + n) (?[^#0, ^#1] : V) := by
    have h := le_add_self (a := (2 : V)) (b := n)
    exact isSemitermVec_mono hv2 (by rwa [show n + 2 = 2 + n by ring] at h)
  rw [iTR, subst_qqAlls_two (IsUFormula.imp.mpr ⟨hA.isUFormula, hF.isUFormula⟩),
    subst_imp (n := 2 + n) (m := m) hA hF hw2,
    substs_substs (l := 2) (n := 2 + n) (m := m) (p := cRel R)
      (isSemiformula_cRel R) hw2 hmono]

end GodelQ.ITSubsts1
