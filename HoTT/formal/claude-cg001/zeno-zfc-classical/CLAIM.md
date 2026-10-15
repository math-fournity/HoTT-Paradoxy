# CG001-C-423：经典芝诺的两句落到 Foundation 的 𝗭𝗙𝗖

> **证明包**：`MP-CG001-ZENO-ZFC-CLASSICAL-001`（`GodelQ/Zeno/QualificationZenoZFC.lean`）；负控制 `MP-CG001-ZENO-ZFC-CLASSICAL-NEG-001`。
>
> **目标包**：CG-010（worktree `claude/012-opus-w8` 中的 `.claude/goals/CG-010-remaining-formalization-alignment/`），R1。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。
>
> **理论变体**：Lean 4（v4.34.0）内核，加 Mathlib（`5ed29652`）与 FormalizedFormalLogic/Foundation（`1fb01b72`）。经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。𝗭𝗙𝗖 是 Foundation 中的一阶理论（ℒₛₑₜ 语法、LK 证明系统）。不涉及 HoTT 路径。
>
> **身份**：机器证明，范围见 §2、§5。𝗭𝗙𝗖 的一致性由 Lean 元层的 `Universe` 模型提供（Foundation `zfc_consistent`），只用于 (3)。

## 0. 这一条在研究里的位置

- **缺口表第 9 行**（`形式化追踪/README.md`）原先写着：经典芝诺上，“极限是 1”与“任何有限步都到不了 1”这两句，𝗭𝗙𝗖 都证得出，但只是数学上显然，没有单独机器核对。
- **CN-076 §6 第 1 条**提议用算术写法、经 C-109 落到 𝗭𝗙𝗖。
- 研究发起人 2026-10-14 给出 Q 的定义【原话】：“ZFC缺的Q，是一种对数学理论M的观察力，这种观察力就是对某种存在于理论M中的表述L是否是“可计算的、可停机的”的判断。”在这个读法下，本包落实的是：𝗭𝗙𝗖 看得见过程的两面，缺的是门口那一问（ASK），不是眼睛。见 CN-080 第 3 处、CG-010 `认知对齐.md` §2。

## 1. 记号

- `halvedC K n := K ≤ n`：到第 n 步，跑者至少已减半 K 次，即剩余距离 (1/2)ⁿ ≤ 2⁻ᴷ。经典芝诺没有驱动过程，每一步都减半。这是 W5（C-117）`halvedF` 去掉驱动之后的样子。
- `arriveC := ∀K ∃N ∀n (N ≤ n → halvedC K n)`：极限意义的到达，即剩余距离趋于 0 的 ε–N 写法，ε 取 2⁻ᴷ。
- `noFiniteC := ¬∃n ∀K halvedC K n`：没有哪一步余量为零。余量为零，就是对每个 K 都已减半 K 次。
- `arithTrln`：W1–W8 共用的翻译，把算术句译到 ℒₛₑₜ（数字为 ω 的元素）。

## 2. 精确命题（类型逐字见 `GodelQ/Zeno/QualificationZenoZFC.lean`）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-423 | `qual_C423` | (1) `𝗭𝗙𝗖 ⊢ arriveCᵗ`；(2) `𝗭𝗙𝗖 ⊢ noFiniteCᵗ`；(3) `𝗭𝗙𝗖 ⊬ ∼ noFiniteCᵗ`，即 𝗭𝗙𝗖 证明不了“有一步余量为零”；(4) 实数读法：(1/2)ⁿ ≤ (1/2)ᴷ ⟺ K ≤ n；(5) (1/2)ⁿ → 0；(6) 每一步 (1/2)ⁿ > 0 |

- (1)(2) 的证明是语义的：
  - 在每一个 𝗣𝗔⁻ 模型里两句都成立（`models_arriveC` 取 N = K；`models_noFiniteC` 取 K = n + 1）；
  - 𝗭𝗙𝗖 每个模型的 ω 满足 𝗣𝗔（C-109 的 `models_PA`，经 `models_N_iff` 换到标准 ℒₒᵣ 结构）；
  - 再用 Foundation 的完备性 `SetTheory.complete`。
- (3) 由 (2) 与 𝗭𝗙𝗖 的一致性得到。

## 3. 承接了原话的哪一部分

- 【证明】经典芝诺的过程两面，𝗭𝗙𝗖 都证得出：极限意义上“到了”，以及哪一步都没到。它也绝不会证出“在某一步到了”。
- 【判断】所以经典芝诺上，“ZFC 缺 Q”不是缺证明能力（眼睛），而是缺 ASK：在把“极限意义的到达”当作“原过程走完”之前，先问过程走不走得完。研究发起人 KC-000068 说“因为Q是缺失性的，所以无从拒绝P”，按这个读法成立：两句 𝗭𝗙𝗖 都有，却没有一道门要求它在两者之间作取舍。
- **没有承接**：
  - “所有步之后那一刻”（时刻 1）与连续性，即 A 在芝诺上的落点（C-106–C-108、C-116 在 Mathlib 里），不在这个算术写法之内；
  - 实数在 ℒₛₑₜ 中的构造（缺口表第 2 行，CG-010 R7）。这里的精度 ε 取 2⁻ᴷ，用的是整数写法。

## 4. 负控制

| proof id | 文件 | 被否定的说法 | 预期 |
|---|---|---|---|
| `MP-CG001-ZENO-ZFC-CLASSICAL-NEG-001` | `GodelQ/Negative/WrongFiniteArrival.lean` | 每一个 𝗣𝗔⁻ 模型里都有一步余量为零（取第 0 步） | 拒绝：要证每个 K 都等于 0（K ≤ 0），证不出；正面定理 `models_noFiniteC` |

## 5. 文件与禁止外推

- **逐字节复制**：18 个依赖模块，复制自 `../godel-q-zfc-runner-arrival/GodelQ/`，复制时核对过 SHA-256：
  - `ProcessObservation`、`EffectiveTheory`、`GodelZenoRunner`、`FoundationArith`；
  - `ZFC/` 下的 OmegaArith、ArithInterp、OmegaLaws、SetLanguage、SchemaDelta1、ReplacementDelta1、ZFCDelta1、NumeralCode、NeverRE、NumeralSemantics、R0Model、Effective、Soundness、PAModel。
- **新文件**：
  - `GodelQ/Zeno/ZenoClassicalZFC.lean`：两句、模型、𝗭𝗙𝗖；
  - `GodelQ/Zeno/ZenoReading.lean`：实数读法；
  - `GodelQ/Zeno/QualificationZenoZFC.lean`：命题对照；
  - `GodelQ/Negative/WrongFiniteArrival.lean`：负控制。
- **禁止外推**：
  1. 不推出 ZFC ⊢ ⊥。
  2. (3) 依赖 Lean 元层的 `Universe` 模型给出的一致性，不是 𝗭𝗙𝗖 内部的事实。
  3. “缺的是门不是眼”是判断，不是定理；𝗭𝗙𝗖 没有“任务要哪一种完成”的语句，这一点是元层的观察。
  4. 数学内容是平凡的。新的是它在真实的 𝗭𝗙𝗖 上被机器核对，并接到研究发起人的 Q（ASK）上。
