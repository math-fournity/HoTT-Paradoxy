-- CG-009: settle the two open numbers for the func branch.
--  (a) how many binders does ve2's qqAlls wrap?
--  (b) in `iVE_open`'s func branch, what is `n` in `iVE_func` relative to `mm`?
import GodelQ.ZFC.QVec2Probe2

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.Ve2BinderProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

/-- **(a)** `ve2 n k f w` = `qqAlls <body> 2` — exactly **two** binders. -/
example (n k f w : V) : ve2 n k f w =
    qqAlls (imp ℒₛₑₜ (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤))
      (subst ℒₛₑₜ ((^#2 : V) ∷ ?[^#0, ^#1]) (cFunc k f))) 2 := by
  rw [ve2]

end GodelQ.Ve2BinderProbe

namespace GodelQ.Ve2BinderProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

/-- **(b)** In `iVE_open`'s func branch the layer passed to `iVE` is `mm + 1`,
    so `iVE_func`'s `n` is `mm + 1`, i.e. `ve2 (mm+1) 2 f _` and
    `conjunct 3 (mm+1) i _` with `i ∈ {0,1}`.  Two descents turn the outer
    vector `QvecV (mm+1)` into `QvecV (mm+3)` — exactly the layer
    `subst_QvecV_conjunct` wants (with `n := mm+1`). -/
example (mm : V) : (mm + 1) + 2 = mm + 3 := by ring

end GodelQ.Ve2BinderProbe

namespace GodelQ.Ve2BinderProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

/-- The exact residual mismatch, spelled out as a checked arithmetic fact.

    Body of `ve2 (mm+1) 2 f w` contains `conjunct 3 (mm+1) i _`, so
    `subst_QvecV_conjunct` applies with `n := mm+1` and vector `QvecV (mm+4)`.
    The outer `subst (QvecV (mm+1))` descends `ve2`'s two `qqAlls` binders,
    giving `qVec² (QvecV (mm+1)) = QvecV (mm+3)`.
    Hence the residual mismatch is exactly one level: `mm+4` vs `mm+3`.

    Either (i) `ve2` really has a third binder somewhere, or (ii) the outer
    vector in `iVE_open`'s statement should be `QvecV (mm+2)`, or (iii)
    `subst_QvecV_conjunct` needs a *weaker* hypothesis than `i < n+3`.
    Option (iii) is the interesting one: the conjunct's own vector
    `^#i ∷ shiftVec 3 n` has length `n+1` and needs only `QvecV` to be the
    identity on `0..n+1`... which `QvecV (n+2)` (length `n+3`, identity on
    `0..n+1`) already does. -/
example (mm : V) : (mm + 1) + 3 = mm + 4 := by ring
example (mm : V) : (mm + 1) + 2 = mm + 3 := by ring

end GodelQ.Ve2BinderProbe

namespace GodelQ.Ve2BinderProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

/-- The conjunct's own substitution vector `^#i ∷ shiftVec 3 n` has length `n+1`
    and its entries read only indices `{i} ∪ {3..n+2}`.  Wait: `shiftVec 3 n`
    has `n` entries `^#(3+j)` for `j < n`, so the max index used is `3 + (n-1)
    = n+2`; and the *vector length* is `n+1`, so `termSubstVec` reads the
    substitution vector only at indices `0..n` — i.e. at `i` and `3+j` for
    `j < n` mapped through... no.  `termSubstVec k w v` reads `w` at the index
    baked into each *entry of v*, not at `0..k`.  So `QvecV w` must be the
    identity at indices `i` and `3+j` (`j<n`), the largest being `n+2`.
    `QvecV (n+3)` (length `n+4`, identity on `0..n+2`) suffices; but so does
    `QvecV (n+3)` only — `QvecV (n+2)` (length `n+3`, identity on `0..n+1`)
    is NOT enough because index `n+2` is needed.

    **So option (iii) is refuted**: the hypothesis `i < n+3` with vector
    `QvecV (n+3)` is exactly right, and the residual mismatch is real. -/
example (n j : V) (hj : j < n) : 3 + j < n + 3 := lt_three_add_three hj

end GodelQ.Ve2BinderProbe

namespace GodelQ.Ve2BinderProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

-- Confirm: `termSubstVec k w v` at entry i equals `termSubst w v.[i]`, and
-- `termSubst w ^#z = w.[z]` — so `w` is read at the bvar index `z`, not at `i`.
example (k w v z : V) (_hw : IsUTermVec ℒₛₑₜ k w) (hv : IsUTermVec ℒₛₑₜ k v)
    (i : V) (hi : i < k) (hz : v.[i] = (^#z : V)) :
    (termSubstVec ℒₛₑₜ k w v).[i] = w.[z] := by
  rw [nth_termSubstVec hv hi, hz, termSubst_bvar]

end GodelQ.Ve2BinderProbe

namespace GodelQ.Ve2BinderProbe
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.IVEOpenFunc11 GodelQ.IVEOpenFunc12

/-- **Decisive check**: inside `ve2 (mm+1) 2 f w` the conjunct is
    `conjunct 3 (mm+1) i _`, whose vector `^#i ∷ shiftVec 3 (mm+1)` has
    entries at bvar-index `3 + j` for `j < mm+1`, so the largest is
    `3 + mm = mm + 3`.  The descent of the outer `subst (QvecV (mm+1))`
    through `ve2`'s two `qqAlls` yields `QvecV (mm+3)`, whose slot at
    index `mm+3` is `^&0` — **not** the identity.  Hence the two `qqAlls`
    descents do NOT suffice on their own: one more level is needed.

    Where does the extra level come from?  Answer: `subst` on `^∀ p`
    replaces `w` by `qVec w`, and `qVec` *prepends* `^#0` — so after the
    descent the body's free bvar indices have all been shifted by 2 as well.
    The `conjunct` inside the body therefore sees its own `y` already
    shifted, and `subst_QvecV_conjunct` must be applied to the *shifted*
    conjunct, not the raw one.  That is exactly what `shift_conjunct`
    (`TranslateShiftCompat.lean`) is for — the parallel `ve2` lemma
    `shift_ve2` does the same dance.

    **Conclusion**: the func branch needs BOTH
      `substs_all` (twice, to descend) AND
      `shift_conjunct` (to realign the inner conjunct),
    composed.  Both ingredients already exist and are proved. -/
example (mm j : V) (hj : j < mm + 1) : 3 + j < mm + 1 + 3 :=
  lt_three_add_three (n := mm + 1) hj

/-- `QvecV (mm+3)`'s slot at index `mm+3` is `^&0`, i.e. NOT the identity.
    So the two `qqAlls` descents alone cannot fix the inner conjunct. -/
example (mm : V) : (QvecV (V := V) (mm + 3)).[mm + 3] = (^&0 : V) :=
  nth_QvecV_last (mm + 3)

end GodelQ.Ve2BinderProbe
