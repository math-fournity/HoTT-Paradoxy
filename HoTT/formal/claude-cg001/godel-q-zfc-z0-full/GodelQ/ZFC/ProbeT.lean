import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeT
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `W n`：`free` 在 `iT` 上的代入向量

`free X = subst ℒₛₑₜ ?[^&0] (shift X)`。把 `subst` 推过 `iT` 内部的 `n` 层量词后，
向量变成 `qVec^n ?[^&0]`。本文件把它写成**原始递归**（照 `shiftVec` 的先例）：

```
W n = ?[^#0, ^#1, …, ^#(n-1), ^&0]      （n + 1 个分量）
```

即 `W 0 = ?[^&0]`，`W (n+1) = ^#0 ∷ termBShiftVec (W n)`。

先证三条基本性质（照 `shiftVec` 的写法）。 -/

section W

/-! **`W n` 的构造**：`W 0 = ?[^&0]`，`W (n+1) = ^#0 ∷ termBShiftVec n (W n)`。

**长度与层数的账**（照 `shiftVec` 的 `b n` 两参形式）：
`W n` 有 `n + 1` 个分量（`n` 个 bvar 加一个 fvar），层数为 `n + 1`。
`termBShiftVec k v` 保持 `len v` 不变、把层数加一。
所以 `W_succ` 里 `termBShiftVec` 的第一个参数（长度）应是 `len (W n) = n + 1`。
下面的定义把 `n` 作为**索引**传入，`W_succ` 的等式里用 `n + 1` 写长度——
与 `shiftVec_succ`（那里 `termBShiftVec n ih` 的 `n` 恰好是长度）不同，
因为 `shiftVec` 的 `zero` 是空向量而 `W` 的 `zero` 已有一个分量。 -/

noncomputable def W.blueprint : PR.Blueprint 1 where
  zero := .mkSigma “y b. ∃ f, !qqFvarDef f 0 ∧ !adjoinDef y f 0”
  succ := .mkSigma “y ih n. ∃ h, !qqBvarDef h 0 ∧ ∃ t, !(termBShiftVecGraph ℒₛₑₜ) t (n + 1) ih ∧ !adjoinDef y h t”

noncomputable def W.construction : PR.Construction V W.blueprint where
  zero := fun _ ↦ (?[^&0] : V)
  succ := fun _ n ih ↦ ^#(0:V) ∷ termBShiftVec ℒₛₑₜ (n + 1) ih
  zero_defined := .mk fun v ↦ by simp [W.blueprint]
  succ_defined := .mk fun v ↦ by simp [W.blueprint]

/-- `W n = ?[^#0, ^#1, …, ^#(n-1), ^&0]`（`n + 1` 个分量）。 -/
noncomputable def W (n : V) : V := W.construction.result ![0] n

@[simp] lemma W_zero : W (V := V) 0 = (?[^&0] : V) := by
  simp [W, W.construction]

@[simp] lemma W_succ (n : V) :
    W (V := V) (n + 1) = ^#(0:V) ∷ termBShiftVec ℒₛₑₜ (n + 1) (W (V := V) n) := by
  simp [W, W.construction]

-- 首分量恒为 `^#0`（`conjunct` 的换名靠它）
@[simp] lemma W_head (n : V) : (W (V := V) (n + 1)).[0] = (^#(0:V) : V) := by
  rw [W_succ, nth_adjoin_zero]

-- `W n` 是项向量（长度 `n+1`、层数 `n+1`）——`V` 层的 `len` 账用 `IsUTermVec` 绕开
lemma isUTermVec_W : ∀ n : ℕ, IsUTermVec ℒₛₑₜ ((n : V) + 1) (W (V := V) (n : V)) := by
  intro n
  induction n with
  | zero =>
    rw [Nat.cast_zero, W_zero]
    exact IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.fvar (x := (0:V)))
  | succ k ih =>
    rw [show ((k + 1 : ℕ) : V) = (k : V) + 1 by push_cast; ring, W_succ]
    exact IsUTermVec.adjoin (ih.termBShiftVec) (IsUTerm.bvar (z := (0:V)))

end W

/-! ## `iT_free` 的一般形状（用 `W` 陈述）

猜想：

```
iT_free :  iT n (subst ℒₒᵣ (W n) p) = subst ℒₛₑₜ (W n) (iT (n + 1) p)     （p 层 n+1）
```

`n = 0` 时 `W 0 = ?[^&0]`，即 `iT 0 (subst ?[^&0] p) = subst ?[^&0] (iT 1 p)`
——正是 `hAll` 要的（配合已证的 `iT_shift` 与 `free_imp_domZero`）。

先用 `semiformula_result_induction` 搭骨架，`rel` 支先留。 -/

