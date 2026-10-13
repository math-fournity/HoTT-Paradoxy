import GodelQ.ZFC.CG008SingleInstance

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008WallSynthesis

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate GodelQ.CG008SingleInstance

/-!
# CG-008 · 靶心合成：单实例 × 非标准码（001-Master 派工）

## 两条收窄

**收窄一（002-Step，本日）**：Z0 只需要**一条** D3 实例（Gödel 句 `𝐆 = gödel zfcTr`）：
`𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)`（`CG008SingleInstance.lean`，机器化）。

**收窄二（002-Flash，本日）**：`AxStep` 的**标准码半边已证**（`axStep_standard`）；
剩余 = **非标准码**（非标准 `p ∈ 𝗜𝚺₁.Δ₁Class` 必是归纳模式的非标准实例）。

## 合成后的靶心（本文件机器化）

把两条合起来，Z0 的**充分目标**冻结为一条：

```
WallStatement := 𝗜𝚺₁ ⊢ Pr_{𝗜𝚺₁}(zfcTr 𝐆) 🡒 zfcTr (zfcTr 𝐆)
```

**为什么它充分**（三步全部机器化在本文件）：

1. `zfcTr 𝐆` 是 Σ₁ 句（`zfcTr_sigma1`），Foundation 的 `provable_sigma_one_complete`
   **免费**给出 `𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 Pr_{𝗜𝚺₁}(zfcTr 𝐆)`——这一步不需要任何缺口
   （`wall_step_i`）；
2. 与 `WallStatement` 经蕴含传递合成即**单实例**（`single_instance_of_wall`）；
3. 单实例经已证的 `zfc_z0_full_of_single` 即**完整形式 Z0**（`zfc_z0_full_of_wall`）。

**`WallStatement` 的数学内容**（V 形式，`wall_V_form`）：对任意 `V ⊧ 𝗜𝚺₁`，
V 内部的**任意** 𝗜𝚺₁-推导 `d`（V 非标准时 `d` 可非标准）都要能**变换**成
V 内部的 ZFC-推导（`d'` 的尾句是 `translate(zfcTr 𝐆)`）。

**这就是推导变换（`Derivation.induction1` 十支）在固定尾句 `zfcTr 𝐆` 上的义务**：
九支与 `T` 无关（纯语法；其中 exs 支的形状由 004-Step 的 `ExsBlockerQ` 处理），
唯一依赖 `T` 的 axm 支 = `AxStep` = 收窄二：标准码已证，非标准码 = 「V 内证明 ω 归纳」。

## 一条必须说清的边界（防止过度合并）

**单实例收窄不缩小 `AxStep` 所需的实例集。** 理由（可检验的 padding 推导）：
对任意公理 `q`，把 `{q}`（axm 叶）与任给的 `{ψ}` 推导 `d₀` 经 `andIntro`
与 cut（配逻辑重言 `{¬(ψ∧q), ψ}`）合起来即得 `{ψ}` 的另一条推导——
所以 `d` 的公理叶可以含**任意** `q ∈ Δ₁Class`。
两条收窄合起来是「靶子的**消费端**（只消费 `𝐆` 一句）+ **难点端**（难点只在非标准码）」，
**不是**把难点再削一层。

## Foundation 缺什么（沿用 002-Flash 清单，本文件复核）

1. **V 内版「解释保可证性」**：现走 `DirectInterpretation.of_provability`
   （`LK/Interpretation.lean:443`，经完备性，元层语义论证），不产生 V 内推导码；
2. **V 内版「ω 最小归纳」**：`PAModel.lean` 的 `naturalNumber_induction` 量化的是
   元层 `φ : Semiformula ℒₒᵣ ℕ 1`，不覆盖 V 的非标准码；
3. **`Provable.sound`/`provable_iff_provable` 载体硬接线 `ℕ`**（`D1.lean:40`）：
   V→ℕ 下降不存在，所以前提不能降到元层去用 `interpret_theory`。

## 不声称

- `WallStatement`、单实例、C、`hD3G`、`AxStep` 非标准半边**均未证**；
- **完整形式 Z0 未证成，不交付**；影子级 `zfc_z0`/`sh_z0`（无条件）不受影响；
- 本文件是**归约与合成**，不是证明；所有定理都是「以 `WallStatement` 为显式前提」的
  条件定理，`rc=0`、零未证标记，可进收据。 -/

/-- **第 (i) 步（免费）**：`zfcTr 𝐆` 是 Σ₁ 句，Foundation 的 Σ₁ 完全性给出
`𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 Pr_{𝗜𝚺₁}(zfcTr 𝐆)`。**这一步不需要任何缺口。** -/
theorem wall_step_i :
    𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒
      Bootstrapping.provabilityPred 𝗜𝚺₁ (zfcTr (gödel zfcTr)) :=
  provable_sigma_one_complete (T := 𝗜𝚺₁) (zfcTr_sigma1 (gödel zfcTr))

/-- **合成靶心（`WallStatement`）**：把「单实例」的免费半步做掉后剩下的那一步。

V 形式：任意 V ⊧ 𝗜𝚺₁ 内的 𝗜𝚺₁-推导（可非标准）要能变换成 ZFC-推导。 -/
def WallStatement : Prop :=
  𝗜𝚺₁ ⊢ Bootstrapping.provabilityPred 𝗜𝚺₁ (zfcTr (gödel zfcTr)) 🡒
    zfcTr (zfcTr (gödel zfcTr))

/-- **`WallStatement` ⟹ 单实例**（免费步 + 靶心步，经蕴含传递）。 -/
theorem single_instance_of_wall (h : WallStatement) :
    𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 zfcTr (zfcTr (gödel zfcTr)) := by
  exact C_trans wall_step_i h

/-- **`WallStatement` ⟹ 完整形式 Z0**（经已证的单实例定理 `zfc_z0_full_of_single`）。 -/
theorem zfc_z0_full_of_wall (h : WallStatement) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  zfc_z0_full_of_single (single_instance_of_wall h)

/-- **`WallStatement` 的 V 形式**：对任意 `V ⊧ 𝗜𝚺₁`，V 内部的 𝗜𝚺₁-推导码
要能变成 V 内部的 ZFC-推导码（「推导变换」义务的精确陈述）。 -/
theorem wall_V_form (h : WallStatement) :
    ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      Provable 𝗜𝚺₁ (⌜zfcTr (gödel zfcTr)⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr (gödel zfcTr))⌝ : V) := by
  intro V _ hV2 hp
  have hp' : V↓[ℒₒᵣ] ⊧ Bootstrapping.provabilityPred 𝗜𝚺₁ (zfcTr (gödel zfcTr)) := by
    simpa [models_iff] using hp
  have hV := models_of_provable hV2 h
  rw [Semantics.Imp.models_imply] at hV
  exact (models_zfcTr_iff V (zfcTr (gödel zfcTr))).mp (hV hp')

end GodelQ.CG008WallSynthesis

#print axioms GodelQ.CG008WallSynthesis.single_instance_of_wall
#print axioms GodelQ.CG008WallSynthesis.zfc_z0_full_of_wall
#print axioms GodelQ.CG008WallSynthesis.wall_V_form
