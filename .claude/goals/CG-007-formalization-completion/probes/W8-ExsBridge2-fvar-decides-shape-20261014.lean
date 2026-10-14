import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ 决定性问题：`ExsBridge2` 对含 fvar 的 `t` 是否**为假**（2026-10-14）

Master 情报：`IsTerm t := IsSemiterm L 0 t` **只约束 bvar，fvar 不受约束**
（`Term/Basic.lean:755-757`）。Foundation 的 `exsIntro` 语义条目
（`Proof/Basic.lean:458-461`）**也只要求 `IsTerm`**，没加 FVFree。

**故**：`ExsBlockerQ` 里的 `t` 可以含自由变量。

**若 `ExsBridge2` 对含 fvar 的 `t` 为假**，则桥的**形状必须收窄或重找**——
这是「桥要收窄」vs「桥要重找」的分水岭（001-Step 正在做同一探针）。

**论据（若成立则为假）**：取 `t = ^&0`（fvar）、`p = #0 = #0`（层 1）。
* LHS：`iT 0 (substs1 ^&0 p)` = `iT 0 (^&0 = ^&0)`；
* RHS：`^∃ (domZero ⋏ iT 1 p)`。

**语义上**：LHS 是「`a = a`」（a 任意），RHS 是「`∃x∈ω, x = x`」。
`a = a` 对任意 `a` 真，但 `∃x∈ω` 要求 ω 非空——**两者都是真的**。
故这一例**不构成反例**。真正的分歧要看别处。

## 核验结果（exit 0）

| 项 | 结果 |
|---|---|
| `IsTerm ℒₒᵣ ^&0` | ✅ **成立**（`IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := 0) 0`） |
| `IsSemiterm.fvar (n x)` | **对 `x` 无条件** —— 任意 fvar 在任意层（含层 0）都是半项 |
| `IsSemiterm.bvar (n z)` | 有条件：`z < n`（**只有 bvar 受层数约束**） |
| `Derivation.exsIntro` / `Derivable.ex_m` | 前提都只有 `IsTerm L t`，**未加 FVFree** |

**⟹ 确认 Master 的情报**：`ExsBlockerQ` 里的 `t` **确实可以含自由变量**。

## 对 `ExsBridge2` 形状的影响（我的分析，标身份：AI 判断，未证）

取 `t = ^&0`、`p = #0 = #0`（层 1）试作反例：
* **LHS** `iT 0 (substs1 ^&0 p)` = `iT 0 (^&0 = ^&0)`——语义是「`a = a`」，对任意 `a` 真；
* **RHS** `^∃ (domZero ⋏ iT 1 p)` = 「`∃x∈ω, x = x`」——ω 非空时为真。

**两者都真，故此例不构成反例。** 真正的分歧不在这一处。

**但有一个真实的风险**（这是我要与 001-Step 对表的）：
`ExsBridge2` 断言的是 `Provable (imp A B)`。若 `t` 含 fvar，则 **`A` 含自由变量**，
而 `Provable φ`（φ 带自由变量）在 LK 里等价于 `⊢ ∀x φ`（全称化）。
**⟹ 对含 fvar 的 `t`，`ExsBridge2` 实际要求的是 `⊢ ∀a (iT 0 (p[a]) → ∃x∈ω p(x))`。**
这在语义上**仍为真**（任取 a，若 a∈ω 则见证 a；若 a∉ω 则 LHS 可能假）——
**但「a∉ω 时 LHS 假」这一点要具体核**，它正是 001-Step 的 fvar 边界探针要查的。

**故我不开工**，先与 001-Step 对表：它查边界，我按 Master 的分工攻见证引理，
两边不重叠。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeFvarDecides
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① 决定性前提：`IsTerm ^&0` 成立吗？（若成立，则 t 确实可含 fvar）
example : IsTerm ℒₒᵣ (^&(0:V) : V) := IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (0:V)) 0

-- ② `IsSemiterm.fvar` 的形状（确认 fvar 在任意层都成立，含层 0）
#check @IsSemiterm.fvar

-- ③ 对照 `IsSemiterm.bvar`（bvar 才受层数约束）
#check @IsSemiterm.bvar

-- ④ Foundation 的 exsIntro 语义条目的前提
#check @Bootstrapping.Derivation.exsIntro
#check @Bootstrapping.Derivable.ex_m

end ProbeFvarDecides