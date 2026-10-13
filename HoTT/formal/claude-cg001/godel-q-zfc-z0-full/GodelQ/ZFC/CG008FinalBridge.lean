import GodelQ.ZFC.CG008D3Chain

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008FinalBridge

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 桥：`Sh ⊢ sigma → 𝗜𝚺₁ ⊢ zfcTr sigma`

这是 `zfcTr.D1`（`Z0Full.lean:62` 的 `bew_def`）的直接后果：
    bew_def {sigma} : Sh ⊢ sigma → 𝗜𝚺₁ ⊢ zfcTr sigma

于是 `Sh.craig ⊢ sigma → 𝗜𝚺₁ ⊢ zfcTr sigma` 由 `Sh.craig ⪯ Sh` 给出。

**注意**：这是**外部**可证性（元层 `⊢`），不是内部的 `provabilityPred`。
本文件把它钉住。 -/

/-- **查实 1**：`zfcTr.D1`——`Sh ⊢ sigma → 𝗜𝚺₁ ⊢ zfcTr sigma`。 -/
example (sigma : ArithmeticSentence) (h : Sh ⊢ sigma) : 𝗜𝚺₁ ⊢ zfcTr sigma :=
  zfcTr.D1 h

/-- **查实 2**：经 `Sh.craig ⪯ Sh` 加强到 `Sh.craig`。 -/
example (sigma : ArithmeticSentence) (h : Sh.craig ⊢ sigma) : 𝗜𝚺₁ ⊢ zfcTr sigma :=
  zfcTr.D1 ((inferInstance : Sh.craig ⪯ Sh).wk h)

end GodelQ.CG008FinalBridge
