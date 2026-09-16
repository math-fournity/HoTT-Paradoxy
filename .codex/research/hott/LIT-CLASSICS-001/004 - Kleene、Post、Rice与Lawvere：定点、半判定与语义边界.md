<!-- governance-shard:v2
logical_id: LIT-CLASSICS-001
shard_id: 004
index: ../LIT-CLASSICS-001.md
-->

# Kleene、Post、Rice与Lawvere：定点、半判定与语义边界

## 一、Kleene 1938 的程序索引自指

Kleene 先区分 total general recursive 与可能未定义的 partial recursive function，并用有效编号 `Φ_e` 表示所有部分递归函数。印刷页 153 给出参数定理的形式：存在 primitive recursive `S`，把一个多参程序的 code 与固定参数变成剩余参数程序的 code。该 7 页扫描现已有 MinerU 全文；三个转换目录在 Markdown、正规化 PDF、页结构和引用图片上逐字节同一，规范导入只保留其中一份派生副本，外部目录全部原样保留。

同页最后给出第二递归定理的原始短形式：对任意部分递归 `ψ(z,x)`，存在编号 `f`，使 `f` 所编号的函数在 `x` 上与 `ψ(f,x)` 相同。其构造把 `ψ` 与参数化函数组合，再令 `f = S(e,e)`。这里的 self-reference 来自三项可计算结构：

1. 程序的有效编号；
2. s-m-n 型代码专门化；
3. universal evaluation／acceptable numbering 的一致性。

它不是源代码文本直接包含自身的无限展开，也不是 proof checker 必须不停止。对当前 R2，这说明只给 `encode/decode` 还不够；还要给代码变换器及其语义保持证明。MinerU OCR 在符号上下标处并不完全可靠，所以参数定理与最后的定点句仍以已视觉核对的印刷页 153 为裁决依据；Markdown 主要提供全文检索入口。

## 二、Post 1944：枚举、归约、oracle 时序与完成点

Post 原文现已从 *Bulletin of the American Mathematical Society* 50(5) 的整期扫描中抽取：source zero-based pages 1–33 对应印刷页 284–316，下一页已经进入另一篇文章。33 页项目 PDF、全文文本、逐页 hash 与 page map 已由 `import_post_1944_primary.py` 固定；抽取页 1、12、28、33 已视觉核对。以下均为原文报道、尚未在本项目 proof assistant 中重放的结果。

Introduction 与 §1 把 r.e. set 视为一元递归函数的值域，并用只增不减的生成过程解释；集合 recursive 当且仅当它与补集都 r.e.，反向算法公平交错两个正枚举。因此单边 positive semi-decision 不能冒充 total decision，两边都能正枚举才产生总答案。

§§2–4 构造 complete set `K`、Gödel miniature 与 creative sets，并区分 one-one/many-one reducibility；§§5–10 构造 simple 与 hyper-simple sets，证明 bounded truth-table、unrestricted truth-table 和一般 reduction 口径会改变 degree 结论。机器统观据此必须固定 reduction 的查询能力、自适应性、观察和完成标准，不能用“都不可判定”代替保真归约。

§11 对本研究尤其关键。Post 把单生成过程描述为一步接一步的单一 time sequence；Turing reduction 的后续 oracle query 可依赖之前的答案，因而具有真实时序依赖。更进一步，他区分三件事：由某个 basis 生成的 r.e. set 事实上有限；存在一个最后元素已经出现的 stage；一般不存在从任意 basis 有效认出“此刻已经全部出现”的方法。对象的有限性、完成时刻的存在与当前可认证的 completion certificate 不能互换。

这条原文与 `C-141` 的 `isFinSet` 形状接口防御同向：mere finiteness／截断有限呈现不自动交付 chosen enumeration 或完成阶段。它只提供一手问题来源；只有找到自然 HoTT consumer 把前者提升为后者时，才可能形成目标候选。Post 的原始 Turing-degree 中间问题在文中仍保持开放，不能把 simple/hyper-simple 构造误写成已解决；Friedberg–Muchnik 与 2024 CIC 机器化是后续 forward chain。

## 三、Rice 1953 的精确量词

Rice 从 Kleene 的部分递归函数有效编号 `Φ(n,x)` 出发，用“该函数枚举出的 r.e. set”定义 extensional class。若两个 index 枚举同一 set，class membership 必须同时包含或同时排除它们；这是真正的语义不变性前提。

Theorem 8 的原始范围是：按其 weak definition，没有非平凡的 r.e.-set class 是 completely recursive。它不是字面上的“所有非平凡程序性质都不可判定”；常见现代 Rice theorem 需要把程序语义、acceptable numbering 与非平凡 extensional property 对齐。

对机器统观的约束是：

- 若目标属性依赖运行时间、语法、proof trace 或表示，它不是纯 extensional semantic property，不能直接套 Rice；
- 若候选类确实只依赖部分函数／r.e. set 的外延语义，任何声称“自动完整决定所有非平凡候选”的系统必须面对 Rice 型边界；
- 有限 grammar 的完整枚举不受此定理否定；从有限 denominator 扩大到所有程序时才触发。

这解释了为什么 machine-overview 可以对 L1 文法完整，但不能因此成为 `COMP-6` 全局悖论发现器。

## 四、Lawvere 1969 的统一对角骨架

Lawvere Theorem 1.1：在 cartesian closed category 中，若存在弱点满射 `A → Y^A`，则 `Y` 的每个 endomorphism 有固定点。反向使用时，若 `Y` 有一个无固定点自映射（如二值否定），就排除这种弱点满的 universal evaluator／naming map。

Theorem 3.2/3.3 把该骨架用于 truth/provability，但额外要求：

- Lindenbaum 类别及 consistency 给出 `false ≠ true`／无固定点 negation；
- substitution 在理论中可定义；
- 公式／句子与 code 的关系足以承担 naming；
- provability 在所选关系下可表示；
- 由 completeness 把“非 true”压成 false。

因此 Lawvere 并没有删除 Gödel 编码／表示义务，而是把它们重写成 point-surjectivity、substitution 和 representability。其附录还指出，第一不完备性的部分论证可弱化具体编号关系；第二不完备性可能仍需要公式与编号的具体关系。

### HoTT 移植义务

HoTT/∞-groupoid 中的“point”、等式、函数空间与 surjectivity 可能带截断或高阶结构。只有机器证明以下之一，才能称 HoTT 特定：

1. 一个原生 HoTT 弱点满／截断点满假设确实足以推出相应 path-fixed point；
2. 截断使命名能力弱化，经典 Lawvere 步骤失败，并由自然 consumer 错把弱能力当强能力；
3. modality／univalence 改变 point-surjectivity 的适用域，并产生同任务失配。

一般 CCC 定点骨架本身可在普通类型论中实现，不能单独通过 HoTT-essentiality gate。
