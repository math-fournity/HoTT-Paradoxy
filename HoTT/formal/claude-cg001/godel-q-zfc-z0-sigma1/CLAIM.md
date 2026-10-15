# CG001-C-413–C-417：经翻译的形式化 Σ1 完全性、D3 与不带前提的完整 Z0

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-SIGMA1-001`；负控制 `MP-CG001-GODEL-Q-ZFC-Z0-SIGMA1-NEG-BALL-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W8；本机会话 95a1a81b（012-Opus，Opus 5.5），2026-10-14，独立 worktree `/Volumes/D/HoTT-worktrees/012-opus-w8`（分支 `claude/012-opus-w8`）。研究发起人 2026-10-08【原话】“按照你的想法进行优先级安排，完成后续所有“形式化和机器证明”工作。”
>
> **理论变体**：同 `../godel-q-zfc-z0-translate/`：Lean 4（v4.34.0）加 Mathlib（`5ed29652`）与 Foundation（`1fb01b72`），经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。
>
> **身份**：机器证明（范围见 §4、§5）。C-417 是 W8 的目标定理 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ`，不带任何未证前提。
>
> **编号**：接本 worktree 的 C-410–C-412。2026-10-14 核对了全部分支与全部 worktree 的 `CLAIM_EVIDENCE_MATRIX.md`、`CLAIM_NAMESPACE_LEDGER.md`：舰队最高到 C-406，`dev` 到 C-401，没有别处用过 C-413–C-417。

## 0. 位置

- `dev` 的 `Z0Full.lean` 已把完整 Z0 归结为一个前提：定理 `zfc_z0_full_of_D3_internalize` 的 `h`，即对 𝗜𝚺₁ 的每个模型 V 与每个算术句 τ，在 V 中“𝗭𝗙𝗖 证明 τ 的翻译 ⟹ 𝗭𝗙𝗖 证明 `zfcTr τ` 的翻译”。这是可证性谓词 `zfcTr` 的 D3 的内化形式。
- `zfcTr τ` 是 Σ1 句（`zfcTr_sigma1`）。所以只需“经翻译的形式化 Σ1 完全性”：在每个 V 中，真的 Σ1 句，它的翻译 𝗭𝗙𝗖 可证。
- 本包照 Foundation `D3.lean` 的 `bold_sigma_one_complete` 证明它，对标准 Σ1 公式作元层归纳。与算术的差别有两处：
  - 集合语言没有函数符号，一个数 a ∈ V（可以非标准）不能用项命名。本包改用 Rayo 式数字公式 N_a：N_0(z) = ∀u(u ∉ z)，N_{a+1}(z) = ∃y(N_a(y) ∧ z = y ∪ {y})（`NumeralCode.lean` 的 `numCode` 在 V 中的有型版本 `numF`）。
  - 参数不用代入，改成“自由变量加假设”：把公式的第 i 个约束变量换成项 e i，并在上下文 Γ 中假设 N_{w i}(e i)（`NumHyp`）。
- 舰队的路线是把推导逐条翻译。它的归纳不变量在 ℕ 中就不成立（C-410–C-412，`../godel-q-zfc-z0-freevar/`）。本包不走那条路线。

## 1. 精确命题

记 `Z V := 𝗭𝗙𝗖.internalize V`（V 中的“𝗭𝗙𝗖 可证”）。`Γ ⊢[Z V] φ` 是 Foundation 的有限上下文可证性。ω、加法 `Add`、乘法 `Mul` 都取翻译 `arithTrln` 所用的定义（`ArithInterp.lean`）。以下各条都对 𝗜𝚺₁ 的每个模型 V 成立。

| 编号 | 定理（文件） | 内容 |
|---|---|---|
| CG001-C-413 | `numF_exists`、`numF_dom`、`numF_uniq`、`numF_congr`（`SetNum.lean`）；`numF_add`、`numF_mul`、`numF_lt`、`numF_nlt`、`numF_neq`（`SetNumArith.lean`）；`numF_add_rev`、`numF_mul_rev`（`TransTerm.lean`） | 对 V 中任意的 a、b、d（可以非标准），`Z V` 证明下列各条。<br>• 存在：∃x N_a(x)。<br>• 属于 ω：∀x(N_a(x) → x ∈ ω)。<br>• 唯一：∀x y(N_a(x) → N_a(y) → x = y)。<br>• 相合：∀x y(x = y → N_a(x) → N_a(y))。<br>• 加法：∀z x y(N_a(x) → N_b(y) → Add(z,x,y) → N_{a+b}(z))，以及反向 ∀z x y(N_a(x) → N_b(y) → N_{a+b}(z) → Add(z,x,y))。<br>• 乘法：同加法，两个方向。<br>• 小于：∀x y(N_a(x) → N_{a+d+1}(y) → x ∈ y)。<br>• 不小于（b ≤ a 时）：∀x y(N_a(x) → N_b(y) → ¬ x ∈ y)。<br>• 不等（a ≠ b 时）：∀x y(N_a(x) → N_b(y) → ¬ x = y)。 |
| CG001-C-414 | `term_ve`（`TransTerm.lean`），形状引理 `veF_bvar`、`veF_func0`、`veF_func2`、`veF_bShift`、`trRel2`（`TransTyped.lean`） | 设 t 是有 n 个变量的标准算术项，w : Fin n → V，Γ 是上下文，e 是 n 个项，且对每个 i 有 `Γ ⊢[Z V] N_{w i}(e i)`。记 VE_t(z; e) 为 Foundation 的变量等式 `varEqual t`（翻译中“z 等于 t 的值”），其变量取 e。则：<br>• (ex) `Γ ⊢[Z V] ∃z(z ∈ ω ∧ VE_t(z; e))`；<br>• (ch) 对每个项 z，`Γ ⊢[Z V] VE_t(z; e) → N_{t(w)}(z)`。 |
| CG001-C-415 | `ball_merge`（`TransBall.lean`） | 对 V 中任意的 b、任意的上下文 Γ 与任意的单变量公式 Φ（可含自由变量）：若对每个 i < b 都有 `Γ ⊢[Z V] ∀x(N_i(x) → Φ(x))`，则 `Γ ⊢[Z V] ∀z ∀x(N_b(z) → x ∈ z → Φ(x))`。 |
| CG001-C-416 | `tr_sigma1_complete`、`tr_sigma1_provable`（`TransSigma1.lean`） | 对每个有 n 个变量的 Σ1 算术公式 φ（`ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ`）与 w : Fin n → V：若 `V ⊧/w φ`，则对满足上面假设的每个 Γ、e，`Γ ⊢[Z V] ⌜φᵗ⌝[e]`。句子形式：若 σ 是 Σ1 句且 V ⊧ σ，则 `Z V ⊢ ⌜σᵗ⌝`。φᵗ 是 `arithTrln.translate φ`。 |
| CG001-C-417 | `zfcTr_D3`、`zfc_z0_unconditional`（`Z0D3.lean`） | (1) 对每个 V 与每个算术句 τ：`Provable 𝗭𝗙𝗖 ⌜τᵗ⌝ → Provable 𝗭𝗙𝗖 ⌜(zfcTr τ)ᵗ⌝`（在 V 中）。<br>(2) `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence)`：𝗭𝗙𝗖 证明不了“𝗭𝗙𝗖 一致”（Foundation 的一致性句）的翻译。 |

## 2. 证明

- **C-413**：凡是不含 N_a 的事实，都是标准 𝗭𝗙𝗖 句，涉及 ω、后继、加法、乘法、等号、∈。这些句子用 `SetTheory.complete` 在 𝗭𝗙𝗖 的每个模型里证明（用 `OmegaArith`、`ArithInterp` 的语义引理），再用 `internal_provable_of_outer_provable` 搬进 V，在自由变量处实例化。含 N_a 的部分在 V 中归纳（`ISigma1.sigma1_succ_induction`）：
  - 存在、属于 ω、唯一、加法、乘法，对 a 或 b 归纳；
  - 小于对 d 归纳；
  - 相合、不小于、不等不归纳。

  归纳谓词“`Z V` 证明某个码”是 Σ1 的，由 `definability` 验证。反向加法与乘法由加法、乘法在 ω 上全定义、N 的唯一性与 Add、Mul 对等号相合得出。
- **C-414**（对项 t 作元层结构递归）：
  - 变量：VE 是 z = e i。(ex) 取 e i 本身为见证；(ch) 用相合。
  - 常数 0、1：变量等式是标准句，直接在模型里证明。
  - 加法、乘法：`veF_func2` 把 VE_{f(u,v)}(z; e) 写成 ∀y₀ y₁((y₀ ∈ ω ∧ VE_u(y₀)) ∧ (y₁ ∈ ω ∧ VE_v(y₁)) → F(z, y₀, y₁))。
    - (ch)：用子项的 (ex) 取 y₀、y₁，用子项的 (ch) 得 N_{u(w)}(y₀)、N_{v(w)}(y₁)，再用 C-413 的正向计算律；
    - (ex)：取第 t(w) 个数作值，用子项的 (ch) 与反向计算律。
  - 形状引理把 Foundation 翻译的有型引号在任意参数代换下写成块的组合。其中 `veF_bShift` 说多出的约束变量不出现在变量等式里，有界 ∀ 的情形要用它。
- **C-415**：对 c ≤ b 在 V 中归纳。c = 0 时用“空集没有元素”；c → c + 1 时用“x ∈ v ∪ {v} 则 x ∈ v 或 v = x”，再分两种情况：一是用归纳假设，二是用 N_c 的相合加上 i = c 的前提。两条事实都是标准句。
- **C-416**：用 `Bounding.Hierarchy.arithmetic_sigma₁_induction'`，共十种情形：
  - ⊤、⊥、∧、∨：直接；
  - 原子 =、<：两次推广后，用 C-414 的 (ch) 得 N_{t₁(w)}(y₀)、N_{t₂(w)}(y₁)，再用 C-413 的唯一性或小于；
  - 否定原子 ≠、≮：用 C-414 的 (ex) 取两个见证，再用 C-413 的不等或不小于；
  - ∃：取第 a 个数为见证（`numF_exists`），参数假设随之扩展（`NumHyp.cons`）；
  - 有界 ∀：对每个 i < t(w)，由归纳假设得 ∀x(N_i(x) → φᵗ(x))，用 C-415 合并；再用 C-414 的 (ex) 与 (ch) 取出界 t 的值 z 和 N_{t(w)}(z)，把 x < t 的翻译实例化成 x ∈ z。
