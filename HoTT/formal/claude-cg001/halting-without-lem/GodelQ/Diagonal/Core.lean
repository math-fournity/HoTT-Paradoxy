/-!
# 判不全不靠排中律：图灵对角论证的逻辑核心（CG001-C-422）

CN-079 说：“判不全不是哪个理论造成的。任何机器都判定不了停机，这个证明用不到排中律。”
那一句原先是凭记忆的文献判断。本文件把它的逻辑核心写成定理，并且只用 Lean 内核（不导入
Mathlib）；`QualificationDiag.lean` 的公理审计机器断言这里的定理不依赖 `Classical.choice`。

做法：把“编程系统”只抽出一条性质——**翻转程序**：给定任何程序 `d`，都能写出程序 `f`，它在
输入 `x` 上停机，恰好当 `d` 对“对子 (x, x)”回答“否”。这是一条普通的编程事实：先运行 `d`，
答“否”就停，答别的就一直循环。它不含自指，也不预设结论；自指只发生在证明里（把 `f` 喂给它
自己）。`MathlibCodes.lean` 证明 Mathlib 的计算模型（部分递归函数的代码）有这条性质。

* `no_liar`：`P ↔ ¬P` 推出矛盾。这一步就是说谎者的形状，不用排中律。
* `no_never_recognizer`：在任何有翻转程序的系统里，没有程序恰好认出“永不停机”。
* `no_decider`：推论，没有完全的停机判定器。
* `recognizer_without_flip`：正控制。去掉翻转程序这一条，“认出永不停机”的程序可以存在，
  所以这一条是用到的前提。
-/

namespace GodelQ.Diagonal

/-- 一个编程系统：程序与输入都用自然数编号。 -/
structure ProgSystem where
  /-- 程序 `e` 在输入 `x` 上停机。 -/
  Halts : Nat → Nat → Prop
  /-- 程序 `d` 在输入“对子 (e, x)”上停机，并回答“否”。 -/
  SaysNo : Nat → Nat → Nat → Prop
  /-- 翻转程序：对每个程序 `d`，有一个程序 `f`，它在输入 `x` 上停机，恰好当 `d` 对 (x, x) 回答“否”。 -/
  flip : ∀ d, ∃ f, ∀ x, Halts f x ↔ SaysNo d x x

/-- 程序 `d` 恰好认出“永不停机”：`d` 对 (e, x) 回答“否”，恰好当程序 `e` 在 `x` 上永不停机。 -/
def RecognizesNever (S : ProgSystem) (d : Nat) : Prop :=
  ∀ e x, S.SaysNo d e x ↔ ¬ S.Halts e x

/-- 程序 `d` 是完全的停机判定器：对每个 (e, x) 都答对“是”或“否”。 -/
def Decides (S : ProgSystem) (SaysYes : Nat → Nat → Nat → Prop) (d : Nat) : Prop :=
  ∀ e x, (SaysYes d e x ↔ S.Halts e x) ∧ (S.SaysNo d e x ↔ ¬ S.Halts e x)

/-- 说谎者的形状：`P ↔ ¬P` 推出矛盾。不用排中律。 -/
theorem no_liar (P : Prop) (h : P ↔ ¬ P) : False :=
  have hn : ¬ P := fun hp => (h.mp hp) hp
  hn (h.mpr hn)

/-- C-422 (1)：在任何有翻转程序的编程系统里，没有程序恰好认出“永不停机”。 -/
theorem no_never_recognizer (S : ProgSystem) : ¬ ∃ d, RecognizesNever S d := by
  intro ⟨d, hd⟩
  obtain ⟨f, hf⟩ := S.flip d
  exact no_liar (S.Halts f f) ((hf f).trans (hd f f))

/-- C-422 (2)：推论，没有完全的停机判定器。 -/
theorem no_decider (S : ProgSystem) (SaysYes : Nat → Nat → Nat → Prop) :
    ¬ ∃ d, Decides S SaysYes d :=
  fun ⟨d, hd⟩ => no_never_recognizer S ⟨d, fun e x => (hd e x).2⟩

/-- C-422 (3)，正控制：去掉翻转程序，“恰好认出永不停机”的程序可以存在
（什么都不停机、判定器一律回答“否”的系统）。 -/
theorem recognizer_without_flip :
    ∃ (H : Nat → Nat → Prop) (N : Nat → Nat → Nat → Prop) (d : Nat),
      (∀ e x, N d e x ↔ ¬ H e x) ∧ ¬ (∀ d, ∃ f, ∀ x, H f x ↔ N d x x) := by
  refine ⟨fun _ _ => False, fun _ _ _ => True, 0, fun _ _ => ⟨fun _ h => h, fun _ => trivial⟩, ?_⟩
  intro hflip
  obtain ⟨f, hf⟩ := hflip 0
  exact (hf 0).mpr trivial

end GodelQ.Diagonal

#print axioms GodelQ.Diagonal.no_liar
#print axioms GodelQ.Diagonal.no_never_recognizer
#print axioms GodelQ.Diagonal.no_decider
#print axioms GodelQ.Diagonal.recognizer_without_flip
