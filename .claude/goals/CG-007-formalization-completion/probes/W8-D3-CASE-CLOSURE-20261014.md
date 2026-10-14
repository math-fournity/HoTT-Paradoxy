# D3（`RootBlockerQ`）结案文档 — 2026-10-14

> 本文件把本会话 10 份 `W8-D3-*` 探针的结论固化为一份文档，
> 使未来重启的人不必重复搜索。**判据一律是 exit code + `#print axioms`。**

## 0. 目标

```
RootBlockerQ : p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗂 (iT 0 p)
```
它等于 D3（`zfcTr.HBL3`）的唯一实质内容；`zfc_z0_full_of_D3_internalize`
表明它一旦成立，Z0 完整形式 `𝗭𝗙𝗂 ⊬ (𝗭𝗙𝗶.consistent)ᵗ` 立即成立。

## 1. 三条候选路 —— 全部机器核验，全部否掉

| 候选路 | 关键件 | 判定 | 探针 |
|---|---|---|---|
| **语义 / 完备性** | `SetTheory.complete` + `models_iff_provable_of_Sigma0_param` | ❌ **循环**：后者要 `[T.SoundOnHierarchy 𝚺 1]`，而该 instance **蕴含 `Consistent T`**（`FirstOrder/Arithmetic/Basic/Hierarchy.lean:189`）。用「𝗭𝗙𝗂 一致」证「𝗭𝗙𝗶 一致」的反命题 | `W8-D3-soundonhierarchy-20261013.lean`（证 `sound_on_hierarchy_implies_consistent`，exit 0） |
| **Foundation 现成 D3** | `provable_internalize`（`DerivabilityCondition/D3.lean:175`） | ❌ 对 `T := Sh` 用不了：`#synth Theory.Δ₁ Sh` **失败**；改 `T := 𝗜𝚺₁` 则谓词不同 | `W8-D3-FOUNDATION-HAS-IT-20261014.lean`、`W8-D3-provabilityPred-eq-zfcTr-20261014.lean` |
| **反向引理**（码 → 引号） | `IsSemiformula → ∃ φ, p = ⌜φ⌝` | ❌ **为假**：`IsUFormula` 是 `Fixpoint`，非标准模型含非标准元素。Foundation 的 `IsSemiformula.sound`（`Formula/Coding.lean:478`）载体是 `ℕ`，「限定在 ℕ」是**本质的** | 见记忆 `cg007-nonstandard-model-refutations` |

### 1.1 ★ 关键区分：Foundation 有**两个** D3 定理，别混

| 定理 | 形态 | 前提 | 状态 |
|---|---|---|---|
| `bold_sigma_one_complete`（`D3.lean:82`） | `V ⊧/w φ → T.internalize V ⊢ (toNumVec w ⤔ ⌜φ⌝)` | `[Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]` | ✅ **本身可用**（`Theory.Δ₁ 𝗜𝚺₁` 已机核验合成），但同样卡 `Theory.Δ₁ Sh` |
| `provable_internalize`（`D3.lean:175`） | `Provable T ⌜σ⌝ → Provable T ⌜provabilityPred T σ⌝` | 同上 | 这才是 **D3 本身**。对 `T := Sh` 卡 `Theory.Δ₁ Sh`；`T := 𝗜𝚺₁` 则 `provabilityPred 𝗜𝚺₁ σ ≠ zfcTr σ` |

**两条是同一堵墙**（都要 `[Theory.Δ₁ T]`）。

## 2. `Theory.Δ₁ Sh` 的失败原因 —— = 显式义务

`Theory.Δ₁`（`Bootstrapping/Syntax/Theory.lean:16`）要 `ch : 𝚫ᴬ₁.Semisentence 1`，即 **Σ₁ 且 Π₁**：

* **Σ₁ 侧（已有）**：`trProv`（本包 `Z0Full.lean:40`）= `∃ y, iTDef y 0 x ∧ provable 𝗭𝗙𝗶 y`；
* **Π₁ 侧（义务，未证）**：`¬∃ y, iTDef y 0 x ∧ provable 𝗭𝗙𝗶 y` 的 Π₁ 定义。

**Π₁ 侧的数学内容** = 「`x` 的翻译在 𝗭𝗙𝗂 中**不可证**」要在 𝗜𝚺₁ 内有 Π₁ 表示。
而 D3 说的正是「**可证性**能被内部表示」——故 **Π₁ 侧与 D3 是同一件难事**
（⚠️ AI 判断，未证；012-Flash 独立判断一致）。

**⟹ Foundation 的 D3 路线对 `T := Sh` 是循环的**（用 D3 证 D3 的前提）。

## 3. 两个已澄清的误区（别再重复踩）

