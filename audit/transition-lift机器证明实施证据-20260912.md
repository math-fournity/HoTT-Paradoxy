# MP-TRANSITION-LIFT-001 实施证据：R036/R038 核心边界的原生 Cubical 升级

> 文档身份：F-011 implementation evidence
> 日期：2026-09-12
> proof ID：`MP-TRANSITION-LIFT-001`；claim IDs：`C-110`–`C-117`
> final run：`HoTT/verification/runs/20260912-MP-TRANSITION-LIFT-001-01/`
> 状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`

## 0. 本轮目标

STATE revision 44 把第一工作包固定为 **N3：把 R036/R038 的过渡抽象/当前态提升边界升级到原生 Cubical Agda**。目标不是重述有限 Python 模型，而是：

1. 用原生 Cubical Path/HIT 语义（命题截断）形式化 R036 的有限商/提升反例；
2. 形式化 R038-D 的“截断与极限不可交换”核心；
3. 保留正向控制（原过程确实终止、真实前缀确实提升）；
4. 给出零 warning 的 final run、source/run/index 证据链；
5. 不升级为 HoTT 悖论：预期最多 `REPRESENTATION_BOUNDARY`。

## 1. 形式化内容

源文件：`HoTT/formal/transition-lift/TransitionLift.agda`（`--safe --cubical --guardedness`）。

### 1.1 R036 有限模型

- 状态 `S = {a,b,d}`，抽象 `Q = {w,W}`，`α a = α b = w`，`α d = W`；
- 转移用一个全函数 `step : S → Maybe S`（`a ↦ just b`，`b ↦ just d`，`d ↦ nothing`）定义，`R x y := step x ≡ just y`；
- 存在像 `E u v := ∥ Σ x y, α x ≡ u × R x y × α y ≡ v ∥₁`；
- 当前后继 `C s v := ∥ Σ t, R s t × α t ≡ v ∥₁`。

八条 claim 见 `HoTT/formal/transition-lift/README.md` 与 `HoTT/CLAIM_EVIDENCE_MATRIX.md`（C-110–C-117），包括：终止正控制、抽象自环与无限路径、无两步具体提升、无当前态提升函数、无严格下降纤维恒定等级、精确极限为空、截断极限有元素、比较映射无逆。

## 2. 实现选择与失败谱系

所有失败都按责任点修复，没有削弱命题：

1. **MissingDefinitions `_≤_` / NotInScope `¬`、`⊤`**：初版把库假设写错；改为本地定义 `¬_`，并显式导入 `Cubical.Data.Unit`/`Cubical.Data.Maybe`。
2. **AmbiguousName `rec`**：`Cubical.Data.Empty.rec` 与 `Cubical.HITs.PropositionalTruncation.rec` 冲突；重命名为 `PT-rec`。
3. **ClashingDefinition `just-inj`**：库已提供 `Cubical.Data.Maybe.Properties.just-inj`；删除本地重复定义并显式传 `(x y)`。
4. **UnequalTerms 于 `≤` 辅助引理**：把 `_≤_` 从索引归纳族改为按构造子递归的函数定义，避免 `UnsupportedIndexedMatch` 警告；零警告目标因此达成。
5. **UnsolvedConstraints 于 `j`**：`≤-drop-suc` 的隐式参数无法从被阻塞的项推断；显式写 `{k = k} {m = m}`。

最终命令（由 `capture_agda_proof_run.py` 复现）：

```text
agda --ignore-interfaces --library-file=HoTT/formal/transition-lift/AGDA_LIBRARIES \
     -l cubical-0.9 -i HoTT/formal/transition-lift \
     HoTT/formal/transition-lift/TransitionLift.agda
```

final run：exit 0、stdout 9,458 bytes、stderr 0 bytes、零 warning。

## 3. Run/索引证据

- `RUN.json`：`KERNEL_ACCEPTED_WITH_SCOPE`、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`、exit 0；
- `source-manifest.json`：源文件 + `TOOLCHAIN.json` + `AGDA_LIBRARIES` 哈希；
- `index-row-manifest.json`：proof row + 8 claim rows 冻结（9 行）；
- `verify_formal_proof_run.py --rerun`：

```text
kernel_status=KERNEL_ACCEPTED_WITH_SCOPE
index_status=INDEXED_IN_CLAIM_EVIDENCE_MATRIX
index_validation=EXACT_INDEX_SNAPSHOT_MATCH
replay=EXACT_EXIT_STDOUT_STDERR_MATCH
```

工具链身份与十个既有 `MP-*` 包相同：Agda 2.8.0-3d04bac、官方 release SHA-256、Cubical v0.9（tag commit `b150186d…`、tree SHA-256 `73ccfbaf…`）。

## 4. 旧包在矩阵增长后的重验

矩阵追加 C-110–C-117 后，十个既有 package 全部重放：

```text
ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH
```

详见本轮 Session 的 `RUNS.json` 与 `POST-CHECKPOINT.json`；旧 proof/claim 行未被改写。

## 5. 判词与边界

- 判词：`TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`（第二级；不是 HoTT 悖论）；
- `E` 是合法 may 过近似，抽象无限路径不等于具体发散；
- 反例是有限的：`w,w,w` 在抽象上有证据，但从 `a` 无相容两步提升；`C` 与 `E` 的差异被机器精确化；
- `C-114`–`C-116` 是 R038-D 的原生版本：精确极限为空、截断极限有元素、无逆；
- R038-A/B（Acc 命题性与迁移定理）**未**进入本包，仍是 paper 级；
- 不证明任何实际库/系统强制使用坏解释，不主张物理时间或原创性。

## 6. 证据锚点

- `HoTT/formal/transition-lift/TransitionLift.agda`；
- `HoTT/formal/transition-lift/README.md`、`TOOLCHAIN.json`、`AGDA_LIBRARIES`；
- `HoTT/verification/runs/20260912-MP-TRANSITION-LIFT-001-01/`；
- `HoTT/CLAIM_EVIDENCE_MATRIX.md`（`MP-TRANSITION-LIFT-001` 行与 C-110–C-117）；
- `workspace/.codex/research/hott/reviews/TRANSITION-ABSTRACTION-001/PROOF_NOTE.md`、`.../002/PROOF_NOTE.md`；
- `理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md`。
