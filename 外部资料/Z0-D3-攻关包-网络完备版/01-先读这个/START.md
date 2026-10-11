# 先读这个（网络完备版攻关包）

本目录把主线收尾唯一剩下的数学定理 `ShCraigElim`（即 D3）打包成一个**最小、自包含、可网络自取**
的工作包，专门给一个能联网、能编译 Lean 4.34.0 的外部 AI 专攻证明。它不像"最小完整版"那样把
308 个 Foundation 源打包进来，而是给出 **167 个精确依赖模块的 GitHub raw URL**，运行环境有网络时
直接 `bash 06-Foundation模块获取/fetch_foundation.sh` 即可拉齐——这回应了之前某位 AI 在沙箱里
"看不到 API、交不出骨架"的困境：这里每个模块的 URL 都实测可达（commit 1fb01b72）。

阅读顺序：
1. 本文件（先读这个）
2. `02-目标命题/GOAL.md`（精确定理全文 + 归约链，读完后就知道"证完它主线就完成"）
3. `03-缺口精确定位/STATUS.md`（**真实进度**：10 个归纳支仍是 sorry 骨架，neg 律已证但未接）
4. `04-攻坚路线/ROUTES.md`（8 个待填支逐支给目标形状、可用引理、卡点）
5. `05-可用引理与API/API.md`（已证可用的 iT 相容律、Derivable 规则、关键 Foundation 位置）
6. `06-Foundation模块获取/`（`fetch_foundation.sh` + 167 行 URL 清单）
7. `07-项目模块/GodelQ/ZFC/`（本 repo 当前真实的 .lean 源，作为可编译基线）

关键事实（本机已实测，非猜测）：
- Lean 4.34.0 编译 import Z0Full 的探针约 12s exit 0，依赖链通。
- `ShCraigElimNegLaw.iT_neg`（一般 iT/neg 相容律，9 支）0 sorry 已编译。
- `ShCraigElimSetup.induction_setup` 仍是 10 个 `sorry` 骨架——这是真正的剩余工作。
- Foundation 依赖闭包 = 167 个模块（见 06/ 的清单），每个都有 raw URL。
