import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `iT_substs1` 的 `nrel` 支**归约到 `rel` 支**（2026-10-13）

`iT_substs1`（003 线 `ITSubsts1.lean`）九支里：`rel` **已证**、`nrel` **未证**（唯一 `sorry`）。
本探针给出 `nrel` 支从 `rel` 支的**归约**——`nrel` 支不含新的数学内容。

### 归约（σ = `^nrel k R v`）

```
左 = iT 0 (subst ?[^&0] (^nrel k R v))
   = iT 0 (^nrel k R (termSubstVec ℒₒᵣ k ?[^&0] v))      -- substs_nrel
   = neg (iTR 0 k R (termSubstVec ℒₒᵣ k ?[^&0] v))        -- iT_nrel
   = neg (iT 0 (^rel k R (termSubstVec ℒₒᵣ k ?[^&0] v)))  -- ← iT_rel（反向）
右 = subst ?[^&0] (iT 1 (^nrel k R v))
   = subst ?[^&0] (neg (iTR 1 k R v))                      -- iT_nrel
   = neg (subst ?[^&0] (iTR 1 k R v))                      -- substs_neg
```

**两边同构**：左 `neg (X)`、右 `neg (Y)`，其中

* `X = iTR 0 k R (termSubstVec ℒₒᵣ k ?[^&0] v)`
* `Y = subst ?[^&0] (iTR 1 k R v)`

而 **`X = Y` 正是 `rel` 支的结论**——`rel` 支证的就是
`iT 0 (subst ?[^&0] (^rel k R v)) = subst ?[^&0] (iTR 1 k R v)`，
左端经 `iT_rel` 展开即 `X`。

⟹ **`nrel` 支 = `rel` 支 + 三条现成引理**，无需重复 `rel` 支那几十行分量比对。

### 落成 Lean 的写法（给 003）

```lean
· -- nrel
  intro n param k R v hR hv h h1
  -- 与 rel 支同：先定 k = 2、造层副本
  have hk : k = (2:V) := by
    rcases Arithmetic.isRel_iff_LOR.mp hR with hh | hh <;> exact hh.1
  subst hk
  rw [Bootstrapping.substs_nrel (L := ℒₒᵣ) hR hv.isUTerm]   -- 左端展开
  -- …（与 rel 支相同的层数簿记：hn1 / hvp / hvw / hsub2）
  rw [iT_nrel hR hsub2.isUTerm]                              -- 左 → neg (iTR …)
  rw [iT_nrel hR hv]                                         -- 右内层 → neg (iTR …)
  rw [substs_neg (isSemiformula_iTR hR hv) (isSemitermVec_single_fvar …)]
  -- 剩：neg (iTR 0 2 R (termSubstVec …)) = neg (subst ?[^&0] (iTR 1 2 R v))
  congr 1
  -- 这正是 rel 支已证的那条（把 rel 支抽成独立 lemma 后直接引用）
  exact iT_substs1_rel_branch hR hv h h1
```

**建议**：把 `rel` 支的证明体**抽成独立 `lemma`**（如 `iT_substs1_rel_branch`），
`rel` 支与 `nrel` 支各一行引用——这样 `nrel` 支不再需要复制那几十行。

### 本探针已核（exit 0）

四条零件全部存在且签名如预期：

```
#check @Bootstrapping.substs_nrel   -- subst w (^nrel k R v) = ^nrel k R (termSubstVec L k w v)
#check @GodelQ.Translate.iT_nrel    -- iT n (^nrel k R v) = neg (iTR n k R v)
#check @Bootstrapping.substs_neg    -- subst w (neg p) = neg (subst w p)   （要 IsSemiformula + IsSemitermVec）
#check @GodelQ.Translate.iT_rel     -- iT n (^rel k R v) = iTR n k R v
```

⚠ **注意 `substs_neg` 的前提**：它要 `IsSemiformula L n p`（**层数 `n` 与向量层 `m` 分开**）
与 `IsSemitermVec L n m w`——`rel` 支已有的那些 `hYs`/`hX` 型良构性证明在这里同样要给。
`iT_nrel` 要 `IsUTermVec`（**不是** `IsSemitermVec`）。

**性质照实写明**：本探针只核验零件可用 + 给出归约骨架；
**归约本身未在 Lean 里落成**（003 树里 `ITSubsts1.lean` 尚未编译通过，
本树无该模块的 olean，无法端到端编译）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeNR
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

#check @Bootstrapping.substs_nrel
#check @GodelQ.Translate.iT_nrel
#check @Bootstrapping.substs_neg
#check @GodelQ.Translate.iT_rel

end GodelQ.ProbeNR
