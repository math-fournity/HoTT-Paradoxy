# CG001-C-429：𝗭𝗙𝗖 证 Con(𝗣𝗔) 落在哪条义务上——归结、标准模型与“只靠 ω 是 𝗣𝗔 的模型不够”

> **证明包**：`MP-CG001-ZFC-CON-PA-BOUNDARY-001`（`GodelQ/ZFC/QualificationConPA.lean`）；负控制 `MP-CG001-ZFC-CON-PA-BOUNDARY-NEG-001`。
>
> **目标包**：CG-010（worktree `claude/012-opus-w8`）R8。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。
>
> **理论变体**：Lean 4（v4.34.0）内核，加 Mathlib（`5ed29652`）与 FormalizedFormalLogic/Foundation（`1fb01b72`）。经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。𝗭𝗙𝗖 与 𝗣𝗔 都是 Foundation 中的一阶理论。不涉及 HoTT 路径。
>
> **身份**：机器证明，但**不是** “𝗭𝗙𝗖 ⊢ Con(𝗣𝗔)”本身。那是经典定理，本包没有证出它；本包证明的是它归结成哪条义务，以及那条义务不能怎样付。CG-010 R8 据此标为 **BLOCKED**，剩余义务见 §4。

## 0. 这一条在研究里的位置

- CN-079 §6 第 2 条（Claude 的建议）：把“A 把不停机往上搬”的第一级落到 Foundation 的 𝗭𝗙𝗖 上。这一级就是 𝗭𝗙𝗖 证明 𝗣𝗔 一致。
- CN-079 的读法（【判断】，待研究发起人确认）：
  - 𝗣𝗔 的矛盾搜索永不停，𝗣𝗔 自己证不出这一点（第二不完备）；
  - 𝗭𝗙𝗖 把 ω 当作一个现成的集合，在它上面定义真值，于是证得出；
  - 𝗭𝗙𝗖 自己的矛盾搜索，它又证不出（C-417）。
- CG-010 `方案.md` R8 写明：工作量大，Foundation 只有 ZF 的基础文件；做不完就在真实尝试之后写明阻塞与精确的剩余义务。本包是那次尝试的机器部分。

## 1. 记号

- `conPA`：Foundation 的 𝗣𝗔 一致性句（Π1 算术句“𝗣𝗔 证不出 ⊥”，用 𝗣𝗔 的 Δ1 公理化与内部可证性写成）。
- `arithTrln.translate`：把算术句译到 ℒₛₑₜ（ω 上的解释）。
- `W M`：𝗭𝗙𝗖 的模型 M 中的 ω，作为算术结构（C-109）。
- `Universe`：Foundation 在 Lean 元层构造的 𝗭𝗙𝗖 的标准模型。

## 2. 精确命题（类型逐字见 `GodelQ/ZFC/QualificationConPA.lean`）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-429 | `qual_C429` | (1) `𝗭𝗙𝗖 ⊢ (conPA)ᵗ` 当且仅当 𝗭𝗙𝗖 的每个模型 M 都有 `W M ⊧ conPA`；(2) 𝗭𝗙𝗖 每个模型的 `W M` 都是 𝗣𝗔 的模型（C-109）；(3) `Universe ⊧ (conPA)ᵗ`；(4) `𝗭𝗙𝗖 ⊬ ∼(conPA)ᵗ`，𝗭𝗙𝗖 驳不倒它；(5) 并非每个 𝗣𝗔 的模型都满足 `conPA` |

公理报告：全部定理只用三条标准公理。

## 3. 证明思路

- **(1)**：
  - ⇒ 是可靠性：模型满足 𝗭𝗙𝗖 的定理，翻译解释与 `W M` 同真；
  - ⇐ 是 𝗭𝗙𝗖 的完备性（`SetTheory.complete`），同 C-423 的路线。
- **(3)**：`Universe` 的 ω 与 ℕ 同构（C-100 的 `natEquivN`），所以与 ℕ 满足同样的算术句。ℕ 是 𝗣𝗔 的模型，所以 𝗣𝗔 一致，于是 ℕ 满足 `conPA`（Foundation 的 `standard_consistent`）。
- **(4)**：由 (3)，且 `Universe` 是 𝗭𝗙𝗖 的模型。
- **(5)**：𝗣𝗔 证不出自己一致（Foundation 的 `consistent_unprovable`，第二不完备），由算术的完备性（`Arithmetic.complete`），有 𝗣𝗔 的模型不满足 `conPA`。

