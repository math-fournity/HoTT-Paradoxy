# MP-RACE-TIMEOUT-001：partiality 结果商的竞争边界

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY`

本目录把 R041 纸笔证明单（`与Web GPT 交流用的文件夹/PROOF_NOTE(20260912-061537) - R401.md`）的核心操作闭包问题在原生 Cubical Agda 中机器核实：结果等价（只看“是否返回、返回什么”）可以支持顺序 `bind`，但不支持 `race` 与截止期 consumer。

## 固定模型（R041 §1 的一个忠实片段）

- 计算对象是单线程确定性 delay：`ω`（永不返回）或 `ret n a`（n 个内部回合后返回 a），即 R041 明示的 `δ^n now(a)` 族与 `ω`；
- `p ≈ q` 定义为 R041 §1 的收敛行为等价：对每个 `b`，`p ⇓ b ⇔ q ⇓ b`；
- `bind` 与 `race` 逐子句采用 R041 §1 的定义（`bind` 额外加一个 δ；`race` 同步公平轮询、左方平局优先）；
- `deadline k`（超时/截止期观察）采用 R041 §6 的有限形式：k 回合内返回 `some a`，否则 `none`。

## 冻结命题

- `C-71`：若 `p ≈ p'` 且 `f`、`g` 逐点结果等价，则 `bind p f ≈ bind p' g`（正例，R041 §2）。
- `C-72`：对固定 continuation `f`，`bind` 下降到 Cubical 集合商 `Delay A / ≈`，得到 `bindQ : Q A → Q B`，且在代表层按 `refl` 满足 β（R041 §2.1 的固定 f 版本）。
- `C-73`：`p0 = now true`、`p2 = δδ now true`、`q1 = δ now false` 满足 `p0 ≈ p2`，但 `race p0 q1` 与 `race p2 q1` 不等价（显式有限见证，R041 §3）。
- `C-74`：业务 continuation `deliver(true) = now true`、`deliver(false) = ω` 使 `Composed p = bind(race(p, q1), deliver)` 在 `p0` 上返回、在 `p2` 上发散（R041 §4 的完成性差异）。
- `C-75`：`deadline 1 p0 = some true` 而 `deadline 1 p2 = none`（截止期 consumer 分离同一等价对，R041 §6）。
- `C-76`：不存在 `r : Q Bool → Q Bool → Q Bool` 使 `r [p] [q] ≡ [race p q]` 对所有 `p q` 成立（用 Cubical `HITs.SetQuotients.Properties.effective`，R041 §3 的商级不可能性）。

## 解释边界（判词）

本包的正反成对结论判为 `REPRESENTATION_BOUNDARY`：

- 正例：结果等价是真实等价关系，`bind` 尊重它并可下降到 Cubical 集合商；
- 负例：`race` 与 `deadline` 读取被 `≈` 主动忽略的完成先后，因此不能下降为商上的函数；
- 这不是 HoTT 内部矛盾，也不是“HoTT 强迫错误替换”：HoTT 正确地把时序能力留在商之外。

自然 consumer 桥梁：在已核证据内（R039/R041 记录、Cubical 库提供的集合商理论、本文件固定接口），**没有**找到把结果商自然提升为含完成先后交付能力的实际 consumer。因此本方向停在 `REPRESENTATION_BOUNDARY`，不升级为 `NATURAL_USAGE_MISMATCH`；重开条件是在具体库/接口/模式中找到同一任务、自然承诺与真实失配。

## 不证明（非目标）

- 不证明 HoTT 内部不一致，不证明任何现实并发实现的失配；
- 不证明“所有 race 语义都不可下降”：本包只覆盖上述固定模型与固定 `race`/平局/截止期约定；
- 不证明 R041 的 25 项测试、源码或 `cf58f27` 增量容器谱系；
- 不认领原创性；R041 已给出纸笔原型。

## 证明身份

- proof ID：`MP-RACE-TIMEOUT-001`
- claim IDs：`C-71`–`C-76`
- final run：`20260912-MP-RACE-TIMEOUT-001-01`
- source：`PartialityRaceTimeout.agda`
- toolchain：`TOOLCHAIN.json` + `AGDA_LIBRARIES`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件；运行原件、外部依赖哈希与命令见 `../../verification/runs/20260912-MP-RACE-TIMEOUT-001-01/`。当前未获 Git commit/tag 授权，因此不能称 `MACHINE_PROVED_VERSION_CLOSED`。
