# GZ-001：G0-R3 Coq 资格化与 Foundation 后继

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G0-R3`。
>
> **状态：** `EVIDENCE_RECORDED / COQ_CURRENT_RERUN_EXTERNALLY_BLOCKED / FOUNDATION_SUCCESSOR_ACTIVE`。
>
> **工作树：** `/Users/aurolafly/.codex/worktrees/godel-zfc-r3-replay/HoTT_AI_HANDOFF_20260911`，起始 HEAD `dcf12f4b`，该 worktree 在此单位开始时 clean。

## 1. Parent gap

`G0-R3` 需要一个版本固定、可重放的形式系统不完备性基准。它必须显示可编码的语法／证明或形式系统、有效验证或可枚举性、替换／自应用所依赖的计算结构，以及精确的独立性 theorem；它不能以“出现了自指”或一次 proof-search timeout 代替这些内容。

历史资产 `MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001` 曾在 Coq 中完成这一角色，但当前总路线不能仅根据旧报告把它称为已在当前分支版本闭合。因此本单位先资格化 archive、run receipt、current verifier 和 Git closure，再决定是否需要新的 replay。

## 2. 冻结 target

| 字段 | 值 |
|---|---|
| 上游理论／实现 | `uds-psl/coq-synthetic-incompleteness@cd7d8490f8542bfe85658c465bcb26b2ed163f53`，branch `csl` |
| 对象层 | first-order arithmetic / Robinson `Q` 的 enumerable consistent theories |
| 元层 | Coq 8.15.2 kernel checking `FOL/Incompleteness/fol_incompleteness.vo` |
| 现有 proof ID | `MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001`，claims `C-244`–`C-249` |
| 历史 run | `HoTT/verification/runs/20260915-MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001-01` |
| 完成判词 | `R3` 的技术基准已重放／重新资格化；它不等于 exact HoTT instance、`Accept_ZFC`、`OriginDone` 或 bare ZFC 归因。 |

## 3. 先于 Foundation 调查的自身构造与反证条件

### 候选构造

目标 theorem 至少应有如下形状：对明确语言中的、可枚举且一致、包含足够算术的理论 `T`，构造一个指定公式 `φ`，并证明 `T` 不证明 `φ` 且不证明其否定。其证明应经有效语法、proof relation、编码／可计算 predicate、substitution 或等价的递归不可分离机制发生，而不是把一个外部元层不可判定性口号直接赋给 HoTT 或 ZFC。

对于当前 Coq target，预期 `Q_incomplete` 会保留 `Peirce`、`CTQ`、`Qeq ⊑ T`、`enumerable T` 与 `~ T ⊢T ⊥` 前提；`insep_essential_incompleteness` 会保留 universality、extension 与 strong separation。恰当的 R3 结果是这些条件性 theorem 的 kernel acceptance。

### Falsifier

下列任一事实会拒绝此 target 作为当前 R3 基准：

1. repo-contained archive 或 manifest 当前不再匹配冻结 commit；
2. `Qualification.v` 不再加载并输出目标 constants／assumptions；
3. theorem type 缺少可核的 universality、formal-system 或独立性结构；
4. 当前版本闭包或实际 rerun 失败，且无法定位为工具链外部状态；
5. 将 first-order `Q` 的 theorem 偷换为 exact HoTT 或 bare ZFC 的 theorem。

### Controls

- **正控制：** archive validation 与 `verify_formal_proof_run` 应复核现有 run 的 source hashes、receipt、claim rows 与 scope；
- **版本闭包控制：** `verify_proof_version_closure` 必须能发现 command/source manifest 不一致，而不能因旧 run exit 0 静默放行；
- **不同任务控制：** R3 的 `FormalDone` 是 Coq kernel 接受固定 theorem build；不存在到芝诺／圆环／H0 `OriginDone` 的 bridge，故本单位不声称现实过程完成。

## 4. 实际资格化结果

### 4.1 已支付

1. `python3 -B scripts/audit/import_coq_synthetic_incompleteness.py validate` 返回 `VALID`：archive 为 2,019,830 bytes / SHA-256 `5ffbeb…c7c8a`，包含 807 tracked files / 7,423,361 bytes / tree SHA `d9dd…80ca`；
2. `python3 -B scripts/audit/verify_formal_proof_run.py --project-root . --run-dir HoTT/verification/runs/20260915-MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001-01` 返回 `PASS_WITH_SCOPE`，保留 `C-244`–`C-249`、`KERNEL_ACCEPTED_WITH_SCOPE` 和显式非目标；
3. 当前 verifier 将自身字节差异列为 `audit_tool_provenance_drift`，而没有误报为 theorem source drift；
4. `Qualification.v`、`CLAIM-R3-SYNTHETIC-INCOMPLETENESS.md` 与历史 report 均保留 exact theorem signatures：`self_halting_diverge`、`recursively_separating_diverge`、`insep_essential_incompleteness`、`epf_mu_ctq` 与 `Q_incomplete`。

### 4.2 未支付／阻塞

1. `verify_proof_version_closure.py --proof-id MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001` 与 `--evidence-only` 均返回 `BLOCKED / LATER_COMMAND_SOURCE_MISMATCH`。原因是该 historical `RUN.json.command_argv` 启动的是 replay wrapper，而通用 later-package contract 当前要求 command argv 直接含一个 source path；这是一项版本化证据合同不匹配，不能被旧 run 的 exit 0 覆盖。
2. 实际 `--rerun` 需要 Docker image `hott-coq-synthetic-incompleteness:cd7d849`。当前 `docker image inspect` 与 `docker info` 均因 Unix socket `/Users/aurolafly/.orbstack/run/docker.sock` 不存在而失败；因此没有重跑 build，也没有生成新的 Coq kernel receipt。

## 5. 判词

```text
COQ_R3_SOURCE_AND_HISTORICAL_KERNEL_RECEIPT_VALID_WITH_SCOPE
COQ_R3_CURRENT_GIT_VERSION_CLOSURE_BLOCKED_BY_COMMAND_CONTRACT_MISMATCH
COQ_R3_FRESH_KERNEL_RERUN_EXTERNALLY_BLOCKED_BY_DOCKER_DAEMON_UNAVAILABLE
NOT_A_HOTT_INSTANCE
NOT_A_ZFC_ACCEPTANCE_OR_COMPLETION_BRIDGE
```

这不是 `R3` 被否定，也不是 Coq theorem 失效。它仅表明：当前 route 不能把该历史 Coq receipt升级为此 worktree 的 fresh/version-closed R3 交付。

## 6. Required successor

`GZ-002 / G0-R3-FOUNDATION-001`：冻结 FormalizedFormalLogic/Foundation 的 exact commit，定位 Gödel First theorem 的 source module、theorem signature、toolchain和可重放 minimal import；以一个独立 Lean kernel 为 R3 differential target。它必须仍区分：

```text
first-order arithmetic incompleteness theorem
≠ exact HoTT calculus incompleteness
≠ bare ZFC Q precision verdict
```

若 Foundation target 也无法 current-run，须记录该 target 的 exact toolchain/source reason，再回到 Coq Docker external blocker 或第三个 candidate；不得重复本 Coq Docker probe。

## 7. Reopen conditions

- Docker daemon/匹配 image 变为可用，且 replay wrapper 可实际运行；
- version-closure contract 允许该 wrapper command 的可验证 source dependency，或为此 package建立新的 current receipt；
- 上游 source/archive/theorem signatures 改变；
- 出现 exact HoTT calculus 将 R3 theorem 参数实际实例化的证据。

## 8. GZ-002：Foundation 独立 R3 source calibration

### 固定 source 与自身构造

本后继固定 `FormalizedFormalLogic/Foundation@f3972f4204fc61e1b736ed843415894c83f35508` 与
`Foundation.FirstOrder.Incompleteness.First`。自己的预期是：该 source 必须不只声明一个 `Incomplete` 名字，
还必须在代码中呈现能审计的 RE predicate、code、quotation、substitution、provability 与对角句结构；
qualification 必须显示精确算术／soundness assumptions，而不是把它们当作 ambient truth。

反证条件是：冻结 root 的 commit/lock 文件不匹配；`lake build` 无法检查 `First` module；qualification 缺少
first-incompleteness declarations；或者省略 `T.SoundOnHierarchy 𝚺 1` 仍被接受。

### 实际结果

1. frozen root 的 HEAD、`lakefile.toml`、`lake-manifest.json`、`lean-toolchain` 与此前 Foundation Zermelo control 的 hash 均一致；
2. `lake build Foundation.FirstOrder.Incompleteness.First` exit 0，报告 1,242 jobs 完成；
3. `Qualification.lean` exit 0，打印 `incomplete`、`incomplete_of_RE`、两个 true-but-unprovable declarations；四项均列出 `propext`、`Classical.choice`、`Quot.sound`；
4. `WrongMissingSoundness.lean` exit 1，准确拒绝缺少 `T.SoundOnHierarchy 𝚺 1`；
5. 初次 capture `-01` 因 build 输出被错误混入 qualification stdout 而不能精确 rerun，`-02` 又因未登记的 external-tree label 而被 verifier 拒绝；两者均保留在 package `REVISIONS.md`。最终 primary/negative `-03` 同时分离 build evidence 与 command-output evidence，并使用已资格化的同一 Foundation source-tree label。

### G0 判词与后继

```text
R3_FOUNDATION_FIRST_INCOMPLETENESS_SOURCE_CALIBRATION_MACHINE_PROVED_WITH_SCOPE
R3_GENERAL_FIRST_ORDER_ARITHMETIC_ONLY
R4_HOTT_CALCULUS_BRIDGE_REQUIRED
```

G0 已经有一个当前可构建、可检查的独立 Lean source calibration。它与 Coq source 的外部 Docker blocker 不同，
因此不需要等待 Docker 才能进入下一 G1/R4 单位。下一动作是 `GZ-003 / R4-HOTT-CALCULUS-BRIDGE-001`：选择 exact HoTT calculus，逐项检查 H-SYNTAX 至 H-EFFECTIVITY，而不把 Foundation 的 `ArithmeticTheory` 误称为 HoTT。
