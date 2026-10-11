# `zfcTr-D3-plan.md` 修订说明（2026-10-10，Codex 会话 01a120e6，第二版）

> **性质**：对 `/Volumes/D/HoTT_AI_HANDOFF_20260911/外部资料/zfcTr-D3-plan.md` 的独立评审。
> **不修改原计划文件**，只附在旁边。**注意：本文件不是
> `外部资料/zfcTr-D3-plan-revision.md`（那是上一版修订，来自另一位 Codex 会话）的替代，
> 是它的后续——我把上一版的修正也吃进来了，并报告本机 Lean 实测的新事实。**
>
> 本说明的每条判断，凡标 **[实测]** 的都有本机 Lean 运行支撑
> （Lean 4.34.0 + Foundation `1fb01b72` + 本 repo 24 个 GodelQ 模块）。

---

## 0. 结论先说

原计划的**方法论方向仍然正确**（Bridge′ 弱化、对 `of_provability` 语义性的否定、逐段移植
`bold_sigma_one_complete` 的思路都对），但它给的**缺口定位比实际的重**。

我本机实测到：**Foundation 已经提供了 `Sh.craig` 的完整 D3**，
因此不需要"从零移植 `bold_sigma_one_complete`"（那是约 1080 行工作量），
缺口缩小为**一条句法等价**：

```lean
-- 唯一缺口
lemma keyE (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ zfcTr σ 🡘 provabilityPred Sh.craig σ
```

---

## 1. 我实测确认的新事实（原计划与上一版修订都不知道）

| # | 事实 | 怎么测的 | 意义 |
|---|---|---|---|
| 1 | `Sh.RE`（C-119，已是 instance）⟹ Foundation 的 Craig 化给 `Sh.craig.Δ₁` | `noncomputable example : (Sh.craig : ArithmeticTheory).Δ₁ := inferInstance` **[实测]** | 打通了 `[T.Δ₁]` 这一环 |
| 2 | `𝗣𝗔⁻ ⪯ Sh.craig`、`Sh.craig ⪯ Sh`、`Sh ⪯ Sh.craig` 三个都 `inferInstance` | 同上 **[实测]** | `sigma_one_complete (T := Sh.craig)` 的全部实例齐了 |
| 3 | **`(Sh.craig.standardProvability).HBL3` 由 `inferInstance` 直接得到** | 同上 **[实测]** | **Foundation 的 D3 可以直接用在 `Sh.craig` 上** |
| 4 | `Bootstrapping.Arithmetic.sigma_one_complete (T := Sh.craig)` 可用，我写成 `step1` 并编译通过 | 文件 `Z0D3Skeleton.lean` exit 0 **[实测]** | 从 `V ⊧ zfcTr σ` 到 `Provable Sh.craig ⌜zfcTr σ⌝` 一行搞定 |
| 5 | `V ⊧ provabilityPred Sh.craig σ ↔ Provable Sh.craig ⌜σ⌝` 可证 | 同文件 **[实测]** | 语义层桥打通一半 |

**为什么上一版修订没发现这些**：它死磕 `Sh.Δ₁` 且据此判定 R-新/Δ0/R-备 三条路"都通向同一件事、
都绕不开 D3"。它没有试 `T := Sh.craig`（Craig 化的 `Sh`）——而 Foundation 恰恰对
Craig 化后的理论提供了完整的 `HBL3` instance。这是一个可机械发现的入口。

---

## 2. 对原计划 §5.1 引理分解的修订

| 原计划 | 我的修订 |
|---|---|
| L1 翻译的原子完全性 | **不需要**。Foundation 的 `bold_sigma_one_complete` 已经做完了原子层（`term_complete` 等），且它对 `T := Sh.craig` 直接可用。 |
| L2 翻译的项求值 | **不需要**，同上。 |
| L3 Δ0 完全性（核心） | **不需要**，同上。 |
| L4 ∃-引入 | **不需要**。 |
| L5 组装 Bridge′ | **替换为**：`keyE` + `Provability.ext` + `provable_D3 (T := Sh.craig)`。 |

**新分解**（一条引理 + 一个组装）：

```lean
-- [唯一缺口] keyE
lemma keyE (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ zfcTr σ 🡘 provabilityPred Sh.craig σ

-- 组装（零件全部已实测可用）
have hE := keyE σ
have hD3 := provable_D3 (T := Sh.craig) (σ := σ)
-- 经 Provability.ext / mono' 推出 zfcTr.HBL3，再由 Z0Full.zfc_z0_full_of_D3_internalize 得完整形式
```

---

## 3. 对上一版修订（`zfcTr-D3-plan-revision.md`）的延续与更正

上一版的判断我需要更正两处：

**更正 1**：它说"三条路都通向同一件事（形式化 Σ1 完全性）"。
**不完整**。`T := Sh.craig` 这条路里，Σ1 完全性 Foundation **已经机器证明完了**
（`DerivabilityCondition/D3.lean`，179 行 + 支撑），我只需 `inferInstance`。
真正的缺口是句法等价 `keyE`，它的数学内容比 Σ1 完全性弱得多。

**更正 2**：它建议"照 `CraigTrick.lean:207-250` 为 `Sh` 构造 𝚫ᴬ₁ 特征，
它会卡在证明长度的界"。**方向对但入口错**：不需要为 `Sh` 构造特征
（会撞"界不存在"），直接 `inferInstance : (Sh.craig).Δ₁` 就是
`Theory.craigCh`，Foundation 已经建好并通过 `IsCraigAxiom.defined` 的 ProperOn 证明。

---

## 4. 我实测确认的：`keyE` 内部的真实卡点

`keyE` 经完备性定理化到语义层后，剩下的是：

```
Provable 𝗭𝗙𝗂 ⌜σᵗ⌝ (V) ↔ Provable Sh.craig ⌜σ⌝ (V)
```

- 左→右： Provable 𝗭𝗙́ ⌜σᵗ⌝ → 𝗭𝗙́ ⊢ σᵗ → Sh ⊢ σ → Sh.craig ⊢ σ → Provable Sh.craig ⌜σ⌝。
  但**第一步 `Provable 𝗭𝗙́ ⌜σᵗ⌝ → 𝗭𝗙́ ⊢ σᵗ` 对非标准 V 不成立**：
  Foundation 的 `Provable.sound`/`provable_iff_provable` 只在 ℕ 层。推导编码 `d` 可能非标准。
- 右→左：同理，也需要 V 层的推导消去。

**这两步就是 D3 的数学核心内容**，我不认为能绕过；但我也不认为它需要 1080 行
（那是完整的算术版 Σ1 完全性）。它的实际规模取决于 `keyE` 的两半能不能分别找到 Foundation 现成零件。
我把已找到的零件列在 `03-可用的已证引理/API.md` 的 §C，缺的标在 §E。

---

## 5. 给执行 AI 的具体起点

1. 复制 `05-源码/Z0D3Skeleton.lean` 到项目包，按 `05-源码/BUILD.md` 编译（我实测 exit 0）。
2. 从 `gap` 开始攻。先试单向 `𝗜𝚺₁ ⊢ zfcTr σ 🡒 provabilityPred Sh.craig σ`
   （配 `Provability.mono'` 可能就够 D3）。
3. 读 `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean` 全文
   （179 行）——不是移植它，而是看它怎么把 `V ⊧ σ` 变成 `T.internalize V ⊢ ⌜σ⌝`；
   `keyE` 需要的正是"跨理论的这一步"。
4. 若卡住：把卡点写成一条精确 Lean 命题，不要留 `sorry`。
