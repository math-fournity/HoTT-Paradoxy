# CG001-C-121、C-122、C-128：Z0 的内部化只差一条内部解释；其余前提与一条归约都是定理

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-FULL-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W8；本机 Codex 会话接手 Claude Opus 5.5 会话 d58e0c0d 中断的同一单元，2026-10-09。授权原话（2026-10-08）：“按照你的想法进行优先级安排，完成后续所有“形式化和机器证明”工作。”
>
> **理论变体**：同 `../godel-q-zfc-z0-translate/`：Lean 4（v4.34.0）加 Mathlib（`5ed29652`）与 Foundation（`1fb01b72`），经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。
>
> **身份**：机器证明（范围见 §4、§7、§8）。把 C-120 读成“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”所差的最后一步，被固定成**一条**精确的 Lean 命题；C-128 再把这条命题在 `Type` 宇宙上归约到一条更窄的内部解释。除此之外的全部前提都是定理。D3 本身仍未证。

## 0. 位置

- C-120 已给出 `𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`（不带前提）。这里的一致性句 `Sh.craig.consistent` 是 Foundation 用选择挑出的某个 Σ1 定义（包内补注见 `../godel-q-zfc-z0-translate/REVISIONS.md`），它在 𝗜𝚺₁ 内部与 Con(𝗭𝗙𝗖) 的关系无从推理。
- 本包换一条显式的路：把“𝗭𝗙𝗖 证明 x 的翻译”本身当作可证性谓词，即 `𝔅Z(x) := Provable 𝗭𝗙𝗼 (iT 0 x)`，作为 `Sh` 的 `Provability 𝗜𝚺₁ Sh`。它没有选择，逐字由 C-119 的内部翻译 `iT` 给出。
- 走 Foundation 的抽象第二定理（`ProvabilityAbstraction.con_unprovable`）。它要的条件逐条核对：D1、D2 成为定理；`𝗜𝚺₁ ⪯ Sh` 是 C-110；`Sh` 一致是 C-103；对角化是 Foundation 对 𝗜𝚺₁ 自带的；**只剩 D3**。
- D3 被固定成 `GodelQ/ZFC/Z0Blocked.lean` 的 `zfcTr_D3_internalize`，它带未证标记，因此不是本运行的编译源。`Z0Full.zfc_z0_full_of_D3_internalize` 表明：这条引理一旦成立，完整形式 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ` 立即随之成立，无需别的东西。

## 1. 精确命题（类型逐字见 `GodelQ/ZFC/Z0Full.lean`、`GodelQ/ZFC/Z0Blocked.lean`）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-121 | `GodelQ.Z0Full.zfcTr` 及随之四条 | (1) `𝔅Z := TrProvable x := Provable 𝗭𝗙𝗼 (iT 0 x)` 是 `Provability 𝗜𝚺₁ Sh`，其 Σ1 公式 `trProv`；`V ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗼 ⌜σᵗ⌝`。(2) D1（`zfcTr.bew_def`，由 C-119 的 `iT_quote` 与 Foundation 的 `internalize_provability`）。(3) D2 = HBL2（`modus_ponens_sentence`）。(4) `𝗜𝚺₁ ⊢ zfcTr.con 🡘 (𝗭𝗙𝗖.consistent)`（一致性句在 𝗜𝚺₁ 中等价）。(5) `zfcTr σ` 是 𝚺₁ 句。(6) 正对照：D3 在标准模型 ℕ 中成立 |
| CG001-C-122 | `GodelQ.Z0Full.zfc_z0_full_of_D3_internalize` | 阻塞引理 `zfcTr_D3_internalize`（见 §4）一旦成立，`𝗭𝗙𝗼 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`，即 Z0 的完整形式 |
| CG001-C-128 | `GodelQ.Z0Bridge.zfcTr_D3_internalize_of_sigma1_bridge`、`zfc_z0_full_of_sigma1_bridge` | 若每个 `Type` 层的 𝗜𝚺₁ 模型都能把 Σ1 算术句的内部证明编码沿 `arithTrln` 变成 𝗭𝗙𝗖 证明编码，则该宇宙上的 D3 形状成立，并且 `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`。见 §8 |

`Sh_z0_full`、`zfc_z0_full` 是 C-122 在 D3 作为实例给出时的两个特例，与 C-122 同一次编译。

## 2. 证明

- **𝔅Z 的构造**：`trProv : 𝚺ᴬ₁.Semisentence 1 := “x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗼) y”`。`𝚺ᴬ₁-Predicate (TrProvable : V → Prop) via trProv` 由 `iT_quote`（C-119）给出：`iT 0 ⌜σ⌝ = ⌜σᵗ⌝`。
- **D1**：`Sh ⊢ σ → 𝗜𝚺₁ ⊢ zfcTr σ`。经完备性化为每个 𝗜𝚺₁ 模型 V 中 `V ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗼 ⌜σᵗ⌝`，再由 Foundation 的 `internalize_provability` 从 `𝗭𝗙𝗼 ⊢ σᵗ` 得到。
- **D2**：`𝗜𝚺₁ ⊢ zfcTr (σ 🡒 τ) 🡒 zfcTr σ 🡒 zfcTr τ`。同样经完备性，两侧都用 `models_zfcTr_iff` 化成 `Provable 𝗭𝗙𝗼`，再用 Foundation 的 `modus_ponens_sentence`。
- **一致性句等价**：`zfcTr.con = ∼zfcTr ⊥`，而 `zfcTr ⊥ = Provable 𝗭𝗙𝗼 (iT 0 ⌜⊥⌝)`；`iT 0 ⌜⊥⌝ = ⌜⊥⌝` 由 `iT_quote` 与 `⊥` 的翻译。所以 `zfcTr.con` 与 Foundation 的 `𝗭𝗙𝗖.consistent` 在每个模型中都等价于 `¬ Provable 𝗭𝗙𝗼 ⌜⊥⌝`。
- **`zfcTr σ` 是 Σ1 句**：`trProv` 由 `mkSigma` 给出，`/[⌜σ⌝]` 保持层级（`Bounding.Hierarchy.rew`）。
- **正对照**：D3 在 ℕ 中成立，因为真的 Σ1 句子被 𝗭𝗙𝗼 证明（D1）加上 `Sh ⊢ σ ↔ 𝗭𝗙𝗼 ⊢ σᵗ`。
- **完整形式**：`con_unprovable (𝔅 := zfcTr)` 需要 `[zfcTr.HBL]`（= HBL2 + HBL3）与 `Sh` 一致。HBL2 是定理；HBL3 由阻塞引理在模型层逐点给出（`zfc_z0_full_of_D3_internalize` 的证明）。

## 3. 负控制

本包没有负控制运行：正结果全部以一条显式前提为条件，D3 的正对照已在同一运行中机器核对。阻塞引理本身不进入收据源，因此不存在“应当被拒绝而未拒绝”的目标。这与 CG-007 其它单元（每个单元都有至少一个负控制）不同，记在此处。

## 4. 还差什么：唯一阻塞引理

`GodelQ/ZFC/Z0Blocked.lean:zfcTr_D3_internalize`，逐字为：

```lean
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗼 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗼 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

