# ZFC-H0 总证明闭环：F1-B CCHM target 的 feature coverage matrix

> **身份：** `RESEARCH_COGNITION_CLOSURE / M1_FULL_H0MAP / F1B / NOT_A_MODEL_THEOREM`。
>
> **问题：** C-365 已把 exact H0 的 `Delay/runFor` 输出投影到 h-set trace。这个 operational fragment 能否扩展成 fixed Cubical Agda H0 到 CCHM/集合论语义的完整 `H0Map`？

## 1. 本项目自己的先验分解

在查阅新来源前，当前构造给出如下判断：

1. `Delay ℕ` 的有限观察天然可以写成 `ℕ → Maybe ℕ`，C-365 已在同一 Cubical Agda 变体内证明这一步；
2. 这不等于 CCHM semantics，因为 H0 的 `question = never` 依赖的不只是 Delay：还依赖 universe、h-level、EM1、suspension、truncation 和 univalence；
3. 因此最可能的阻塞不是 `runFor` 的等式本身，而是 **native coinductive record / guardedness 是否在同一 target model 中有解释，且该解释能与 Cubical Agda library 的 HIT/universe 依赖合成**；
4. 反控制是：若某文献只有 guarded `later` modality 或 clocked calculus，它只能说明一个近邻机制，不能自动解释 H0 的 unguarded `Delay` record。

这四项是本轮查源前的候选，而不是从标题或模型名倒推出的结论。

## 2. 学术界与开源实现的对照

| 来源/代码 | 实际支持 | 对 exact H0Map 的限制 |
|---|---|---|
| CCHM, *Cubical Type Theory: a constructive interpretation of the univalence axiom* | 构造性 cubical-set semantics、univalence；说明某些 HIT（球与 propositional truncation）的语义。 | 文章没有给 Cubical Agda 2.8.0 + cubical 0.9 library 的逐模块 map；其 HIT 举例不能替代 EM1、suspension、truncation 所组成的 exact H0 dependency closure。 |
| Cubical Agda 官方文档/库 | Cubical Agda 是 CCHM variation；`transp`、`hcomp`、univalence、HIT 是本项目 source variant 的实际语法接口。GitHub `agda/cubical` 提供 codata/stream/M-type 开发。 | 实现/库存在不等于对整个实现的 set/cubical-set semantic model。 |
| Vezzosi–Mörtberg–Abel, *Cubical Agda* | 明说 coinductive types 由 projection copattern/path interaction 处理；stream bisimulation 可对应 path equality，库含 stream property/M-type 代码。 | 这是 Cubical Agda 的语言/证明能力，不是 CCHM 对 native coinductive records 的 published full model theorem。 |
| Agda 2.8 coinduction docs | coinductive record、copattern、guardedness 的实际规则；eta 对 coinductive records 被禁以避免 checker loop。 | 规则/实现文档不提供 external semantic `H0Map`。 |
| GCTT / clocked cubical work | guarded recursion 和 coinductive reasoning在 presheaf semantics中有明确路线。 | 它使用 `later`/clock discipline；fixed H0 是 `--guardedness` 下的 native unguarded coinductive record，未给 source-defined translation。 |
| Mörtberg, *Computational Proofs in Cubical Type Theories* slides | 明确区分 CCHM-based Cubical Agda 与 cartesian/equivariant models，并报告把 Cubical Agda proofs transport 到另一 cubical theory 是困难的。 | 这是反对“同属 cubical 就自动翻译”的直接控制，不是不可翻译定理。 |

## 3. CCHM feature coverage

| H0 feature | fixed H0 中的实际身份 | CCHM-family source coverage | 当前判词 |
|---|---|---|---|
| Core cubical syntax | `Path`、`transp`、`hcomp` | CCHM 的直接对象 | `FAMILY_LEVEL_COVERAGE` |
| Univalence / universe | `Type ℓ-zero` 与 h-level inquiry | CCHM 有 univalence/universe 语义路线 | `PARTIAL_VARIANT_COVERAGE`：尚未对 Cubical Agda 2.8.0 library expression 给 map |
| Basic HIT | H0 dependency closure 中的 higher constructions | CCHM 文章例示 circle、spheres、propositional truncation | `PARTIAL_HIT_COVERAGE` |
| `EM1` / Eilenberg–MacLane | C-75 通过 `EM ℤ (1+n)` 支持 universe no-level | 本轮一手来源未发现 exact EM1 interpretation theorem | `UNPAID` |
| suspension / truncation composition | `EM` library closure 的部分 | 单独 HIT 例子存在，组合依赖未被 exact source map | `UNPAID` |
| native coinductive record | `Delay` 的 `force : Delay' A` | Cubical Agda source/doc 有规则；原 CCHM `cubicaltt` grammar 只给 `data` / `hdata` 声明和有限 reserved-keyword 列表，未给 `record` 或 `coinductive` rule。 | `ORIGINAL_CUBICALTT_IMPLEMENTATION_GAP_DIRECT_SOURCE` |
| `never` / finite `runFor` | H0 output observation | C-365 有 native h-set trace | `H0_OPERATIONAL_FRAGMENT_ONLY` |
| `QuestioningDelay` | fixed `question (Type ℓ-zero) judge ≡ never` | 当前未发现 source-defined syntax/model translation | `UNPAID` |

## 4. F1-B 判词与下一行动

```text
CCHM_FAMILY_RELEVANT
H0_OPERATIONAL_FRAGMENT_ONLY
ORIGINAL_CUBICALTT_IMPLEMENTATION_GAP_WITH_SCOPE
FULL_H0MAP_NOT_YET_CONSTRUCTED
```

因此，CCHM 是合理的 first target，却还不能以“理论同族”写成 H0Map。下一动作曾是检查 `mortberg/cubicaltt` 的 exact syntax；该检查现已完成：其 README 的 reserved keywords 和 `Exp.cf` 的 declaration grammar 只包含 `data` / `hdata`，未包含 `record` 或 `coinductive`。故 fixed H0 的 native record 无法直接作为这个 **具体 CCHM implementation** 的源项。

这支付的是一个范围明确的 source/code verdict：

```text
ORIGINAL_CUBICALTT_IMPLEMENTATION_GAP_WITH_SCOPE
```

它不证明“所有 CCHM mathematical semantics 都不能加入 coinduction”。F1 的下一个 target 必须转为有明示 coinductive-record/guarded-recursion规则的 cubical extension，并逐字段检查它能否同时承接 CCHM/HIT/universe；GCTT 是候选，但其 `later`/clock calculus 先被视为不同 variant，不能自动接收 H0。

## 5. 一手入口

- CCHM 原论文：<https://arxiv.org/abs/1611.02108>
- Cubical Agda 论文：<https://staff.math.su.se/anders.mortberg/papers/cubicalagda.pdf>
- Agda coinduction 文档：<https://agda.readthedocs.io/en/v2.8.0/language/coinduction.html>
- Cubical library：<https://github.com/agda/cubical>
- GCTT：<https://arxiv.org/abs/1611.09263>
- Mörtberg slides：<https://staff.math.su.se/anders.mortberg/slides/wg6.pdf>
- `mortberg/cubicaltt` README：<https://github.com/mortberg/cubicaltt>
- `mortberg/cubicaltt` grammar `Exp.cf`：<https://github.com/mortberg/cubicaltt/blob/master/Exp.cf>
