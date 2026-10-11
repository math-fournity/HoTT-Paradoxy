import GodelQ.ZFC.ShRE

/-!
# CG-007 · W4b：算术到集合论的翻译，在 𝗜𝚺₁ 内部写成 Σ1 函数

Foundation 的 `arithTrln.translate`（S3 的直接翻译：把算术解释在 ω 上）是按公式结构递归定义的 Lean 函数。
本文件在 𝗜𝚺₁ 的每个模型 V 内部，用 Foundation 的内部递归机制重写这条翻译，并证明二者逐字一致：

* `iVE n t`：项的内部递归（`Language.TermRec`），对应 `varEqual`（“#0 等于项 t 的值”，层数 n）；
* `iTR n k R v`：原子公式的内部翻译，对应 `translateRel`；
* `iT n p`：公式的内部递归（`UformulaRec1`），对应 `translate`；量词换成限制在 ω 上的量词，
  层数参数在量词下加一。
* 三者都是 𝚺₁ 可定义的函数（`iVE_defined`、`iTR_defined`、`iT_defined`）。
* **正确性**：对每个闭项 t，`iVE n ⌜t⌝ = ⌜varEqual t⌝`（`iVE_quote`）；对每个算术公式 φ，
  `iT n ⌜φ⌝ = ⌜translate φ⌝`（`iT_quote`）。证明在任意 𝗜𝚺₁ 模型中进行，沿项与公式的结构归纳。

符号表（ℒₒᵣ 的编码）：零 0、一 1（0 元），加 0、乘 1（2 元）；等号 0、小于 1。翻译用到的固定公式
（定义域、函数与关系的定义公式）以编码常数进入（`cDomN`、`cFuncN`、`cRelN`）。
-/

namespace GodelQ.Translate

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.ZFCArith
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `shiftVec b n = [^#b, ^#(b+1), …, ^#(b+n-1)]` -/

section shiftVec

noncomputable def shiftVec.blueprint : PR.Blueprint 1 where
  zero := .mkSigma “y b. y = 0”
  succ := .mkSigma “y ih n b. ∃ h, !qqBvarDef h b ∧ ∃ t, !(termBShiftVecGraph ℒₛₑₜ) t n ih ∧ !adjoinDef y h t”

noncomputable def shiftVec.construction : PR.Construction V shiftVec.blueprint where
  zero := fun _ ↦ 0
  succ := fun b n ih ↦ ^#(b 0) ∷ termBShiftVec ℒₛₑₜ n ih
  zero_defined := .mk fun v ↦ by simp [shiftVec.blueprint]
  succ_defined := .mk fun v ↦ by simp [shiftVec.blueprint]

/-- `shiftVec b n = [^#b, ^#(b+1), …, ^#(b+n-1)]`。 -/
noncomputable def shiftVec (b n : V) : V := shiftVec.construction.result ![b] n

@[simp] lemma shiftVec_zero (b : V) : shiftVec b 0 = 0 := by
  simp [shiftVec, shiftVec.construction]

@[simp] lemma shiftVec_succ (b n : V) :
    shiftVec b (n + 1) = ^#b ∷ termBShiftVec ℒₛₑₜ n (shiftVec b n) := by
  simp [shiftVec, shiftVec.construction]

