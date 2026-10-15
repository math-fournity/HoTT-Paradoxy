import GodelQ.EffectiveTheory
import Mathlib.Data.Set.Finite.Basic

/-!
# CG-007 · W1：图灵路线——不对理论做自指的观察力不完备

哥德尔路线（C-85、C-89）构造一个对角过程 `d`：“我停下，当且仅当你接受我永不停下”。
本文件走另一条路，不构造任何关于被观察理论的自指过程或自指句，只比较两个集合：

* 一个可靠、可枚举的永不完成观察者 `O` 所接受的过程，可以被机器列出（`O.re`）；
* 真正永不完成的过程，不能被任何机器列出（`never_done_not_re`，即 Mathlib 的停机问题）。

于是：

* `NeverObserver.misses_not_re`：`O` 的漏点集 `{e ∣ ¬ Done e ∧ ¬ O.accepts e}` 不可枚举。
  若可枚举，把它并上 `O` 的接受集，就列出了全部永不完成者；
* `NeverObserver.misses_infinite`：漏点有无穷多个，因为有限集都可枚举；
* `NeverObserver.misses_nonempty`：漏点存在；
* `NeverObserver.patch`：给 `O` 补上任意有限个确实永不完成的点，得到的仍是可靠、可枚举的观察者，
  所以上面三条照样成立——有限的补丁补不完；
* `EffectiveTheory.not_completeForNever_turing`：有效理论的 Q 不完备，证明不经过对角点；
* `EffectiveTheory.misses_not_re`、`misses_infinite`：有效理论漏掉的“永不完成”无穷且列不全。

**“不对理论做自指”的确切范围。** 文件末尾的依赖检查在 Lean 环境中机器核对：本文件的定理不依赖
`GodelQ.diagonal_fixed_point`、`GodelQ.diagonal_escape` 及其推论；它们依赖 Mathlib 的
`ComputablePred.halting_problem_not_re`。停机问题本身在 Mathlib 中经 Rice 定理证明，用到了 Kleene
递归定理 `Nat.Partrec.Code.fixed_point₂`——图灵自己的证明也是对角论证。所以“无哥德尔”指的是：
不对被观察的理论（例如 𝗭𝗙𝗖）及其可证性做自指；计算本身的对角论证仍在底层。检查同时核对这一点。

**与哥德尔路线的区别。** 哥德尔路线指名一个漏点 `d`，并给出 `Done d ↔ T.provesNever d`；
图灵路线不指名漏点，只证明漏点存在、无穷、列不全。
-/

namespace GodelQ

open Nat.Partrec Nat.Partrec.Code

/-! ## 有限集可枚举 -/

/-- 单点集可判定，因而可枚举。 -/
theorem singleton_re (d : Process) : REPred (fun e : Process => e = d) :=
  ComputablePred.to_re (PrimrecPred.computablePred (Primrec.eq.comp Primrec.id (Primrec.const d)))

/-- 空集可枚举。 -/
theorem empty_re : REPred (fun _ : Process => False) :=
  ComputablePred.to_re ⟨fun _ => instDecidableFalse, by simpa using (Computable.const false)⟩

