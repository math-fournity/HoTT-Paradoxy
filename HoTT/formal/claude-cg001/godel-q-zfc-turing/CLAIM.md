# CG001-C-104、C-105：图灵路线——不对 𝗭𝗙𝗖 做自指的观察力不完备

> **证明包**：`MP-CG001-GODEL-Q-ZFC-TURING-001`；负控制 `MP-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W1；本机会话 d58e0c0d，Opus 5.5，2026-10-08。
>
> **理论变体**：Lean 4（v4.34.0）内核，加 Mathlib（`5ed29652`）与 FormalizedFormalLogic/Foundation（`1fb01b72`）。经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。对象是 Foundation 中的一阶 `𝗭𝗙𝗖`（ℒₛₑₜ 语法、LK 证明系统）。不涉及 HoTT 路径。
>
> **身份**：机器证明，范围见 §3、§6。𝗭𝗙𝗖 的一致性与数字句的 Σ1 可靠性，沿用 `../godel-q-zfc/`（C-95–C-100）的 Lean 元层 `Universe` 模型（要用宇宙），不是 𝗭𝗙𝗖 内部可证的事。

## 0. 这一条在研究里的位置

- 【原话】研究发起人要两个结果（dev-notes 0115，2026-10-05）：“1、无哥德尔的思路。2、有哥德尔的思路。”本包是“无哥德尔”一路的第一个形式交付（`形式化追踪/02-无哥德尔路线/`，候选形态 (a)）。
- 【原话】这条路的出发点是研究发起人的计算视角（KC-000024）：“悖论们都是在揭示理论由于对时间和时序的特殊对待，给自己制造了哥德尔不完备性，也就是在计算理论角度看，是不可停机的问题。”
- 【解释】一句话：𝗭𝗙𝗖 能证明为“永不停”的过程，可以被机器一一列出；真正永不停的过程，没有任何机器能列全。所以 𝗭𝗙𝗖 必有漏网之鱼，而且漏掉的有无穷多个，连“漏掉的那些”也列不全。证明不需要构造任何“说自己”的过程或句子。

## 1. 记号

- 过程、`Done`、`DoneBy`、`NeverObserver`、`EffectiveTheory`：同 `../godel-q/CLAIM.md` §1。
- 漏点：`O.Misses := {e ∣ ¬ Done e ∧ ¬ O.accepts e}`；`T.Misses := {e ∣ ¬ Done e ∧ ¬ T.provesNever e}`。
- 补丁：`O.patch F hF hnever` 接受 `O.accepts e ∨ e ∈ F`。其中 `F` 有限，且其中的过程都确实永不完成。
- 𝗭𝗙𝗖 的漏点：`zfcMisses := {e ∣ ¬ Done e ∧ 𝗭𝗙𝗖 ⊬ neverS ΦH ⌜e⌝}`。`neverS`、`haltsS`、`ΦH`、`ΨN` 同 `../godel-q-zfc/CLAIM.md`。

## 2. 精确命题（类型逐字见 `GodelQ/ZFC/QualificationTuring.lean`）

| 编号 | 定理 | 内容 | 前提 |
|---|---|---|---|
| CG001-C-104 | `qual_C104` | (1) 任一可靠、可枚举的永不完成观察者：漏点集不可枚举，且无穷。(2) 补上任意有限个确实永不完成的点之后，仍不可枚举、仍无穷；补丁只拿走那几个点。(3) 任一有效理论：Q 不完备；漏掉的“永不完成”不可枚举、无穷；每个漏点的每个有限时刻都被确认“尚未完成” | 观察者：可枚举、可靠。理论：C-88 的四条元性质 |
| CG001-C-105 | `qual_C105` | 对 Foundation 的 `𝗭𝗙𝗖`：(1) 漏点恰是“永不停机”句独立于 𝗭𝗙𝗖 的过程，即“停机”句与“永不停机”句都不可证；(2) 漏点不可枚举，且无穷；(3) 𝗭𝗙𝗖 对每个漏点的每个 k 证明“k 步内尚未停机”；(4) 𝗭𝗙𝗖 的 Q 不完备，𝗭𝗙𝗖 不完全；(5) 有限补丁之后，漏点仍不可枚举、仍无穷 | 无额外前提（C-95–C-100 的已证事实） |

## 3. “无哥德尔”的确切范围（机器核对）

`GodelQ/Turing.lean` 与 `GodelQ/ZFC/TuringZFC.lean` 的末尾各有一段 `run_cmd` 依赖检查。它从每个定理出发，在 Lean 环境中对“定义体与类型里出现的常量”做传递闭包；不满足预期就报错，编译即失败。它核对四件事：

1. **不经过本项目的对角点**：C-104、C-105 的各定理不依赖以下声明：
   - `GodelQ.diagonal_fixed_point`、`diagonal_escape`；
   - `no_complete_never_observer`、`complete_observer_not_re`、`tower_step`；
   - `EffectiveTheory.godel_I_process_form`、`not_completeForNever`、`devils_bargain`；
   - C-99、C-100 的对角过程定理 `godel_I_process_form_zfc`、`godel_I_process_form_zfc_full`。
2. **经过停机定理**：不可枚举、无穷与不完全这几条，都依赖 Mathlib 的 `ComputablePred.halting_problem_not_re`。
3. **正控制**：检查器能看见已知的对角依赖：`godel_I_process_form` 与 `godel_I_process_form_zfc_full` 都到达 `diagonal_fixed_point`。
4. **照实记下的底层事实**：Mathlib 的 `halting_problem_not_re` 经 Rice 定理到达 Kleene 递归定理 `Nat.Partrec.Code.fixed_point₂`。

所以“无哥德尔”的确切意思是：**不对被观察的理论（𝗭𝗙𝗖）及其可证性做自指**。计算本身的对角论证（图灵的停机问题）仍在底层。对 𝗭𝗙𝗖 只用了两条性质：

- 它证明的“永不停机”可枚举（C-97，即“证明有限、可机械核对”）；
- 它不说错（C-88/C-99：一致性加 Σ1 完全）。

## 4. 与哥德尔路线（C-89、C-99、C-100）的关系

| | 哥德尔路线 | 图灵路线（本包） |
|---|---|---|
| 漏点 | 指名一个对角过程 d，`Done d ↔ 𝗭𝗙𝗖 ⊢ “d 永不停”` | 不指名；证明漏点存在、无穷、列不全 |
| 用到 𝗭𝗙𝗖 的什么 | 可枚举、可靠，加上把 𝗭𝗙𝗖 的可证性放进对角过程 | 只用可枚举、可靠 |
| 结论的强度 | 一个确定的独立句 | 独立句无穷多，且它们的集合不可枚举；有限补丁补不完 |
| 共同点 | 都是“每一刻看得见，‘永远’看不见”：每个漏点的每个有限时刻，𝗭𝗙𝗖 都证明“尚未停机” | 同左 |

【判断】两条路线在“计算视角”上会合：哥德尔路线的对角过程，是图灵路线所说漏点中的一个具体成员。

## 5. 研究发起人的话与本包承接了什么

- “不是没有时间维度的观察力，只是没有完备的观察力”（KC-000066）：
  - C-105 (3) 是“不是没有”：对每个漏点，𝗭𝗙𝗖 在每个有限时刻都确认它尚未停机；
  - C-105 (1)(2) 是“只是没有完备的”：这样的漏点无穷多，而且列不全。
- “bare ZFC 理论精度不够”（KC-000070）：对象是 Foundation 中真实的 𝗭𝗙𝗖，不是使用模型。
- **没有承接**：
  - 时间的另一面，即稠密与离散（扩展认知 002 的澄清，KC-000003、KC-000048），由 W2 承接；
  - “时间维度 = 过程的逐步运行”是解释桥，不是定理（同 C-84–C-103）。

## 6. 负控制

| proof id | 文件 | 去掉的前提 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-001` | `GodelQ/Negative/WrongTuringWithTruthObserver.lean` | 可枚举：把“真理观察者”（接受集 = 全部永不完成者，可靠但不可枚举）当作可枚举观察者套漏点定理 | 拒绝：`re` 字段无法提供（`simp` 无进展）。真理观察者的漏点集是空集，在同一文件中由 `empty_re` 证明可枚举；所以若能提供 `re`，就会推出矛盾。 |

