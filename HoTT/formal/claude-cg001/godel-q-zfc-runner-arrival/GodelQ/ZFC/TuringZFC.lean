import GodelQ.ZFC.Soundness
import GodelQ.Turing

/-!
# CG-007 · W1：图灵路线落在真实的 𝗭𝗙𝗖 上

对象是 Foundation 中的 `𝗭𝗙𝗖`（ℒₛₑₜ 语法、LK 证明系统）。`zfcEffective`（C-95–C-99）把它看作有效理论：
`provesNever e := 𝗭𝗙𝗖 ⊢ neverS ΦH ⌜e⌝`。本文件只用两条性质——这个集合可以被机器列出（C-97），
以及它不说错（由一致性与 Σ1 完全）——再加上停机问题，不构造任何关于 𝗭𝗙𝗖 的自指过程。

* `zfcMisses`：确实永不停机、𝗭𝗙𝗖 却证明不了“永不停机”的过程。
* `zfcMisses_eq_independent`：漏点恰是“永不停机”句独立于 𝗭𝗙𝗖 的那些过程（用 Σ1 可靠性，C-100）。
* `zfc_misses_not_re`、`zfc_misses_infinite`：这样的过程有无穷多个，而且任何机器都列不全。
* `zfc_miss_seen_every_instant`：对每个漏点，𝗭𝗙𝗖 在每一个有限时刻都证明“尚未停机”。
* `zfc_not_completeForNever_turing`、`zfc_incomplete_turing`：𝗭𝗙𝗖 的 Q 不完备、𝗭𝗙𝗖 不完全，证明不经过对角点。
* `zfc_patch_misses`：把 𝗭𝗙𝗖 可证的“永不停机”再补上任意有限个确实永不停机的过程，漏点仍无穷、仍列不全。

文件末尾的依赖检查机器核对：这些定理不依赖本项目的对角点（`diagonal_fixed_point` 等），也不依赖
C-99/C-100 的对角过程定理（`godel_I_process_form_zfc`、`godel_I_process_form_zfc_full`）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic

namespace GodelQ.ZFCTuring

open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff GodelQ.ZFCSound

/-- 𝗭𝗙𝗖 的漏点：确实永不停机、𝗭𝗙𝗖 却证明不了“永不停机”的过程。 -/
def zfcMisses : Set Process := {e | ¬ Done e ∧ 𝗭𝗙𝗖 ⊬ neverS ΦH (Encodable.encode e)}

theorem zfcMisses_eq : zfcMisses = zfcEffective.Misses := rfl

/-- **漏点 = 独立点**：一个过程是 𝗭𝗙𝗖 的漏点，当且仅当它的“永不停机”句独立于 𝗭𝗙𝗖
（“停机”句与“永不停机”句都不可证）。 -/
theorem zfcMisses_eq_independent :
    zfcMisses = {e | 𝗭𝗙𝗖 ⊬ neverS ΦH (Encodable.encode e) ∧ 𝗭𝗙𝗖 ⊬ haltsS ΦH (Encodable.encode e)} := by
  ext e
  simp only [zfcMisses, Set.mem_ofPred_eq]
  have h := zfc_provesHalts_iff e
  constructor
  · rintro ⟨hnd, hna⟩
    exact ⟨hna, fun hH => hnd (h.mp hH)⟩
  · rintro ⟨hna, hnH⟩
    exact ⟨fun hd => hnH (h.mpr hd), hna⟩

/-- **图灵路线，落在 𝗭𝗙𝗖 上 (a)**：𝗭𝗙𝗖 的漏点（等价地：“永不停机”句独立于 𝗭𝗙𝗖 的过程）列不全。 -/
theorem zfc_misses_not_re : ¬ REPred (· ∈ zfcMisses) := zfcEffective.misses_not_re

/-- **图灵路线，落在 𝗭𝗙𝗖 上 (b)**：这样的过程有无穷多个。 -/
theorem zfc_misses_infinite : zfcMisses.Infinite := zfcEffective.misses_infinite

/-- 每一刻看得见：对每个漏点，𝗭𝗙𝗖 对每个 k 证明“它在 k 步内尚未停机”。 -/
theorem zfc_miss_seen_every_instant (e : Process) (he : e ∈ zfcMisses) (k : ℕ) :
    𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (e, k)) :=
  zfcEffective.misses_seen_every_instant e he k

