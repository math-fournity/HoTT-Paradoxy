# CG001-C-432…C-435：罗素「解决」考古的形式化面——对角层、分离层、正则层与无界概括负控制

> **证明包**：`MP-CG001-RUSSELL-ARCHAEOLOGY-001`（`GodelQ/Russell/Qualification.lean`）；负控制
> `MP-CG001-RUSSELL-ARCHAEOLOGY-NEG-001`（`GodelQ/Negative/WrongSepContradiction.lean`）。
>
> **目标包**：罗素解决考古工作包（研究发起人 2026-10-16 批准；唯一交接真值
> `docs/罗素解决考古/01-交接文档-20261016.md`）。本机会话 CodeArts（glm-5.3），2026-10-16。
>
> **理论变体**：Lean 4（v4.34.0）内核，加 Mathlib 与 FormalizedFormalLogic/Foundation。
> 经典逻辑。四条核心定理与合取定理经公理审计（`#print axioms`）**不依赖任何公理**
> （清单为空）；`𝗭` 只在实例化节作为前提提供者出现，不进入核心命题。
>
> **身份**：机器证明，但**不是**「ZFC 解决了罗素悖论」的证明，也不是其否定。本包把
> 该社区叙事拆成四条可机器检查的分层命题，作为步骤 4 三栏对照表的形式化底座。考古
> 问题（该「解决」当初的形式化证明是什么）由步骤 2 文献考古承担；工作假说
> （QUESTION 状态）：不存在这样的证明——Zermelo 1908 做的是公理删除/准入层拒绝，
> 「解决」是未经支付的非形式诠释跳跃。

## 0. 这一条在研究里的位置

- 交接文档 01 §3.1 的四命题设计：把「ZFC 解决了罗素悖论」拆成**部件解剖**——
  对角层（任何一致于一阶逻辑的理论都有的东西）、分离层（Zermelo 1908 实际做的
  事：`R_A ∉ A`，非矛盾）、正则层（1930 年代的第二道准入门）、无界概括（被删除
  的爆炸燃料）。
- 四条命题两两对照给出考古结论的机器面：
  - C-432 vs C-435：对角论证本身无公理（不是 ZFC 的功劳）；爆炸的充分条件是
    无界概括（被删除的东西）。
  - C-433 vs 负控制：分离版结论 `R_A ∉ A` **不是矛盾**——照搬无界版对角结尾
    被 Lean 在类型层面拒绝（`R ∉ R` 给不出 `R ∈ A ∧ R ∉ R`）。
  - C-434：`∀ x, x ∉ x` 是**准入禁止**（连自含集合都禁止存在），又一个
    「宣布 vs 手段」的实例。

## 1. 记号

- `SetStructure V`：`Membership V V` 的 abbrev（Foundation 库 `Basic/Misc.lean`），
  一个裸的二元成员关系，无任何集合论公理。
- `sep x P`：Foundation 库的分离公理造集（`Z/Z.lean`），`mem_sep_iff` 给出成员刻画
  `z ∈ sep x P ↔ z ∈ x ∧ P z`。
- `𝗭`：Foundation 库的 Zermelo 集合论（Schindler 教科书口径 `𝗕𝗦𝗧 ∪ 𝗦𝗘𝗣`，
  **含正则公理**，与 Zermelo 1908 历史系统不同）。
- `{z ∈ x ; P z}`：`internalSetBuilder` notation，elaborate 成 `sep x (fun z ↦ P z)`。

## 2. 精确命题（类型逐字见 `GodelQ/Russell/` 各文件）

| 编号 | 定理 | 内容 |
|---|---|---|
| CG001-C-432 | `noRussellSet` | `¬ ∃ R : V, ∀ x : V, x ∈ R ↔ x ∉ x`——纯逻辑，环境只有 `SetStructure V` |
| CG001-C-433 | `sep_russell_not_mem`（核心）+ `sep_russell_not_mem'`（𝗭 实例化） | 分离式成员刻画 `∀ z, z ∈ R ↔ (z ∈ A ∧ z ∉ z)` ⇒ `R ∉ A`（非矛盾）；𝗭 中 `{x ∈ A ; x ∉ x} ∉ A` |
| CG001-C-434 | `foundation_irrefl`（核心）+ `foundation_irrefl'`（𝗭 实例化） | 正则公理（显式形式）+ 单元素集存在 ⇒ `∀ x : V, x ∉ x` |
| CG001-C-435 | `unboundedComprehensionFalse` | 无界概括（命题形态 hypothesis：`∀ P : V → Prop, ∃ S, ∀ z, z ∈ S ↔ P z`）⇒ `False` |
| （合取） | `qual_russell_arch` | 上述四核的合取，公理审计全空 |

