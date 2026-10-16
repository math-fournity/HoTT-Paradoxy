# CG001-C-111：𝗭𝗙𝗖 的定理集可枚举；Z0 归结为一条纯语法引理

> **证明包**：`MP-CG001-GODEL-Q-ZFC-Z0-RE-001`；负控制 `MP-CG001-GODEL-Q-ZFC-Z0-RE-NEG-COMP-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W4a；本机会话 d58e0c0d，Opus 5.5，2026-10-09。
>
> **理论变体**：同 `../godel-q-zfc-z0-pa/`：Lean 4（v4.34.0）加 Mathlib（`5ed29652`）与 Foundation（`1fb01b72`），经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。
>
> **身份**：机器证明（范围见 §3、§4）。Z0 仍是条件形式；条件从“`Sh.RE`”收窄成“翻译 `arithTrln.translate` 可计算”，这是关于一个具体语法函数的命题，与 𝗭𝗙𝗖 的可证性无关。

## 0. 位置

- C-103 把 Z0 化成两条前提；C-110 证明了其中的 `𝗜𝚺₁ ⪯ Sh`。剩下的 `Sh.RE`，本包把它归结为翻译的可计算性。
- 剩下的缺口是“机械的”：翻译按公式结构递归定义，它可计算，在数学上没有疑问。难在 Lean 里要逐层证明语法操作在编码上原始递归，而 Foundation 目前只证明了编码本身（`PrimrecCoding.lean`）。

## 1. 精确命题（类型逐字见 `GodelQ/ZFC/QualificationShRE.lean`）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-111 | `qual_C111` | (1) `REPred (fun φ : Sentence ℒₛₑₜ ↦ 𝗭𝗙𝗖 ⊢ φ)`：𝗭𝗙𝗖 的定理集可枚举。它推广 C-97，后者只针对“永不停机”句一族。(2) 任一可计算的 τ，只要对每个算术句 σ 都有 `𝗭𝗙𝗖 ⊢ τ σ ↔ 𝗭𝗙𝗖 ⊢ σᵗ`，就给出 `Sh.RE`。(3) 若 `arithTrln.translate` 可计算，则 `𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`。 |

## 2. 证明

- (1)：由 `𝗭𝗙𝗖.Δ₁`（C-95），`b ↦ Provable 𝗭𝗙𝗖 b` 是 Σ1 谓词（Foundation 的 `definability`），于是可枚举（`rePred_iff_sigma1`）。再由 Foundation 的 `provable_iff_provable` 与 `Sentence.quote_eq_encode_nat`，把内部编码接到 Mathlib 的 `encode`，与 `Computable.encode` 复合。
- (2)：可枚举谓词与可计算函数复合仍可枚举（`REPred.comp`）；`σ ∈ Sh` 按定义就是 `𝗭𝗙𝗖 ⊢ σᵗ`。
- (3)：(2) 的特例，接 C-110 的 `zfc_z0_of_RE`。

## 3. 负控制

| proof id | 文件 | 去掉的前提 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-RE-NEG-COMP-001` | `GodelQ/Negative/WrongShREWithoutComputability.lean` | 翻译的可计算性（想用 `simp` 搪塞） | 拒绝：`simp` 无进展。本包没有证明这条引理。 |

## 4. 阻塞引理与最小可续路线

**阻塞引理**：`Computable (fun σ : ArithmeticSentence ↦ arithTrln.translate σ)`。

翻译的定义（Foundation `LK/Interpretation.lean`）：
- 原子公式经 `translateRel`：对每个参数项用 `varEqual` 引入中间变量，套 k 重全称、一个合取与一条蕴涵，并对 `domain`、`rel`、`func` 这几个固定公式做 `Rew.subst`、`Rew.embSubsts`、`Rew.emb` 代换；
- 量词经 `fal`、`exs` 加上定义域限制；
- 联结词直接下传。

要证它可计算，按依赖次序是四个子引理：

1. **代换在编码上原始递归**：对公式编码做值域递归，项编码上的代换嵌在原子情形里，量词下要移位约束变量。可以仿 Foundation 自己证明解码原始递归的做法（`Primrec.nat_omega_rec'` 加 `subArgs` 与 `step`，`PrimrecCoding.lean` 第 440–700 行）。
2. **`varEqual` 在项编码上原始递归**：对项做值域递归，用到 1。
3. **`translateRel` 原始递归**：由 1、2，再加上 k 重全称的迭代（`Nat.rec`）与有限合取。
4. **`translateAux` 原始递归**：对公式编码做值域递归。
   - ⋏、⋎：用 Foundation 的 `primrec₂_and`、`primrec₂_or`；
   - ∀、∃：套上固定的定义域公式编码，这个编码与元数无关；
   - rel、nrel：用 3，nrel 再取否定的编码。

另一条路线是内部路线：用 Foundation Bootstrapping 的 `UformulaRec1` 定义“内部翻译”，证明它 Σ1 可定义，并且等于翻译的编码，就像 S2c 对数字公式 `numCode` 所做的那样。原子情形同样要先做一个对项的内部递归。

两条路线的工作量都估计在上千行。CG-007 先做其他单元，再回到这里（W4b）。

## 5. 文件

- 下列 20 个文件逐字节复制自 `../godel-q-zfc-z0-pa/GodelQ/`：从 `ProcessObservation` 到 `Z0PA` 的依赖链，不含其负控制与命题对照，复制时核对过。
- 新文件：
  - `GodelQ/ZFC/ShRE.lean`；
  - `GodelQ/ZFC/QualificationShRE.lean`；
  - `GodelQ/Negative/WrongShREWithoutComputability.lean`。

## 6. 禁止外推

1. 不推出 Z0 对 𝗭𝗙𝗖 已经成立：阻塞引理（§4）没有证明；另有内部化（Con(𝗭𝗙𝗖) → Con(Sh.craig) 在 𝗜𝚺₁ 中，CG-007 W8）。
2. 不推出 ZFC ⊢ ⊥。
3. “𝗭𝗙𝗖 的定理集可枚举”是经典事实；新的是在 Foundation 中把它对真实的 𝗭𝗙𝗖 形式化，并接到 Z0 上。
