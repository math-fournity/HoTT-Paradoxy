-- CG-009 / Claude 独立方向：Z0 的最小完成门（local D3 at the Gödel sentence）
--
-- 本会话审计 §8.1 发现：Foundation 的第二定理链只在 Gödel 句 G := gödel zfcTr 处
-- 使用一次 D3。本文件把它形式化：
--   * 通用版本：`con_unprovable_of_local_D3` —— 第二定理只需要 G 处的 D3 实例，
--     不需要全称 HBL3；
--   * 实例化：`zfc_z0_full_of_local_D3` —— 最终 Z0 的完整形式只需要一条前提
--     `𝗜𝚺₁ ⊢ zfcTr G 🡒 zfcTr (zfcTr G)`（G 处的一次 D3），而不是对全部 σ 的 ShCraigElim。
import GodelQ.ZFC.Z0Full

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open FFL.FirstOrder.ProvabilityAbstraction.Provability
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

namespace GodelQ.Z0LocalGate

section Generic

variable {L : Language} [L.ReferenceableBy L]
  {T₀ T : Theory L} {𝔅 : Provability T₀ T}
  [Diagonalization T₀] [L.DecidableEq] [T₀ ⪯ T] [Consistent T]

local notation "𝐆" => gödel 𝔅

omit [Diagonalization T₀] [L.DecidableEq] [T₀ ⪯ T] [Consistent T] in
/-- 与 Foundation 的 `formalized_consistent_of_existance_unprovable` 同体，但只要求 `HBL2`。 -/
lemma con_of_unprovable_HBL2 [𝔅.HBL2] {σ : Sentence L} :
    T₀ ⊢ ∼𝔅 σ 🡒 𝔅.con := contra <| mdp D2 <| D1 efq

set_option linter.unusedSectionVars false in
/-- **局部化的 `formalized_unprovable_gödel`**：只使用 G 处的 D3 实例。 -/
theorem formalized_unprovable_gödel_of_local_D3 [𝔅.HBL2]
    (d3G : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆)) : T₀ ⊢ 𝔅.con 🡒 ∼𝔅 𝐆 := by
  suffices T₀ ⊢ ∼𝔅 ⊥ 🡒 ∼𝔅 𝐆 from this
  have h₁ : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆) := d3G
  have h₂ : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆 🡒 ⊥) := 𝔅.mono' <| by cl_prover [gödel_spec (T₀ := T₀)]
  have h₃ : T₀ ⊢ 𝔅 (𝔅 𝐆 🡒 ⊥) 🡒 𝔅 (𝔅 𝐆) 🡒 𝔅 ⊥ := D2
  cl_prover [h₁, h₂, h₃]

/-- **局部化的 `gödel_iff_con`**：只使用 G 处的 D3 实例。 -/
theorem gödel_iff_con_of_local_D3 [𝔅.HBL2]
    (d3G : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆)) : T₀ ⊢ 𝐆 🡘 𝔅.con := by
  have h₁ : T₀ ⊢ ∼𝔅 𝐆 🡒 𝔅.con := con_of_unprovable_HBL2 (𝔅 := 𝔅) (σ := 𝐆)
  have h₂ : T₀ ⊢ 𝔅.con 🡒 ∼𝔅 𝐆 := formalized_unprovable_gödel_of_local_D3 d3G
  have h₃ : T₀ ⊢ 𝐆 🡘 ∼𝔅 𝐆 := gödel_spec
  cl_prover [h₁, h₂, h₃]

/-- **局部化的第二定理**：`T ⊬ 𝔅.con` 只需要 G 处的一次 D3，不需要全称 `HBL3`。 -/
theorem con_unprovable_of_local_D3 [𝔅.HBL2]
    (d3G : T₀ ⊢ 𝔅 𝐆 🡒 𝔅 (𝔅 𝐆)) : T ⊬ 𝔅.con := by
  intro h
  have : T₀ ⊢ 𝐆 🡘 𝔅.con := gödel_iff_con_of_local_D3 d3G
  have : T ⊢ 𝐆 := by cl_prover [h, this]
  exact unprovable_gödel this

end Generic