## 7. 文件

- 下列 16 个文件逐字节复制自 `../godel-q-zfc/GodelQ/`，复制时核对过：
  - `GodelQ/ProcessObservation.lean`、`EffectiveTheory.lean`、`GodelZenoRunner.lean`、`FoundationArith.lean`；
  - `GodelQ/ZFC/` 下的 SetLanguage、SchemaDelta1、ReplacementDelta1、ZFCDelta1、NumeralCode、NeverRE、OmegaArith、NumeralSemantics、ArithInterp、R0Model、Effective、Soundness。
- 新文件：
  - `GodelQ/Turing.lean`：抽象层与依赖检查器；
  - `GodelQ/ZFC/TuringZFC.lean`：𝗭𝗙𝗖 实例与依赖检查；
  - `GodelQ/ZFC/QualificationTuring.lean`：命题对照；
  - `GodelQ/Negative/WrongTuringWithTruthObserver.lean`：负控制。

## 8. 禁止外推

1. 不推出 ZFC ⊢ ⊥，也不推出 bare ZFC 不一致。
2. “无哥德尔”只指不对 𝗭𝗙𝗖 做自指；停机问题本身的证明是对角论证（§3 第 4 条）。不得说成“完全不用对角论证”。
3. 漏点“列不全”指漏点集不是可枚举集；不指任何具体过程的身份不可知。
4. 补丁定理只对“接受 = 𝗭𝗙𝗖 可证 或 属于 F”的观察者成立；它没有处理“𝗭𝗙𝗖 加上有限条新公理之后的演绎闭包”。那个理论若仍一致、可枚举，C-104 (3) 对它同样成立，但本包没有为它单独构造 `EffectiveTheory` 实例。
5. 𝗭𝗙𝗖 一致与 Σ1 可靠来自 Lean 元层的 `Universe` 模型，不是 𝗭𝗙𝗖 内部可证。
6. 停机问题、Rice 定理是经典结果。新的是读法：把“𝗭𝗙𝗖 在时间维度上的观察力不完备”落成“可列与不可列”的比较，并核对它不对 𝗭𝗙𝗖 做自指。没有做过文献查重。
