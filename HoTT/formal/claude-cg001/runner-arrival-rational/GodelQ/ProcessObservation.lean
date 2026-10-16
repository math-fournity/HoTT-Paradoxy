import Mathlib.Computability.Halting

/-!
# CG-005 · 计算层：过程完成的观察与 Kleene–罗素对角

研究发起人把时间悖论的特征定为“不可计算性/不可停机性”（KC-000010），把芝诺定为
“结结实实的计算步骤、过程”（2026-10-04）。本文件按这个口径把“过程”取作部分递归程序，
把“原过程完成”取作在输入 0 上停机，然后证明：

* `done_iff_exists_stage`：完成恰好是某个有限阶段完成（每一次完成都发生在某一刻）；
* `doneBy_mono`、`doneBy_computable`：阶段观察单调，且每一刻都可机械判定；
* `diagonal_escape`：任何可枚举（effective）且可靠的“永不完成”观察者，都漏掉一个
  确实永不完成的过程 `d`；`d` 由 Kleene 第二递归定理（`Code.fixed_point₂`）实际构造，
  其行为是“恰在观察者接受它永不完成时停机”——罗素式对角的计算版本；
* `no_complete_never_observer`、`complete_observer_not_re`：可枚举、可靠、完备三者不可兼得；
* `tower_step`：给观察者加上它漏掉的对角点，得到严格更大的可靠观察者，后者仍有新的漏点。

本文件不用任何公理声明；每个主定理后打印所依赖的内核公理。
-/

namespace GodelQ

open Nat.Partrec Nat.Partrec.Code

/-- 过程：一份部分递归程序的代码。 -/
abbrev Process := Code

/-- 原过程完成：程序在输入 0 上停机。 -/
def Done (e : Process) : Prop := (eval e 0).Dom

/-- 阶段观察：程序在 `k` 步燃料之内已经停机。 -/
def DoneBy (e : Process) (k : ℕ) : Prop := (evaln k e 0).isSome = true

instance (e : Process) (k : ℕ) : Decidable (DoneBy e k) := by
  unfold DoneBy; infer_instance

/-- C-84 (a)：完成恰好是某一有限阶段完成。 -/
theorem done_iff_exists_stage (e : Process) : Done e ↔ ∃ k, DoneBy e k := by
  constructor
  · intro h
    obtain ⟨x, hx⟩ := Part.dom_iff_mem.mp h
    obtain ⟨k, hk⟩ := evaln_complete.mp hx
    refine ⟨k, ?_⟩
    unfold DoneBy
    rw [Option.mem_def] at hk
    rw [hk]; rfl
  · rintro ⟨k, hk⟩
    unfold DoneBy at hk
    obtain ⟨x, hx⟩ := Option.isSome_iff_exists.mp hk
    exact Part.dom_iff_mem.mpr ⟨x, evaln_sound (Option.mem_def.mpr hx)⟩

/-- C-84 (b)：阶段观察单调——一旦在某一刻看到完成，以后各刻都看到完成。 -/
theorem doneBy_mono {e : Process} {k₁ k₂ : ℕ} (h : k₁ ≤ k₂) (h₁ : DoneBy e k₁) :
    DoneBy e k₂ := by
  unfold DoneBy at *
  obtain ⟨x, hx⟩ := Option.isSome_iff_exists.mp h₁
  have := evaln_mono h (Option.mem_def.mpr hx)
  rw [Option.mem_def] at this
  rw [this]; rfl

/-- C-84 (c)：每一刻的观察都可机械判定（作为过程与阶段的二元谓词可计算）。 -/
theorem doneBy_computable : ComputablePred (fun p : Process × ℕ => DoneBy p.1 p.2) := by
  have hev : Computable (fun p : Process × ℕ => evaln p.2 p.1 0) :=
    (primrec_evaln.to_comp).comp
      ((Computable.pair (Computable.pair Computable.snd Computable.fst) (Computable.const 0)))
  have hsome : Computable (fun p : Process × ℕ => (evaln p.2 p.1 0).isSome) :=
    (Primrec.option_isSome.to_comp).comp hev
  refine Computable.computablePred ?_
  have heq : (fun p : Process × ℕ => decide (DoneBy p.1 p.2)) =
      (fun p : Process × ℕ => (evaln p.2 p.1 0).isSome) := by
    funext p; unfold DoneBy; exact Bool.decide_eq_true
  rw [heq]; exact hsome

/-- 一个“永不完成”观察者：一个可枚举的接受集，只接受确实永不完成的过程。
`re` 表示它是机械可执行的（例如一个有效公理化理论证明出的“永不停机”句的集合）；
`sound` 表示它不说错。 -/
structure NeverObserver where
  accepts : Process → Prop
  re : REPred accepts
  sound : ∀ e, accepts e → ¬ Done e

