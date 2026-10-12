import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeA8
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 本轮定位：`iT_free` 的项层地基是**两条不同向量的等式**

先前把 `iVE_subst` 想成「同一个向量两边都适用」，机器反例否掉了：

* `subst ?[^&0] (iVE 0 t)` **不是** `iVE 0 t`（`eqAtom` 自带的 `#0` 会被换掉）；
* `subst ?[^&0] (iVE 1 t)` **不是** `iVE 0 (termSubst ?[^&0] t)`
  （前者首分量是 `^&0`、后者是 `^#0`）。

正确的形状（由 `iT_free` 的 atom 情形逐项手算得出，`i < 2`、`t` 层数 1）：

```
subst ?[^#i, ^&0] (iVE 1 t) = subst ?[^#i] (iVE 0 (termSubst ?[^&0] t))
```

**两侧的向量不同**：左边是 `conjunct` 的内层代入（保护 `#0`、把 `#1` 换成 `^&0`），
右边是 `termSubst` 后的 `iVE 0`（`#0` 是 `eqAtom` 自己的）。

本文件的例子把这条等式在三个具体项上机器验证。 -/

/-- `t = ^#0`（层数 1）。 -/
example {i : V} (hi : i < 2) :
    subst ℒₛₑₜ (?[^#i, ^&0] : V) (iVE (1:V) (^#(0:V) : V))
      = subst ℒₛₑₜ (?[^#i] : V)
          (iVE (0:V) (termSubst ℒₒᵣ (?[^&0] : V) (^#(0:V) : V))) := by
  have hR : (ℒₛₑₜ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  rw [termSubst_bvar, nth_adjoin_zero]
  rw [iVE_fvar, iVE_bvar, eqAtom, eqAtom]
  rw [show (^#(0+1) : V) = (^#1 : V) by norm_num]
  rw [show (?[^#0, ^#1] : V) = (^#0 : V) ∷ ((^#1 : V) ∷ (0 : V)) from rfl,
    show (?[^#0, ^&0] : V) = (^#0 : V) ∷ ((^&0 : V) ∷ (0 : V)) from rfl,
    show (?[^#i, ^&0] : V) = (^#i : V) ∷ ((^&0 : V) ∷ (0 : V)) from rfl,
    show (?[^#i] : V) = (^#i : V) ∷ (0 : V) from rfl,
    show (?[^&0] : V) = (^&0 : V) ∷ (0 : V) from rfl]
  rw [Bootstrapping.substs_rel (L := ℒₛₑₜ) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (1:V)))) (IsUTerm.bvar (z := (0:V))))),
    Bootstrapping.substs_rel (L := ℒₛₑₜ) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.bvar (z := (1:V)))) (IsUTerm.bvar (z := (0:V))))),
    Bootstrapping.substs_rel (L := ℒₛₑₜ) hR
      (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
        (IsUTerm.fvar (x := (0:V)))) (IsUTerm.bvar (z := (0:V)))))]
  congr 1
  -- 左侧：`termSubstVec 2 (^#i ∷ ?[^&0]) ?[^#0,^#1]` = `?[^#i, ^&0]`
  have hL : termSubstVec ℒₛₑₜ (2:V) (^#i ∷ (^&0 : V) ∷ (0:V)) (^#0 ∷ (^#1 : V) ∷ (0:V))
      = (^#i : V) ∷ ((^&0 : V) ∷ (0:V)) := by
    rw [show (^#0 ∷ (^#1 : V) ∷ (0:V) : V) = (?[^#0, ^#1] : V) from rfl,
      show (^#i ∷ (^&0 : V) ∷ (0:V) : V) = (?[^#i, ^&0] : V) from rfl]
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := i)) (IsUTerm.bvar (z := (1:V))),
      termSubst_bvar, termSubst_bvar]
  -- 右侧：`termSubstVec 2 (^#i ∷ 0) ?[^#0,^&0]`——向量长度 1，越界补零
  have hR' : termSubstVec ℒₛₑₜ (2:V) (^#i ∷ (0:V)) (^#0 ∷ (^&0 : V) ∷ (0:V))
      = (^#i : V) ∷ ((^&0 : V) ∷ (0:V)) := by
    rw [show (^#i ∷ (0:V) : V) = (?[^#i] : V) from rfl]
    rw [resultVec_of_not (L := ℒₛₑₜ) (V := V)]
    · rw [show (?[^#i] : V).[0] = (^#i : V) from rfl]
      rw [show (?[^#i] : V).[0 + 1] = (0 : V) from by
        rw [show (?[^#i] : V) = ((^#i : V) ∷ (0:V)) from rfl]; simp]
      rfl
    · intro h
      have hl := h.lh
      rw [show len (?[^#i] : V) = (1:V) from by simp [len_adjoin, len_nil]] at hl
      norm_num at hl
  rw [hL, hR']

end GodelQ.ProbeA8
