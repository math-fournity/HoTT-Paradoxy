# 把停机过程写成程序：Delay 单子里的发散与收敛；地点类型的反向对称（C-55、C-56）

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：Terra 复审 009。
> - §3 与 O-025：C-47 证明的是“不存在停机时刻”与“每个有限燃料的搜索都返回 nothing”，它没有给程序操作语义，所以“程序不停机”还不是形式命题。要声称程序不停止，须给出操作语义或无限执行的证明。
> - §5.2：提出第三分支（选项 C），即实际事件只取生成元 `go`、`back`，`sym go` 只是群胚补全的逆。
>
> 本包对这两点各给一个机器证明。讨论见 CN-030 与回信 012。
>
> - proof id：`MP-CG001-PEDOMETER-SEMANTICS-001`（主包）；负控制 `MP-CG001-PEDOMETER-SEMANTICS-NEG-001`、`-NEG-002`。
> - claim：`CG001-C-55`、`CG001-C-56`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设，不加公理，零警告。C-47、C-50、C-51 的定义在本文件中原样重述，文件自包含。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §13（GOAL_LOCAL_INDEX_ONLY）。

## 命题全文

### C-55（停机过程作为程序）

语义：Delay 单子，即一般递归的标准语义。程序是可能无穷的一串 `later` 步，可能以 `now a` 结束；`never` 是永远运行的程序。它是余归纳类型，其中的路径即互模拟。

- **(a) 无界搜索是程序，无见证即发散**：
  - 对任意可判定的停机条件 `P`，`searchFrom k` 检查 `P k`：成立就返回 `k`，否则走一步 `later`，从 `k + 1` 继续。
  - 若对一切 `k` 都 `¬ P k`，则 `searchFrom k ≡ never`（`Diverges.diverges`），特别地 `program ≡ never`（`programIsNever`）。
  - 另有 `convergesAtOne`：若 `¬ P 0` 且 `P 1`，则 `runFor 1 program ≡ just 1`。
- **(b) P-rev 规格下，停机过程就是 `never`**（`PRevProgram.stopProgramIsNever`）：
  - 对任意类型、任意路径 `p`、任意族 `B`、任意读数与初值，来回为 `p ∙ sym p`（P-rev），随身之物由 `subst` 携带（C-47 的规格）；
  - “多走 2 步就停”的程序等于 `never`。
- **(c) 其他三种规格下，同一个程序在燃料 1 时收敛到 1**：
  - `Escape.stopProgramConverges`：C-50 的规格，往回走是另一条独立路径，ℤ 纤维；
  - `Directed.stopProgramConverges`：C-51 的规格，自由范畴中的行走，由 `refl`；
  - `AsData.stopProgramConverges`：C-47 (c) 的规格，步子的列表，由 `refl`。

### C-56（方向是一种选择）

在 C-50 的地点类型 `Escape.Places` 上：
- `reverse` 是对合：`reverseInvolutive`，由 `refl`；`reverseEquiv : Places ≃ Places`。
- 它固定两个城镇：`reverseFixesWest`、`reverseFixesEast`。
- 它把 `go` 送到 `sym back`，把 `back` 送到 `sym go`：`reverseSendsGoToTheReverseOfBack`、`reverseSendsBackToTheReverseOfGo`，均由 `refl`。
- 经它携带，计数器沿 `go` 从 0 变为 −1（`reversedCounterRetreatsAlongGo`），沿 `sym go` 从 0 变为 +1（`reversedCounterAdvancesAlongSymGo`），均由 `refl`。

### 负控制

- `WrongPRevHalts.agda`（`-NEG-001`，对应 C-55）：在 C-50 的地点类型上取 P-rev 规格（回程为 `sym go`），以 `refl` 断言程序一步后返回 1。被拒：`nothing != just 1`，内核实际运行后什么也没得到。
- `WrongReverseFixesGo.agda`（`-NEG-002`，对应 C-56）：以 `refl` 断言 `cong reverse go ≡ go`。被拒：`back (~ i) != go i`。

## 解读【解释】

- **对 O-025**：
  - “不停机”现在是一个形式命题：在一般递归的标准语义里，P-rev 规格下的停机过程等于永远运行的程序。
  - 它仍然条件于 P-rev，这一点我在 012 中让步。
  - 正控制 (c) 表明，同一个程序在另外三种规格下都在一步内收敛，所以差别恰好在回程与携带的规格上。
- **对选项 C**：
  - 选项 C 是正当的建模纪律，我接受它是第三分支。
  - C-56 显示它的代价：哪些路径算实际事件，不由类型及其城镇决定。存在一个固定两镇的对称，把事件与“反事件”互换，计数的正负随之互换；方向要靠点名生成元另行给出。
  - 在有向模型（C-51）中，这样的对称连写都写不出来：固定城镇的函子必须把 `go` 送到一条自西向东的行走，而每条行走都使计数增加（C-51 (c)(e)）。
  - 这是“方向是附加结构还是内在结构”的形式对照；它是否就是用户 KC-000011 所说的“时序不参与思考过程”，属于解释，由用户裁定。
- **语义来源**：Delay 单子作为一般递归的语义，见 Capretta 2005（*General recursion via coinductive types*，LMCS），来源报告，未在本仓库重放；本包自己定义了 Delay，不依赖该文。

## 禁止外推

- C-55 (b) 的发散条件于 P-rev 与“随身即运输”的规格。它不是一般的不可判定性，不是超时，也不说 HoTT 不能停机：(c) 中同一程序收敛。
- C-56 不说选项 C 不正当，只说方向是附加结构。
- “行人”“路”“计步器”“停下”“事件”是解释标签。
- 数学内容标准（Delay 单子、HIT 上的对称），**不主张原创**。
