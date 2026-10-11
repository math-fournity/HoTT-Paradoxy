# R-新 实测要点（2026-10-10）

## 已确认可用
- 环境：/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0（1893 模块，完整）
- 基线：24 模块全 exit 0，约 60 秒
- C-128 归约（Z0Bridge.lean）exit 0
- tprovable_iff_provable（Typed.lean:168）:
    T.internalize V ⊢ σ ↔ Provable T σ.val     [T.Δ₁]
  → Provable ZFC ⌜translate σ⌝ ↔ ZFC.internalize V ⊢ ⌜translate σ⌝
- L2 四层命题规则全部 rfl/simp 落地
- ZFC ⊢ Theory.Eq.refl ℒₛₑₜ 可由 𝗘𝗤 _ ⪯ 𝗭𝗙𝗖 + by_axm 得到
- 𝗣𝗔 ⪯ Sh（Z0PA.lean:24）、𝗜𝚺₁ ⪯ Sh（:28）均为现成 instance

## 唯一障碍
- Sh.Δ₁ 无实例。Theory.Δ₁ 要三条字段（Syntax/Theory.lean:16）：
    ch : 𝚫ᴬ₁.Semisentence 1
    mem_iff : ∀ φ, ℕ ⊧/![⌜φ⌝] ch.val ↔ ∃ σ ∈ T, φ = σ
    isDelta1 : ch.ProvablyProperOn 𝖨Σ₁
- trProv 已是 Σ1 公式（zfcTr_sigma1, C-121）→ ch 的 Σ1 半边现成

## R-新 计划
1. 构造 Sh.Δ₁.ch = trProv 的 𝚫ᴬ₁ 对（Σ1 = trProv，Π1 = 其补）
2. mem_iff：用 internalize_provability + Provable.complete
3. isDelta1：最重，与形式化 Σ1 完全性纠缠
4. 得 sigma_one_complete (T := Sh) → Bridge′ → D3 → Z0 完整形式
