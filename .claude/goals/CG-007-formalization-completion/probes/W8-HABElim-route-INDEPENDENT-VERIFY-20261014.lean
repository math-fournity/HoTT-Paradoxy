/-! ## ★★ `hAll` 的**第二条独立路线**——9276 线独立核验（2026-10-14）

Master 报 001-Flash 的 `HABElim` 路线也把 `hAll` 无条件化（`fd8b8305`）。
本文件记**我自己的独立复现**——两条路线到同一结论，交叉验证。

### 复现方法

* 资产：`fd8b8305` 的 `.cg009-verification/round31/src/`（136 文件）
  ——**该树无任何预编译 olean**，故全部从源码编译（`skipped=0`）
* `git archive` 提取到 `/private/tmp/cg007-habelim-verify/`（不动共享树）
* 自写 driver（**Kahn 拓扑序**），`cwd = ASM` + `LEAN_PATH` 模式
* 目标：`GodelQ.ZFC.HAllUncond`

### 结果（本机实跑）

```
closure=70  ordered=70  skipped=0
compiled OK=70/70 skipped=0 (201s)
```

```
GodelQ.HAllUncond.hAll : [propext, Classical.choice, Quot.sound]
```

**无 `sorryAx`，`skipped=0`。** 与 Master 报的「70 模块、skipped=0」**逐项吻合**。

### 两条路线的关系（**关键：它们不同**）

| | 路线 A（装配，`701a0e3d`） | 路线 B（HABElim，`fd8b8305`） |
|---|---|---|
| 证什么 | `AllBlockerQ`（我定义的 blocker） | `hAll`（`ShCraigElimBranches` 风格的直接形式） |
| 桥怎么来 | `iT_subst_open` 的 m=0 实例（**等式**） | `HABElim.hAB_derivable`（**重言式**，`A → (C → A)`） |
| 规模 | 41 文件（9276 种子 + 40 移植） | 70 文件（全从源码） |
| 交叉点 | 都用到本线 `allKey_of_bridge`/`allBlockerQ_of_key` 或 `HAllProof.hAll_uncond` | 同 |

**路线 B 的机制**（`HAllUncond.lean` 源码）：`HAllProof.hAll_uncond` 的唯一前提 `hAB`
由 `HABElim.hAB_derivable p hpS` 提供——**不是等式桥，是命题重言式**
（`A → (C → A)`，`A = free (iT 1 p)`、`C = subst ?[^&0] domZero`）。
故它与路线 A 的数学内容**不同**，是**独立**的。

### 移植成本对比（给生产包选型）

* 路线 A：41 文件，但含 9276 已有的 33 个种子 ⟹ **净移植 40 文件**
  （含 `ITSubstOpen1-9` 链 + `QvecV` + `SubstDomZero`）
* 路线 B：70 文件全从源码，但**净移植取决于 9276 已有什么**——
  需先算 9276 ∩ 路线 B 闭包。已知路线 B 闭包含 `ZFC.Effective`/`Soundness`/
  `Z0Shadow`/`PAModel`/`R0Model`/`FoundationArith`/`GodelZenoRunner`/`EffectiveTheory`/
  `ProcessObservation` 等 **9276 也有的**（W1/W2 的图灵与时间结构），
  故净移植可能比路线 A **更小**。

**结论**：两条路线都成立且都独立复现。**选型时按「净移植文件数」而非总规模定**
——建议下一步先算路线 B 的净差集。

### 复现要点（我踩的坑，与路线 A 同）

1. `LEAN_PATH` 要 11 项（build / Foundation / Mathlib / 8 个 Mathlib 包）——少一个编译不过；
2. **拓扑序必须用标准 Kahn**（我自写的「就绪集」版本有 bug，误报 CYCLE，
   白花两轮排查——**误报的 CYCLE 要先怀疑自己的算法**）；
3. `skipped=0` 才作数（本树无预编译，天然满足）。 -/
