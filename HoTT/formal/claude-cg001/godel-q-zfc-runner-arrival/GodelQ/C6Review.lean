import GodelQ.ZFC.TuringZFC

/-!
# CG-007 · W7（二）：C6——元理论对标准解的审查力（AI 提案）

研究发起人【原话】（十三条 [3]，KC-000065）：“按道理来说，Meta Theory应该能够检验Sub Theory的边界，也就是说，
它能够解决什么问题，不能够解决什么问题？……由于Meta Theory的理论精度不够……它对于Sub Theory的错误，无法产生批判力”。
GPT 的 dev-01 把这件事写成 SOP 的 C0–C6 总门，并要求“审查责任”的来源（dev-01 #13、#14）。这里的来源就是上面
研究发起人自己的话；下面的**定义是 AI 的提案**，口径要研究发起人裁定。

* 任务族：哥德尔–芝诺跑者（C-91）。子理论（极限理论）的标准解对跑者 d 的完成判词，是极限意义的到达
  `Arrives d`；原过程完成是在某个有限阶段取到终点 1（研究发起人固定的“有限阶段余量精确为零”）。
* `Review`（审查）：对每个 d，元理论要么证明“标准解在 d 上充分”（判词与原过程完成一致），要么证明“不充分”；
  所证不错；元理论有效，即它证明的“不充分”可枚举。
* `no_complete_review`：有效的审查都不完备——总有某个跑者，元理论既确认不了“充分”，也确认不了“不充分”。
  证明经停机定理（图灵式），不经对角点。
* `zfc_review_gap`：落在 𝗭𝗙𝗖 上——有一个跑者，𝗭𝗙𝗖 既证明不了标准解对它充分，也证明不了不充分。
  这里把“𝗭𝗙𝗖 证明充分／不充分”取为证明它停机／永不停机，依据是元层的等价（`inadequate_iff`）；
  直接用 ℒₛₑₜ 写“跑者到达”的句子，要等跑者到达句（CG-007 W5）。
-/

namespace GodelQ.C6

open Nat.Partrec Nat.Partrec.Code

/-- 原过程完成：跑者在某个有限阶段取到终点 1。 -/
def ReachesEnd (d : Process) : Prop := ∃ n, position d n = 1

theorem not_reachesEnd (d : Process) : ¬ ReachesEnd d := fun ⟨n, hn⟩ => (position_lt_one d n).ne hn

/-- 标准解在 d 上充分：极限意义的到达与原过程完成一致。 -/
def Adequate (d : Process) : Prop := Arrives d ↔ ReachesEnd d

/-- 不充分恰是“跑者到达”，即过程永不停机（因为跑者永远到不了 1）。 -/
theorem inadequate_iff (d : Process) : ¬ Adequate d ↔ ¬ Done d := by
  unfold Adequate
  rw [← arrives_iff]
  constructor
  · intro h
    by_contra ha
    exact h ⟨fun hA => absurd hA ha, fun hR => absurd hR (not_reachesEnd d)⟩
  · intro hA h
    exact not_reachesEnd d (h.mp hA)

theorem adequate_iff (d : Process) : Adequate d ↔ Done d := by
  have := inadequate_iff d
  constructor
  · intro h
    by_contra hd
    exact (this.mpr hd) h
  · intro hd
    by_contra h
    exact (this.mp h) hd

/-- **C6（AI 提案）**：元理论对标准解在跑者族上的审查。 -/
structure Review where
  provesAdequate : Process → Prop
  provesInadequate : Process → Prop
  sound_adequate : ∀ d, provesAdequate d → Adequate d
  sound_inadequate : ∀ d, provesInadequate d → ¬ Adequate d
  re_inadequate : REPred provesInadequate

/-- 审查完备：对每个跑者都给出裁决。 -/
def Review.Complete (R : Review) : Prop := ∀ d, R.provesAdequate d ∨ R.provesInadequate d

/-- **有效的审查都不完备。** -/
theorem no_complete_review (R : Review) : ¬ R.Complete := by
  intro hc
  apply never_done_not_re
  refine R.re_inadequate.of_eq fun d => ⟨fun h => (inadequate_iff d).mp (R.sound_inadequate d h),
    fun hnd => ?_⟩
  rcases hc d with h | h
  · exact absurd (R.sound_adequate d h) ((inadequate_iff d).mpr hnd)
  · exact h

/-- 正控制：去掉有效性这一条，照真值裁决的审查可靠且完备；所以让审查不完备的正是“有效”。 -/
theorem truth_review_complete :
    ∃ pa pi : Process → Prop, (∀ d, pa d → Adequate d) ∧ (∀ d, pi d → ¬ Adequate d) ∧
      ∀ d, pa d ∨ pi d :=
  ⟨Adequate, fun d => ¬ Adequate d, fun _ h => h, fun _ h => h, fun d => em (Adequate d)⟩

