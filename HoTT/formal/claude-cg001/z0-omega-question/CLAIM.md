# CG001-C-427：Z0 作为具体的 ω 追问——𝗭𝗙𝗖 每一刻都确认“还没找到矛盾”，却证明不了“永远找不到”

> **证明包**：`MP-CG001-Z0-OMEGA-QUESTION-001`（`GodelQ/ZFC/QualificationZ0Omega.lean`）；负控制 `MP-CG001-Z0-OMEGA-QUESTION-NEG-001`。
>
> **目标包**：CG-010（worktree `claude/012-opus-w8`）R9。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。
>
> **理论变体**：Lean 4（v4.34.0）内核，加 Mathlib（`5ed29652`）与 FormalizedFormalLogic/Foundation（`1fb01b72`）。经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。𝗭𝗙𝗖 是 Foundation 中的一阶理论。不涉及 HoTT 路径。
>
> **身份**：机器证明，范围见 §2、§8。“Z0 就是 𝗭𝗙𝗖 对自身矛盾的搜索”是 CG-005 以来的读法；研究发起人的原话只说 Z0 是“H0在ZFC中的对应物”（§0）。

## 0. 这一条在研究里的位置

- 研究发起人十三条 [1]（KC-000063）【原话】：“而且某种意义上我们甚至还可以找到Q0（H0（Z0）），意思就是Q0是ZFC的Q，其实对应了H0在ZFC中的对应物Z0。”
- 缺口表第 3 行：“同一个 Q 只到图式”。
  - C-93（Lean）把芝诺、H0、Z0 放进同一个 ω 追问图式，但 Z0 只以“某个过程”的形式出现；
  - C-112、C-113（Cubical Agda）里，Z0 是参数。
  - 此后 C-417 证明了 𝗭𝗙𝗖 证明不了自己一致（Foundation 的一致性句的翻译），但那里没有把 Z0 写成一个逐步的追问。
- 本包把 Z0 写成 Lean 里一个具体的 ω 追问，与芝诺用同一个类型、同一个图式，并接上 C-417。

## 1. 记号

- `Process`、`Done`、`DoneBy`：过程（部分递归代码）、停机、在 k 步内停机（C-84 起）。
- `OmegaQuestion`、`processQ`、`zenoQ`：C-93 的 ω 追问、过程的停机追问、经典芝诺（`godel-q/GodelQ/OmegaQuestion.lean`，逐字节复制）。
- `zfcEffective`：𝗭𝗙𝗖 作为有效理论（C-105）。`provesNotYet e k` 即 `𝗭𝗙𝗖 ⊢ haltsS ΨN ⌜(e, k)⌝`：𝗭𝗙𝗖 证明“e 在 k 步内尚未停机”。
- `z0Code`：一个程序，按编号逐个检查 𝗭𝗙𝗖 的证明，找到 ⊥ 的证明就停。
  - 它的存在来自 C-111 的 `zfc_provable_re`（𝗭𝗙𝗖 的定理集可枚举），用 `Classical.choose` 取定；
  - 本包只用到它的规格 `Done z0Code ↔ 𝗭𝗙𝗖 ⊢ ⊥`，没有把代码逐条写出。
- `z0Q := processQ z0Code`：第 k 问是“到第 k 步，找到 𝗭𝗙𝗖 的矛盾了吗”。
- `𝗭𝗙𝗖.consistent`：Foundation 的一致性句（Π1 算术句，“没有 ⊥ 的证明”）；`arithTrln.translate` 把它译到 ℒₛₑₜ。

## 2. 精确命题（类型逐字见 `GodelQ/ZFC/QualificationZ0Omega.lean`）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-427 | `qual_C427` | (1) `Done z0Code ↔ 𝗭𝗙𝗖 ⊢ ⊥`；(2) `z0Q.Done ↔ 𝗭𝗙𝗖 ⊢ ⊥`；(3) `z0Q.Never`，Z0 永不落定；(4) 对每个 k，𝗭𝗙𝗖 证明“Z0 到第 k 步还没找到矛盾”；(5) 一致性句在 ℕ 中为真，当且仅当 `z0Q.Never`；(6) `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ`（C-417，导入）；(7) P_fin 在 Z0 上被否定：任何“形式上完成的整体”都推不出 Z0 在某一步完成；(8) 由 Z0 驱动的哥德尔–芝诺跑者到达；(9) 同一个类型里，芝诺与 Z0 都永不落定 |

公理报告：全部定理只用三条标准公理。

## 3. 证明思路

- **(1)**：𝗭𝗙𝗖 的定理集可枚举（C-111），在 ⊥ 处取它的半判定程序，再用 Mathlib 的 `Code.exists_code` 取一个代码。
- **(2)**：C-93 的 `processQ_done_iff`。
- **(3)**：𝗭𝗙𝗖 一致（Foundation 的 `zfc_consistent`），所以 (1) 的右边不成立。
- **(4)**：C-105 的 `zfcEffective` 对每个不停机的过程、每个 k，都证明“尚未停机”（Δ0 完全性）。
- **(5)**：Foundation 的 `consistent.defined` 与 `provable_iff_provable`：一致性句在 ℕ 中为真，就是 ℕ 里没有 ⊥ 的证明，也就是 𝗭𝗙𝗖 ⊬ ⊥；再用 (2)。
- **(6)**：C-417 的 `zfc_z0_unconditional`，本包导入它所在的全部模块。
- **(7)(8)(9)**：C-93 的 `P_fin_refuted`、`processQ_never_iff_arrives`、`zenoQ_never`。