noncomputable def shiftVecDef : 𝚺ᴬ₁.Semisentence 3 :=
  shiftVec.blueprint.resultDef |>.rew (Rew.subst ![#0, #2, #1])

instance shiftVec_defined : 𝚺ᴬ₁-Function₂ (shiftVec : V → V → V) via shiftVecDef := .mk
  fun v ↦ by simp [shiftVec.construction.result_defined_iff, shiftVecDef]; rfl

end shiftVec

/-! ## 固定公式的编码（常数） -/

section constants

/-- 定义域公式 `x ∈ ω` 的编码。 -/
noncomputable def cDomN : ℕ := ⌜(arithTrln.domain : Semisentence ℒₛₑₜ 1)⌝

/-- 函数符号的定义公式的编码：按元数 k 与符号编码 f 分派（0 元：零、一；2 元：加、乘）。 -/
noncomputable def cFuncN (k f : ℕ) : ℕ :=
  if k = 0 then
    (if f = 0 then ⌜(arithTrln.func Language.ORing.Func.zero : Semisentence ℒₛₑₜ 1)⌝
     else ⌜(arithTrln.func Language.ORing.Func.one : Semisentence ℒₛₑₜ 1)⌝)
  else
    (if f = 0 then ⌜(arithTrln.func Language.ORing.Func.add : Semisentence ℒₛₑₜ 3)⌝
     else ⌜(arithTrln.func Language.ORing.Func.mul : Semisentence ℒₛₑₜ 3)⌝)

/-- 关系符号的翻译公式的编码（等号、小于）。 -/
noncomputable def cRelN (R : ℕ) : ℕ :=
  if R = 0 then ⌜(arithTrln.rel Language.ORing.Rel.eq : Semisentence ℒₛₑₜ 2)⌝
  else ⌜(arithTrln.rel Language.ORing.Rel.lt : Semisentence ℒₛₑₜ 2)⌝

/-- ℒₛₑₜ 的等号关系的编码。 -/
noncomputable def cEqN : ℕ := Encodable.encode (Language.Eq.eq : (ℒₛₑₜ).Rel 2)

end constants


/-! ## 内部变量等式（varEqual）的各个部件 -/

section parts

/-- 原子 `#0 = t`（ℒₛₑₜ 的等号）的编码。 -/
noncomputable def eqAtom (t : V) : V := ^rel 2 (cEqN : V) ?[^#0, t]

noncomputable def eqAtomDef : 𝚺ᴬ₁.Semisentence 2 := .mkSigma
  “y t. ∃ b, !qqBvarDef b 0 ∧ ∃ v, !mkVec₂Def v b t ∧ !qqRelDef y 2 ↑cEqN v”

instance eqAtom_defined : 𝚺ᴬ₁-Function₁ (eqAtom : V → V) via eqAtomDef := .mk fun v ↦ by
  simp [eqAtomDef, eqAtom, numeral_eq_natCast]

/-- 函数符号定义公式的编码（V 中）。 -/
noncomputable def cFunc (k f : V) : V :=
  if k = 0 then (if f = 0 then ((cFuncN 0 0 : ℕ) : V) else ((cFuncN 0 1 : ℕ) : V))
  else (if f = 0 then ((cFuncN 2 0 : ℕ) : V) else ((cFuncN 2 1 : ℕ) : V))

noncomputable def cFuncDef : 𝚺ᴬ₁.Semisentence 3 := .mkSigma
  “y k f. (k = 0 ∧ f = 0 ∧ y = ↑(cFuncN 0 0)) ∨ (k = 0 ∧ f ≠ 0 ∧ y = ↑(cFuncN 0 1)) ∨
    (k ≠ 0 ∧ f = 0 ∧ y = ↑(cFuncN 2 0)) ∨ (k ≠ 0 ∧ f ≠ 0 ∧ y = ↑(cFuncN 2 1))”

instance cFunc_defined : 𝚺ᴬ₁-Function₂ (cFunc : V → V → V) via cFuncDef := .mk fun v ↦ by
  simp only [cFuncDef, cFunc]
  by_cases hk : v 1 = 0 <;> by_cases hf : v 2 = 0 <;> simp [hk, hf, numeral_eq_natCast]

/-- 合取项 `A_i = domain/[#i] ⋏ (y 换名：#0 ↦ #i，#(j+1) ↦ #(j+b))`。 -/
noncomputable def conjunct (b n i y : V) : V :=
  (subst ℒₛₑₜ ?[^#i] (cDomN : V)) ^⋏ (subst ℒₛₑₜ (^#i ∷ shiftVec b n) y)

noncomputable def conjunctDef : 𝚺ᴬ₁.Semisentence 5 := .mkSigma
  “r b n i y. ∃ bi, !qqBvarDef bi i ∧ ∃ v1, !mkVec₁Def v1 bi ∧ ∃ d, !(substsGraph ℒₛₑₜ) d v1 ↑cDomN ∧
    ∃ sv, !shiftVecDef sv b n ∧ ∃ wv, !adjoinDef wv bi sv ∧ ∃ e, !(substsGraph ℒₛₑₜ) e wv y ∧
    !qqAndDef r d e”

instance conjunct_defined : 𝚺ᴬ₁-Function₄ (conjunct : V → V → V → V → V) via conjunctDef := .mk
  fun v ↦ by simp [conjunctDef, conjunct, numeral_eq_natCast]

end parts

/-! ## 内部变量等式 `iVE n t`（对项的内部递归） -/

section iVE

/-- 0 元函数符号：`⊤ 🡒 F_f[#0]`。 -/
noncomputable def ve0 (k f : V) : V := imp ℒₛₑₜ ^⊤ (subst ℒₛₑₜ ?[^#0] (cFunc k f))

noncomputable def ve0Def : 𝚺ᴬ₁.Semisentence 3 := .mkSigma
  “y k f. ∃ c, !cFuncDef c k f ∧ ∃ b, !qqBvarDef b 0 ∧ ∃ v1, !mkVec₁Def v1 b ∧
    ∃ s, !(substsGraph ℒₛₑₜ) s v1 c ∧ ∃ t, !qqVerumDef t ∧ !(impGraph ℒₛₑₜ) y t s”

instance ve0_defined : 𝚺ᴬ₁-Function₂ (ve0 : V → V → V) via ve0Def := .mk fun v ↦ by
  simp [ve0Def, ve0]

/-- 2 元函数符号：`∀∀ ((A₀ ⋏ (A₁ ⋏ ⊤)) 🡒 F_f[#2, #0, #1])`，`A_i` 由第 i 个参数的结果换名得到。 -/
noncomputable def ve2 (n k f w : V) : V :=
  qqAlls (imp ℒₛₑₜ (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ^⊤))
    (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) (cFunc k f))) 2

noncomputable def ve2Def : 𝚺ᴬ₁.Semisentence 5 := .mkSigma
  “y n k f w. ∃ w0, !nthDef w0 w 0 ∧ ∃ w1, !nthDef w1 w 1 ∧ ∃ a0, !conjunctDef a0 3 n 0 w0 ∧
    ∃ a1, !conjunctDef a1 3 n 1 w1 ∧ ∃ t, !qqVerumDef t ∧ ∃ c1, !qqAndDef c1 a1 t ∧
    ∃ c0, !qqAndDef c0 a0 c1 ∧ ∃ c, !cFuncDef c k f ∧ ∃ b0, !qqBvarDef b0 0 ∧
    ∃ b1, !qqBvarDef b1 1 ∧ ∃ b2, !qqBvarDef b2 2 ∧ ∃ v2, !mkVec₂Def v2 b0 b1 ∧
    ∃ v3, !adjoinDef v3 b2 v2 ∧ ∃ s, !(substsGraph ℒₛₑₜ) s v3 c ∧ ∃ im, !(impGraph ℒₛₑₜ) im c0 s ∧
    !qqAllsDef y im 2”

instance ve2_defined : 𝚺ᴬ₁-Function₄ (ve2 : V → V → V → V → V) via ve2Def := .mk fun v ↦ by
  simp [ve2Def, ve2]

noncomputable def iVE.blueprint : Language.TermRec.Blueprint 1 where
  bvar := .mkSigma “y z n. ∃ b, !qqBvarDef b (z + 1) ∧ !eqAtomDef y b”
  fvar := .mkSigma “y x n. ∃ b, !qqFvarDef b x ∧ !eqAtomDef y b”
  func := .mkSigma “y k f v w n. (k = 0 ∧ !ve0Def y k f) ∨ (k ≠ 0 ∧ !ve2Def y n k f w)”

noncomputable def iVE.construction : Language.TermRec.Construction V iVE.blueprint where
  bvar := fun _ z ↦ eqAtom (^#(z + 1))
  fvar := fun _ x ↦ eqAtom (^&x)
  func := fun p k f _ w ↦ if k = 0 then ve0 k f else ve2 (p 0) k f w
  bvar_defined := .mk fun v ↦ by simp [iVE.blueprint]
  fvar_defined := .mk fun v ↦ by simp [iVE.blueprint]
  func_defined := .mk fun v ↦ by
    by_cases hk : v 1 = 0 <;> simp [iVE.blueprint, hk]

/-- **内部变量等式**：`iVE n ⌜t⌝` 是 `varEqual t`（层数 n）的编码。 -/
noncomputable def iVE (n t : V) : V := iVE.construction.result ℒₒᵣ ![n] t

end iVE

noncomputable def iVEDef : 𝚺ᴬ₁.Semisentence 3 :=
  (iVE.blueprint.result ℒₒᵣ).rew (Rew.subst ![#0, #2, #1])

instance iVE_defined : 𝚺ᴬ₁-Function₂ (iVE : V → V → V) via iVEDef := .mk fun v ↦ by
  simp [iVEDef, iVE, iVE.construction.result_graphDef]; rfl

/-! ## 内部原子翻译 `iTR n k R v` 与内部翻译 `iT n p` -/

section iT

/-- 关系符号翻译公式的编码（V 中）。 -/
noncomputable def cRel (R : V) : V := if R = 0 then ((cRelN 0 : ℕ) : V) else ((cRelN 1 : ℕ) : V)

noncomputable def cRelDef : 𝚺ᴬ₁.Semisentence 2 := .mkSigma
  “y R. (R = 0 ∧ y = ↑(cRelN 0)) ∨ (R ≠ 0 ∧ y = ↑(cRelN 1))”

instance cRel_defined : 𝚺ᴬ₁-Function₁ (cRel : V → V) via cRelDef := .mk fun v ↦ by
  simp only [cRelDef, cRel]
  by_cases hR : v 1 = 0 <;> simp [hR, numeral_eq_natCast]

/-- 原子 `R(v₀, v₁)` 的翻译：`∀∀ ((A₀ ⋏ (A₁ ⋏ ⊤)) 🡒 R'(#0, #1))`。 -/
noncomputable def iTR (n _k R v : V) : V :=
  qqAlls (imp ℒₛₑₜ (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤))
    (subst ℒₛₑₜ ?[^#0, ^#1] (cRel R))) 2

noncomputable def iTRDef : 𝚺ᴬ₁.Semisentence 5 := .mkSigma
  “y n k R v. ∃ v0, !nthDef v0 v 0 ∧ ∃ v1, !nthDef v1 v 1 ∧ ∃ e0, !iVEDef e0 n v0 ∧
    ∃ e1, !iVEDef e1 n v1 ∧ ∃ a0, !conjunctDef a0 2 n 0 e0 ∧ ∃ a1, !conjunctDef a1 2 n 1 e1 ∧
    ∃ t, !qqVerumDef t ∧ ∃ c1, !qqAndDef c1 a1 t ∧ ∃ c0, !qqAndDef c0 a0 c1 ∧
    ∃ c, !cRelDef c R ∧ ∃ b0, !qqBvarDef b0 0 ∧ ∃ b1, !qqBvarDef b1 1 ∧ ∃ v2, !mkVec₂Def v2 b0 b1 ∧
    ∃ s, !(substsGraph ℒₛₑₜ) s v2 c ∧ ∃ im, !(impGraph ℒₛₑₜ) im c0 s ∧ !qqAllsDef y im 2”

instance iTR_defined : 𝚺ᴬ₁-Function₄ (iTR : V → V → V → V → V) via iTRDef := .mk fun v ↦ by
  simp [iTRDef, iTR]

attribute [irreducible] shiftVecDef eqAtomDef cFuncDef conjunctDef ve0Def ve2Def iVEDef cRelDef iTRDef

/-- 定义域限制 `domain/[#0]` 的编码。 -/
noncomputable def domZero : V := subst ℒₛₑₜ ?[^#0] (cDomN : V)

noncomputable def iT.blueprint : UformulaRec1.Blueprint where
  rel := iTRDef
  nrel := .mkSigma “y n k R v. ∃ y', !iTRDef y' n k R v ∧ !(negGraph ℒₛₑₜ) y y'”
  verum := .mkSigma “y n. !qqVerumDef y”
  falsum := .mkSigma “y n. !qqFalsumDef y”
  and := .mkSigma “y n p₁ p₂ y₁ y₂. !qqAndDef y y₁ y₂”
  or := .mkSigma “y n p₁ p₂ y₁ y₂. !qqOrDef y y₁ y₂”
  all := .mkSigma “y n p₁ ys. ∃ y₁, !nthDef y₁ ys 0 ∧ ∃ b, !qqBvarDef b 0 ∧ ∃ v1, !mkVec₁Def v1 b ∧
    ∃ d, !(substsGraph ℒₛₑₜ) d v1 ↑cDomN ∧ ∃ im, !(impGraph ℒₛₑₜ) im d y₁ ∧ !qqAllDef y im”
  exs := .mkSigma “y n p₁ ys. ∃ y₁, !nthDef y₁ ys 0 ∧ ∃ b, !qqBvarDef b 0 ∧ ∃ v1, !mkVec₁Def v1 b ∧
    ∃ d, !(substsGraph ℒₛₑₜ) d v1 ↑cDomN ∧ ∃ c, !qqAndDef c d y₁ ∧ !qqExsDef y c”
  allChanges := .mkSigma “n' n i. n' = n + 1”
  exsChanges := .mkSigma “n' n i. n' = n + 1”

noncomputable def iT.construction : UformulaRec1.Construction V iT.blueprint where
  rel n k R v := iTR n k R v
  nrel n k R v := neg ℒₛₑₜ (iTR n k R v)
  verum _ := ^⊤
  falsum _ := ^⊥
  and _ _ _ y₁ y₂ := y₁ ^⋏ y₂
  or _ _ _ y₁ y₂ := y₁ ^⋎ y₂
  all _ _ ys := ^∀ (imp ℒₛₑₜ domZero ys.[0])
  exs _ _ ys := ^∃ (domZero ^⋏ ys.[0])
  allChanges n _ := n + 1
  exsChanges n _ := n + 1
  rel_defined := iTR_defined
  nrel_defined := .mk fun v ↦ by simp [iT.blueprint]
  verum_defined := .mk fun v ↦ by simp [iT.blueprint]
  falsum_defined := .mk fun v ↦ by simp [iT.blueprint]
  and_defined := .mk fun v ↦ by simp [iT.blueprint]
  or_defined := .mk fun v ↦ by simp [iT.blueprint]
  all_defined := .mk fun v ↦ by simp [iT.blueprint, domZero, numeral_eq_natCast]
  exs_defined := .mk fun v ↦ by simp [iT.blueprint, domZero, numeral_eq_natCast]
  allChanges_defined := .mk fun v ↦ by simp [iT.blueprint]
  exChanges_defined := .mk fun v ↦ by simp [iT.blueprint]
  allChanges_monotone := fun _ ↦ le_rfl
  exsChanges_monotone := fun _ ↦ le_rfl

/-- **内部翻译**：`iT n ⌜φ⌝` 是 `arithTrln.translate φ`（层数 n）的编码。 -/
noncomputable def iT (n p : V) : V := iT.construction.result ℒₒᵣ n p

noncomputable def iTDef : 𝚺ᴬ₁.Semisentence 3 := iT.blueprint.result ℒₒᵣ

instance iT_defined : 𝚺ᴬ₁-Function₂ (iT : V → V → V) via iTDef :=
  iT.construction.result_defined

instance iT_definable : 𝚺ᴬ₁-Function₂ (iT : V → V → V) := iT_defined.to_definable

end iT

/-! ## 正确性：内部翻译等于翻译的编码 -/

section correctness

/-- `bvs c n = [^#c, ^#(c+1), …, ^#(c+n-1)]`（标准的 n）。 -/
noncomputable def bvs (c : V) (n : ℕ) : V := matrixToVec (fun j : Fin n ↦ (^#(c + (j : V)) : V))

@[simp] lemma bvs_zero (c : V) : bvs c 0 = 0 := rfl

lemma bvs_succ (c : V) (n : ℕ) : bvs c (n + 1) = ^#c ∷ bvs (c + 1) n := by
  simp only [bvs, matrixToVec_succ]
  congr 1
  · simp [Matrix.vecHead]
  · congr 1
    funext j
    simp only [Matrix.vecTail, Function.comp_apply, Fin.val_succ, Nat.cast_add, Nat.cast_one]
    congr 1
    ring

lemma isUTermVec_bvs (c : V) : ∀ n : ℕ, IsUTermVec ℒₛₑₜ (n : V) (bvs c n)
  | 0 => by simp
  | n + 1 => by
    rw [bvs_succ, Nat.cast_succ]
    exact (isUTermVec_bvs (c + 1) n).adjoin (by simp)

lemma termBShiftVec_bvs (c : V) : ∀ n : ℕ, termBShiftVec ℒₛₑₜ (n : V) (bvs c n) = bvs (c + 1) n
  | 0 => by simp
  | n + 1 => by
    rw [bvs_succ, bvs_succ, Nat.cast_succ,
      termBShiftVec_cons (by simp) (isUTermVec_bvs (c + 1) n), termBShift_bvar,
      termBShiftVec_bvs (c + 1) n]

lemma shiftVec_nat (b : V) : ∀ n : ℕ, shiftVec b (n : V) = bvs b n
  | 0 => by simp
  | n + 1 => by
    rw [Nat.cast_succ, shiftVec_succ, shiftVec_nat b n, termBShiftVec_bvs, bvs_succ]

variable {L : Language} [L.Encodable] [L.LORDefinable]

lemma quote_imp' {n : ℕ} (A B : Semisentence L n) : (⌜A 🡒 B⌝ : V) = imp L ⌜A⌝ ⌜B⌝ := by
  simp [Sentence.quote_eq]

lemma quote_neg' {n : ℕ} (A : Semisentence L n) : (⌜∼A⌝ : V) = neg L ⌜A⌝ := by
  simp [Sentence.quote_eq]

lemma quote_allItr' {n : ℕ} : ∀ (k : ℕ) (A : Semisentence L (n + k)),
    (⌜∀¹^[k] A⌝ : V) = qqAlls ⌜A⌝ (k : V)
  | 0, A => by simp
  | k + 1, A => by
    rw [allItr_succ, quote_allItr' k (∀¹ A), Sentence.quote_all, Nat.cast_succ, qqAlls_succ']

lemma quote_substs' {k m : ℕ} (σ : Semisentence L k) (w : Fin k → ClosedSemiterm L m) :
    (⌜σ ⇜ w⌝ : V) = subst L (SemitermVec.val fun i ↦ (⌜w i⌝ : Bootstrapping.Semiterm V L m)) ⌜σ⌝ := by
  rw [Sentence.quote_def, Rewriting.emb_subst_eq_subst_emb, Semiformula.quote_def,
    Semiformula.typed_quote_substs, Bootstrapping.Semiformula.val_substs]
  rfl

omit [L.Encodable] [L.LORDefinable] in
lemma embSubsts_app {k m : ℕ} (σ : Semisentence L k) (w : Fin k → ClosedSemiterm L m) :
    Rewriting.app (Rew.embSubsts w) σ = σ ⇜ w := by
  have : (Rew.embSubsts w : Rew L Empty k Empty m) = Rew.subst w := by
    ext x
    · simp
    · exact Empty.elim x
  rw [this]

omit [L.Encodable] [L.LORDefinable] in
lemma emb_app_self {n : ℕ} (σ : Semisentence L n) :
    Rewriting.app (Rew.emb : Rew L Empty n Empty n) σ = σ := by
  simp [Rew.emb_eq_id]

omit [L.Encodable] [L.LORDefinable] in
lemma quote_eqBvars {m : ℕ} (a b : Fin m) :
    (⌜(“#a = #b” : Semisentence ℒₛₑₜ m)⌝ : V) = ^rel 2 (cEqN : V) (^#(a : V) ∷ ^#(b : V) ∷ 0) := rfl

lemma iVE_quote_bvar {n : ℕ} (x : Fin n) :
    iVE (n : V) ⌜(#x : ClosedSemiterm ℒₒᵣ n)⌝ =
      ⌜(arithTrln.varEqual (#x : ClosedSemiterm ℒₒᵣ n) : Semisentence ℒₛₑₜ (n + 1))⌝ := by
  simp only [DirectTranslation.varEqual]
  rw [quote_eqBvars]
  simp [iVE, iVE.construction, eqAtom]

lemma closedVec_val {n k : ℕ} (v : Fin k → ClosedSemiterm ℒₒᵣ n) :
    (SemitermVec.val fun i ↦ (⌜v i⌝ : Bootstrapping.Semiterm V ℒₒᵣ n)) = matrixToVec fun i ↦ (⌜v i⌝ : V) := rfl

lemma quote_func_eq {n k : ℕ} (f : (ℒₒᵣ).Func k) (v : Fin k → ClosedSemiterm ℒₒᵣ n) :
    (⌜(Semiterm.func f v : ClosedSemiterm ℒₒᵣ n)⌝ : V) =
      ^func (k : V) ⌜f⌝ (matrixToVec fun i ↦ (⌜v i⌝ : V)) := rfl

lemma iVE_func_lhs2 {n : ℕ} (f : (ℒₒᵣ).Func 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n) :
    iVE (n : V) ⌜(Semiterm.func f v : ClosedSemiterm ℒₒᵣ n)⌝ =
      ve2 (n : V) 2 ⌜f⌝ ?[iVE (n : V) ⌜v 0⌝, iVE (n : V) ⌜v 1⌝] := by
  have hu := Semiterm.empty_quote_isUTerm (V := V) (Semiterm.func f v : ClosedSemiterm ℒₒᵣ n)
  rw [quote_func_eq] at hu ⊢
  simp only [Nat.cast_ofNat] at hu ⊢
  obtain ⟨hf, hv⟩ := IsUTerm.func_iff.mp hu
  rw [iVE, iVE.construction.result_func' hf hv]
  have h0 : (iVE.construction.resultVec ℒₒᵣ ![(n : V)] 2 (matrixToVec fun i ↦ (⌜v i⌝ : V))).[0] =
      iVE (n : V) ⌜v 0⌝ := by
    rw [iVE.construction.nth_resultVec ℒₒᵣ ![(n : V)] hv (by simp)]
    simp [iVE]; rfl
  have h1 : (iVE.construction.resultVec ℒₒᵣ ![(n : V)] 2 (matrixToVec fun i ↦ (⌜v i⌝ : V))).[1] =
      iVE (n : V) ⌜v 1⌝ := by
    rw [iVE.construction.nth_resultVec ℒₒᵣ ![(n : V)] hv (by simp)]
    simp [iVE]; rfl
  generalize iVE.construction.resultVec ℒₒᵣ ![(n : V)] 2 (matrixToVec fun i ↦ (⌜v i⌝ : V)) = W at h0 h1 ⊢
  simp only [iVE.construction, Matrix.cons_val_zero, two_ne_zero, ite_false]
  simp only [ve2, h0, h1]
  simp

omit [L.Encodable] [L.LORDefinable] in
lemma matrix_conj_two {n : ℕ} (A : Fin 2 → Semisentence L n) : Matrix.conj A = A 0 ⋏ (A 1 ⋏ ⊤) := rfl

omit [L.Encodable] [L.LORDefinable] in
lemma matrix_conj_zero {n : ℕ} (A : Fin 0 → Semisentence L n) : Matrix.conj A = ⊤ := rfl

lemma closedVec_val' {m k : ℕ} (w : Fin k → ClosedSemiterm L m) :
    (SemitermVec.val fun i ↦ (⌜w i⌝ : Bootstrapping.Semiterm V L m)) = matrixToVec fun i ↦ (⌜w i⌝ : V) := rfl

lemma cDomN_eq : ((cDomN : ℕ) : V) = ⌜(arithTrln.domain : Semisentence ℒₛₑₜ 1)⌝ :=
  Sentence.coe_quote_eq_quote _

lemma bvs_eq_fun (c : ℕ) (n : ℕ) (g : Fin n → ℕ) (hg : ∀ j, g j = c + j) :
    matrixToVec (fun j : Fin n ↦ (^#((g j : ℕ) : V) : V)) = shiftVec (c : V) (n : V) := by
  rw [shiftVec_nat, bvs]
  congr 1
  funext j
  rw [hg j]
  push_cast
  rfl

omit [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] [L.Encodable] [L.LORDefinable] in
@[simp] lemma val_addCast' {n : ℕ} (m : ℕ) (i : Fin n) : ((Fin.addCast m i : Fin (m + n)) : ℕ) = i := rfl

lemma val_vec_shift {n m : ℕ} (c : ℕ) (a : Fin m) (g : Fin n → Fin m) (hg : ∀ j, (g j : ℕ) = c + j) :
    (SemitermVec.val fun i ↦
        (⌜((#a :> fun j ↦ #(g j)) : Fin (n + 1) → ClosedSemiterm L m) i⌝ : Bootstrapping.Semiterm V L m)) =
      ^#((a : ℕ) : V) ∷ shiftVec (c : V) (n : V) := by
  rw [closedVec_val', matrixToVec_succ, ← bvs_eq_fun c n (fun j ↦ (g j : ℕ)) hg]
  rfl

lemma val_vec_one {m : ℕ} (a : Fin m) :
    (SemitermVec.val fun i ↦ (⌜(![#a] : Fin 1 → ClosedSemiterm L m) i⌝ : Bootstrapping.Semiterm V L m)) =
      ^#((a : ℕ) : V) ∷ 0 := rfl

lemma val_vec_three {m : ℕ} (a b c : Fin m) :
    (SemitermVec.val fun i ↦ (⌜((#a :> ![#b, #c]) : Fin 3 → ClosedSemiterm L m) i⌝ : Bootstrapping.Semiterm V L m)) =
      ^#((a : ℕ) : V) ∷ ^#((b : ℕ) : V) ∷ ^#((c : ℕ) : V) ∷ 0 := rfl

lemma varEqual_rhs2 {n : ℕ} (f : (ℒₒᵣ).Func 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n) :
    (⌜(arithTrln.varEqual (Semiterm.func f v) : Semisentence ℒₛₑₜ (n + 1))⌝ : V) =
      qqAlls (imp ℒₛₑₜ
        (conjunct 3 (n : V) 0 ⌜(arithTrln.varEqual (v 0) : Semisentence ℒₛₑₜ (n + 1))⌝ ^⋏
          (conjunct 3 (n : V) 1 ⌜(arithTrln.varEqual (v 1) : Semisentence ℒₛₑₜ (n + 1))⌝ ^⋏ ^⊤))
        (subst ℒₛₑₜ (^#2 ∷ ?[^#0, ^#1]) ⌜(arithTrln.func f : Semisentence ℒₛₑₜ 3)⌝)) 2 := by
  rw [DirectTranslation.varEqual, quote_allItr', quote_imp', matrix_conj_two]
  simp only [Sentence.quote_and, emb_app_self, embSubsts_app, Nat.cast_ofNat]
  rw [show ∀ {k m : ℕ} (σ : Semisentence ℒₛₑₜ k) (w : Fin k → ClosedSemiterm ℒₛₑₜ m),
      Rewriting.app (Rew.subst w) σ = σ ⇜ w from fun _ _ ↦ rfl]
  simp only [quote_substs']
  rw [val_vec_shift 3 _ _ (fun j ↦ by simp; omega), val_vec_shift 3 _ _ (fun j ↦ by simp; omega),
    val_vec_one, val_vec_one]
  simp only [closedVec_val', matrixToVec_succ, matrixToVec_nil, Matrix.vecHead, Matrix.vecTail,
    Matrix.cons_val_zero, Matrix.cons_val_succ, Function.comp_apply, Semiterm.empty_quote_bvar,
    Sentence.quote_verum, conjunct, cDomN_eq, val_addCast', Fin.val_addNat, Nat.cast_ofNat]
  simp

lemma cFunc_quote2 (f : (ℒₒᵣ).Func 2) :
    cFunc (2 : V) ⌜f⌝ = ⌜(arithTrln.func f : Semisentence ℒₛₑₜ 3)⌝ := by
  cases f
  · show cFunc (2 : V) ((Encodable.encode (Language.ORing.Func.add : (ℒₒᵣ).Func 2) : ℕ) : V) = _
    have h : Encodable.encode (Language.ORing.Func.add : (ℒₒᵣ).Func 2) = 0 := rfl
    simp [cFunc, cFuncN, Sentence.coe_quote_eq_quote, h]
  · show cFunc (2 : V) ((Encodable.encode (Language.ORing.Func.mul : (ℒₒᵣ).Func 2) : ℕ) : V) = _
    have h : Encodable.encode (Language.ORing.Func.mul : (ℒₒᵣ).Func 2) = 1 := rfl
    simp [cFunc, cFuncN, Sentence.coe_quote_eq_quote, h]

lemma iVE_quote2 {n : ℕ} (f : (ℒₒᵣ).Func 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n)
    (h0 : iVE (n : V) ⌜v 0⌝ = ⌜(arithTrln.varEqual (v 0) : Semisentence ℒₛₑₜ (n + 1))⌝)
    (h1 : iVE (n : V) ⌜v 1⌝ = ⌜(arithTrln.varEqual (v 1) : Semisentence ℒₛₑₜ (n + 1))⌝) :
    iVE (n : V) ⌜(Semiterm.func f v : ClosedSemiterm ℒₒᵣ n)⌝ =
      ⌜(arithTrln.varEqual (Semiterm.func f v) : Semisentence ℒₛₑₜ (n + 1))⌝ := by
  rw [iVE_func_lhs2, varEqual_rhs2, h0, h1, ← cFunc_quote2]
  simp [ve2]

lemma cFunc_quote0 (f : (ℒₒᵣ).Func 0) :
    cFunc (0 : V) ⌜f⌝ = ⌜(arithTrln.func f : Semisentence ℒₛₑₜ 1)⌝ := by
  cases f
  · show cFunc (0 : V) ((Encodable.encode (Language.ORing.Func.zero : (ℒₒᵣ).Func 0) : ℕ) : V) = _
    have h : Encodable.encode (Language.ORing.Func.zero : (ℒₒᵣ).Func 0) = 0 := rfl
    simp [cFunc, cFuncN, Sentence.coe_quote_eq_quote, h]
  · show cFunc (0 : V) ((Encodable.encode (Language.ORing.Func.one : (ℒₒᵣ).Func 0) : ℕ) : V) = _
    have h : Encodable.encode (Language.ORing.Func.one : (ℒₒᵣ).Func 0) = 1 := rfl
    simp [cFunc, cFuncN, Sentence.coe_quote_eq_quote, h]

lemma iVE_quote0 {n : ℕ} (f : (ℒₒᵣ).Func 0) (v : Fin 0 → ClosedSemiterm ℒₒᵣ n) :
    iVE (n : V) ⌜(Semiterm.func f v : ClosedSemiterm ℒₒᵣ n)⌝ =
      ⌜(arithTrln.varEqual (Semiterm.func f v) : Semisentence ℒₛₑₜ (n + 1))⌝ := by
  have hu := Semiterm.empty_quote_isUTerm (V := V) (Semiterm.func f v : ClosedSemiterm ℒₒᵣ n)
  rw [quote_func_eq] at hu ⊢
  simp only [Nat.cast_zero] at hu ⊢
  obtain ⟨hf, hv⟩ := IsUTerm.func_iff.mp hu
  rw [iVE, iVE.construction.result_func' hf hv]
  simp only [iVE.construction, ite_true, ve0]
  rw [DirectTranslation.varEqual, allItr_zero, quote_imp', matrix_conj_zero, Sentence.quote_verum, embSubsts_app,
    quote_substs']
  simp only [closedVec_val', matrixToVec_succ, matrixToVec_nil, Matrix.vecHead, Matrix.cons_val_zero,
    Semiterm.empty_quote_bvar, Fin.val_addNat]
  rw [cFunc_quote0]
  simp

/-- **内部变量等式的正确性**：对每个闭项 t（层数 n），`iVE n ⌜t⌝ = ⌜varEqual t⌝`。 -/
theorem iVE_quote {n : ℕ} : ∀ t : ClosedSemiterm ℒₒᵣ n,
    iVE (n : V) ⌜t⌝ = ⌜(arithTrln.varEqual t : Semisentence ℒₛₑₜ (n + 1))⌝
  | #x => iVE_quote_bvar x
  | &x => x.elim
  | FFL.FirstOrder.Semiterm.func Language.ORing.Func.zero v => iVE_quote0 _ v
  | FFL.FirstOrder.Semiterm.func Language.ORing.Func.one v => iVE_quote0 _ v
  | FFL.FirstOrder.Semiterm.func Language.ORing.Func.add v => iVE_quote2 _ v (iVE_quote (v 0)) (iVE_quote (v 1))
  | FFL.FirstOrder.Semiterm.func Language.ORing.Func.mul v => iVE_quote2 _ v (iVE_quote (v 0)) (iVE_quote (v 1))

/-! ### 原子公式 -/

lemma quote_rel_sent {n k : ℕ} (R : (ℒₒᵣ).Rel k) (v : Fin k → ClosedSemiterm ℒₒᵣ n) :
    (⌜(FFL.FirstOrder.Semiformula.rel R v : Semisentence ℒₒᵣ n)⌝ : V) =
      ^rel (k : V) ⌜R⌝ (matrixToVec fun i ↦ (⌜v i⌝ : V)) := rfl

lemma quote_nrel_sent {n k : ℕ} (R : (ℒₒᵣ).Rel k) (v : Fin k → ClosedSemiterm ℒₒᵣ n) :
    (⌜(FFL.FirstOrder.Semiformula.nrel R v : Semisentence ℒₒᵣ n)⌝ : V) =
      ^nrel (k : V) ⌜R⌝ (matrixToVec fun i ↦ (⌜v i⌝ : V)) := rfl

lemma translateRel_quote2 {n : ℕ} (R : (ℒₒᵣ).Rel 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n) :
    (⌜(arithTrln.translateRel R v : Semisentence ℒₛₑₜ n)⌝ : V) =
      qqAlls (imp ℒₛₑₜ
        (conjunct 2 (n : V) 0 ⌜(arithTrln.varEqual (v 0) : Semisentence ℒₛₑₜ (n + 1))⌝ ^⋏
          (conjunct 2 (n : V) 1 ⌜(arithTrln.varEqual (v 1) : Semisentence ℒₛₑₜ (n + 1))⌝ ^⋏ ^⊤))
        (subst ℒₛₑₜ ?[^#0, ^#1] ⌜(arithTrln.rel R : Semisentence ℒₛₑₜ 2)⌝)) 2 := by
  rw [DirectTranslation.translateRel, quote_allItr', quote_imp', matrix_conj_two]
  simp only [Sentence.quote_and, emb_app_self, embSubsts_app, Nat.cast_ofNat]
  rw [show ∀ {k m : ℕ} (σ : Semisentence ℒₛₑₜ k) (w : Fin k → ClosedSemiterm ℒₛₑₜ m),
      Rewriting.app (Rew.subst w) σ = σ ⇜ w from fun _ _ ↦ rfl]
  simp only [quote_substs']
  rw [val_vec_shift 2 _ _ (fun j ↦ by simp; omega), val_vec_shift 2 _ _ (fun j ↦ by simp; omega),
    val_vec_one, val_vec_one]
  simp only [closedVec_val', matrixToVec_succ, matrixToVec_nil, Matrix.vecHead, Matrix.vecTail,
    Function.comp_apply, Semiterm.empty_quote_bvar, Sentence.quote_verum, conjunct, cDomN_eq,
    val_addCast', Nat.cast_ofNat]
  simp

lemma cRel_quote (R : (ℒₒᵣ).Rel 2) :
    cRel (⌜R⌝ : V) = ⌜(arithTrln.rel R : Semisentence ℒₛₑₜ 2)⌝ := by
  cases R
  · show cRel ((Encodable.encode (Language.ORing.Rel.eq : (ℒₒᵣ).Rel 2) : ℕ) : V) = _
    have h : Encodable.encode (Language.ORing.Rel.eq : (ℒₒᵣ).Rel 2) = 0 := rfl
    simp [cRel, cRelN, Sentence.coe_quote_eq_quote, h]
  · show cRel ((Encodable.encode (Language.ORing.Rel.lt : (ℒₒᵣ).Rel 2) : ℕ) : V) = _
    have h : Encodable.encode (Language.ORing.Rel.lt : (ℒₒᵣ).Rel 2) = 1 := rfl
    simp [cRel, cRelN, Sentence.coe_quote_eq_quote, h]

/-- **内部原子翻译的正确性**。 -/
lemma iTR_quote {n : ℕ} (R : (ℒₒᵣ).Rel 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n) :
    iTR (n : V) 2 ⌜R⌝ (matrixToVec fun i ↦ (⌜v i⌝ : V)) =
      ⌜(arithTrln.translateRel R v : Semisentence ℒₛₑₜ n)⌝ := by
  have e0 : (matrixToVec fun i ↦ (⌜v i⌝ : V)).[0] = ⌜v 0⌝ := by
    simpa using matrixToVec_nth (fun i ↦ (⌜v i⌝ : V)) 0
  have e1 : (matrixToVec fun i ↦ (⌜v i⌝ : V)).[1] = ⌜v 1⌝ := by
    simpa using matrixToVec_nth (fun i ↦ (⌜v i⌝ : V)) 1
  rw [translateRel_quote2, iTR, e0, e1, iVE_quote, iVE_quote, cRel_quote]

/-! ### 内部翻译沿公式结构的计算规则 -/

lemma iT_rel {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    iT n (^rel k R v) = iTR n k R v := by
  rw [iT, iT.construction.result_rel hR hv]; rfl

lemma iT_nrel {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    iT n (^nrel k R v) = neg ℒₛₑₜ (iTR n k R v) := by
  rw [iT, iT.construction.result_nrel hR hv]; rfl

lemma iT_verum (n : V) : iT n ^⊤ = ^⊤ := by
  rw [iT, iT.construction.result_verum]; rfl

lemma iT_falsum (n : V) : iT n ^⊥ = ^⊥ := by
  rw [iT, iT.construction.result_falsum]; rfl

lemma iT_and {n p q : V} (hp : IsUFormula ℒₒᵣ p) (hq : IsUFormula ℒₒᵣ q) :
    iT n (p ^⋏ q) = iT n p ^⋏ iT n q := by
  rw [iT, iT.construction.result_and hp hq]; rfl

lemma iT_or {n p q : V} (hp : IsUFormula ℒₒᵣ p) (hq : IsUFormula ℒₒᵣ q) :
    iT n (p ^⋎ q) = iT n p ^⋎ iT n q := by
  rw [iT, iT.construction.result_or hp hq]; rfl

lemma iT_all {n p : V} (hp : IsUFormula ℒₒᵣ p) :
    iT n (^∀ p) = ^∀ (imp ℒₛₑₜ domZero (iT (n + 1) p)) := by
  rw [iT, iT.construction.result_all hp rfl]
  show ^∀ (imp ℒₛₑₜ domZero (?[iT (n + 1) p]).[0]) = _
  simp

lemma iT_exs {n p : V} (hp : IsUFormula ℒₒᵣ p) :
    iT n (^∃ p) = ^∃ (domZero ^⋏ iT (n + 1) p) := by
  rw [iT, iT.construction.result_exs hp rfl]
  show ^∃ (domZero ^⋏ (?[iT (n + 1) p]).[0]) = _
  simp

/-! ### 带定义域限制的量词 -/

lemma quote_domain_zero {n : ℕ} :
    (⌜(Rewriting.app (Rew.emb : Rew ℒₛₑₜ Empty (n + 1) Empty (n + 1))
        (arithTrln.domain/[#0]) : Semisentence ℒₛₑₜ (n + 1))⌝ : V) = domZero := by
  rw [emb_app_self, quote_substs', val_vec_one]
  simp [domZero, cDomN_eq]

lemma quote_fal {n : ℕ} (φ : Semisentence ℒₛₑₜ (n + 1)) :
    (⌜(DirectTranslation.fal arithTrln φ : Semisentence ℒₛₑₜ n)⌝ : V) =
      ^∀ (imp ℒₛₑₜ domZero ⌜φ⌝) := by
  rw [DirectTranslation.fal, FFL.FirstOrder.ball, Sentence.quote_all, quote_imp', quote_domain_zero]

lemma quote_exs {n : ℕ} (φ : Semisentence ℒₛₑₜ (n + 1)) :
    (⌜(DirectTranslation.exs arithTrln φ : Semisentence ℒₛₑₜ n)⌝ : V) =
      ^∃ (domZero ^⋏ ⌜φ⌝) := by
  rw [DirectTranslation.exs, FFL.FirstOrder.bexs, Sentence.quote_ex, Sentence.quote_and, quote_domain_zero]

/-! ### 公式归纳 -/

lemma iT_quote_rel {n : ℕ} (R : (ℒₒᵣ).Rel 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n) :
    iT (n : V) ⌜(FFL.FirstOrder.Semiformula.rel R v : Semisentence ℒₒᵣ n)⌝ =
      ⌜(arithTrln.translate (FFL.FirstOrder.Semiformula.rel R v) : Semisentence ℒₛₑₜ n)⌝ := by
  have hu := Sentence.quote_isUFormula (V := V) (FFL.FirstOrder.Semiformula.rel R v : Semisentence ℒₒᵣ n)
  rw [quote_rel_sent] at hu ⊢
  simp only [Nat.cast_ofNat] at hu ⊢
  obtain ⟨hR, hv⟩ := IsUFormula.rel.mp hu
  rw [iT_rel hR hv, iTR_quote, DirectTranslation.translate_rel]

lemma iT_quote_nrel {n : ℕ} (R : (ℒₒᵣ).Rel 2) (v : Fin 2 → ClosedSemiterm ℒₒᵣ n) :
    iT (n : V) ⌜(FFL.FirstOrder.Semiformula.nrel R v : Semisentence ℒₒᵣ n)⌝ =
      ⌜(arithTrln.translate (FFL.FirstOrder.Semiformula.nrel R v) : Semisentence ℒₛₑₜ n)⌝ := by
  have hu := Sentence.quote_isUFormula (V := V) (FFL.FirstOrder.Semiformula.nrel R v : Semisentence ℒₒᵣ n)
  rw [quote_nrel_sent] at hu ⊢
  simp only [Nat.cast_ofNat] at hu ⊢
  obtain ⟨hR, hv⟩ := IsUFormula.nrel.mp hu
  rw [iT_nrel hR hv, iTR_quote, DirectTranslation.translate_nrel, quote_neg']

/-- **内部翻译的正确性**：对每个算术公式 φ（层数 n），`iT n ⌜φ⌝ = ⌜arithTrln.translate φ⌝`。 -/
theorem iT_quote : ∀ {n : ℕ} (φ : Semisentence ℒₒᵣ n),
    iT (n : V) ⌜φ⌝ = ⌜(arithTrln.translate φ : Semisentence ℒₛₑₜ n)⌝
  | _, FFL.FirstOrder.Semiformula.rel Language.ORing.Rel.eq v => iT_quote_rel _ v
  | _, FFL.FirstOrder.Semiformula.rel Language.ORing.Rel.lt v => iT_quote_rel _ v
  | _, FFL.FirstOrder.Semiformula.nrel Language.ORing.Rel.eq v => iT_quote_nrel _ v
  | _, FFL.FirstOrder.Semiformula.nrel Language.ORing.Rel.lt v => iT_quote_nrel _ v
  | _, ⊤ => by
    rw [Sentence.quote_verum, iT_verum, LogicalConnective.HomClass.map_top, Sentence.quote_verum]
  | _, ⊥ => by
    rw [Sentence.quote_falsum, iT_falsum, LogicalConnective.HomClass.map_bot, Sentence.quote_falsum]
  | _, φ ⋏ ψ => by
    rw [Sentence.quote_and, iT_and (Sentence.quote_isUFormula φ) (Sentence.quote_isUFormula ψ),
      iT_quote φ, iT_quote ψ, LogicalConnective.HomClass.map_and, Sentence.quote_and]
  | _, φ ⋎ ψ => by
    rw [Sentence.quote_or, iT_or (Sentence.quote_isUFormula φ) (Sentence.quote_isUFormula ψ),
      iT_quote φ, iT_quote ψ, LogicalConnective.HomClass.map_or, Sentence.quote_or]
  | _, ∀¹ φ => by
    rw [Sentence.quote_all, iT_all (Sentence.quote_isUFormula φ), ← Nat.cast_succ, iT_quote φ,
      DirectTranslation.translate_all, quote_fal]
  | _, ∃¹ φ => by
    rw [Sentence.quote_ex, iT_exs (Sentence.quote_isUFormula φ), ← Nat.cast_succ, iT_quote φ,
      DirectTranslation.translate_ex, quote_exs]

end correctness


end GodelQ.Translate
