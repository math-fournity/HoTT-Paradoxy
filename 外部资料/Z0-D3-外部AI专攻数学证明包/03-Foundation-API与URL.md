# Foundation 关键 API 与 GitHub 地址

> commit：`1fb01b72de546e1b50821fd05b1314a8d958583f`（Foundation 1fb01b72）。
> 仓库：`https://github.com/FormalizedFormalLogic/Foundation`
> 单文件 raw：`https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/<相对路径>`

## 证明里会直接用的引理（本地路径 → GitHub raw）
| 引理 | 本地路径 | GitHub raw |
|---|---|---|
| `neg_rel` / `neg_nrel` / `neg_and` / `neg_or` / `neg_all` / `neg_ex`（均 `@[simp]`） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean:75-96` | `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean` |
| `IsUFormula.neg_neg` | `.../Syntax/Formula/Functions.lean:127` | 同上 |
| `CraigTrick.craigCh` / `Sh.craig` 构造 | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean` | `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean` |
| `sigma_one_complete`（算术理论 Σ1 完全性） | `Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean` | `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean` |
| `Derivation.induction1` | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean` | `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean` |
| `Provable` 定义 `∃ d, Proof T d φ` | `Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:541` | `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean` |
| `of_provability`（语义，搬不进非标准 V） | `Foundation/FirstOrder/LK/Interpretation.lean:443` | `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/Foundation/FirstOrder/LK/Interpretation.lean` |

> 注意：第三位 AI 曾把 `R0/Basic.lean` 写成 `Foundation/FirstOrder/Arithmetic/Bootstrapping/R0/Basic.lean`（404）。
> 正确路径是 `Foundation/FirstOrder/SetTheory/R0/Basic.lean`（200）。但本包根本不用 R0，无关。

## 全量源码
- 本地：`/Volumes/D/HoTT-toolchain-cache/foundation-src/`（314 个 .lean）
- 已打包：`外部资料/Z0-D3-攻关包-完整版/Foundation/`（308 个 .lean，与 1fb01b72 一致）
- 逐条 URL 清单：`外部资料/Z0-D3-攻关包-完整版/foundation_modules_urls.txt`
