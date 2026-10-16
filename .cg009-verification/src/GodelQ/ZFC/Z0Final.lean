import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import GodelQ.ZFC.TranslateRE

/-!
# CG-008（廉价传递尝试）：诚实收尾

## 实验结论（2026-10-11 机器验证）

目标：用已无条件证明的影子形式
`zfc_z0 : 𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val)`
经一致性等价桥梁推出 Z0 完整形式
`𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`。

所需的桥梁为 `𝗜𝚺₁ ⊢ Sh.craig.consistent.val ↔ 𝗭𝗙𝗖.consistent`
（即 `Con(Sh.craig) ↔ Con(𝗭𝗙𝗖)` 在 𝗜𝚺₁ 内部成立）。

### 直接尝试（已证伪）

直接 `complete 𝗜𝚺₁` 证明该桥梁：Lean 无法闭合目标，静默用 `sorry` 回填，
`#print axioms` 报告 `sorryAx`。这说明桥梁坍缩为与 Σ₁ 内部化（D3 /
`zfcTr_D3_internalize`）**完全相同的缺口**：它要求把两个估值化（valuated）
可证性谓词在非标准模型中等同，而 ZFC 的可证性是 Σ₁ 而非 Δ₁，ZFC 的 Σ₁
完全性不可在 𝗜𝚺₁ 内证。

### 条件形式尝试（已诚实降格）

以桥梁为显式前提写条件定理 `zfc_z0_full_of_bridge` 时，其证明主体需用
`cl_prover [e, hSh]` 在 `Sh` 内由 `Sh ⊢ (A ↔ B)` 与 `Sh ⊢ B` 推出 `Sh ⊢ A`。
由于 `e` 是经 `WeakerThan.pbl` 包裹的**抽象**前提，`cl_prover` 在
12 000 000 心跳预算下仍确定性超时（证据见 `HoTT/verification/runs/
2026-10-11-z0final-conditional/build2.log`）。该定理数学上正确，但当前
Foundation 的 `cl_prover` 对抽象等价比前提无法在合理预算内闭合。

因此廉价传递**不能**闭合 Z0，也不保留任何伪造收据。本文件给出诚实的
条件形式 `zfc_z0_full_of_D3_cheap`：把 D3 内部化（`zfcTr_D3_internalize`）
作为显式前提，链接到完整形式。完整形式要闭合，仍须走 CG-008 主线
（集合论 Σ₁ 完全性，需 Foundation 上游改动，另案授权）。

本文件零 `sorry`；所有未决内容都以显式前提呈现，绝不伪造证明。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.Z0Final

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

/--
**诚实条件形式（D3 廉价链接）。** 直接把 D3 内部化假设
`zfcTr_D3_internalize` 链接到 Z0 完整形式。与 `Z0Blocked.zfcTr_D3_internalize`
同一未决前提；仅作诚实的传递，不引入任何新 `sorry`。

（廉价传递路线「`Con(Sh.craig) ↔ Con(𝗭𝗙𝗖)` 在 𝗜𝚺₁ 内证 ⇒ 完整形式」与
D3 等价，其条件定理 `zfc_z0_full_of_bridge` 因 `cl_prover` 对抽象等价比
前提超时已被诚实移除，见文件头注释；未决内容仍精确落在 D3 / `Theory.Δ₁ Sh`。）
-/
theorem zfc_z0_full_of_D3_cheap
    (d3 : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence),
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (Z0Full.zfcTr τ)⌝ : V)) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  zfc_z0_full_of_D3_internalize d3

end GodelQ.Z0Final

#print axioms GodelQ.Z0Final.zfc_z0_full_of_D3_cheap
