# T4 审计：第五层 consumer——真实系统的“自证/已验证交付”声明

> 文档身份：`CURRENT AUDIT EVIDENCE / BOUNDED_DEFENSE_WITH_TRUST_BASE`
> 日期：2026-09-12
> 触发：S057 路由的第一工作包 T4（按 C9 §4 四条件审计真实系统的"自证/已验证交付"声明）
> 审计集合：5 个固定来源（全部抓取留证，SHA-256 与字节数在 §5）；来源为公开文档/网站与一篇论文摘要，抓取日期 2026-09-12（本地时间）。
> 结论：**在固定集合内没有找到满足 C9 §4 四条件的 P8 候选**。真实系统不但不越级，而且**显式记录各自的围栏**：信任内核、验证相对规范、传输值可能不计算、内部化需要 QIIT 且只形式化大部分构造。最强声明（Rocq/MetaRocq 的 verified reference checker"正确且完备 w.r.t. 规范"）自带三层限定，不构成"把数学分类/存在当有效交付"的同任务越级。判词 **`BOUNDED_DEFENSE_WITH_TRUST_BASE`**。

## 0. 审计集合与四条件

判据沿用 C9 §4（`W51_GENERIC_BOUNDARY_WITH_OPEN_NATURAL_LIFT` 的第三层验收条件）：

1. **真实性**：固定版本、可回查的接口/工程/论文承诺；
2. **资格越级**：把 M 层数学分类或存在（LEM 或等价经典承诺）当作 E 层有效交付（同输入、同输出、同任务）；
3. **无新增假设**：不引入神谕、额外选择、用户实现映射、unsafe/外部运行或削弱后的输出规格；
4. **可核查性**：失败链或防御链可在本 repo 工具链中机器核查，或以固定来源 + 实际运行原始输出留证。

| ID | 来源 | 版本/日期 | 抓取字节 | SHA-256 | 可核层级 |
|---|---|---|---:|---|---|
| `T4-S1` | Agda 2.8.0 文档·Safe Agda | v2.8.0 | 19,744 | `66b490f389b844f8c66f6decfef96d3a61b3f5d282dbf71e7c509c29764f6b88` | 文档全文 |
| `T4-S2` | Agda 2.8.0 文档·Cubical（What works, and what doesn't） | v2.8.0 | 192,251 | `9b6ed6875e1fdbefe4443e2c859d7dc90c9f343cfa2705688863feca9445d0c4` | 文档全文 |
| `T4-S3` | MetaRocq 项目网站 | 2026-09-12 抓取 | 23,897 | `b0fdad21a17714383f44d369adb1ef6944a2bd8e718503486e3bed8a704ce425` | 站点正文 |
| `T4-S4` | Rocq Prover 官方网站 | 2026-09-12 抓取 | 243,688 | `48ca6d72425b47baaed77847e58ed5c0aef8f34cd3468489ee1a5eb99eaf1f72` | 站点正文 |
| `T4-S5` | Altenkirch–Kaposi, *Normalisation by Evaluation for Type Theory, in Type Theory*（LMCS 13(4), 2017；arXiv:1612.02462v4） | v4（2017-10-20） | 42,351 | `be1c5aa12826fecdb29d74400d7e69ea7c1a18b5de4fa78f6ea5bef0dfa75611` | 摘要页全文 |

## 1. 逐源评估

### T4-S1 Agda 安全模式：声称的是"屏蔽已知不健全特性"，不是自证

文档原文（关键行）：

```text
--type-in-type and --omega-in-omega and pragma NO_UNIVERSE_CHECK ;
allow the user to encode the Girard-Hurken paradox.
pragma INJECTIVE ; allows to prove false by declaring a non-injective function as injective.
--no-termination-check and pragmas TERMINATING and NON_TERMINATING ; give loopy programs any type.
```

