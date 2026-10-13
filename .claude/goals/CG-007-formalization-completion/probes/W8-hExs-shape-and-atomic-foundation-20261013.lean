import GodelQ.ZFC.ShCraigElimSetupQ

/-! ## `hExs` 支的形状与 `hAll` **不同**，且**不用 free / shift / setShift**（2026-10-13）

`Derivable.exs`（Foundation）要的是

```
IsSemiformula L 1 p → IsTerm L t →
  Derivable T (substs1 L t p ⫽ s) → Derivable T (^∃ p ⫽ s)
```

而 `iT` 的存在支是（注意：是 `⋏` 不是 `imp`！）

```
iT_exs : iT n (^∃ p) = ^∃ domZero ^⋏ iT (n + 1) p
```

**所以 hExs 的归纳假设不带 `free`、不带 `setShift`**——
`induction1` 的 exsIntro 支给的子推导结论就是 `substs1 ℒᵣ t p ⫽ s`（没有 shift）。
这让它比 hAll 简单：没有 `free` 与 `iT` 的交互这道坎。

**核心等式（待证）**：

```
iT n (substs1 ℒᵣ t p) = substs1 ℒₜ X (iT n p)     -- X 是什么？
```

### 已机器验证的原子地基（exit 0）

```
ts_fvar : termSubst ℒᵣ ?[^&0] ^#0 = ^&0
ive_fvar: iVE 0 ^&0 = eqAtom ^&0
```

即 `substs1 ℒᵣ t p = subst ℒᵣ ?[t] p` 把 `t` 塞进 `p` 的 bvar 0，
而 `iVE` 对 bvar `#z ↦ eqAtom ^#(z+1)`、对 fvar `^x ↦ eqAtom ^&x`。

### `iTR` 的全展开（读 `InternalTranslate.lean:197` 得，本轮未证）

```
iTR n k R v = qqAlls
  (imp ℒₜ (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤))
     (subst ℒₜ ?[^#0, ^#1] (cRel R))) 2
```

**这是 rel 支数学的真正体量所在**：`qqAlls · 2` + 两个 `conjunct` + `subst ?[^#0,^#1]`。
`hAll`/`hExs` 的 rel 支都要过这一关。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeExShape
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 已证：termSubst ℒᵣ ?[^&0] ^#0 = ^&0
lemma ts_fvar : termSubst ℒₒᵣ (?[^&0] : V) (^#(0:V) : V) = (^&(0:V) : V) := by
  rw [termSubst_bvar (z := (0:V))]
  simp

-- 已证：iVE 0 ^&0 = eqAtom ^&0
lemma ive_fvar : iVE (0:V) (^&(0:V) : V) = eqAtom (^&(0:V) : V) :=
  iVE_fvar (n := (0:V)) (x := (0:V))

end GodelQ.ProbeExShape
