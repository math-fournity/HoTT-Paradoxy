# MP-SIP-REPRESENTATION-001：SIP/UA 作为替换许可的最小边界

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`

本包把 N7 选定的 SIP/表示消费者候选做成最小原生 Cubical 机器构造：**两个在签名内同构的点结构被 `ua` 识别，但签名外的可观察量在它们上不同；任何从结构类型出发的函数都被该识别强制为在这两点上相等。把可观察量加入签名后，识别不再成立，投影可以恢复/区分它（正控制）。**

## 固定构造

- 签名：点结构 `Str = Σ[ X ∈ Type₀ ] X`；
- `s = (Bool , true)`，`t = (Bool , false)`；
- 识别：`C-124-identification : s ≡ t`，由 `ΣPathP (ua notEquiv , toPathP (uaβ notEquiv true))` 构造——这是点结构上的 SIP 实例，关键步骤使用 `ua`/`uaβ`；
- 签名外可观察量：`s` 与 `t` 的裸点分量（`true` 与 `false`）；它不能成为 `Str → Bool` 的全函数，因为 carrier 是抽象的，必须带有“carrier 是 Bool”的额外表示数据；
- 细化结构：`Str' = Σ[ X ∈ Type₀ ] Σ[ x ∈ X ] Bool`，投影 `obs' (_ , _ , b) = b`。

## 冻结命题（`C-124`–`C-128`）

| claim | 形式化结果 |
|---|---|
| `C-124` | `transport (ua notEquiv) true ≡ false`（`C-124-ua-transport`），且存在原生路径 `s ≡ t`（`C-124-identification`）。 |
| `C-125` | 签名外可观察量在两个结构上不同：`¬ (observable-s ≡ observable-t)`（`C-125-obs-differs`）。 |
| `C-126` | 任意 `f : Str → Bool` 都被识别强制为常数：`f s ≡ f t`（`C-126-any-function-constant`）。 |
| `C-127` | 不存在统一恢复函数 `f : Str → Bool` 同时满足 `f s ≡ true`、`f t ≡ false`（`C-127-no-recovery`）。 |
| `C-128` | 细化结构中可观察量进入签名：`C-128-obs'-differs` 给出投影区分，`C-128-no-identification` 证明 `¬ (s' ≡ t')`——正控制。 |

## 解释边界（判词）

判词：`SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`（第二级结构性结果）：

- SIP/UA 识别的是**签名内结构**；签名外的表示/标签/来源/成本观察量不会被该识别保留，也不能从结构类型统一恢复；
- 消费者若需要该观察量，必须把它加入签名（`C-128` 正控制）或保留具体表示；
- 这不是 HoTT 内部矛盾：理论正确地只承诺结构签名内的替换，并把“结构外观察量”留给更丰富的结构或具体表示；
- 与既有边界的关系：`MP-COST-FACTORIZATION-001` 用 funext 处理裸函数/成本；本包用 SIP/UA 处理结构识别；二者共享“忘掉维度后不可免费恢复”的一般形状，但关键规则不同。

## 不证明（非目标）

- 不调用完整 SIP 模块；本包手写点结构上的 SIP 实例（`ΣPathP` + `ua` + `uaβ`）；
- 不构造一般结构范畴的 SIP 定理；
- 不证明任何真实库/系统把 SIP 等价当作完整替换许可（N5 审计在固定集合内未找到此类 consumer）；
- 不主张原创性（SIP/UA 的替换语义是标准结果，本包是其最小机器实例与控制）。

## 证明身份

- proof ID：`MP-SIP-REPRESENTATION-001`
- claim IDs：`C-124`–`C-128`
- source：`SIPRepresentation.agda`
- toolchain：`TOOLCHAIN.json` + `AGDA_LIBRARIES`
- final run：`20260912-MP-SIP-REPRESENTATION-001-01`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件；运行原件、外部依赖哈希与命令在 `../../verification/runs/20260912-MP-SIP-REPRESENTATION-001-01/`。当前未获 Git commit/tag 授权，因此不能称 `MACHINE_PROVED_VERSION_CLOSED`。
