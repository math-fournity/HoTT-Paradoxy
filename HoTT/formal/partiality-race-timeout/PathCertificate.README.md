# MP-PATH-CERTIFICATE-001：R034 路径证书边界的原生核查

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`

本包用真实 Cubical Path / 命题截断 / univalence 原生核查 R034 的核心边界：**有实际路径时迁移存在；仅有等价存在（命题截断）时全宇宙的统一迁移不存在。** 这是 `DIR-W-PATH-CERTIFICATE` 自列为"以真实 Cubical Agda 完成原生核查"的直接执行（普通 Lean `Eq` 不参与）。

## 固定构造

- 取反等价 `notEquiv : Bool ≃ Bool` 与单价路径 `loop := ua notEquiv : Bool ≡ Bool`；
- 连通分量 `C := Σ[ Y ∈ Type ] ∥ Bool ≡ Y ∥₁`，基点 `z₀ := (Bool , ∣ refl ∣₁)`；
- 由 `isProp→PathP`（截断是命题）与 `ΣPathP` 构造回路 `loop-point : z₀ ≡ z₀`；
- 反证：假设统一接口 `m : (Y : Type) → ∥ Bool ≡ Y ∥₁ → Bool → Y`，令 `s (Y , h) := m Y h false`；对回路用依赖路径作用 `ω i := s (loop-point i)` 与 `fromPathP` 得 `transport loop (s (loop-point i0)) ≡ s (loop-point i1)`，再用 `uaβ` 得 `not (s z₀) ≡ s z₀`，与 Bool 无不动点矛盾。

## 冻结命题

- `C-100`：`transport (ua notEquiv) ≡ not`（单价路径按等价计算）。
- `C-101`：`∥ Bool ≡ Y ∥₁` 是命题，且 `∥ Bool ≡ Bool ∥₁` 有元素。
- `C-102`：固定端点弱接口 `∥ Bool ≡ Bool ∥₁ → Bool → Bool` 存在（恒等函数）。
- `C-103`：固定源统一变体 `(Y : Type) → ∥ Bool ≡ Y ∥₁ → Bool → Y` 不可栖居。
- `C-104`：全宇宙统一接口 `MereMove := (X Y : Type) → ∥ X ≡ Y ∥₁ → X → Y` 不可栖居（`C-103` 的推论）。
- `C-105`：路径版接口 `(X ≡ Y) → X → Y` 由 `transport` 构造（与 `C-104` 形成对照）。

## 解释边界（判词）

判词：`MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS`（判词阶梯第二级的结构性版本）：

- 被排除的是"删掉具体路径后仍能统一自然迁移"的接口；固定端点与路径版接口都可构造（正控制）；
- 反证是构造性的（无 LEM、选择、停机神谕）；它是函数类型非栖居，不是超时推测；
- 不是 HoTT 内部矛盾：标准 transport 的输入是实际路径，截断规则不自动提供 `MereMove`，理论没有批准这个接口。

## 不证明（非目标）

- 不实现 R032 有限证书系统的完整语法/回读，也不重放 R034 的 24 项 Python 测试；
- 不证明"HoT + 通常选择不一致"；不证明所有实例都无解；
- 不主张原创性（R034 已给出纸笔推导，本包是其原生核查 + 正控制）。

## 证明身份

- proof ID：`MP-PATH-CERTIFICATE-001`
- claim IDs：`C-100`–`C-105`
- final run：`20260912-MP-PATH-CERTIFICATE-001-01`
- source：`PathCertificate.agda`
- toolchain：同目录 `TOOLCHAIN.json` + `AGDA_LIBRARIES`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件。运行原件见 `../../verification/runs/20260912-MP-PATH-CERTIFICATE-001-01/`。当前未获 Git commit/tag 授权，不能称 `MACHINE_PROVED_VERSION_CLOSED`。
