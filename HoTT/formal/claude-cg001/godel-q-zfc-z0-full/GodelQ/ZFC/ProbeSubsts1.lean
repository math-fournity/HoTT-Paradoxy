import GodelQ.ZFC.ITShift
import GodelQ.ZFC.ShiftConjunct

/-!
# CG-007 · W8 第二层（十七）：`iT` 与变量代换的相容律

`hAll` 支需要：把 `iT 1 q` 的自由变量换成 `^&0`（即 `free`/`substs1` 所做的事），
等价于先把 `q` 的自由变量换掉再以层 0 翻译：

```
subst ℒₛₑₜ ?[^&0] (iT 1 q) = iT 0 (termSubst ℒₒᵣ ?[^&0] q)      -- 桥（本文件的目标）
```

`q` 层 1。**机制**：`iVE m ^#z = eqAtom ^#(z+1)`——`iVE` 把 bvar 索引整体加一，
而 `free` 用的向量 `?[^&0]` 在两层量词（`iTR` 的 `qqAlls _ 2`）下长成
`qVec (qVec ?[^&0]) = [#0, #1, ^&0]`——末位的 `^&0` 正好落进被换名的槽。

本文件先证**项层子律 T1**（`t` 层 1）：

```
subst (^#a ∷ ?[^&0]) (iVE 1 t) = subst ?[^#a] (iVE 0 (subst ?[^&0] t))
```

bvar/fvar 支直接算；func 支分 `k = 0`（`ve0`，走 `substs_substs`）与
`k = 2`（`ve2`，走 `subst_qqAlls_two`/`subst_conjunct` + 归纳假设）。

## 陷阱（本会话踩过两次）

`qVec` 用 `termBShift`（bvar **+1**、fvar **不动**），不是 `termShift`（fvar +1）。
按 `termShift` 手算会得出「桥不成立」的**假反例**：实测 `qVec ?[^&0] = [#0, ^&0]`。
-/

set_option maxHeartbeats 8000000

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 原子支：`q = ^rel 2 R ?[^#0, ^#0]`
example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R (?[^#0, ^#0] : V))) =
      subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (^rel 2 R (?[^#0, ^#0] : V))) := by
  trace_state
  sorry

end GodelQ.ProbeSubsts1
