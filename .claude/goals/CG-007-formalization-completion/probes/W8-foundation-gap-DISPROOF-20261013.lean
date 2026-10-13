import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 「Foundation 空白」前提核验 —— 结论：前提为假（2026-10-13）

我此前报「`termSubstVec` 保 `IsUTermVec` 在 Foundation 里是空白，需要自己证」。
按 [[probe-simp-residual-is-not-a-goal]] 纪律：**先反驳，再证明**。

本探针直接引用两条引理；**exit 0 即证明前提为假**：

* `IsUTermVec.termSubst`（Functions.lean:121）
* `IsSemitermVec.termSubstVec`（Functions.lean:128）

⚠ 注意：这两条**不是** `termSubstVec` 保 `IsUTermVec`——
`IsSemitermVec` 是 class（`isUTermVec` + `bv` 两个字段，Basic.lean:761），
保的是**带绑定变量上界的**更强结论。裸 `IsUTermVec` 版本是它们的推论。

（`IsSemitermVec` 在 `FFL.FirstOrder.Arithmetic.Bootstrapping` 命名空间下，
不在 `IsUTermVec` 的 namespace 里——第一次探针就是这里写错。） -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace GodelQ.ProbeFoundationGap

-- ① 裸版本（我原本以为要自己证的）：是 class 版本的推论
example {n w t : V} (hw : IsUTermVec ℒₒᵣ n w) (ht : IsSemiterm ℒₒᵣ n t) :
    IsUTerm ℒₒᵣ (termSubst ℒₒᵣ w t) :=
  IsUTermVec.termSubst hw ht

-- ② 带 bv 的版本，Foundation 已直接提供
example {n m w t : V} (hw : IsSemitermVec ℒₒᵣ n m w) (ht : IsSemiterm ℒₒᵣ n t) :
    IsSemiterm ℒₒᵣ m (termSubst ℒₒᵣ w t) :=
  IsSemitermVec.termSubst hw ht

-- ③ 向量版：正是「termSubstVec 保 IsUTermVec」的带 bv 形态
example {k n m v w : V} (hw : IsSemitermVec ℒₒᵣ n m w) (hv : IsSemitermVec ℒₒᵣ k n v) :
    IsSemitermVec ℒₒᵣ k m (termSubstVec ℒₒᵣ k w v) :=
  IsSemitermVec.termSubstVec hw hv

end GodelQ.ProbeFoundationGap