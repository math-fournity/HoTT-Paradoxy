# R2-NATCODE-001：指令／程序的自然数编码与数值有界解释器

> Proof ID：`MP-CUBICAL-NAT-PROGRAM-CODE-001`  
> Claim IDs：`C-195`–`C-198`  
> Theory：Cubical Agda 2.8.0-3d04bac，Cubical library v0.9  
> Source：`NatProgramCode.agda`  
> Parent semantics：`MachineHalting.agda`、`ProgramCode.agda`

## 工作包角色

本包完成 `R2-NATCODE-001`：把 R2 第一薄层的 `Instr` 与有限 `ProgramCode` 映入自然数，给出对全部自然数有定义的 decoder，并证明合法编码像上的往返、单射、覆盖与有界执行语义保持。它使用自定界一元参数、固定指令标签、显式程序终止位，以及带前导 sentinel 的最低位优先 bit-list 编码。

本包中的“数值解释器”仍以外部 fuel 为界，只回答给定有限步数内的状态／终止观察。它没有构造 `(program,input,fuel)` 的公平交错调度，也没有证明当前双计数器语言的计算通用性或停机不可判定性。

## 精确主张

### `C-195`：自然数编码、总解码与非法码策略

`bitsInstr` 为五个合法指令构造子分配三位标签：

```text
000 halt
001 inc0
010 inc1
011 dec0
100 dec1
```

参数使用 `n` 个 `true` 后接一个 `false` 的自定界一元码；`bitsProgram` 用 `true` 引入一个指令、用 `false` 终止有限表。`codeBits` 把 bit list 编为自然数，`unbits` 以自然数自身作为 fuel 取回低位流。由此定义：

```agda
encodeNat : ProgramCode → ℕ
decodeNat : ℕ → ProgramCode

encodeInstrNat : Instr → ℕ
decodeInstrNat : ℕ → Instr
```

decoder 对每个自然数都终止并有结果。默认行为被固定为：fuel 为零或 bit stream 提前结束时返回 `pcNil`；未分配标签 `101`、`110`、`111` 均解释为 `halt`；空自然数码的控制与一个具体 `101` 自然数码分别由下列命题核查：

```agda
decodeNat-zero : decodeNat zero ≡ pcNil

decodeNat-invalid101 :
  decodeNat invalid101Nat ≡ pcCons halt pcNil
```

`invalid101`、`invalid110`、`invalid111` 还分别固定三个 parser-state 等式，而不是仅在文档中描述默认分支。

### `C-196`：合法像往返、单射与 decoder 覆盖

bit bundle 的取回、长度界、流式 parser 与编码自身作为 fuel 的界共同给出：

```agda
decodeNat-encodeNat :
  (code : ProgramCode) → decodeNat (encodeNat code) ≡ code

encodeNat-injective :
  (left right : ProgramCode) →
  encodeNat left ≡ encodeNat right → left ≡ right

decodeNat-surjective :
  (code : ProgramCode) →
  Σ′ ℕ (λ number → decodeNat number ≡ code)

decodeInstrNat-encodeInstrNat :
  (instruction : Instr) →
  decodeInstrNat (encodeInstrNat instruction) ≡ instruction

encodeInstrNat-injective :
  (left right : Instr) →
  encodeInstrNat left ≡ encodeInstrNat right → left ≡ right
```

这里的 surjectivity 是 `decodeNat : ℕ → ProgramCode` 对有限程序表的覆盖：每个程序至少在其 `encodeNat` 位置出现。它没有给出多维任务的公平访问次序。

### `C-197`：数值有界解释器在编码像上的语义保持

```agda
runNat : ℕ → ℕ → Config → Config
finalNat : ℕ → ℕ → Config → Bool
haltsWithinNat : ℕ → ℕ → Config → Bool
```

对任意有限程序表、状态与 fuel，数值解释器先解码其自然数，再调用既有 R2 解释器；合法像上的三项语义分别相等：

```agda
runNat-on-image :
  (fuel : ℕ) (code : ProgramCode) (state : Config) →
  runNat fuel (encodeNat code) state ≡ runFor fuel code state

finalNat-on-image :
  (fuel : ℕ) (code : ProgramCode) (state : Config) →
  finalNat fuel (encodeNat code) state ≡ finalAt fuel code state

haltsWithinNat-on-image :
  (fuel : ℕ) (code : ProgramCode) (state : Config) →
  haltsWithinNat fuel (encodeNat code) state ≡
  haltsWithin fuel code state
```

### `C-198`：编码后的停机／循环控制

R2 原有的停机与循环程序经自然数编码后仍具有同一有限观察行为：

```agda
haltNat-within : (fuel : ℕ) →
  haltsWithinNat fuel (encodeNat haltCode) initial ≡ true

loopNat-not-final : (fuel : ℕ) →
  finalNat fuel (encodeNat loopCode) initial ≡ false

loopNat-never-within : (fuel : ℕ) →
  haltsWithinNat fuel (encodeNat loopCode) initial ≡ false
```

## 禁止外推

本证明包不建立：

- `(program,input,fuel)` 或任意多维自然数任务的公平／无饥饿枚举；
- 当前双计数器指令语言的通用计算能力；
- 通用停机问题不可判定或任何 certified reduction；
- s-m-n 代码专门化、Kleene 递归定理或自应用；
- 对象理论的公式／证明编码、可证性表示、Gödel／Rosser／Löb 定理；
- HoTT 规则对本编码结论的数学必要性；本包使用 Cubical Agda 内核，但主要编码结构是一般可计算语法工程；
- natural consumer、现实同任务桥梁、方向 A／B 的现实相对不相容；
- HoTT 或 Cubical Agda 的内部矛盾。

因此本包只关闭 `R2-NATCODE-001`，并为下一项 `R2-FAIR-001` 提供可数程序入口。R2 的公平调度、半判定、通用性与不可判定仍保持开放。
