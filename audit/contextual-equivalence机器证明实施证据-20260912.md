# MP-CONTEXTUAL-EQUIV-001 机器证明实施证据（2026-09-12）

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY`。

本文件记录 `MP-RACE-TIMEOUT-001` 续作（contextual equivalence 层次）的构造、被核验命题与边界。

## 1. 触发与依据

- 触发：S034 后 `方向追踪.md` §6 第 4 项把第一工作包定为“操作族下的 contextual equivalence 层次”。
- 依据：R041 §1（delay/≈/bind/race 定义）、R041 §6（deadline 观察），以及 `MP-RACE-TIMEOUT-001` 已冻结的 `PartialityRaceTimeout` 模块（本包以 `open import` 复用其模型定义，不改写旧源码）。

## 2. 本轮构造

- 上下文族 `Ctx`：`hole`、`cbind C f`、`crace₁ C q`、`crace₂ q C`；`plug C d` 将计算装回上下文；
- 上下文等价 `p ≡c q`：全部上下文保持 `≈` 且全部“上下文 + deadline k”观察不可区分；
- 分离工具：`deadline 0`（立即 vs 延迟）、与 `ω` 的 race（返回 vs 发散）、`bind` 配合值移动延续 `x ↦ ret 0 (not x)`（同刻不同值）、时间对齐 race 配合 `leb-refl`/`lt-leb`（严格更晚返回）。

## 3. 被机器核验的 claim

| claim | 精确内容 | 关键定义 |
|---|---|---|
| `C-77` | `≡c` 是等价关系（自反/对称/传递） | `≡c-refl`、`≡c-sym`、`≡c-trans` |
| `C-78` | `p ≡c q → p ≈ q`（空上下文） | `≡c-to-≈` |
| `C-79` | `¬ (ret (suc n) a ≡c ret zero a)` | `deadline-zero-separates` |
| `C-80` | `¬ (ret n a ≡c ω)` | `divergence-separates` |
| `C-81` | `a ≠ b → ¬ (ret n a ≡c ret n b)` | `value-separates` |
| `C-82` | `lt n m ≡ true → ¬ (ret n a ≡c ret m a)` | `lt-timing-separates`、`leb-refl`、`lt-leb` |
| `C-83` | `(p0 ≈ p2) × ¬ (p0 ≡c p2)` | `result-coarser-than-contextual` |

## 4. 运行与核验

- final run：`HoTT/verification/runs/20260912-MP-CONTEXTUAL-EQUIV-001-01/`（RUN.json、stdout/stderr、environment、source-manifest、index-row-manifest）；
- 命令复用同一 Agda 2.8.0 + Cubical v0.9 工具链（官方 release/tree hash 再次核验）；exit 0，stderr 0 字节；
- 独立重放：

```text
kernel_status=KERNEL_ACCEPTED_WITH_SCOPE
index_status=INDEXED_IN_CLAIM_EVIDENCE_MATRIX
index_validation=EXACT_INDEX_SNAPSHOT_MATCH
replay=EXACT_EXIT_STDOUT_STDERR_MATCH
```

- 矩阵追加后重放三个旧包（Lean、truncation、race/timeout），全部 `ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH`。

## 5. 失败与修订谱系

本包源码一次编译通过前的两处机械修正：`×` 需显式导入 `Cubical.Data.Sigma.Base`；其余按上一包学到的显式量化/固定 fixity 风格书写。没有为求绿削弱命题。

## 6. 判词与边界

判词：`REPRESENTATION_BOUNDARY`（强化版）。

- 强于上一包：不是"某个 race 选择子不存在"，而是**完整固定上下文族（bind/双侧 race + deadline 观察）所尊重的最粗等价严格保留时序**；
- 仍不是 HoTT 内部矛盾：理论正确区分结果商与上下文等价，没有从商上伪造竞争能力。

未证明：全部可能上下文语言/全部 race 政策下的最粗等价刻画、一般商单子 `Q(A)×(A→Q(B))→Q(B)`（下一工作包）、现实并发失配与原创性。

## 7. Git 与版本状态

源码、运行原件与索引均为本地未提交状态（无 commit/tag/push 授权），不能称 `MACHINE_PROVED_VERSION_CLOSED`。
