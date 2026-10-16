# CG001-C-119、C-120：翻译可计算；Z0 的影子形式不再带前提

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-001`；负控制 `MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-RE-001`、`MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-DOMAIN-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W4b；本机会话 d58e0c0d，Opus 5.5，2026-10-09。研究发起人 2026-10-08【原话】“按照你的想法进行优先级安排，完成后续所有“形式化和机器证明”工作。”
>
> **理论变体**：同 `../godel-q-zfc-z0-re/`：Lean 4（v4.34.0）加 Mathlib（`5ed29652`）与 Foundation（`1fb01b72`），经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。
>
> **身份**：机器证明（范围见 §4、§7）。C-111 留下的阻塞引理（翻译可计算）已证；C-103 的两条前提都成了定理，Z0 的影子形式 `𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ` 不再带前提。把它读成“𝗭𝗙𝗖 证明不了自己的一致性”，还差内部化（§4，CG-007 W8）。

## 0. 位置

- C-103 把 Z0 化成条件形式，前提是 `Sh.RE` 与 `𝗜𝚺₁ ⪯ Sh`。C-110 证明了后者；C-111 把前者归结为“翻译 `arithTrln.translate` 可计算”。本包证明这条引理。
- C-111 的 §4 列了两条路线：在 Mathlib 里逐层证明语法操作原始递归；或者在 𝗜𝚺₁ 内部重写翻译。本包走的是第二条：用 Foundation Bootstrapping 的内部递归，把翻译写成 𝗜𝚺₁ 中的 Σ1 函数，并证明它在 𝗜𝚺₁ 的每个模型里都恰好算出翻译的编码。到了标准模型 ℕ，这就是一个 Σ1 可定义、等于 `σ ↦ ⌜σᵗ⌝` 的函数；Foundation 的 `computable_iff_sigma1` 再把它变成 Mathlib 意义下的可计算函数。

## 1. 精确命题（类型逐字见 `GodelQ/ZFC/QualificationTranslate.lean`）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-119 | `qual_C119` | (1) 在 𝗜𝚺₁ 的每个模型 V 中：内部变量等式 `iVE` 与内部翻译 `iT` 是 𝚺₁ 可定义的函数（`iVEDef`、`iTDef`）；对每个闭项 t（n 个约束变量），`iVE n ⌜t⌝ = ⌜varEqual t⌝`；对每个算术公式 φ（n 个约束变量），`iT n ⌜φ⌝ = ⌜translate φ⌝`。(2) 在 ℕ 中，`iT 0 (encode σ) = encode σᵗ`。(3) `Computable (fun σ : ArithmeticSentence ↦ arithTrln.translate σ)`。 |
| CG001-C-120 | `qual_C120` | (1) `{σ ∣ 𝗭𝗙𝗖 ⊢ σᵗ}` 可枚举。(2) `Sh.RE`，并且 `𝗜𝚺₁ ⪯ Sh`（C-110）：C-103 的两条前提都是定理。(3) `𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`，不带前提。(4) `Sh ⊬ Sh.craig.consistent`。 |

## 2. 证明

内部翻译分三层，每层都是 𝚺₁ 可定义的函数，正确性都在任意 𝗜𝚺₁ 模型 V 中沿结构归纳证明（`GodelQ/ZFC/InternalTranslate.lean`）。

- **项**（`Language.TermRec`）：`iVE n t` 对应 `varEqual t`，即“#0 等于项 t 的值”（n 个约束变量）。
  - 约束变量 `#z` 给出原子 `#0 = #(z+1)`。
  - 0 元函数（零、一）给出 `⊤ 🡒 F_f[#0]`。
  - 2 元函数（加、乘）给出 `∀∀((A₀ ⋏ (A₁ ⋏ ⊤)) 🡒 F_f[#2, #0, #1])`。其中 `A_i` 是“#i 在 ω 中”与“第 i 个参数的结果换名”（`#0 ↦ #i`，`#(j+1) ↦ #(j+3)`）的合取。
  - 换名向量 `shiftVec b n = [#b, …, #(b+n−1)]` 本身由内部原始递归定义；对标准的 n，它等于逐项写出的向量（`shiftVec_nat`）。
  - 正确性 `iVE_quote`：按闭项归纳，情形为约束变量、零、一、加、乘。
- **原子公式**：`iTR n 2 R v` 对应 `translateRel R v`，即 `∀∀((A₀ ⋏ (A₁ ⋏ ⊤)) 🡒 R′(#0, #1))`。ℒₒᵣ 只有两个二元关系，等号与小于。正确性见 `iTR_quote`。
- **公式**（`UformulaRec1`，参数是约束变量的个数，进量词时加一）：`iT n p` 对应 `translate`。
  - 联结词直接下传；
  - 否定原子取 `neg`；
  - `^∀ p` 译为 `^∀ (domain/[#0] 🡒 ·)`，`^∃ p` 译为 `^∃ (domain/[#0] ⋏ ·)`，即量词限制到 ω。
  - 正确性 `iT_quote`：按公式归纳，情形为 rel、nrel、⊤、⊥、⋏、⋎、∀、∃。
