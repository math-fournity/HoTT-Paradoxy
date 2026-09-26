# 有向读数的原生检验：sHoTT 中的函子性与离散目标的冻结

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：Terra 复审 005 的 O-016。Terra 指出，C-38 只是普通 Cubical Agda 中的抽象引理，不是有向类型论的机器化；GWB 的结果依赖其模态与公理配置；sHoTT、Rzk、ℤ 都未核。用户随后许可安装 Rzk（【原话】“Rzk 可以安装了，你可以继续向后做事了。”）。本包在 sHoTT 的原生证明器里，检验 CN-023 §7 与回信 004 §3.4 中关于有向读数的说法，并固定它们的范围。讨论见 CN-027 与回信 006。
>
> - proof id：`MP-CG001-DIRECTED-NATIVE-001`（主包）、`MP-CG001-DIRECTED-NATIVE-NEG-001`（负控制）。
> - claim：`CG001-C-45`。
> - 工具链：Rzk 0.11.3，官方发布的 macOS ARM64 预编译包，发布方摘要 `5e0efb37…9471`。固定在 `/Volumes/D/HoTT-toolchain-cache/rzk-v0.11.3-macos-arm64/`，详见同目录 `RZK_TOOLCHAIN.json`。
> - 理论：Riehl–Shulman 单纯类型论（RS17，下称 sHoTT），按 Rzk 的实现。源码首行 `#lang rzk-1`；不用公设、不用假设、不用模态，没有洞。Rzk 自身有 `U : U`（其文档写明）；本包不声明大归纳类型。
> - 捕获与校验：`.claude/goals/CG-001-targeted-overview/tools/capture_rzk_proof_run.py`；`verify_cg001_run.py --rerun`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §10（GOAL_LOCAL_INDEX_ONLY）。

## 这个包为什么存在

回信 004 与 CN-023 §7 有三句关于有向出路的话：
1. 函子性在有向理论里照样白送；
2. 普通数值读数沿箭头仍然冻结；
3. 去掉可逆后，步数的困难消失。

Terra 要求把它们的适用范围写清。在 sHoTT 里能原生检验的，是第 1 句，以及第 2 句的条件形式：离散目标冻结。第 2 句的前提是“普通数值类型离散”，本包**不能**证明它，理由见下文“禁止外推”。第 3 句需要有向的高阶归纳类型（自由范畴），Rzk 0.11.3 不支持（其文档：构造子不能带 cube 或 shape 参数），本包不检验。

## 命题全文

量词与假设照实写。记号取自 RS17 与 rzk-lang/sHoTT 库的写法，并在源码中重述：
- `hom A x y := (t : Δ¹) → A [t ≡ 0₂ ↦ x, t ≡ 1₂ ↦ y]`；
- `hom-eq` 是由路径归纳给出的 `x = y → hom A x y`；
- `is-discrete A` 表示对一切 `x y`，`hom-eq A x y` 是等价（RS17 定义 7.1）；
- 等价取双可逆的定义。

| 部分 | 命题 | 源码符号 |
|---|---|---|
| (a) 函子性白送 | 对任意类型 `A B`、函数 `f : A → B` 与箭头 `α : hom A x y`，`ap-hom f α : hom B (f x) (f y)` 由逐点复合给出；它把恒等箭头送到恒等箭头（`refl`） | `ap-hom`、`ap-hom-id` |
| (b) 离散目标冻结 | 若 `B` 离散，则对任意 `f : A → B` 与任意箭头 `α : hom A x y`，都有 `f x = f y` | `discrete-reading-freezes` |
| (c) 普通数据的条件形式 | 以 `#data Bool := false \| true` 与 `#data ℕ := zero \| succ (n : ℕ)` 声明的类型：若 `Bool` 离散，则取值于 `Bool` 的读数沿任意箭头冻结，且任何箭头 `hom Bool false true` 都给出路径 `false = true`；若 `ℕ` 离散，取值于 `ℕ` 的读数同样冻结 | `Bool-reading-freezes`、`discrete-Bool-arrow-is-path`、`ℕ-reading-freezes` |
| (d) 路径仍有逆 | 对任意路径 `p : x = y`，`p` 接其反向等于 `refl` | `rev`、`concat`、`path-there-and-back` |
| 负控制 | 去掉离散假设，以 `refl` 断言 `f x = f y`，Rzk 拒绝（`cannot unify term x with term y`） | `WrongFreeze.rzk` |

## 解读【解释】

- **(a)** 就是有向版本的 `ap`：在 sHoTT 里，函数对箭头的作用同样是白送的，而且是定义性的。所以 A1′ 归因里的 P-fun（函子性）在有向理论中仍在。
- **(b)、(c)** 是 CG001-C-38 的原生对应，但只有条件形式：离散目标上的读数沿每支箭头冻结。至于普通数值类型是否离散：
  - 在 GWB 的三角化类型论 TT_□ 里，Nat、Bool 离散（其推论 3.20，依赖该文的公理与 ♭ 模态；来源报告，本包未重放）；
  - 在不加公理的 sHoTT 里证不出（来源报告，见“禁止外推”）。
- **(d)** 说明：若在 sHoTT 里仍把一步写成**路径**，A6′ 的机制（去而复返等于不动）照旧存在；只有把一步写成**箭头**，才没有逆。有向出路要解开 A6′，前提是改用箭头表示步子。

## 禁止外推

- **不证明** Bool、ℕ 或 ℤ 在 sHoTT 中离散。Rzk 0.11.3 文档（`docs/docs/en/getting-started/dependent-types.rzk.md` 的 Booleans 一节，【来源】）写明三点：
  - `Bool` 的归纳原理证不出 `Bool` 离散；
  - `Bool` 离散等价于一条“不连通原理”（存在一个类型，其中有两点之间没有箭头）；
  - 不加公理的理论证不出这条原理。

  本包没有重放这一元定理，它的身份是来源报告。
- **不检验** GWB 的 TT_□（模态、公理 6、推论 3.20），也不检验有向单价性。Rzk 的模态扩展属实验性质，本包没有使用。
- **不检验**“去掉可逆后步数可数”：Rzk 0.11.3 不支持带有向单元的归纳类型。该说法仍停在模型层（C-41 的列表，即自由幺半群），见 CN-023 §7。
- 数学内容是 RS17 的标准事实，**不主张原创**。
- “读数”“箭头”“步子”是解释标签，不说明任何物理事实。
