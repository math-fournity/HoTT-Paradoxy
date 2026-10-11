# R-新 最终判定（2026-10-10,Codex 会话 01a120e6）

## 一句话

R-新 不是免费通路,但它把缺口**精确定位**到了 Foundation 已经解决过的同一类问题上,
而且给出了可照抄的模板(`CraigTrick`)。

## 实测成果(都有 Lean 输出支撑)

| 项 | 状态 | 关键 Lean 事实 |
|---|---|---|
| `shCh : 𝚫ᴬ₁.Semisentence 1` | ✅ 构造成功 | `.mkDelta trProv trProv.negSigma`(negSigma 机器构建 𝚷1 证明) |
| `mem_iff`(Theory.Δ₁ 三条字段之一) | ✅ 三行打通 | `rw [models_trProv_iff, mem_Sh, provable_iff_provable]` |
| `tprovable_iff_provable` | ✅ | `T.internalize V ⊢ σ ↔ Provable T σ.val` |
| `shCh.ProperOn ℕ`(isDelta1 的语义半边) | ❌ **不可证** | 它要求 `trProv ↔ ¬trProv`,在 trProv 有确定真值的模型中为假 |

## 核心数学发现

`Theory.Δ₁ Sh` 的第三条字段 `isDelta1 : ch.ProvablyProperOn 𝖨Σ₁` 可以从
`ProperOn M`(语义等价)经 `arithmetic_ofProperOn` 得到。而对
`shCh = mkDelta trProv (∼trProv)`,`ProperOn` 就是 `trProv ↔ ¬trProv` —— **假**。

所以:`trProv` 是 Σ1 **但不是 Δ1**。"存在 ZFC 证明"与"不存在 ZFC 证明"当然不等价。

**推论:R-新 没有绕过 D3。它把"经翻译的形式化 Σ1 完全性"换成了"`trProv` 的 Δ1 性",
而后者在 Foundation 框架下需要同一件事:Σ1 与 Π1 在 𝖨Σ₁ 中等价。**

## 但找到了可照抄的模板(这是本轮真正的收获)

Foundation 的 `Bootstrapping/Syntax/CraigTrick.lean:210` 完整解决了同一问题:

```lean
noncomputable def _root_.FFL.FirstOrder.Theory.craigCh : 𝚫ᴬ₁.Semisentence 1 := .mkDelta
  (.mkSigma "x. ∃ s < x, ∃ p < x, ∃ v < x,
    !qqVerumsGraph v s ∧ !qqAndDef x p v ∧ !(T.reWitness.val) s p")
  (.mkPi "x. ∃ s < x, ∃ p < x, ∃ v < x,
    (∀ v', !qqVerumsGraph v' s → v' = v) ∧ !qqAndDef x p v ∧ !(T.reWitness.val) s p")
```

关键手法:**两半都用有界量词 `∃ s < x`,Π1 半只多加一条唯一性条件**
(`∀ v', Graph v' s → v' = v`)。这样:
- 语义上:有界存在 + 唯一 ⟺ 唯一有界存在,两半等价;
- 语法上:Σ1 半边是真的 Σ1,Π1 半边是真的 Π1(唯一性是 Π1)。

而 `ProperOn` 证明(CraigTrick.lean:222-234)只用了**有界/无界量化互换**的初等引理
(`lt_K!_right`、`le_qqVerums`),**没有用到任何 Σ1 完全性**。

## 因此下一步有明确的形状

为 `Sh` 构造 `𝚫ᴬ₁` 特征,照 CraigTrick 的模式:

- **Σ1 半边**:`∃ d < x, iTDef d 0 x' ∧ provableZFC d x`(x' 是 x 的翻译输入) ——
  但 `iTDef d 0 x'` 里 d 要小于 x 需要有界化处理;
- **Π1 半边**:同上的有界存在 + 关于"这样的 d 给出同一个公式"的唯一性。

**这仍然不免费**——Foundation 的 CraigTrick 只处理"公理集是 r.e."这一情形,
而 `Provable 𝗭𝗙𝗸` 是"存在证明",引理 244 行的 `T.exists_mem_of_reCh` 正是把
"存在 reCh 见证"变成"存在公理"的那一步,它用到 `T.RE`。
我们的 `Provable 𝗭𝗙𝗸 x` 是"存在 d 是 x 的 𝗭𝗙𝗸 证明",要把它有界化到 `d < x` 需要
"证明长度不超过某个 x 的多项式/指数函数"这类界——**这正是 D3 需要的形式化 Σ1 完全性**。

## 结论

1. Z0 完整形式(𝗭𝗙𝗰 ⊬ Con(𝗭𝗙𝗶))缺的是同一件事:形式化 Σ1 完全性。
   R-新、Δ0 路线、R-备 三条路都通向它。
2. 本轮的真实收获:缺口被精确定位到 `Sh.Δ₁.isDelta1`,且找到了 Foundation 内
   可照抄的 `CraigTrick` 模板与它**没有**用到的引理清单。
3. 下一步若要继续攻,最有希望的方向是照 `CraigTrick.lean:210` 的形状,
   尝试为 `Provable 𝗭𝗙𝗸` 构造有界化的 𝚫ᴬ₁ 特征。它会卡在"证明长度的界"这一点上,
   而那个界就是 D3。
