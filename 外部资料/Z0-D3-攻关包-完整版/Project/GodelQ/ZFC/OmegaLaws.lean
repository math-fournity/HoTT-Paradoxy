import GodelQ.ZFC.ArithInterp
import Foundation.FirstOrder.SetTheory.Ordinal

/-!
# CG-007 · W3（一）：Zermelo 模型的 ω 上的算术律与序

在任意 `V ⊧ 𝗭` 中，对 ω 的元素证明 `OmegaArith` 的加法、乘法满足 𝗣𝗔⁻ 所需的各条律：

* 加法：`zero_add`、`succ_add`、`add_comm`、`add_assoc`；
* 乘法：`zero_mul`、`mul_one`、`succ_mul`、`mul_comm`、`mul_add`、`mul_assoc`；
* 序（`<` 取 `∈`）：ω 的元素都是序数（Foundation 的 `IsOrdinal.nat`），于是有三分、传递、
  反自反；`succ_subset_of_mem`、`succ_mem_succ`、`add_mem_add`、`le_add`、`exists_add_of_subset`、
  `mul_mem_mul`。

每条用 ω 归纳（Foundation 的 `naturalNumber_induction`，归纳谓词须 ℒₛₑₜ 可定义）。为此先登记
加法、乘法作为二元函数的 ℒₛₑₜ 可定义性。
-/

namespace GodelQ.ZFCArith

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory

variable {V : Type*} [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭]

/-! ## 可定义性 -/

instance add_definable : ℒₛₑₜ-function₂[V] (add : V → V → V) := by
  refine ⟨⟨(funcDef Language.ORing.Func.add).emb, fun v => ?_⟩⟩
  obtain ⟨z, x, y, rfl⟩ : ∃ z x y : V, v = ![z, x, y] :=
    ⟨v 0, v 1, v 2, funext fun i => match i with | 0 => rfl | 1 => rfl | 2 => rfl⟩
  simpa using eval_funcDef_add (V := V) z x y

instance mul_definable : ℒₛₑₜ-function₂[V] (mul : V → V → V) := by
  refine ⟨⟨(funcDef Language.ORing.Func.mul).emb, fun v => ?_⟩⟩
  obtain ⟨z, x, y, rfl⟩ : ∃ z x y : V, v = ![z, x, y] :=
    ⟨v 0, v 1, v 2, funext fun i => match i with | 0 => rfl | 1 => rfl | 2 => rfl⟩
  simpa using eval_funcDef_mul (V := V) z x y

/-! ## 加法 -/

@[simp] lemma add_empty (x : V) : add x ∅ = x := add_zero x

@[simp] lemma mul_zero' (x : V) : mul x 0 = 0 := mul_zero x

@[simp] lemma mul_empty (x : V) : mul x ∅ = ∅ := mul_zero x

lemma zero_add {y : V} (hy : y ∈ (ω : V)) : add 0 y = y := by
  refine naturalNumber_induction (fun y ↦ add 0 y = y) ?_ ?_ ?_ y hy
  · definability
  · exact add_zero 0
  · intro y hyω ih
    rw [add_succ _ hyω, ih]

lemma succ_add (x : V) {y : V} (hy : y ∈ (ω : V)) :
    add (SetTheory.succ x) y = SetTheory.succ (add x y) := by
  refine naturalNumber_induction (fun y ↦ add (SetTheory.succ x) y = SetTheory.succ (add x y))
    ?_ ?_ ?_ y hy
  · definability
  · simp
  · intro y hyω ih
    rw [add_succ _ hyω, add_succ _ hyω, ih]

lemma add_comm' {x y : V} (hx : x ∈ (ω : V)) (hy : y ∈ (ω : V)) : add x y = add y x := by
  refine naturalNumber_induction (fun y ↦ add x y = add y x) ?_ ?_ ?_ y hy
  · definability
  · rw [add_zero, zero_add hx]
  · intro y hyω ih
    rw [add_succ _ hyω, ih, succ_add _ hx]

