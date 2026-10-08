# 分支上的形式包

> GPT 各线在各自分支上写成的形式包，以及它们的去向。权威记录是 `HoTT/CLAIM_NAMESPACE_LEDGER.md` §3；分支命题用前缀 D01、D02、D09 区分。

| 分支（提交） | 包 | 编号 | 去向 | 说明 |
|---|---|---|---|---|
| dev-01（`f10899cb`） | `zfc-dense-quantized-motion`、`zfc-dense-quantized-contract`、`zfc-meta-subtheory-adequacy` | D01-C-369–C-371 | 已并入 `dev`（`4a3535d9`，逐字节相同） | 稠密性与运动的机器控制。归入无哥德尔路线的组件，见第 02 章 |
| dev-09（`ac6391b6`） | `cubical-godel-fragment` | D09-C-370–C-386 | 已并入 `dev`（`4a3535d9`） | Cubical Agda 中的哥德尔编码片段，只到语法形状，没有对象层的可表示性定理 |
| dev-09 | `external-foundation-incompleteness` | D09-C-369 | 留在分支 | 运行依赖已不存在的 `/tmp` 检出；作用已被 CG001-C-102 与 C-95–C-101 取代 |
| dev-02（`4005fa80`） | `zfc-actual-q-policy`（分支版） | D02-C-359–C-365 | 留在分支 | 与 `dev` 同路径而内容不同，合并会形成双重真值；是条件性政策演算 |
| dev-03（`854a6aba`）、dev-04（`f97bbcb4`） | `zfc-observation-boundary`（两版） | 无 C 编号（`MP-ZFC-OBSERVATION-BOUNDARY-001` 等） | 留在分支 | 两版各自分叉；是条件性政策演算。来源卡（UOU 教材、SEP）在终局报告中按“分支@提交:路径”引用 |
| dev-06、dev-07 | 无新的形式包 | — | 留在分支 | Pattern-First 的方案、卡片与审计；H0 过程锚七字段已由 CG-005 吸收 |

## 取用

- 用 `git show <分支>@<提交>:<路径>` 读，不要切换检出。
- 并入前先看映射表 §3 的理由，并按 `HoTT/CLAIM_NAMESPACE_LEDGER.md` 的规则编号：`dev` 的下一个共享编号是 C-387。

## 下一步

无。只有当某个包对第 01、02 章的推进有直接用处时，才按需取用。
