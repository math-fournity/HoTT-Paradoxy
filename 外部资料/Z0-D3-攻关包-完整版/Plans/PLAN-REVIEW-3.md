# `zfcTr-D3-plan.md` 独立评审（第三份修订，2026-10-11，Codex 会话 9276）

> **性质**：对 `zfcTr-D3-plan.md` 的独立评审。**不修改原计划**，只附在旁边。
> 这是继 `zfcTr-D3-plan-revision.md`（第二位 AI）与
> `Z0-D3-攻关包-最小完整版/PLAN-REVISION.md`（第三位 AI）之后的**第三份**修订。
> 我把前两份的修正都吃进来了，并报告它们之后本机新出现的事实。
>
> 每条判断凡标 **[实测]** 的都有本机 Lean 4.34.0 + Foundation `1fb01b72` 运行支撑。

---

## 0. 直接回答"这个计划是对的吗"

**方向对，缺口定位错，工作量估计错。**

| 项 | 判断 |
|---|---|
| §3 的 Bridge′ 弱化 | **对**，而且是关键洞察 |
| §4 对 `of_provability` 语义性的否定 | **完全正确**（[实测] 全量 grep 确认无内化版本） |
| §5 的移植思路 | **方向对，但不必做**——Foundation 已提供 Craig 化后的 D3 |
| §5.1 的 L1–L5 分解 | **不必做**（见 §2） |
| §5.1 L3 的有界 ∀ 情形 | **写错了量词方向**（第二位 AI 已指出，[实测] 确认） |
| §6 的"备选路线" | **判死了错的路线，漏掉了对的那条** |
| §7.3 的环境描述 | **与实际不符**（第二位 AI 已指出，[实测] 确认） |
| §8 的验收标准 | **正确，可采用** |

**一句话**：原计划把"重做 1080 行的 Σ1 完全性"当作必由之路，
但真正的缺口是**一条句法等价的一个方向**，规模小得多。

---

## 1. 三份修订的关系

| 修订 | 作者 | 核心贡献 | 本评审的处理 |
|---|---|---|---|
| `zfcTr-D3-plan-revision.md` | 第二位 AI（Codex 会话 01a120e6 之前） | ① 指出 L3 量词方向错；② 指出环境路径错；③ 试 R-新（`Sh.Δ₁`）并判死 | **两条指出全部采纳**（§3、§4）；③ 的判死**成立但不必要**（§5） |
| `Z0-D3-攻关包-最小完整版/PLAN-REVISION.md` | 第三位 AI | 发现 `Sh.craig` 的 D3 可由 `inferInstance` 得到；缺口缩为 `keyE` | **采纳**，并推进到 §2 |
| 本评审 | 本次 | 确认缺口是 `bwd` **一个方向**；给出零件清单与两条可行路径；全量 grep 证据 | — |

---

## 2. 本机实测：缺口比两份修订说的还小

### 2.1 三个 `inferInstance` 决定一切（[实测] exit 0）

```lean
noncomputable example : (Sh.craig : ArithmeticTheory).Δ₁ := inferInstance
noncomputable example : (Sh.craig.standardProvability).HBL3 := inferInstance
noncomputable example : 𝗣𝗔⁻ ⪯ Sh.craig := inferInstance
```

**这三条同时成立**意味着：

- `Sh.craig` 有 𝚫ᴬ₁ 公理表示（**不必自己 Craig 化**）；
- **Foundation 对 Craig 化后的理论已提供完整的 D3**（`HBL3` 由类型类搜索直接合成）；
- `sigma_one_complete (T := Sh.craig)` 的全部前提齐备。

所以原计划 §5.1 的 L1–L5（原子完全性、项求值、Δ0 完全性、∃-引入、组装）
**全部不必做**——Foundation 的 `DerivabilityCondition/D3.lean` 已经做完了，
且对 `Sh.craig` 直接可用。

### 2.2 缺口 = 一条句法等价的**一个方向**

```lean
-- 唯一缺口（骨架里的 bwd）
lemma keyE_bwd {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (σ : ArithmeticSentence)
    (h : V ↓[ℒₒᵣ] ⊧ ↑(provabilityPred (Theory.craig Sh) (zfcTr σ))) :
    V ↓[ℒₒᵣ] ⊧ ↑(zfcTr (zfcTr σ))
```

- **`fwd`（`→`）免费**：`provable_sigma_one_complete`，因为 `zfcTr σ` 是 Σ1 句
  （`zfcTr_sigma1` 已证）。骨架里已写成 `lemma fwd`，无 `sorry`。
- **`bwd`（`←`）是唯一缺口**：展开后即
  `Provable Sh.craig ⌜zfcTr σ⌝ (V) → Provable 𝗭𝗙𝗖 ⌜(zfcTr σ)ᵗ⌝ (V)`。

### 2.3 元层影子是通的（[实测] exit 0）

```lean
example (σ : ArithmeticSentence) (h : Sh.craig ⊢ σ) : 𝗭𝗙𝗖 ⊢ arithTrln.translate σ := by
  have h1 : Sh ⊢ σ := Entailment.weakerThan_iff.mp (inferInstance : Sh.craig ⪯ Sh) h
  exact (Sh_provable_iff σ).mp h1
```