- **C-417**：由 `models_zfcTr_iff`，V ⊧ `zfcTr τ` 当且仅当 `Provable 𝗭𝗙𝗖 ⌜τᵗ⌝`（在 V 中）。`zfcTr τ` 是 Σ1 句，所以由 C-416 得 `Z V ⊢ ⌜(zfcTr τ)ᵗ⌝`，这就是 (1)。把 (1) 代入 `zfc_z0_full_of_D3_internalize`（`Z0Full.lean`，与 `dev` 逐字节相同）即得 (2)。

## 3. 负控制

| proof id | 文件 | 改动 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-SIGMA1-NEG-BALL-001` | `GodelQ/Negative/BallMergeOffByOne.lean` | 与 `ball_merge` 逐字相同的证明脚本，结论里的 N_b 改成 N_{b+1}。前提只覆盖 i < b，结论却要覆盖第 b 个数 | 拒绝：脚本末步 `key b le_rfl` 给出的是关于 N_b 的结论，与 N_{b+1} 不符。这表明合并的界由前提逐一支撑，脚本不会多证 |

## 4. 这说明什么，不说明什么

- **说明**：
  - 可证性谓词 `zfcTr`（“𝗭𝗙𝗖 证明它的翻译”）满足 D3 的内化形式；连同已有的 D1、D2，它满足 Hilbert–Bernays–Löb 条件。
  - 于是 Gödel 第二不完全性对 `Sh`（𝗭𝗙𝗖 的算术影子）成立，翻译回去就是 𝗭𝗙𝗖 证明不了“𝗭𝗙𝗖 一致”的翻译。
  - 这条结论在本仓库此前是条件定理：C-120 只对影子成立，`Z0Full.lean` 的完整形式以 D3 为前提。现在前提已经证出。
- **“不带前提”的含义**：
  - Gödel 第二不完全性需要“被讨论的理论一致”。这一条由 Foundation 的 `zfc_consistent`（Lean 元层的 `Universe` 模型）经 `Sh_consistent`（`Z0Shadow.lean`）提供。
  - 也就是说，Lean 的元理论（带宇宙）证明了 𝗭𝗙𝗖 一致，定理因此不需要把“𝗭𝗙𝗖 一致”写成假设。
  - 这不是 𝗭𝗙𝗖 内部的事实，也不说明 𝗭𝗙𝗖 一致可以在比 Lean 更弱的元理论中得到。
- **不说明**：
  1. 不推出 ZFC ⊢ ⊥，也不推出 𝗭𝗙𝗖 的其他具体不可证性。
  2. 一致性句是 Foundation 的 `𝗭𝗙𝗖.consistent`，用 𝗭𝗙𝗖 的 Δ1 公理化 `ZFCDelta1.ZFC.delta1` 编码，经 `arithTrln` 翻译：定义域 ω，0 ↦ ∅，1 ↦ ∅ ∪ {∅}，加法、乘法取 ω 上的递归定义，= ↦ =，< ↦ ∈。别的编码与别的翻译，本包没有处理。
  3. C-416 是元层定理模式：对每个具体的标准 Σ1 公式 φ（参数可以是 V 中的非标准数）各给一个证明。它不是 𝗜𝚺₁ 内部对“所有 Σ1 公式编码”的断言。
  4. 不涉及舰队的 `ShCraigElim` 与“证明翻译”路线的真假。

## 5. 禁止外推

1. 不把 C-417 说成“𝗭𝗙𝗖 自己证明了自己一致性的不可证性”。(2) 是 Lean 中关于 𝗭𝗙𝗖 的元定理。
2. 不把 Lean 元层的 `Universe` 模型或 `zfc_consistent` 说成 𝗭𝗙𝗖 内部可证的事（同 C-103、C-118）。
3. 不把 C-413 至 C-416 的“`Z V` 证明……”读成标准自然数上的可证性。它们对 𝗜𝚺₁ 的每个模型 V 成立，V = ℕ 只是特例。
4. 机器证明的范围就是表中各定理的 Lean 陈述。人话复述以 Lean 陈述为准。

## 6. 文件

- 依赖模块 23 个，从 `ProcessObservation` 到 `ZFC/TranslateRE.lean`，逐字节复制自 `../godel-q-zfc-z0-translate/GodelQ/`（2026-10-14 逐个 `cmp` 核对）。
- `GodelQ/ZFC/Z0Full.lean`：逐字节复制自 `dev`（`53f4f82d`）的 `../godel-q-zfc-z0-full/GodelQ/ZFC/Z0Full.lean`，SHA-256 `660f2755…bc75a`。
- 新文件，按编译次序：
  - `GodelQ/ZFC/IntLogic.lean`：内部逻辑小工具；
  - `GodelQ/ZFC/SetNum.lean`、`GodelQ/ZFC/SetNumArith.lean`：C-413；
  - `GodelQ/ZFC/TransTyped.lean`、`GodelQ/ZFC/TransTerm.lean`：C-414，以及 C-413 的反向律；
  - `GodelQ/ZFC/TransBall.lean`：C-415；
  - `GodelQ/ZFC/TransSigma1.lean`：C-416；
  - `GodelQ/ZFC/Z0D3.lean`：C-417；
  - `GodelQ/Negative/BallMergeOffByOne.lean`：负控制。

## 7. 运行

见 `README.md` 的运行表。捕获工具：`.claude/goals/CG-007-formalization-completion/tools/capture_run.py`（驱动 `zfc_lean_check.py` 原样复用）。
