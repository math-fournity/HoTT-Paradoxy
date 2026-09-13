# SEM-B04：`solve-Precategory!` 反射求解器边界探针

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTRIBUTOR_FORMAL_PROBE`
>
> 分支：`codex/semantic-overview`
>
> run：`20260913-SEM-B04-PRECATEGORY-REFLECTION-001-01`

本目录保存三个最小 Agda 探针，用来核验固定版本 agda-unimath 的
`solve-Precategory!` reflection macro 在其实际承诺边界内做了什么。这里检查的是
**类型检查期间的证明项生成和拒绝行为**，不是编译后程序的运行语义，也不是 HoTT 或
Agda 的自验证定理。

## 固定输入

- Agda：`2.8.0-3d04bac`，二进制 SHA-256
  `ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e`；
- agda-unimath commit：`7b81411d9f60afec359d29ed1e4edf43f4711c8a`；
- agda-unimath tree SHA-256：
  `88460bc7d2e0ffd2bc85d60ca7fa0ea8e0b833bc12e1e6e9cd18ccd517db41c5`；
- solver source：`reflection/precategory-solver.lagda.md`，SHA-256
  `4e34f147a01b4ffce9deb863c25521fd997dddc1a072e94e1b03f5cf444a7882`；
- reflection TCM source：`reflection/type-checking-monad.lagda.md`，SHA-256
  `519f08b73ba6dd29cac3a41566a1b356147b9e27d96ba9970f1dd550c0b8a52e`。

完整文件清单及逐文件哈希位于 run 的 `source-manifest.json`。

## 三个探针

| 文件 | 目标 | 预期 | 本次结果 |
|---|---|---|---|
| `SemB04Positive.agda` | 三个态射复合的结合律 | 宏构造证明项且 Agda 接受 | exit `0` |
| `SemB04FalseEqualityNegative.agda` | 任意平行态射 `f ＝ g` | 归一形不相等，拒绝以 `refl` 填入 | exit `42`，`[UnequalTerms]` |
| `SemB04NonEqualityNegative.agda` | 非等式目标 `unit` | 在目标边界检查处拒绝 | exit `42`，`[GenericDocError]` |

正例只覆盖求解器声明支持的一类方程实例。两个负例证明本次固定输入没有静默接受这两类
错误目标；它们不构成“所有错误输入、所有依赖版本和所有 reflection macro 都会失败关闭”
的全称证明。

## 重放

从本 worktree 根运行：

```bash
python3 -B semantic-overview/tools/run_sem_b04.py
```

runner 对既有 run 目录执行拒绝覆盖；当前收据已存在，因此重复运行应以 exit `2` 停止。
若要进行新的证据运行，应复制 runner、分配新的 run ID，并保留旧目录不动。

本次 run 执行五步：打印 Agda 版本、以 `--ignore-interfaces` fresh 检查固定 solver 及其
实际导入闭包、运行一个正例和两个负例。run 目录保存原始 stdout/stderr、环境摘要、
source audit、source manifest 与机器可读 `RUN.json`。

## 解释边界

固定 solver 的路径是：读取并归约洞的目标、确认目标是等式、将两端重建为
`Precategory-Expression`、归一化，再构造
`solve-Precategory-Expression ... refl` 并用 `unify` 填洞。该 lemma 由归一化可靠性证明
把归一形相等送回原态射相等。因此正例展示的是“宏生成一个仍由 Agda 类型检查的证明项”。

reflection TCM 接口同时暴露 `declare-postulate`，但固定 solver 源码对该标识符的调用数为
零。该源码事实与本目录的行为探针共同支持对这个 solver 的有界判断；它不能替代对其他
宏、Agda reflection 实现或 safe 模式的单独审计。