/-- 𝗭𝗙𝗖 的 Q 不完备（图灵式证明）。 -/
theorem zfc_not_completeForNever_turing : ¬ zfcEffective.CompleteForNever :=
  zfcEffective.not_completeForNever_turing

/-- **𝗭𝗙𝗖 不完全（图灵式证明）**：取任一漏点，它的“永不停机”句独立于 𝗭𝗙𝗖。 -/
theorem zfc_incomplete_turing : Entailment.Incomplete 𝗭𝗙𝗖 := by
  obtain ⟨e, he⟩ := zfc_misses_infinite.nonempty
  rw [zfcMisses_eq_independent] at he
  obtain ⟨hna, hnH⟩ := he
  refine ⟨⟨neverS ΦH (Encodable.encode e), hna, ?_⟩⟩
  intro h
  apply hnH
  have h' : 𝗭𝗙𝗖 ⊢ ∼∼ haltsS ΦH (Encodable.encode e) := h
  cl_prover [h']

/-- **有限的补丁补不完**：接受“𝗭𝗙𝗖 证明它永不停机，或它属于有限集 F”（F 中都确实永不停机）的观察者，
漏点恰是 𝗭𝗙𝗖 的漏点去掉 F，仍列不全、仍无穷。 -/
theorem zfc_patch_misses (F : Set Process) (hF : F.Finite) (hnever : ∀ e ∈ F, ¬ Done e) :
    (zfcEffective.observer.patch F hF hnever).Misses = zfcMisses \ F ∧
      ¬ REPred (· ∈ (zfcEffective.observer.patch F hF hnever).Misses) ∧
      (zfcEffective.observer.patch F hF hnever).Misses.Infinite :=
  zfcEffective.observer.patch_misses F hF hnever

end GodelQ.ZFCTuring

open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let diagonal : List Name :=
    [``GodelQ.diagonal_fixed_point, ``GodelQ.diagonal_escape, ``GodelQ.no_complete_never_observer,
     ``GodelQ.complete_observer_not_re, ``GodelQ.tower_step, ``GodelQ.EffectiveTheory.godel_I_process_form,
     ``GodelQ.EffectiveTheory.not_completeForNever, ``GodelQ.EffectiveTheory.devils_bargain,
     ``GodelQ.ZFCEff.godel_I_process_form_zfc, ``GodelQ.ZFCSound.godel_I_process_form_zfc_full]
  let turing : List Name :=
    [``GodelQ.ZFCTuring.zfcMisses_eq_independent, ``GodelQ.ZFCTuring.zfc_misses_not_re,
     ``GodelQ.ZFCTuring.zfc_misses_infinite, ``GodelQ.ZFCTuring.zfc_miss_seen_every_instant,
     ``GodelQ.ZFCTuring.zfc_not_completeForNever_turing, ``GodelQ.ZFCTuring.zfc_incomplete_turing,
     ``GodelQ.ZFCTuring.zfc_patch_misses]
  for r in turing do
    if GodelQ.reaches env r diagonal then
      throwError m!"{r} depends on a GodelQ diagonal declaration"
  for r in [``GodelQ.ZFCTuring.zfc_misses_not_re, ``GodelQ.ZFCTuring.zfc_misses_infinite,
            ``GodelQ.ZFCTuring.zfc_incomplete_turing] do
    unless GodelQ.reaches env r [``ComputablePred.halting_problem_not_re] do
      throwError m!"{r} does not go through the halting theorem"
  unless GodelQ.reaches env ``GodelQ.ZFCSound.godel_I_process_form_zfc_full [``GodelQ.diagonal_fixed_point] do
    throwError "checker failed its positive control"
  logInfo m!"W1 dependency check (ZFC): {turing.length} theorems avoid all {diagonal.length} diagonal declarations (incl. C-99/C-100); the non-r.e., infinitude and incompleteness theorems go through ComputablePred.halting_problem_not_re; positive control passed."

#print axioms GodelQ.ZFCTuring.zfcMisses_eq_independent
#print axioms GodelQ.ZFCTuring.zfc_misses_not_re
#print axioms GodelQ.ZFCTuring.zfc_misses_infinite
#print axioms GodelQ.ZFCTuring.zfc_miss_seen_every_instant
#print axioms GodelQ.ZFCTuring.zfc_not_completeForNever_turing
#print axioms GodelQ.ZFCTuring.zfc_incomplete_turing
#print axioms GodelQ.ZFCTuring.zfc_patch_misses
