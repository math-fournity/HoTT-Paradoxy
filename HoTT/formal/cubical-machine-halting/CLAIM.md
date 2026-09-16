# Cubical Agda 中固定程序的停机与发散校准

> Proof ID：`MP-CUBICAL-MACHINE-HALTING-001`  
> Claim IDs：`C-188`–`C-190`  
> Theory：Cubical Agda 2.8.0-3d04bac，Cubical library v0.9  
> Source：`MachineHalting.agda`

本证明包把一个确定性的双计数器指令语言、有限步观察、停机命题与发散谓词写进 Cubical Agda。它的任务是校准“对象程序不停止”与“证明检查过程不停止”之间的区别，并为后续 `R2-PROGRAMCODE-001` 的程序编码、通用性和自指义务提供一个可重放基线。

源码逐字节取自只读贡献 worktree `/Volumes/D/HoTT-machine-overview` 中已经审计过的候选，候选 SHA-256 为 `c53089ec3f2b0c69f47f34748d8379f4840ec4272d5f232f29234a67b0e807e8`。本主库为它分配自己的 proof/claim/run 身份并使用本主库工具链重新检查；外部 run 不作为当前证据。

## 精确主张

### `C-188`：停机正控制

在源码给定的 `Instr`、`Program`、`Config`、`step`、`iterate`、`isFinal` 与命题截断停机定义下：

```agda
halt-now : Halts haltProgram initial
```

见证的有限步下标是 `zero`，因为 `haltProgram` 把每个标签映射到 `halt`。

### `C-189`：固定循环程序在每个有限步都未终止

在同一组定义下：

```agda
loop-diverges : Diverges loopProgram initial
```

展开 `Diverges` 后，精确量词是：

```agda
(n : ℕ) →
  isFinal loopProgram
    (iterate n (step loopProgram) initial)
  ≡ false
```

`loopProgram` 把每个标签映射到 `inc0 zero`，所以任意有限观察下标上的 `isFinal` 都计算为 `false`。

### `C-190`：固定循环程序没有截断的有限停机见证

在同一组定义下：

```agda
loop-not-halts : ¬ Halts loopProgram initial
```

证明把命题截断消去到空类型：任何有限停机见证都断言同一个布尔终止测试为 `true`，而 `loop-diverges` 断言它为 `false`。

## 假设、结构与对应边界

- 源码未引入 `postulate`。
- 精确 `OPTIONS` 行启用 Cubical Agda、`--safe` 与 guardedness 检查。
- `Halts` 使用 Cubical library 的命题截断；机器一步转移及固定程序的不变量仍处于集合／命题层。
- `halt-now`、`loop-diverges` 与 `loop-not-halts` 的证明项由 Agda kernel 检查完成。被证明没有有限停机见证的是建模对象 `loopProgram`；证明检查器本次运行自身应正常结束。
- 这是 `R1-FIXEDMACHINE-001` 校准，不满足长期目标所要求的 HoTT-essential、自然消费者与同一现实任务三项条件。

## 禁止外推

本证明包不建立：

- 所有程序上的停机不可判定性；
- 当前 `Program` 表示中通用机的存在或不存在；
- Gödel 句、可证性谓词或不完备定理；
- 发散的 HoTT 特有原因；
- HoTT 或 Cubical Agda 的矛盾；
- 与物理过程或社会过程的同任务现实对应；
- 关于所有机器、时间或计算概念的全称结论；
- “证明检查器不停止”这一运行事实。
