import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `ExsBridge2` 的 `p = ⊤` 情形：**语义路线完整证明**（2026-10-13）

目标：`Provable 𝗭𝗙𝗖 (^∃ (domZero ⋏ ⊤))`（即「ω 非空」）。

**路线**：`SetTheory.complete` 把 `𝗭𝗙𝗖 ⊢ σ` 化为「在每个 𝗭𝗙𝗖 模型里成立」，
而「ω 非空」由 `zero_mem_ω` 给出。再经 `tprovable_tquote_iff_provable_quote_sentence`
的多态版接回 `Provable`。

**本探针证出第一步（元层 `⊢`）——exit 0**：

```
theorem omega_nonempty_provable :
    (𝗭𝗙𝗖 : SetTheory) ⊢ (∃¹ (domainDef ⋏ ⊤) : SetTheorySentence)
```

证法：`SetTheory.complete` → 取 `x = 0` → `eval_domainDef` + `zero_mem_ω` + `EvalAux` 展开。

**意义**：这是语义路线在**具体情形**下的**首个落地定理**，
证明「`complete` + 模型论证」这条链在本项目里**可用**。

**重要**：这条证明**与反向引理无关**——`p = ⊤` 是**具体**的，
`domainDef` 是 Foundation 里现成的 `SetTheorySemisentence`。
故它**不受非标准码反例影响**，可作为语义路线可行性的**独立验证**。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeBridge2TopProof

open FFL FFL.FirstOrder FFL.FirstOrder.SetTheory

/-- **「ω 非空」在 𝗭𝗙𝗖 中可证**（元层）。 -/
theorem omega_nonempty_provable :
    (𝗭𝗙𝗖 : SetTheory) ⊢ (∃¹ ((ZFCArith.domainDef : SetTheorySemisentence 1) ⋏ ⊤) : SetTheorySentence) := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  simp only [models_iff]
  -- 目标：存在 x 使 `x ∈ ω`；由 `zero_mem_ω` 给 `0 ∈ ω`
  refine ⟨0, ?_⟩
  -- 目标是 `EvalAux (…) ![0] (domainDef ⋏ ⊤)`；
  -- 用 `eval_domainDef`（它是 `Evalb` 层，即 `Eval` 的 `Empty.elim` 版）
  have h0 : Semiformula.EvalAux (standardStructure M) Empty.elim ![(0 : M)]
      (ZFCArith.domainDef) := (ZFCArith.eval_domainDef (V := M) 0).mpr SetTheory.zero_mem_ω
  show Semiformula.EvalAux (standardStructure M) Empty.elim ![(0 : M)]
      (ZFCArith.domainDef ⋏ ⊤)
  rw [show (ZFCArith.domainDef ⋏ (⊤ : Semiformula ℒₛₑₜ Empty 1))
        = Semiformula.and ZFCArith.domainDef ⊤ from rfl]
  simp only [Semiformula.EvalAux]
  exact ⟨h0, trivial⟩

end ProbeBridge2TopProof

#print axioms ProbeBridge2TopProof.omega_nonempty_provable