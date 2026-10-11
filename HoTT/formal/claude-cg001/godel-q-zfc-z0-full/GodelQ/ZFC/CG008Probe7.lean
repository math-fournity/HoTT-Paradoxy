import GodelQ.ZFC.CG008Probe6

/-!
# CG-008 探针 7（非收据）：分层测量两座桥的 elaboration 成本

`CG008Raw.lean` 想接的两座桥：
1. `tprovable_iff_provable`（`Typed.lean:168`）：`T.internalize V ⊢ σ ↔ Provable T σ.val`
2. `internal_provable_iff_internal_derivable`（`Basic.lean:939`）：
   `Provable T φ ↔ Derivable T (insert φ ∅ : V)`

逐条测，找出哪一步慢。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe7

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 桥 1（单独）：typed 内部可证性 → `Provable`
example {φ : Formula V ℒₛₑₜ} (h : 𝗭𝗙𝗖.internalize V ⊢ φ) : Provable 𝗭𝗙𝗖 φ.val :=
  (tprovable_iff_provable (T := 𝗭𝗙𝗖) (V := V)).mp h

-- 桥 2（单独）：`Provable` → `Derivable`（编码层）
example (ψ : V) : Provable 𝗭𝗙𝗖 ψ ↔ Derivable 𝗭𝗙𝗖 (insert ψ ∅ : V) :=
  internal_provable_iff_internal_derivable

end GodelQ.CG008Probe7
