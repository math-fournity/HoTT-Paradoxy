import GodelQ.ZFC.InternalTranslate

/-! 负控制：翻译把算术解释在 ω 上，量词必须限制到 ω（`domain`）。把内部翻译的量词步写成
不带定义域限制的 `^∀ ⌜φ⌝`，与翻译的编码不符：改写之后剩下的目标
`^∀ (imp ℒₛₑₜ domZero ⌜φ⌝) = ^∀ ⌜φ⌝` 不能自动闭合，Lean 必须拒绝。这表明 `iT_quote` 的量词情形
确实核对了 ω 限制，而不是把它当作记号略去。 -/

namespace GodelQ.TranslateNeg

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.Translate GodelQ.ZFCArith
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma wrong_quote_fal_no_domain {n : ℕ} (φ : Semisentence ℒₛₑₜ (n + 1)) :
    (⌜(DirectTranslation.fal arithTrln φ : Semisentence ℒₛₑₜ n)⌝ : V) = ^∀ ⌜φ⌝ := by
  rw [DirectTranslation.fal, FFL.FirstOrder.ball, Sentence.quote_all, quote_imp', quote_domain_zero]

end GodelQ.TranslateNeg
