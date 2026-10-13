import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **决定性反例（`iT_substs1` 一般版为假）**。

`subst ?[^#0,^&0] (iVE 2 ^#1)` —— `iVE 2 ^#1 = eqAtom ^#2 = ^rel 2 cEqN ?[^#0,^#2]`。
代入向量 `?[^#0,^&0]` 长度 2，而 `^#2` **越界**，故被**补零**为 `0`：

```
subst ?[^#0,^&0] (iVE 2 ^#1) = ^rel 2 cEqN ?[^#0, 0]
```

而 `iT_substs1` 的一般形状要求它是 `iVE 1 ^&0 = ^rel 2 cEqN ?[^#0,^&0]`。
**`0 ≠ ^&0`，故该律不成立。**

这正是「保护语义 vs 替换语义」不可调和的**具体位置**：
`iVE` 引入的绑定变量 `#2` 在 `subst` 下被**补零**，而 `iT` 的绑定层用的是 `qVec`
（首分量 `^#0`）的保护语义——两者对同一个位置给出不同的值。 -/
lemma iVE_bvar2_subst_zero :
    subst ℒₛₑₜ (?[^#0, ^&0] : V) (iVE (2:V) (^#1 : V))
      = (^rel 2 (↑cEqN) (?[^#0, 0] : V) : V) := by
  have hR : (ℒₛₑₜ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  rw [iVE_bvar]
  rw [show eqAtom (^#(1+1) : V) = (^rel 2 (↑cEqN) (?[^#0, ^#(1+1)] : V) : V) from rfl]
  rw [show (^#(1+1) : V) = (^#2 : V) by norm_num]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR
    (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
      (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (2:V)))))]
  congr 1
  rw [show (?[^#0, ^#2] : V) = (^#0 : V) ∷ ((^#2 : V) ∷ (0:V)) from rfl,
    show (?[^#0, 0] : V) = (^#0 : V) ∷ ((0:V) ∷ (0:V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (2:V)))]
  rw [show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
  simp only [termSubst_bvar, nth_adjoin_zero]
  rw [show ((^#0 : V) ∷ ((^&0 : V) ∷ (0:V))).[2] = (0:V) from by
    rw [nth_adjoin_two (^#0 : V) ((^&0 : V) ∷ (0:V))]
    rw [nth_adjoin_one (^&0 : V) (0:V)]
    rw [show (0:V).[0] = fstIdx (0:V) from nth_zero 0]
    simp [fstIdx, pi₁_zero]]

end GodelQ.ProbeFL
