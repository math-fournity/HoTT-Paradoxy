# CG001-C-410–C-412：自由变量不受 ω 限制——“证明逐条翻译”的不变量在 ℕ 中就不成立

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-FREEVAR-001`；负控制 `MP-CG001-GODEL-Q-ZFC-Z0-FREEVAR-NEG-OMEGA-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W8；本机会话 95a1a81b（012-Opus，Opus 5.5），2026-10-14，独立 worktree `/Volumes/D/HoTT-worktrees/012-opus-w8`（分支 `claude/012-opus-w8`）。研究发起人 2026-10-08【原话】“按照你的想法进行优先级安排，完成后续所有“形式化和机器证明”工作。”
>
> **理论变体**：同 `../godel-q-zfc-z0-translate/`：Lean 4（v4.34.0）加 Mathlib（`5ed29652`）与 Foundation（`1fb01b72`），经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。
>
> **身份**：机器证明（范围见 §5）。C-410 是正结果（内部翻译对带自由变量的公式也逐字正确）；C-411、C-412 是反例，否定的是舰队在 W8 上采用的两条中间陈述，不否定 Z0，也不否定舰队的 `ShCraigElim`（它只对句子陈述）。
>
> **编号**：舰队各分支已用到 CG001-C-406（`codex/cg007-w8-d3`）。为免与尚未并入 `dev` 的编号相撞，本包跳过 C-407–C-409，从 C-410 起。

## 0. 位置

- W8 要把 Z0 的影子形式（C-120）读成“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”。dev 上的 `Z0Full.lean` 已把它归结为一条可导性条件 D3（`zfc_z0_full_of_D3_internalize`）。
- 2026-10-11 至 10-14，舰队沿“把 `Sh.craig` 的推导逐条翻译成 𝗭𝗙𝗖 的推导”推进 D3：对推导 d 作归纳，不变量取
  `Q d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`（`codex/9276-cg007-w8-d3` 的 `ShCraigElimPredicate.lean:65`）。十个规则支里七支已证；∀ 支（`AllBlockerQ`）已证；剩下 ∃ 支（`ExsBlockerQ`，归约到 `ExsBridge2`）与公理支（`RootBlockerQ`，即 D3 本身）。
- Foundation 的翻译 `arithTrln.translate` 把量词限制在 ω 上，**不给自由变量加“属于 ω”的前提**：自由变量仍是集合变量。内部翻译 `iT` 也一样（本包 C-410 把这一点机器证实到带自由变量的公式）。于是，一个自由变量若取 ω 以外的集合，原子公式的翻译 `∀y₀y₁((y₀∈ω ∧ y₀=x) ∧ … → …)` 前件不可满足、为真，它的否定为假。推导里的 ∃ 引入可以用自由变量作见证，这一步就把“真”传成了“假”。

## 1. 精确命题

| 编号 | 定理（文件） | 内容 |
|---|---|---|
| CG001-C-410 | `iVE_pquote`、`iT_pquote`（`GodelQ/ZFC/OpenTranslate.lean`） | 在 𝗜𝚺₁ 的每个模型 V 中：对每个项 t（可含自由变量，n 个约束变量），`iVE n ⌜t⌝ = ⌜varEqual t⌝`；对每个算术公式 φ（可含自由变量），`iT n ⌜φ⌝ = ⌜translate φ⌝`。自由变量 `&x` 译为 `“#0 = &x”`，不带 ω 限制。 |
| CG001-C-411 | `exsBridge2_false`（`GodelQ/ZFC/FreeVarCounter.lean`） | 在 V = ℕ 中，`∀ p t, IsUFormula ℒₒᵣ p → IsTerm ℒₒᵣ t → Provable 𝗭𝗙𝗖 (imp ℒₛₑₜ (iT 0 (substs1 ℒₒᵣ t p)) (^∃ (domZero ^⋏ iT 1 p)))` 不成立。这是舰队 round31 `ExsBridge2.lean` 的 `exsBridge2` 逐字的陈述（取 V = ℕ）。反例：p = ⌜#0 < 0⌝，t = `^&0`。 |
| CG001-C-412 | `dCounter_derivation`、`dCounter_not_Q`、`q_invariant_false`、`exsBlockerQ_false`（同上） | (1) ℕ 中的纯逻辑推导 `dCounter`：结论 sequent `{∃x (x<0), ¬(&0<0)}`，由 ∃ 引入（见证 &0）作用在公理 `{&0<0, ∃x (x<0), ¬(&0<0)}` 上；它不用理论公理，所以对每个带 Δ₁ 定义的算术理论 T 都是 T 的推导。(2) 它的结论翻译后，𝗭𝗙𝗖 不可导。(3) 所以存在 `Sh.craig` 的推导 d（在 ℕ 中），`¬ Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`：舰队的不变量 `Q` 对 `Sh.craig` 的推导不成立。(4) 舰队的 `ExsBlockerQ`（`ShCraigElimSetupQ.lean`，把 `Q` 展开逐字写出，取 V = ℕ）不成立：上面的实例满足它的全部前提，结论不成立。 |

`translateSeq` 来自 `GodelQ/ZFC/SeqTranslate.lean`，与 `dev`、`codex/9276-cg007-w8-d3`、舰队 round31 与 master-assembly 各处的副本逐字节相同（SHA-256 `c8d044db…26bd7`）。

## 2. 证明

- **C-410**（`OpenTranslate.lean`）：照搬句子版 `iT_quote`（C-119）的证明，换成 `Semiproposition` 的引号。多出来的部件：
  - 自由变量情形：`iVE` 的构造把 `^&x` 送到 `eqAtom (^&x)`，与 Foundation `varEqual (&x) = “z. z = &x”` 的编码相同；
  - `Rew.emb`（从 `Empty` 到 ℕ）与 `Rew.embSubsts` 的引号：`embSubsts w ▹ σ = (emb σ) ⇜ w`，再用 Foundation 的 `typed_quote_substs`。
