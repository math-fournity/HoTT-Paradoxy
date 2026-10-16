# 同伦补丁理论撞上的墙：原生重建

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 6fd0312a。起因：回应外部审计（GPT-5.6 Terra）“找一个真实使用者”的要求。
> proof id：`MP-CG001-PATCH-WALL-001`（主包）、`MP-CG001-PATCH-WALL-NEG-001`（负控制）；claims：`CG001-C-28`、`CG001-C-29`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理；零警告。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §7（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`；来源与解读见 `.claude/思考与发现/CN-021 - 同伦补丁理论：把状态改变写成路径的真实使用者.md`。

## 这个包为什么存在

Angiuli、Morehouse、Licata、Harper 的 *Homotopical Patch Theory*（ICFP 2014；JFP 扩展版）是把“改变仓库状态的编辑”写成 HIT 路径的已发表应用。其“更丰富上下文”一节报告了两处困难（本处为转述）：
- 上下文按行数分类、加一行是一条路径时，最自然的解释，即把上下文解释为该长度文件的类型，行不通；
- 若每个上下文都能从空仓库到达，所有上下文都只能被解释为可缩类型。

本包在本项目的工具链中原生重建这两点的数学核心，把“真实使用者撞上 A1 的墙”从来源报告升为有范围的机器证明。它对应 A1 的 C-19（沿路径变化的读数不能尊重路径）与 C-14、C-26（状态都被认同）。

数学内容是 transport 与路径的标准推论，**不主张原创**；它不是对原论文的复现，只重建其中两条陈述的核心。

## 命题全文

记号：`File zero = Unit`，`File (suc n) = Bool × File n`（两字母表上的 n 行文件）；HIT `R` 由 `doc : ℕ → R` 与 `add : (n : ℕ) → doc n ≡ doc (suc n)` 生成。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-28**（最自然的解释行不通） | `isProp (File 0)`；`¬ (Path (File 1) (true , tt) (false , tt))`；不存在 `F : R → Type` 同时满足 `F (doc 0) ≡ File 0` 与 `F (doc 1) ≡ File 1`。负控制：直接定义 `F (doc n) = File n`、`F (add n i) = File n`，内核拒绝（边界处 `Bool × File n` 与 `File n` 不等）。 | `File`、`R`、`isPropFile0`、`oneLineFilesDiffer`、`noLengthInterpretation`；负控制 `WrongLengthInterpretation.agda` |
| **CG001-C-29**（可达即被迫可缩） | 对任意 `F : R → Type`：若 `isContr (F (doc 0))`，则对任意 `n`，`isContr (F (doc n))`。 | `allContextsContractible` |

## 禁止外推

- 本包不说补丁理论失败：原论文改用“由补丁历史索引上下文”，得到了可行的形式化。本包重建的是被他们放弃的那种写法为何行不通。
- `File n` 用两字母表代替原文的字符串文件；C-28 只在 0 行与 1 行之间给出不等价，已足以挡住最自然的解释。原文关于任意 n 的说法本包未重建。
- 不说任何版本控制系统的事实；“上下文”“文件”“行”是解释标签。