/-- 跑者族上，审查与“看见每一个永不停机”是同一件事：完备的审查给出完备的永不完成观察。 -/
theorem complete_review_sees_every_never (R : Review) (hc : R.Complete) :
    ∀ d, ¬ Done d → R.provesInadequate d := fun d hnd =>
  (hc d).resolve_left fun h => (inadequate_iff d).mpr hnd (R.sound_adequate d h)

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ZFCNum GodelQ.ZFCEff GodelQ.ZFCSound GodelQ.ZFCTuring

/-- 𝗭𝗙𝗖 的审查：证明“d 停机”即证明标准解对 d 充分，证明“d 永不停机”即证明不充分（经元层的
`adequate_iff`、`inadequate_iff`）。 -/
noncomputable def zfcReview : Review where
  provesAdequate d := 𝗭𝗙𝗖 ⊢ haltsS ΦH (Encodable.encode d)
  provesInadequate d := 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode d)
  sound_adequate d h := (adequate_iff d).mpr ((zfc_provesHalts_iff d).mp h)
  sound_inadequate d h := (inadequate_iff d).mpr (zfcEffective.never_sound d h)
  re_inadequate := zfcEffective.re_never

/-- **𝗭𝗙𝗖 审查不了标准解**：有一个跑者，标准解对它确实不充分（极限说到了，原过程永远没到），
𝗭𝗙𝗖 却既证明不了“充分”，也证明不了“不充分”。 -/
theorem zfc_review_gap :
    ∃ d : Process, ¬ Adequate d ∧ ¬ zfcReview.provesAdequate d ∧ ¬ zfcReview.provesInadequate d := by
  obtain ⟨e, he⟩ := zfc_misses_infinite.nonempty
  have hnd : ¬ Done e := he.1
  rw [zfcMisses_eq_independent] at he
  exact ⟨e, (inadequate_iff e).mpr hnd, he.2, he.1⟩

theorem zfc_review_incomplete : ¬ zfcReview.Complete := no_complete_review zfcReview

/-- 用任一 ℒₛₑₜ 公式 Φ 写“标准解在 d 上出错”（形如 `neverS Φ ⌜d⌝`）时，只要 𝗭𝗙𝗖 不错证它，
它就是一个可靠、可枚举的永不完成观察者（可枚举由 C-97）。 -/
noncomputable def criticObserver (Φ : SetTheorySemisentence 1)
    (hsound : ∀ d : Process, 𝗭𝗙𝗖 ⊢ neverS Φ (Encodable.encode d) → ¬ Adequate d) : NeverObserver where
  accepts d := 𝗭𝗙𝗖 ⊢ neverS Φ (Encodable.encode d)
  re := (never_re Φ).comp Computable.encode
  sound d h := (inadequate_iff d).mp (hsound d h)

/-- **𝗭𝗙𝗖 对子理论的错误没有完备的批判力**：不论用哪个 ℒₛₑₜ 公式 Φ 来写“标准解在 d 上出错”，只要
𝗭𝗙𝗖 不错证它，标准解确实出错、𝗭𝗙𝗖 却证明不了它出错的跑者就有无穷多个，而且列不全。 -/
theorem zfc_cannot_criticize (Φ : SetTheorySemisentence 1)
    (hsound : ∀ d : Process, 𝗭𝗙𝗖 ⊢ neverS Φ (Encodable.encode d) → ¬ Adequate d) :
    {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ neverS Φ (Encodable.encode d)}.Infinite ∧
    ¬ REPred (· ∈ {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ neverS Φ (Encodable.encode d)}) := by
  have heq : {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ neverS Φ (Encodable.encode d)} =
      (criticObserver Φ hsound).Misses := by
    ext d
    simp only [NeverObserver.Misses, criticObserver, Set.mem_ofPred_eq, inadequate_iff]
  rw [heq]
  exact ⟨(criticObserver Φ hsound).misses_infinite, (criticObserver Φ hsound).misses_not_re⟩

end GodelQ.C6

#print axioms GodelQ.C6.inadequate_iff
#print axioms GodelQ.C6.adequate_iff
#print axioms GodelQ.C6.no_complete_review
#print axioms GodelQ.C6.complete_review_sees_every_never
#print axioms GodelQ.C6.zfcReview
#print axioms GodelQ.C6.zfc_review_gap
#print axioms GodelQ.C6.zfc_review_incomplete
#print axioms GodelQ.C6.truth_review_complete
#print axioms GodelQ.C6.zfc_cannot_criticize
