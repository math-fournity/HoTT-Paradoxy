# 环境

## 本机（我已实测跑通）

| 项 | 值 |
|---|---|
| Lean | `4.34.0`（commit `293d5d0c`），路径 `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0` |
| Foundation | `1fb01b72de546e1b50821fd05b1314a8d958583f`，构建树 `/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean`（1893 模块） |
| Mathlib | `5ed2965256430c3649e86755f9576b54eca72435`，`/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-*/...` |
| 编译 24 个项目模块 | 约 18 秒（有缓存增量）/ 约 60 秒（全链冷启动） |
| 源码 | `05-源码/Foundation/`（167 个模块）+ `05-源码/项目模块/GodelQ/` |

自验（不需要 Lean）：

```bash
cd 05-源码 && python3 verify_coverage.py
# 期望: MISSING 0, project modules hash-ok 24, mismatch 0
```

## 若你在没有这套构建树的机器上

`05-源码/` 给了 **Foundation 的 167 个 `.lean` 源码**（全部导入闭包内的模块）。
Mathlib 的 1726 个模块没有给（上游，太大；版本由 `MATHLIB_CLOSURE.json` 锁定）。
所以你仍然需要一份 Mathlib + Foundation 构建树才能编译，但**不需要联网**。

`05-源码/项目模块/MATHLIB_CLOSURE.json` 的 `lean_path` 字段列了全部 9 个库根，
`library_roots` 给了每个根的名字到路径的映射。

## 关键 API 的 GitHub 位置

Foundation commit `1fb01b72de546e1b50821fd05b1314a8d958583f`，URL 前缀：

```
https://github.com/FormalizedFormalLogic/Foundation/blob/1fb01b72de546e1b50821fd05b1314a8d958583f/
```

| 模块 | 路径 |
|---|---|
| D3 家族 | `FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean` |
| D1 | `FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D1.lean` |
| CraigTrick | `FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean` |
| 可证性抽象 | `FirstOrder/Incompleteness/ProvabilityAbstraction/Basic.lean` |
| Tait 推导规则 | `FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean` |
| `Theory.Δ₁`/`RE` | `FirstOrder/Arithmetic/Bootstrapping/Syntax/Theory.lean` |
| 直接翻译 | `FirstOrder/LK/Interpretation.lean` |
