# MP-RACE-TIMEOUT-001 机器证明实施证据（2026-09-12）

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY`。

本文件记录 `DIR-W-RACE-TIMEOUT` 第一工作包的实现、被核验的精确命题、失败与边界。它只描述本目录实际产生的源码、运行原件与索引，不重述或替代数学正文。

## 1. 触发与依据

- 触发：`方向追踪.md` §6 第 4 项与 FRONTIER 第一工作包；上一轮（S031/S032）判定命题截断为 `DEFENSE_WORKS` 后，把第一工作包转到 partiality quotient × race/timeout。
- 纸笔依据：`与Web GPT 交流用的文件夹/PROOF_NOTE(20260912-061537) - R401.md`（R041）§1–§4、§6。R041 是 `PAPER_ONLY`；本轮把其核心操作闭包在原生 Cubical Agda 中重做并机器核实。
- 工具链：`HoTT/formal/partiality-race-timeout/TOOLCHAIN.json` 复用已资格化的 Agda 2.8.0 + Cubical v0.9（官方 release digest、extracted binary、1111-file source tree hash 均在运行收据中重新核验）。

## 2. 本轮构造

- 对象语言：`Delay A` = `ω | ret n a`，即 R041 明示的单次返回族 `δ^n now(a)` 与 `ω` 的忠实表示；
- 等价：`p ≈ q` 即 R041 §1 的收敛行为等价（对每个 `b`，`p ⇓ b ⇔ q ⇓ b`）；
- 操作：`bind`、`race`（同步公平轮询、左方平局优先）逐子句采用 R041 §1；`deadline k` 为 R041 §6 截止期观察的有限形式；
- 商：`Q A = Delay A / ≈` 使用 Cubical `HITs.SetQuotients`，并用其 `effective` 引理把商相等反推为代表等价。

## 3. 被机器核验的 claim

| claim | 精确内容 | 关键定义 |
|---|---|---|
| `C-71` | `p ≈ p'` 且 `f`、`g` 逐点结果等价 ⇒ `bind p f ≈ bind p' g` | `bind-cong` |
| `C-72` | 固定 `f` 时 `bind` 下降到集合商，且代表层 β 按 `refl` 成立 | `bind-descends`、`bindQ`、`bindQ-β` |
| `C-73` | `p0 = now true`、`p2 = δδ now true`、`q1 = δ now false`：`p0 ≈ p2` 但两 race 结果不等价 | `race-noncongruent` |
| `C-74` | `deliver(true)=now true`、`deliver(false)=ω` 时 `Composed p0` 返回而 `Composed p2` 发散 | `completion-gap` |
| `C-75` | `deadline 1 p0 = some true` 而 `deadline 1 p2 = none` | `deadline-separation` |
| `C-76` | 不存在 `r : Q Bool → Q Bool → Q Bool` 使 `r [p] [q] ≡ [race p q]` 对所有输入成立 | `no-quotient-race`（经 `effective`） |

## 4. 运行与核验

- final run：`HoTT/verification/runs/20260912-MP-RACE-TIMEOUT-001-01/`（`RUN.json`、stdout/stderr、environment、source-manifest、index-row-manifest）；
- 命令：Agda 2.8.0 `--ignore-interfaces --library-file=…/AGDA_LIBRARIES -l cubical-0.9`，XDG/TMP 全部指向 D 盘缓存；exit 0，stderr 0 字节；
- 独立重放 `verify_formal_proof_run.py --rerun`：

```text
kernel_status=KERNEL_ACCEPTED_WITH_SCOPE
index_status=INDEXED_IN_CLAIM_EVIDENCE_MATRIX
index_validation=EXACT_INDEX_SNAPSHOT_MATCH
replay=EXACT_EXIT_STDOUT_STDERR_MATCH
```

- 索引：`HoTT/CLAIM_EVIDENCE_MATRIX.md` 新增 proof 行与 `C-71`–`C-76` 六行；`index-row-manifest.json` 冻结 proof 行与六个 claim 行的逐行哈希。

## 5. 失败与修订谱系

源码在本轮从零写出，经编译迭代后通过；失败均保留在对话/命令历史，不伪装成数学拒绝。主要类别：

1. generalizable variable 在定义体中的层级歧义（`GeneralizeNotSupportedHere`、`UnequalSorts`）→ 改为显式量化；
2. `_race_` 与 `_≈_` 同级导致解析歧义 → 显式 fixity；
3. `⊥`（`Type₀`）与 `⊥*`（`Lift ⊥`）在层级多态上下文混用 → 引入 `exFalso`/`rec*`、`lower` 并保持 `¬` 在 `Type₀`；
4. 集合商元素表达式的关系参数未定（unsolved metas）→ 增加 `_≋_` 类型别名固定 `Q A` 上的等式；
5. `bind-cong` 返回/返回分支缺少回程 ⇔ 组合 → 补 `⇔-sym (bind-conv-ret …)`。

上述修订只改变证明写法与类型标注；固定命题本身未削弱。

## 6. 判词与边界

判词：`REPRESENTATION_BOUNDARY`。

- 正例：结果等价是真实等价关系；`bind` 尊重它并在固定 continuation 下下降到 Cubical 集合商；
- 负例：`race` 与 `deadline` 读取 `≈` 主动忽略的完成先后，因此不能下降为商上的函数；`C-76` 给出商级不可能性；
- 这是理论对“时序能力”的表示边界，不是 HoTT 内部矛盾；`C-74` 的完成/发散反差是模型内过程反差，不是现实并发系统失配。

自然 consumer 桥梁：本轮在已核证据内没有找到把结果商自然提升为含完成先后交付能力的实际 HoTT consumer，因此不升级为 `NATURAL_USAGE_MISMATCH`，也不启动 ERCF-3。重开条件：在具体库/接口/模式中固定同一任务、自然承诺与真实失配。

## 7. Git 与版本状态

证明源码、工具链 manifest、运行原件、索引与治理更新均为本地未提交状态（无 commit/tag/push 授权），不能称 `MACHINE_PROVED_VERSION_CLOSED`。Cubical Agda 的 `.agdai` 接口文件可再生且被 `.gitignore` 忽略，不进入来源身份。