1. **`Sh.RE` 是白送的**：`#synth Theory.RE Sh` ✅（`Sh_RE`，来自
   `Sh_RE_of_translate_computable` + W4b 的 `translate_computable`）。
   本包旧文档与 `Z0Shadow.lean:14-17` 把 `Sh.RE` 记为「未证条件」**已过时**。
   **卡点不是 `Sh.RE`。**
2. **Foundation 没有 `Theory.Δ₁_of_RE`**：全库 grep 过。全部 Δ₁ 构造子只有
   `ofFinite` / `singleton` / `add` / `insert` / `ofEq` /
   `InductionScheme.delta1_of` / `T.craig` / `𝗣𝗔⁻` / `Con` / `Incon` /
   `InductionScheme univ·hierarchy·prenex`——**没有一个从 `T.RE` 出发**。
   `T.craig` 那条虽假设 `[T.RE]`，但产出 `(T.craig).Δ₁` 而非 `T.Δ₁`
   （它换了个理论，绕过去而非建出来）。

## 4. 已落地的零件（不是义务）

```
lemma isUFormula_qqVerums : ∀ (k : ℕ), IsUFormula ℒₒᵣ (qqVerums (k : V))
theorem iT_qqVerums (n : V) : ∀ (k : ℕ), iT n (qqVerums (k : V)) = qqVerums (k : V)
```
已入**生产包** `GodelQ/ZFC/TranslateShiftCompat.lean`，
`#print axioms = [propext, Classical.choice, Quot.sound]`，**无 sorryAx**，
全链 33 模块重建 rc = 0。

意义：`Theory.IsCraigAxiom (T := Sh)` 的 V 层展开里有 `qqVerums s`
（`s` 个 `⊤` 的合取），本引理说明它在 `iT` 下**不变**。

## 5. 归约链（若未来重启）

```
𝗭𝗙𝗶 ⊢ translate τ                          (假设)
  ↔ Sh ⊢ τ                                  (Sh_provable_iff，包内已证)
  → Sh ⊢ provabilityPred Sh τ               (Foundation D3)   ← 卡 Theory.Δ₁ Sh
  ↔ 𝗭𝗙𝗶 ⊢ translate (provabilityPred Sh τ)     (Sh_provable_iff)
  = 𝗭𝗙𝗶 ⊢ translate (zfcTr τ)               (需 provabilityPred Sh τ = zfcTr τ)
```

012-Flash 提议：不必证两个谓词**相等**，只要证 `⌜zfcTr σ⌝` 与
`⌜provabilityPred 𝗜𝚺₁ σ⌝` 在 ℕ 中**同真值**，就够 `sigma_one_complete` 用。
（未核验。）

## 6. 探针索引

| 探针 | 结论 | exit |
|---|---|---|
| `W8-D3-soundonhierarchy-20261013.lean` | `SoundOnHierarchy 𝚺 1 ⟹ Consistent T`（循环的根源） | 0 |
| `W8-D3-reduction-shape-20261013.lean` | 归约链四步 + `reWitness` 是 `reCh` 的 Σ₀ 见证矩阵 | 0 |
| `W8-D3-reflection-found-20261013.lean` | Σ₀ 反射工具定位 + 两个前提（载体 ℕ、SoundOnHierarchy） | 0 |
| `W8-D3-qqVerums-iT-20261013.lean` | `iT_qqVerums`（已入生产包） | 0 |
| `W8-D3-bold-sigma-one-20261014.lean` | `bold_sigma_one_complete` 形状与前提核验 | 0 |
| `W8-D3-FOUNDATION-HAS-IT-20261014.lean` | `provable_internalize 𝗜𝚺₁` 实例化**真的能用** | 0 |
| `W8-D3-provabilityPred-eq-zfcTr-20261014.lean` | 短路口不存在（谓词不同） | 0 |
| `W8-D3-zfcTr-vs-provabilityPred-20261014.lean` | 归约链两处卡点 | 0 |
| `W8-D3-Pi1-side-equals-D3-20261014.lean` | `Sh.RE` ✅ / `Theory.Δ₁ Sh` ❌ / `trProv` Σ₁ 侧 ✅ | 0 |
| `W8-D3-Flash-stepI-II-20261014.lean` | 复核 012-Flash 三步；`Theory.craig`/`IsCraigAxiom` 的 `#print` | 0 |

## 7. 结论

**`RootBlockerQ` 没有捷径。** 要么直接攻 `zfcTr_D3_internalize`
（在 ℒₛₑₜ 里构造该蕴含的 𝗭𝗙𝗶 推导），
要么把 `Theory.Δ₁ Sh` 的 Π₁ 侧作为**独立的显式义务**交还。

按 goal 完成门 2，「照实写明阻塞引理」是允许的交付形态——本文件即该形态。
