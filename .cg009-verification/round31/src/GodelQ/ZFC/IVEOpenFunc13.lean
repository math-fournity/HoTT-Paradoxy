-- CG-009: settling the layer question for the `conjunct` piece (numeric probe).
import GodelQ.ZFC.IVEOpenFunc10
import GodelQ.ZFC.LayerMono

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.IVEOpenFunc13
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.LayerMono

-- Concrete probe at m = 0: which vector layer fixes `^#i ∷ shiftVec 3 1`?
-- `^#i ∷ shiftVec 3 1` has length 2, entries [^#i, ^#3].
-- Under `subst`, descending 2 binders multiplies the vector by qVec twice.

-- QvecV 3 has length 4, entries [^#0,^#1,^#2,^&0].
-- So index 1 -> ^#1 (identity), index 3 -> ^&0.
example : (QvecV (V := V) 3).[1] = (^#1 : V) := nth_QvecV_lt 3 1 (by norm_num)
example : (QvecV (V := V) 3).[3] = (^&0 : V) := nth_QvecV_last 3

-- The conjunct vector's second entry is ^#3 — and QvecV 3 maps index 3 to ^&0.
-- Therefore `QvecV 3` (i.e. `QvecV (m+3)` at m=0) does NOT fix it.
-- We need `QvecV 4`: length 5, entries [^#0,^#1,^#2,^#3,^&0] — index 3 is identity.
example : (QvecV (V := V) 4).[3] = (^#3 : V) := nth_QvecV_lt 4 3 (by norm_num)

end GodelQ.IVEOpenFunc13


namespace GodelQ.IVEOpenFunc13
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc2 GodelQ.IVEOpenFunc3 GodelQ.IVEOpenFunc4
open GodelQ.IVEOpenFunc5 GodelQ.IVEOpenFunc6 GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc9
open GodelQ.IVEOpenFunc10 GodelQ.LayerMono

/-! ## `iTR` (b = 2) vs `ve2` (b = 3) — the decisive difference

`iTR n 2 R v` uses `conjunct 2 n j (iVE n v.[j])`, whose vector `^#i ∷ shiftVec 2 n`
has length `n+1` and reads indices `0..n`, the last entry being `^#(2+(n-1)) = ^#(n+1)`.
For `n = m+1` the top index is `m+1` with entry `^#(m+2)`.

`ve2 n k f w` uses `conjunct 3 n j w.[j]`, whose vector `^#i ∷ shiftVec 3 n` has
length `n+1` and reads indices `0..n`, the last entry being `^#(3+(n-1)) = ^#(n+2)`.
For `n = m+1` the top index is `m+1` with entry `^#(m+3)`.
-/

-- `iTR` case (b = 2): the top entry is `^#(m+2)`, and `QvecV (m+3)` is the identity
-- on every index `≤ m+2` — so the `b = 2` conjunct is *fixed* by `QvecV (m+3)`.
example (m : V) : (QvecV (V := V) (m + 3)).[m + 2] = (^#(m + 2) : V) := by
  apply nth_QvecV_lt
  have h := lt_add_self_add_one (m + 2) 0
  have e : (0 : V) + (m + 2) + 1 = m + 3 := by ring
  rwa [e] at h

-- `ve2` case (b = 3): the vector reaches `^#(m+3)` at index `m+3` — exactly where
-- `QvecV (m+3)` has `^&0`.  Hence `ve2` needs `QvecV (m+4)`.
example (m : V) : (QvecV (V := V) (m + 3)).[m + 3] = (^&0 : V) := nth_QvecV_last (m + 3)

end GodelQ.IVEOpenFunc13
