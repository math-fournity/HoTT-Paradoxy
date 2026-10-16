# Delay 的单子结构与“等于 never”的观察含义（C-59，Cubical Agda）

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：Terra 复审 013 §2.1 的范围第 1、2 条：
> - `PedometerSemantics.agda` 只定义了 Capretta 风格的余归纳 `Delay` 对象，没有 `bind`，也没有验证单子律，所以“Delay monad”在那里只能作来源性简称；
> - `≡ never` 是 Cubical Agda 的路径相等，文件把它**解释**为互模拟。
>
> 本文件**导入**同一个 `Delay` 类型（不重抄），补上单子结构，并给出“等于 never”的内部观察刻画。讨论见 CN-031 与回信 014。
>
> - proof id：`MP-CG001-DELAY-MONAD-001`（主包）、`MP-CG001-DELAY-MONAD-NEG-001`（负控制）。
> - claim：`CG001-C-59`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9（`HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`），`--safe --cubical --guardedness`，无公设。运行由 `scripts/audit/capture_agda_proof_run.py` 捕获，`PedometerSemantics.agda` 作为依赖进入源码清单。
> - 标签：`FORMAL_DELAY_MONAD_LAWS_AND_OBSERVATIONAL_DIVERGENCE_WITH_SCOPE`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §14（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文（`DelayMonad.agda`）

- **(a) 单子结构**：`return`、`bind`（顺序组合：先运行前一个程序，再把它的值交给后续），以及三条单子律，都是路径：
  - `leftIdentity`：`bind (return a) f ≡ f a`；
  - `rightIdentity`：`bind d return ≡ d`；
  - `associativity`：`bind (bind d f) g ≡ bind d (λ a → bind (f a) g)`。
- **(b) `never` 是 `bind` 的左零元**：`neverBind`：`bind never f ≡ never`，先等一个发散程序的程序，不论后续是什么都发散。另有 `neverIsNotReturn`：`never` 不等于任何 `return a`。
- **(c) 发散是可观察的**：
  - `divergesRunsNothing`：`d ≡ never` 蕴含对一切燃料 `n`，`runFor n d ≡ nothing`；
  - `runsNothingDiverges`：反过来，对一切燃料都得到 `nothing` 蕴含 `d ≡ never`（余归纳构造）。
  - 所以“等于 never”恰好是“无论运行多少有限步都得不到结果”，不必借助“路径即互模拟”的解读。
- **(d) 纯后续映射有限观察**：`runForBindReturn`：`runFor n (bind d (return ∘ f)) ≡ map-Maybe f (runFor n d)`。
- **(e) 作为部件的停机程序**（C-55 的程序，经导入）：
  - P-rev 规格：`stopProgramRunsNothing`：停机程序对一切燃料都返回 `nothing`（C-47 (c) 的内容，现在由程序推出）；`stopThenAnythingIsNever`：停机程序接任何后续都等于 `never`，例如 `stopThenReportIsNever`（“停下后报告计数加一”）。
  - 正控制：在逃逸（C-50）、有向（C-51）、数据（步子列表）三种规格下，“停下后报告计数加一”在燃料 1 报出 2（`escapeStopThenReport`、`directedStopThenReport`、`dataStopThenReport`）。
- **负控制**（`WrongNeverBindRefl.agda`）：以 `refl` 断言 `bind never f ≡ never`，被拒：`bind never f != never of type Delay B`。两者展开后是 `later (bind never f)` 与 `later never`，余归纳记录没有 eta，相等只能由余归纳的路径给出。

## 解读【解释】

- Terra 的范围第 1 条由 (a) 补足：C-55 用的 `Delay` 连同 `return`、`bind` 构成单子，三条单子律以路径成立。“Delay 单子”这个名称现在有本地证明。
- Terra 的范围第 2 条由 (c) 回答：C-55 的 `stopProgramIsNever` 等价于“任何有限的运行都得不到结果”。这是一个内部、可观察的刻画，与 C-47 的有限燃料命题互相推出。它仍然不是墙钟时间或真实设备上的运行证据。
- (e) 把停机程序当作更大程序的一部分：在 P-rev 规格下，发散沿顺序组合传播，后面的一切都不会发生；在另外三种规格下，同一个组合程序报出计数。

## 禁止外推

- 单子律是对本文件的 `bind`、`return` 证明的；不涉及其他 Delay 实现，也不证明 Delay 与其他偏函数模型的等价。
- (c) 刻画的是本文件的 `runFor` 观察；不是现实程序、操作系统或证明助手的运行时间。
- P-rev 规格仍是规格，不是 HoTT 定理推出的现实义务（Terra 013 §2.1 第 4 条，接受）。
- 数学内容标准（Capretta 2005 一类结果的本地重证），**不主张原创**。
