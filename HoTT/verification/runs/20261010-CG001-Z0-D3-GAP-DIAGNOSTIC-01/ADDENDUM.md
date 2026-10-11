# 诊断补充（2026-10-11）：`zfcTr_D3_internalize` 缺口的精确 API 定位 + 诚实降格重验证

> 本文件是对 `RUN.json`（诊断运行 `20261010-CG001-Z0-D3-GAP-DIAGNOSTIC-01`）的补充，**不是机器证明收据**。
> 目的：把缺口从"ZFC 内部化 Σ1 完全性"进一步精确到 Foundation 的类型类实例层；并重验诚实降级的 `Z0Blocked.lean` 与干净收据文件 `Z0Full.lean` / `Z0Bridge.lean` 的编译状态。

## A. 决定性探针 `GodelQ/Probe_d3final.lean`

`#check Theory.Δ₁ Sh` 与 `#check provable_D3 (T := Sh)` 的输出（捕获于 `stdout_probe_d3final.txt`）：

```
Theory.Δ₁ Sh : Type
GodelQ/Probe_d3final.lean:14:7: error(lean.synthInstanceFailed): failed to synthesize instance of type class
  Theory.Δ₁ Sh
```

含义：
- `Theory.Δ₁ Sh` 是良定义的 Type（类**存在**）；
- 但 `provable_D3 (T := Sh)` 需要 `[Theory.Δ₁ Sh]` 实例，而该实例无法被合成。
- 由 `Sh_provable_iff`（`zfcTr σ ↔ provabilityPred Sh σ`），`zfcTr_D3_internalize` 等价于 `provable_D3 (T := Sh)`，故缺口 == 缺失的 `Theory.Δ₁ Sh` 实例 == **ZFC 的 Σ₁ 完全性**，Foundation（commit `1fb01b72`）尚未形式化。

## B. 诚实降级的重验证（2026-10-11，本地驱动 `/tmp/build_z0.py`）

| 文件 | 禁用标记检查 | 结果 | 捕获 |
|---|---|---|---|
| `GodelQ/ZFC/Z0Blocked.lean` | 关闭（含精确 `sorry`） | `rc=0` + `warning: declaration uses 'sorry'` | `stdout_reverify_Z0Blocked.txt` |
| `GodelQ/ZFC/Z0Full.lean` | 开启（须无 `sorry`） | `rc=0`，无 `sorry` | （同基线，Z0Bridge 依赖） |
| `GodelQ/ZFC/Z0Bridge.lean` | 开启（须无 `sorry`） | `rc=0`，无 `sorry` | `stdout_reverify_Z0Bridge.txt` |

结论：`Z0Blocked.lean` 的精确 `sorry` 命题类型可检查（缺口良定义、非类型错误）；`Z0Full.lean` / `Z0Bridge.lean` 收据文件无 `sorry`，降级未引入新错误。

## C. 治理

- 不产出 Z0 机器证明收据（`zfcTr_D3_internalize` 保留 `sorry`）。
- 闭合需 CG-008：形式化 `Theory.Δ₁ Sh`（集合论 Σ₁ 完全性）或 `Z0Bridge.bridge`。
- F-011 合规：未 push、未碰 `sources/` / `private-audit/`；仅下游 `HoTT/formal/`、`HoTT/verification/runs/`、矩阵与追踪文档。
