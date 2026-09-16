# R2-MM2-BRIDGE-001：两计数器源模型到 `ProgramCode` 的编译保持

> Proof ID：`MP-CUBICAL-MM2-BRIDGE-001`  
> Claim IDs：`C-209`–`C-213`  
> Theory：Cubical Agda 2.8.0-3d04bac，Cubical library v0.9  
> Source：`MM2Bridge.agda`  
> Parent semantics：`MachineHalting.agda`、`ProgramCode.agda`、`NatProgramCode.agda`  
> External source qualification：`MP-COQ-MM2-UNDECIDABILITY-REPLAY-001` / `C-208`

## 工作包角色

本包完成 `R2-UNIVERSALITY-001` 的编译桥核心，但不宣称整个 universality／undecidability 链已经闭合。它在 Cubical Agda 内定义一个与 Coq Undecidability Library `MM2.v` 指令约定逐项对应的函数式源模型：

- program counter 从 1 开始；
- `incA/incB` 增量后落到 `i+1`；
- `decA j/decB j` 在正计数器上减一并跳到 `j`，在零上落到 `i+1`；
- 标签 0 或超出有限程序表表示停止。

然后把每条源指令编译到项目既有 `Instr`，在目标 label 0 放置 `halt` 哨兵，并证明查表、终止观察、单步、有限运行和停机存在性全部保持。

Coq 原文件使用关系闭包与 `mm2_stop`，本包使用确定性 totalized step 加 `mm2IsFinal`。两者的语义对应已经逐条审计，但还没有一个 proof assistant 同时读取两种语言的 AST 并证明跨语言等价。因此 C-208 不能仅凭本包自动搬运成关于当前 Agda `ProgramCode` 的 synthetic-undecidability 定理。

## 精确主张

### `C-209`：源模型与查表编译

```agda
data MM2Instr : Type where
  incA incB : MM2Instr
  decA decB : ℕ → MM2Instr

compileMM2 : MM2Program → ProgramCode

lookup-compileMM2 :
  (program : MM2Program) (label : ℕ) →
  lookupInstr (compileMM2 program) label ≡
  compileObserved label (lookupMM2 program label)
```

`compileTail` 按当前位置写入显式 fall-through label；`lookup-compileTail` 处理自然数加法与递归位置。目标 label 0 的 `halt` 哨兵同时实现源 jump-to-zero 与源停止标签。

### `C-210`：终止观察与单步保持

```agda
compileFinal-agrees :
  mm2IsFinal program state ≡
  isFinal (decode (compileMM2 program)) state

compileStep-agrees :
  mm2Step program state ≡
  universalStep (compileMM2 program) state
```

证明覆盖四种指令、两个 decrement 的零／后继分支、label 0 与表外缺省分支。

### `C-211`：全部有限运行与精确终止观察保持

```agda
compileRun-agrees :
  mm2Run steps program state ≡
  runFor steps (compileMM2 program) state

compileFinalAt-agrees :
  mm2FinalAt steps program state ≡
  finalAt steps (compileMM2 program) state
```

这两个定理对任意程序、输入状态和有限步数全称量化，不只是样例测试。

### `C-212`：有限停机存在性的双向保持

```agda
MM2Halts↔CodeHalts :
  (program : MM2Program) (state : Config) →
  (MM2Halts program state → CodeHalts (compileMM2 program) state) ×
  (CodeHalts (compileMM2 program) state → MM2Halts program state)
```

两个停机命题都使用 propositional truncation 包装有限精确步 witness；转换不恢复规范或最小 witness，只保留同一个步数的终止等式。

### `C-213`：翻译控制

本包机器核验：空程序在 label 1 立即停止；单条 `incA` 正确增加 A 并落到表外，随后停止；`decA` 的零分支落到下一标签；正分支 jump 0 到停止哨兵；单条 `incA` 编译后具有 `CodeHalts` witness。这些控制覆盖本次编译最容易交换的 label 与分支方向。

## 与 C-208 的精确关系

C-208 已在 Coq 8.15.2 中重放：

```coq
MM2_HALTING_undec : undecidable MM2_HALTING
```

并且上游 `undecidable P` 的定义是：

```coq
decidable P -> enumerable (complement SBTM_HALT)
```

本包为相同指令约定建立 Agda 内部编译保持。当前可交付的组合判词是：

```text
EXTERNAL_MM2_SYNTHETIC_UNDECIDABILITY_REPLAYED
+ AGDA_LOCAL_MM2_TO_PROGRAMCODE_HALTING_EQUIVALENCE_PROVED
/ CROSS_LANGUAGE_THEOREM_TRANSPORT_NOT_MACHINE_PROVED
```

## 禁止外推

本证明包不建立：

- Coq 关系语义与 Agda 函数式源语义的机器核验跨语言等价；
- C-208 到当前 `ProgramCode` 的已机器证明 theorem transport；
- 纯构造元理论中的无条件 `¬ decidable CodeHalts`；
- 当前 `ProgramCode` 对所有可计算函数的内部表示性、s-m-n 或自应用；
- Gödel／Rosser／Löb 或 exact HoTT calculus 不完备性；
- univalence、HIT 或高阶 path 对该编译必不可少；
- natural consumer、现实同任务桥梁或 HoTT 内部矛盾。

下一项应在 Coq 一侧定义与本项目 TaskSpec 同构的 target evaluator，机器证明 `MM2_HALTING` 到该 target 的 reduction；并把两侧共享的逐构造子测试与规格哈希固定为跨内核 correspondence。只有在明确说明跨语言保真层级后，才能判断 R2 universality／synthetic undecidability 是否足够关闭。