/-- **最小完成门（实例化）**：最终 Z0 的完整形式，只需要一条前提——
G 处的一次 D3 实例 `zfcTr G 🡒 zfcTr (zfcTr G)`（在 𝗜𝚺₁ 内可证）。
对比 `Z0Full.zfc_z0_full` 需要的全称 `[zfcTr.HBL3]`（对所有 σ）。 -/
theorem zfc_z0_full_of_local_D3
    (d3G : 𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 zfcTr (zfcTr (gödel zfcTr))) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  have hSh : Sh ⊬ zfcTr.con := con_unprovable_of_local_D3 (𝔅 := zfcTr) (T := Sh) d3G
  intro hZ
  have hcon : Sh ⊢ (𝗭𝗙𝗖.consistent : ArithmeticSentence) := (Sh_provable_iff _).mpr hZ
  have e : Sh ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
    WeakerThan.pbl zfcTr_con_iff
  exact hSh (K_right e ⨀ hcon)

/-- 全称 HBL3 蕴含局部前提（门确实更弱；反向无此定理）。 -/
example (h : zfcTr.HBL3) :
    𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 zfcTr (zfcTr (gödel zfcTr)) :=
  h.D3

/-- **把门接到 ShCraigElim 上（只用一个句子！）**：若"Sh.craig 推导消去"只在
Gödel 句 `zfcTr G` 这一个句子上成立（而非对全部 σ），则局部 D3 前提成立。
配合 `zfc_z0_full_of_local_D3`，最终 Z0 的完整形式只欠
**单句实例**：`∀ V, Provable Sh.craig ⌜zfcTr G⌝ → Provable ZFC ⌜translate (zfcTr G)⌝`。
这比所有会话在攻的"全称 ShCraigElim（∀ σ）"弱得多。 -/
theorem local_D3_of_elim_at_godel
    (elim : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      Provable Sh.craig (⌜zfcTr (gödel zfcTr)⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr (gödel zfcTr))⌝ : V)) :
    𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 zfcTr (zfcTr (gödel zfcTr)) := by
  apply complete 𝗜𝚺₁ _
  intro V _ _
  apply Semantics.Imp.models_imply.mpr
  intro hp
  -- V ⊧ zfcTr G ⇒ Provable Sh.craig ⌜zfcTr G⌝（即骨架的 step1，免费）
  have hP : Provable Sh.craig (⌜zfcTr (gödel zfcTr)⌝ : V) :=
    Bootstrapping.Arithmetic.sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 (gödel zfcTr)) hp
  -- elim 单句实例 ⇒ V ⊧ zfcTr (zfcTr G)
  exact (models_zfcTr_iff V (zfcTr (gödel zfcTr))).mpr (elim V hP)

/-- **闭环：单句消去 ⇒ 最终 Z0。** 组合 `local_D3_of_elim_at_godel` 与
`zfc_z0_full_of_local_D3`：最终 Z0 的完整形式只欠一条单句前提——
`∀ V ⊨ 𝗜𝚺₁, Provable Sh.craig ⌜zfcTr G⌝ → Provable ZFC ⌜translate (zfcTr G)⌝`
（G := gödel zfcTr 这一个句子），而非全称的 `ShCraigElim`（∀ σ）。 -/
theorem zfc_z0_full_of_elim_at_godel
    (elim : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      Provable Sh.craig (⌜zfcTr (gödel zfcTr)⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr (gödel zfcTr))⌝ : V)) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  zfc_z0_full_of_local_D3 (local_D3_of_elim_at_godel elim)

/-- elim@G 蕴含 bwd@G：经 fwd（`Provable ZFC (translate G) ⇒ V ⊧ zfcTr G ⇒ Provable Sh.craig ⌜zfcTr G⌝`）。
即下面的 bwd@G 门不比 elim@G 强。 -/
theorem bwd_at_godel_of_elim_at_godel
    (elim : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      Provable Sh.craig (⌜zfcTr (gödel zfcTr)⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr (gödel zfcTr))⌝ : V)) :
    ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (gödel zfcTr)⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr (gödel zfcTr))⌝ : V) := by
  intro V _ _ hV
  have hmod : V↓[ℒₒᵣ] ⊧ zfcTr (gödel zfcTr) := (models_zfcTr_iff V (gödel zfcTr)).mpr hV
  exact elim V (Bootstrapping.Arithmetic.sigma_one_complete (T := Sh.craig)
    (zfcTr_sigma1 (gödel zfcTr)) hmod)

