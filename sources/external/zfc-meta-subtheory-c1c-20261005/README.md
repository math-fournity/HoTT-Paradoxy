# C1C 外部原典快照：Isabelle/ZF 的 metric / uniform / halving sequence ingress（2026-10-05）

> **身份：** `SOURCE_SNAPSHOT_MANIFEST / C1C_INPUT / NOT_A_CORE_VERDICT`。
>
> **固定上游提交：** `SKolodynski/IsarMathLib@e0d7f7d8aa523709e3b139305ba6570df7d68fdd`；tree identity 与 C1A-2 相同。

| 文件 | 路径身份 | SHA-256 | C1C 用途 |
|---|---|---|---|
| `MetricUniform_ZF.thy` | pinned upstream `IsarMathLib/MetricUniform_ZF.thy` | `af123578a7a72c6c55c3642213a1e568e601564eb61b3a7e6a36cb1149d36021` | 明确的 `halving_seq_base` theorem：uniformity 中的 inductively defined halving sequence image 是 uniform base。 |
| `MetricUniform_ZF_1.thy` | pinned upstream `IsarMathLib/MetricUniform_ZF_1.thy` | `5b1a9cf57cf6e56642c346ebeb7a1c7ad9f412597d005c766351e98517d50e43` | countable entourages sequence / powerset infrastructure。 |
| `MetricSpace_ZF.thy` | pinned upstream `IsarMathLib/MetricSpace_ZF.thy` | `5e56316f584d9ed638dc57cdf6722ca97161e6f827c5059e6fa7fcba6ad4910f` | metric-space source ingress。 |
| `MetricSpace_ZF_1.thy` | pinned upstream `IsarMathLib/MetricSpace_ZF_1.thy` | `314c92b3420a184e09850e7108e6d66ba71da2a91bfd93b12d75b01585065d50` | metric-space continuation。 |
| `Topology_ZF.thy` | pinned upstream `IsarMathLib/Topology_ZF.thy` | `bc7841ac7bf95fa038789f31f1f4320bdc74b3a44d2cb9ec9b200b60922d01c3` | topology source ingress。 |
| `Topology_ZF_1.thy` | pinned upstream `IsarMathLib/Topology_ZF_1.thy` | `0880a596dd788872152afc6fed701e0d1fc1f6464a166470c38fd164c3922535` | topology continuation。 |

## 搜索范围与边界

- 上游 recursive tree 的 path-level filter 显示：`real=6`、`sequence=2`（其一是 `ExactSequence_ZF`，不是 real-analysis sequence）、`series=0`、`limit=0`、`conver=0`；这只是 frozen tree 的文件名层观察。
- 这次实际读取上述六个局部理论文件，并检索 `sequence/Cauchy/converg/limit/geometric/series/partial sum/tendsto`。命中的 substantive material 是 uniformity 的 halving/thirding entourage sequences；不是 IEP runner 的 geometric partial sums 或 endpoint-arrival theorem。
- 本机仍没有 Isabelle/ZF checker，故任何上游 theorem 在本项目的证据等级仍是 `SOURCE_REPORTED_FORMAL_THEOREM_UNREPLAYED`。
