/-!
# CG-005 · 证明论层：Löb、哥德尔第二不完备与自用 P 的崩塌（Z0）

`HBLTheory` 是一个抽象的有效理论：句子集 `S`，可证性 `Pr`，蕴涵 `imp`，假 `bot`，
以及理论内部的可证性算子 `box`（`box φ` 读作 ⌜φ 可证⌝，即“对 φ 的证明搜索会停机”）。
前提是标准的 Hilbert–Bernays–Löb 可推导条件 D1–D3、蕴涵的 K、S 公理与分离规则，
以及对角引理（对任意 φ 有 G 使 `G ↔ (box G → φ)` 可证）。对 bare ZFC，这些都是
教科书元定理（Hilbert–Bernays 1939；Löb 1955）。

* `loeb`：若 `box φ → φ` 可证，则 `φ` 可证；
* `goedel_II`：若理论证明自己的一致性 `con := box bot → bot`，则它证明 `bot`；
* `goedel_II_consistent`：一致的理论证明不了自己的一致性；
* `con` 就是 Z0：`box bot` 读作“对矛盾的证明搜索会停机”，`con` 读作“这个搜索永不停机”；
* `self_consistency_collapse`：把自身一致性当作公理（“完成的整体宣布：我的矛盾搜索已经
  完成，什么也没找到”）的理论是矛盾的；
* `extension_strict`：ZFC-1 = ZFC + Con(ZFC) 严格强于 ZFC（在 ZFC 一致时）；
* `trivialBoxModel`：前提可以同时被一个一致的模型满足（非空）。

本文件只用 Lean 核心，不导入 Mathlib。
-/

namespace GodelQ

/-- 满足 Hilbert–Bernays–Löb 可推导条件与对角引理的抽象理论。 -/
structure HBLTheory where
  S : Type
  Pr : S → Prop
  imp : S → S → S
  bot : S
  box : S → S
  ax_k : ∀ a b, Pr (imp a (imp b a))
  ax_s : ∀ a b c, Pr (imp (imp a (imp b c)) (imp (imp a b) (imp a c)))
  mp : ∀ {a b}, Pr (imp a b) → Pr a → Pr b
  d1 : ∀ {a}, Pr a → Pr (box a)
  d2 : ∀ a b, Pr (imp (box (imp a b)) (imp (box a) (box b)))
  d3 : ∀ a, Pr (imp (box a) (box (box a)))
  diag : ∀ φ, ∃ G, Pr (imp G (imp (box G) φ)) ∧ Pr (imp (imp (box G) φ) G)

namespace HBLTheory

variable (T : HBLTheory)

/-- 理论自己的一致性陈述：`box bot → bot`。读作 Z0：“对矛盾的证明搜索永不停机”。 -/
def con : T.S := T.imp (T.box T.bot) T.bot

/-- 假言三段论，由 K、S 与分离规则推出。 -/
theorem syl {a b c : T.S} (hab : T.Pr (T.imp a b)) (hbc : T.Pr (T.imp b c)) :
    T.Pr (T.imp a c) := by
  have h1 : T.Pr (T.imp a (T.imp b c)) := T.mp (T.ax_k _ _) hbc
  have h2 : T.Pr (T.imp (T.imp a b) (T.imp a c)) := T.mp (T.ax_s _ _ _) h1
  exact T.mp h2 hab

/-- 由 `a → (b → c)` 与 `a → b` 得 `a → c`（S 公理的应用）。 -/
theorem s_app {a b c : T.S} (h1 : T.Pr (T.imp a (T.imp b c))) (h2 : T.Pr (T.imp a b)) :
    T.Pr (T.imp a c) :=
  T.mp (T.mp (T.ax_s _ _ _) h1) h2

