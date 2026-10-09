import GodelQ.ZFC.TuringZFC
import GodelQ.Zeno.Runners

/-!
# CG-007 · W7（一）：想法 T 的一般形式——观察力不完备的两种形式与观察脚手架

研究发起人想法 T（十三条 [12]，KC-000074）【原话】：
“从更高精度的理论的视角去看，所谓的不完备，就是低精度理论的所谓的精度低，表现形式：维度缺失，或者维度不缺失，
但是理论在某个维度上的观察力不完备。”“在证明想法T的过程中，我们得到了一套观察任意理论的脚手架”。

下面是 AI 对这段定性论述的**形式化提案**（措辞与边界见 `CLAIM.md`）。一个观察者经接口 `π : X → Y` 看对象，
用接受集 `A : Y → Prop` 去确认一个“维度” `D : X → Prop`（一族事实）。

* `form_one_dimension_missing`（形式一，维度缺失）：接口把 D 上的差别压平了（有 `π x₁ = π x₂`，`D x₁` 而 `¬ D x₂`），
  则不存在经 π 的完备可靠观察者——不论它可不可计算。
* `form_two_observation_incomplete`（形式二，维度在、观察力不完备）：D 不可枚举，则每个可靠、可枚举的观察者
  都漏掉一个不可枚举、无穷的集合；它总能被严格加细，加细之后仍有漏点。
* `scaffold`（脚手架）：存在经 π 的可靠、完备、可枚举的观察者，当且仅当 D 在 π 的纤维上恒定，并且 D 可枚举。
  所以观察者的不完备恰有两个来源：接口看不见这一维（形式一），或这一维的真假不可枚举（形式二）。
* `two_forms_differ`：两者不是一回事。停机维度经恒等接口，纤维恒定（维度不缺失），完备可枚举的观察者仍不存在。
  所以“一切不完备都是维度缺失”不成立（GPT dev-09 #3 提过这句话，并指出需要明确假设）。

实例：停机维度（形式二，C-104；对 𝗭𝗙𝗖 见 `zfc_form_two`）；芝诺的极限接口（形式一，C-107）。
-/

namespace GodelQ.IdeaT

open Nat.Partrec Nat.Partrec.Code

section general

variable {X Y : Type}

/-- 观察者经接口 π、用接受集 A 确认维度 D：可靠。 -/
def Sound (π : X → Y) (A : Y → Prop) (D : X → Prop) : Prop := ∀ x, A (π x) → D x

/-- 完备。 -/
def Complete (π : X → Y) (A : Y → Prop) (D : X → Prop) : Prop := ∀ x, D x → A (π x)

/-- D 在 π 的纤维上恒定：接口看得见这一维。 -/
def FiberConstant (π : X → Y) (D : X → Prop) : Prop := ∀ x₁ x₂, π x₁ = π x₂ → (D x₁ ↔ D x₂)

/-- **形式一（维度缺失）**：接口压平了 D 上的差别，则经 π 的完备可靠观察者不存在。 -/
theorem form_one_dimension_missing (π : X → Y) (D : X → Prop)
    (h : ∃ x₁ x₂, π x₁ = π x₂ ∧ D x₁ ∧ ¬ D x₂) :
    ¬ ∃ A : Y → Prop, Sound π A D ∧ Complete π A D := by
  rintro ⟨A, hs, hc⟩
  obtain ⟨x₁, x₂, he, h1, h2⟩ := h
  exact h2 (hs x₂ (he ▸ hc x₁ h1))

theorem not_fiberConstant_iff (π : X → Y) (D : X → Prop) :
    ¬ FiberConstant π D ↔ ∃ x₁ x₂, π x₁ = π x₂ ∧ D x₁ ∧ ¬ D x₂ := by
  constructor
  · intro h
    by_contra hn
    apply h
    intro x₁ x₂ he
    constructor
    · intro h1
      by_contra h2
      exact hn ⟨x₁, x₂, he, h1, h2⟩
    · intro h2
      by_contra h1
      exact hn ⟨x₂, x₁, he.symm, h2, h1⟩
  · rintro ⟨x₁, x₂, he, h1, h2⟩ hf
    exact h2 ((hf x₁ x₂ he).mp h1)

