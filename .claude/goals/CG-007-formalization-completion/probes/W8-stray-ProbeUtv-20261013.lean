import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsFinal
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### 不证一般保持引理，改用具体项的 IsUTerm 构造子

义务三实际需要的不是一般形，而是具体
`termSubstVec 2 ?[^&0] ?[^#0,^#0] = ?[^&0,^&0]`——bvar 代入成 fvar，
两者都有现成 IsUTerm 构造子，绕开 Foundation 缺的一般保持引理。 -/

/-! ### 小工具：`termSubst` 保 `IsUTerm`（Foundation 缺的那条）",
"",
"三支：bvar → `w.[z]`（用 `nth_termSubstVec_cons₂` + hv），fvar → `^&x`，func → `^func …`。
其中 func 支需要 `termSubstVec` 保 `IsUTermVec`（递归），故做成**同一个归纳**。",
"",
"先只做能立刻用的**前两支**，func 支留给后续（我的义务三只用 bvar/fvar）。 -/",
"",
"lemma termSubst_pres_bvar (w z : V) (h : IsUTerm " + LOR + " (^#z)) :",
"    IsUTerm " + LOR + " (termSubst " + LOR + " w (^#z)) := by",
"  rw [termSubst_bvar]",
"  sorry",
"",
"lemma termSubst_pres_fvar (w x : V) :",
"    IsUTerm " + LOR + " (termSubst " + LOR + " w (^&x)) := by",
"  rw [termSubst_fvar]",
"  exact IsUTerm.fvar x",
"",
"end GodelQ.ProbeExsFinal",
