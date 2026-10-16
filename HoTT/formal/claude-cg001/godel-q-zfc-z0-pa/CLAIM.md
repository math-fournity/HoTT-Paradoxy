# CG001-C-109、C-110：𝗭𝗙𝗖 解释 𝗣𝗔；Z0 只剩一条前提

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-PA-001`；负控制 `MP-CG001-GODEL-Q-ZFC-Z0-PA-NEG-RE-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W3；本机会话 d58e0c0d，Opus 5.5，2026-10-08。
>
> **理论变体**：Lean 4（v4.34.0）内核，加 Mathlib（`5ed29652`）与 FormalizedFormalLogic/Foundation（`1fb01b72`）。经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。对象是 Foundation 中的一阶 `𝗭𝗙𝗖`（ℒₛₑₜ、LK）与 `𝗣𝗔`（ℒₒᵣ）。不涉及 HoTT 路径。
>
> **身份**：机器证明，范围见 §4。从“在每个模型中成立”到“𝗭𝗙𝗖 可证”，用的是 Foundation 在 Lean 中证明的一阶完备性定理（`SetTheory.complete`），这是元层定理。

## 0. 这一条在研究里的位置

- 【原话】十三条 [1]（KC-000063）：研究发起人设想的 Q0（H0（Z0）），即 H0 在 ZFC 中的对应物 Z0。CG-005 把 Z0 取为“ZFC 对自身矛盾的逐步搜索”；它与 H0 逐字段同形，差别在于 HoTT 看得见自己追问的永不停（C-78），ZFC 看不见自己的（哥德尔第二定理）。
- C-103（CG-006）把“ZFC 看不见”化成了两条精确前提：`Sh.RE` 与 `𝗜𝚺₁ ⪯ Sh`。本包证明了后一条，所以 Z0 现在只剩一条前提。
- 【解释】一句话：在 ZFC 的任何一个模型里，自然数（ω）都满足全部皮亚诺公理，连同对任意性质的数学归纳；所以 ZFC 能证明皮亚诺算术的每一个定理。

## 1. 记号

- `arithTrln`、`N M := arithTrln.Model M`、`Sh := {σ ∣ 𝗭𝗙𝗖 ⊢ σᵗ}`，同 `../godel-q-zfc-z0/CLAIM.md`。
- `W M`：与 `N M` 同一个 ω，取 Foundation 的标准 ℒₒᵣ 解释，即 `ORingStructure`：0 = ∅，1 = succ ∅，加乘取 ω 上的递归，`<` 取 `∈`。
- `theta : N M ≃ W M`：恒等双射，保持全部函数与关系，于是两者满足同样的公式（S4 的 `eval_equiv_iff`）。

## 2. 精确命题（类型逐字见 `GodelQ/ZFC/QualificationZ0PA.lean`）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-109 | `qual_C109` | (1) 对每个 `M ⊧ 𝗭𝗙𝗖`，`(N M) ⊧* 𝗣𝗔`；(2) 直接解释 `paInterp : 𝗭𝗙𝗖 ⊳ 𝗣𝗔`（翻译仍是 `arithTrln`）；(3) `𝗣𝗔 ⊢ σ → 𝗭𝗙𝗖 ⊢ σᵗ`。 |
| CG001-C-110 | `qual_C110` | (1) `𝗣𝗔 ⪯ Sh`；(2) `𝗜𝚺₁ ⪯ Sh`，即 C-103 的第二条前提成为定理；(3) 在 `[Sh.RE]` 下，`𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ` 且 `Sh ⊬ Sh.craig.consistent`。 |

## 3. 证明的结构

1. **ω 上的算术律**（`GodelQ/ZFC/OmegaLaws.lean`）：
   - 在任意 `V ⊧ 𝗭` 中，对 ω 的元素证明加法的交换、结合，乘法的交换、结合，分配律，以及各条序公理；
   - 每条用 Foundation 的 `naturalNumber_induction`。归纳谓词的 ℒₛₑₜ 可定义性由登记加法、乘法为可定义的二元函数后的 `definability` 给出；
   - 序的部分用 Foundation 的 `Ordinal.lean`：ω 的元素是序数，∈ 三分、传递、反自反。
