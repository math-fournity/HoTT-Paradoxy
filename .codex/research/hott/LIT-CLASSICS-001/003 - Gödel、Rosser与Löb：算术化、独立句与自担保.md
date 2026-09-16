<!-- governance-shard:v2
logical_id: LIT-CLASSICS-001
shard_id: 003
index: ../LIT-CLASSICS-001.md
-->

# Gödel、Rosser与Löb：算术化、独立句与自担保

## 一、Gödel 1931 的前提链

Gödel 在 §1 把公式视为有限符号串、证明视为有限公式序列，再把符号和有限序列一一编码为自然数。由此，`Formula`、`proof figure`、`provable formula` 等元数学关系成为自然数关系；决定性下一步不是“有了数字”，而是证明所需递归关系能在对象系统中定义／表示。

原文当前与项目最相关的结果：

| 原文 | 精确前提／对象 | source-reported 结果 | 项目义务 |
|---|---|---|---|
| Satz VI | 递归公式类 + ω-consistency；系统能定义递归关系 | 构造既不可证也不可证否定的句子 | R4 必须冻结 exact calculus、axiom enumeration 与 representability |
| Satz VII/VIII | 每个递归关系是算术的，并能在系统内形式化 | 获得不可判定算术句 | 不能用元层 Python/Agda 函数冒充对象层表示 |
| Satz IX/X | 把递归全称问题归约到 restricted functional calculus satisfiability | 该演算存在不可判定问题 | 需要保真 reduction，不是关键词类比 |
| Satz XI | 递归且一致的公式类；对象化一致性句 | 该系统不能证明自己的该一致性句 | 原文此处是 proof sketch；需要 HBL/现代形式化对照 |

Satz VI 的原始两支使用不同强度：由普通 consistency 排除 Gödel 句可证；排除其否定可证使用 ω-consistency。原文自己明确讨论“只假设 consistency”时能得到的较弱结论。Rosser 的贡献不能被省略为措辞调整。

Satz XI 也不能读成“任何理论都不能知道自己任何事实”。它要求一个可编码、递归、足够表达算术的形式系统，且对象化的 `Con(T)` 与外部一致性假设必须分层。一个 kernel 在外层检查某证明，不等于对象理论内部证明自己的 global soundness。

## 二、Rosser 1936：原文的枚举、证明比较与 consistency 强化

Rosser primary body 现已进入本地语料：PDF 第 1 页是 JSTOR 封面，第 2–6 页完整对应 *The Journal of Symbolic Logic* 1(3) 的印刷页 87–91；题名、作者、卷期、页码、收稿信息、正文开头与 `HARVARD UNIVERSITY` 末尾均已视觉核对。原始下载 PDF 与 MinerU 正规化 PDF 的 bytes/SHA-256 分开固定。以下是原文报道的定理内容；当前项目尚未在 proof assistant 中重放，证据等级为 `SOURCE_REPORTED_NOT_REPLAYED`。

原文 Introduction 先固定四项语义：

- `simply consistent`：不存在公式 `A` 使 `A` 与 `~A` 均可证；
- `ω-consistent`：沿 Gödel 的定义；
- general recursive／primitive recursive：沿 Kleene 的定义；
- Entscheidungsverfahren：以公式 Gödel number 为输入、对可证与不可证分别输出 0/1 的 general recursive function，并显式采用 Church 对 general recursiveness 与 effective calculability 的识别。

§1 的 Lemma I 与 Corollary I 先把“由 general recursive function 可枚举、允许重复”的类转换为 primitive-recursive enumeration。随后定义一组推理规则何谓 general recursive，并以 Lemma II 说明：从递归可枚举公理类和 general-recursive 推理规则取得的最小证明闭包仍递归可枚举。这不是附带技巧；它把后续不完备结论的适用条件从“原始公理／规则 primitive recursive”扩展到“可证公式递归可枚举”的工作层。

§2 的结果分层如下：

