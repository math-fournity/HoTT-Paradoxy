import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **⚠ 一次失败的反驳尝试（记录下来避免重犯）**

我曾想用 `v = ?[^&0, ^&0]` 反驳 `iT_substs1_atom_gen`，理由是
「`subst ?[^&0]` 只有 1 格、`^rel` 元数 2，故第 2 格越界补零」。

**这个理由是错的。** `termSubst_fvar` 说 fvar **不动**：

```
termSubst L w ^&x = ^&x
```

故 `termSubstVec 2 ?[^&0] ?[^&0,^&0] = ?[^&0, ^&0]`（**没有补零**），
本引理机器确认。越界补零只发生在 **bvar** `^#z` 且 `z ≥ len w` 时。

**教训**：`subst` 对 fvar 不动——想构造越界反例，`v` 的分量必须是 **bvar**。 -/
lemma fvar_no_zerofill :
    termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) (?[^&0, ^&0] : V) = (?[^&0, ^&0] : V) := by
  rw [termSubstVec_cons₂ (IsUTerm.fvar (x := (0:V))) (IsUTerm.fvar (x := (0:V)))]
  rw [termSubst_fvar, termSubst_fvar]

/-- **bvar 才会补零**（对照）：`?[^#1, ^#0]` 的第 0 格 `^#1` 越界补零为 `0`。 -/
lemma bvar_zerofill :
    termSubstVec ℒₒᵣ (2:V) (?[^&0] : V) (?[^#1, ^#0] : V) = (?[0, ^&0] : V) := by
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (1:V))) (IsUTerm.bvar (z := (0:V)))]
  rw [termSubst_bvar, termSubst_bvar]
  rw [show ((^&0 : V) ∷ (0:V)).[1] = (0:V) from by
    rw [show ((^&0 : V) ∷ (0:V)) = (^&0 : V) ∷ (0:V) from rfl]
    rw [nth_adjoin_one]
    rfl]
  rw [show ((^&0 : V) ∷ (0:V)).[0] = (^&0 : V) from nth_adjoin_zero _ _]

end GodelQ.ProbeFL
