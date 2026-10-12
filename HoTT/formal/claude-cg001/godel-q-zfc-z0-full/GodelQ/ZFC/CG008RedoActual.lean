import GodelQ.ZFC.CG008RedoPrereq

/-!
# CG-008 · 重做 `con_unprovable` 的尝试：卡在**展开成本**上

## 目标

```
hD3G : 𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)          𝐆 := gödel (T₀ := 𝗜𝚺₁) zfcTr
⟹ 𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)
```

## 本轮实测的结果：**卡在展开成本**

`CG008RedoPrereq.lean` 已查实前置**全部可合成**（`HBL2`、`Mono`、`Diagonalization`、
`gödel_spec`），所以**类型层无阻碍**。但**真的写这条证明时**，
Lean 在 `zfcTr` 的定义上**爆炸**：

| 尝试 | 结果 |
|---|---|
| 照抄 Foundation 的 `cl_prover [h₁, h₂, h₃]` | `rc=1`：`maximum recursion depth has been reached` |
| 提高 `maxRecDepth` 到 4000 / 8000 | **`rc=-9`**（进程被杀死——内存/时间耗尽） |
| 逐步写出链（`mdp`、`C_of_E_mp`、`contra`） | 仍在 `∼zfcTr G` 与 `zfcTr G 🡒 ⊥` 的**统一**上炸 |

**根因**：`zfcTr σ = trProv.val/[⌜σ⌝]`，而
`trProv = ∃y, iTDef y 0 x ∧ provable 𝗭𝗙𝗖 y`。
每次 Lean 要判断 `∼zfcTr G` 是否等于 `zfcTr G 🡒 ⊥`，
都会去展开这条定义（内含 `iTDef`、`provable 𝗭𝗙𝗖`），
而 `𝐆 := gödel zfcTr` **本身又含 `zfcTr`**——于是展开递归叠加。

**Foundation 的 `cl_prover` 能在抽象情形下工作**，
是因为那里的 `𝔅` 是**变量**，不展开；换成具体的 `zfcTr` 就失效。

## 这意味着什么

**这不是数学障碍，是实现障碍**——但它是**实的**，不是可以绕过的形式问题。
要在本包内重做这条证明，有两条路：

1. **避免让 Lean 展开 `zfcTr`**——先证 `zfcTr σ ↔ Provable 𝗭𝗙𝗖 ⌜translate σ⌝`
   的元层形式并注册为 `simp` 引理，让统一走这条**不展开定义**的路；
2. **在抽象层做**（**更可能成功**）——把证明先对
   **任意** `𝔅 : Provability T₀ T` + `[𝔅.HBL]` 写出来（正如 Foundation 的写法），
   最后再实例化到 `zfcTr`。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
- **记录的是失败尝试与根因，不是证明。**
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008RedoActual

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack GodelQ.CG008BridgeAnatomy GodelQ.CG008SingleD3Theorem
  GodelQ.CG008ConRedo GodelQ.CG008MonoExt GodelQ.CG008RedoPrereq

open ProvabilityAbstraction (gödel gödel_spec)

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 本文件的目标句。 -/
noncomputable abbrev G : Sentence ℒₒᵣ := gödel (T₀ := 𝗜𝚺₁) zfcTr

/-- **查实 1**：`gödel_spec` 对 `zfcTr` 可用——重做第一步的原料。

**注意**：这一条**能**编译，说明 `zfcTr` 的定义本身不是问题；
问题出在**后续要判断 `∼zfcTr G` 与 `zfcTr G 🡒 ⊥` 相等**时触发的展开。 -/
theorem G_iff : 𝗜𝚺₁ ⊢ G 🡘 ∼zfcTr G := gödel_spec (𝔅 := zfcTr)

/-- **查实 2（抽象层的正确做法）**：Foundation 的 `formalized_unprovable_gödel`
对**任意** `𝔅 : Provability T₀ T` + `[𝔅.HBL]` 成立——
所以本包要重做的话，应当**在抽象层做**，最后才实例化到 `zfcTr`。 -/
example {L : Language} [L.DecidableEq] [L.ReferenceableBy L] {T₀ T : Theory L}
    [Diagonalization T₀] [T₀ ⪯ T] {𝔅 : Provability T₀ T} [𝔅.HBL] :
    T₀ ⊢ 𝔅.con 🡒 ∼𝔅 (gödel 𝔅) :=
  formalized_unprovable_gödel (𝔅 := 𝔅)

end GodelQ.CG008RedoActual