/-- **最尖的最小门（bwd@G）**：前提不再经过 `Sh.craig`——直接是 G 处的一次反向蕴含
（"V 认为 ZFC 证明了 translate G ⇒ V 认为 ZFC 证明了 translate(zfcTr G)"），
且该前提被 elim@G 蕴含（`bwd_at_godel_of_elim_at_godel`）。
最终 Z0 的完整形式只欠这一个单句、单方向、跨非标准模型的实例。 -/
theorem zfc_z0_full_of_bwd_at_godel
    (h : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (gödel zfcTr)⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr (gödel zfcTr))⌝ : V)) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  apply zfc_z0_full_of_local_D3
  apply complete 𝗜𝚺₁ _
  intro V _ _
  apply Semantics.Imp.models_imply.mpr
  intro hp
  exact (models_zfcTr_iff V (zfcTr (gödel zfcTr))).mpr
    (h V ((models_zfcTr_iff V (gödel zfcTr)).mp hp))

/-- **单句反向桥 ⇒ d3G**：`provabilityPred Sh.craig (zfcTr G) 🡒 zfcTr (zfcTr G)` 在 𝗜𝚺₁ 中可证
（bd4295b5 的 `hbl3_of_reverse_on_image` 的门，但**只在 G 一个句子**上），配 fwd（免费）即得 d3G。 -/
theorem d3G_of_reverse_at_godel
    (bridge : 𝗜𝚺₁ ⊢ provabilityPred Sh.craig (zfcTr (gödel zfcTr)) 🡒 zfcTr (zfcTr (gödel zfcTr))) :
    𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 zfcTr (zfcTr (gödel zfcTr)) :=
  C_trans (provable_sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 (gödel zfcTr))) bridge

/-- **单句反向桥 ⇒ 最终 Z0**（bd4295b5 家族在单句上的最弱版本）。 -/
theorem zfc_z0_full_of_reverse_at_godel
    (bridge : 𝗜𝚺₁ ⊢ provabilityPred Sh.craig (zfcTr (gödel zfcTr)) 🡒 zfcTr (zfcTr (gödel zfcTr))) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  zfc_z0_full_of_local_D3 (d3G_of_reverse_at_godel bridge)

/-- **单句 `keyE` ⇒ 最终 Z0**：规范形状的 `keyE`（追踪文档里的"唯一缺口"）
只需要在**一个句子** `zfcTr G` 处成立：
`𝗜𝚺₁ ⊢ zfcTr (zfcTr G) 🡘 provabilityPred Sh.craig (zfcTr G)`。
经 `K_right` 得单句反向桥，再走上面的链。 -/
theorem zfc_z0_full_of_keyE_at_image
    (keyE : 𝗜𝚺₁ ⊢ zfcTr (zfcTr (gödel zfcTr)) 🡘 provabilityPred Sh.craig (zfcTr (gödel zfcTr))) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
  zfc_z0_full_of_reverse_at_godel (K_right keyE)

/-! ## 缺口周围的免费事实（把剩余缺口钉成一个单句蕴含）

整个剩余缺口 = `gateG : 𝗜𝚺₁ ⊢ □Craig(zfcTr G) 🡒 zfcTr(zfcTr G)`（单句、单方向）。
下面三条是围绕它的免费事实，全部机器核过：
* `fwd_at_G`：`zfcTr G → □Craig(zfcTr G)`（Σ1 完全性，免费）；
* `craig_D3_at_image`：`□Craig(zfcTr G) → □Craig(□Craig(zfcTr G))`（Sh.craig 的 D3 在该句的实例，免费）；
* `gate_of_elim_at_godel`：单句消去（elim@G）⇒ gateG（即：若全称消去成功，本门自动关闭）。 -/

/-- fwd 在 τ := G 的实例（免费）：`zfcTr G → □Craig(zfcTr G)`。 -/
theorem fwd_at_G :
    𝗜𝚺₁ ⊢ zfcTr (gödel zfcTr) 🡒 provabilityPred Sh.craig (zfcTr (gödel zfcTr)) :=
  provable_sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 (gödel zfcTr))