**这说明元层没有任何障碍**。缺口纯粹在"V 层"：`bwd` 拿到的是
`Provable Sh.craig ⌜zfcTr σ⌝`（V 中存在推导编码 `d`），而 `d` 在非标准 V 中
可能对应非标准推导，元层的 `Sh_provable_iff` 接不上它。

---

## 3. 采纳第二位 AI 对 §5.1 L3 的更正（[实测] 确认）

原计划 L3 的有界 ∀ 情形写"在 𝖨Σ₁ 内对 `u ≤ b` 做 Σ₁ 归纳，
证 `∀ u ≤ b, Provable 𝗭𝗙𝗖 ⌜…⌝`"。**这是错的**：要证的命题本身就是全称的，
而 Lean 里你只有 `hw : V ⊧ θ(w)` 这个 Prop，**取不出逐个 `u` 的见证**。

正确形状是 `PeanoMinus.lean:235` 的 `ball_intro`：

```lean
lemma ball_intro (φ : Semiformula V ℒₒᵣ 1) (n : V)
    (bs : ∀ i < n, T.internalize V ⊢ φ.subst ![𝕹 i]) :
    T.internalize V ⊢ φ.ball (𝕹 n)
```

**假设是元层全称**——对每个 `i < n` 分别给一条 V 内推导。**采纳。**

---

## 4. 采纳第二位 AI 对 §7.3 的更正（[实测] 确认）

原计划说环境在 `~/workspace/toolchain-cache/`，有 137/181 模块，8G 机器 OOM。
**实际**：

```
~/workspace/toolchain-cache/           不存在
/Volumes/D/HoTT-toolchain-cache/foundation-src/                   308 个 .lean
/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean/   2500 个 olean
```

[实测] 24 个 GodelQ 模块 + SeqTranslateFormula 全链编译约 **27 秒**（增量几乎瞬时）。
**没有 OOM 问题。** 原计划的悲观描述会让执行 AI 去找不存在的环境。**采纳。**

---

## 5. 不采纳第二位 AI 的一处结论：R-新 的判死成立，但不必要

第二位 AI 在 §4b 论证：为 `Sh` 构造 `Theory.Δ₁` 会卡在 `isDelta1`，
因为 `mkDelta trProv (∼trProv)` 要求 `trProv ↔ ¬trProv`（假）。
它进一步说"照 CraigTrick 模板为 `Sh` 造特征会卡在证明长度的界"。

**前半成立**（[实测]：`trProv` 是 Σ1 不是 Δ1）。
**后半不必要**：**不需要为 `Sh` 构造 Δ1 特征**——`Sh.craig` 的 Δ1 特征
Foundation 已经建好，`inferInstance` 即可（§2.1）。

所以 R-新 的"判死"只说明"取 `ch := trProv` 这一条具体路不通"，
不说明"必须自己 Craig 化"。**第三位 AI 的入口（`T := Sh.craig`）才是对的。**

---

## 6. 对本机第三位 AI（PLAN-REVISION.md）的补充

它的 `keyE` 分解正确，但它对 `keyE` 的**两半**的刻画可以更精确：

它写"左→右与右→左都需要 V 层的推导消去"。**实测修正**：

- **左→右（`fwd`）不需要推导消去**——它就是 `provable_sigma_one_complete`，
  纯 Σ1 完全性，Foundation 现成，[实测] exit 0。
- **只有右→左（`bwd`）需要**。

所以真正要做的只有**一条**推导消去，不是两条。

---

## 7. 修订后的执行顺序（给执行 AI）

| 顺序 | 内容 | 依据 |
|---|---|---|
| 1 | 复制 `Z0-D3-补充包二-全量源码与缺口骨架/04-缺口骨架/缺口骨架.lean` 到项目包 | [实测] exit 0 |
| 2 | 试**路径 2**：只对标准 Σ1 句重走 `bold_sigma_one_complete`（`D3.lean:82`）的结构，把目标从 `T.internalize V ⊢ ⌜φ⌝` 换成 `Provable 𝗭𝗙𝗖 ⌜translate φ⌝` | 见 `04-缺口骨架/缺口的精确形状.md` §4 |
| 3 | 若路径 2 卡住，试**路径 1**：对 `Sh.craig` 推导的 10 条规则（`Proof/Basic.lean:412`）做 V 内归纳逐规则消去 | 同上 |
| 4 | 证完删 `sorry`，按 `BUILD.md` 出正式收据 | 原计划 §8 |

**两条路径都不必重做 Σ1 完全性**，这是相对原计划最大的节省。

---

## 8. 总判断

原计划的**数学直觉是对的**（Bridge′ 弱化、`of_provability` 不可内化、
需要跨"元层推导 → V 内编码"这一步），**但它把这一步的重量估成了 1080 行**。

本机实测表明：这一步落在 **`bwd` 一个方向**上，而
`Sh.craig` 的 Craig 化与 D3 都**不必自己做**（Foundation 已提供，`inferInstance` 即得）。
所以缺口的真实规模介于"几行"与"1080 行"之间——是**一条推导消去**的规模，
而不是重做形式化 Σ1 完全性的规模。

**唯一仍需诚实承认的**：`bwd` 是真的数学工作，不是 Lean 工程细节。
`Provable.sound` 只在 ℕ 层成立，跨不过去；这一步的数学内容就是 D3 本身。