评估：`--safe` 的公开含义是**保守地禁用一组已知不健全特性**（并要求库作者兼容）；它不声称类型检查器本身被验证，也不声称完备性。四条件：真实性 ✓；资格越级 ✗（没有把分类当交付的声明）；无新增假设不适用；可核查性 ✓（本 repo 可实测 `--safe` 行为）。判词：`DEFENSE_BY_RESTRICTION`。

### T4-S2 Cubical Agda 文档：官方记录"传输值可能不计算"

文档原文（"What works, and what doesn't"节）：

```text
This section lists some of the common cases where pattern matching unification
produces something that can not be extended to cover transports, and the cases
in which it can. The following pair of definitions relies on injectivity for
data constructors (specifically of the constructor suc), and so will not
compute on transported values.
```

评估：C10 的 `A-11`（抽象 transport 的 stuck）在官方文档中作为**已知限制**被明确记录，而不是被包装成能力。四条件：真实性 ✓；资格越级 ✗；可核查性 ✓（本 repo 的 N10 探针给出同方向的工具链级围栏）。判词：`DOCUMENTED_FENCE`。

### T4-S3 MetaRocq：把 Rocq 形式化在 Rocq 中，并提供"认证插件"

站点原文：

```text
MetaRocq is a project formalizing Rocq in Rocq and providing tools for
manipulating Rocq terms and developing certified plugins (i.e. translations,
compilers or tactics) in Rocq.
```

评估：这是"理论关于自身"的真实工程（与用户 `KC-000035`/`KC-000036` 的主题最接近），但其声明是**构建认证插件/检查器**，没有声称"本理论内含总停机、健全、完备且内部自证的真值裁决器"。四条件：真实性 ✓；资格越级 ✗（声明的产物是插件与其正确性证明，不是"分类即交付"）；无新增假设 —— 见 S4 的信任基；可核查性 ✓（项目有文档与代码仓库）。判词：`CERTIFIED_TOOLING_NOT_SELF_CERTIFICATION`。

### T4-S4 Rocq 官方：内核 + MetaRocq verified reference checker（最强声明）

站点原文：

```text
Its well-studied core type theory ... is implemented in a well-delimited kernel
using the performant and safe OCaml programming language, providing the highest
possible guarantees on mechanised artifacts. The core type theory is itself
formalised in Rocq in the MetaRocq project, a verified reference checker is
proven correct and complete with respect to this specification.
```

评估：这是本集合中最接近"自证"的**真实声明**，但它自带三层限定：

1. **信任基**：生产内核是 OCaml 实现（未被形式验证的部分是信任基）；被验证的是 *reference* checker；
2. **相对性**："correct and complete **with respect to this specification**" 指 checker 接受/拒绝与**规范**一致，而不是"理论完备/全真可判定"；
3. **范围**：验证覆盖核心类型论的规范片段，而非整个证明环境。

四条件：真实性 ✓；资格越级 ✗（这是对 checker 正确性的声明，不是把数学分类当有效交付；且完备性是相对规范而非相对全真）；无新增假设 —— 信任基是显式的（满足"无新增假设"的诚实记录：信任基被点名）；可核查性 ✓（论文/项目公开）。判词：`DEFENSE_WORKS_WITH_EXPLICIT_TRUST_BASE`。

### T4-S5 NBE-in-TT：内部化的真实前置（QIIT + 部分形式化）

摘要原文（关键行）：

```text
Our construction is formulated in the metalanguage of type theory using
quotient inductive types. ... We prove normalisation, completeness, stability
and decidability of definitional equality. Most of the constructions were
formalized in Agda.
```

评估：这是"类型论在类型论中"的**真实机器化成果**，同时恰好给出 C8 `P6` 的经验证据：

1. 元语言需要 **QIIT**（表示/分层前置，正是 C8 的 `SAME_LAYER_INTERNALIZATION` 议题的实证）；
2. 形式化覆盖是 **"most of the constructions"**（非全部）；
3. 结论是 normalization/decidability（元定理），不是"理论内含自证真理裁决器"。