/-- Löb 定理。 -/
theorem loeb (φ : T.S) (h : T.Pr (T.imp (T.box φ) φ)) : T.Pr φ := by
  obtain ⟨G, hG1, hG2⟩ := T.diag φ
  -- □G → □(□G → φ)
  have h3 : T.Pr (T.imp (T.box G) (T.box (T.imp (T.box G) φ))) :=
    T.mp (T.d2 _ _) (T.d1 hG1)
  -- □G → (□□G → □φ)
  have h5 : T.Pr (T.imp (T.box G) (T.imp (T.box (T.box G)) (T.box φ))) :=
    T.syl h3 (T.d2 _ _)
  -- □G → □φ
  have h7 : T.Pr (T.imp (T.box G) (T.box φ)) := T.s_app h5 (T.d3 G)
  -- □G → φ
  have h9 : T.Pr (T.imp (T.box G) φ) := T.syl h7 h
  -- G, □G, φ
  have h10 : T.Pr G := T.mp hG2 h9
  exact T.mp h9 (T.d1 h10)

/-- 哥德尔第二不完备定理：证明自己一致性的理论证明 `bot`。 -/
theorem goedel_II (h : T.Pr T.con) : T.Pr T.bot := T.loeb T.bot h

/-- 一致的理论证明不了自己的一致性（Z0：一致的理论看不见“自己的矛盾搜索永不停机”）。 -/
theorem goedel_II_consistent (hcon : ¬ T.Pr T.bot) : ¬ T.Pr T.con := fun h =>
  hcon (T.goedel_II h)

/-- 自用 P 的崩塌：把“我的矛盾搜索已完成且一无所获”当作公理的理论是矛盾的。 -/
theorem self_consistency_collapse (hax : T.Pr T.con) : T.Pr T.bot := T.goedel_II hax

end HBLTheory

/-- 一个扩张：同一批句子上的更强可证性，它证明了原理论的一致性（ZFC-1 = ZFC + Con(ZFC)）。 -/
structure HBLExtension (T : HBLTheory) where
  Pr' : T.S → Prop
  extends_ : ∀ s, T.Pr s → Pr' s
  proves_con : Pr' T.con

/-- ZFC-1 严格强于 ZFC：原理论一致时，扩张证明了原理论证明不了的句子（它自己的一致性）。 -/
theorem extension_strict (T : HBLTheory) (E : HBLExtension T) (hcon : ¬ T.Pr T.bot) :
    ∃ s, E.Pr' s ∧ ¬ T.Pr s :=
  ⟨T.con, E.proves_con, T.goedel_II_consistent hcon⟩

/-- 非空控制：前提可被一个一致的模型同时满足——句子取命题，可证取为真，
内部可证性取为恒真（一个“相信一切都可证”的理论，类似 PA + ¬Con(PA)）。 -/
def trivialBoxModel : HBLTheory where
  S := Prop
  Pr p := p
  imp p q := p → q
  bot := False
  box _ := True
  ax_k _ _ := fun ha _ => ha
  ax_s _ _ _ := fun habc hab ha => habc ha (hab ha)
  mp h ha := h ha
  d1 _ := trivial
  d2 _ _ := fun _ _ => trivial
  d3 _ := fun _ => trivial
  diag φ := ⟨φ, fun hφ _ => hφ, fun h => h trivial⟩

theorem trivialBoxModel_consistent : ¬ trivialBoxModel.Pr trivialBoxModel.bot := fun h => h

/-- 在该模型中，Gödel II 的结论确实成立：一致性陈述不可证。 -/
theorem trivialBoxModel_con_unprovable : ¬ trivialBoxModel.Pr trivialBoxModel.con :=
  trivialBoxModel.goedel_II_consistent trivialBoxModel_consistent

end GodelQ

#print axioms GodelQ.HBLTheory.syl
#print axioms GodelQ.HBLTheory.loeb
#print axioms GodelQ.HBLTheory.goedel_II
#print axioms GodelQ.HBLTheory.goedel_II_consistent
#print axioms GodelQ.HBLTheory.self_consistency_collapse
#print axioms GodelQ.extension_strict
#print axioms GodelQ.trivialBoxModel
#print axioms GodelQ.trivialBoxModel_consistent
#print axioms GodelQ.trivialBoxModel_con_unprovable
