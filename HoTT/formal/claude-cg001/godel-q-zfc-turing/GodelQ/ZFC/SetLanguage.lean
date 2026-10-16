import Foundation.FirstOrder.Arithmetic.Bootstrapping.Syntax.Theory
import Foundation.FirstOrder.SetTheory.Basic.Misc
import Foundation.FirstOrder.Syntax.Classical.Eq

/-!
# CG-006 · S2a：集合论语言 ℒₛₑₜ 的三个语言实例

`ℒₛₑₜ` 没有函数符号；关系符号只有元数 2 的 `=`（编码 0）与 `∈`（编码 1）。据此给出
`LORDefinable`（符号集在算术中 𝚺₀ 可定义）、`Language.Primcodable`（编码解码原始递归）、
`Language.Finite`（等号公理组 `𝗘𝗤 ℒₛₑₜ` 因而是有限集）。
-/

namespace GodelQ.SetLang

open FFL FFL.FirstOrder

lemma func_range (k c : ℕ) :
    c ∈ Set.range (Encodable.encode : (ℒₛₑₜ).Func k → ℕ) ↔ False := by
  constructor
  · rintro ⟨f, _⟩; exact (f : Empty).elim
  · intro h; exact h.elim

lemma rel_range (k c : ℕ) :
    c ∈ Set.range (Encodable.encode : (ℒₛₑₜ).Rel k → ℕ) ↔ (k = 2 ∧ c = 0) ∨ (k = 2 ∧ c = 1) := by
  constructor
  · rintro ⟨r, rfl⟩
    cases r
    · exact Or.inl ⟨rfl, rfl⟩
    · exact Or.inr ⟨rfl, rfl⟩
  · rintro (⟨rfl, rfl⟩ | ⟨rfl, rfl⟩)
    · exact ⟨Language.Set.Rel.eq, rfl⟩
    · exact ⟨Language.Set.Rel.mem, rfl⟩

end GodelQ.SetLang

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic in
instance GodelQ.SetLang.lorDefinable : (ℒₛₑₜ).LORDefinable where
  func := .mkSigma “k f. ⊥”
  rel  := .mkSigma “k r. (k = 2 ∧ r = 0) ∨ (k = 2 ∧ r = 1)”
  func_iff {k c} := by simp [models_iff]
  rel_iff {k c} := by simpa [models_iff] using! GodelQ.SetLang.rel_range k c

open FFL FFL.FirstOrder in
instance GodelQ.SetLang.primcodable : Language.Primcodable ℒₛₑₜ where
  func := by
    refine (Primrec₂.const (0 : ℕ)).of_eq ?_
    intro k e
    rfl
  rel := by
    have h : Primrec fun p : ℕ × ℕ ↦ if p.1 = 2 ∧ p.2 < 2 then p.2 + 1 else 0 := by
      primrec
    refine h.of_eq ?_
    rintro ⟨k, e⟩
    match k, e with
    |     2,     0 => rfl
    |     2,     1 => rfl
    |     2, _ + 2 => simp [Encodable.decode]
    |     0,     _ => simp [Encodable.decode]
    |     1,     _ => simp [Encodable.decode]
    | _ + 3,     _ => simp [Encodable.decode]

open FFL FFL.FirstOrder in
instance GodelQ.SetLang.finite : Language.Finite ℒₛₑₜ where
  func := ⟨∅, fun x ↦ (x.2 : Empty).elim⟩
  rel := ⟨{⟨2, Language.Set.Rel.eq⟩, ⟨2, Language.Set.Rel.mem⟩}, fun ⟨k, r⟩ ↦ by cases r <;> simp⟩

open FFL FFL.FirstOrder in
example : Set.Finite (𝗘𝗤 ℒₛₑₜ) := Theory.EqAxiom.finite

#print axioms GodelQ.SetLang.lorDefinable
#print axioms GodelQ.SetLang.primcodable
#print axioms GodelQ.SetLang.finite
