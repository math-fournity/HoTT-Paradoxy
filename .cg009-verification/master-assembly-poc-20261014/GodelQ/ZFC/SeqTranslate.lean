import GodelQ.ZFC.InternalTranslate

/-!
# CG-007 · W8 第二层（一）：sequent 的翻译

把 sequent（公式码的集合）里的每个公式换成它的内部翻译 `iT 0`。

`setShift` 用 `sigma₁_replacement` 定义，这里照搬同一手法。这是第二层所有规则支的公共前置：
`Derivable Sh.craig s → Derivable 𝗭𝗙𝗖 (translateSeq s)`。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma translateSeq_existsUnique (s : V) :
    ∃! t : V, ∀ y, y ∈ t ↔ ∃ x ∈ s, y = iT (0 : V) x :=
  sigma₁_replacement (by definability) s

/-- sequent 的翻译：把每个公式码换成它的翻译码。 -/
noncomputable def translateSeq (s : V) : V := Classical.choose! (translateSeq_existsUnique s)

lemma mem_translateSeq_iff {s y : V} : y ∈ translateSeq s ↔ ∃ x ∈ s, y = iT (0 : V) x :=
  Classical.choose!_spec (translateSeq_existsUnique s) y

lemma translateSeq_graph (t s : V) :
    t = translateSeq s ↔
      (∀ y ∈ t, ∃ x ∈ s, y = iT (0 : V) x) ∧ (∀ x ∈ s, iT (0 : V) x ∈ t) := by
  constructor
  · rintro rfl
    exact ⟨fun y hy ↦ (mem_translateSeq_iff.mp hy), fun x hx ↦ mem_translateSeq_iff.mpr ⟨x, hx, rfl⟩⟩
  · rintro ⟨h₁, h₂⟩
    apply mem_ext; intro y; constructor
    · intro hy; exact mem_translateSeq_iff.mpr (h₁ y hy)
    · intro hy
      rcases mem_translateSeq_iff.mp hy with ⟨x, hx, rfl⟩
      exact h₂ x hx

noncomputable def translateSeqGraph : 𝚺ᴬ₁.Semisentence 2 := .mkSigma
  “t s. (∀ y ∈' t, ∃ x ∈' s, !iTDef y 0 x) ∧ (∀ x ∈' s, ∃ y, !iTDef y 0 x ∧ y ∈ t)”

instance translateSeq.defined : 𝚺ᴬ₁-Function₁[V] translateSeq via translateSeqGraph :=
  .mk fun v ↦ by simp [translateSeqGraph, translateSeq_graph]

instance translateSeq.definable : 𝚺ᴬ₁-Function₁[V] translateSeq := translateSeq.defined.to_definable

@[simp] lemma translateSeq_empty : translateSeq (∅ : V) = ∅ := by
  apply mem_ext; intro y
  simp [mem_translateSeq_iff]

@[simp] lemma translateSeq_insert {x s : V} :
    translateSeq (insert x s) = insert (iT (0 : V) x) (translateSeq s) := by
  apply mem_ext; intro y
  simp only [mem_translateSeq_iff, mem_bitInsert_iff]
  constructor
  · rintro ⟨z, (rfl | hz), rfl⟩
    · exact Or.inl rfl
    · exact Or.inr ⟨z, hz, rfl⟩
  · rintro (rfl | ⟨z, hz, rfl⟩)
    · exact ⟨x, Or.inl rfl, rfl⟩
    · exact ⟨z, Or.inr hz, rfl⟩

lemma translateSeq_union {s t : V} :
    translateSeq (s ∪ t) = translateSeq s ∪ translateSeq t := by
  apply mem_ext; intro y
  simp only [mem_translateSeq_iff, mem_cup_iff]
  constructor
  · rintro ⟨z, (hz | hz), rfl⟩
    · exact Or.inl ⟨z, hz, rfl⟩
    · exact Or.inr ⟨z, hz, rfl⟩
  · rintro (⟨z, hz, rfl⟩ | ⟨z, hz, rfl⟩)
    · exact ⟨z, Or.inl hz, rfl⟩
    · exact ⟨z, Or.inr hz, rfl⟩

lemma translateSeq_mono {s t : V} (h : ∀ x, x ∈ s → x ∈ t) :
    ∀ y, y ∈ translateSeq s → y ∈ translateSeq t := by
  intro y hy
  rcases mem_translateSeq_iff.mp hy with ⟨x, hx, rfl⟩
  exact mem_translateSeq_iff.mpr ⟨x, h x hx, rfl⟩

end GodelQ.SeqTranslate
