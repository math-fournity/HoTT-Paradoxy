import GodelQ.ZFC.Z0Full

/-!
# 实证尝试：用 `internalize_provability` 关闭 `zfcTr_D3_internalize` 是否可行

本文件是一次**失败但信息量充足**的实证尝试，用来精确刻画 Z0 的唯一缺口
`zfcTr_D3_internalize`（`Z0Blocked.lean` 中的 `sorry`）。

目标命题：
```
zfcTr_D3_internalize {V} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (τ) (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V))
  : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```
两端都是**外部**的 `Provable 𝗭𝗙𝗖 (…)`（与模型 V 无关，V 只是占位参数）；
由 `iT_quote` 可知 `⌜arithTrln.translate τ⌝ = iT 0 ⌜τ⌝`，所以前提即 `𝗭𝗙𝗖 ⊢ arithTrln.translate τ`。

结论句 `arithTrln.translate (zfcTr τ)` 是把 Σ1 算术句
`zfcTr τ = “∃ y, iTDef y 0 code(τ) ∧ provable 𝗭𝗙𝗖 y”`
翻译成集合论句，它断言“𝗭𝗙𝗖 证明了 τ 的翻译”。
而前提句 `arithTrln.translate τ` 是 τ 的翻译本身。两句话**不同**：
结论是前提句的“内部化证明编码”版本（经 `iTDef` + `provable 𝗭𝗙𝗖` 包裹）。

`internalize_provability {φ} : T ⊢ φ → Provable T (⌜φ⌝ : V)` 对任意 `[T.Δ₁]` 的理论 T
（包括 `𝗭𝗙𝗖`，见 `ZFCDelta1.ZFC.delta1`）都成立；它把**外部**证明 `𝗭𝗙𝗖 ⊢ φ`
重写成内部派生 `𝗭𝗙𝗖.internalize V ⊢ ⌜φ⌝`，但只能产生**同一句** `⌜φ⌝` 的内部形式，
绝不能凭空合成“包裹了 `iTDef` + `provable 𝗭𝗙𝗖` 的”结论句。

因此下面的 `exact internalize_provability (V := V) h` 给出**类型不匹配**错误，
正好从实证上说明：仅凭 `internalize_provability` 无法关闭缺口；要得到结论句，
必须让 𝗭𝗙𝗖 在其**内部**对自身编码（`iTDef`、`provable 𝗭𝗙𝗖`）做 Σ1 推理——
即 𝗭𝗙𝗖 的**内部化 Σ1 完全性 / 反射**（可推导性条件 D3 对集合论版本），
而 Foundation 只提供**算术理论**的 `sigma_one_complete`（`D3.lean`），
对集合论没有对应物（已在 `LK/`、`SetTheory/` 中确认搜索无结果）。

这正是前两个 AI 会话与审计所声称的“实缺口”的精确形式：缺口不在语法包装，
而在 𝗭𝗙𝗖 的**内部化** Σ1 完全性尚未在 Foundation 中被形式化。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Z0Full GodelQ.ZFCArith GodelQ.ZFCZ0

namespace GodelQ.Z0D3Attempt

-- 实证：把 `internalize_provability` 直接喂给结论，预期得到类型不匹配（两句话不同）。
theorem zfcTr_D3_internalize_attempt {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  -- 前提 h : 𝗭𝗙𝗖 ⊢ arithTrln.translate τ（由 iT_quote 等价）。
  -- internalize_provability 只把同一句重写，无法合成包裹后的结论句。
  -- 这一步会失败并报告：目标句是 `… translate (zfcTr τ) …`，而项类型是 `… translate τ …`。
  exact internalize_provability (V := V) h
