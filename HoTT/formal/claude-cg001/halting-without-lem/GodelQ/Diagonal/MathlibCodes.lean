import Mathlib.Computability.Halting
import GodelQ.Diagonal.Core

/-!
# 翻转程序在真实的计算模型里存在（CG001-C-422 的实例）

`Core.lean` 的对角论证只要求一条编程事实：翻转程序。本文件在 Mathlib 的计算模型里证明它：
程序是部分递归函数的代码（`Nat.Partrec.Code`，按自然数编号），“停机”是在输入上求值有定义，
“回答‘否’”是在输入“对子 (e, x)”上求值得到 0。

* `code_flip`：对每个程序 `d`，有程序 `f`：`f` 在 `x` 上停机，恰好当 `d` 对 (x, x) 回答“否”。
  `f` 的写法就是“先运行 `d`，答 0 就停，答别的就永远不停”。
* `codeSystem`：于是 Mathlib 的代码组成一个 `ProgSystem`。
* `turing_codes`：没有程序恰好认出“永不停机”；没有完全的停机判定器。

**身份**：本文件是经典的（Mathlib 的可计算性库依赖 `Classical.choice`，审计核对）。经典的只是
“翻转程序存在”这一句正面的编程事实；“认不全”那一步是 `Core.lean` 的 `no_never_recognizer`，
不依赖任何公理。
-/

namespace GodelQ.Diagonal

open Nat.Partrec

/-- 程序 `e` 在输入 `x` 上停机。 -/
def codeHalts (e x : ℕ) : Prop := (Code.eval (Denumerable.ofNat Code e) x).Dom

/-- 程序 `d` 在输入“对子 (e, x)”上停机并回答“否”（输出 0）。 -/
def codeSaysNo (d e x : ℕ) : Prop := Code.eval (Denumerable.ofNat Code d) (Nat.pair e x) = Part.some 0

/-- 程序 `d` 回答“是”（输出 1）。 -/
def codeSaysYes (d e x : ℕ) : Prop := Code.eval (Denumerable.ofNat Code d) (Nat.pair e x) = Part.some 1

/-- 翻转的计算：先得到 `p` 的值，是 0 就停（输出 0），不是 0 就永远不停。 -/
def flipStep (r : ℕ) : Part ℕ := bif r == 0 then Part.some 0 else Part.none

theorem flipStep_dom (p : Part ℕ) : (p.bind flipStep).Dom ↔ p = Part.some 0 := by
  rw [Part.bind_dom, Part.eq_some_iff, Part.mem_eq]
  constructor
  · rintro ⟨h, hd⟩
    refine ⟨h, ?_⟩
    unfold flipStep at hd
    cases hr : (p.get h == 0) with
    | false => rw [hr] at hd; exact absurd hd (by simp)
    | true => exact beq_iff_eq.mp hr
  · rintro ⟨h, hv⟩
    refine ⟨h, ?_⟩
    unfold flipStep
    rw [hv]
    simp

/-- 翻转程序在 Mathlib 的计算模型里存在。 -/
theorem code_flip (d : ℕ) : ∃ f, ∀ x, codeHalts f x ↔ codeSaysNo d x x := by
  let g : ℕ →. ℕ := fun x => (Code.eval (Denumerable.ofNat Code d) (Nat.pair x x)).bind flipStep
  have h1 : Partrec (fun x : ℕ => Code.eval (Denumerable.ofNat Code d) (Nat.pair x x)) :=
    Code.eval_part.comp (Computable.const _)
      (Primrec₂.natPair.comp Primrec.id Primrec.id).to_comp
  have h2 : Partrec₂ (fun (_ : ℕ) (r : ℕ) => flipStep r) := by
    unfold Partrec₂ flipStep
    exact Partrec.cond ((Primrec.beq.comp Primrec.snd (Primrec.const 0)).to_comp)
      ((Computable.const 0).partrec) Partrec.none
  have hg : Partrec g := Partrec.bind h1 h2
  obtain ⟨c, hc⟩ := Code.exists_code.mp (Partrec.nat_iff.mp hg)
  refine ⟨Encodable.encode c, fun x => ?_⟩
  unfold codeHalts codeSaysNo
  rw [Denumerable.ofNat_encode, hc]
  exact flipStep_dom _

/-- Mathlib 的代码组成一个有翻转程序的编程系统。 -/
def codeSystem : ProgSystem where
  Halts := codeHalts
  SaysNo := codeSaysNo
  flip := code_flip

/-- C-422 (4)：在 Mathlib 的计算模型里，没有程序恰好认出“永不停机”，也没有完全的停机判定器。 -/
theorem turing_codes :
    (¬ ∃ d, ∀ e x, codeSaysNo d e x ↔ ¬ codeHalts e x) ∧
    (¬ ∃ d, ∀ e x, (codeSaysYes d e x ↔ codeHalts e x) ∧ (codeSaysNo d e x ↔ ¬ codeHalts e x)) :=
  ⟨no_never_recognizer codeSystem, no_decider codeSystem codeSaysYes⟩

end GodelQ.Diagonal

#print axioms GodelQ.Diagonal.flipStep_dom
#print axioms GodelQ.Diagonal.code_flip
#print axioms GodelQ.Diagonal.turing_codes
