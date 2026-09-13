# MP-PATH-CERTIFICATE-001 机器证明实施证据（2026-09-12）

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`。

本文件记录 R034 路径证书边界的原生核查：有实际路径时有迁移，只有等价存在（截断）时全宇宙统一迁移不存在。

## 1. 触发与依据

- 触发：S039 后 `方向追踪.md` §6 第 4 项（R034 path-certificate 原生核查）。
- 依据：用户提供的同 SHA 文件 `与Web GPT 交流用的文件夹/PROOF_NOTE(20260912-061551) - R034.md`（P3/P4）；R034 的 `MereMigration.agda` 当时是参数化草稿且未编译，本包用真实 Cubical Path/截断/univalence 完成核查。

## 2. 本轮构造

- `notEquiv : Bool ≃ Bool` 与 `loop := ua notEquiv`；
- `C := Σ[ Y ∈ Type ] ∥ Bool ≡ Y ∥₁`、基点 `z₀`；由 `isProp→PathP` 与 `ΣPathP` 构造回路 `loop-point`；
- 反证：统一接口 `m` 给出依赖截面 `s`；`ω i := s (loop-point i)` 与 `fromPathP` 给出沿回路的运输等式；`uaβ` 把它算成 `not (s z₀) ≡ s z₀`，与 Bool 无不动点矛盾。

## 3. 被机器核验的 claim

| claim | 精确内容 | 关键定义 |
|---|---|---|
| `C-100` | `transport (ua notEquiv) ≡ not` | `ua-move-computes`、`ua-move-is-not` |
| `C-101` | 截断命题性 + 栖居 | `H-is-prop`、`H-inhabited` |
| `C-102` | 固定端点弱接口存在 | `fixed-pair-interface` |
| `C-103` | 固定源统一变体不可栖居 | `no-fixed-source-mere-move` |
| `C-104` | `MereMove` 不可栖居 | `no-mere-move` |
| `C-105` | 路径版接口存在 | `path-move` |

## 4. 运行与核验

- final run：`HoTT/verification/runs/20260912-MP-PATH-CERTIFICATE-001-01/`；
- 同一 Agda 2.8.0 + Cubical v0.9 工具链；exit 0，stderr 0 字节；
- 独立重放：`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`；
- 矩阵第七次增长后重放八个旧包，全部 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。

## 5. 失败与修订谱系

本轮编译迭代修正：`H`/`C`/`MereMove` 的宇宙层级（等价类型的 identity 位于 Type₁）、最终等式的方向。命题未削弱。

## 6. 判词与边界

判词：`MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`。

- 正控制：固定端点接口（C-102）与路径版接口（C-105）均可构造；
- 负例：固定源统一变体与全宇宙 `MereMove` 不可栖居（C-103/C-104），反证构造性（无 LEM/选择/神谕）；
- 不是 HoTT 内部矛盾：标准 transport 输入实际路径，截断不自动提供 `MereMove`；
- 未实现 R032 证书语法回放，未处理 HoTT+选择关系，未主张原创性。

## 7. Git 与版本状态

源码、运行原件与索引均为本地未提交状态（无 commit/tag/push 授权），不能称 `MACHINE_PROVED_VERSION_CLOSED`。
