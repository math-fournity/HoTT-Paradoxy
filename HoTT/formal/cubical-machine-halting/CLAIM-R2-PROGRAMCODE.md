# R2-PROGRAMCODE-001：有限程序语法与通用有界解释器

> Proof ID：`MP-CUBICAL-PROGRAM-CODE-001`  
> Claim IDs：`C-191`–`C-194`  
> Theory：Cubical Agda 2.8.0-3d04bac，Cubical library v0.9  
> Source：`ProgramCode.agda`  
> Parent semantics：`MachineHalting.agda`

## 工作包角色

本包把 R1 中的函数空间程序 `Program = ℕ → Instr` 替换为可归纳构造的有限指令表 `ProgramCode`，给出总 decoder 和以自然数 fuel 为结构递减参数的通用有界解释器。这里“通用”只表示同一个解释器接受本语法中的任意有限程序表；它不表示已经证明该语言具有通用计算能力。

## 精确主张

### `C-191`：有限程序表与总 decoder

`ProgramCode` 由 `pcNil` 与 `pcCons` 有限构造。`lookupInstr` 在表内按标签查找，表外统一返回 `halt`，所以：

```agda
decode : ProgramCode → Program

decode-head : (instruction : Instr) (rest : ProgramCode) →
  decode (pcCons instruction rest) zero ≡ instruction

decode-tail : (instruction : Instr) (rest : ProgramCode) (label : ℕ) →
  decode (pcCons instruction rest) (suc label) ≡ decode rest label

decode-outside-empty : (label : ℕ) → decode pcNil label ≡ halt
```

### `C-192`：通用有界解释器与 R1 语义一致

`runFor fuel code state` 对 fuel 做结构递归，因此对所有输入都是总函数；它与 R1 的 `iterate` 在任意程序表、状态和有限步数上相等：

```agda
runFor-agrees : (fuel : ℕ) (code : ProgramCode) (state : Config) →
  runFor fuel code state ≡ iterate fuel (step (decode code)) state
```

相应终止观察也一致：

```agda
finalAt-agrees : (fuel : ℕ) (code : ProgramCode) (state : Config) →
  finalAt fuel code state ≡
  isFinal (decode code) (iterate fuel (step (decode code)) state)
```

### `C-193`：停机正控制

单元素指令表 `haltCode = pcCons halt pcNil` 在任意 fuel 的 bounded observation 中均返回 `true`：

```agda
haltCode-within : (fuel : ℕ) → haltsWithin fuel haltCode initial ≡ true
```

### `C-194`：循环负控制与截断停机否定

单元素指令表 `loopCode = pcCons (inc0 zero) pcNil` 的程序计数器始终回到标签零。于是每个精确有限步的 `finalAt` 与每个有限界的 `haltsWithin` 都返回 `false`，并且不存在截断的有限停机见证：

```agda
loopCode-not-final : (fuel : ℕ) → finalAt fuel loopCode initial ≡ false

loopCode-never-within : (fuel : ℕ) →
  haltsWithin fuel loopCode initial ≡ false

loopCode-not-halts : ¬ CodeHalts loopCode initial
```

## 禁止外推

本证明包不建立：

- `ProgramCode` 到自然数的 Gödel 编码或总的数值 decoder；
- 对所有有限程序的公平枚举；
- 当前双计数器指令语言的通用计算能力；
- 通用停机问题不可判定；
- s-m-n、自应用、递归定理或 certified many-one reduction；
- Gödel 句、可证性谓词或任何不完备性定理；
- 发散的 HoTT 特有原因、自然消费者失配或现实同任务对应；
- HoTT 或 Cubical Agda 的内部矛盾。

因此本包只完成 `R2-PROGRAMCODE-001` 的第一薄层：有限语法、decoder、bounded evaluator、语义一致性与正负控制。R2 的枚举、通用性和不可判定部分仍开放。
