import GodelQ.ZFC.ITShift
import GodelQ.ZFC.SubstImp

/-!
# CG-007 · W8 第二层（十八）：`hAll` 支的唯一公式义务 `hkey`（机器证）

`ShCraigElim` 的 `hAll` 支归纳步需要把外层 free 变量收成 `^&0`。
`ProbeHAllRoute.lean` 已把整条归纳步归约到一条公式恒等式 `hkey`
（其余全是 `Derivable` 的构造）。本文件证出 `hkey`。

```
free ℒₛₑₜ (imp domZero (iT 1 p))
  = imp (subst ?[^&0] cDomN) (iT 0 (free ℒₒᵣ p))        (p 层 1)
```

证法四步：
1. `free = substs1 ^&0 ∘ shift`（Foundation 定义）展开两侧；
2. `shift_imp` + `shift_domZero`：LHS 成 `substs1 (imp domZero (iT 1 (shift p)))`；
3. `← iT_shift`：`shift (iT 1 p)` → `iT 1 (shift p)`，再把 `imp` 拆开；
4. **桥 `B`**（`iT_substs1`）把 `iT 1 (shift p)` 换成 `iT 0 (subst ?[^&0] (shift p))`，
   最后 `hD` 收尾 `domZero` 侧。

**因此 `hAll` 支只剩桥 `B` 一条公式义务**（`ITSubsts1.lean` 的 `iT_substs1`，
层 1 版 `iT_substs1'`）。

## 本文件的两个显式参数

- `hB`：桥 `B(q)` = `GodelQ.ITSubsts1.iT_substs1'`；
- `hD`：`subst ?[^&0] domZero = subst ?[^&0] ↑cDomN` = `GodelQ.ITSubsts1.subst_domZero`。

两者都取自 `ITSubsts1.lean`。**该文件当前（2026-10-13 实测）编译尚未通过**
（error 数已从 17 降到 6，重复声明已清零，见
`HoTT/verification/runs/20261013-CG001-Z0-W8-BRIDGE-STATE-0*.txt`），
所以本文件**有意不用 import 它**：`hB`/`hD` 保持为显式参数，
桥一通就可以接线（`hkey` 因此独立于桥的编译状态而过核）。

本文件只 import `ITShift` 与 `SubstImp`（`subst_imp` 从在建的 `ITSubsts1.lean`
抽到 `SubstImp.lean`，正是为了这条"不 import 在建文件"的纪律）。

`#print axioms` 仅 `[propext, Classical.choice, Quot.sound]`，**不含未证明占位所产生的公理**。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate
open GodelQ.ITSubsts1

namespace GodelQ.HAllKey

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`hAll` 路线的唯一公式义务 `hkey`**（2026-10-12 证出）。

把 `free ℒₛₑₜ (imp domZero (iT 1 p))` 归约到 `imp (subst ?[^&0] cDomN) (iT 0 (free ℒₒᵣ p))`。
证法：`free = substs1 ^&0 ∘ shift`，`shift` 进 `imp`，`shift_domZero` 消掉 `domZero` 侧，
`iT_shift` 反向把 `shift (iT 1 p)` 换成 `iT 1 (shift p)`，再上**桥 `B`** 与 `hD`。

依赖两条外部义务：
1. `hB` —— 公式层桥 `B(q)`（`iT_substs1`，本文件集下一步的目标）；
2. `hD` —— `subst ?[^&0] domZero = subst ?[^&0] ↑cDomN`（`subst_domZero` + `substs1`）。 -/
lemma hkey_probe {p : V} (hp1 : IsSemiformula ℒₒᵣ 1 p)
    (hB : ∀ q : V, IsSemiformula ℒₒᵣ 1 q →
      subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) q) = iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) q))
    (hD : subst ℒₛₑₜ (?[^&0] : V) domZero = subst ℒₛₑₜ (?[^&0] : V) ↑(cDomN : ℕ)) :
    free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (1 : V) p)) =
      imp ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) (cDomN : V)) (iT (0 : V) (free ℒₒᵣ p)) := by
  have hq1 : IsSemiformula ℒₒᵣ 1 (shift ℒₒᵣ p) := hp1.shift
  rw [free, free]
  rw [GodelQ.ShiftTools.shift_imp
    (isSemiformula_domZero (n := (0 : V))).isUFormula
    (isSemiformula_iT (n := (1 : V)) p hp1).isUFormula]
  rw [GodelQ.ShiftTools.shift_domZero]
  rw [← GodelQ.ITShift.iT_shift (n := (1 : V)) p hp1]
  -- substs1 分配到 imp；domZero 侧用 subst_domZero 收尾
  have hwf : IsSemitermVec ℒₛₑₜ 1 1 (?[^&0] : V) :=
    IsSemitermVec.singleton.mpr (IsSemiterm.fvar 1 (0 : V))
  have hd : IsSemiformula ℒₛₑₜ (0 + 1) (domZero (V := V)) := isSemiformula_domZero (n := (0 : V))
  have hd1 : IsSemiformula ℒₛₑₜ 1 (domZero (V := V)) := by
    have e : (0 : V) + 1 = 1 := by norm_num
    rw [← e]
    exact hd
  have e : subst ℒₛₑₜ (?[^&0] : V) (imp ℒₛₑₜ domZero (iT (1 : V) (shift ℒₒᵣ p))) =
      imp ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) domZero)
        (subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (shift ℒₒᵣ p))) :=
    subst_imp (n := 1) (m := 1) hd1 (isSemiformula_iT (n := 1) (shift ℒₒᵣ p) hq1) hwf
  rw [substs1]
  rw [e]
  rw [hB (shift ℒₒᵣ p) hq1]
  rw [hD]
  rw [substs1]

#print axioms GodelQ.HAllKey.hkey_probe

end GodelQ.HAllKey
