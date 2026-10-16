# 目标命题（逐字）与归约链

## 唯一阻塞引理（当前带 sorry）

文件 `07-项目模块/GodelQ/ZFC/Z0Blocked.lean`：

```lean
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  sorry
```

## 已证好的归约链（无需你重做）

```
ShCraigElim  (本缺口，待证)
   → bwd_of_shcraig_elim   (Z0UniBridge.lean, C-390, 已收据)
   → bwd
   → keyE
   → zfcTr_D3_internalize  (Z0Blocked.lean, 当前带 sorry 的那条)
   → zfc_z0_full_of_D3_internalize  (Z0Full.lean, C-122, 已收据)
   → 𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)
```

即：证完 `ShCraigElim`，主线"形式化与机器证明"即彻底完成（Z0 完整形式成立）。

## ShCraigElim 的精确形状（你要写出来的定理）

```lean
-- 新文件：GodelQ/ZFC/ShCraigElim.lean
theorem ShCraigElim {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (σ : ArithmeticSentence) (h : Provable Sh.craig (⌜σ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) := by
  -- 对 Sh.craig 的推导编码 d 做 Derivation.induction1，把 10 个规则支都填成无 sorry 引理
```

`Sh.craig` 由 Foundation 直接 `inferInstance` 给出完整 D3（无需你重做 Craig 填充的 D3）。
你只需把 `Sh.craig` 的一条推导编码沿内部翻译 `iT` 结构归纳消去成 `𝗭𝗙𝗖` 推导编码。