读作：**“𝗭𝗙𝗖 证明了 τ 的翻译，那么 𝗭𝗙𝗼 也能证明‘𝗭𝗙𝗼 证明了 τ 的翻译’这句话的翻译。”** 这就是 Hilbert–Bernays 条件 D3 在这个显式谓词下的形状，即**经翻译的形式化 Σ1 完全性**。

- Foundation 对算术理论的 D3 有完整机器证明（`Bootstrapping/DerivabilityCondition/D3.lean`，179 行，加 `PeanoMinus`/`EquationalTheory` 共约 1080 行）；它服务的是 `T.standardProvability`（谓词 `Provable T ⌜σ⌝`，T 是算术理论）。本处谓词是 `Provable 𝗭𝗙𝗼 (iT 0 x)`，作用对象是**翻译后**的公式，不能直接套用。
- 需要的这一步在数学上是“证明的内部翻译”：给出一个 𝗜𝚺₁ 内的证明搜索，把一条 𝗭𝗙𝗼 证明变成“𝗭𝗙𝗼 证明这句话”的 𝗭𝗙𝗼 证明。Foundation 的 `LK/Interpretation.lean:443 of_provability`（`U ⊢ σ → T ⊢ π.translate σ`）是用**完备性定理**证明的语义证明，其中没有可搬进 𝗜𝚺₁ 的语法翻译。
- 因此这条引理是实的、可交给下一个工作单元或外部复核的精确缺口。它不是措辞问题：把 D3 写成别的形式也绕不过同一内容。
- C-128 不取消这条缺口。它只证明：在 `Type` 宇宙上，缺口可以再收成“Σ1 算术证明编码沿 `arithTrln` 变成 𝗭𝗙𝗖 证明编码”。`Z0Blocked` 的 `Type*` 陈述比 C-122 实际消费的前提更强，C-128 不对它作声称。