end general

section effective

variable {X Y : Type} [Primcodable X]

/-- 有限集可枚举。 -/
theorem finite_re (S : Set X) (hS : S.Finite) : REPred (· ∈ S) := by
  refine Set.Finite.induction_on (motive := fun S _ => REPred (· ∈ S)) S hS ?_ ?_
  · exact (ComputablePred.to_re ⟨fun _ => instDecidableFalse, by simpa using (Computable.const false)⟩).of_eq
      fun e => by simp
  · intro a s _ _ ih
    exact (REPred.or' (ComputablePred.to_re (PrimrecPred.computablePred
      (Primrec.eq.comp Primrec.id (Primrec.const a)))) ih).of_eq fun e => by simp

/-- **形式二（维度在，观察力不完备）**：D 不可枚举，则每个可靠、可枚举的观察者（接口为恒等）漏掉的点
不可枚举、无穷；它可以被严格加细（多接受一个漏点，仍可靠、可枚举），加细之后仍有漏点。 -/
theorem form_two_observation_incomplete (D : X → Prop) (hD : ¬ REPred D)
    (A : X → Prop) (hA : REPred A) (hs : ∀ x, A x → D x) :
    ¬ REPred (· ∈ {x | D x ∧ ¬ A x}) ∧ {x | D x ∧ ¬ A x}.Infinite ∧
    ∃ A' : X → Prop, REPred A' ∧ (∀ x, A' x → D x) ∧ (∀ x, A x → A' x) ∧
      (∃ x, A' x ∧ ¬ A x) ∧ {x | D x ∧ ¬ A' x}.Nonempty := by
  have key : ∀ B : X → Prop, REPred B → (∀ x, B x → D x) → ¬ REPred (· ∈ {x | D x ∧ ¬ B x}) :=
    fun B hB hsB hM => hD ((REPred.or' hB hM).of_eq fun x => ⟨fun h => h.elim (hsB x) (·.1),
      fun hx => by
        by_cases hb : B x
        · exact Or.inl hb
        · exact Or.inr ⟨hx, hb⟩⟩)
  have inf : ∀ B : X → Prop, REPred B → (∀ x, B x → D x) → {x | D x ∧ ¬ B x}.Infinite :=
    fun B hB hsB hfin => key B hB hsB (finite_re _ hfin)
  obtain ⟨x₀, hx₀D, hx₀A⟩ := (inf A hA hs).nonempty
  let A' : X → Prop := fun x => A x ∨ x = x₀
  have hA' : REPred A' := REPred.or' hA (ComputablePred.to_re (PrimrecPred.computablePred
    (Primrec.eq.comp Primrec.id (Primrec.const x₀))))
  have hsA' : ∀ x, A' x → D x := fun x h => h.elim (hs x) (fun e => e ▸ hx₀D)
  exact ⟨key A hA hs, inf A hA hs, A', hA', hsA', fun x h => Or.inl h, ⟨x₀, Or.inr rfl, hx₀A⟩,
    (inf A' hA' hsA').nonempty⟩

/-- **脚手架**：存在经 π 的可靠、完备、可枚举的观察者，当且仅当 D 在 π 的纤维上恒定并且 D 可枚举。 -/
theorem scaffold (π : X → Y) (D : X → Prop) :
    (∃ A : Y → Prop, Sound π A D ∧ Complete π A D ∧ REPred (fun x => A (π x))) ↔
      (FiberConstant π D ∧ REPred D) := by
  constructor
  · rintro ⟨A, hs, hc, he⟩
    exact ⟨fun x₁ x₂ h => ⟨fun h1 => hs x₂ (h ▸ hc x₁ h1), fun h2 => hs x₁ (h.symm ▸ hc x₂ h2)⟩,
      he.of_eq fun x => ⟨hs x, hc x⟩⟩
  · rintro ⟨hf, hr⟩
    refine ⟨fun y => ∃ x, π x = y ∧ D x, fun x ⟨x', hx', hD⟩ => (hf x' x hx').mp hD,
      fun x hD => ⟨x, rfl, hD⟩, hr.of_eq fun x => ?_⟩
    exact ⟨fun hD => ⟨x, rfl, hD⟩, fun ⟨x', hx', hD⟩ => (hf x' x hx').mp hD⟩

end effective

/-! ## 实例 -/

/-- 停机维度，接口为恒等：纤维恒定（维度不缺失），而完备可枚举的观察者不存在——两种形式不是一回事。 -/
theorem two_forms_differ :
    FiberConstant (id : Process → Process) (fun e => ¬ Done e) ∧
    ¬ ∃ A : Process → Prop, Sound id A (fun e => ¬ Done e) ∧ Complete id A (fun e => ¬ Done e) ∧
      REPred (fun x => A (id x)) := by
  refine ⟨fun x₁ x₂ h => by simp only [id] at h; rw [h], fun h => never_done_not_re ?_⟩
  exact ((scaffold (id : Process → Process) (fun e => ¬ Done e)).mp h).2

/-- 停机维度上的形式二：任一可靠、可枚举的永不完成观察者（例如有效理论证明的“永不停”）。 -/
theorem halting_form_two (O : NeverObserver) :
    ¬ REPred (· ∈ {x | ¬ Done x ∧ ¬ O.accepts x}) ∧ {x | ¬ Done x ∧ ¬ O.accepts x}.Infinite ∧
    ∃ A' : Process → Prop, REPred A' ∧ (∀ x, A' x → ¬ Done x) ∧ (∀ x, O.accepts x → A' x) ∧
      (∃ x, A' x ∧ ¬ O.accepts x) ∧ {x | ¬ Done x ∧ ¬ A' x}.Nonempty :=
  form_two_observation_incomplete _ never_done_not_re O.accepts O.re O.sound

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory in
open GodelQ.ZFCNum GodelQ.ZFCEff in
/-- 𝗭𝗙𝗖 上的形式二：𝗭𝗙𝗖 证明的“永不停机”是可靠、可枚举的观察者，它的漏点不可枚举、无穷，加细也补不完。 -/
theorem zfc_form_two :
    ¬ REPred (· ∈ {x | ¬ Done x ∧ ¬ 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode x)}) ∧
    {x | ¬ Done x ∧ ¬ 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode x)}.Infinite :=
  ⟨(halting_form_two zfcEffective.observer).1, (halting_form_two zfcEffective.observer).2.1⟩

