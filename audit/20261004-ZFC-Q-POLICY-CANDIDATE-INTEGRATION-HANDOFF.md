# ZFC Q／P／A／B 形式化候选：canonical `dev` 集成交接

> **身份：** `CANDIDATE_NOT_CURRENT / INTEGRATION_REQUIRED / NO_CANONICAL_OWNER_MUTATION_IN_THIS_WORKTREE`。
>
> **本候选内容范围：** `35448f86^..5e04698c`（包括最初 C-359 包、C-360 至 C-365、来源范围审计和形式化收尾矩阵），branch `codex/zfc-q-policy-formalization`，共同基线 `e10771d96940f43ebfb7747898bb1ce6ecb29b17`。本交接单自身的后续更新不倒灌进这组 content commits；集成前仍须重新读取 branch tip。
>
> **最近观察的 canonical target：** `refs/heads/dev = 213a616a653ca964127a710497f231a0a3d3fef9`；它是本次读取时的事实，不是可直接写入目标。

## 1. 本候选交付什么

| 项 | 本候选的可复核结果 |
|---|---|
| `C-359` | Lean 4 core 的条件性政策核：强 P、形式 `PolicyScopeWitness`、B 同时成立时导出 `False`；`TaskEquiv` 型 `SameActualQ` 是充分的反类比控制；Q gap 不自动推出 P；metadata equality 不推出 task equivalence；use-model 不自动推出 B。 |
| `C-362` | Lean 4 core 的成员语言边界：同一 membership model 可以有相反的外加 `originDone` 扩张；显式 `CompletionBridge` 是阻断这种异判的正控制。 |
| `C-363` | Lean 4 core 的统一政策条件定理：同一完整 QProfile 的原任务已解决／bridge-required 异判破坏 `QUniform`；O3–O5 无 bridge 控制与 payment-difference 反控制一并保存。 |
| `C-364` | Lean 4 core 的未付 P 反模型：有 formal completion witness 的 base/subtheory interface 有一份同公开字段、origin completion 为假的 expansion；显式 bridge 与 adequacy 是 P 的正控制。 |
| `C-365` | Lean 4 core 的成员语言不变性：最小 `=`／`∈` 一阶公式和同语言 theory 在相同 membership 的外加 Done expansion 中不变；这给 C-362/C-364 的语言边界以归纳语义证明。 |
| `C-360` | Cubical Agda 原生控制：固定截断 Q 的 stage-one completion 不反射为原 universe Q 的有限 halt；负控制在 `nothing != just 1` 处被拒绝。 |
| `C-361` | Lean/Mathlib 实分析控制：(1-2^{-n}) 的形式极限不推出任何有限自然数阶段到达 endpoint；闭连续时间 endpoint 正控制同时成立，经典依赖明示。 |
| 来源与范围 | IEP/SEP/Norton 的 Zeno-side local completion policy、跨 kernel 映射、HoTT 动机文献 B0–B2 回流，以及明确的 actual-Q/cross-case-scope 未支付项；总判词见 [收敛 closure](20261004-ZFC-ACTUAL-Q-RESEARCH-CLOSURE.md)，七项 theorem 与 controls 的交叉核验见[形式化收尾矩阵](20261004-ZFC-FORMAL-CLOSURE-MATRIX.md)。 |
| 收据基础设施 | capture 工具改为由 `git rev-parse --show-toplevel` 接受 linked worktree，并可 pin Lean binary。 |
| 用户原文 | 2026-10-04 一手原文已保存；generation-14 curation 已做 63-KC、62/62 transition 的只读预演，尚未直接覆盖 current core。 |

本候选中 C-359/C-360/C-361/C-362/C-363/C-364/C-365 的 selected version closure 已在内容 tip `5e04698c` 复核通过；canonical integrator 仍须在接收后的 target snapshot 重跑：

```text
python3 -B scripts/audit/verify_proof_version_closure.py \
  --proof-id MP-ZFC-ACTUAL-Q-POLICY-002 \
  --proof-id MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001 \
  --proof-id MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001 \
  --proof-id MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001 \
  --proof-id MP-ZFC-COMPLETION-POLICY-UNIFORMITY-001 \
  --proof-id MP-ZFC-UNPAID-COMPLETION-PROMOTION-001 \
  --proof-id MP-ZFC-MEMBERSHIP-LANGUAGE-INVARIANCE-001
```

