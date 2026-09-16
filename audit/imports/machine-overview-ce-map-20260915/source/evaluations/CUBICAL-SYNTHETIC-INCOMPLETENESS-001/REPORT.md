# Cubical synthetic incompleteness：从递归不可分离到具体独立句

> Evaluation：`CUBICAL-SYNTHETIC-INCOMPLETENESS-001`  
> Proof ID：`PF-CUBICAL-SYNTHETIC-INCOMPLETENESS-001`  
> Claims：`MP-CSI-PARTIAL-BOOL-001`、`MP-CSI-SEPARATOR-DIVERGENCE-001`、`MP-CSI-EFFECTIVE-SYSTEM-001`、`MP-CSI-INDEPENDENT-SENTENCE-001`、`MP-CSI-ESSENTIAL-INCOMPLETENESS-001`  
> 当前阶段：`CONDITIONAL_SYNTHETIC_ESSENTIAL_INCOMPLETENESS_CORE_MACHINE_PROVED; SMALL_CALCULUS_EFFECTIVE_CLASSIFIER_INSTANTIATED`  
> 现实相对结论：`NOT_ESTABLISHED`  
> HoTT 自身实例：`NOT_INSTANTIATED`

## 1. 为什么这一步比“再造一个自循环”更重要

Gödel 分支需要说明：一个形式系统为何会产生一个既不可证也不可证否的**具体句子**，以及这种不可完成怎样由系统的有效证明过程与代码化自应用共同产生。仅观察一个证明搜索过程超时，或者仅写出一个递归调用，都没有给出这条因果链。

Kirst–Peters 2023 的 synthetic computational route 提供了一个紧凑分解：

```text
universal partial functions
  → two self-return predicates that no total computation can separate
  → a formal system strongly representing those predicates
  → its proof/refutation classifier fails to return on a constructed sentence
  → that sentence and its negation are both unprovable
```

本包在 Cubical Agda 中把这条抽象核心写成无 `postulate` 的条件性定理。所有强前提均通过函数参数进入，不被文件悄悄假定为已有事实。

## 2. 一手来源与固定身份

| 来源 | 固定身份 | 本轮用途 |
|---|---|---|
| Kirst & Peters, *Gödel’s Theorem Without Tears*, CSL 2023 | DOI `10.4230/LIPIcs.CSL.2023.30`；PDF 18 页 / 749,481 B / SHA-256 `422aa3f3…31bf`；提取文本 SHA-256 `5475d25d…e2de` | Definitions 7/17/18、Fact 19、Theorem 20；抽象 formal system、recursive inseparability、essential incompleteness |
| accompanying Coq development | `https://github.com/uds-psl/coq-synthetic-incompleteness`；commit `cd7d8490f8542bfe85658c465bcb26b2ed163f53`；807 tracked paths | 直接读取 `utils.v`、`epf.v`、`formal_systems.v`、`abstract_incompleteness.v`；核对 partial-function、EPF、classifier 和 extension 的实际实现 |
| Kirst & Hermes, ITP 2021 | DOI `10.4230/LIPIcs.ITP.2021.23`；PDF 20 页 / 801,450 B / SHA-256 `b5738da6…d8a` | 对照 first-order axiom systems、many-one reductions、standard-model/soundness 条件 |
| O’Connor, TPHOLs 2005 | DOI `10.1007/11541868_16`；paper PDF 17 页 / 188,561 B / SHA-256 `d5acae99…9610` | 对照传统 formula/proof coding、primitive-recursive substitution/checker、fixed point 与 Rosser 构造 |
| Swan & Uemura, *On Church’s Thesis in Cubical Assemblies* | arXiv `1905.03014`；PDF 23 页 / 291,460 B / SHA-256 `417e713e…fff0` | 约束 HoTT 解释：Church thesis 不成立于完整 cubical assemblies model，但作者在其反射子宇宙中建立与 univalent type theory 的相容模型 |

