# SEM-B01 形式探针：公理化截断的数学与交付边界

> 身份：`CANDIDATE_NOT_CURRENT / BRANCH_LOCAL_VERIFICATION`
>
> 理论配置：Agda without-K；agda-unimath `7b81411d9f60afec359d29ed1e4edf43f4711c8a`
>
> 判词：`KERNEL_ACCEPTS_PROPOSITIONAL_COMPUTATION / RUNTIME_POSTULATE_BOUNDARY`

## 验证对象

本目录用一个闭合 `unit → bool` 弱常值函数，隔离验证
`map-universal-property-set-quotient-trunc-Prop` 的五层身份：类型、kernel、判断相等、后端生成和实际运行。

| 文件 | 作用 | 预期 |
|---|---|---|
| `SemB01Kernel.agda` | 从 `unit-trunc-Prop star` 得到 `truncatedResult : bool`，并用库的命题计算律证明 `truncatedResult ＝ true` | kernel 接受 |
| `SemB01DefinitionalNegative.agda` | 试图用 `refl` 证明同一等式 | `[UnequalTerms]`；确认没有 judgmental reduction |
| `SemB01DirectRuntime.agda` | 不经截断直接打印库 Bool | JS/Node 正控输出 `TRUE` |
| `SemB01TruncatedRuntime.agda` | 强制打印截断消费者结果 | typecheck/JS 生成成功；Node 在未实现的 `unit-trunc` 处失败 |

## 唯一运行入口

从 repo 根运行：

```bash
python3 -B semantic-overview/tools/run_sem_b01.py
```

运行器拒绝覆盖既有 run。当前收据：

```text
semantic-overview/runs/20260913-SEM-B01-TRUNCATION-DELIVERY-001-01/
```

该 run 保存 12 个步骤的 argv、退出码、原始 stdout/stderr、18 项源码/工具链 manifest、JS/GHC 关键生成物与哈希。中心结果为：

- fresh 多项式 kernel 重放 exit 0；
- 命题等式正例 exit 0；
- `refl` 负例 exit 42 / `[UnequalTerms]`；
- 直接 JS/Node 正控 exit 0 / `TRUE`；
- 截断 JS 生成 exit 0，Node exit 1 / `unit-trunc is not a function`；
- GHC 源码生成 exit 0，四个截断 postulate 均生成明确的运行错误；本机无 GHC，未执行。

## 证据边界

本探针证明固定实现与工具链的分层行为。它不证明所有命题截断都不可计算，不声称 agda-unimath 对这些接口承诺可执行交付，不执行完整多项式值，也不建立自然使用失配或 HoTT 内部矛盾。