公理报告：四条核心定理与合取定理**不依赖任何公理**（含 `propext`、`Classical.choice`、
`Quot.sound` 都不用）。`𝗭` 实例化（`sep_russell_not_mem'`、`foundation_irrefl'`）依赖
𝗭 的公理内容，属前提提供者，不参与核心命题的公理审计。

## 3. 证明思路

- **C-432**：`rintro ⟨R, hR⟩`，`x := R` 代入得 `R ∈ R ↔ R ∉ R`；`R ∉ R` 由
  `R ∈ R → (R ∈ R ∧ R ∉ R)` 的右支给出，再 `h.mpr` 回得 `R ∈ R`，自我爆炸。
- **C-433**：同上代入，但 `h.mpr` 现在需要 `R ∈ A ∧ R ∉ R`——`R ∈ A` 是前提给定的
  （hypothesis），于是**只会得到** `R ∉ R`，与 `hRA : R ∈ A` 组合后反证 `R ∉ A`。
  结论是定理（`R ∉ A`），不是 `False`。
- **C-434**：对单元素集 `{x}` 用正则公理，∈-极小元 `y ∈ {x}` 只能 `y = x`，而
  极小性给 `x ∉ y = x`。教科书路径（库内同内容：`Z/Z.lean` 的 `mem_irrefl`）。
- **C-435**：取 `P := fun x ↦ x ∉ x`，无界概括造出 `R`，其成员刻画正是 C-432
  否定掉的无界罗素集，对角接力爆炸。

## 4. 与已有命题和文献的关系

- **C-120**（Sh.craig.consistent 影子形式 `𝗭𝗙𝗜 ⊬ (Sh.craig.consistent)ᵗ`）：同属
  「宣布 vs 手段」主题，无直接形式依赖。
- **文献**（凭记忆，**未核对出处**，落盘时点为待核，由步骤 2 落实）：
  - Zermelo 1908《Untersuchungen über die Grundlagen der Mengenlehre. I》引入
    分离公理（Aussonderung）；是否使用「解决」（lösen）一词**必须核原文**。
  - 正则公理时间线：von Neumann 1925 / Zermelo 1930（待核）。
  - 「ZFC solved Russell's paradox」叙事的传播史（SEP、教科书）：待步骤 2 检索。

## 5. 负控制

| proof id | 文件 | 被否定的说法 | 预期 |
|---|---|---|---|
| `MP-CG001-RUSSELL-ARCHAEOLOGY-NEG-001` | `GodelQ/Negative/WrongSepContradiction.lean` | 分离层的成员刻画同样自我爆炸（「Zermelo 的『解决』= 在新系统内证明出矛盾」的误读）：照搬 C-432 `noRussellSet` 的对角结尾 `exact hne (h.mpr hne)` | 拒绝：`h.mpr hne` 类型不符，`hne : R ∉ R` 但期望 `R ∈ A ∧ R ∉ R`——对角论证在分离层被基底条件挡住，准入层拒绝不是矛盾；正面定理 C-433 |

## 6. 文件

- `GodelQ/Russell/Basic.lean`：C-432（对角层）。
- `GodelQ/Russell/Sep.lean`：C-433 核心 + 𝗭 实例化（分离层）。
- `GodelQ/Russell/Foundation.lean`：C-434 核心 + 𝗭 实例化（正则层）。
- `GodelQ/Russell/Unbounded.lean`：C-435（无界概括负控制核）。
- `GodelQ/Russell/Qualification.lean`：四核合取 `qual_russell_arch` + 公理审计
  `run_cmd`（五条定理逐条 `collectAxioms`，依赖 `Classical.choice` 即编译失败）。
- `GodelQ/Negative/WrongSepContradiction.lean`：负控制（不进正控编译清单）。
- `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`：从
  `HoTT/formal/claude-cg001/zfc-con-pa-boundary/` 复制的固定工具链与导入闭包哈希。

## 7. 禁止外推

1. **本包没有证明「ZFC 解决了罗素悖论」，也没有证明其否定。**考古结论由步骤 4
   对照表交付，且需要步骤 2 的文献证据；形式化面只是底座。
2. 四条命题是**教科书级标准数学内容**，机器化是为了分层对照，**不主张数学内容原创**。
3. R2/R3 的历史归因（1908 分离、1930 年代正则）是文献层主张，落盘时点未核，
   不得当作已证事实引用；Zermelo 1908 原文措辞（ausschließen / lösen）待核。
4. Foundation 库的 `𝗭` 含正则公理（Schindler 口径），**不是** Zermelo 1908 的历史
   公理系统；实例化节只作前提提供者，不冒充历史系统的形式化。
5. 不推出 `ZFC ⊬ ⊥` 或 ZFC 一致性的任何主张；C-435 的 `False` 只说明「纯成员
   结构 + 无界概括前提」的环境不存在，ZFC 本就不含无界概括公理。
6. 「解决 = 未经支付的诠释跳跃」是 QUESTION 状态的工作假说，不是本包的定理。