PDF 与文本原件位于 `/Volumes/D/HoTT-machine-overview-cache/literature/`；提取 manifest 为 `PDF-MANIFEST.json`，pypdf 版本 `6.10.0`。PDF 首页已渲染核对标题与作者。它们是文献证据，不是当前形式证明的依赖闭包。

## 3. 部分计算的精确表示

`PartBool` 不把“运行成功”写成任意关系。它保存一个有限阶段观察函数：

```agda
core : ℕ → OptionBool
```

以及确定性条件：若阶段 `k₁` 与 `k₂` 分别返回 `b₁`、`b₂`，则 `b₁ ≡ b₂`。因此：

```agda
p ⇓ b = Σ[ k ∈ ℕ ] core p k ≡ some b
Diverges p = (b : Bool) → ¬ (p ⇓ b)
```

这里的“不完成”是全称的数学命题：不存在任何有限阶段返回 `false`，也不存在任何有限阶段返回 `true`。它不是某次有限观察窗没有看到输出。

## 4. 对角点怎样被构造出来

`Universal θ` 明确要求：每个 step-indexed partial Boolean function family `f : ℕ → PartBool` 都有一个代码 `c`，使 `θ c` 与 `f` 对所有输入和输出值具有双向相同的收敛行为。

给定一个声称能分离 `θ x x ⇓ true` 与 `θ x x ⇓ false` 的部分分类器 `f`，构造其输出翻转 `flipPart ∘ f`。由 `Universal θ` 取得该翻转族的代码 `c`，再把 `c` 输入自身：

```text
若 f(c) = false，则 θ(c,c) = true，分离条件又迫使 f(c) = true；
若 f(c) = true，则 θ(c,c) = false，分离条件又迫使 f(c) = false。
```

两种返回值都与 `PartBool.deterministic` 冲突。因此 `separator-diverges` 返回：

```agda
Σ[ c ∈ ℕ ] ((b : Bool) → ¬ (f c ⇓ b))
```

这正是用户怀疑的“分类过程在自我应用后于某个问题上不能落定”的一个精确数学形状。当前结论依赖 `Universal θ`，也尚未证明这个 `f` 是 HoTT 自己的自然真理验证过程。

## 5. 从分类不完成到独立句

`FormalSystem S neg` 不把“可证明性”直接声明为一个静态 predicate。它要求一个实际的部分 classifier：

- 返回 `true` 当且仅当 `s` 可导；
- 返回 `false` 当且仅当 `neg s` 可导；
- classifier 本身满足确定性。

若 `r : ℕ → S` 把 self-return-true 输入映到可证句，把 self-return-false 输入映到可证否句，那么把 `classifier (r x)` 代入 `separator-diverges`，得到一个具体 `c`。classifier 在 `r c` 上两个方向均不完成；利用双向对应立即得到：

```agda
Independent fs (r c)
= (¬ Derives fs (r c)) × (¬ Derives fs (neg (r c)))
```

这一步不是“分类器不返回，所以随便称为独立”。它分别通过 proof→true-run 与 refutation→false-run 的已声明定理反推：任一方向若有 derivation，都将与已证明的无有限返回阶段矛盾。

## 6. Essential incompleteness

`Extends base extension` 要求 base 中每个 derivation 都传入 extension。于是 base 的 strong separation 同样传入 extension。对 extension 自己的 classifier 应用同一对角定理，就为每个满足该接口的 extension 产生一个独立句。

因此 `synthetic-essential-incompleteness` 的“essential”不是修辞；它由以下精确量词支持：

```agda
(base extension : FormalSystem S neg)
→ Extends base extension
→ StronglySeparates base Ktrue Kfalse r
→ Σ[ c ∈ ℕ ] Independent extension (r c)
```

它仍只覆盖同一 `S` 与同一 `neg` 上、保持 base derivations 的扩张。

## 7. 机器证明门禁

