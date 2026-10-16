# 往返计步：一个按路径与运输来思考就永不停机的过程

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：Terra 复审 007 §4.4 说，A6′ 的“函数不存在”不是不停机。用户【原话】：“但是我觉得不排除，我们找到了构造理论攻击的角度，而且它的理解未必是对的。”本包按 KC-000048 的针对性思路，专门造一个依赖“步数”的停机过程，检验它在 Think in HoTT 的语义下是否停机。讨论见 CN-028 与回信 008。
>
> - proof id：`MP-CG001-PEDOMETER-HALTING-001`（主包）、`MP-CG001-PEDOMETER-HALTING-NEG-001`（负控制）。
> - claim：`CG001-C-47`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`。源码选项 `--safe --cubical --guardedness`，无公设，不加公理，零警告。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §11（GOAL_LOCAL_INDEX_ONLY）。

## 过程（现实侧）

一个人在两镇之间的路上来回走，身上带着计步器；计步器比出发时多走了 2 步，就停下。现实中，他走完一个来回就停。

## 命题全文

量词与假设照实写。

- **(a) 路径与运输的语义**：
  - 设定：任意类型 `A`；任意路径 `p : a ≡ b`，即路；`roundTrips p n` 为 `n` 个来回 `(p ∙ sym p)` 的复合；随身之物按**运输**跟着走：任意族 `B : A → Type`、任意读数 `read : B a → ℕ`、任意初值 `start : B a`，走完 `n` 个来回后的值是 `after n = subst B (roundTrips p n) start`。
  - 结论：
    - 对一切 `n`，`roundTrips p n ≡ refl`，且 `after n ≡ start`；
    - 不存在 `n`，使 `read (after n) ≡ 2 + read start`；
    - 带燃料的停机时间搜索 `run fuel`（在 `0 … fuel` 中找第一个满足停机条件的 `n`，条件用 `discreteℕ` 判定）对一切 `fuel` 都返回 `nothing`。
  - 源码符号：`roundTripsAreStaying`、`Carried.neverMoves`、`Carried.noHaltingTime`、`Carried.neverHalts`。
- **(b) 那个确实会为前进计数的族**：
  - 圆上的 `helix` 沿 `loop` 运输给数加一：`subst helix loop (pos 0) ≡ pos 1`，由 `refl`，即计算。
  - 但以 `abs` 读出、初值 `pos 0` 的来回步行，停机搜索对一切燃料都返回 `nothing`。
  - 源码符号：`helixCountsForward`、`helixWalkNeverHalts`。
- **(c) 正控制：步行作为数据**：
  - 步子的列表 `oscillation n`（`n` 个 `fwd ∷ back`）；计步器读列表长度。
  - 结论：一个来回后读数为 2（`dataHaltingTime = (1 , refl)`）；同一种搜索在燃料 1 时返回 `just 1`，由 `refl`，即计算。
  - 源码符号：`dataHaltingTime`、`dataHalts`。
- **负控制**：以 `refl` 断言 `subst helix (loop ∙ sym loop) (pos 0) ≡ pos 2`，内核拒绝（`0 != 2`：内核把往返算回了 0）。源码：`WrongHelixRoundTrip.agda`。

## 解读【解释】

- **不停机的含义**：这里的不停机是一个**指定过程**的不停机——对停机时间的无界搜索没有见证，任何燃料都跑不完。它不是观察窗内的超时，也不是一般的不可判定性。数学上它是 C-39（`noCarriedPedometer`）的推论；新的是把“函数不存在”转写成了用户 KC-000010 所说的那种“不可停机”：一个在现实中两步就停的过程，按理论的方式来思考就停不下来。
- **靶前提**（KC-000048 的针对性）：理论把“往回走”建模为“撤销”（逆路径，`p ∙ sym p ≡ refl`），把“随身携带”建模为运输。这两条都是 HoTT 的原生读法：路径是运动（Book 的合成读法，立场 S；补丁理论把补丁序列写成路径）；随身之物沿路径的变化就是运输（Book §2.3 的路径提升）。
- **(b) 说明问题不在“选错了族”**：螺旋族对前进步确实加一，但往回走恰是撤销，于是减一。任何随身计数器都只能数净位移，不能数步数。
- **(c) 说明任务本身不难**：把步行记成数据，同一个停机规则一步就停。要停机，就得把步子从路径里取出来，当作带先后的数据。这正对应用户 KC-000011 所说：“并不是Think in HoTT的标的中不能存在一个时间变量，而是Think in HoTT的思考过程、结果并不想时间、时序参与到其中。”

## 禁止外推

- 不说 HoTT 不能数步数，也不说 HoTT 不能停机：(c) 在 HoTT 中计数并停机。
- 不说一般问题不可判定，也不说运行超时：这里只有一个指定搜索没有停机见证。
- “步行按路径、随身按运输”是**解释桥**，身份见 CN-028：对补丁理论，它由作者的写法支持（补丁序列是路径；模型沿补丁运输仓库内容）；对物理步行，它条件于立场 S。
- 数学内容是标准事实（群胚律、运输、有界搜索），**不主张原创**。
- “步行”“计步器”“停下”是解释标签，不说明任何物理事实。