/-- Sh.craig 标准可证性的 D3 在句子 `zfcTr G` 处的实例（免费，来自 `inferInstance` 的 HBL3）。 -/
theorem craig_D3_at_image :
    𝗜𝚺₁ ⊢ provabilityPred Sh.craig (zfcTr (gödel zfcTr)) 🡒
      provabilityPred Sh.craig (provabilityPred Sh.craig (zfcTr (gödel zfcTr))) :=
  haveI : (Sh.craig.standardProvability).HBL3 := inferInstance
  D3 (𝔅 := Sh.craig.standardProvability)

/-- elim@G ⇒ gateG（单句反向桥）。 -/
theorem gate_of_elim_at_godel
    (elim : ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      Provable Sh.craig (⌜zfcTr (gödel zfcTr)⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr (gödel zfcTr))⌝ : V)) :
    𝗜𝚺₁ ⊢ provabilityPred Sh.craig (zfcTr (gödel zfcTr)) 🡒 zfcTr (zfcTr (gödel zfcTr)) := by
  apply complete 𝗜𝚺₁ _
  intro V _ _
  apply Semantics.Imp.models_imply.mpr
  intro h
  have hP : Provable Sh.craig (⌜zfcTr (gödel zfcTr)⌝ : V) := by
    rw [models_iff] at h
    simpa [provabilityPred,
      (inferInstance : 𝚺ᴬ₁-Predicate (Provable Sh.craig : V → Prop) via (provable Sh.craig)).iff] using h
  exact (models_zfcTr_iff V (zfcTr (gödel zfcTr))).mpr (elim V hP)

/-! ## 第二个单句面：⊥ 门（影子形式路线）

与 G 门并列的另一条单句收缩：`gateBot : 𝗜𝚺₁ ⊢ □Craig(⊥) 🡒 zfcTr ⊥`。
两条都只欠"单句反向蕴含"，且承载同一核心内容（Craig 证书桥在该句实例上）。
本文件给出 ⊥ 门的无 cl_prover、无 change 的修复写法（BottomStage2 结论的固化）。 -/

/-- **⊥ 门 ⇒ 最终 Z0**（bd4295b5 `zfc_z0_full_of_reverse_at_bottom` 的修复写法：
`contra` 显式 MP 替代 `cl_prover`，去掉两行导致 elaboration 超时的 `change`）。 -/
theorem zfc_z0_full_of_gate_bot
    (bridge : 𝗜𝚺₁ ⊢ provabilityPred Sh.craig (⊥ : ArithmeticSentence) 🡒 zfcTr ⊥) :
    𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence) := by
  intro h
  have hz : Sh ⊢ (𝗭𝗙𝗖.consistent : ArithmeticSentence) := (Sh_provable_iff _).mpr h
  have he : Sh ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent : ArithmeticSentence) :=
    WeakerThan.pbl zfcTr_con_iff
  have hp : Sh ⊢ zfcTr.con := K_right he ⨀ hz
  have hb : Sh ⊢ provabilityPred Sh.craig (⊥ : ArithmeticSentence) 🡒 zfcTr ⊥ :=
    WeakerThan.pbl bridge
  have hc : Sh ⊢ Sh.craig.consistent.val :=
    contra hb ⨀ hp
  exact craig_consistent_unprovable_of_RE Sh hc

