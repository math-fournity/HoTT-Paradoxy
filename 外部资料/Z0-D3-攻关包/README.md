# Z0-D3 攻关包

**目标**：在 Lean 4 中证明一条引理，从而完成哥德尔第二不完备定理在真实 𝗭𝗙𝗖 上的完整形式化。

**任务只有一件事**：证明 `Leanservice/Z0Blocked.lean` 中的 `zfcTr_D3_internalize`。

**不需要做的事**：理解这个 repo 的研究背景、读任何历史文档、跑任何测试。本包装下了所有必需的定义与已证定理，全部在 `Leanservice/` 的 4 个文件里。

---

## 1. 要证什么

```lean
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

读作：**“𝗭𝗙𝗖 证明了 σ 的翻译，那么 𝗭𝗙𝗖 也能证明‘𝗭𝗙𝗖 证明了 σ 的翻译’这句话的翻译。”**

- `V` 是算术理论 `𝗜𝚺₁` 的任意模型（可能是非标准的）；
- `Provable 𝗭𝗙𝗖 φ` 即 `∃ d, Proof 𝗭𝗙𝗖 d φ`——存在一个 𝗭𝗙𝗖 推导编码 d 推出 φ；
- `σᵗ := arithTrln.translate σ` 是算术句 σ 到集合论的**直接翻译**；
- `zfcTr σ := trProv.val/[⌜σ⌝]`，其中 `trProv := “x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y”` 是一个 Σ1 公式。

**为什么是它**：这是 Hilbert–Bernays 可导性条件 D3 在这个显式可证性谓词下的形状，即**经翻译的形式化 Σ1 完全性**。证明它之后，`Z0Full.zfc_z0_full_of_D3_internalize`（本包内，已过核、无 `sorry`）立即给出完整形式 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ`。

**当前状态**：`Z0Blocked.lean` 里这条定理是 `sorry`。把它填掉即可。

---

## 2. 已经有什么（全部已过核）

`Leanservice/` 下 4 个文件，编译次序：

| 次序 | 文件 | 行数 | 内容 |
|---|---|---|---|
| 1 | `InternalTranslate.lean` | 637 | 内部翻译 `iT`/`iVE`/`iTR` + 正确性 `iT_quote`、`iVE_quote` |
| 2 | `TranslateRE.lean` | 66 | 翻译可计算、`Sh.RE`、Z0 影子形式无条件 |
| 3 | `Z0Full.lean` | 145 | `trProv`、`zfcTr`、D1、D2、一致性句等价、`models_zfcTr_iff`、`zfc_z0_full_of_D3_internalize` |
| 4 | `Z0Blocked.lean` | 37 | **要证的引理**（`sorry`） |

它们 import `GodelQ.ZFC.ShRE`，后者依赖更早的 20 个模块；那些模块在完整 repo 的
`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/` 下，是稳定的，不需要动。

编译命令与运行收据见 `收据/`（24 个模块顺序编译，exit 0，约 60 秒）。

## 2b. 我改了一处（否则文件编译不过）

`Z0Blocked.lean` 在 repo 里的版本缺一行 `open GodelQ.Z0Full`，所以 `zfcTr` 无法解析。
这个文件一直带 `sorry`、从没进过收据源，所以这个 bug 没被发现。
**本包已补上这一行**（`Leanservice/Z0Blocked.lean:20`）。现在它 elaborates 正常（只剩预期的 `sorry` 警告）。

已实测：把 `sorry` 换成 `intro hp; exact hp` 会被内核拒绝，目标非平凡。

## 3. 三条可直接用的引理

```lean
-- (a) TrProvable 与其 Σ1 公式 trProv 的对应（Z0Full.lean:46）
lemma trProvable_quote (σ : ArithmeticSentence) (V : Type*) [...] :
    TrProvable (⌜σ⌝ : V) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

-- (b) 语义层：V 满足 trProv 代入 σ  ⟺  𝗭𝗙𝗖 证明 σ 的翻译（Z0Full.lean:53）
lemma models_trProv_iff (V : Type) [...] (σ : ArithmeticSentence) :
    V↓[ℒₒᵣ] ⊧ (trProv.val/[⌜σ⌝] : ArithmeticSentence) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

-- (c) zfcTr 的语义（Z0Full.lean:66）
lemma models_zfcTr_iff (V : Type) [...] (σ : ArithmeticSentence) :
    V↓[ℒₒᵣ] ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

-- (d) zfcTr σ 是 Σ1 句（Z0Full.lean:87）
theorem zfcTr_sigma1 (σ : ArithmeticSentence) : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (zfcTr σ)
```

