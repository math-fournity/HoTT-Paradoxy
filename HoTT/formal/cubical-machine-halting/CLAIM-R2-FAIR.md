# R2-FAIR-001：程序、输入与 fuel 的公平有限阶段枚举

> Proof ID：`MP-CUBICAL-FAIR-ENUMERATION-001`  
> Claim IDs：`C-199`–`C-202`  
> Theory：Cubical Agda 2.8.0-3d04bac，Cubical library v0.9  
> Source：`FairEnumeration.agda`  
> Parent semantics：`MachineHalting.agda`、`ProgramCode.agda`、`NatProgramCode.agda`

## 工作包角色

本包完成 `R2-FAIR-001`。它把 `ProgramCode × Config × fuel` 的每个有限 case 放到一个明确的自然数索引，定义按索引 `0,1,2,…` 读取的总 schedule，并证明每个 case 在一个显式有限 stage 之前出现。因此“公平／无饥饿”由有限到达界而不是枚举直觉表达。

本包同时把 schedule 的某一位置连接到 R2 的 `haltsWithin`。它仍没有实现一个持续搜索到首个 `true` 才返回的 partial procedure，也没有从 `CodeHalts` 构造 semi-decidability／enumerability 定理；那是下一项 `R2-SEMIHALT-001`。

## 精确主张

### `C-199`：固定三元组与 `Config` 的自然数往返

三个自然数分别以自定界一元码串接，再复用 `NatProgramCode.codeBits/unbits`：

```agda
encodeTriple : ℕ → ℕ → ℕ → ℕ
decodeTriple : ℕ → Triple

decodeTriple-encodeTriple :
  (left middle right : ℕ) →
  decodeTriple (encodeTriple left middle right) ≡
  triple left middle right
```

从而 triple encoding 单射，decoder 覆盖所有三元组。`Config = (pc,r0,r1)` 使用同一编码：

```agda
encodeConfig : Config → ℕ
decodeConfig : ℕ → Config

decodeConfig-encodeConfig :
  (state : Config) → decodeConfig (encodeConfig state) ≡ state
```

并证明 `encodeConfig-injective` 与 `decodeConfig-surjective`。decoder 在缺参数／提前结束时由 `readUnary [] = 0` 给出总默认行为。

### `C-200`：公平 schedule 与无饥饿

```agda
caseAt : ℕ → SearchCase

caseIndex : ProgramCode → Config → ℕ → ℕ

caseAt-caseIndex :
  (program : ProgramCode) (input : Config) (fuel : ℕ) →
  caseAt (caseIndex program input fuel) ≡
  searchCase program input fuel
```

`AppearsBy stage target` 保存一个 `index ≤ stage` 及 `caseAt index ≡ target`。每个 case 以自身的 `caseIndex` 作为有限到达界：

```agda
eventuallyVisited :
  (program : ProgramCode) (input : Config) (fuel : ℕ) →
  AppearsBy (caseIndex program input fuel)
            (searchCase program input fuel)

noStarvation :
  (program : ProgramCode) (input : Config) (fuel : ℕ) →
  Σ[ stage ∈ ℕ ]
    AppearsBy stage (searchCase program input fuel)
```

这给出全域有限 case 覆盖；同一 case 可以在其它非法／非规范码位置重复出现，公平性不要求唯一索引。

### `C-201`：scheduled bounded observation 保持任务

```agda
observeAt : ℕ → Bool

observeAt-caseIndex :
  (program : ProgramCode) (input : Config) (fuel : ℕ) →
  observeAt (caseIndex program input fuel) ≡
  haltsWithin fuel program input
```

因此 schedule 不只是枚举三元组的形状；它在规范索引处执行的正是原来那个 bounded halting observation。

### `C-202`：公平 schedule 的停机／循环控制

```agda
haltCase-visited-true : (fuel : ℕ) →
  observeAt (caseIndex haltCode initial fuel) ≡ true

loopCase-visited-false : (fuel : ℕ) →
  observeAt (caseIndex loopCode initial fuel) ≡ false
```

正负控制说明三元组编码、schedule 与观察连接没有交换 `haltCode`／`loopCode` 的既有结果。

## 禁止外推

本证明包不建立：

- 一个在没有停机见证时仍总返回的 unbounded search；
- `CodeHalts` 的完整 semi-decider／enumerator；
- 当前双计数器语言的通用计算能力；
- 通用停机问题不可判定或 certified many-one reduction；
- s-m-n、代码专门化、程序自应用或 Kleene recursion theorem；
- Gödel／Rosser／Löb 或 exact HoTT calculus 不完备性；
- 公平编码依赖 HoTT 特有规则；
- natural consumer、现实同任务 A/B 失配或 HoTT 内部矛盾。

因此本包只关闭 `R2-FAIR-001`。下一项应以这条 schedule 构造 `R2-SEMIHALT-001`，证明：若某个程序／输入具有有限停机见证，则公平搜索最终发现一个 `true`；没有见证时不伪造总的否定答案。
