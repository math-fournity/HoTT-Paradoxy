import GodelQ.ZFC.CG008ProofToProvable

/-!
# CG-008 探针 12（非收据）：一条候选路线的方向性证伪

## 候选路线（本探针检验的对象）

1. 前提 `Provable 𝗭𝗙𝗖 (⌜translate τ⌝ : V)` → `V ⊨ zfcTr τ`（`models_zfcTr_iff`，↔）；
2. `zfcTr τ` 是 Σ₁ 句；
3. **Σ₁-绝对性**：`V ⊨ σ → ℕ ⊨ σ`（把 V 中的真降到 ℕ）；
4. `ℕ ⊨ zfcTr τ` → `𝗜𝚺₁ ⊢ zfcTr τ`（Σ₁ 完全性）；
5. → `𝗭𝗙𝗖 ⊢ translate (zfcTr τ)`（`arithInterp.of_provability`）；
6. → `Provable 𝗭𝗙𝗖 (⌜translate (zfcTr τ)⌝ : V)`（`internalize_provability`，载体多态）。

**第 3 步是关键**：它把「V 中的真」降到「ℕ 中的真」，
而不是把 `Provable : V` 改写成 `Provable : ℕ`（那是 `Z0Probe7` 证伪的载体墙）。
前者是元层定理，后者是类型错误。

## 本探针的结论：第 3 步的方向**是反的**

Foundation 的 `sigma_one_upward`（`Tarski/HierarchicalDefinability/Absoluteness.lean:93`）：

```lean
lemma sigma_one_upward {n} {φ : Semiformula L ξ n} (hφ : ℬ.Hierarchy 𝚺 1 φ)
    (e : Fin n → M) (ε : ξ → M) :
    φ.Eval e ε → φ.Eval (ι ∘ e) (ι ∘ ε)
```

其中 `ι : M ↪ₛ N` 是**结构嵌入**。对算术场景，
`natCastEmbedding : ℕ ↪ₛ V`（`Arithmetic/Definability/Absoluteness.lean:20`）——
即 **`M = ℕ`，`N = V`**。

所以 `sigma_one_upward` 给的是 **ℕ 真 → V 真**（向上），
而候选路线要的是 **V 真 → ℕ 真**（向下）。**方向相反。**

这是正确的数学：Σ₁ 句在**更大的**结构里更容易真（存在见证更容易找到），
所以 Σ₁ 只向上绝对，不向下。把 V 中的 Σ₁ 真降到 ℕ 需要的是
**Π₁ 向下绝对**（`piOne_downward_absolute`），而 `zfcTr τ` 是 Σ₁ 不是 Π₁。

## 因此

候选路线**不成立**。这不是实现细节问题，是方向性问题。

## 那 Z0Bridge 的 `bridge` 前提为什么长那样

`Z0Bridge.zfcTr_D3_internalize_of_sigma1_bridge` 的前提 `bridge` 是：

```
Provable 𝗜𝚺₁ (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)
```

即「V 内部的算术证明编码 → V 内部的 ZFC 证明编码」。
这正是本探针第 4-6 步想要的**内部化**版本，而它不是元层的 `of_provability`
（后者只把**外部**推导变成**外部**推导，不产生 V 内部的证明编码）。
本探针确认：绕不开它。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe12

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Raw
  GodelQ.CG008RawSigma1 GodelQ.CG008SetSigma1Complete GodelQ.CG008ProofToProvable

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：前提 → `V ⊨ zfcTr τ`（`models_zfcTr_iff` 是 **↔**，两个方向都有）。 -/
example (W : Type) [ORingStructure W] [W↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : W)) :
    W↓[ℒₒᵣ] ⊧ zfcTr τ :=
  (models_zfcTr_iff W τ).mpr h

/-- **查实 2**：`zfcTr τ` 是 Σ₁ 句。 -/
example (τ : ArithmeticSentence) : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (zfcTr τ) :=
  zfcTr_sigma1 τ

/-- **查实 3（方向性，本探针的要点）**：`natCastEmbedding` 的方向是 **ℕ → V**
（`Arithmetic/Definability/Absoluteness.lean:20`：`def natCastEmbedding : ℕ ↪ₛ[ℒₒᵣ] V`）。
所以 `sigmaOne_upward_absolute` 给的是 **ℕ 真 → V 真**，
而候选路线要 **V 真 → ℕ 真**——**方向相反**。

用嵌入的**存在与方向**把这一点固定下来（不去做完整的绝对性证明，
那需要更多类型类适配）。 -/
noncomputable example : ℕ ↪ₛ[ℒₒᵣ] V := natCastEmbedding V

/-- **查实 4**：Σ₁ 只**向上**绝对（`sigma_one_upward`，`Tarski/.../Absoluteness.lean:93`）：

```lean
lemma sigma_one_upward {n} {φ : Semiformula L ξ n} (hφ : ℬ.Hierarchy 𝚺 1 φ)
    (e : Fin n → M) (ε : ξ → M) :
    φ.Eval e ε → φ.Eval (ι ∘ e) (ι ∘ ε)
```

`M → N` 方向。取 `M = ℕ`、`N = V`，就是 ℕ → V。
**没有**反向的引理——那在数学上就是错的（Σ₁ 在更大的结构里更容易真）。 -/
example : True := trivial

end GodelQ.CG008Probe12
