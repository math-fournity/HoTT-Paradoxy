# CG-007 形式化工具

> 本目录的工具都属于 **CG-007 目标包**，不是收据工具。收据工具是
> `capture_run.py` 与（校验侧）`.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py`。

## 一览

| 工具 | 用途 | 是否产出收据 |
|---|---|---|
| `capture_run.py` | 抓一次正式运行（`RUN.json`/`stdout`/`stderr`/`environment`/`source-manifest`） | **是** |
| `capture_branch_run.py` | 同上，用于分支包（不同 package 约定） | **是** |
| `make_pins.py` / `make_mathlib_pins.py` | 生成/更新 `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 否（基础设施） |
| `devbuild.py` | 增量编译，迭代用 | 否 |
| `devbuild_ns.py` | 同上，无沙箱变体（宿主不允许嵌套沙箱时用） | 否 |
| `lean_probe.py` | 单文件探针，快速验证一条引理能否 elaborate | 否 |

## `devbuild.py`：迭代编译

```bash
cd <repo>
PKG=HoTT/formal/claude-cg001/godel-q-zfc-z0-full
T=.claude/goals/CG-007-formalization-completion/tools

python3 -B $T/devbuild.py $PKG \
  GodelQ/ProcessObservation.lean GodelQ/EffectiveTheory.lean GodelQ/GodelZenoRunner.lean \
  GodelQ/FoundationArith.lean GodelQ/ZFC/SetLanguage.lean GodelQ/ZFC/SchemaDelta1.lean \
  GodelQ/ZFC/ReplacementDelta1.lean GodelQ/ZFC/ZFCDelta1.lean GodelQ/ZFC/NumeralCode.lean \
  GodelQ/ZFC/NeverRE.lean GodelQ/ZFC/OmegaArith.lean GodelQ/ZFC/NumeralSemantics.lean \
  GodelQ/ZFC/ArithInterp.lean GodelQ/ZFC/R0Model.lean GodelQ/ZFC/Effective.lean \
  GodelQ/ZFC/Soundness.lean GodelQ/ZFC/OmegaLaws.lean GodelQ/ZFC/PAModel.lean \
  GodelQ/ZFC/Z0Shadow.lean GodelQ/ZFC/Z0PA.lean GodelQ/ZFC/ShRE.lean \
  GodelQ/ZFC/InternalTranslate.lean GodelQ/ZFC/TranslateRE.lean GodelQ/ZFC/Z0Full.lean
```

**顺序必须是真实的 import 拓扑序。** 例如 `SeqTranslate.lean` 在 `InternalTranslate.lean`
之后；`Z0UniBridge.lean` 在 `Z0Full.lean` 之后。顺序错了会报
`object file ... does not exist`。

**缓存位置**：默认 `<repo>/.cg007-build/<package-name>/`（已进 `.gitignore`）。
可用环境变量 `CG007_BUILD_DIR` 改到别处。**不要**放进包目录——包目录会进收据源。

**增量语义**：对（有序源列表）做链式 SHA-256；一个源只有在它自己**和它前面的全部源**
都没变时才跳过。

## `lean_probe.py`：单文件探针

```bash
python3 -B $T/lean_probe.py $PKG /path/to/probe.lean
```

探针文件可以 import 任何已被 `devbuild.py` 编译过的模块。适合"这个名字对不对、
这个签名长什么样"这类问题，几秒出结果，不污染包。

## 完整环境

```
Lean 4.34.0      /Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0
Foundation 源码  /Volumes/D/HoTT-toolchain-cache/foundation-src
Foundation 构建  /Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean
Mathlib          /Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-*
```

包内的 `LEAN_TOOLCHAIN.json` 与 `MATHLIB_CLOSURE.json` 把路径钉死。
换机器时改这两个 JSON 的 `prefix` / `lean_path` 即可，工具本身不用动。

## 不要做的事

- **不要**把工具或缓存放进收据源（`capture_run.py --source` 的列表）。
- **不要**改 Foundation / Mathlib 源码。
- `capture_run.py` 的 `--source` 顺序同样是 import 拓扑序；顺序错会让运行失败，
  而失败的 run 目录要先清掉才能重跑同名 run-id。
