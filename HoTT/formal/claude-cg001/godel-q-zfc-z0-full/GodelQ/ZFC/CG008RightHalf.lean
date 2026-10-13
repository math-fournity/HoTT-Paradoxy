import GodelQ.ZFC.CG008CLocal

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008RightHalf

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.CG008CLocal

/-! # 右半的可行性分解（**只分解，不证**）

## 定位再确认

右半 = 在 `V └§ 𝗭` 下做算术版 `term_complete` 的集合对偶。
它**不能**补进 Z0 证明（Z0 要任意 `V └§ 𝗜𝚺칠`），
但作为**独立对照资产**有价值：它证明「零件齐全、方向可走」，
把 C 的困难从猜测变成有对照实验的定位。

## 零件清单（逐条给 Foundation/本包出处）

| # | 零件 | 出处 | 状态 |
|---|---|---|---|
| P1 | `ofNat : ℕ → V`（`0 ↦ └┐`、`n+1 ↦ succ (ofNat n)`） | `SetTheory/Z/Z.lean:427` | ✅ 现成 |
| P2 | `omega_succ_closed` | Foundation | ✅ 本包 `ArithInterp.lean:86` 已在用 |
| P3 | `add_mem_omega` | Foundation | ✅ 本包 `ArithInterp.lean:92` 已在用 |
| P4 | `mul_mem_omega` | Foundation | ✅ 本包 `ArithInterp.lean:99` 已在用 |

**所以「元素收进 omega」这一族全有。**

## 分解为四个工作项（按依赖排序）

### W1：定义「项求值 → ofNat 常项」的向量版（`toNumVec` 对偶）

算术版：`toNumVec {n k} (w : Fin n → V) : SemitermVec V ℒₒᵣ n k := ((𝕹 ·)⨟ w)`。
集合对偶要：`toOmegaVec (w : Fin n → V) : SemitermVec V ℒ₧ n k := ((ofNat ·)⨟ w)`。

**关键**：这是纯定义，**一行**。困难不在这。

### W2：`toOmegaVec w ⤕ ... ≐ ...` 的闭项等式（`term_complete` 对偶）

算术版 `term_complete`（`D3.lean:45`）按项的结构归纳（bvar/fvar/func 三支），
func 支又按 zero/one/add/mul 四个符号分派，每个用 P2–P4 的 omega 闭包。

**工作量**：套结构，机械但**需逐支写**。预计是右半的主要工作量（约等于把 `D3.lean:45-90` 抄一遍并换 numeral）。

### W3：`levy_sigma_succ_induction` 的八情形实例化

骨架已有（`SetTheory/Definability/Definable.lean:66`），谓词实例化为
`fun n phi psi ↦ (V └§ phi → Provable 𝗭𝗙𝗢 └ñphi└╗)`。

**其中 hEQ/hMem 用 W2；hAnd/hOr/hBall/hExs 用 `TProof` 的存量引理。**

### W4：`hEQ` 情形的最后一步——从「V 满足等式」造 ZFC 推导

**这是右半唯一真新的数学内容**：算术版的对应步是 
`bold_sigma_one_complete` 里用 `term_complete` 把等式两边都换成 `𝕹`，
然后用 `EquationalTheory.eq_refl`。集合对偶要「omega 元素的同一性」引理。

**预判**：这一步**可能**已经是 Foundation 的存量（`set_eq_refl` 的近亲），需查。

## 可行性判断

**PRACTICAL（四步都可走，W1-W3 机械，W4 需查一次）。**

**但我同意 Master 的排序**：等 `ExsBlockerQ`（004-Step）有结果再派人。
理由：右半**不能**补进 Z0 证明，它是**对照资产**；
而 `ExsBlockerQ` 可能直接关闭一条**能**进 Z0 的路。**先做能进证明的。**

## 治理

- Foundation 只读；本文件纯下游。
- **本文件只分解，不含未证标记，不声称右半已证或可证完。** -/

/-- 引用 1：P1（`ofNat`）在 `V └§ 𝗭` 下现成。 -/
noncomputable example (V : Type) [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖] :
    ℕ → V := ofNat

end GodelQ.CG008RightHalf
