import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## D3 的精确归约链（2026-10-13）

目标（`RootBlockerQ`）：`p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)`。

**第一步（已证）**：`p ∈ Sh.craig.Δ₁Class ↔ Theory.IsCraigAxiom Sh p`
（`Theory.IsCraigAxiom.defined (T := Sh)` 的 `.iff`）。

**第二步**：展开 `IsCraigAxiom`：`∃ s p', p = p' ^⋏ qqVerums s ∧ Evalb ![s,p'] ↑Sh.reWitness.val`。

**第三步**：`iT 0 p = iT 0 (p' ^⋏ qqVerums s) = iT 0 p' ^⋏ qqVerums s`（`iT_and` + `iT_qqVerums`）。

**第四步（真正的难点）**：从 `Evalb ![s,p'] ↑Sh.reWitness.val` 得到
`Provable 𝗭𝗙𝗖 (iT 0 p' ^⋏ qqVerums s)`。

本探针核验前三步的机械性。

## ★ 第四步的精确内容（本会话查明）

`reWitness` 的定义（`CraigTrick.lean:103`）：
```
noncomputable def reWitness : 𝚺ᴬ₀.Semisentence 2 :=
  .mkSigma (ISigma1.exists_matrix_provable T.reCh.sigma_prop).choose.val
```
配 `reWitness_spec : V ⊧/e T.reCh.val ↔ ∃ w, V ⊧/(w :> e) T.reWitness.val`。

**即**：`reWitness` 是 `reCh` 的 **Σ₀ 见证矩阵**（把 Σ₁ 的 `reCh` 展成 Σ₀ 矩阵 + 存在量词）。
`reCh` 又 = `codeOfREPred (encode '' T)`，即「`φ` 的码在 `T` 里」的 RE 谓词。

**故第四步的实质是**：
`Evalb ![s,p'] ↑Sh.reWitness.val`（Σ₀ 事实：`s` 是「`p'` 在 `Sh` 里」的见证）
⟹ `Provable 𝗭𝗙𝗖 (iT 0 p' ^⋏ qqVerums s)`。

**这一步正是「可证性谓词的内部化」**——`reWitness` 是**语法见证**，
而 `Provable` 是**语义谓词**，两者之间的桥就是 D3 的全部内容。

**注意**：这与 `iT_qqVerums` 那种纯构造块不同——
第四步需要「Σ₀ 事实 ⟹ 可证」的**反射原理**（Σ₀-完备性）。
Foundation 有 `ISigma1` 相关工具，值得查。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeD3Chain
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 第一步：成员关系 ↔ IsCraigAxiom（已证，此处复核）
example (p : V) (h : p ∈ (Sh.craig).Δ₁Class) : Theory.IsCraigAxiom (V := V) Sh p :=
  ((Theory.IsCraigAxiom.defined (V := V) (T := Sh)).iff).mp h

-- 第三步的件：`iT_qqVerums`（本会话已证）+ `iT_and`
#check @iT_and
#check @Theory.IsCraigAxiom.defined

-- 核验 `IsCraigAxiom` 的展开形状（rfl）
#check @Theory.IsCraigAxiom

end ProbeD3Chain