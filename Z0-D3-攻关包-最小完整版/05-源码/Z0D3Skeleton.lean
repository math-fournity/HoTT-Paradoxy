import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-!
# Z0-D3 攻坚骨架（2026-10-10，Codex 会话 01a120e6）

**这个文件我本机编译通过（exit 0）**：Lean 4.34.0 + Foundation `1fb01b72`
+ 本 repo 的 24 个 GodelQ 模块。

它把"我可以确定成立的部分"全部落成可编译引理，把唯一的缺口写成 `gap`。
你的工作：把 `gap` 证掉（或把卡点写清楚）。

**怎么用**：复制这个文件到
`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0D3Skeleton.lean`，
按 `BUILD.md` 的次序编译，然后改。

注意：本文件会进入收据源，所以**不得有 `sorry`**。
现在 `gap` 用 `sorry` 占位只是为了让你看到形状；证完请删掉这一行。
-/



open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full

namespace Z0D3Skeleton

/-! ## 第 1 部分：Craig 化 —— 本机实测可合成 -/

/-- `Sh.RE`（C-119）经 Foundation 的 Craig 化给出 Δ1 公理表示。 -/
noncomputable example : (Sh.craig : ArithmeticTheory).Δ₁ := inferInstance

/-- Craig 化保持 𝗣𝗔⁻。 -/
noncomputable example : 𝗣𝗔⁻ ⪯ Sh.craig := inferInstance

/-- Craig 化双向弱于原理论（故等价）。 -/
example : Sh.craig ⪯ Sh := inferInstance
example : Sh ⪯ Sh.craig := inferInstance

lemma shCraig_iff (σ : ArithmeticSentence) : Sh.craig ⊢ σ ↔ Sh ⊢ σ := by
  refine ⟨fun h ↦ ?_, fun h ↦ ?_⟩
  · exact Entailment.weakerThan_iff.mp (inferInstance : Sh.craig ⪯ Sh) h
  · exact Entailment.weakerThan_iff.mp (inferInstance : Sh ⪯ Sh.craig) h

/-- **本轮核心发现**：`Sh.craig` 的标准可证性谓词满足全部 HBL 条件，包括 D3。
这条 `inferInstance` 能成功，意味着 Foundation 的 `provable_D3` 可以直接用在 `Sh.craig` 上。 -/
noncomputable example : (Sh.craig.standardProvability).HBL3 := inferInstance

/-- Foundation 的形式化 Σ1 完全性对 `Sh.craig` 可用。 -/
lemma sigma1_complete_craig (σ : ArithmeticSentence) (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) :
    𝗜𝚺₁ ⊢ σ 🡒 provabilityPred Sh.craig σ :=
  FFL.FirstOrder.Arithmetic.provable_sigma_one_complete hσ

/-! ## 第 2 部分：语义层桥 —— 本机实测可证 -/

/-- `V ⊧ provabilityPred Sh.craig σ ↔ Provable Sh.craig ⌜σ⌝`。 -/
lemma models_provabilityPred_craig {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (σ : ArithmeticSentence) :
    V↓[ℒₒᵣ] ⊧ (↑(provabilityPred (Theory.craig Sh) σ) : Sentence ℒₒᵣ) ↔
      Provable Sh.craig (⌜σ⌝ : V) := by
  rw [models_iff]
  simp [provabilityPred,
    (inferInstance : 𝚺ᴬ₁-Predicate (Provable Sh.craig : V → Prop) via (provable Sh.craig)).iff]

/-- **`step1`（本机实测可证）**：`zfcTr` 的语义给出 `Sh.craig` 的推导编码。 -/
theorem step1 {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence)
    (h : V↓[ℒₒᵣ] ⊧ zfcTr σ) : Provable Sh.craig (⌜zfcTr σ⌝ : V) :=
  Bootstrapping.Arithmetic.sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 σ) h

/-! ## 第 2b 部分：D3 的两个方向之一已经免费（本机实测 exit 0） -/

/-- **已证（免费）**：`𝗜𝚺₁ ⊢ zfcTr τ 𝡒 provabilityPred Sh.craig (zfcTr τ)`。
这一条就是 Foundation 的 `provable_sigma_one_complete`，因为 `zfcTr τ` 是 Σ1 句
（`zfcTr_sigma1`）。**没有任何新工作。** -/
lemma fwd (τ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ (↑(zfcTr τ) 🡒 (↑(provabilityPred (Theory.craig Sh) (zfcTr τ)) : Sentence ℒₒᵣ)) :=
  FFL.FirstOrder.Arithmetic.provable_sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 τ)

/-! ## 第 3 部分：唯一缺口 = D3 的另一个方向 -/

/-- **GAP = D3 的唯一实质内容，一个方向**（2026-10-10 晚进一步压缩）。

上面的 `fwd` 已由 Foundation 免费给出。剩下的是反方向：
语义上，"V 中有一条 `Sh.craig` 推导" ⊢ "V 中有一条 `𝗭𝗙𝗖` 推导"。

`rw [models_zfcTr_iff]` 之后目标就是 `Provable 𝗭𝗙𝗖 ⌜(zfcTr σ)ᵗ⌝`，
即 V 中的 𝗭𝗙𝗖 推导编码。 -/
lemma bwd {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence)
    (h : V ↓[ℒₒᵣ] ⊧ ↑(provabilityPred (Theory.craig Sh) (zfcTr σ))) :
    V ↓[ℒₒᵣ] ⊧ ↑(zfcTr (zfcTr σ)) := by
  rw [models_zfcTr_iff]
  sorry

/-- 由 `fwd` 与 `bwd` 合成 HBL3；`fwd` 已证，`bwd` 是缺口。 -/
lemma HBL3_of_fwd_bwd (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ ↑(zfcTr σ) 🡒 ↑(zfcTr (zfcTr σ)) := by
  sorry

end Z0D3Skeleton