lemma add_assoc' (x y : V) {z : V} (hz : z ∈ (ω : V)) (hy : y ∈ (ω : V)) :
    add (add x y) z = add x (add y z) := by
  refine naturalNumber_induction (fun z ↦ add (add x y) z = add x (add y z)) ?_ ?_ ?_ z hz
  · definability
  · simp
  · intro z hzω ih
    rw [add_succ _ hzω, add_succ _ hzω, ih, add_succ _ (add_mem_ω hy hzω)]

/-! ## 乘法 -/

lemma zero_mul {y : V} (hy : y ∈ (ω : V)) : mul 0 y = 0 := by
  refine naturalNumber_induction (fun y ↦ mul 0 y = 0) ?_ ?_ ?_ y hy
  · definability
  · exact mul_zero 0
  · intro y hyω ih
    rw [mul_succ _ hyω, ih, add_zero]

lemma mul_one' {x : V} (hx : x ∈ (ω : V)) : mul x (SetTheory.succ 0) = x := by
  rw [mul_succ _ zero_mem_ω, mul_zero', zero_add hx]

lemma succ_mul {x : V} (hx : x ∈ (ω : V)) {y : V} (hy : y ∈ (ω : V)) :
    mul (SetTheory.succ x) y = add (mul x y) y := by
  refine naturalNumber_induction (fun y ↦ mul (SetTheory.succ x) y = add (mul x y) y)
    ?_ ?_ ?_ y hy
  · definability
  · simp
  · intro y hyω ih
    have hxy : mul x y ∈ (ω : V) := mul_mem_ω hx hyω
    rw [mul_succ _ hyω, ih, mul_succ _ hyω, add_succ _ hx, add_succ _ hyω,
      add_assoc' (mul x y) y hx hyω, add_assoc' (mul x y) x hyω hx, add_comm' hyω hx]

lemma mul_comm' {x y : V} (hx : x ∈ (ω : V)) (hy : y ∈ (ω : V)) : mul x y = mul y x := by
  refine naturalNumber_induction (fun y ↦ mul x y = mul y x) ?_ ?_ ?_ y hy
  · definability
  · rw [mul_zero', zero_mul hx]
  · intro y hyω ih
    rw [mul_succ _ hyω, ih, succ_mul hyω hx]

lemma mul_add' {x y : V} (hx : x ∈ (ω : V)) (hy : y ∈ (ω : V)) {z : V} (hz : z ∈ (ω : V)) :
    mul x (add y z) = add (mul x y) (mul x z) := by
  refine naturalNumber_induction (fun z ↦ mul x (add y z) = add (mul x y) (mul x z))
    ?_ ?_ ?_ z hz
  · definability
  · simp
  · intro z hzω ih
    rw [add_succ _ hzω, mul_succ _ (add_mem_ω hy hzω), ih, mul_succ _ hzω,
      add_assoc' _ _ hx (mul_mem_ω hx hzω)]

lemma mul_assoc' {x y : V} (hx : x ∈ (ω : V)) (hy : y ∈ (ω : V)) {z : V} (hz : z ∈ (ω : V)) :
    mul (mul x y) z = mul x (mul y z) := by
  refine naturalNumber_induction (fun z ↦ mul (mul x y) z = mul x (mul y z)) ?_ ?_ ?_ z hz
  · definability
  · simp
  · intro z hzω ih
    rw [mul_succ _ hzω, ih, mul_succ _ hzω, mul_add' hx (mul_mem_ω hy hzω) hy]

/-! ## 序 -/

lemma isOrdinal_of_mem_ω {x : V} (hx : x ∈ (ω : V)) : IsOrdinal x := IsOrdinal.nat hx

lemma mem_ω_of_mem {x y : V} (hy : y ∈ (ω : V)) (hxy : x ∈ y) : x ∈ (ω : V) :=
  IsTransitive.mem_trans IsTransitive.ω hxy hy

lemma lt_trans' {x y z : V} (hz : z ∈ (ω : V)) (hxy : x ∈ y) (hyz : y ∈ z) : x ∈ z :=
  IsTransitive.mem_trans (IsTransitive.nat hz) hxy hyz

lemma lt_trichotomy' {x y : V} (hx : x ∈ (ω : V)) (hy : y ∈ (ω : V)) : x ∈ y ∨ x = y ∨ y ∈ x := by
  have := isOrdinal_of_mem_ω hx
  have := isOrdinal_of_mem_ω hy
  exact IsOrdinal.mem_trichotomy (V := V) (α := x) (β := y)

lemma subset_iff_eq_or_mem {x y : V} (hx : x ∈ (ω : V)) (hy : y ∈ (ω : V)) :
    x ⊆ y ↔ x = y ∨ x ∈ y := by
  have := isOrdinal_of_mem_ω hx
  have := isOrdinal_of_mem_ω hy
  exact IsOrdinal.subset_iff (V := V) (α := x) (β := y)

lemma zero_le' {x : V} (hx : x ∈ (ω : V)) : 0 = x ∨ 0 ∈ x :=
  (subset_iff_eq_or_mem zero_mem_ω hx).mp (by simp [zero_def])

lemma succ_subset_of_mem {x y : V} (hy : y ∈ (ω : V)) (hxy : x ∈ y) : SetTheory.succ x ⊆ y := by
  intro z hz
  rcases mem_succ_iff.mp hz with rfl | hz
  · exact hxy
  · exact lt_trans' hy hz hxy

lemma succ_mem_succ {x y : V} (hy : y ∈ (ω : V)) (hxy : x ∈ y) :
    SetTheory.succ x ∈ SetTheory.succ y := by
  rcases (subset_iff_eq_or_mem (ω_succ_closed (mem_ω_of_mem hy hxy)) hy).mp
    (succ_subset_of_mem hy hxy) with h | h
  · rw [h]; exact mem_succ_iff.mpr (Or.inl rfl)
  · exact mem_succ_iff.mpr (Or.inr h)

lemma add_mem_add {x y : V} (hy : y ∈ (ω : V)) (hxy : x ∈ y) {z : V} (hz : z ∈ (ω : V)) :
    add x z ∈ add y z := by
  refine naturalNumber_induction (fun z ↦ add x z ∈ add y z) ?_ ?_ ?_ z hz
  · definability
  · simpa using hxy
  · intro z hzω ih
    rw [add_succ _ hzω, add_succ _ hzω]
    exact succ_mem_succ (add_mem_ω hy hzω) ih

lemma le_add {x : V} (hx : x ∈ (ω : V)) {z : V} (hz : z ∈ (ω : V)) : z ⊆ add x z := by
  refine naturalNumber_induction (fun z ↦ z ⊆ add x z) ?_ ?_ ?_ z hz
  · definability
  · simp [zero_def]
  · intro z hzω ih
    rw [add_succ _ hzω]
    intro w hw
    rcases mem_succ_iff.mp hw with rfl | hw
    · rcases (subset_iff_eq_or_mem hzω (add_mem_ω hx hzω)).mp ih with h | h
      · exact mem_succ_iff.mpr (Or.inl h)
      · exact mem_succ_iff.mpr (Or.inr h)
    · exact mem_succ_iff.mpr (Or.inr (ih w hw))

lemma subset_succ_iff' {x y : V} (hx : x ∈ (ω : V)) (hy : y ∈ (ω : V)) :
    x ⊆ SetTheory.succ y ↔ x = SetTheory.succ y ∨ x ⊆ y := by
  rw [subset_iff_eq_or_mem hx (ω_succ_closed hy), subset_iff_eq_or_mem hx hy, mem_succ_iff]

lemma exists_add_of_subset {x : V} (hx : x ∈ (ω : V)) {y : V} (hy : y ∈ (ω : V)) :
    x ⊆ y → ∃ z ∈ (ω : V), add x z = y := by
  refine naturalNumber_induction (fun y ↦ x ⊆ y → ∃ z ∈ (ω : V), add x z = y) ?_ ?_ ?_ y hy
  · definability
  · intro h
    have : x = 0 := by
      rcases (subset_iff_eq_or_mem hx zero_mem_ω).mp h with h | h
      · exact h
      · simp [zero_def] at h
    exact ⟨0, zero_mem_ω, by rw [this, add_zero]⟩
  · intro y hyω ih h
    rcases (subset_succ_iff' hx hyω).mp h with h | h
    · exact ⟨0, zero_mem_ω, by rw [add_zero, h]⟩
    · obtain ⟨z, hzω, hz⟩ := ih h
      exact ⟨SetTheory.succ z, ω_succ_closed hzω, by rw [add_succ _ hzω, hz]⟩

lemma eq_zero_or_succ {z : V} (hz : z ∈ (ω : V)) :
    z = 0 ∨ ∃ w ∈ (ω : V), z = SetTheory.succ w := by
  refine naturalNumber_induction (fun z ↦ z = 0 ∨ ∃ w ∈ (ω : V), z = SetTheory.succ w)
    ?_ ?_ ?_ z hz
  · definability
  · exact Or.inl rfl
  · intro z hzω _
    exact Or.inr ⟨z, hzω, rfl⟩

lemma mul_mem_mul_succ {x y : V} (hy : y ∈ (ω : V)) (hxy : x ∈ y) {w : V} (hw : w ∈ (ω : V)) :
    mul x (SetTheory.succ w) ∈ mul y (SetTheory.succ w) := by
  have hx : x ∈ (ω : V) := mem_ω_of_mem hy hxy
  refine naturalNumber_induction (fun w ↦ mul x (SetTheory.succ w) ∈ mul y (SetTheory.succ w))
    ?_ ?_ ?_ w hw
  · definability
  · rw [mul_one' hx, mul_one' hy]; exact hxy
  · intro w hwω ih
    have hw1 := ω_succ_closed hwω
    rw [mul_succ _ hw1, mul_succ _ hw1]
    have hb : mul y (SetTheory.succ w) ∈ (ω : V) := mul_mem_ω hy hw1
    have h1 : add (mul x (SetTheory.succ w)) x ∈ add (mul y (SetTheory.succ w)) x :=
      add_mem_add hb ih hx
    have h2 : add (mul y (SetTheory.succ w)) x ∈ add (mul y (SetTheory.succ w)) y := by
      rw [add_comm' hb hx, add_comm' hb hy]
      exact add_mem_add hy hxy hb
    exact lt_trans' (add_mem_ω hb hy) h1 h2

lemma mul_mem_mul {x y z : V} (hy : y ∈ (ω : V)) (hxy : x ∈ y) (hz : z ∈ (ω : V)) (h0 : 0 ∈ z) :
    mul x z ∈ mul y z := by
  rcases eq_zero_or_succ hz with rfl | ⟨w, hw, rfl⟩
  · simp [zero_def] at h0
  · exact mul_mem_mul_succ hy hxy hw

end GodelQ.ZFCArith

#print axioms GodelQ.ZFCArith.add_comm'
#print axioms GodelQ.ZFCArith.add_assoc'
#print axioms GodelQ.ZFCArith.mul_comm'
#print axioms GodelQ.ZFCArith.mul_assoc'
#print axioms GodelQ.ZFCArith.mul_add'
#print axioms GodelQ.ZFCArith.lt_trichotomy'
#print axioms GodelQ.ZFCArith.exists_add_of_subset
#print axioms GodelQ.ZFCArith.mul_mem_mul
