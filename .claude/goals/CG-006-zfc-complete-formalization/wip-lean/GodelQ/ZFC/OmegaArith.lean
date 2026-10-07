import Foundation.FirstOrder.SetTheory.NaturalNumberRec

/-!
# CG-006 · S3a：Zermelo 模型的 ω 上的加法与乘法

在任意 `V ⊧ 𝗭` 中，用 Foundation 的 `NaturalNumberRec`（ω 上的递归，带可定义性）定义

* `add x y`：`add x 0 = x`，`add x (succ y) = succ (add x y)`；
* `mul x y`：`mul x 0 = 0`，`mul x (succ y) = add (mul x y) x`。

并证明它们在标准数字 `ofNat n` 上算得正确（只用元层归纳），以及
`x ∈ ofNat n ↔ ∃ i < n, x = ofNat i`、`ofNat` 单射。这些是“𝗥₀ 在 ZFC 模型的 ω 上成立”
所需的全部模型事实。
-/

namespace GodelQ.ZFCArith

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory

variable {V : Type*} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭]

/-! ## 加法 -/

def addBlueprint : NaturalNumberRec.Blueprint 1 := {
  zero := “z x. z = x”
  succ := “u z i x. !succ.dfn u z”
}

noncomputable def addC : NaturalNumberRec.Construction V addBlueprint := {
  zero := fun v ↦ v 0
  succ := fun _ _ z ↦ SetTheory.succ z
  zero_defined := ⟨fun v ↦ by simp [addBlueprint]⟩
  succ_defined := ⟨fun v ↦ succ.defined.eval_iff ![v 0, v 1]⟩
}

/-- ω 上的加法（`y ∉ ω` 时取 `∅`）。 -/
noncomputable def add (x y : V) : V := addC.result ![x] y

@[simp] lemma add_zero (x : V) : add x 0 = x := by
  simp [add, addC]

lemma add_succ (x : V) {y : V} (hy : y ∈ (ω : V)) :
    add x (SetTheory.succ y) = SetTheory.succ (add x y) := by
  simp [add, addC, NaturalNumberRec.Construction.result_succ _ _ hy]

/-! ## 乘法 -/

def mulBlueprint : NaturalNumberRec.Blueprint 1 := {
  zero := “z x. !isEmpty z”
  succ := “u z i x. !addBlueprint.resultDef u x z”
}

noncomputable def mulC : NaturalNumberRec.Construction V mulBlueprint := {
  zero := fun _ ↦ ∅
  succ := fun v _ z ↦ add z (v 0)
  zero_defined := ⟨fun v ↦ by
    simp [mulBlueprint, isEmpty_iff_eq_empty]⟩
  succ_defined := ⟨fun v ↦ by
    simp [mulBlueprint, add, addC.result_defined.iff, Matrix.vec_single_eq_const]⟩
}

/-- ω 上的乘法。 -/
noncomputable def mul (x y : V) : V := mulC.result ![x] y

@[simp] lemma mul_zero (x : V) : mul x 0 = ∅ := by
  simp [mul, mulC]

lemma mul_succ (x : V) {y : V} (hy : y ∈ (ω : V)) :
    mul x (SetTheory.succ y) = add (mul x y) x := by
  simp [mul, mulC, NaturalNumberRec.Construction.result_succ _ _ hy]

/-! ## 标准数字上的计算 -/

lemma ofNat_mem_ω' (m : ℕ) : (ofNat m : V) ∈ (ω : V) := ofNat_mem_ω m