| 项目 | 结果 |
|---|---|
| Source | `HoTT/formal/cubical-synthetic-incompleteness/SyntheticIncompleteness.agda` |
| Claim spec | `HoTT/formal/cubical-synthetic-incompleteness/CLAIM.md` |
| Agda / Cubical | 2.8.0-3d04bac / v0.9 |
| Canonical run | `HoTT/verification/runs/20260914-CUBICAL-SYNTHETIC-INCOMPLETENESS-001/` |
| Native result | exit 0 / stderr 0 / `KERNEL_ACCEPTED_WITH_SCOPE` |
| Matrix | package row + 5 claim rows；6 rows frozen |
| Independent rerun | `PASS_WITH_SCOPE`；exact index snapshot；exact exit/stdout/stderr match |
| Source declarations | no `postulate`、no `TERMINATING`、no `NON_TERMINATING` |
| Git | `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

## 8. 它与 HoTT 的真实关系

这一定理在 Cubical Agda 的原生 Path 理论环境中通过，但证明没有使用 univalence、HIT、truncation 或高阶路径。因此“Cubical Agda 接受它”证明的是该构造可以在这一环境里表达和核验，不证明其原因来自 HoTT 的高阶结构。

Swan–Uemura 给出一项重要的模型论约束。按其论文，Church thesis 不成立于完整 cubical assemblies model；另一方面，作者构造一个反射子宇宙，使 Church thesis 在其中成立且与 univalent type theory 相容。由此可以合理推断：synthetic incompleteness 与 univalence 并不先验冲突，但 `Universal θ` 的成立依赖所选宇宙/模态环境，不能无条件加到任意 HoTT 实现上。本报告只把这点作为文献支持的模型论路线，不声称已经把本文 `Universal` 与该反射子宇宙形式地对应起来。

2LTT 提供另一条相反方向的提示：若对象理论的元语法、严格相等和全局编码不能在 inner HoTT 中直接表达，可以在 outer theory 中内化其元理论。这样做能完成形式研究，却也明确显示验证责任发生了层级迁移。层级迁移本身是支付装置，不是已发现的 HoTT 错误。

## 9. 对“非现实性悖论”的贡献与不足

本包首次把当前研究中的三个元素连成一个机器证明的过程：

1. 有效系统试图同时捕获证明与证否；
2. 自我代码化把分类器的行为重新送入它自己的输入；
3. 由 universality 构造出的输入使分类过程没有任何有限返回阶段，并对应为独立句。

这已经是一个比“某命令超时”强得多的自馈非完成实例，也比旧 L5 Löb 条件目标多出了具体部分计算与对角 index。

它仍未满足现实相对 `N5`。尚未固定一个现实中可完成而理论中不可完成的同一任务，也未证明 HoTT 的某项抽象额外制造了这个分类要求。相反，当前结果更接近一种一般有效理论的内在边界：只要承担 universal computation 与 strong separation，就继承该非完成点。是否把它解释为用户所说的“程序的问题成为 HoTT 的问题”，需要一个 exact HoTT calculus 实例和自然自我担保消费者。

## 10. 下一最小可验工作

后续不应重复证明同一抽象对角。真正提高结论等级的接口有三项：

1. `PF-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001` 已从 `NatProofCode.checkProofNat` 构造 step-indexed proof/refutation classifier，机器证明 K/S/MP 语义一致性、跨 stage 确定性和 `FormalSystem` 四条双向对应；这项连接已经完成。
2. 下一未闭合接口是为一个具有足够算术的 object theory 证明 self-return-true/false 的 strong separation，或完整复用 Coq synthetic development 的 Robinson `Q` 实例。
3. 对 exact HoTT calculus 建立 sentence code、proof code、enumerable axioms 与 strong-separation 实例，判断这些元对象必须留在 outer theory，还是能在一个明确的 univalent reflective subuniverse 中取得。

当前小型 K/S/MP calculus 的 classifier 已完成，但它没有表示 self-return predicates 的公理或算术语言，不能提供 strong separation。第二项因此是现阶段唯一会把条件 theorem 真正变成对象理论不完备性实例的数学接口；第三项才决定该实例能否进一步指向 HoTT 自身。