/-- C-85 (a)：Kleene–罗素对角点。对任一可枚举的接受集 `accepts`，存在一个过程 `d`，
它停机当且仅当 `accepts d`。`d` 由 Kleene 第二递归定理构造：程序 `d` 去执行接受集的
半判定过程，并以自己的代码为输入——“我停下，当且仅当你接受我”。 -/
theorem diagonal_fixed_point (accepts : Process → Prop) (hre : REPred accepts) :
    ∃ d : Process, (Done d ↔ accepts d) := by
  have hf : Partrec₂ (fun (c : Code) (_ : ℕ) =>
      Part.map (fun _ : Unit => (0 : ℕ)) (Part.assert (accepts c) fun _ => Part.some ())) := by
    have h1 : Partrec (fun p : Code × ℕ => Part.assert (accepts p.1) fun _ => Part.some ()) :=
      hre.comp Computable.fst
    exact Partrec.map h1 (Computable.const (0 : ℕ)).to₂
  obtain ⟨d, hd⟩ := fixed_point₂ hf
  refine ⟨d, ?_⟩
  unfold Done
  rw [hd]
  simp [Part.assert]

/-- C-85 (b)：对角逃逸。任一可枚举且可靠的永不完成观察者 `O`，都有一个过程 `d`：
`d` 确实永不完成，`O` 却不接受它；并且 `d` 停机当且仅当 `O` 接受 `d`。 -/
theorem diagonal_escape (O : NeverObserver) :
    ∃ d : Process, ¬ Done d ∧ ¬ O.accepts d ∧ (Done d ↔ O.accepts d) := by
  obtain ⟨d, hd⟩ := diagonal_fixed_point O.accepts O.re
  have hna : ¬ O.accepts d := fun ha => O.sound d ha (hd.mpr ha)
  exact ⟨d, fun hD => hna (hd.mp hD), hna, hd⟩

/-- C-86 (a)：不存在可枚举、可靠且完备的永不完成观察者。 -/
theorem no_complete_never_observer :
    ¬ ∃ O : NeverObserver, ∀ e, ¬ Done e → O.accepts e := by
  rintro ⟨O, hcomplete⟩
  obtain ⟨d, hnd, hna, _⟩ := diagonal_escape O
  exact hna (hcomplete d hnd)

/-- C-86 (b)：任何可靠且完备的永不完成判定集都不可枚举——完备的观察需要不可计算的东西。 -/
theorem complete_observer_not_re (accepts : Process → Prop)
    (sound : ∀ e, accepts e → ¬ Done e) (complete : ∀ e, ¬ Done e → accepts e) :
    ¬ REPred accepts := fun hre =>
  no_complete_never_observer ⟨⟨accepts, hre, sound⟩, complete⟩

/-- C-86 (c)：与 Mathlib 停机问题的独立交叉核对：“永不完成”本身不可枚举
（Mathlib 经 Rice 定理证明，与本文件的对角证明是两条独立路线）。 -/
theorem never_done_not_re : ¬ REPred (fun e : Process => ¬ Done e) :=
  ComputablePred.halting_problem_not_re 0

/-- 两个可枚举谓词之并仍可枚举。 -/
theorem REPred.or' {α : Type} [Primcodable α] {p q : α → Prop}
    (hp : REPred p) (hq : REPred q) : REPred (fun a => p a ∨ q a) := by
  obtain ⟨k, hk, H⟩ := Partrec.merge' hp hq
  refine (Partrec.dom_re hk).of_eq ?_
  intro a
  rw [(H a).2]
  simp [Part.assert]

/-- 观察者加入一个确实永不完成的新点之后，仍是可枚举且可靠的观察者。 -/
def NeverObserver.extend (O : NeverObserver) (d : Process) (hd : ¬ Done d) : NeverObserver where
  accepts e := O.accepts e ∨ e = d
  re := REPred.or' O.re
    (ComputablePred.to_re (PrimrecPred.computablePred
      (Primrec.eq.comp Primrec.id (Primrec.const d))))
  sound e h := by
    rcases h with h | rfl
    · exact O.sound e h
    · exact hd

/-- C-87：补丁塔的一步。任一观察者 `O` 都有严格更大的可靠观察者 `O'`（多接受一个 `O`
漏掉的真永不完成者），而 `O'` 仍然漏掉某个永不完成者。补丁永远打不完。 -/
theorem tower_step (O : NeverObserver) :
    ∃ O' : NeverObserver, (∀ e, O.accepts e → O'.accepts e) ∧
      (∃ d, O'.accepts d ∧ ¬ O.accepts d) ∧ (∃ d', ¬ Done d' ∧ ¬ O'.accepts d') := by
  obtain ⟨d, hnd, hna, _⟩ := diagonal_escape O
  let O' := O.extend d hnd
  obtain ⟨d', hnd', hna', _⟩ := diagonal_escape O'
  exact ⟨O', fun e h => Or.inl h, ⟨d, Or.inr rfl, hna⟩, ⟨d', hnd', hna'⟩⟩

end GodelQ

#print axioms GodelQ.done_iff_exists_stage
#print axioms GodelQ.doneBy_mono
#print axioms GodelQ.doneBy_computable
#print axioms GodelQ.diagonal_fixed_point
#print axioms GodelQ.diagonal_escape
#print axioms GodelQ.no_complete_never_observer
#print axioms GodelQ.complete_observer_not_re
#print axioms GodelQ.never_done_not_re
#print axioms GodelQ.tower_step
