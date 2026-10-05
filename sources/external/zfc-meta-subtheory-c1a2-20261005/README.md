# C1A-2 外部原典快照：Isabelle/ZF 中的实数构造（2026-10-05）

> **身份：** `SOURCE_SNAPSHOT_MANIFEST / C1A-2_INPUT / NOT_A_CORE_VERDICT`。
>
> **固定上游提交：** `SKolodynski/IsarMathLib@e0d7f7d8aa523709e3b139305ba6570df7d68fdd`（`master` 在读取时的 OID）。

| 文件 | 原始 URL／身份 | SHA-256 | C1A-2 用途 |
|---|---|---|---|
| `IsarMathLib-README.md` | `https://raw.githubusercontent.com/SKolodynski/IsarMathLib/e0d7f7d8aa523709e3b139305ba6570df7d68fdd/README.md` | `4be3f07b001ddb6a244c5c306288874ecd818b733e05f5f6997e0e26cd03f6e0` | 项目自述为 Isabelle/ZF 数学库，并说明需要构建 ZF heap、可用 `isabelle build -D` 重新检查。 |
| `Real_ZF_1.thy` | 同 commit 的 `IsarMathLib/Real_ZF_1.thy` | `b7c7c7cc92a70b4e04aad2ce86c7dd02d5f918c54e30aa14875e1418b8d93802` | `eudoxus_reals_are_reals`：从整数加法群构造的实数给出 complete ordered field。 |
| `Real_ZF_2.thy` | 同 commit 的 `IsarMathLib/Real_ZF_2.thy` | `095a60f84c7d24092c77c3bdf78cbebd496f6269e6367380ea3cdb47a4ed4898` | 明确这套构造在 ZF world 中提供所需 real model；后续语境使用一个 complete ordered field，定义 metric/topology、supremum 等。 |
| `GitHub-tree-e0d7f7d8.json` | GitHub Git tree API, `?recursive=1` | `9342795ab1bfaf4099ad918a35d80f5fee7715c64090b4857fb692f2b0bf2537` | 当前候选版本的 327-entry tree；用于限制本轮 source search 的文件身份。 |

## 严格边界

- `Real_ZF_1.thy` 是 source-reported Isabelle/ZF theorem。本机未发现 `isabelle` 可执行文件，因此本项目没有重新检查这个 theorem。
- `eudoxus_reals_are_reals` 支付的是 **ZF 中实数模型／complete ordered field 的构造**，不是 Achilles/Dichotomy 的 finite-time theorem，也不是 IEP 的 actual promotion P。
- `Real_ZF_2.thy` 的 complete-field locale 以模型为条件，并不自动把一个指定的 partial-sum sequence 与目标关联。
- Git tree 检索与 selected-file 阅读只说明 C1A-2 的已读范围，不能证明整个仓库不存在某个可用的 sequence-limit theorem。