/-! **层数配对的重新审视**：`iT_shift` 能用 `param = n` 是因为它**不改层数**。
`iT_free` 里 `subst (W param) p` 与 `iT param` 是同层，但右边要 `iT (param+1) p`
——差一层，这正是 `free` 剥掉一层绑定的体现。

**绕法**：不走 `semiformula_result_induction` 的 `result`，
而是**先证 `iT` 在 `subst` 下的显式计算规则**（对每个构造子），
用 `iT_rel`/`iT_all` 这类**已有的**计算规则（它们直接给出 `iT n` 的形状，
不经过 `result`）。这样层数配对由 `iT_all` 的 `iT (n+1)` 自然给出。

下面先测最简的**原子**情形（`param = 0`，`p = ^rel 2 R ?[^#0,^#0]`）。 -/

-- `W 0 = ?[^&0]`
example : W (V := V) 0 = (?[^&0] : V) := W_zero

-- 原子情形：`iT 0 (subst ?[^&0] p) = subst ?[^&0] (iT 1 p)`
example {R : V} (hR : (ℒₒᵣ).IsRel 2 R) :
    iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (^rel 2 R (?[^#0, ^#0] : V)))
      = subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (^rel 2 R (?[^#0, ^#0] : V))) := by
  have hbB : IsSemiterm ℒₒᵣ 1 (^#(0:V) : V) := IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)
  have hvB : IsSemitermVec ℒₒᵣ 2 1 (?[^#0, ^#0] : V) := IsSemitermVec.doubleton.mpr ⟨hbB, hbB⟩
  have htv : termSubstVec ℒₒᵣ 2 (?[^&0] : V) (?[^#0, ^#0] : V) = (?[^&0, ^&0] : V) := by
    rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0 : V)) from rfl]
    rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (0:V)))]
    simp only [termSubst_bvar, nth_adjoin_zero]
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hvB.isUTerm, htv]
  rw [iT_rel (V := V) (n := (0 : V)) (k := (2 : V)) (R := R)
    (v := (?[^&0, ^&0] : V)) hR
    (IsSemitermVec.doubleton.mpr ⟨IsSemiterm.fvar (n := 1) 0, IsSemiterm.fvar (n := 1) 0⟩).isUTerm]
  rw [iT_rel (V := V) (n := (1 : V)) (k := (2 : V)) (R := R)
    (v := (?[^#0, ^#0] : V)) hR hvB.isUTerm]
  simp only [iTR]
  -- 两侧都形如 `qqAlls · 2`；右侧要推 `subst ?[^&0]` 过去（`substs_all` 用 `qVec`）
  -- 左边内层：`conjunct 2 0 i (iVE 0 ^&0)`
  -- 右边内层：`conjunct 2 1 i (iVE 1 ^#0)`，经 `subst (qVec² ?[^&0])`
  have hbody : IsUFormula ℒₛₑₜ
      (imp ℒₛₑₜ (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V)) ^⋏
          (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V)) ^⋏ ^⊤))
        (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R))) := by
    have hc0 : IsSemiformula ℒₛₑₜ 3 (conjunct 2 1 0 (iVE (1:V) (^#(0:V) : V))) :=
      isSemiformula_conjunct (b := 2) (n := 1) (i := 0)
        (isSemiformula_iVE (n := 1) (^#(0:V) : V)
          (IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)))
        (by norm_num)
    have hc1 : IsSemiformula ℒₛₑₜ 3 (conjunct 2 1 1 (iVE (1:V) (^#(0:V) : V))) :=
      isSemiformula_conjunct (b := 2) (n := 1) (i := 1)
        (isSemiformula_iVE (n := 1) (^#(0:V) : V)
          (IsSemiterm.bvar.mpr (Arithmetic.zero_lt_one : (0:V) < 1)))
        (by norm_num)
    have hsub : IsSemiformula ℒₛₑₜ 3 (subst ℒₛₑₜ (?[^#0, ^#1] : V) (cRel R)) :=
      IsSemiformula.subst (L := ℒₛₑₜ) (isSemiformula_cRel R)
        (by simpa using isSemitermVec_two_bvars (n := 1))
    exact IsUFormula.or.mpr
      ⟨(IsSemiformula.and.mpr ⟨hc0, IsSemiformula.and.mpr ⟨hc1, IsSemiformula.verum⟩⟩).isUFormula.neg,
       hsub.isUFormula⟩
  -- 右侧最外层是 `^∀`，直接推
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ) (IsUFormula.all.mpr hbody)]
  congr 1
  -- 内层：`qqAlls BODY_L 1 = subst (qVec ?[^&0]) (qqAlls BODY_R 1)`
  rw [Bootstrapping.substs_all (L := ℒₛₑₜ) hbody]
  sorry

end GodelQ.ProbeT
