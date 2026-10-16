# MP-TRANSITION-LIFT-001：状态商/当前态提升边界的原生 Cubical 升级

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`

本包把 WebGPT R036/R038 的核心边界从“纸笔 + 有限 Python 检查”升级为原生 Cubical Agda 机器证明：

- R036 的有限状态商反例：`a → b → d`、`α(a)=α(b)=w`、`α(d)=W`；
- R038-D 的截断—极限不可交换核心：`A k = Σ m, k ≤ m` 的精确相容极限为空，而逐层截断后的相容极限有元素。

它使用真实 Cubical Path/HIT 语义：命题截断 `∥_∥₁` 用于存在像 `E`、当前后继 `C` 与截断极限；`--safe --cubical --guardedness`，最终运行 exit 0、零 warning。

## 冻结命题（`C-110`–`C-117`）

| claim | 形式化结果 |
|---|---|
| `C-110` | 固定三状态过程从 `a` 经两步到达 `d`（`C-110-terminates`），且 `d` 无出边（`C-110-d-terminal`）。 |
| `C-111` | 存在像 `E` 有自环 `E w w`（来自 `a → b`）与边 `E w W`（来自 `b → d`）；常值路径 `β n = w` 给出任意长的抽象运行（`C-111-e-ww`、`C-111-e-wW`、`C-111-beta-path`）。 |
| `C-112` | 抽象两步前缀 `w,w,w` 有抽象证据（`C-112-abstract-two-www`），但从初态 `a` 没有相容具体提升（`C-112-no-lift-two`）。 |
| `C-113` | 不存在把每个 `E(α s, v)` 变为 `C(s, v)` 的当前态提升函数；见证在 `(b,w)`（`C-113-no-current-lift`）。 |
| `C-114` | `A k = Σ m, k ≤ m` 的精确相容极限为空（`C-114-LimA-empty`）。 |
| `C-115` | 同一塔逐层截断后的相容极限有元素（`C-115-limTrunc`）。 |
| `C-116` | 不存在从截断极限回到精确极限的函数，因此比较映射无逆（`C-116-no-inverse`）。 |
| `C-117` | 不存在同时在 `R` 上严格下降、在 `α` 纤维上恒定的自然数等级（`C-117-no-descending-fiber-constant-rank`）。 |

## 解释边界（判词）

判词：`TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`（判词阶梯第二级的结构性版本）：

- `E` 是合法的 may 过近似；它的自环与无限抽象路径是抽象模型里的真实对象，不证明具体过程发散；
- 缺口是“逐边可行”不能拼成“同一条具体轨迹”：`C-112`/`C-113` 给出有限、可判定、无 LEM/选择的反例；
- `C-114`–`C-116` 精确表达“先要求相容再截断”与“先逐层截断再要求相容”不交换；
- `C-110` 是正向控制：原过程确实在两步内完成；
- 不是 HoTT 内部矛盾；HoTT 正确区分了 `C`（固定当前代表）与 `E`（只固定抽象端点）。

## 不证明（非目标）

- 不证明一般图的 lift/limit 定理（只覆盖固定有限模型与固定塔）；
- 不覆盖 R038 的 Acc 迁移定理（R038-A/B 仍为 paper 级）；
- 不证明任何实际系统或库强制采用“把 may 抽象当精确执行谱”；
- 不主张物理时间、HoTT 独有性或原创性（R036/R038 已给出纸笔推导；本包是原生升级 + 正控制）。

## 证明身份

- proof ID：`MP-TRANSITION-LIFT-001`
- claim IDs：`C-110`–`C-117`
- source：`TransitionLift.agda`
- toolchain：`TOOLCHAIN.json` + `AGDA_LIBRARIES`
- final run：`20260912-MP-TRANSITION-LIFT-001-01`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件；运行原件、外部依赖哈希与命令在 `../../verification/runs/20260912-MP-TRANSITION-LIFT-001-01/`。当前未获 Git commit/tag 授权，因此不能称 `MACHINE_PROVED_VERSION_CLOSED`。
