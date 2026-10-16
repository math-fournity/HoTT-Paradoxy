# 给外部 AI 的攻关包：README 与复现环境

本目录是一个**最小、自包含、可编译**的工作包，目标只有一个：把主线收尾唯一剩下的数学定理
`ShCraigElim` 证出来（见 `00-缺口精确定位.md`）。你不需要关心本仓库 8 个方向的其余历史。

## 1. 它包含什么

| 文件 | 内容 |
|---|---|
| `00-缺口精确定位.md` | 目标定理、为什么是它、10 支现状、核心难点、排除的死路 |
| `01-README与复现环境.md` | 本文件：环境、命令、边界 |
| `02-API引用与源代码地址.md` | 每个关键 Foundation API 的本地路径 + 可联网 `curl` 的 GitHub 原始地址 |
| `03-九支归纳任务拆解.md` | 8 个待填支的逐支目标 + 可用引理 + 卡点 |
| `04-编译与收据命令.md` | 拓扑序编译命令、收据工具、禁令 |
| `Foundation_fetch_list.txt` | 本项目实际依赖的 Foundation 模块清单（相对路径，每行一个） |
| `Foundation_modules_urls.txt` | 上述每个模块的 GitHub 原始地址（可 `curl -O` 复现） |

## 2. 复现环境（已实测可用）

**工具链（固定，不得修改 Foundation/Mathlib 源码）**：
- Lean **4.34.0**，`commit 293d5d0c`，二进制在 `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean`
  （其它机器用 `leanprover/lean4:v4.34.0` 镜像）。
- Mathlib `5ed29652`：构建目录 `/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435/`
- Foundation `1fb01b72`：
  - 源码：`/Volumes/D/HoTT-toolchain-cache/foundation-src/`（308 个 `.lean`，与本攻关包 `Foundation_modules_urls.txt` 完全对应）
  - olean 构建：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean`
- 增量编译脚本：`/tmp/d3build/devbuild.py`（仅开发期用，非收据工具）。

**目标证明包（你要改的）**：
`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/`（含 `GodelQ/ZFC/` 下 45 个 `.lean`）。

## 3. 复现步骤（联网机器）

1. 安装 Lean 4.34.0（elan：`leanprover/lean4:v4.34.0`）。
2. 取得 Mathlib `5ed29652` 与 Foundation `1fb01b72` 的构建（Foundation 仓库：
   `https://github.com/FormalizedFormalLogic/Foundation`，固定 commit
   `1fb01b72de546e1b50821fd05b1314a8d958583f`）。
3. 用 `Foundation_modules_urls.txt` 逐条 `curl -O` 把依赖模块拉到本地
   （地址模板见 `02-API引用与源代码地址.md` 的 §0），或用本机已验证的 308 个模块全量
   （`外部资料/Z0-D3-攻关包-完整版/Foundation/`，与本攻关包选择的依赖一致）。
4. 按 `04-编译与收据命令.md` 的拓扑序编译。

## 4. 边界（务必遵守）

- **只读依赖**：Foundation / Mathlib 源码不得修改。新增引理只能加在 `godel-q-zfc-z0-full` 包内新文件。
- **不进收据源**：任何含 `sorry` 的文件都会被 `zfc_lean_check.py` 拒收；必须真证完。
- **不碰**：`sources/`、`private-audit/`、他人未提交文件、`main` 分支与其他 Session 工作树。
- **这是数学证明任务**：环境已确认可用，难点在于归纳支的证明，不在于工具。
- 八方向覆盖已闭合，只攻 `ShCraigElim` 这一个定理。

## 5. 快速自检（证明你能编译）

```bash
cd <repo根>/HoTT/formal/claude-cg001/godel-q-zfc-z0-full
python3 -B /tmp/d3build/devbuild.py . GodelQ/ZFC/EnvProbe.lean
# 期望：编译 EnvProbe.lean（只 import Z0Full）exit 0，约 12 秒
```

若此步通过，说明依赖链通了，可以开始改 `ShCraigElimSetup.lean` 的 8 个 `sorry`。