## 2. canonical `dev` 中发现的互补候选

在交接时，`/Volumes/D/HoTT_AI_HANDOFF_20260911` 的 `dev` 是 dirty，且有另一组未提交的同主题实物。它包含：

```text
HoTT/formal/zfc-actual-q-policy/ZenoLimitControl.lean
MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001 / C-361
```

该 source 固定几何数列 (s_n=1-2^{-n})，证明其收敛到 1 而没有有限自然数阶段到达 1，并给出闭连续时间 endpoint 正控制。本 worktree 已对该 exact source 作只读 Lean 重放：exit `0`；`#print axioms` 明示 `propext`、`Classical.choice`、`Quot.sound`。随后本候选用独立 source-manifest 与可重放 `LEAN_PATH` command 将 C-361 纳入自身；canonical `dev` 中保留的同名未提交版本仍须与本 branch 的 C-361 primary receipt 作内容比对，不可双重登记。

它的 C-359 用 `SameFullQ := fingerprint equality` 运输政策。当前候选的 `Bool`／`Unit` 反控制已经证明这不足以代表“同一个实际 Q”。两套工作应当组合，而不是二选一：保留 C-361 的实分析控制，采用 `TaskEquiv` 作为严格反类比控制，并将实际跨领域的政策运输明确留给由 source card 资格化的 `PolicyScopeWitness`。

## 3. 不可直接 cherry-pick 的原因

1. canonical `dev` 有大量未提交 current-owner、registry、matrix、run 和 session 变化；不能 reset、stash、clean、直接 merge 或整块 `ours/theirs`。
2. 两边都占用 `C-359`、`C-360` 和同一 `zfc-actual-q-policy/` 路径，直接 cherry-pick 会把两个不同的 Same-Q 语义并列成冲突的 current claim。
3. current core 的 STATE/HEAD 已有未提交 generation-13 checkpoint；generation-14 只能在冻结的 canonical snapshot 上原子应用。

## 4. canonical integrator 的推荐顺序

1. 冻结 `dev` target OID、index、dirty 所有权与 current `STATE/HEAD`；不触碰无关路径。
2. 逐文件比较本 commit 的 C-359 与 dev 的 C-359，保留本候选的 `TaskEquiv` 严格控制、`PolicyScopeWitness`、metadata counterexample、B non-forcing control；删除／归档旧 metadata-only transport，避免双真值。
3. 比对 dev 与本候选的 `ZenoLimitControl.lean`；以单一 source hash、C-361 primary receipt、matrix/registry row 为准，把严格 finite-stage control保留为独立 C-361，而不归因给 Standard Solution。
4. 用唯一 matrix／registry entries 连接 final C-359、C-360、C-361、C-362、C-363、C-364、C-365；重新跑 selected proof closure 和每个 final receipt 的 exact replay。
5. 按 [CORE-INGESTION](../HoTT/formal/zfc-actual-q-policy/CORE-INGESTION.md) 在 canonical current STATE 上应用 core generation-14，不从本候选 worktree 拷贝 dirty STATE/HEAD。
6. 将 source card、C-359/360/361/362/363 与实际强 P、`PolicyScopeWitness`、严格 `TaskEquiv`／跨 kernel B／QProfile 的开放义务写回 canonical current owners；不能把 formal controls升级为 bare-ZFC 结论。

## 5. 保持开放的实际问题

集成完成后仍不能说“ZFC 已证明矛盾”。最需要来源和任务证据支付的是：

```text
actual Zeno/circle State/input/step/observe/originDone
actual source-owned cross-case strong P（Zeno-side local policy 已有来源）
A ↔ admitted P
 actual source-qualified PolicyScopeWitness
actual Zeno–HoTT TaskEquiv（严格路径，不是唯一的实际来源路径）
跨 kernel B 映射
实际原过程 Done 的 membership-defined bridge（C-362 只证明未定义时的边界）
实际 Zeno／圆环／HoTT 的完整 QProfile 与相反来源 judgment（C-363 只证明条件性政策后果）
实际 base/subtheory model 与 source-defined bridge（C-364 只证明未付 P 的反模型）
完整 ZFC axiom schema 到 C-365 成员语言语义的保真编码（C-365 只固定 language fragment）
```

任一项被来源明确拒绝、替换或付款，都会让 `C-359` 的条件 theorem 不能用于实际 ZFC 判词；这是预期的可证伪结果。