2. **𝗣𝗔⁻**（`PAModel.lean`，`models_PeanoMinus_W`）：在 `W M` 上，17 条公理化成 ω 上的算术律，逐条支付；等号公理由 Foundation 自动给出。
3. **归纳模式**（`W_induction`、`models_succInd_W`）：
   - 任一算术公式 φ（带参数）在 ω 上定义的谓词，等于 φ 的翻译在 M 中定义的谓词（`indPred_iff`，用 Foundation 的 `eval_translate_iff`）；
   - 于是它 ℒₛₑₜ 可定义（`indPred_definable`）；
   - 经 `naturalNumber_induction`（分离取成集合，ω 是最小的归纳集）得到归纳实例。
4. **传回 `N M`**（`models_N_iff`）与解释：`models_PA`、`paInterp`。完备性定理 `SetTheory.complete` 把“每个模型中成立”化成“𝗭𝗙𝗖 可证”，与 S3 的 `arithInterp : 𝗭𝗙𝗖 ⊳ 𝗥₀` 同一条路线。
5. **接到 Z0**（`Z0PA.lean`）：
   - `PA_le_Sh` 由 `paInterp` 与 `Sh_provable_iff` 得到；
   - `ISigma1_le_Sh` 由 Foundation 的 `𝗜𝚺₁ ⪯ 𝗣𝗔` 传递得到；
   - `zfc_z0_of_RE` 就是 C-103 的 `zfc_z0_conditional`，只是 `𝗜𝚺₁ ⪯ Sh` 的实例现在由定理提供。

## 4. 还差什么（Z0 的剩余两步）

- **`Sh.RE`**（CG-007 W4）：要证 `σ ↦ 𝗭𝗙𝗖 ⊢ σᵗ` 可枚举。𝗭𝗙𝗖 的可证性已是 Σ1（C-95、C-97）；缺翻译 `arithTrln.translate` 的可计算性，或它的内部 Σ1 定义。
- **内部化**（CG-007 W8）：结论里的一致性句是“Sh（经 Craig 公理化）不矛盾”。要读成“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”，需要在 𝗜𝚺₁ 中证明 Con(𝗭𝗙𝗖) → Con(Sh.craig)，即“Sh 的证明可以翻译成 𝗭𝗙𝗖 的证明”的内部版本。

## 5. 负控制

| proof id | 文件 | 去掉的前提 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-PA-NEG-RE-001` | `GodelQ/Negative/WrongZ0WithoutRE.lean` | `Sh.RE`（`𝗜𝚺₁ ⪯ Sh` 已是定理） | 拒绝：实例 `Theory.RE Sh` 找不到。本包没有证明 `Sh.RE`，剩下的这条前提确实被用到。 |

## 6. 文件

- 下列 17 个文件逐字节复制，复制时核对过：
  - 16 个来自 `../godel-q-zfc-z0/GodelQ/`（含 `ZFC/Z0Shadow.lean`）；
  - `GodelQ/ZFC/Soundness.lean` 来自 `../godel-q-zfc/`。
- 新文件：`GodelQ/ZFC/OmegaLaws.lean`、`PAModel.lean`、`Z0PA.lean`、`QualificationZ0PA.lean`、`GodelQ/Negative/WrongZ0WithoutRE.lean`。

## 7. 禁止外推

1. 不推出 ZFC ⊢ ⊥。
2. 不推出 Z0 对 𝗭𝗙𝗖 已经成立：还差 `Sh.RE` 与内部化（§4）。
3. “ZFC 解释 PA”是经典事实，新的是在 Foundation 中把它形式化，并接到 C-103 上。
4. 完备性定理与模型都在 Lean 元层；结论 `𝗭𝗙𝗖 ⊢ σᵗ` 是关于形式可证性的陈述，它的证明经过了元层的模型论证。
5. 没有做过文献查重。
