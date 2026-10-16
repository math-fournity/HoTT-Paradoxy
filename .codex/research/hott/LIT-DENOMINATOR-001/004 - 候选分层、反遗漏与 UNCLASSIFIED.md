<!-- governance-shard:v2
logical_id: LIT-DENOMINATOR-001
shard_id: 004
index: ../LIT-DENOMINATOR-001.md
-->

# 候选分层、反遗漏与 UNCLASSIFIED

## 一、保守分层

`triage_lit_denominator_candidates.py` 只看标题信号，不读取摘要，不做最终排除：

| 层 | 数量 | 语义 |
|---|---:|---|
| `DIRECT_TITLE_SIGNAL` | 32 | 标题同时含 HoTT/univalent/cubical 与计算机制，或直接是 synthetic/incompleteness/formalization 主题 |
| `ADJACENT_TITLE_SIGNAL` | 164 | 标题含相关类型论或 HoTT，但需要摘要/正文判断计算关系 |
| `UNCLASSIFIED_TITLE_INSUFFICIENT` | 1,745 | 标题不足；全部保留，不能当作排除或无关 |
| **总计** | **1,941** | remainder=0；每个 discovery candidate 恰有一个 tier |

离线 verifier 已检查 source hash、候选 key 唯一性、tier 集合、计数和 33 个 seed 分母，结果 `VALID`。

## 二、直接信号中的重要新增项

除既有 41 条地图外，当前 direct/adjacent 候选至少提出下列高价值全文任务：

- *Canonicity and Computability in Homotopy Type Theory*（2023）；
- *Canonicity and homotopy canonicity for cubical type theory*（2022）；
- *First Steps in Synthetic Tait Computability: The Objective Metatheory of Cubical Type Theory*（2021）；
- *Syntax and models of Cartesian cubical type theory*（2021）；
- *Type Theory in Type Theory using a Strictified Syntax*（2025）；
- *Decidability of conversion for type theory in type theory*（2017）；
- *On fixed-point theorems in synthetic computability*（2017）；
- *Guarded Cubical Type Theory*（2016/2018）；
- *Oracle Computability and Turing Reducibility in CIC*（2023）；
- *Continuous and algebraic domains in univalent foundations*、*Domain theory in univalent foundations I*（2024）；
- *Can We Formalise Type Theory Intrinsically without Any Compromise?*（2026）；
- *Multi-Clocked Guarded Recursion Beyond ω* 与 *Representing Guardedness…*（2026）。

这些条目尚未因标题信号升级为核心依赖；下一步读取摘要/正文并与 R2、G-HOTT-SYNTAX、TC-06/07/09/11/14 映射。

## 三、已观察到的假阳性

metadata query 返回 MRI synthetic CT、调和单叶函数、泛 Gödel 哲学、用 HoTT 命名的 AI/量子故事等。它们说明 broad query 的 recall 与 precision 需要分开：噪声不会进入核心 seed，但在没有摘要审查前仍保留原始候选。版本化 preprint/DOI 也可能以不同 key 重复，后续需做 work-level 版本聚合，不能把版本数当独立工作数。

## 四、已观察到的假阴性

33 个预注册 seed 有 20 个 exact miss。这证明 query/provider 的负结果不能支持“不存在”或“没有相关工作”。补偿机制为：

1. 核心 seed 强制并集；
2. DOI/title/author 逐项 primary lookup；
3. backward/forward citations；
4. 场馆与官方项目扫描；
5. 独立 holdout；
6. 新论文使旧 denominator stale。

## 五、为什么 UNCLASSIFIED 必须显式保留

标题无法表达论文中一个小但决定性的 theorem、limitation 或 implementation note。1,745 条 remainder 不能逐篇永久常驻上下文，但其机器文件、key 和来源查询必须可按主题/年份/引用再次筛选。后续 abstract triage 可以移动层级；只有一手审查才可给 `OUT_OF_SCOPE_WITH_REASON`。

