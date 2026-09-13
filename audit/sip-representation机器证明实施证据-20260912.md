# MP-SIP-REPRESENTATION-001 实施证据：SIP/UA 替换许可的最小边界

> 文档身份：F-011 implementation evidence
> 日期：2026-09-12
> proof ID：`MP-SIP-REPRESENTATION-001`；claim IDs：`C-124`–`C-128`
> final run：`HoTT/verification/runs/20260912-MP-SIP-REPRESENTATION-001-01/`
> 状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`

## 0. 本轮目标

STATE revision 49 把第一工作包固定为 **N8：SIP/表示消费者机器构造**。目标：固定带签名的结构类型，构造签名内同构、签名外可观察量不同的最小实例；用 SIP/UA 得到识别；机器证明签名外观察量不可统一恢复；给出把观察量加入签名后的细化正控制。预期最多 `REPRESENTATION_BOUNDARY`。

## 1. 形式化内容

源文件：`HoTT/formal/sip-representation/SIPRepresentation.agda`（`--safe --cubical --guardedness`）。

- 签名：点结构 `Str = Σ[ X ∈ Type₀ ] X`；
- `s = (Bool , true)`、`t = (Bool , false)`；
- 识别：`C-124-identification : s ≡ t`，由 `ΣPathP (ua notEquiv , toPathP (uaβ notEquiv true))` 构造；这是点结构的 SIP 实例，关键步骤使用 `ua`/`uaβ`；
- 签名外可观察量：`s`、`t` 的裸点分量（`true`、`false`）。它不是 `Str → Bool` 的全函数，因为 carrier 是抽象的；使用它需要额外“carrier 是 Bool”的表示数据；
- 细化结构 `Str' = Σ[ X ∈ Type₀ ] Σ[ x ∈ X ] Bool`，投影 `obs'`。

五条 claim：`C-124` 识别与 `uaβ` 计算；`C-125` 签名外观察量不同；`C-126` 任意 `f : Str → Bool` 在 `s,t` 上相等；`C-127` 不存在统一恢复函数；`C-128` 细化结构恢复/区分（正控制）。

## 2. 实现选择与失败谱系

1. **NotInScope `⊥`**：补充 `Cubical.Data.Empty` 导入。
2. **设计修正：签名外观察量不是 `Str → Bool`**：初版尝试 `obs (X , x) = x`，但 `x : X` 对抽象 carrier 不是 Bool；正确形式是把 observable 记为 `s`/`t` 上的值（`true`/`false`），并明确它需要额外“carrier 是 Bool”表示数据。此修正是对命题的忠实修正，不是削弱：`C-127` 的不存在性仍然量化真正可能被使用的统一函数 `Str → Bool`。
3. **UnequalSorts**：`Str : Type₁`，Σ 也在 `Type₁`；把 `¬_` 改为宇宙多态 `∀ {ℓ} → Type ℓ → Type ℓ`。

最终命令（由 `capture_agda_proof_run.py` 复现）：

```text
agda --ignore-interfaces --library-file=HoTT/formal/sip-representation/AGDA_LIBRARIES \
     -l cubical-0.9 -i HoTT/formal/sip-representation \
     HoTT/formal/sip-representation/SIPRepresentation.agda
```

final run：exit 0、stdout 9,800 bytes、stderr 0 bytes、零 warning。

## 3. Run/索引证据

- `RUN.json`：`KERNEL_ACCEPTED_WITH_SCOPE`、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`、exit 0；
- `source-manifest.json`：`SIPRepresentation.agda` + `TOOLCHAIN.json` + `AGDA_LIBRARIES` 哈希；
- `index-row-manifest.json`：proof row + 5 claim rows 冻结（6 行）；
- `verify_formal_proof_run.py --rerun`：

```text
kernel_status=KERNEL_ACCEPTED_WITH_SCOPE
index_status=INDEXED_IN_CLAIM_EVIDENCE_MATRIX
index_validation=EXACT_INDEX_SNAPSHOT_MATCH
replay=EXACT_EXIT_STDOUT_STDERR_MATCH
```

工具链身份与既有 `MP-*` 包相同：Agda 2.8.0-3d04bac、官方 release SHA-256、Cubical v0.9（tag commit `b150186d…`、tree SHA-256 `73ccfbaf…`）。

## 4. 旧包在矩阵增长后的重验

矩阵追加 C-124–C-128 后，十二个既有 package 全部重放：

```text
ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH
```

详见本轮 Session 的 `RUNS.json` 与 `POST-CHECKPOINT.json`；旧 proof/claim 行未被改写。

## 5. 判词与边界

- 判词：`SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`（第二级；不是 HoTT 悖论）；
- SIP/UA 只承诺结构签名内的替换；签名外的表示/标签/来源/成本观察量不会被该识别保留，也不能从结构类型统一恢复；
- 消费者需要该观察量时必须把它加入签名（`C-128` 正控制）或保留具体表示；
- 与 `MP-COST-FACTORIZATION-001` 的关系：后者用 funext 处理裸函数/成本；本包用 SIP/UA 处理结构识别；关键规则不同；
- 不调用完整 SIP 模块；本包是点结构上手写的 SIP 实例；
- 不证明任何真实库/系统把 SIP 等价当作完整替换许可，不主张原创性。

## 6. 证据锚点

- `HoTT/formal/sip-representation/SIPRepresentation.agda`；
- `HoTT/formal/sip-representation/README.md`、`TOOLCHAIN.json`、`AGDA_LIBRARIES`；
- `HoTT/verification/runs/20260912-MP-SIP-REPRESENTATION-001-01/`；
- `HoTT/CLAIM_EVIDENCE_MATRIX.md`（`MP-SIP-REPRESENTATION-001` 行与 C-124–C-128）；
- `理解章节/C7-post-N6距离综合与剩余域选择-20260912.md`（N8 选择）；
- `audit/derived-development-consumer审计-20260912.md`（N5 未找到 SIP consumer）。
