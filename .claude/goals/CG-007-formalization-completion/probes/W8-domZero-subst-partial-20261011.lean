import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeT

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 引理 1：termSubstVec 1 ?[^&0] ?[^#0] = ?[^&0]
-- termSubstVec 逐分量做 termSubst：对 bvar z 换成 w.[z]。
-- 这里 v = ?[^#0]，第 0 分量是 ^#0，故 termSubst ?[^&0] ^#0 = ?[^&0].[0] = ^&0。
lemma termSubstVec_fvar_single :
    termSubstVec ℒₛₑₜ 1 (?[^&0] : V) (?[^#0] : V) = ?[^&0] := by
  rw [show (1 : V) = 0 + 1 by norm_num,
      termSubstVec_cons (IsUTerm.bvar (z := 0)) IsUTermVec.empty,
      termSubst_bvar, termSubstVec_nil]
  simp

-- 引理 1.5：引号化句子上任意代入都是恒等
-- cDomN = ⌜arithTrln.domain⌝ 是 Semisentence 的引号（V 层），无自由 bvar，
-- 故 subst 不动它。这需要 Foundation 的 subst_quote 类引理。
#check @Bootstrapping.subst_quote

-- 引理 2：subst ?[^&0] domZero = domZero
lemma subst_fvar_domZero :
    subst ℒₛₑₜ (?[^&0] : V) (domZero (V := V)) = domZero (V := V) := by
  show subst ℒₛₑₜ (?[^&0] : V) (subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V)
  have hw : IsSemitermVec ℒₛₑₜ 1 1 (?[^&0] : V) :=
    IsSemitermVec.singleton.mpr (IsSemiterm.fvar 1 0)
  have hv : IsSemitermVec ℒₛₑₜ 1 1 (?[^#0] : V) :=
    isSemitermVec_single_bvar (n := 1) (by simp)
  have hstep := substs_substs (L := ℒₛₑₜ) (p := ((cDomN : ℕ) : V))
    (l := (1 : V)) (n := (1 : V)) (m := (1 : V))
    (isSemiformula_cDomN) hw hv
  rw [hstep, termSubstVec_fvar_single]
  -- 剩下的：subst ?[^&0] cDomN = subst ?[^#0] cDomN
  -- 两者都是「引号化句子上代入」，都是恒等（cDomN 无自由 bvar）
  rw [subst_quote_sentence_eq, subst_quote_sentence_eq]

end GodelQ.ProbeT