- **在 `Universe` 中求值**（`FreeVarCounter.lean` §2）：每个自由变量都赋值为 ω（Foundation 的 𝗭𝗙𝗖 模型 `Universe`，`ω ∉ ω` 由 `mem_irrefl`）。
  - `eval_tLtZ`：`(&0 < 0)ᵗ` 为真。原子翻译的求值化成 “对所有 w，若每个 w i 属于 ω 且满足第 i 个变量等式，则 w₀ ∈ w₁”；第 0 个条件要求 w₀ ∈ ω 且 w₀ = ω，不可满足。
  - `not_eval_tExLtB`：`(∃x, x < 0)ᵗ` 为假。取 w = (x, ∅)，结论化成 x ∈ ∅。
- **可靠性**（§3）：ℕ 中的内部可导性给出真的 LK2 推导（Foundation `Derivation.sound`、`Provable.sound2`）；LK2 推导经 `toProofData` 化成 LK 推导加有限个 𝗭𝗙𝗖 公理，在 `Universe` 中可靠（`LK.Derivation.sound`；公理在 `Universe` 中为真）。所以 sequent 里总有一个公式在任一赋值下为真。
- **C-411**：ExsBridge2 的码在 ℕ 中等于 `⌜(&0<0)ᵗ 🡒 (∃x, x<0)ᵗ⌝`（C-410、`iT_exs`、`substs1` 的引号）。可证就意味着它在赋值 ω 下为真，即“真 → 假”，矛盾。
- **C-412**：`translateSeq (fstIdx dCounter)` 等于 `⌜{(∃x, x<0)ᵗ, ¬(&0<0)ᵗ}⌝`；两者在赋值 ω 下都为假，与可靠性矛盾。`ExsBlockerQ` 的前提 `Q dd` 成立：`dd` 的结论翻译后含互补的一对 `(&0<0)ᵗ` 与 `¬(&0<0)ᵗ`（`Derivable.em`）。

## 3. 负控制

| proof id | 文件 | 改动 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-FREEVAR-NEG-OMEGA-001` | `GodelQ/Negative/WrongCounterInOmega.lean` | 自由变量改赋 ∅（∅ ∈ ω），照搬 `eval_tLtZ` 的证明脚本 | 拒绝：`h0.right` 的类型是 `w 0 = ∅`，而证明需要 `w 0 = ω`。这表明反例确实依赖“自由变量取 ω 以外的值”，不是空洞地成立 |

## 4. 这说明什么，不说明什么

- **说明**：按 `Q` 这个不变量逐条翻译推导，第二层归纳在 ∃ 支上就不可能闭合；ExsBridge2 不是“难证”，而是假的，且在标准模型 ℕ 中就假。原因只有一个：翻译不给自由变量加 ω 前提，而推导的中间 sequent 含自由变量。
- **不说明**：
  1. 不否定舰队的 `ShCraigElim`（`Provable Sh.craig ⌜σ⌝ → Provable 𝗭𝗙𝗖 ⌜σᵗ⌝`，只对句子 σ 陈述）；
  2. 不否定 D3，不涉及 Z0 的真假；
  3. 不说“证明翻译”这条路线本身走不通：把不变量改成带上自由变量的 ω 前提（例如 `Derivable 𝗭𝗙𝗖 (H(d) ∪ translateSeq (fstIdx d))`，`H(d)` 是“第 i 个自由变量 ∉ ω”的否定式），∃ 支的反例就不再适用；这一改法本包没有证明。
- 本会话的主路线不走证明翻译，而走“经翻译的形式化 Σ1 完全性”，见 `../godel-q-zfc-z0-sigma1/PLAN.md`。

## 5. 禁止外推

1. 不推出 ZFC ⊢ ⊥，也不推出 𝗭𝗙𝗖 的任何具体不可证性（C-411、C-412 里的“𝗭𝗙𝗖 不可导”只是靠 `Universe` 这个 Lean 元层模型的可靠性推出的；对 𝗭𝗙𝗖 之外的事实不作断言）。
2. 反例只在 V = ℕ 中给出；它们否定的是“对一切 𝗜𝚺₁ 模型 V 成立”的全称陈述。
3. `Universe` 是 Lean 元层的模型（同 C-103、C-118），它的存在不是 𝗭𝗙𝗖 内部可证的事。
4. C-410 是对每个具体公式 φ 的元层定理（在 𝗜𝚺₁ 的每个模型中），不是 𝗜𝚺₁ 内部对“所有公式编码”的断言。

## 6. 文件

- 23 个依赖模块逐字节复制自 `../godel-q-zfc-z0-translate/GodelQ/`（从 `ProcessObservation` 到 `ZFC/TranslateRE.lean`，复制时核对过）。
- `GodelQ/ZFC/SeqTranslate.lean`：逐字节复制自 `dev` 的 `../godel-q-zfc-z0-full/GodelQ/ZFC/SeqTranslate.lean`。
- 新文件：
  - `GodelQ/ZFC/OpenTranslate.lean`（C-410）；
  - `GodelQ/ZFC/FreeVarCounter.lean`（C-411、C-412）；
  - `GodelQ/Negative/WrongCounterInOmega.lean`（负控制）。

## 7. 运行

见 `README.md` 的运行表。捕获工具：`.claude/goals/CG-007-formalization-completion/tools/capture_run.py`（驱动 `zfc_lean_check.py` 原样复用）。
