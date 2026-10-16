# R2-SEMIHALT-001：分阶段停机半判定与公平正见证枚举

> Proof ID：`MP-CUBICAL-SEMI-HALTING-001`  
> Claim IDs：`C-203`–`C-207`  
> Theory：Cubical Agda 2.8.0-3d04bac，Cubical library v0.9  
> Source：`SemiHalting.agda`  
> Parent semantics：`MachineHalting.agda`、`ProgramCode.agda`、`NatProgramCode.agda`、`FairEnumeration.agda`

## 工作包角色

本包关闭 `R2-SEMIHALT-001`。它把现有 bounded evaluator 组织成一个分阶段的 partial answer：

```agda
semiHaltAt : ℕ → ProgramCode → Config → Maybe Unit
```

每个给定 stage 的调用都由结构递归总结束。`just tt` 是已经找到有限停机见证的正答案；`nothing` 只表示该有限 stage 尚未找到见证，不被解释成程序永远不停机。这样，代码层接口保留了有限观察与无界否定之间的计算差异。

本包还把上一轮的全域公平 schedule 变成一个正见证枚举流，并证明每个 bounded positive case 都在其显式 `caseIndex` 处出现。它没有证明当前指令语言具备通用计算能力，也没有证明不存在某个不同的总停机判定器；后者必须等待 `R2-UNIVERSALITY` 与 certified reduction。

## 精确主张

### `C-203`：分阶段 partial answer 与持续性

```agda
isSome-semiHaltAt :
  (stage : ℕ) (program : ProgramCode) (input : Config) →
  isSome (semiHaltAt stage program input) ≡
  haltsWithin stage program input

semiHaltAt-persistent :
  (stage : ℕ) (program : ProgramCode) (input : Config) →
  isSome (semiHaltAt stage program input) ≡ true →
  isSome (semiHaltAt (suc stage) program input) ≡ true
```

因此每个有限 approximant 可执行；一旦发现正见证，下一阶段不会把它撤回。`nothing` 没有携带无界否定含义。

### `C-204`：精确步见证与 bounded observation 的双向桥梁

```agda
finalAt-implies-haltsWithin :
  finalAt stage program input ≡ true →
  haltsWithin stage program input ≡ true

haltsWithin-implies-CodeHalts :
  haltsWithin stage program input ≡ true →
  CodeHalts program input
```

第二个方向对有限界归纳：若当前状态终止，取精确步数 0；否则把剩余 bounded witness 递归转换为后继步数的精确 witness。结果进入 propositional truncation，不选择规范的最小停机时刻。

### `C-205`：`CodeHalts` 与 partial search 返回的双向对应

```agda
SemiReturns program input =
  ∥ Σ[ stage ∈ ℕ ]
      isSome (semiHaltAt stage program input) ≡ true ∥₁

CodeHalts↔SemiReturns :
  (program : ProgramCode) (input : Config) →
  (CodeHalts program input → SemiReturns program input) ×
  (SemiReturns program input → CodeHalts program input)
```

这给出本 TaskSpec 内精确的半判定正确性和完备性：存在有限停机见证，当且仅当某个有限搜索阶段返回正答案。这里的“双向对应”是两条函数，不声称已经构造 universe-level equivalence。

### `C-206`：公平的全域正见证枚举

```agda
enumerateHalting : ℕ → Maybe SearchCase

isSome-enumerateHalting :
  (index : ℕ) →
  isSome (enumerateHalting index) ≡ observeAt index

bounded-case-eventually-emitted :
  haltsWithin stage program input ≡ true →
  isSome (enumerateHalting (caseIndex program input stage)) ≡ true

canonical-emission-sound :
  isSome (enumerateHalting (caseIndex program input stage)) ≡ true →
  haltsWithin stage program input ≡ true
```

`enumerateHalting` 逐个执行公平 schedule 的 bounded observation，只在观察为 `true` 时发出 `caseAt index`。完备性使用上一包的显式 `caseIndex`；soundness 把正发射还原为原始 `haltsWithin`。

### `C-207`：停机与持续运行控制

```agda
haltCode-returns-at-zero :
  isSome (semiHaltAt zero haltCode initial) ≡ true

loopCode-never-returns : (stage : ℕ) →
  isSome (semiHaltAt stage loopCode initial) ≡ false

loopCode-not-SemiReturns : ¬ SemiReturns loopCode initial
```

同时，`haltCode-scheduled-positive` 与 `loopCode-scheduled-negative` 证明两个控制在公平枚举中的规范索引上仍分别为正和负。这里确实构造并机器证明了一个具体持续运行程序在每个有限 stage 都没有返回；这仍只是该显式程序的归纳不变量，不是通用停机不可判定定理。

## 禁止外推

本证明包不建立：

- 当前双计数器 `ProgramCode` 语言对某个标准通用机器模型的编译正确性；
- 对所有程序不存在总停机判定器；
- halting problem 的 certified many-one reduction；
- s-m-n、代码专门化、自应用或 Kleene recursion theorem；
- Gödel／Rosser／Löb 或 exact HoTT calculus 的不完备性；
- 这些半判定事实依赖 univalence、HIT 或高阶 path；
- natural consumer、现实同任务 A/B 失配或 HoTT 内部矛盾。

因此本包证明的是“正停机性质可由有限阶段半判定和公平枚举捕获”，并把无界负结论留空。下一项应进入 `R2-UNIVERSALITY`：固定标准机器模型或已知通用的两计数器模型，给出翻译、逐步模拟、终止保持及逆向充分性，再将经典不可判定性结论以 certified reduction 连接到当前 `ProgramCode`。

