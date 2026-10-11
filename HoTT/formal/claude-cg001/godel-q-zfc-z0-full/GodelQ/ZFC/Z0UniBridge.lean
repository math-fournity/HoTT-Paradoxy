import GodelQ.ZFC.Z0Full

/-!
# CG-007 · W8 续：`bwd` 的宇宙层级障碍已清除，缺口缩为一条消去

`Z0Blocked.lean` 的目标定理写的是 `{V : Type*}`，而项目里现成的两条桥
（`models_trProv_iff`、`models_zfcTr_iff`，`Z0Full.lean:54/:67`）都锁在 `V : Type`。
于是 `rw [models_zfcTr_iff]` 在目标定理的宇宙下**直接失败**：

```
error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
  Semantics.Models.{1, 0} ?V↓[ℒₒᵣ] (↑zfcTr ?σ)
in the target expression
  Semantics.Models.{u_1 + 1, 0} V↓[ℒₒᵣ] (↑zfcTr (↑zfcTr σ))
```

本文件给出宇宙多态的替代 `models_zfcTr_iff'`（无新假设，只是把同一条证明
写成 `V : Type*`），并把 `bwd` 精确归约为**一条消去**：

> `Provable Sh.craig ⌜σ⌝ (V) → Provable 𝗭𝗙𝗖 ⌜translate σ⌝ (V)`

这一条就是 D3 的实质内容（`of_provability` 是语义的，搬不进非标准 V）。
本文件**不证**这条消去；它只证明：除此以外，`bwd` 的所有零件都已就位。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

namespace GodelQ.Z0UniBridge

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **宇宙多态的 `models_zfcTr_iff`**：项目自带的版本锁在 `V : Type`，
这条对 `V : Type*` 成立——正是目标定理需要的那个宇宙。

证法同 `Z0Full.models_zfcTr_iff`，只是不经过 `(V : Type)` 的限制：
`zfcTr_def` 把 `zfcTr σ` 化成 `trProv.val/[⌜σ⌝]`，
再走宇宙多态的 `trProvable_quote` 与 `models_iff`。 -/
lemma models_zfcTr_iff' (σ : ArithmeticSentence) :
    (V ↓[ℒₒᵣ] ⊧ zfcTr σ) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) := by
  rw [zfcTr_def, ← trProvable_quote]
  simp [models_iff]

end GodelQ.Z0UniBridge

/-- **`Sh.craig` 推导消去**：D3 的实质内容，固定在一个宇宙里便于传递。 -/
abbrev ShCraigElim (V : Type*) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] : Prop :=
  ∀ (σ : ArithmeticSentence),
    Provable Sh.craig (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

namespace GodelQ.Z0UniBridge

/-- **缺口归约**：给定消去假设，`bwd` 立即成立。

两侧的零件：
* 结论侧 `V ⊧ zfcTr (zfcTr σ)` 经 `models_zfcTr_iff'` 变成
  `Provable 𝗭𝗙𝗖 ⌜translate (zfcTr σ)⌝`；
* 假设侧 `V ⊧ provabilityPred Sh.craig (zfcTr σ)` 经 `models_iff` 变成
  `Provable Sh.craig ⌜zfcTr σ⌝`。

中间的桥正是 `elim`。 -/
lemma bwd_of_shcraig_elim {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (elim : ShCraigElim V)
    (σ : ArithmeticSentence)
    (h : V ↓[ℒₒᵣ] ⊧ ↑(provabilityPred (Theory.craig Sh) (zfcTr σ))) :
    V ↓[ℒₒᵣ] ⊧ ↑(zfcTr (zfcTr σ)) := by
  rw [models_zfcTr_iff']
  apply elim
  rw [models_iff] at h
  simpa using h

end GodelQ.Z0UniBridge

#print axioms GodelQ.Z0UniBridge.models_zfcTr_iff'
#print axioms GodelQ.Z0UniBridge.bwd_of_shcraig_elim
