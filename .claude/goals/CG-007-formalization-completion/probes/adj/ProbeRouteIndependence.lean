import GodelQ.ZFC.ShCraigElimSetupQ
import GodelQ.ZFC.ITSubstOpen9
/-!
裁决探针 12（**不是收据**）：两条 `AllBlockerQ` 路线是否真的独立？

## 结论：**不独立。** 两条路线在 `ITSubstOpen9.iT_subst_open` 的 m=0 实例上汇合。

## 路线①（Master 装配，`master-assembly-poc-20261014/GodelQ/MasterAssemblyProbe.lean`）

```
ITSubstOpen9.iT_subst_open (V) (0) q        -- 一般开口律 ∀m，取 m = 0
  → (QvecVOr_zero, QvecV_zero, zero_add)
bridgeB : subst ℒₜ ?[^&0] (iT 1 q) = iT 0 (subst ℒₒᵣ ?[^&0] q)
  → allKey_of_bridge → AllKey → allBlockerQ_of_key → AllBlockerQ
```

## 路线②（`HABKey`/`HABElim`/`HAllUncond`，`origin/claude/infallible-mestorf-ce08c0` @ `fd8b8305`）

```
ITSubstOpen9.iT_subst_open (V) (0) (shift ℒₒᵣ p)   -- 同一个一般律，取 m = 0，q := shift p
HABKey.iT_free_eq : iT 0 (free p) = subst ℒₜ ?[^&0] (iT 1 (shift p))
  → HABElim.free_iT（配 iT_shift，把 B 化成 imp (x∈ω) A）
  → HABElim.hAB_derivable（neg A ⋎ (neg C ⋎ A)，排中律）
  → HAllProof.hAll_uncond 的 hAB 参数
  → HAllUncond.hAll（hAll 无条件）
```

## 共同依赖（这是判"独立"的关键）

`HABKey.iT_free_eq` 的证明体逐字是：
```lean
have h := GodelQ.ITSubstOpen9.iT_subst_open (V := V) 0 (shift (L := ℒₒᵣ p)) h1
rw [GodelQ.QvecVDefs.QvecVOr_zero, GodelQ.QvecVDefs.QvecV_zero] at h
rw [show (0 : V) + 1 = 1 from _root_.zero_add 1] at h
exact h
```

而路线①的 `bridgeB` 证明体逐字是：
```lean
have h := GodelQ.ITSubstOpen9.iT_subst_open (V := V) (0 : V) q h1
rw [GodelQ.QvecVDefs.QvecVOr_zero, GodelQ.QvecVDefs.QvecV_zero] at h
rw [show (0 : V) + 1 = 1 from _root_.zero_add 1] at h
exact h.symm
```

**两者调用的是同一条定理的同一个 m=0 实例**，差别只在 `q` 取 `shift p` 还是 `p`、以及取不取 `.symm`。
`ITSubstOpen9.iT_subst_open`（001-Flash 的一般开口律 ∀m）是**两条路线共同且唯一的承载件**。

本探针把这三点在机器侧固定下来。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeTwoRoutes

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 两条路线共同的承载件：一般开口律 ∀m
#check @GodelQ.ITSubstOpen9.iT_subst_open

-- 两条路线都落在同一条定理的 m=0 实例上；这里把两侧的**目标形状**固定下来（不断言可证）
-- 路线②（HABKey.iT_free_eq）：iT 0 (free p) = subst ℒₜ ?[^&0] (iT 1 (shift p))
-- 路线①（bridgeB）        ：subst ℒₜ ?[^&0] (iT 1 q)     = iT 0 (subst ℒₒᵣ ?[^&0] q)
-- 二者经 free 的定义（free p = subst ℒₒᵣ ?[^&0] (shift p)）互化，q := shift p 时形状相同。
example (p : V) (hp : IsSemiformula ℒₒᵣ (1 : V) p) :
    free (L := ℒₒᵣ) p = subst (L := ℒₒᵣ) (?[^&0] : V) (shift (L := ℒₒᵣ) p) := rfl

-- 承载件的签名（两条路线都调它）
#check @GodelQ.ITSubstOpen9.iT_subst_open
#check @GodelQ.QvecVDefs.QvecVOr_zero
#check @GodelQ.QvecVDefs.QvecV_zero

end GodelQ.ProbeTwoRoutes