/-- 有限的过程集可枚举。 -/
theorem finite_re (S : Set Process) (hS : S.Finite) : REPred (· ∈ S) := by
  refine Set.Finite.induction_on (motive := fun S _ => REPred (· ∈ S)) S hS ?_ ?_
  · exact empty_re.of_eq fun e => by simp
  · intro a s _ _ ih
    exact (REPred.or' (singleton_re a) ih).of_eq fun e => by simp

/-! ## 观察者的漏点 -/

namespace NeverObserver

variable (O : NeverObserver)

/-- 观察者 `O` 的漏点：确实永不完成、`O` 却不接受的过程。 -/
def Misses : Set Process := {e | ¬ Done e ∧ ¬ O.accepts e}

/-- 接受集并上漏点集，恰是全部永不完成者（由可靠性）。 -/
theorem accepts_or_misses_iff (e : Process) : (O.accepts e ∨ e ∈ O.Misses) ↔ ¬ Done e := by
  constructor
  · rintro (h | ⟨h, -⟩)
    · exact O.sound e h
    · exact h
  · intro h
    by_cases ha : O.accepts e
    · exact Or.inl ha
    · exact Or.inr ⟨h, ha⟩

/-- **图灵路线 (a)**：可靠、可枚举的永不完成观察者，其漏点集不可枚举。 -/
theorem misses_not_re : ¬ REPred (· ∈ O.Misses) := fun hM =>
  never_done_not_re ((REPred.or' O.re hM).of_eq (O.accepts_or_misses_iff))

/-- **图灵路线 (b)**：漏点有无穷多个。 -/
theorem misses_infinite : O.Misses.Infinite := fun hfin =>
  O.misses_not_re (finite_re _ hfin)

/-- **图灵路线 (c)**：漏点存在。 -/
theorem misses_nonempty : O.Misses.Nonempty := O.misses_infinite.nonempty

/-- 补丁：给 `O` 补上一个有限集 `F` 中的过程（它们确实永不完成），仍得到可靠、可枚举的观察者。 -/
def patch (F : Set Process) (hF : F.Finite) (hnever : ∀ e ∈ F, ¬ Done e) : NeverObserver where
  accepts e := O.accepts e ∨ e ∈ F
  re := REPred.or' O.re (finite_re F hF)
  sound e h := by
    rcases h with h | h
    · exact O.sound e h
    · exact hnever e h

/-- **有限的补丁补不完**：任意有限补丁之后，漏点仍不可枚举、仍无穷；补丁只拿走了 `F` 中的点。 -/
theorem patch_misses (F : Set Process) (hF : F.Finite) (hnever : ∀ e ∈ F, ¬ Done e) :
    (O.patch F hF hnever).Misses = O.Misses \ F ∧
      ¬ REPred (· ∈ (O.patch F hF hnever).Misses) ∧ (O.patch F hF hnever).Misses.Infinite := by
  refine ⟨?_, (O.patch F hF hnever).misses_not_re, (O.patch F hF hnever).misses_infinite⟩
  ext e
  simp only [Misses, patch, Set.mem_ofPred_eq, Set.mem_sdiff, not_or]
  tauto

end NeverObserver

/-! ## 有效理论 -/

namespace EffectiveTheory

variable (T : EffectiveTheory)

/-- **Q 不完备，图灵式证明**：若 `T` 看得见每一个“永不完成”，则由 Π1 可靠性，`T` 证明的“永不完成”
恰是全部永不完成者，于是后者可枚举，与停机问题矛盾。证明不经过任何对角点。 -/
theorem not_completeForNever_turing : ¬ T.CompleteForNever := fun hC =>
  never_done_not_re (T.re_never.of_eq fun e => ⟨T.never_sound e, hC e⟩)

/-- 有效理论漏掉的“永不完成”：确实永不完成、`T` 却证明不了。 -/
def Misses : Set Process := {e | ¬ Done e ∧ ¬ T.provesNever e}

theorem misses_eq_observer : T.Misses = T.observer.Misses := rfl

/-- 有效理论漏掉的“永不完成”列不全。 -/
theorem misses_not_re : ¬ REPred (· ∈ T.Misses) := T.observer.misses_not_re

/-- 有效理论漏掉的“永不完成”有无穷多个。 -/
theorem misses_infinite : T.Misses.Infinite := T.observer.misses_infinite

/-- 对每个漏点，`T` 在每个有限时刻都确认“尚未完成”——每一刻看得见，“永远”看不见。 -/
theorem misses_seen_every_instant (e : Process) (he : e ∈ T.Misses) (k : ℕ) : T.provesNotYet e k :=
  T.observes_every_instant e he.1 k

end EffectiveTheory

end GodelQ

/-! ## 依赖检查：图灵路线不经过本项目的对角点

`reaches env root targets`：从常量 `root` 出发，沿“定义体与类型中出现的常量”做传递闭包，看能否到达
`targets` 中的某个常量。下面的 `run_cmd` 在不满足预期时报错，编译即失败；满足时打印一行。 -/

open Lean in
/-- 依赖闭包中是否出现 `targets` 里的常量。 -/
def GodelQ.reaches (env : Environment) (root : Name) (targets : List Name) : Bool := Id.run do
  let mut seen : NameSet := {}
  let mut stack : Array Name := #[root]
  let mut found := false
  while !stack.isEmpty && !found do
    let n := stack.back!
    stack := stack.pop
    if !seen.contains n then
      seen := seen.insert n
      if targets.contains n then
        found := true
      else
        match env.find? n with
        | some ci => for m in ci.getUsedConstantsAsSet do stack := stack.push m
        | none => pure ()
  return found

open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let diagonal : List Name :=
    [``GodelQ.diagonal_fixed_point, ``GodelQ.diagonal_escape, ``GodelQ.no_complete_never_observer,
     ``GodelQ.complete_observer_not_re, ``GodelQ.tower_step, ``GodelQ.EffectiveTheory.godel_I_process_form,
     ``GodelQ.EffectiveTheory.not_completeForNever, ``GodelQ.EffectiveTheory.devils_bargain]
  let turing : List Name :=
    [``GodelQ.NeverObserver.misses_not_re, ``GodelQ.NeverObserver.misses_infinite,
     ``GodelQ.NeverObserver.misses_nonempty, ``GodelQ.NeverObserver.patch_misses,
     ``GodelQ.EffectiveTheory.not_completeForNever_turing, ``GodelQ.EffectiveTheory.misses_not_re,
     ``GodelQ.EffectiveTheory.misses_infinite]
  for r in turing do
    if GodelQ.reaches env r diagonal then
      throwError m!"{r} depends on a GodelQ diagonal declaration"
    unless GodelQ.reaches env r [``ComputablePred.halting_problem_not_re] do
      throwError m!"{r} does not go through the halting theorem"
  -- 正控制：检查器确实看得见对角依赖。
  unless GodelQ.reaches env ``GodelQ.EffectiveTheory.godel_I_process_form [``GodelQ.diagonal_fixed_point] do
    throwError "checker failed its positive control"
  -- 照实核对：Mathlib 的停机问题经 Rice 定理用到了递归定理。
  unless GodelQ.reaches env ``ComputablePred.halting_problem_not_re [``Nat.Partrec.Code.fixed_point₂] do
    throwError "expected the halting theorem to use the recursion theorem"
  logInfo m!"W1 dependency check: {turing.length} Turing-route theorems avoid all {diagonal.length} GodelQ diagonal declarations and use ComputablePred.halting_problem_not_re; positive control passed; Mathlib's halting_problem_not_re reaches Nat.Partrec.Code.fixed_point₂ (via rice)."

#print axioms GodelQ.finite_re
#print axioms GodelQ.NeverObserver.misses_not_re
#print axioms GodelQ.NeverObserver.misses_infinite
#print axioms GodelQ.NeverObserver.misses_nonempty
#print axioms GodelQ.NeverObserver.patch_misses
#print axioms GodelQ.EffectiveTheory.not_completeForNever_turing
#print axioms GodelQ.EffectiveTheory.misses_not_re
#print axioms GodelQ.EffectiveTheory.misses_infinite
#print axioms GodelQ.EffectiveTheory.misses_seen_every_instant