/-- **等价闭环：gateG ⇒ elim@G**。把门在任意 `V ⊨ 𝗜𝚺₁` 上实例化，即得单句消去。
配合 `gate_of_elim_at_godel`（elim@G ⇒ gateG），二者完全等价——
**整个剩余缺口 = 单句消去 elim@G = 单句门 gateG**，三者是同一件事的三个名字。 -/
theorem elim_at_godel_of_gate
    (gate : 𝗜𝚺₁ ⊢ provabilityPred Sh.craig (zfcTr (gödel zfcTr)) 🡒 zfcTr (zfcTr (gödel zfcTr))) :
    ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
      Provable Sh.craig (⌜zfcTr (gödel zfcTr)⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr (gödel zfcTr))⌝ : V) := by
  intro V _ _ h
  have hmod : V↓[ℒₒᵣ] ⊧ provabilityPred Sh.craig (zfcTr (gödel zfcTr)) := by
    rw [models_iff]
    simpa [provabilityPred,
      (inferInstance : 𝚺ᴬ₁-Predicate (Provable Sh.craig : V → Prop) via (provable Sh.craig)).iff] using h
  have hgate : V↓[ℒₒᵣ] ⊧ (provabilityPred Sh.craig (zfcTr (gödel zfcTr)) 🡒
      zfcTr (zfcTr (gödel zfcTr))) :=
    models_of_provable (L := ℒₒᵣ) inferInstance gate
  have h2 : V↓[ℒₒᵣ] ⊧ zfcTr (zfcTr (gödel zfcTr)) :=
    Semantics.Imp.models_imply.mp hgate hmod
  simpa using (models_zfcTr_iff V (zfcTr (gödel zfcTr))).mp h2

/-! ## 正对照：门在标准模型 ℕ 上成立（非标准模型才是全部困难所在） -/

/-- **`gateG_standard`**：门 `□Craig(zfcTr G) → zfcTr(zfcTr G)` 在 ℕ 上成立。
链：ℕ 中的 `□Craig(zfcTr G)` 是标准编码 ⇒ `provable_iff_provable` 降元层（`Sh.craig` 定理）⇒
`Sh.craig ⪯ Sh` 弱化 ⇒ `Sh_provable_iff` 转 ZFC 定理 ⇒ `internalize_provability` 回 ℕ 编码 ⇒
`models_zfcTr_iff` 收口。这说明门不是假的；其困难全部在非标准 V。 -/
theorem gateG_standard :
    ℕ↓[ℒₒᵣ] ⊧ (provabilityPred Sh.craig (zfcTr (gödel zfcTr)) 🡒
      zfcTr (zfcTr (gödel zfcTr))) := by
  rw [Semantics.Imp.models_imply]
  intro h
  have hP : Provable Sh.craig (⌜zfcTr (gödel zfcTr)⌝ : ℕ) := by
    rw [models_iff] at h
    simpa [provabilityPred,
      (inferInstance : 𝚺ᴬ₁-Predicate (Provable Sh.craig : ℕ → Prop) via (provable Sh.craig)).iff] using h
  have hD : Sh.craig ⊢ zfcTr (gödel zfcTr) := (provable_iff_provable (T := Sh.craig)).mp hP
  have hS : Sh ⊢ zfcTr (gödel zfcTr) :=
    Entailment.weakerThan_iff.mp (inferInstance : Sh.craig ⪯ Sh) hD
  have hZ : 𝗭𝗙𝗖 ⊢ arithTrln.translate (zfcTr (gödel zfcTr)) := (Sh_provable_iff _).mp hS
  exact (models_zfcTr_iff ℕ (zfcTr (gödel zfcTr))).mpr (internalize_provability (V := ℕ) hZ)

end GodelQ.Z0LocalGate

#print axioms GodelQ.Z0LocalGate.con_unprovable_of_local_D3
#print axioms GodelQ.Z0LocalGate.zfc_z0_full_of_local_D3
#print axioms GodelQ.Z0LocalGate.local_D3_of_elim_at_godel
#print axioms GodelQ.Z0LocalGate.zfc_z0_full_of_elim_at_godel
#print axioms GodelQ.Z0LocalGate.bwd_at_godel_of_elim_at_godel
#print axioms GodelQ.Z0LocalGate.zfc_z0_full_of_bwd_at_godel
#print axioms GodelQ.Z0LocalGate.d3G_of_reverse_at_godel
#print axioms GodelQ.Z0LocalGate.zfc_z0_full_of_reverse_at_godel
#print axioms GodelQ.Z0LocalGate.zfc_z0_full_of_keyE_at_image
#print axioms GodelQ.Z0LocalGate.fwd_at_G
#print axioms GodelQ.Z0LocalGate.craig_D3_at_image
#print axioms GodelQ.Z0LocalGate.gate_of_elim_at_godel
#print axioms GodelQ.Z0LocalGate.zfc_z0_full_of_gate_bot
#print axioms GodelQ.Z0LocalGate.gateG_standard
