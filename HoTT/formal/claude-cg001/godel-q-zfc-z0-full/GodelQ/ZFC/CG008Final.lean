import GodelQ.ZFC.CG008HBL3Test

/-!
# CG-008 · 本轮收束：缺口的精确定位与诚实降格

本文件把 CG-008 这一轮（2026-10-11，P2）的**最终结论**固定下来，
供后继工作单元直接接手。**不声称 D3 已证。**

## 一、缺口的三重等价形状

| # | 形状 | 出处 |
|---|---|---|
| 1 | `Provable 𝗭𝗙𝗖 ⌜translate τ⌝ → Provable 𝗭𝗙𝗖 ⌜translate (zfcTr τ)⌝`（任意 `V ⊨ 𝗜𝚺₁`） | `Z0Blocked.lean:61-65` |
| 2 | 集合语言的 `provable_internalize`——与算术版 `D3.lean:175` 逐字同形，只差 `T : ArithmeticTheory` → `T = 𝗭𝗙𝗖 : Theory ℒₛₑₜ` | `CG008GapShape.lean` 六步链 |
| 3 | **`zfcTr.HBL3`**——即 `∀ σ, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)` | `CG008HBL3.lean` |

**第 3 个形状是本轮最重要的收获**：它把缺口放进 Foundation 已有的
抽象可证性框架（`ProvabilityAbstraction/Basic.lean:25-93`），
与既有文献（Vis21 的抽象 G2，见 `Refutability.lean:119`）可直接对照。

## 二、卡点的精确位置

Foundation 已经给了**充分条件实例**：

```lean
instance [∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)] : 𝔅.HBL3 := ⟨by simp⟩
```

所以缺口 = 建成 `∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)`。

**为什么它不白送**——D1 与 D3 的前提在**不同的层**：

| | D1（已建成） | D3（缺口） |
|---|---|---|
| 形状 | `Sh ⊢ σ → 𝗜𝚺₁ ⊢ zfcTr σ` | `𝗜𝚺₁ ⊢ zfcTr σ → zfcTr (zfcTr σ)` |
| 前提位置 | **元层**（系统外的可证性） | **系统内**（可证性谓词自己的编码） |
| 桥 | `internalize_provability`（`D1.lean:27`）白送 | ❌ 无 |

D1 的证明（`Z0Full.lean:62-63`）走的就是
`Sh ⊢ σ`（元层）→ `internalize_provability` → `Provable 𝗭𝗙𝗖 ⌜translate σ⌝` → `complete 𝗜𝚺₁`。

D3 要的是把**内部的** `zfcTr σ`（即 `V ⊨ zfcTr σ`）变回**元层的** `Sh ⊢ σ`，
而 Foundation 唯一的这类桥 `Provable.complete`（`D1.lean:35`）**只对 ℕ** 成立：

```lean
@[simp] lemma Provable.complete {φ : Sentence L} :
    T.internalize ℕ ⊢ ⌜φ⌝ ↔ T ⊢ φ
```

注意 `ℕ` 是**硬编码**的。`provable_iff_provable`（`D1.lean:41`）同样只对 `ℕ`。
这就是 `Z0Blocked.lean` 诊断第 2 条说的「模型无关报价转换」缺口，本文件独立复核确认。

## 三、为什么这是数学事实而非实现细节

D1 与 D3 的差别正是 Hilbert–Bernays–Löb 三条件中**唯一不白送**的那条。
若 D3 对 `zfcTr` 白送，则 `𝗭𝗙𝗖 ⊢ Con(𝗭𝗙𝗖)`，与哥德尔第二定理矛盾——
而 Z0 要证的正是那个矛盾。**所以缺口不能白送，是定理的必然。**

## 四、本轮的净进展

**没有缩小缺口，但显著提高了定位精度**：

- 从「集合语言的 Σ₁ 完全性」（需逐一处理十种句形，且 `ℒₛₑₜ` 无常项/函数符号，
  算术版的 `toNumVec` 无对偶）——**改述为**——
- 「`Sh` 上可证性谓词的 `HBL3`」（标准形状，Foundation 已有框架与充分条件实例）。

**下一步的具体靶子**：建成 `∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)`，
或等价地补上 `ℕ` 之外的模型无关报价转换。

## 五、治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
- **不声称 D3 已证**；`Z0Blocked.lean:65` 的未证标记仍在，不伪造收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Final

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本轮的靶子）**：缺口 = 建成这个实例。

`FormalizedCompleteOn` 展开为 `𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)`，
再经 `models_zfcTr_iff` 就是 `V ⊨ zfcTr σ → V ⊨ zfcTr (zfcTr σ)`。 -/
example (σ : ArithmeticSentence) [zfcTr.FormalizedCompleteOn (zfcTr σ)] :
    𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ) :=
  Provability.formalized_complete_on (𝔅 := zfcTr) (σ := zfcTr σ)

/-- **查实 2**：一旦实例建成，`HBL3` 由 Foundation 的实例立即给出。 -/
example [∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)] : zfcTr.HBL3 :=
  inferInstance

/-- **查实 3（卡点，本文件的要点）**：`Provable.complete` **只对 ℕ**。

这是 D1→D3 之间缺的那座桥。注意类型里 `ℕ` 是硬编码的：
`T.internalize ℕ ⊢ ⌜φ⌝ ↔ T ⊢ φ`。
没有把 `ℕ` 换成一般 `V ⊨ 𝗜𝚺₁` 的版本——那正是缺口。 -/
example {T : Theory ℒₒᵣ} [T.Δ₁] {φ : Sentence ℒₒᵣ} :
    T.internalize ℕ ⊢ ⌜φ⌝ ↔ T ⊢ φ :=
  Provable.complete

/-- **查实 4**：`Sh` 侧的同一条桥（`provable_iff_provable`）同样只对 ℕ。 -/
example {T : Theory ℒₒᵣ} [T.Δ₁] {φ : Sentence ℒₒᵣ} :
    Provable T (⌜φ⌝ : ℕ) ↔ T ⊢ φ :=
  provable_iff_provable

end GodelQ.CG008Final