四条件：真实性 ✓；资格越级 ✗；无新增假设 —— 其元语言假设（QIIT、presheaf 解释）被显式写出；可核查性 ✓（论文 + Agda 形式化声明；本 repo 未重跑其代码）。判词：`REPRESENTATION_PREREQUISITE_DOCUMENTED`。

## 2. 四条件总表

| 来源 | 真实性 | 资格越级 | 无新增假设 | 可核查性 | 判词 |
|---|---|---|---|---|---|
| `T4-S1` Agda safe | ✓ | ✗ | — | ✓ | `DEFENSE_BY_RESTRICTION` |
| `T4-S2` Cubical 文档 | ✓ | ✗ | — | ✓ | `DOCUMENTED_FENCE` |
| `T4-S3` MetaRocq | ✓ | ✗ | 信任基显式 | ✓ | `CERTIFIED_TOOLING_NOT_SELF_CERTIFICATION` |
| `T4-S4` Rocq 官方 | ✓ | ✗ | 信任基显式 | ✓ | `DEFENSE_WORKS_WITH_EXPLICIT_TRUST_BASE` |
| `T4-S5` NBE-in-TT | ✓ | ✗ | QIIT/presheaf 显式 | ✓ | `REPRESENTATION_PREREQUISITE_DOCUMENTED` |

## 3. 结论与解释

1. **无 P8 候选**：五个来源没有任何一个把"数学分类/存在"当作"有效总交付"，也没有声称"总停机 + 健全 + 完备 + 内部自证"的完整包；恰恰相反，每个来源都**显式记录自己的围栏**（禁用特性清单、传输不计算、信任内核、验证相对规范、QIIT 元语言与部分形式化）。
2. 与 ERCF-3（C8）：最接近的真实系统（Rocq/MetaRocq）执行的正是 C8 所要求的**资格分离**（checker 验证 vs 内核信任基 vs 规范），而不是越过它。`P8` 因而仍为空。
3. 与 W51（C9）：`T4-S3/S4` 显示"理论关于自身"的工程化路径是**分层 + 认证工具**，而不是同层总自证——与 C9 的 W51-2（通用边界）一致。
4. 与 C10（A 方向）：`T4-S2` 官方文档化了 C10 `A-11` 的 stuck 现象；这再次说明该现象是**已知限制**而非隐藏悖论。
5. 五层审计塔至此完整：核心库/论文（N1）、提取接口（N2）、派生开发（N5）、编译后端（N10）、自证声明（T4）。在固定版本集合内，五层均为防御或有界负结论；`REPRESENTATION_BOUNDARY`（第二级）保持，`NATURAL_USAGE_MISMATCH` 仍无候选。

## 4. 重开条件

1. 出现真实系统/论文**明确要求**"总停机 + 健全 + 完备 + 内部自证"（而非其受限版本），且可用于同一任务；
2. 上述任一来源的新版本改变了围栏（例如生产内核被形式验证、编译支持 cubical、完备性声明改为对全真）；
3. 出现把 `χ`/`Rep` 或等价分类-交付对象用于实际交付的接口（E6）；
4. 用户给出新的元数学原文改变方向。

## 5. 证据与哈希

抓取原件保存在 `.codex/research/hott/sessions/S-RES-20260912-058-T4-SELF-VERIFICATION-CONSUMER/evidence/fetched/`：`agda-safe-mode.html`、`agda-cubical.html`、`metarocq-site.html`、`rocq-site.html`、`qiit-abs.html`（哈希见 §0 表）；`metacoq-site.html` 为 297 字节的重定向页（已记录重定向目标 `https://metarocq.github.io`），`metacoq-search.xml`/`proofchecker-search.xml` 记录 arXiv API 限流（`Rate exceeded.`），不作为证据。

审计限制：本轮只做**文档/摘要级**核对（未重跑 MetaRocq 的验证、未审计 Rocq 内核代码本身）；结论只覆盖上述五个固定来源与其抓取版本。
