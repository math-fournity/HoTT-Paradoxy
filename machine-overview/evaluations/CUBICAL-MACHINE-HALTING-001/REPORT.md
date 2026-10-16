# Cubical Agda 对象机器的具体停机与发散证明

> Evaluation：`CUBICAL-MACHINE-HALTING-001`
> Proof ID：`PF-CUBICAL-MACHINE-HALTING-001`
> Claim IDs：`MP-CMH-HALTS-001`、`MP-CMH-DIVERGES-001`、`MP-CMH-NOT-HALTS-001`
> 结果等级：`R1 CERTIFIED_DIVERGENCE`
> 门禁状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED`
> 日期：2026-09-14

## 1. 这次证明了什么

本评价在 Cubical Agda 中定义一台确定性的两计数器指令机器：

```agda
data Instr : Type where
  inc0 : ℕ → Instr
  inc1 : ℕ → Instr
  dec0 : ℕ → ℕ → Instr
  dec1 : ℕ → ℕ → Instr
  halt : Instr

Program = ℕ → Instr
```

configuration 包含 program counter 和两个自然数寄存器。`step` 是总的确定性转移，`iterate n` 执行有限的 `n` 步，
`isFinal` 判断当前 label 的指令是否为 `halt`。

停机命题定义为：存在一个有限步数使机器到达 final，并用命题截断消去“选择哪一个停机步数”的额外结构：

```agda
Halts P initial =
  ∥ Σ[ n ∈ ℕ ]
      isFinal P (iterate n (step P) initial) ≡ true
  ∥₁
```

具体发散定义为每个有限步观察均未到达 final：

```agda
Diverges P initial =
  (n : ℕ) →
    isFinal P (iterate n (step P) initial) ≡ false
```

证明文件随后给出：

```agda
halt-now : Halts haltProgram initial

loop-diverges : Diverges loopProgram initial

loop-not-halts : ¬ Halts loopProgram initial
```

`haltProgram` 在每个 label 上都是 `halt`，所以 `zero` 是停机见证。`loopProgram` 在每个 label 上都是 `inc0 zero`；无论
执行多少有限步，`isFinal` 都判断为 `false`。`loop-not-halts` 将任何被截断的 halting witness 消去到 `⊥`：同一个 Bool
一方面由见证等于 `true`，另一方面由 `loop-diverges` 等于 `false`。

## 2. 为什么证明项会完成

`loopProgram` 表示一个没有有限 halt 状态的对象程序；Agda proof term 没有模拟“真的运行到无限”。
`loop-diverges` 接收任意有限 `n`，通过程序的定义直接计算 `isFinal`，返回一个有限的 Path `refl`。全称量词表达“每一个
有限观察都失败”，证明器只检查该函数对任意 `n` 的结构是否正确。

因此，这项结果清楚地区分：

```text
modeled program has no finite halting witness
                           ≠
proof checker does not complete
```

这是“机器证明不能停机”的严格含义之一：机器证明系统以一个会完成核验的证明对象，证明另一台形式机器不会到达停机状态。

## 3. 原生证明门禁

| 项目 | 固定值 |
|---|---|
| Source | `HoTT/formal/cubical-machine-halting/MachineHalting.agda` |
| Claim specification | `HoTT/formal/cubical-machine-halting/CLAIM.md` |
| Toolchain | `HoTT/formal/partiality-race-timeout/TOOLCHAIN.json` |
| Agda | `2.8.0-3d04bac` |
| Cubical library | `v0.9` / tag commit `b150186d2544e7efeddd31e5d14a8b9ecbb100f7` |
| Run | `HoTT/verification/runs/20260914-CUBICAL-MACHINE-HALTING-001/` |
| Kernel result | `KERNEL_ACCEPTED_WITH_SCOPE` / exit 0 / stderr 0 |
| Index | `HoTT/CLAIM_EVIDENCE_MATRIX.md`；4 rows frozen |
| Independent replay | `PASS_WITH_SCOPE`; `EXACT_EXIT_STDOUT_STDERR_MATCH` |
| Git status | `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

Run package 保存 `RUN.json`、原始 stdout/stderr、environment、source manifest 和 index-row manifest。外部依赖由 Agda
release asset、二进制、Cubical release asset、library file 和 1111-file source tree 的 hash 固定。

本次运行同时验证了 canonical capture 的 linked-worktree 兼容修复：run 中 `git.linked_worktree=true`，git root、git-dir、
common-dir、branch 和 exact HEAD 均由 `git rev-parse` 得到，而不是要求 `.git` 必须是目录。

