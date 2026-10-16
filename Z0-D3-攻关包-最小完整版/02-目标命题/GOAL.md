# 目标命题（逐字）

文件：`GodelQ/ZFC/Z0Blocked.lean`（`02-目标命题/Z0Blocked.lean` 是同件拷贝，含一个修复见下）。

```lean
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

（**修复**：本包拷贝已补上 `open GodelQ.Z0Full` 一刀——repo 原版缺这一行导致 `zfcTr` 无法解析。
该文件一直带 `sorry`、从没收进过收据源，所以这个 bug 没被发现。第 20 行。）

## 读法

- `V` 是算术理论 `𝗜𝚺₁` 的任意模型（**可能非标准**）；
- `Provable 𝗭𝗙𝗖 φ` 即 `∃ d, Proof 𝗭𝗙𝗖 d φ`——V 中存在一个 ZFC 推导编码 d 推出 φ；
- `σᵗ := arithTrln.translate σ` 是算术句 σ 到集合论的**直接翻译**；
- `zfcTr σ := trProv.val/[⌜σ⌝]`，其中 `trProv := "x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y"` 是一个 Σ1 公式。

## 为什么是它

它是 Hilbert–Bernays 可导性条件 **D3** 在这个显式可证性谓词 `𝔅Z(x) := Provable 𝗭𝗙𝗖 (iT 0 x)` 下的形状，
即**经翻译的形式化 Σ1 完全性**。

`Z0Full.zfc_z0_full_of_D3_internalize`（`02-目标命题/Z0Full-tail-excerpt.txt` 摘了证明尾段，已过核、无 `sorry`）
表明：这条引理一旦成立，完整形式 `𝗭𝗙𝗂 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)` 立即随之成立。

## 已就绪的正反两面

- `Z0Full.zfc_z0_full_of_D3_internalize`：无未证标记，已过核。引理一旦成立完整形式立即成立。
- `Z0Full.zfcTr_D3_standard`：D3 在标准模型 ℕ 中成立的**正对照**（同一运行内机器核对过）。

## 阻塞引理在极小形式下的形状

`Z0Full.lean:117` 的 `zfc_z0_full_of_D3_internalize` 把引理写成
`∀ (V : Type) ... (τ) , Provable 𝗭𝗙𝗂 ⌜translate τ⌝ → Provable 𝗭𝗙𝗂 ⌜translate (zfcTr τ)⌝`，
即它消费的是 `V : Type` 层。目标引理写的是 `V : Type*`。
**建议你把要证的版本降成 `V : Type`**（够 C-122 用，少一层宇宙麻烦）；若想保留 `Type*`，
需先把 `models_zfcTr_iff`/`models_trProv_iff` 从 `Type` 推广。
