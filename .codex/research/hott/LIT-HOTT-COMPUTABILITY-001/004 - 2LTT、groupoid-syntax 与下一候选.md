<!-- governance-shard:v2
logical_id: LIT-HOTT-COMPUTABILITY-001
shard_id: 004
index: ../LIT-HOTT-COMPUTABILITY-001.md
-->

# 2LTT、groupoid-syntax 与下一候选

## 2017 2LTT 不是可直接冻结的 exact raw syntax

2LTT 明分 outer 与 inner：outer 有 UIP 的传统 MLTT，inner 是可含 univalent universes/HIT 的 HoTT，共享 contexts，并有 inner→outer conversion。可是论文在 §2 开头明确说其 suggested syntax 不是 complete specification；作者以 two CwF sharing contexts 的模型语义为精确定义，term model/initiality 的完整证明超出范围。§2.6 的 conservativity也在 initial-model/semantic 视角下陈述，且只反射 inhabitation。

因此 `G-HOTT-SYNTAX-001` 不能把 §2.1 的规则清单直接当作 raw syntax、checker、enumerator 与 proof-code 已完备。Strengthenings T1–T3、A1–A6 又会改变 conversion、Nat、fibrancy、equality reflection 和 conservativity；每个 R4 theorem 必须写出使用哪个版本。

## 首个 exact machine-replayed slice

`MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001` 已把 CSL 2026 `cohtt` 固定成真实机器切片：

- syntax：`Con/Sub/Ty/Tm`、substitution、context extension、`U/El`、Π/β/η、二阶 substitution coherence；
- truncation：`Sub`/`Tm` 为 set，`Ty` 先为 groupoid；
- theorem：α-normalisation 给 `isSetTy`；
- comparison：`isoCon/isoSub/isoTy/isoTm` 对应 set syntax；
- replay：20 个 TT 模块两阶段 fresh check，项目 probe exact replay。

它仍缺 Nat、一般 identity/Path object former、对象层 univalence/HIT、raw derivation/checker、proof enumeration 与 arithmetic representation，所以 R4 仍为 `OPEN`。C-244–C-249 已另行重放一般 R3 essential incompleteness/Robinson Q，但不能填补这些 target-calculus 缺口。R3→R4 十二义务矩阵把当前状态固定为 2 scoped present / 3 absent-by-definition / 7 open。下一扩张不能一句“加入这些构造”，而要逐项证明 syntax、checking/effectivity、编码/substitution 与模型保真仍成立。

## 第二 target 候选：可执行 cubical calculus

2026-09-15 的 exact source 资格化入口包括 `cubicaltt@9baa6f24`、`redtt@ae766588`、`cooltt@b39bf299` 与 `cctt@3695c69e`。cubicaltt/cooltt/cctt 的源码直接出现 Nat、Path/universe、conversion 或 HIT；但实验实现同时可能允许 `undefined`、holes、未解 metavariables或无 termination check 的一般递归。故 `R4-HOTT-NAT-EFFECTIVITY-001` 先定义闭合证明输入规范，递归检查整个 import closure，并把这些 incomplete forms 列为证明关系域外；build/test 成功本身不能证明它们构成一致有效的 proof relation。

## 新的高判别力候选：internal fibrant replacement

2LTT §2.7 报道一个比一般 Gödel 口号更接近本项目目标的具体 no-go：若把 outer type 的 fibrant replacement `R A` 以内在、context-stable 的形成／引入／消去／计算规则加入 2LTT，则 inner level 满足 UIP。论文同时说明，homotopical models 中外部 fibrant replacement 可以存在，但通常不在 base change 下稳定，因而不能按该内部规则自然化。

这形成候选 `CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001`：

```text
模型/现实侧：每个对象可在外部选择 fibrant replacement
理论经济提升：把逐对象外部过程压成可替换、对 context 自然的内部 type former
机器目标：internal R rules → inner UIP；inner univalence + Bool/loop control → contradiction or homotopy collapse
```

它可能属于方向 A：现实／模型层逐例可做的过程，被理论 uniform internalisation 加上额外自然性／相干义务，最终破坏原本的高阶结构。它也有方向 B 读法：把外部可得 replacement 提升成内部普遍可用操作。当前只到 `SOURCE_REPORTED_COUNTEREXAMPLE_CANDIDATE`；Theorem 2.20 尚未在本项目机器重放，现实同任务桥梁与“HoTT 必要性”仍须消融。

下一 bounded successor 应先形式化该 theorem 的最小规则包并给 univalence/Bool 正负 controls。若去掉 context-stable eliminator 或把 replacement 保持在 crisp/outer 层后 UIP 不再推出，就能精确定位抽象变化；若只得到“人为加入不相容公理”，则降级，不冒充最终悖论。
