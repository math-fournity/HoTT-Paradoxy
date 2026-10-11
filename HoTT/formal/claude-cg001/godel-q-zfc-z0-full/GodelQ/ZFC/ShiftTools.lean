import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（十二）：`shift` 的两个枢纽工具

`hAll` / `hShift` 需要 `iT` 与 `shift` 的相容律。其量词支与原子支都要处理
`shift` 作用在**引号化公式**上的情形——而这类公式的自由变量域是 `Empty`
（`Semisentence L n = Semiformula L Empty n`），`Rewriting.shift` 对它们恒等。

本文件给出两个工具：

* `rew_shift_emb`：`Rewriting.shift` 固定 `emb σ`（`Semisentence` 的 `Semiproposition` 嵌入）。
* `shift_quote`：**V 层**——`shift ℒₛₑₜ (⌜φ⌝ : V) = ⌜φ⌝`，对任意 `Semisentence ℒₛₑₜ n`。
* `shift_domZero`：**枢纽**——`shift domZero = domZero`。
  `iT` 给每个量词多引一个 `domZero`，`shift` 不引；这个错位恰好被此式抹平。

## 来源

这三条由并行工位（`elegant-mclaren-767fb0`，CG-009）在 2026-10-11 证出，
本 worktree 独立重编译核验后吸收（exit 0、公理仅三条标准公理）。
原文件：`docs/形式化综合研判-20261011/成果-IShiftDomZero/{ShiftDomZero,ShiftQuote}.lean`。
本文件去掉对 `GateBranches` 的依赖，使它在 CG-007 W8 的包内自足。

## 证明要点

`Semisentence L n = Semiformula L Empty n`（自由变量域是 `Empty`）
⇒ `Semiformula.fvSup_sentence` 给 `fvSup (emb σ) = 0`
⇒ `Semiformula.rew_eq_self_of` 配 `Semiformula.lt_fvSup_of_fvar?` 排除任何 fvar
⇒ `Rewriting.shift` 恒等 ⇒ 经 `Semiformula.quote_shift` 与 `Sentence.quote_def` 下到 V 层。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShiftTools

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `Rewriting.shift` 固定 `emb σ`：`Semisentence` 经 `emb` 嵌入后没有自由变量。 -/
lemma rew_shift_emb {n : ℕ} (σ : Semisentence ℒₛₑₜ n) :
    Rewriting.shift ((Rewriting.emb (ξ := ℕ) σ : Semiproposition ℒₛₑₜ n)) =
      (Rewriting.emb (ξ := ℕ) σ : Semiproposition ℒₛₑₜ n) := by
  apply Semiformula.rew_eq_self_of
  · intro x; rfl
  · intro x hx
    have h0 : ((Rewriting.emb (ξ := ℕ) σ : Semiproposition ℒₛₑₜ n)).fvSup = 0 :=
      Semiformula.fvSup_sentence σ
    have : x < 0 := by
      rw [← h0]
      exact Semiformula.lt_fvSup_of_fvar? hx
    exact absurd this (by simp)

/-- **V 层工具**：`shift` 固定任意 `Semisentence ℒₛₑₜ n` 的引号。 -/
lemma shift_quote {n : ℕ} (φ : Semisentence ℒₛₑₜ n) :
    shift (L := ℒₛₑₜ) ((⌜φ⌝ : V)) = (⌜φ⌝ : V) := by
  rw [Sentence.quote_def]
  rw [← Semiformula.quote_shift (V := V) (L := ℒₛₑₜ)
    (φ := (Rewriting.emb (ξ := ℕ) φ : Semiproposition ℒₛₑₜ n))]
  rw [rew_shift_emb]

/-- **枢纽**：`shift domZero = domZero`。 -/
lemma shift_domZero : shift (L := ℒₛₑₜ) (domZero (V := V)) = domZero (V := V) := by
  have h : domZero (V := V) = (⌜(arithTrln.domain/[#0] : Semisentence ℒₛₑₜ (0 + 1))⌝ : V) := by
    rw [← quote_domain_zero (V := V) (n := 0), emb_app_self]
  rw [h, Sentence.quote_def]
  rw [← Semiformula.quote_shift (V := V) (L := ℒₛₑₜ)
    (φ := (Rewriting.emb (ξ := ℕ) (arithTrln.domain/[#0]) : Semiproposition ℒₛₑₜ (0 + 1)))]
  rw [rew_shift_emb]

/-- `shift` 与 `imp` 相容（`imp a b = neg a ⋎ b`）。 -/
lemma shift_imp {p q : V} (hp : IsUFormula ℒₛₑₜ p) (hq : IsUFormula ℒₛₑₜ q) :
    shift (L := ℒₛₑₜ) (imp ℒₛₑₜ p q) =
      imp ℒₛₑₜ (shift (L := ℒₛₑₜ) p) (shift (L := ℒₛₑₜ) q) := by
  rw [imp, imp, shift_or hp.neg hq]
  congr 1
  exact shift_neg hp.isSemiformula

/-- `shift` 固定 `cFunc 0 f`（0 元函数符号，numeral）。 -/
lemma shift_cFunc0 (f : V) : shift (L := ℒₛₑₜ) (cFunc (V := V) 0 f) = cFunc (V := V) 0 f := by
  simp only [cFunc, cFuncN, reduceIte]
  split
  · rw [Sentence.coe_quote_eq_quote]
    exact shift_quote _
  · split
    · rename_i h; exact absurd h (by decide)
    · rw [Sentence.coe_quote_eq_quote]
      exact shift_quote _

/-- `shift` 固定 `subst [#0] (cFunc 0 f)`——闭代换。 -/
lemma shift_subst_cFunc0 (f : V) :
    shift (L := ℒₛₑₜ) (subst ℒₛₑₜ (^#0 ∷ 0) (cFunc (V := V) 0 f)) =
      subst ℒₛₑₜ (^#0 ∷ 0) (cFunc (V := V) 0 f) := by
  rw [shift_substs (L := ℒₛₑₜ) (n := 1) (m := 1) (p := cFunc (V := V) 0 f)
    (isSemiformula_cFunc_arity0 f)
    (isSemitermVec_single_bvar (n := 1) (by simp))]
  congr 1
  · rw [termShiftVec_cons₁ (IsUTerm.bvar (L := ℒₛₑₜ)), termShift_bvar]
  · exact shift_cFunc0 f

/-- `shift` 固定 `ve0 k f`（func 支的 k=0 情形）。 -/
lemma shift_ve0 (f : V) : shift (L := ℒₛₑₜ) (ve0 (V := V) 0 f) = ve0 (V := V) 0 f := by
  rw [ve0]
  rw [shift_imp IsUFormula.verum ?_]
  · rw [shift_verum (L := ℒₛₑₜ), shift_subst_cFunc0]
  · exact (IsSemiformula.subst (L := ℒₛₑₜ) (n := 1) (m := 1)
      (isSemiformula_cFunc_arity0 f)
      (isSemitermVec_single_bvar (n := 1) (by simp))).isUFormula

end GodelQ.ShiftTools

#print axioms GodelQ.ShiftTools.rew_shift_emb
#print axioms GodelQ.ShiftTools.shift_quote
#print axioms GodelQ.ShiftTools.shift_domZero
#print axioms GodelQ.ShiftTools.shift_imp
#print axioms GodelQ.ShiftTools.shift_cFunc0
#print axioms GodelQ.ShiftTools.shift_subst_cFunc0
#print axioms GodelQ.ShiftTools.shift_ve0