open GodelQ.Zeno in
/-- 芝诺的极限接口上的形式一：接口只交出极限值（`limUnder`），维度是“在某个有限阶段取到它”。
稠密跑者与量子化跑者的极限都是 1，取到与否不同，所以经极限接口的完备可靠观察者不存在（不论可不可计算）。 -/
theorem zeno_form_one :
    ¬ ∃ A : ℝ → Prop,
      Sound (fun s : ℕ → ℝ => Filter.limUnder Filter.atTop s) A
        (fun s => AttainsAt s (Filter.limUnder Filter.atTop s)) ∧
      Complete (fun s : ℕ → ℝ => Filter.limUnder Filter.atTop s) A
        (fun s => AttainsAt s (Filter.limUnder Filter.atTop s)) := by
  apply form_one_dimension_missing
  have h1 : Filter.limUnder Filter.atTop (quantPos 0) = 1 := (quantPos_arrives 0).limUnder_eq
  have h2 : Filter.limUnder Filter.atTop densePos = 1 := densePos_arrives.limUnder_eq
  refine ⟨quantPos 0, densePos, h1.trans h2.symm, ?_, ?_⟩
  · show AttainsAt (quantPos 0) (Filter.limUnder Filter.atTop (quantPos 0))
    rw [h1]; exact quantPos_attains 0
  · show ¬ AttainsAt densePos (Filter.limUnder Filter.atTop densePos)
    rw [h2]; exact densePos_not_attains

end GodelQ.IdeaT

#print axioms GodelQ.IdeaT.form_one_dimension_missing
#print axioms GodelQ.IdeaT.form_two_observation_incomplete
#print axioms GodelQ.IdeaT.scaffold
#print axioms GodelQ.IdeaT.two_forms_differ
#print axioms GodelQ.IdeaT.halting_form_two
#print axioms GodelQ.IdeaT.zfc_form_two
#print axioms GodelQ.IdeaT.zeno_form_one
