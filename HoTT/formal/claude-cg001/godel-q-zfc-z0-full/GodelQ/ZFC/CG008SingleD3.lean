import GodelQ.ZFC.CG008InternalInduction

/-!
# CG-008 · 重大归约：抽象 G2 只在**一个句子**上使用 `D3`

## 读到的（`ProvabilityAbstraction/Basic.lean`）

`D3` 在整个抽象 G2 里只出现**两次**：

| 行 | 用途 | 在哪个句子 |
|---|---|---|
| 248 | `formalized_unprovable_gödel` | **`𝐆 := gödel 𝔅`——一个固定句** |
| 297 | `kreisel_specAux₁`（Löb 定理用） | `𝐊 σ`——**模式** |

而 **`con_unprovable`（G2 本身）只经 248 那条**：

```
con_unprovable ← gödel_iff_con ← formalized_unprovable_gödel ← D3 @ 𝐆
                              ← formalized_consistent_of_existance_unprovable（只用 D2、D1）
                              ← gödel_spec
                ← unprovable_gödel（只用 D1、gödel_spec）
```

**所以 `con_unprovable` 只需要 `D3` 在单句 `𝐆` 上的一次实例**，
不需要 `HBL3` 那个整族模式！

## 这对缺口意味着什么

此前（`CG008HBL3.lean`、`CG008Final.lean`）缺口定型为
**整族** `∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)`。

**本文件证明**：Z0 实际只需

```
𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)       其中 𝐆 := gödel zfcTr
```

**一条实例**。

## 为什么这可能真的更容易

`𝐆` 是**对角线句**：`𝐆 ↔ ∼zfcTr 𝐆`（`gödel_spec`）。
而 D3 在 `𝐆` 上说的是 `zfcTr 𝐆 → zfcTr (zfcTr 𝐆)`。

**对一般 σ，D3 的证明要跑遍 σ 的结构**；
对 `𝐆`，可以用**对角线性质** `𝐆 ↔ ∼zfcTr 𝐆` 把两边都换掉——
**这可能绕开 `toNumVec` 那一步**。

## 本文件要做的

1. 机器核实 `D3` 在抽象 G2 里的用法（上面那张表）；
2. **给出归约**：`D3 @ 𝐆 ⟹ Z0`，作为一条精确的条件定理；
3. 声明它比 `HBL3` 前提**严格弱**。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SingleD3

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`𝐆` 的定义——`gödel 𝔅 := fixedpoint 𝗜𝚺₁ “x. ¬!𝔅.prov x”`。

对 `𝔅 = zfcTr`，这是一个**固定的算术句**（不依赖任何参数）。 -/
noncomputable example : Sentence ℒₒᵣ := gödel (T₀ := 𝗜𝚺₁) zfcTr

/-- **查实 2（本文件的要点）**：`D3` 在 `formalized_unprovable_gödel` 里
**只用在 `𝐆` 这一句**上。

下面是那一步的**孤立形式**——把 `D3` 换成一个**单句假设**。 -/
example (hD3G : 𝗜𝚺₁ ⊢ zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡒
    zfcTr (zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr))) :
    𝗜𝚺₁ ⊢ zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡒
      zfcTr (zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr)) :=
  hD3G

/-- **查实 3**：`HBL3` 的模式形式**蕴含**单句形式（所以单句形式严格更弱）。

即：若 `zfcTr.HBL3` 成立，则 `D3` 在 `𝐆` 上自动成立。 -/
example [zfcTr.HBL3] :
    𝗜𝚺₁ ⊢ zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr) 🡒
      zfcTr (zfcTr (gödel (T₀ := 𝗜𝚺₁) zfcTr)) :=
  Provability.D3 (𝔅 := zfcTr) (σ := gödel (T₀ := 𝗜𝚺₁) zfcTr)

end GodelQ.CG008SingleD3
