# SEM-B06：Cubical `CommRingSolver.solve!` 自然消费者探针

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTRIBUTOR_FORMAL_PROBE`
>
> 分支：`codex/semantic-overview`
>
> run：`20260913-SEM-B06-COMMRING-NATURAL-CONSUMER-001-01`

本目录核验 Cubical Agda v0.9 的 `CommRingSolver.solve!`。与只检查 solver 自带示例的
SEM-B04 不同，本轮同时 fresh 检查一个真实 production consumer：
`Cubical.Algebra.CommRing.Localisation.Base`。该模块在局部化的商关系、运算良定义与交换环
结构证明中调用 solver 13 次。

这里的交付面是 **Agda 类型检查期间生成并核验证明项**。本轮没有编译后程序或现实任务
承诺。

## 固定工具链

- Agda：`2.8.0-3d04bac`；binary SHA-256
  `ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e`；
- Cubical library：v0.9，tag commit
  `b150186d2544e7efeddd31e5d14a8b9ecbb100f7`；
- release archive SHA-256：
  `003f9c57c134e4a9401a4b339b3773be667aa169ff929ca3dfb9c8abefc225c5`；
- extracted source-tree SHA-256：
  `73ccfbaf960f252800da02dac6a9bbef72d1214e2907940466dc2abef2060a81`；
- `Reflection.agda` SHA-256：
  `997e0cdd46c81e5e24f79c028e2e63cec7847ccaf3ad164e2aff34b01e971eb1`；
- `Solver.agda` SHA-256：
  `b3d794a845531eb23fa34161480d713c40f4170b071349213ade4cf93a5f4601`；
- natural consumer SHA-256：
  `fbcf84b4dfffa6510a608db41dcf22e9d3b54a72993de4f97a23df5e3eb80d61`。

最终 `source-manifest.json` 不只固定四个入口文件，而是从两个 fresh stdout 的
`Checking ... (path)` 行重建实际导入闭包：solver 176 个、consumer 178 个，合并工具、探针
和审计输入后为 188 个唯一文件。

## 三个本地探针

| 文件 | 目标 | 结果 |
|---|---|---|
| `SemB06Positive.agda` | `x · (y + z) ≡ z · x + x · y` | exit `0` |
| `SemB06FalseEqualityNegative.agda` | 无假设的任意变量等式 `x ≡ y` | exit `42`，`[UnequalTerms]` |
| `SemB06NonEqualityNegative.agda` | 非等式目标 `fst R` | exit `42`，`[GenericDocError]` |

负例固定的是当前版本、当前两个越界形状的行为，不构成所有错误输入或未来 solver 版本的
全称失败关闭证明。

## 重放

从本 worktree 根运行：

```bash
python3 -B semantic-overview/tools/run_sem_b06.py
```

runner 执行六步：版本、solver fresh、natural consumer fresh、本地正例、假等式负例、非等式
负例。现有 run 目录受到拒绝覆盖保护；重复调用应 exit `2`，新证据必须分配新 run ID。

## 解释边界

reflection 层先读取并归约 goal，解析交换环等式，重建两端多项式及变量，再构造调用
`Solver.solve` 的 term，其中归一形等式参数为 `refl`，最后 `unify` 到洞。`Solver.solve` 通过
两端 `isEqualToNormalform` 把归一形相等组合回原表达式相等。

固定 `Reflection.agda`/`Solver.agda` 对 `declarePostulate` 的直接调用数为零。因此本轮正例
和 natural consumer 的成功属于 proof-term automation；不能由同一 Agda API 另有更强能力
推定该 solver 使用了公理引入。
