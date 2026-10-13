import GodelQ.ZFC.CG008HD3

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008HD3Real

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HD3

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # `hD3G` 的环：每一步的机器化引理

**环**（`H : 𝗜𝚺₁ ⊢ zfcTr sigma`，要 `𝗜𝚺₁ ⊢ zfcTr (zfcTr sigma)`）：

```
H  →(可靠性)  V ⊧ zfcTr sigma
   →(models_trProv_iff)  Provable 𝗭𝗙𝗖 ⌜translate sigma⌝
   →(C，缺)          Provable 𝗭𝗙𝗖 ⌜translate (zfcTr sigma)⌝
   →(ring_step3，缺) 𝗭𝗙𝗖 ⊢ translate (zfcTr sigma)
   →(Sh_provable_iff) Sh ⊢ (zfcTr sigma)
   →(zfcTr.D1)      𝗜𝚺₁ ⊢ zfcTr (zfcTr sigma)
```

**所以 `hD3G` 需要两条搬运，不是一条**：

* **C**（= 002-Flash 的 `MinimalGap`）：V 内「有 `translate sigma` 的推导码」
  ⟹ V 内「有 `translate (zfcTr sigma)` 的推导码」——**V 内到 V 内**；
* **ring_step3**：V 内「有推导码」⟹ **元层** `𝗭𝗙𝗖 ⊢ …`。

第二条正是 012-Flash 报的**方向 2 危险**：V 非标准时 `Evalb` 的见证可能非标准
（`codeOfPartrec'_spec` 仅 `ℕ`；模型层 `code`/`code_uniq` 只给唯一性）。

**注意**：ring_step3 里的码是 `⌜translate (zfcTr sigma)⌝`，是**标准码**，
所以这一条或可由 `Provable.complete` 的 `ℕ` 版加标准码搬移得到——尚未证。

**治理**：本文件只记查实与形状，不含未证标记。 -/

/-- **环步 1**：`sigma ∈ Sh.craig` ⟹ `𝗭𝗙𝗖 ⊢ translate sigma`（元层）。 -/
theorem ring_step1 (sigma : ArithmeticSentence) (h : sigma ∈ Sh.craig) :
    𝗭𝗙𝗖 ⊢ arithTrln.translate sigma := by
  have h1 : Sh.craig ⊢ sigma := by_axm h
  have h2 : Sh ⊢ sigma := (inferInstance : Sh.craig ⪯ Sh).wk h1
  exact (Sh_provable_iff sigma).mp h2

/-- **环步 2**：元层 `𝗭𝗙𝗖 ⊢ translate sigma` ⟹ V 内 `TrProvable ⌜sigma⌝`。

走 `internalize_provability`（`D1.lean:27`，载体多态）+ `iT_quote`。
**这一条是本轮已证的**，它给出「元层 ⟹ V 内编码」的方向。 -/
theorem ring_step2 (sigma : ArithmeticSentence) (h : 𝗭𝗙𝗖 ⊢ arithTrln.translate sigma) :
    TrProvable (⌜sigma⌝ : V) := by
  rw [TrProvable]
  have heq : iT (0 : V) (⌜sigma⌝ : V) =
      ⌜(arithTrln.translate sigma : Semisentence ℒₛₑₜ 0)⌝ := iT_quote (V := V) sigma
  rw [heq]
  exact internalize_provability (T := 𝗭𝗙𝗖) (V := V) h

/-- **环步 3（缺，= C 之外的第二条搬运）**：V 内「有推导码」⟹ 元层 `𝗭𝗙𝗖 ⊢ …`。

本文件只把形状钉住，**不声称已证**。 -/
def ring_step3 : Prop :=
  ∀ (sigma : ArithmeticSentence),
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate sigma⌝ : V) → 𝗭𝗙𝗖 ⊢ arithTrln.translate sigma

end GodelQ.CG008HD3Real
