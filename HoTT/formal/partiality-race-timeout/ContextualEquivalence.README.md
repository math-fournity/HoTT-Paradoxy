# MP-CONTEXTUAL-EQUIV-001：结果商之上的上下文等价层次

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY`

本包是 `MP-RACE-TIMEOUT-001` 的直接续作：R041 delay 片段上，“结果等价”商去掉的完成先后，是否还能被完整操作族当作可替换依据？答案被机器化为一个层次定理——上下文等价严格细于结果等价。

## 固定构造

- 上下文族 `Ctx`：`hole`（空上下文）、`cbind C f`（顺序延续）、`crace₁ C q` 与 `crace₂ q C`（左/右参与同步公平 race）；`plug C d` 把计算装回上下文；
- 上下文等价：`p ≡c q` = “每个上下文把 p、q 送到结果等价的计算” 且 “每个上下文加每个 deadline k 都无法区分”；
- 观察族：结果观察（空上下文上的 `≈`）与 R041 §6 的 `deadline k`。

## 冻结命题

- `C-77`：`≡c` 是等价关系（自反、对称、传递）。
- `C-78`：`≡c` 精化结果等价：`p ≡c q → p ≈ q`。
- `C-79`：`¬ (ret (suc n) a ≡c ret zero a)`——deadline 0 区分“至少晚一步返回”与“立即返回”。
- `C-80`：`¬ (ret n a ≡c ω)`——与 ω 竞争的上下文区分“返回”与“发散”。
- `C-81`：`a ≠ b → ¬ (ret n a ≡c ret n b)`——延续 `x ↦ ret 0 (not x)` 把值差异放大为结果差异。
- `C-82`：`lt n m ≡ true → ¬ (ret n a ≡c ret m a)`——时间对齐的 race 上下文区分严格更晚的返回。
- `C-83`：`(p0 ≈ p2) × ¬ (p0 ≡c p2)`——结果等价严格粗于上下文等价。

## 解释边界（判词）

判词仍是 `REPRESENTATION_BOUNDARY`，但比上一包更强：不是“某个 race 选择子不存在”，而是**完整固定上下文族所尊重的最粗等价必须保留时序**。任何把 `p0` 与 `p2` 视为可互换的替换原则，只要语言含 race 或 deadline 观察，就与上下文等价冲突。

这仍然不是 HoTT 内部矛盾：HoTT 正确地区分了结果商与上下文等价；理论没有义务把竞争能力放进结果商，也没有从商上伪造它。

## 不证明（非目标）

- 不证明全部可能上下文语言/全部 race 政策下的最粗等价刻画（只覆盖本文件固定的 `Ctx` 与 deadline 观察）；
- 不证明一般商单子 `Q(A)×(A→Q(B))→Q(B)`（列为下一工作包）；
- 不证明现实并发系统失配、HoTT 内部矛盾或原创性。

## 证明身份

- proof ID：`MP-CONTEXTUAL-EQUIV-001`
- claim IDs：`C-77`–`C-83`
- final run：`20260912-MP-CONTEXTUAL-EQUIV-001-01`
- source：`ContextualEquivalence.agda`（依赖同目录 `PartialityRaceTimeout.agda`）
- toolchain：同目录 `TOOLCHAIN.json` + `AGDA_LIBRARIES`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件。运行原件与哈希见 `../../verification/runs/20260912-MP-CONTEXTUAL-EQUIV-001-01/`。当前未获 Git commit/tag 授权，不能称 `MACHINE_PROVED_VERSION_CLOSED`。
