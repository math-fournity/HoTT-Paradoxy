<!-- governance-shard:v2
logical_id: LIT-CLASSICS-001
shard_id: 002
index: ../LIT-CLASSICS-001.md
-->

# Turing与Church：可计算、通用机与不可判定

## 一、Turing 1936/37 的精确对象

Turing 的对象不是本项目当前 `halt` 指令语义。原文把机器表写成有限标准描述（standard description），再编码为 description number；§6 构造一台读取任意机器标准描述、模拟其计算序列的 universal machine。这直接支持 R2 的“有限代码 + 通用解释器”结构，但还需要一个机器证明的翻译才能对应当前双计数器语义。

原文的关键区分：

- `circle-free`：不断产生第一类符号（figures），因而计算无限序列；
- `circular`：只产生有限多个 figures；它既包括到达无后继配置，也包括机器继续移动却永远不再产出 figure；
- `satisfactory number`：circle-free machine 的 description number。

因此 `circular` 不是现代“停止”的同义词，`circle-free` 也不是“运行不停止”的简单同义词。一个永远运动但不再输出 figure 的机器在 Turing 术语中是 circular。把原文直接写成“1936 已证明当前 `Halts` 不可判定”会改变观察谓词。

§8 假设存在机器 `D`，对任意标准描述在有限步内裁决 circular/circle-free；将 `D` 与 universal machine 组合成 `H`，再令 `H` 检查自己的 description number，得到两种 verdict 都不可能。随后原文给出更接近 reachability 的独立结果：不存在机器 `R` 能对任意机器判断它是否曾打印给定符号。§11 再把机器“曾打印 0”与功能演算公式 `Un(M)` 的可证性对应，从而否定 Entscheidungsproblem。

### 对 R2 的精确要求

| Turing 部件 | 当前 main 已有 | 尚需机器证明 |
|---|---|---|
| 有限标准描述／description number | `ProgramCode` 只有归纳有限表 | `encode : ProgramCode → ℕ`、`decodeNat : ℕ → ProgramCode` 及所需往返／满射 |
| universal machine | `runFor fuel code state` 统一解释有限表 | 数值 code 输入的 evaluator 与 encode/decode 一致 |
| finite-stage observation | `finalAt`、`haltsWithin` | 公平枚举所有 `(code,input,fuel)` 与 starvation-free 证明 |
| no `D` / no `R` | 尚无 | 自应用编译或从已证模型的 certified reduction |
| Entscheidungsproblem reduction | 尚无 exact HoTT calculus | 后置到 R4；不能从对象机一步跳到 HoTT proof checking |

Turing 原文还包含 1937 correction；它修复 §11 的形式公式，并区分“存在计算某实数的机器”与“由给定生成规则统一算出那台机器的 description number”。这个差异与本项目的 ASK 很接近：存在性结论并不自动提供统一构造器。

## 二、Church 1936 的精确对象

Church 先给 λ-公式、conversion、reduction、normal form 与 Gödel representation，再把“有效可计算”定义为 general recursive（等价地 λ-definable）。Theorems XVI/XVII 给出 recursive 与 λ-definable 的两向对应。原文还明确要求一个可用的符号逻辑系统具备：推理规则是有效操作、规则与公理可有效枚举、数字与表达式表示关系可有效判定。

这为 Gödel/R4 提供四个不同义务：

1. 语法对象有限、可编码；
2. 有效判断 well-formed/code relation；
3. 公理与推理规则可枚举；
4. 证明候选可有限检查。

Theorem XVIII 的对象是“λ-公式是否有 normal form”，不是“任意机器是否进入 halt”。有 normal form 的公式可枚举；若无 normal form 的公式也可枚举，就可并行搜索两边并形成总判定，和 XVIII 冲突。这个论证正是后续 `proof/refutation semi-search` 与公平调度的经典原型。

Theorem XIX 由 XVIII 与 conversion/normal-form 等价推出：不存在总递归函数判定任意两公式是否 convertible。原文最后再在足够表达、ω-consistent 的符号系统上把 conversion 判定归约到 provability Entscheidungsproblem。

### 对本项目的限制

- Church 的 Gödel representation 给“编码可算、合法码可判、合法码可解”范型；它不证明我们新定义的 `ProgramCode` 编码已经满足这些性质。
- normalisation 不可判定、可证性不可判定和对象机 halting 是相关但不同的 TaskSpec；需要显式 reduction。
- Church 1936 采用的 consistency 条件和后来的 Rosser 改进不同；不能把 Rosser 强度倒写回原文。
- 这两个经典结果是一般计算／逻辑边界，在没有 HoTT-essential ablation 之前只支持通用机制线。