- **固定公式**：定义域公式、函数与关系的定义公式以编码常数进入（`cDomN`、`cFuncN`、`cRelN`、`cEqN`）。它们与真实公式编码的对应，逐个由符号编码的 `rfl` 核对（`cFunc_quote0`、`cFunc_quote2`、`cRel_quote`），不是假设。
- **到 ℕ 与可计算性**（`GodelQ/ZFC/TranslateRE.lean`）：
  - `iT_encode`：由 `iT_quote` 与 `Sentence.quote_eq_encode_nat` 得到；
  - `translate_computable`：`iT` 是 𝚺₁ 函数，所以可计算（`computable_iff_sigma1`），再用 `Computable.encode_iff` 从编码搬到句子；
  - `translate_provable_re`：不经可计算性，直接由“`b ↦ Provable 𝗭𝗙𝗖 (iT 0 b)` 是 Σ1 谓词”得到；
  - `Sh_RE`：经 C-111 的 `Sh_RE_of_translate_computable`；
  - `zfc_z0`、`sh_z0`：C-110 的 `zfc_z0_of_RE`、`sh_z0_of_RE`。

## 3. 负控制

| proof id | 文件 | 去掉的东西 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-RE-001` | `GodelQ/Negative/WrongZ0WithoutRE.lean` | 内部翻译（不导入它，于是没有 `Sh.RE` 实例），只留 C-110 的 `𝗜𝚺₁ ⪯ Sh` | 拒绝：找不到实例 `Theory.RE Sh` |
| `MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-DOMAIN-001` | `GodelQ/Negative/WrongTranslateNoDomain.lean` | 量词的 ω 限制（把量词步写成 `^∀ ⌜φ⌝`） | 拒绝：改写后剩下 `^∀ imp ℒₛₑₜ domZero ⌜φ⌝ = ^∀ ⌜φ⌝`，未解 |

## 4. 还差什么：内部化（W8）

- `Sh.craig.consistent` 说的是“𝗭𝗙𝗖 的算术影子（经 Craig 公理化）不矛盾”。在 Lean 元层，`Sh` 矛盾当且仅当 𝗭𝗙𝗖 矛盾。
- 要把 C-120 读成“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”，需要在 𝗜𝚺₁ 内部证明 `Con(𝗭𝗙𝗖) → Con(Sh.craig)`。有了它，由 C-110，𝗭𝗙𝗖 也证明它的翻译，于是 `𝗭𝗙𝗖 ⊢ Con(𝗭𝗙𝗖)ᵗ` 就推出 `𝗭𝗙𝗖 ⊢ (Sh.craig.consistent)ᵗ`，与 C-120 矛盾。
- 这一步的内容是：从 Sh.craig 的公理出发、推出 ⊥ 的一个算术证明，在 𝗜𝚺₁ 内部变成 𝗭𝗙𝗖 推出 ⊥ 的证明。它需要内部的证明翻译，即 Foundation 的 `of_provability` 的内部版本：
  - 逐条翻译 LK 推导；
  - 补上定义域非空、函数全定义的引理；
  - 接上每条公理 σ 的 𝗭𝗙𝗖 证明（σ ∈ Sh 在内部就是“存在 `iT 0 σ` 的 𝗭𝗙𝗖 证明”，它是 Σ1 的，本包已给出）。
- 本包的 `iT` 是这条内部化的第一块：公式的翻译已经在 𝗜𝚺₁ 内部。剩下的是证明的翻译。

## 5. 文件

- 下列 21 个文件逐字节复制自 `../godel-q-zfc-z0-re/GodelQ/`：从 `ProcessObservation` 到 `ZFC/ShRE.lean` 的依赖链，不含其负控制与命题对照，复制时核对过。
- 新文件：
  - `GodelQ/ZFC/InternalTranslate.lean`（内部翻译与正确性）；
  - `GodelQ/ZFC/TranslateRE.lean`（翻译可计算；`Sh.RE`；不带前提的 Z0 影子形式）；
  - `GodelQ/ZFC/QualificationTranslate.lean`（命题对照）；
  - 两个负控制。

## 6. 运行

见 `README.md` 的运行表与 CG-001 证据索引 §34。捕获工具：`.claude/goals/CG-007-formalization-completion/tools/capture_run.py`（驱动 `zfc_lean_check.py` 原样复用）。

## 7. 禁止外推

1. 不推出“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”的 𝗭𝗙𝗖 内部形式：那需要 §4 的内部化。C-120 说的是 𝗭𝗙𝗖 证明不了它的算术影子（经 Craig 公理化）一致性句的翻译。
2. 不推出 ZFC ⊢ ⊥。
3. `Sh` 的一致性来自 Lean 元层的 `Universe` 模型（C-103），不是 𝗭𝗙𝗖 内部可证。
4. `iT_quote` 是对每个具体算术公式 φ 成立的元层定理（在 𝗜𝚺₁ 的每个模型中），不是 𝗜𝚺₁ 内部对“所有公式编码”的一句断言。
5. 翻译可计算、ZFC 的算术影子可枚举，都是数理逻辑的经典事实。新的是：对 Foundation 中真实的翻译 `arithTrln.translate` 把它形式化，并由此得到不带前提的 Z0 影子形式。