## 4. 卡在哪：剩余的义务

由 (1)，“𝗭𝗙𝗖 ⊢ Con(𝗣𝗔)”恰好等于：

> **义务 O**：对 𝗭𝗙𝗖 的每个模型 M，`W M ⊧ conPA`，即 ω^M 里没有 𝗣𝗔 对 ⊥ 的（内部编码的、可以是非标准的）证明。

- 由 (2)(5)，O 不能只用“ω^M 是 𝗣𝗔 的模型”来证，要用 M 里的集合。
- 由 (3)，O 在标准模型上成立，难处全在非标准的 M。
- 负控制把 ℕ 上的证明照搬到任意 𝗣𝗔 模型，被拒绝，类型是 `Consistent ℕ` 对 `Consistent V`。

经典的证法（文献，凭记忆，未核对出处）在 M 内部走三步。每一步在 Foundation 里都没有现成结果：

1. **O1 内部满足关系**：用 M 的递归（Foundation 有 `SetTheory.Recursion`、`NaturalNumberRec`），对 ω^M 中全部内部公式编码定义满足关系 Sat，这是 M 里的一个集合，满足塔斯基条件。要在 Foundation 的内部语法（`Bootstrapping` 的编码，在 `W M` 里）与 M 的集合之间搭桥。
2. **O2 公理都满足**：𝗣𝗔 的每个内部公理编码都在 Sat 里，包括非标准的归纳实例。这要用两件事：Sat 是 M 里的集合（分离公理）；ω^M 的每个非空子集在 M 里有最小元。
3. **O3 内部可靠性**：Foundation 的内部推导（内部 LK、内部代换）保持 Sat。要对推导编码在 M 里归纳，并证明内部代换引理。W8 的 D3 处理过同类的内部代换（`iT_subst_open` 一族），那一项用了多日。

**估计**：O1–O3 合起来的工作量，大于 W8 的 D3。本包照实标为 BLOCKED，不为凑完成去改命题。

## 5. 与已有命题和文献的关系

- **C-109**：(2)。**C-100**：`Universe` 的 ω 与 ℕ 同构。**C-417**：𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)。**C-423**：同一条完备性路线。
- **文献**（凭记忆，未核对）：𝗭𝗙 ⊢ Con(𝗣𝗔) 是集合论与模型论教材里的标准结果（ω 是 𝗣𝗔 的模型，加上可靠性定理在 𝗭𝗙 内部的形式化）。

## 6. 负控制

| proof id | 文件 | 被否定的说法 | 预期 |
|---|---|---|---|
| `MP-CG001-ZFC-CON-PA-BOUNDARY-NEG-001` | `GodelQ/Negative/WrongEveryPAModelCon.lean` | 每个 𝗣𝗔 的模型都满足 Con(𝗣𝗔)：照搬 `nat_conPA` 的证明，把 ℕ 换成任意 𝗣𝗔 模型 V | 拒绝：类型不符，`Theory.Consistent ℕ 𝗣𝗔` 不是 `Theory.Consistent V 𝗣𝗔`；这个说法本身是错的（(5)，`pa_model_refutes_conPA`） |

## 7. 文件

- **逐字节复制，复制时核对过 SHA-256**：18 个模块，来自 `../godel-q-zfc-runner-arrival/GodelQ/`。与 `zeno-zfc-classical` 用的是同一组。
- **新文件**：
  - `GodelQ/ZFC/ConPABoundary.lean`：(1)–(5) 的证明；
  - `GodelQ/ZFC/QualificationConPA.lean`：命题对照；
  - `GodelQ/Negative/WrongEveryPAModelCon.lean`：负控制。
- `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`：固定的 Lean 文件与导入闭包（1,893 个模块）的逐模块哈希。

## 8. 禁止外推

1. **本包没有证明 𝗭𝗙𝗖 ⊢ Con(𝗣𝗔)。** 那是文献结果；在本仓库里它是 BLOCKED，剩余义务见 §4。
2. (3)(4) 依赖 Lean 元层的 `Universe` 模型，不是 𝗭𝗙𝗖 内部的事实。
3. 不推出 ZFC ⊢ ⊥。
4. “A 把不停机往上搬”是 CN-079 的读法，不是定理。
