# 目标命题与归约链（逐字）

## 1. 最终目标

主线“形式化与机器证明”的全部前提都已证，只差 D3（Hilbert–Bernays 第三可导性条件，
即形式化 Σ1 完全性）这一条。固定写成：

```lean
-- Z0Blocked.lean（当前带 sorry，是唯一的阻塞引理）
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  sorry
```

读作：在 𝗜𝚺₁ 的每个模型 V 中，若 𝗭𝗙𝗖 证明了 τ 的翻译，则 𝗭𝗙𝗖 也证明“𝗭𝗙𝗖 证明 τ 的翻译”
这句话的翻译。`zfcTr τ := trProv.val/[⌜τ⌝]`，`trProv` 是 Σ1 公式。

## 2. 归约链（全部已证，引用即成立）

| 环节 | 文件 | 状态 |
|---|---|---|
| `zfc_z0_full_of_D3_internalize`：D3 => Z0 完整形式 | Z0Full.lean | 已证（无 sorry） |
| `zfcTr_D3_internalize_of_bridge'`（C-128） | Z0Bridge.lean | 已证 |
| `bwd_of_shcraig_elim`（C-390）宇宙多态桥 | Z0UniBridge.lean | 已证 |
| `ShCraigElim`：Sh.craig 的 V 内推导编码翻成 ZFC 推导编码 | （待建） | 待证 |

```lean
-- Z0UniBridge.lean
abbrev ShCraigElim (V) [..] : Prop :=
  ∀ (σ : ArithmeticSentence),
    Provable Sh.craig (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)
```

一旦证出无 sorry 的 ShCraigElim，Z0Blocked.lean 的 sorry 改为
`exact bwd_of_shcraig_elim elim σ h`，整条链闭合。

## 3. 为什么 Foundation 的现成工具填不上

- `of_provability`（Foundation/.../LK/Interpretation.lean:443）经完备性定理语义地得到
  `U ⊢ σ → T ⊢ π.translate σ`；它不给“证明编码上的可计算函数”，搬不进非标准 V。
- `provable_internalize`（DerivabilityCondition/D3.lean）只对算术理论 T:ArithmeticTheory；
  ZFC 不是算术理论，不能直接套。
- `sigma_one_complete` 给的是 Provable 𝗜𝚺₁ 编码，我们要的是 Provable 𝗭𝗙𝗖 编码；两者无现成桥。

结论：必须对 Sh.craig 的推导结构做归纳消去——这正是 ShCraigElim。
Foundation 对 Sh.craig 直接 inferInstance 给出 D3，但那是对“算术理论”的；我们要的是跨到 ZFC 的那一步。
