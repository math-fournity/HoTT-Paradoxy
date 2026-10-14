import GodelQ.ZFC.ShCraigElimSetup
/-!
裁决探针 4（**不是收据**）：检验本线 2026-10-13 首报的实质断言
"`↑Sh.reWitness` 与 `↑(Sh.craig).reWitness` 是不同公式（encode '' Sh vs encode '' Sh.craig）"。

`reWitness := .mkSigma (ISigma1.exists_matrix_provable T.reCh.sigma_prop).choose.val`、
`reCh := codeOfREPred (Encodable.encode '' T)`。两者只在 `Encodable.encode '' T`
这一项上不同：`encode '' Sh` vs `encode '' Sh.craig`。

结论（第一探针已定）：即使两者是不同**表达式**，`p ∈ (Sh.craig).Δ₁Class` 对应的
特征是 `Sh.reWitness`，因为 `(Sh.craig).Δ₁ch = Sh.craigCh` 而 `craigCh` 的
body 引用 `T.reWitness` 且 `T := Sh`。
本探针把这一点用现成定理再固定一次。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeAdjudicateCraig4

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 1. Sh.craig 的 Δ₁ch 就是 Sh.craigCh（rfl）
example : (Sh.craig).Δ₁ch = Sh.craigCh := rfl

-- 2. Δ₁Class 成员的最终归属：Sh.IsCraigAxiom
example (p : V) (h : p ∈ (Sh.craig).Δ₁Class) : Theory.IsCraigAxiom (V := V) Sh p :=
  ((Theory.IsCraigAxiom.defined (V := V) (T := Sh)).iff).mp h

example (p : V) (h : Theory.IsCraigAxiom (V := V) Sh p) : p ∈ (Sh.craig).Δ₁Class :=
  ((Theory.IsCraigAxiom.defined (V := V) (T := Sh)).iff).mpr h

-- 3. 它的定义性展开用的是 Sh.reWitness
example (p : V) :
    Theory.IsCraigAxiom (V := V) Sh p =
      (∃ s p' : V, p = p' ^⋏ qqVerums s ∧ (Semiformula.Evalb ![s, p']) ↑Sh.reWitness.val) := by
  rfl

end GodelQ.ProbeAdjudicateCraig4
