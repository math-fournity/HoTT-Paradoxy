import GodelQ.ZFC.Z0Bridge

/-! 探测：Bridge′ 的前两层能否干净落地。只做example,不产定理。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Z0Bridge GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.Z0Delta0Probe

-- 探测 A：命题连接词可交换(这是必然干净的一层)
example (φ ψ : ArithmeticSemisentence 0) :
    arithTrln.translate (φ ⋏ ψ) = arithTrln.translate φ ⋏ arithTrln.translate ψ := rfl

-- 探测 B：否定可交换
example (φ : ArithmeticSemisentence 0) :
    arithTrln.translate (∼φ) = ∼arithTrln.translate φ := by
  simp [DirectTranslation.translate]

-- 探测 C：存在量词相对化
example (φ : ArithmeticSemisentence 1) :
    arithTrln.translate (∃¹ φ) = ∃_[arithTrln] arithTrln.translate φ := rfl

-- 探测 D：全称量词相对化
example (φ : ArithmeticSemisentence 1) :
    arithTrln.translate (∀¹ φ) = ∀_[arithTrln] arithTrln.translate φ := rfl

-- 探测 E(关键)：ZFC 能否证明 ω 上的相等事实？即对标准 n，
-- ZFC ⊢ "ofNat m = ofNat n" 这种形状。先看 ZFC 对 numeral 的定义公式。
example : 𝗭𝗙𝗖 ⊢ “∀ x, !isEmpty x → !isEmpty x” := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp [models_iff]

end GodelQ.Z0Delta0Probe
