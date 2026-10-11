import GodelQ.ZFC.CG008RawSigma1

/-!
# CG-008 探针 8（非收据）：`Derivable` 层能走多远——组合能力逐级测量

缺口需要的是：**在 V 内部，从一条推导造出另一条推导**。
本探针逐级测量 `Derivable`/typed 层的组合能力，定出「哪一级开始断」。

级别：
1. **同层逻辑组合**：`Provable T ⌜φ⌝ → Provable T ⌜φ ⋏ φ⌝`（只需 K_intro）
2. **跨层搬运**：typed ↔ 编码（`CG008Raw` 已有）
3. **内部化自身**：`Provable T ⌜φ⌝ → Provable T ⌜provable T ⌜φ⌝⌝`（这就是 D3 的内容）

第 3 级是缺口要的；前两级若通、第 3 级若断，就精确定位了断点。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe8

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Raw
  GodelQ.CG008RawSigma1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **级别 1（typed 层）**：从 `⊢ φ` 造出 `⊢ φ ⋏ φ`。
这是纯逻辑组合，`set_K_intro` 直接给。 -/
theorem level1_typed {φ : Formula V ℒₛₑₜ}
    (h : 𝗭𝗙𝗖.internalize V ⊢ φ) : 𝗭𝗙𝗖.internalize V ⊢ φ ⋏ φ :=
  set_K_intro φ φ h h

/-- **级别 1（编码层）**：同一件事在 `Derivable` 层。
注意这里是**编码的序列**，不是 typed 公式。 -/
theorem level1_derivable {φ : Formula V ℒₛₑₜ}
    (h : Derivable 𝗭𝗙𝗖 (insert φ.val ∅ : V)) :
    Derivable 𝗭𝗙𝗖 (insert (φ ⋏ φ).val ∅ : V) :=
  d_set_K_intro φ φ h h

/-- **级别 2**：跨层搬运（两个方向都通，见 `CG008Raw`）。
这里写成往返恒等，确认没有信息损失。 -/
theorem level2_roundtrip {φ : Formula V ℒₛₑₜ}
    (h : Derivable 𝗭𝗙𝗖 (insert φ.val ∅ : V)) :
    Derivable 𝗭𝗙𝗖 (insert φ.val ∅ : V) :=
  internal_derivable_of_tprovable (tprovable_of_internal_derivable h)

/-- **级别 2.5**：把 `Provable` 的见证搬到编码层。
`Provable T ψ` 就是 `Derivable T (insert ψ ∅)`，所以这条是恒等——
但它确认了**见证 `d : V` 在两个表示之间是同一个**。 -/
theorem level2_5_witness (ψ : V) :
    Provable 𝗭𝗙𝗖 ψ ↔ Derivable 𝗭𝗙𝗖 (insert ψ ∅ : V) :=
  internal_provable_iff_internal_derivable

/-- **级别 3（缺口要的）**：`Provable T ⌜σ⌝ → Provable T ⌜provabilityPred T σ⌝`。

对**算术**理论 T（且 `[T.Δ₁]`、`[𝗣𝗔⁻ ⪯ T]`），Foundation 已证（`D3.lean:175`）。
这一行用 `𝗜𝚺₁` 作对照，确认「算术版可用」。 -/
theorem level3_arithmetic {σ : ArithmeticSentence}
    (h : Provable 𝗜𝚺₁ (⌜σ⌝ : V)) :
    Provable 𝗜𝚺₁ (⌜provabilityPred 𝗜𝚺₁ σ⌝ : V) :=
  Bootstrapping.Arithmetic.provable_internalize (T := 𝗜𝚺₁) h

end GodelQ.CG008Probe8
