import GodelQ.ZFC.ShCraigElimSetup
/-!
裁决探针 2（**不是收据**）：把"两个 reWitness 是不是同一条公式"也定掉。

第 1 探针已定：`p ∈ (Sh.craig).Δ₁Class ↔ Theory.IsCraigAxiom (T := Sh) p`，
`(Sh.craig).Δ₁ch = Sh.craigCh`（`rfl`），`craigCh` 的 body 引用 `Sh.reWitness`。
所以成员对应的特征是 `Sh.reWitness`。本探针问：`Sh.reWitness` 与 `(Sh.craig).reWitness`
是不是**同一条**公式（definitional 相等），以及 `axm` 支要用的 V 层接口 `reWitness_spec`。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeAdjudicateCraig2

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

#check @Theory.reWitness_spec

-- 两个 reWitness 的差别只在 `Encodable.encode '' T`：Sh 与 Sh.craig 不同（craig 严格更大）
#check (Sh.reWitness : 𝚺ᴬ₀.Semisentence 2)
#check ((Sh.craig).reWitness : 𝚺ᴬ₀.Semisentence 2)
#check (Sh.reCh : 𝚺ᴬ₁.Semisentence 1)
#check ((Sh.craig).reCh : 𝚺ᴬ₁.Semisentence 1)

-- `axm` 支真正要用的 V 层接口（T := Sh）
example (e : Fin 1 → V) :
    V ⊧/e Sh.reCh.val ↔ ∃ w, V ⊧/(w :> e) Sh.reWitness.val :=
  Theory.reWitness_spec (T := Sh) (L := ℒₒᵣ) V e

end GodelQ.ProbeAdjudicateCraig2