lemma add_ofNat (n m : ℕ) : add (ofNat n : V) (ofNat m) = ofNat (n + m) := by
  induction m with
  | zero => exact add_zero _
  | succ m ih =>
    show add (ofNat n : V) (SetTheory.succ (ofNat m)) = SetTheory.succ (ofNat (n + m))
    rw [add_succ _ (ofNat_mem_ω' m), ih]

lemma mul_ofNat (n m : ℕ) : mul (ofNat n : V) (ofNat m) = ofNat (n * m) := by
  induction m with
  | zero => exact mul_zero _
  | succ m ih =>
    show mul (ofNat n : V) (SetTheory.succ (ofNat m)) = ofNat (n * (m + 1))
    rw [mul_succ _ (ofNat_mem_ω' m), ih, add_ofNat, Nat.mul_succ]

lemma mem_ofNat_iff (x : V) (n : ℕ) : x ∈ (ofNat n : V) ↔ ∃ i < n, x = ofNat i := by
  induction n with
  | zero => simp [ofNat]
  | succ n ih =>
    show x ∈ SetTheory.succ (ofNat n : V) ↔ _
    rw [mem_succ_iff, ih]
    constructor
    · rintro (h | ⟨i, hi, rfl⟩)
      · exact ⟨n, Nat.lt_succ_self n, h⟩
      · exact ⟨i, Nat.lt_succ_of_lt hi, rfl⟩
    · rintro ⟨i, hi, rfl⟩
      rcases Nat.lt_succ_iff_lt_or_eq.mp hi with h | rfl
      · exact Or.inr ⟨i, h, rfl⟩
      · exact Or.inl rfl

lemma ofNat_mem_ofNat {m n : ℕ} (h : m < n) : (ofNat m : V) ∈ (ofNat n : V) :=
  (mem_ofNat_iff _ n).mpr ⟨m, h, rfl⟩

lemma ofNat_injective : Function.Injective (ofNat : ℕ → V) := by
  intro m n h
  rcases lt_trichotomy m n with h₁ | h₁ | h₁
  · have := ofNat_mem_ofNat (V := V) h₁
    rw [h] at this
    exact False.elim <| mem_irrefl (ofNat n : V) this
  · exact h₁
  · have := ofNat_mem_ofNat (V := V) h₁
    rw [← h] at this
    exact False.elim <| mem_irrefl (ofNat m : V) this

/-! ## 对 ω 封闭（模型内的 ω 归纳） -/

lemma add_mem_ω {x y : V} (hx : x ∈ (ω : V)) (hy : y ∈ (ω : V)) : add x y ∈ (ω : V) := by
  refine naturalNumber_induction (fun y ↦ add x y ∈ (ω : V)) ?_ (by simpa using hx)
    (fun y hyω ih ↦ ?_) y hy
  · have : ℒₛₑₜ-function₁ (fun y : V ↦ add x y) := by
      refine ⟨⟨addBlueprint.resultDef.emb/[#0, #1, &x], ?_⟩⟩
      intro v
      simp [add, addC.result_defined (V := V).iff ![v 0, v 1, x]]
      simp [Matrix.vec_single_eq_const]
    definability
  · rw [add_succ _ hyω]; exact ω_succ_closed ih

lemma mul_mem_ω {x y : V} (hx : x ∈ (ω : V)) (hy : y ∈ (ω : V)) : mul x y ∈ (ω : V) := by
  refine naturalNumber_induction (fun y ↦ mul x y ∈ (ω : V)) ?_ (by simpa using zero_mem_ω)
    (fun y hyω ih ↦ ?_) y hy
  · have : ℒₛₑₜ-function₁ (fun y : V ↦ mul x y) := by
      refine ⟨⟨mulBlueprint.resultDef.emb/[#0, #1, &x], ?_⟩⟩
      intro v
      simp [mul, mulC.result_defined (V := V).iff ![v 0, v 1, x]]
      simp [Matrix.vec_single_eq_const]
    definability
  · rw [mul_succ _ hyω]; exact add_mem_ω ih hx

end GodelQ.ZFCArith

#print axioms GodelQ.ZFCArith.add_ofNat
#print axioms GodelQ.ZFCArith.mul_ofNat
#print axioms GodelQ.ZFCArith.mem_ofNat_iff
#print axioms GodelQ.ZFCArith.ofNat_injective
#print axioms GodelQ.ZFCArith.add_mem_ω
#print axioms GodelQ.ZFCArith.mul_mem_ω