## 4. 一条已经失败的思路（实测过，不要重复）

**想为 `Sh` 构造 `Theory.Δ₁` 实例，再套 Foundation 的 `sigma_one_complete`（T := Sh）直接得引理。**

卡在第三条字段：`Theory.Δ₁` 要求 `ch.ProvablyProperOn 𝗜𝚺₁`，而它可经
`ProvablyProperOn.arithmetic_ofProperOn`（`Arithmetic/Definability/Hierarchy.lean:64`）从语义层的
`ProperOn M` 得到。若取 `ch := trProv`，`ProperOn` 就是 `trProv ↔ ¬trProv`，
**在 trProv 有确定真值的模型中为假**。即 `trProv` 是 Σ1 但不是 Δ1。

**可照抄的正确模板**（Foundation 内，机器证明过，且**未**用 Σ1 完全性）：
`Bootstrapping/Syntax/CraigTrick.lean:210` 的 `craigCh`。手法是**两半都用有界量词** `∃ s < x`，
Π1 半只多加一条唯一性条件。它的 `ProperOn` 证明在 `:222-234`，只用 `lt_K!_right`、`le_qqVerums`
这类初等引理。

若照这个模板为 `Sh` 造 𝚫ᴬ₁ 特征，需要把 `Provable 𝗭𝗙𝗖 x` 有界化成 `∃ d < x, ...`，
**它会卡在“证明长度不超过 x 的某个界”** —— 那个界就是 D3 本身。

## 5. Foundation 的相关 API（版本 `1fb01b72`）

| 名字 | 位置 | 形状 |
|---|---|---|
| `Provable` | `Bootstrapping/Syntax/Proof/Basic.lean:541` | `def Provable (φ : V) : Prop := ∃ d, Proof T d φ`（**外部**存在量化） |
| `tprovable_iff_provable` | `Bootstrapping/Syntax/Proof/Typed.lean:168` | `T.internalize V ⊢ σ ↔ Provable T σ.val` |
| `internalize_provability`（D1） | `Bootstrapping/DerivabilityCondition/D1.lean:27` | `T ⊢ φ → Provable T ⌜φ⌝` |
| `modus_ponens_sentence`（D2） | `DerivabilityCondition/D2.lean:30` | Provable 层面的 MP |
| `bold_sigma_one_complete` | `Arithmetic/R0/Basic.lean:94` | 沿公式结构归纳的形式化 Σ1 完全性（**算术理论**版） |
| `sigma_one_complete`（D3） | `DerivabilityCondition/D3.lean:170` | `V ⊧ σ → Provable T ⌜σ⌝` |
| `provable_internalize` | `DerivabilityCondition/D3.lean:175` | `Provable T ⌜σ⌝ → Provable T ⌜provabilityPred T σ⌝`（**只对算术 T**） |
| `of_provability` | `LK/Interpretation.lean:443` | `U ⊢ σ → T ⊢ π.translate σ`（**语义证明**，不可搬进 𝗜𝚺₁） |
| `CraigTrick` | `Bootstrapping/Syntax/CraigTrick.lean` | 上述 𝚫ᴬ₁ 模板 |

## 6. 环境

- Lean `4.34.0`（commit `293d5d0c`），Mathlib `5ed29652`，Foundation `1fb01b72`；
- Foundation 完整构建树：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/`（1893 模块）；
- 驱动：`zfc_lean_check.py`（禁网沙盒、绝对路径调 pinned 二进制、编译前核对每个模块的 SHA-256）；
- **不允许改 Foundation/Mathlib 源码**；新引理写在包内新文件，不要带 `sorry`。

## 7. 验收

1. `zfcTr_D3_internalize` 无 `sorry`，类型逐字不变；
2. `#print axioms` 只含 `propext`、`Classical.choice`、`Quot.sound`；
3. 24 个模块顺序编译 exit 0；
4. 抓正式 run 收据，`--rerun` 精确重放；
5. 若失败：把卡住的具体引理写清楚，不要留 `sorry` 冒充完成。

---

**给攻关 AI 的一句话**：这条引理在数学上就是“𝗭𝗙𝗖 的 Σ1 完全性经翻译后仍成立”。
Foundation 对算术理论已做完（约 1080 行），难点只在谓词作用在**翻译后**的公式上。
从 `CraigTrick.lean:207-250` 读起，那是本包内唯一机器证明过的同类 𝚫ᴬ₁ 构造。