## 5. 文件

- 新文件：
  - `GodelQ/ZFC/Z0Full.lean`（𝔅Z、D1、D2、一致性句等价、Σ1 层级、正对照、完整形式的条件形式）；
  - `GodelQ/ZFC/Z0Blocked.lean`（唯一阻塞引理，带未证标记，**不是**任何运行的编译源）；
  - `GodelQ/ZFC/Z0Bridge.lean`（C-128 的条件归约；是归约运行的编译源，不导入 `Z0Blocked.lean`）。
- 21 个依赖模块逐字节复制自 `../godel-q-zfc-z0-translate/GodelQ/`（复制时逐个 `cmp` 核对过）。

## 6. 运行

见 `README.md` 的运行表与 CG-001 证据索引 §35。捕获工具：`.claude/goals/CG-007-formalization-completion/tools/capture_run.py`（驱动 `zfc_lean_check.py` 原样复用）。

## 7. 禁止外推

1. 不声称“𝗭𝗙𝗼 ⊬ Con(𝗭𝗙𝗼)”已证：完整形式以 §4 的阻塞引理为显式前提。已证且不带前提的仍是 C-120 的影子形式（`𝗭𝗙𝗼 ⊬ (Sh.craig.consistent)ᵗ`）。
2. 不推出 ZFC ⊢ ⊥。
3. `Sh` 的一致性来自 Lean 元层的 `Universe` 模型（C-103），不是 𝗭𝗙𝗼 内部可证的事。
4. `iT_quote` 与 `models_zfcTr_iff` 是对每个具体算术公式成立的元层定理（在 𝗜𝚺₁ 的每个模型中），不是 𝗜𝚺₁ 内部对“所有公式编码”的一句断言。
5. D3 在 ℕ 中成立是正对照，不证明它在任意（含非标准）𝗜𝚺₁ 模型中成立。
6. C-128 是条件归约。它不证明 D3，不证明 `Z0Blocked` 的 `Type*` 陈述，也不把 `𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)` 提升为无条件定理。Foundation 的 `sigma_one_complete` 只给出 𝗜𝚺₁ 内部的算术证明编码；沿 `arithTrln` 把它变成 𝗭𝗙𝗖 证明编码仍是未证前提。

## 8. CG001-C-128：把 D3 收成一条内部解释（条件归约，不是 D3 的证明）

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-BRIDGE-001`。类型逐字见 `GodelQ/ZFC/Z0Bridge.lean`。

`zfcTr_D3_internalize_of_sigma1_bridge` 的前提 `bridge` 是：对每个 `Type` 层的 𝗜𝚺₁ 模型 V、每个 Σ1 算术句 σ，若 V 内部有 `Provable 𝗜𝚺₁ ⌜σ⌝`，则 V 内部有 `Provable 𝗭𝗙𝗖 ⌜arithTrln.translate σ⌝`。

在这个前提下：

1. `zfcTr τ` 已是 Σ1 句（C-121 的 `zfcTr_sigma1`），而且假设 `Provable 𝗭𝗙𝗖 ⌜translate τ⌝` 正好是 `V ⊧ zfcTr τ`；
2. Foundation 的 `sigma_one_complete` 因此给出 `Provable 𝗜𝚺₁ ⌜zfcTr τ⌝`，这是 V 内部的算术证明编码；
3. `bridge` 把这个编码变成 `Provable 𝗭𝗙𝗖 ⌜translate (zfcTr τ)⌝`。

`zfc_z0_full_of_sigma1_bridge` 把上面的逐点结论喂给 C-122 的 `zfc_z0_full_of_D3_internalize`，得到同一条完整形式：`𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`。

这不是 D3 的证明。Foundation 的 `DirectInterpretation.of_provability` 只把外部推导经完备性变成另一条外部推导，不产生非标准模型 V 里的证明编码，所以填不上 `bridge`。`Z0Blocked.lean` 仍带未证标记，并且不进入本运行的源清单。