| 原文结果 | 精确前提 | source-reported 结论 | 当前项目映射 |
|---|---|---|---|
| Theorem I.A | `Pκ` 的可证公式递归可枚举；`Pκ` ω-consistent | 存在 primitive-recursive class formula，其闭句与否定均不可证 | R4 需 proof enumeration 与对象层表示 |
| Theorem I.B | 同一可枚举条件；`Pκ` simply consistent | 表达 `Pκ` simple consistency 的形式命题在 `Pκ` 中不可证 | 对象化一致性与外部一致性必须分层 |
| Theorem II | 可证公式递归可枚举；`Pκ` simply consistent | 存在 primitive-recursive class formula，其闭句与否定均不可证 | consistency-only 不完备；需 Rosser proof comparison |
| Theorem III | `Pκ` simply consistent | 不存在一般适用的有效过程来判定任意无自由变量公式是否可证 | 使用 Church identification；不是无条件算法结论 |
| Theorem IV | `Pκ` simply consistent | 可证公式 code 类与不可证公式 code 类不可能同时递归可枚举 | 与 semi-decision／双枚举边界直接相关 |
| Theorem V | `P` simply consistent | 不可证／不可判定公式类非 r.e.；可证／可判定公式类 r.e. 但非 general recursive | 给 R2/R3 的正负枚举判据提供原始分层 |

Theorem II 的关键定义在原文中是：令 `x Bκ y` 表示枚举第 `x` 项得到公式 code `y`，再令 `x Prκ y` 要求 `x Bκ y`，并且没有 `z ≤ x` 使 `z Bκ Neg(y)`。因此 `Provκ(y)` 不是裸“存在一份 `y` 的证明”，而是存在一份在其界内没有较早／不晚的否定证明与之竞争的证明。Rosser 在元层 simple-consistency 假设下说明 `Bewκ` 与 `Provκ` 等价，同时明确指出该等价不能在对象系统内形式证明，因为它本身需要 simple consistency，而 Theorem I.B 已说明相应一致性命题不可由系统自身证明。这个层级差异正是当前 R4 必须保留的内容，不能把元层等价直接写进对象层接口。

Peter Smith 的 §7 与 Peters 2022 学士论文 §§5.2–5.3 现在退回其合适角色：它们分别提供可读重构和机器化推广对照。Smith 的有限步交错叙述解释了枚举直觉；Rosser 原文自身通过 Kleene normal form 给出 Lemma I 的 primitive-recursive enumeration。Peters 将 proof comparison 推广为 disjoint predicates 的 strong separation。三者相互支持，但只有当前 Rosser 扫描承担 1936 原文身份。

对 R2/R4 的直接义务现可写得更精确：公平／有效枚举、proof-code 与 negation-code transformer、有界比较、对象层 representability、simple consistency 的元层位置，以及从“一边可半判定”到“两边同时可枚举／总判定”的禁止跃迁。MinerU 对公式下标、上划线和排版符号仍有 OCR 误差；精确形式以扫描页或后续原生形式化为准。

## 三、Löb 1955：self-guarantee 不是免费接口

Löb 讨论 Henkin 句：一个句子的内容是“具有该句 Gödel 号的公式可证”。原文不是凭自然语言循环直接推出结论，而是在指定系统 `Zμ` 以及更一般的形式系统中要求：

- 一阶谓词演算推理闭包；
- 证明关系的数论谓词；
- 从可递归替换函数得到的 Gödel code 操作可定义；
- 原文列出的 I–V 五个可证性条件。

在这些条件下，核心定理是：若系统证明“`Prov(S) → S`”，则系统证明 `S`。Henkin 的 `S ↔ Prov(S)` 因而是定理。原文末尾给自然语言 Curry 型推演作为类比，但那不是把自然语言悖论当作形式系统已满足 I–V 的证据。

### 对“理论自馈回环”的启发

真正有力的候选不是让 proof checker 调用自己，而是找到自然 consumer 对一族命题提供如下承诺：

```text
∀ φ,  Prov_T(⌜φ⌝) → φ
```

若 `Prov_T`、quote/substitution、fixed point 和 HBL 条件在同一层可用，Löb 将把这一全域 self-guarantee 压缩成极强反射结果。当前仓库没有发现任何 HoTT 社区接口作此承诺；因此它是 `NATURAL-CONSUMER-SELF-GUARANTEE` 的搜索规格，不是已发现的 BUG。

## 四、inner/outer 的不可省略性

Gödel/Löb 的证明总有一个描述对象理论的元层。若将元层结论重新放入对象层，必须证明编码、表示、反射和层级提升的合法性。后续 2LTT 资料显示某些 HoTT 元理论陈述本来就不能在 inner HoTT 中表达；所以“HoTT 在神经网络／代码里，因此可直接令其证明自己的不完备性”缺少一个精确层级合同。
