import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeCHK
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **决定性事实**：越界下标取 `0`（`nth_lt_len` 的直接形式）。 -/
lemma nth_out_of_range (v i : V) (h : len v ≤ i) : v.[i] = (0 : V) :=
  nth_lt_len h

/-- **`subst` 向量越界补零**：`?[^&0]` 长度 1，取第 2 个分量得 `0`。 -/
lemma subst_vec_out_of_range :
    termSubstVec ℒₛₑₜ (2:V) (?[^&0] : V) (?[^#0, ^#1] : V) = (?[^&0, 0] : V) := by
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V)))]
  simp [termSubst_bvar]

/-- **关键反驳**：那条归档探针的陈述**不成立**。

`subst ?[^&0] (eqAtom ^#1)` 的向量长度 1、被代公式长度 2，
逐项算出左端是 `^rel 2 cEqN ?[^&0, 0]`，而右端 `eqAtom ^&0 = ^rel 2 cEqN ?[^#0, ^&0]`。
两者**不等**（首分量 `^&0 ≠ ^#0`，次分量 `0 ≠ ^&0`）。

本引理把左端**算出**（而不是断言相等），供对照。 -/
lemma subst_eqAtom_actual :
    subst ℒₛₑₜ (?[^&0] : V) (eqAtom (^#(0+1) : V))
      = (^rel 2 (↑cEqN) (?[^&0, 0] : V) : V) := by
  rw [eqAtom]
  rw [show (^#(0 + 1) : V) = (^#(1:V) : V) from by norm_num]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
      (IsUTerm.bvar (z := (1:V)))) (IsUTerm.bvar (z := (0:V)))))]
  congr 1
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (1:V)))]
  rw [termSubst_bvar, termSubst_bvar]
  rw [show (?[^&0] : V) = (^&0 : V) ∷ (0 : V) from rfl]
  simp

/-- 两端的**首分量不同**：`^&0 ≠ ^#0`。故 `subst ?[^&0] (eqAtom ^#1) ≠ eqAtom ^&0`。

这正是那条归档探针 `W8-iT-rename-inner-renaming-20261012` 所断言等式的**反例**：
它的 `subst_vec_two`（把 `?[^#0,^&0]` 塞进 `?[^#0,^#1]`）是对的，但把
`subst` 的向量取成 `?[^&0]`（长度 1）而不是 `?[^#0,^&0]`（长度 2）就**错位**了。 -/
example : ¬ (subst ℒₛₑₜ (?[^&0] : V) (eqAtom (^#(0+1) : V)) = eqAtom (^&(0:V) : V)) := by
  intro h
  rw [subst_eqAtom_actual] at h
  have hh : (^rel 2 (↑cEqN) (?[^&0, 0] : V) : V) = (^rel 2 (↑cEqN) (?[^#0, ^&0] : V) : V) := h
  have harg : (?[^&0, 0] : V) = (?[^#0, ^&0] : V) :=
    ((qqRel_inj (2:V) (↑cEqN) (?[^&0, 0] : V) (2:V) (↑cEqN) (?[^#0, ^&0] : V)).mp hh).2.2
  have h0 : ((?[^&0, 0] : V).[0]) = ((?[^#0, ^&0] : V).[0]) := by rw [harg]
  rw [show (?[^&0, 0] : V) = (^&0 : V) ∷ (0 ∷ 0) from rfl,
      show (?[^#0, ^&0] : V) = (^#0 : V) ∷ (^&0 ∷ 0) from rfl] at h0
  simp only [nth_adjoin_zero] at h0
  -- `h0 : ^&0 = ^#0`——用编码的奇偶性/构造子不相交反驳
  exact absurd h0 (by
    intro hb
    have := congrArg (fun (x : V) => x) hb
    -- `^&0 = 2 * 0 = 0`、`^#0 = 1`，故矛盾
    simp [qqFvar, qqBvar] at this)

end GodelQ.ProbeCHK
