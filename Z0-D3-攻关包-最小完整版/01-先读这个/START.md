# START：60 秒版

## 目标（一条 Lean 引理）

```lean
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗂 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

读作：**ZFC 证明了 τ 的翻译，那么 ZFC 也能证明"ZFC 证明了 τ 的翻译"这句话的翻译。**
这是 Hilbert–Bernays 条件 D3 在显式谓词 `zfcTr` 下的形状（= 经翻译的形式化 Σ1 完全性）。

## 它为什么重要

`Z0Full.zfc_z0_full_of_D3_internalize`（已过核、无 sorry）以它为唯一显式前提给出完整形式：
`ZFC ⊬ arithTrln.translate (ZFC.consistent)`。引理一旦证明，Z0 的完整形式立即成立，不需要别的东西。

## 我实测到的新局面（这是本包的核心增量）

Foundation 在 `Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean` 里证完了算术理论的 D3，
其产物是：

```lean
theorem sigma_one_complete {V} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {T} [T.Δ₁] [𝗣𝗔⁻ ⪯ T]
    {σ : ArithmeticSentence} (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ)
    (h : V↓[ℒₒᵣ] ⊧ σ) : Provable T (⌜σ⌝ : V)
```

即 **"真 Σ1 句 → V 中存在推导编码"**，目标理论随便换。我本机实测：

- `Sh.RE`（C-119 已是 instance）⟹ Foundation 的 `Theory.craig` 实例 给出 `Sh.craig.Δ₁`；
- `𝗣𝗔⁻ ⪯ Sh.craig` 可合成；
- `Sh.craig ⪯ Sh` 与 `Sh ⪯ Sh.craig` 都可合成（故 `Sh.craig.standardProvability.HBL3` 由 `inferInstance` 直接得到）；
- 于是 `Bootstrapping.Arithmetic.sigma_one_complete (T := Sh.craig)` **可用**，我已写成 `Z0D3Skeleton.step1` 并编译通过：
  `V ⊧ zfcTr σ → Provable Sh.craig ⌜zfcTr σ⌝`。

## 缺口的精确方向（2026-10-10 晚，本机进一步实测，**最新**）

缺口已压缩到**一条引理的一个方向**。记 Foundation 的标准可证性谓词
`provabilityPred Sh.craig σ`。

### 已证的一端（免费，本机实测 exit 0，无 `sorry`）

```lean
theorem fwd (τ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ (↑(zfcTr τ) 🡒
      (↑(provabilityPred (Theory.craig Sh) (zfcTr τ)) : Sentence ℒₒᵣ)) :=
  FFL.FirstOrder.Arithmetic.provable_sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 τ)
```

这就是 Foundation 的 `provable_sigma_one_complete`：`zfcTr τ` 是 Σ1 句
（`zfcTr_sigma1` 已证），所以 `𝗜𝚺₁ ⊢ zfcTr τ 🡒 provabilityPred Sh.craig (zfcTr τ)`
现成。**没有任何新工作。**

### 缺的另一端（= D3 本身，唯一缺口）

```lean
lemma bwd {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (σ : ArithmeticSentence)
    (h : V ↓[ℒₒᵣ] ⊧ ↑(provabilityPred (Theory.craig Sh) (zfcTr σ))) :
    V ↓[ℒₒᵣ] ⊧ ↑(zfcTr (zfcTr σ)) := by
  rw [models_zfcTr_iff]   -- 目标变成 Provable 𝗭𝗙𝗖 ⌜(zfcTr σ)ᵗ⌝
  sorry
```

读作："V 中有一条 `Sh.craig` 推导" ⊢ "V 中有一条 `𝗭𝗙𝗖` 推导"。

**为什么它是实的**：`h` 给的是 V 中的 `Sh.craig` 推导编码 `d`，目标要 V 中的 `𝗭𝗙𝗖`
推导编码。`d` 在非标准 V 中可能对应非标准推导；Foundation 的 `Provable.sound` /
`provable_iff_provable` 只在 **ℕ 层** 给 `Provable T ⌜σ⌝ ⊢ ⊢`。
跨过这一步的数学内容等于 D3，不是 Lean 工程细节。

**已确认不可用的入口**（都实测过）：
- `Provable T ⌜σ⌝ (V) ⊢ T ⊢ σ` 的一般 V 版：不存在（`Provable.sound` 锁 ℕ）。
- Σ1 向上绝对（`sigmaOne_upward_absolute`）只给 `ℕ → V`；反向是 `piOne_downward_absolute`（Π1）。
- `Sh.Δ₁`（不是 `Sh.craig.Δ₁`）会循环，见 `03-可用的已证引理/API.md` §E。
- `Sh.Δ₁` 取 `ch := trProv`：`ProperOn` 要求 `trProv ↔ ¬trProv`，假。
- 给 `Provable 𝗭𝗙𝗖 x` 找有界形式：对 Sh 这样的界不存在（否则 Sh 可判定）。

## 骨架文件（最新，本机 exit 0）

`05-源码/Z0D3Skeleton.lean` 现在有 **6 条已证引理**（`fwd` 在内）加 **2 个 `sorry`**
（`bwd` 与由 `fwd`/`bwd` 合成 HBL3 的 `HBL3_of_fwd_bwd`）。
复制它到包的 `GodelQ/ZFC/`，按 `05-源码/BUILD.md` 编译，然后从 `bwd` 攻起。
