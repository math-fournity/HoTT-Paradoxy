# SEM-B02 形式探针：仅仅有限与决定分支

> 身份：`CANDIDATE_NOT_CURRENT / BRANCH_LOCAL_VERIFICATION`
>
> 理论配置：Agda without-K；agda-unimath `7b81411d9f60afec359d29ed1e4edf43f4711c8a`
>
> 判词：`NATURAL_THEORY_BRANCH_CONSUMER / EFFECTIVE_RUNTIME_NOT_AVAILABLE`

## 文件

| 文件 | 作用 | 预期 |
|---|---|---|
| `SemB02Kernel.agda` | 比较显式 `inr` 决定与 `has-decidable-equality-is-finite is-finite-bool`，将两者映到 Bool tag | kernel 接受；两个命题等式成立 |
| `SemB02DefinitionalNegative.agda` | 用 `refl` 建立有限性路径的 `finiteTag ＝ false` | `[UnequalTerms]` |
| `SemB02ExplicitRuntime.agda` | 以构造子消去式 FFI 打印显式决定分支 | Node 输出 `FALSE` |
| `SemB02FiniteRuntime.agda` | 打印从仅仅有限性得到的决定分支 | typecheck/JS 生成成功；Node 在 postulate 依赖初始化处失败 |

## 唯一运行入口

```bash
python3 -B semantic-overview/tools/run_sem_b02.py
```

运行器拒绝覆盖已有 run。当前收据：

```text
semantic-overview/runs/20260913-SEM-B02-FINITE-DECISION-001-01/
```

收据保存 13 个步骤的 argv、退出码、原始 stdout/stderr、22 项源码/工具链 manifest、自然消费者 source audit，以及普通/优化 JS 的关键生成物。核心结果是：

- `equality-finite-types` fresh kernel 重放 exit 0，310 条 `Checking`；
- 闭合 kernel 正例 exit 0，`refl` 负例 exit 42 / `[UnequalTerms]`；
- 显式决定 JS/Node 输出 `FALSE`；
- 有限性定理模块的普通和优化 JS 都生成成功，但 Node 在 `equiv-unit-trunc-unit-Set` 的 postulate 依赖处退出 1；
- 没有返回错误决定分支，失败发生在 main 取得结果之前。

## 边界

本探针证明固定源码与工具链的 kernel/JS 行为。显式决定与仅仅有限的输入资格不同；Node 失败发生在传递模块初始化；固定库没有被证明承诺有效执行。因此它不建立同任务现实失配、不证明所有有限性实现不可计算，也不证明 HoTT 内部矛盾。