## 4. HoTT 成分与非 HoTT 成分

`Halts` 使用 Cubical library 的 propositional truncation，这是一个 HoTT/HIT 成分：停机命题只保留“有某个有限见证”，
不让不同见证携带额外可观察结构。`loop-not-halts` 使用 truncation recursor 消去到 proposition `⊥`。

但具体机器的发散机制只依赖自然数、Bool、确定性有限步迭代和一个常量非 halt 程序。普通依赖类型论或其他证明助理也能
表达同一证明。因此本评价建立的是：

```text
CONCRETE_DIVERGENCE_FORMALIZABLE_IN_CUBICAL_HOTT
```

而不是：

```text
HIGHER_PATHS_OR_UNIVALENCE_CAUSE_DIVERGENCE
```

这一负面区分是后续 HoTT 必要性分析的基线。

## 5. 与方向 A、方向 B 和现实对应的关系

这项证明为两类方向提供共同的对象语言底座：

- 方向 A 可以把理论新增的无限完成义务编译为某个 `Program`，再判断现实任务完成而形式程序是否满足 `Diverges`；
- 方向 B 可以把未经计算合法性判断的构造编译为 `Program`，再检查它是否缺少 `Halts` 见证。

但本评价中的 `loopProgram` 是人为选择的常量循环，并没有对应任何已固定的现实任务。它证明“此程序不停止”，没有证明
“HoTT 把一个现实可完成任务异化为不停止程序”。因此现实对应仍为 `NOT_ESTABLISHED`。

## 6. 为什么这还不是停机不可判定性

具体发散与全称不可判定性不同：

```text
R1:  Diverges loopProgram initial

R2:  ¬ ((P : Program) (c : Config) → Dec (Halts P c))
```

当前 `Program = ℕ → Instr` 是一个函数空间；尚未给出有限语法编码、枚举、decode、universal evaluator、自应用或从标准
不可判定问题到 `Halts` 的 many-one reduction。没有这些构造，不能从一个 loop instance 推出 R2。

下一阶段需要选择：

1. 把 Program 改为有限、可编码的 instruction table，构造 universal evaluator 和 diagonal program；或
2. 复用一项已经机器证明的 Minsky/Turing/λ-calculus 停机不可判定性，再给出保真 reduction。

二者都必须由 proof assistant 证明，不能用大量随机运行、长时间未返回或有限枚举替代。

## 7. 为什么这还不是 Gödel 不完备性

本评价没有 Sentence、Formula、ProofCode、substitution、`Prov_T`、derivability conditions 或 fixed-point sentence。
`loopProgram` 的自循环是程序控制流，不是一个陈述自身不可证明性的对象层句子。

因此 Gödel 状态仍是：

```text
NO_PROVABILITY_PREDICATE_OR_DIAGONAL_SENTENCE
```

不过，这个对象机器底座对 Gödel 路线仍有间接价值：停机不可判定性与 recursively enumerable theoremhood 可以通过精确
reduction 连接；这种连接必须在后续 `R2 → R3/R4` 阶段明确构造。

## 8. 结果等级

| 等级 | 当前状态 |
|---|---|
| `R0 operational observation` | 已超越：结论不依赖 timeout |
| `R1 certified divergence instance` | `PASS`：`loop-diverges` 与 `loop-not-halts` machine checked |
| `R2 certified undecidability` | `OPEN`：缺程序编码、universal evaluator 与 diagonal/reduction |
| `R3 HoTT proves Incomplete(T)` | `OPEN` |
| `R4 metatheory proves Incomplete(MiniHoTT)` | `OPEN` |
| `R5 trusted HoTT derives ⊥` | `NOT_ESTABLISHED` |

按现实相对资格轴，本评价具有机器证明但不具有现实对应或 HoTT 特有性；不能把 `R1` 误读为 `N3/N5`。

## 9. 下一项最小可验证工作

1. 定义有限 instruction table 和 code/decode，而不是继续使用不可枚举的函数空间作为 universal-machine 输入；
2. 机器证明 `decode (encode P) ≡ P` 的适用范围和 bounded interpreter 的一步/多步保真；
3. 构造一个足够表达两计数器机器的有限 ProgramCode；
4. 选择 diagonal 或既有 reduction 路线，冻结 exact theorem；
5. 并行利用当前 repo 已有 `ERCF3-T3` 的 repaired formula coding/substitution 结果，继续补 proof predicate 表示性和 fixed-point 义务。

这两条主链分别通向 R2 和 R3/R4；它们共享编码、替换、可表示性与层级纪律，但不能用彼此的阶段性结果冒充完成。