## 4. 承接了原话的哪一部分

- 【证明】Z0 不再是参数或抽象的“某个过程”。它是 Lean 里一个具体的 ω 追问，与芝诺用同一个类型：
  - 𝗭𝗙𝗖 对它每一刻都确认“还没找到矛盾” (4)；
  - 它永不落定 (3)；
  - 在 ℕ 中说“它永不落定”的那句话，𝗭𝗙𝗖 证明不了 (5)(6)。
- 【判断】三个实例放在一起，差别在“理论能不能证明‘永不’”：

  | 实例 | 每一刻 | “永不” | 依据 |
  |---|---|---|---|
  | 芝诺 | 𝗭𝗙𝗖 证得出“每一步都还没到” | 𝗭𝗙𝗖 证得出“没有哪一步余量为零”，同时宣布极限意义的到达 | C-423 |
  | Z0 | 𝗭𝗙𝗖 证得出“到第 k 步还没找到” | 𝗭𝗙𝗖 证不出 | 本包 (4)(5)(6)，C-417 |
  | H0 | HoTT 每一问都答“否” | HoTT 证得出它永不停 | C-78，C-426 (3) |

  - Z0 是三者里唯一“每一刻都看得见、‘永不’却看不见”的。按研究发起人的 Q = ASK（门口那一问：这个过程停不停得下来），𝗭𝗙𝗖 对自己的矛盾搜索恰好问不出答案。
  - 经典逻辑照样认定这个答案：一致性句在 ℕ 中为真 (5)。这就是 CN-080 说的“A 型的真”。
- 【判断】这与 C-112、C-113 `CLAIM.md` §3 记下的不对称一致：HoTT 在自己的内核里证明 H0 永不落定，𝗭𝗙𝗖 证明不了 Z0 的。现在 Z0 一侧是具体的。
- **没有承接**：
  - “永不停机”句的程序形式（`neverS ΦH ⌜z0Code⌝`）与 Foundation 一致性句的翻译，在 𝗭𝗙𝗖 内部是否可证等价，本包没有证明。所以 𝗭𝗙𝗖 证不出的，本包只对后者写出（C-417）。负控制只说明“每一刻的确认合起来就是‘永不’的证明”这一步不能直接走。
  - “同一个 Q”在完整任务合同下的“相同”（缺口表第 3 行，CG-010 D2）。
  - Z0 与 Agda 里的 H0 之间仍是跨内核的对应，不是同一个对象。

## 5. 与已有命题的关系

- **C-93**：图式与芝诺实例，本包把 Z0 实例化。
- **C-105**：`zfcEffective` 及其 Δ0 完全性。
- **C-111**：𝗭𝗙𝗖 的定理集可枚举。
- **C-417**：𝗭𝗙𝗖 证明不了自己一致。
- **C-423**：经典芝诺两句在 𝗭𝗙𝗖 里都证得出（对照表）。
- **C-78、C-112、C-113、C-426**：H0 一侧。

## 6. 负控制

| proof id | 文件 | 被否定的说法 | 预期 |
|---|---|---|---|
| `MP-CG001-Z0-OMEGA-QUESTION-NEG-001` | `GodelQ/Negative/WrongStagesMakeNever.lean` | 𝗭𝗙𝗖 每一刻的确认合起来就是对“Z0 永不停机”的证明（把 (4) 直接交作 `provesNever`） | 拒绝：类型不符，`∀ k, provesNotYet z0Code k` 不是 `provesNever z0Code` |

## 7. 文件

- **逐字节复制，复制时核对过 SHA-256**：
  - 32 个模块，来自 `../godel-q-zfc-z0-sigma1/GodelQ/`（不含负控制），提供 C-105、C-111、C-417；
  - `GodelQ/OmegaQuestion.lean`，来自 `../godel-q/GodelQ/`（SHA-256 `7dafb0fa…`），提供 C-93。
- **新文件**：
  - `GodelQ/ZFC/Z0OmegaQuestion.lean`：Z0 的程序与 ω 追问，(1)–(5)(8)；
  - `GodelQ/ZFC/QualificationZ0Omega.lean`：命题对照；
  - `GodelQ/Negative/WrongStagesMakeNever.lean`：负控制。
- `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`：固定的 Lean 文件与导入闭包（1,893 个模块）的逐模块哈希。

## 8. 禁止外推

1. 不推出 ZFC ⊢ ⊥。
2. (3)(5) 的“永不落定”“在 ℕ 中为真”依赖 𝗭𝗙𝗖 的一致性，它来自 Lean 元层的 `Universe` 模型，不是 𝗭𝗙𝗖 内部的事实。
3. “Z0 就是 𝗭𝗙𝗖 对自身矛盾的搜索”是读法，不是研究发起人的定义；“同一个 Q”的“相同”待研究发起人定义。
4. `z0Code` 由 `Classical.choose` 取定，只知道它的规格，没有逐条写出代码。
5. 程序形式的第二不完备（𝗭𝗙𝗖 ⊬ `neverS ΦH ⌜z0Code⌝`）没有在本包证明。
