import GodelQ.ZFC.Z0D3
import GodelQ.OmegaQuestion

/-!
# CG-010 R9：Z0 作为具体的 ω 追问（CG001-C-427）

研究发起人十三条 [1]（KC-000063）说“Q0（H0（Z0））……H0在ZFC中的对应物Z0”。C-93（Lean）把芝诺、
H0、Z0 放进同一个 ω 追问图式时，Z0 只以“某个过程”的形式出现；C-112、C-113（Cubical Agda）里 Z0 是
参数。本文件把 Z0 写成 Lean 里一个具体的 ω 追问：

* `z0Code`：一个程序，按编号逐个检查 𝗭𝗙𝗖 的证明，找到 ⊥ 的证明就停。它由 C-111 的
  `zfc_provable_re`（𝗭𝗙𝗖 的定理集可枚举）给出：`Done z0Code ↔ 𝗭𝗙𝗖 ⊢ ⊥`。
* `z0Q := processQ z0Code`：第 k 问是“到第 k 步，找到 𝗭𝗙𝗖 的矛盾了吗”。与芝诺的 `zenoQ` 同一个
  类型 `OmegaQuestion`、同一个图式（C-93）。

于是：

* Z0 永不落定（元层，由 Foundation 的 `zfc_consistent`，即 Lean 元层的 `Universe` 模型）；
* 𝗭𝗙𝗖 每一刻都确认“到第 k 步还没找到”（`zfcEffective.observes_every_instant`，C-87 的 𝗭𝗙𝗖 实例）；
* Foundation 的一致性句 `𝗭𝗙𝗖.consistent` 在 ℕ 中为真，恰好当 Z0 永不落定；
* 𝗭𝗙𝗖 证明不了这句话的翻译（C-417，`zfc_z0_unconditional`）；
* P_fin 在 Z0 上被否定：“全部证明的集合”这个完成的整体，不给出某一步的完成；由 Z0 驱动的
  哥德尔–芝诺跑者到达。

与 Agda 里的 H0 之间仍是跨内核的对应，不是同一个对象。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open Nat.Partrec

namespace GodelQ.Z0Omega

open GodelQ GodelQ.ZFCZ0 GodelQ.ZFCEff GodelQ.ZFCArith

/-- 有一个程序，它停机当且仅当 𝗭𝗙𝗖 证明 ⊥（由 𝗭𝗙𝗖 的定理集可枚举，C-111）。 -/
theorem exists_z0_code : ∃ c : Code, (Code.eval c 0).Dom ↔ 𝗭𝗙𝗖 ⊢ (⊥ : Sentence ℒₛₑₜ) := by
  have hg : Partrec (fun _ : ℕ => Part.assert (𝗭𝗙𝗖 ⊢ (⊥ : Sentence ℒₛₑₜ)) fun _ => Part.some ()) :=
    zfc_provable_re.comp (Computable.const (⊥ : Sentence ℒₛₑₜ))
  obtain ⟨c, hc⟩ := Code.exists_code.1 hg
  refine ⟨c, ?_⟩
  rw [hc]
  simp only [Encodable.decode_nat, Part.coe_some, Part.bind_some, Part.map_Dom]
  exact ⟨fun ⟨h, _⟩ => h, fun h => ⟨h, trivial⟩⟩

/-- Z0 的程序：逐个检查 𝗭𝗙𝗖 的证明，找到 ⊥ 的证明就停。 -/
noncomputable def z0Code : Process := Classical.choose exists_z0_code

theorem z0Code_done_iff : Done z0Code ↔ 𝗭𝗙𝗖 ⊢ (⊥ : Sentence ℒₛₑₜ) :=
  Classical.choose_spec exists_z0_code

/-- Z0：第 k 问“到第 k 步，找到 𝗭𝗙𝗖 的矛盾了吗”。 -/
noncomputable def z0Q : OmegaQuestion := processQ z0Code

theorem z0Q_done_iff : z0Q.Done ↔ 𝗭𝗙𝗖 ⊢ (⊥ : Sentence ℒₛₑₜ) :=
  (processQ_done_iff z0Code).trans z0Code_done_iff

/-- Z0 的程序永不停机（元层：𝗭𝗙𝗖 一致，由 Lean 元层的 `Universe` 模型）。 -/
theorem z0Code_not_done : ¬ Done z0Code := fun h =>
  Entailment.Consistent.not_bot (𝓢 := 𝗭𝗙𝗖) (z0Code_done_iff.mp h)

/-- Z0 永不落定。 -/
theorem z0Q_never : z0Q.Never :=
  (OmegaQuestion.never_iff z0Q).mpr fun h => z0Code_not_done ((processQ_done_iff z0Code).mp h)

/-- 𝗭𝗙𝗖 每一刻都确认“到第 k 步还没找到矛盾”：`𝗭𝗙𝗖 ⊢ haltsS ΨN ⌜(z0Code, k)⌝`。 -/
theorem zfc_confirms_every_stage (k : ℕ) : zfcEffective.provesNotYet z0Code k :=
  zfcEffective.observes_every_instant z0Code z0Code_not_done k

/-- Foundation 的一致性句在 ℕ 中为真，恰好当 Z0 永不落定。 -/
theorem consistent_true_iff_z0_never :
    (𝗭𝗙𝗖.consistent : ArithmeticSentence).Evalb (M := ℕ) ![] ↔ z0Q.Never := by
  rw [consistent.defined, OmegaQuestion.never_iff, z0Q_done_iff]
  simp [Theory.Consistent]

/-- 一致性句在 ℕ 中为真。 -/
theorem consistent_true : (𝗭𝗙𝗖.consistent : ArithmeticSentence).Evalb (M := ℕ) ![] :=
  consistent_true_iff_z0_never.mpr z0Q_never

/-- 由 Z0 驱动的哥德尔–芝诺跑者到达。 -/
theorem z0_runner_arrives : Arrives z0Code :=
  (processQ_never_iff_arrives z0Code).mp z0Q_never

end GodelQ.Z0Omega

#print axioms GodelQ.Z0Omega.exists_z0_code
#print axioms GodelQ.Z0Omega.z0Q_never
#print axioms GodelQ.Z0Omega.zfc_confirms_every_stage
#print axioms GodelQ.Z0Omega.consistent_true_iff_z0_never
#print axioms GodelQ.Z0Omega.z0_runner_arrives
