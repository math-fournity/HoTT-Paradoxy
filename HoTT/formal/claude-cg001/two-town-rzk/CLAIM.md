# 两镇往返：同一个任务、同一个演算，只换一步的种类（C-58，Rzk，带显式有向单价接口）

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：Terra 复审 013 §2.4 第 3 条与 T-027：C-57 的路径分支是 `p : A = B` 后取 `rev p`，箭头分支却是**两次相同的自箭头** `Gl A A s`；两个自步不是 `west → east → west` 的同一两镇返程，所以不是严格保任务的往返对照。本包把两镇任务写定一次，两种步子都跑同一个任务。讨论见 CN-031 与回信 014。
>
> - proof id：`MP-CG001-TWO-TOWN-001`（主包）、`MP-CG001-TWO-TOWN-NEG-001`（负控制）。
> - claim：`CG001-C-58`。
> - 工具链：Rzk 0.11.3（`HoTT/formal/claude-cg001/directed-native/RZK_TOOLCHAIN.json`），sHoTT，无公设，不加公理，不用模态。运行由 `.claude/goals/CG-001-targeted-overview/tools/capture_rzk_proof_run.py` 捕获。
> - 标签：`RZK_TYPECHECKED_RELATIVE_TO_EXPLICIT_DIRECTED_UNIVALENCE_INTERFACE / TWO_TOWN_TASK_PRESERVED_AT_INTERFACE_LEVEL`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §14（GOAL_LOCAL_INDEX_ONLY）。

## 任务（两个分支的参数完全相同）

| 项 | 内容 |
|---|---|
| 两镇 | `A B : S`，任意，可以是 S 的两个不同对象 |
| 随身之物 | 起点镇的值 `u0 : El A` |
| 读数 | `ra : El A → R`（在 A 读）、`rb : El B → R`（在 B 读）；`R` 带 `z : R`、`s : R → R`，只用一条事实 `no-fixed`：`z = s (s z)` 不可能（`R` 扮演步数，`s` 为后继） |
| 起点 | `start : ra u0 = z` |
| 计步合同 | 每段加一：对一切 `u`，`rb (carry go u) = s (ra u)`；对一切 `w`，`ra (carry back w) = s (rb w)` |
| 停机（Done） | 去了再回来，在 A 的读数为 `s (s z)` |
| 路径分支 | `go = p : A = B`，`back = rev p`，携带 = 运输 |
| 箭头分支 | `go = Gl A B φ`，`back = Gl B A ψ`，携带 = 协变运输；`φ`、`ψ` 任取，只要 `rb (φ u) = s (ra u)`、`ra (ψ w) = s (rb w)` |

## 接口（只作为定理的假设出现，不是公设；与 C-57 相同）

| 假设 | 来源（GWB，arXiv:2407.09146v2；PDF 编号，括号内为 arXiv HTML 渲染的编号） |
|---|---|
| `S : U`、`El : S → U`，`El` 协变（RS17 定义 8.2） | 引理 5.11（HTML 5.10）：`𝕀 → S` 诱导协变族 |
| `du`：对一切 `A B`，`hom S A B → (El A → El B)`（箭头 ↦ 协变运输）是等价 | 定理 6.13（HTML 6.10），有向单价性，取端点固定的形式 |
| `Gl` 取该等价的截面，`coe-Gl` 由截面律推出 | 定义 6.14（HTML 6.11）、引理 6.15（HTML 6.12） |
| (c) 的 `comp`、`coe-comp` | 引理 6.16（HTML 6.13，S 是 Segal 的：复合存在）、推论 6.17（HTML 6.14：S 中态射的复合由普通函数复合实现） |

编号的来历：GWB v2 的 PDF 文本（sciverse 全文；其正文摘要与作者单位与 v2 HTML 逐字一致、与 v1 不同）中，第 6 节在定理 6.13 之前有 Remark 6.6、Notation 6.7、Remark 6.9 三个与定理共用计数器的环境；v2 HTML 未渲染这三个环境（显示为原始的 `{remark}`、`{notation}`、`{remark}`），也没有计数，于是其后编号整体少 3。第 3 节同理少 6（推论 3.20 在 HTML 中为 3.14）；第 5 节的 Convention 5.3 与 Notation 5.12 未渲染，故 Notation 之前少 1（引理 5.11 在 HTML 中为 5.10）、之后少 2（引理 5.13 在 HTML 中为 5.11）。回源记录见 CN-031 §2。

## 命题全文（`TwoTownRoundTrip.rzk`，26 个定义，`Everything is ok!`）

- **(a) 路径**：
  - `path-round-trip-reading`：对一切 `p : A = B`，去了再回来，A 处的读数等于起点读数 `ra u0`；
  - `path-round-trip-never-stops`：因而停机条件（读数为 `s (s z)`）不成立（依据 `start`、`no-fixed`）；
  - `no-two-way-path-pedometer`：没有路径满足两段都加一的计步合同。
- **(b) 箭头**：
  - `arrow-go-adds-one`、`arrow-back-adds-one`：`Gl A B φ`、`Gl B A ψ` 各使读数加一（`coe-Gl`）；
  - `arrow-round-trip-stops`：去了再回来，A 处的读数为 `s (s z)`，停机条件成立。
- **(c) 复合**：`composite-two-town-round-trip-stops`：在 `comp`、`coe-comp` 的假设下，复合的来回箭头 `comp (Gl A B φ) (Gl B A ψ)` 也满足停机条件。
- **(d) C-57 是特例**：`c57-arrow-walk-as-special-case`、`c57-path-round-trip-as-special-case` 分别由 (b)、(a) 在 `A = B`、`R = El A`、`ra = rb = 恒等`、`φ = ψ = s` 处推出 C-57 的 `arrow-walk-stops` 与 `path-round-trip-never-stops`。
- **负控制**（`WrongReturnAlongGo.rzk`）：在箭头分支里把去程箭头 `Gl A B φ` 当作回程（`hom S B A` 的元素）使用，被拒：`cannot unify term B with term A`。路径分支的回程 `rev p` 白送（P-rev）；箭头分支没有形式的逆，回程必须是第二个独立的步子。

## 解读【解释】

- 两个分支的镇、随身之物、读数、起点、计步合同与停机条件是同一组参数；唯一的区别是步子的种类。这回答了 Terra 013 的“两个自步不是同一两镇返程”：往返现在是 `A → B → A`。
- **C-57 为什么是自箭头**：它是本包在 `A = B` 处的特例（(d)）。而且在 S 里，镇就是类型：S 作为 `𝒰_□` 的子类型是单价的（GWB §6.1 开头；推论 6.18 S 是 Rezk 的），所以纤维等价的两个“镇”在 S 中相等。若坚持用 S 的对象当镇、两镇携带同一种计数，往返按这一认同就是一对自箭头。要让两镇在携带同类计数时仍然不同，镇应取自另一个底类型 `T`，计数族取为 `El ∘ F`（`F : T → S`）；本包 (b) 在 `T = S`、`F = 恒等` 时就是这种形式，一般的 `T` 需要能构造带箭头的底，Rzk 0.11.3 中没有。【来源】+【解释】
- 负控制把 P-rev 的位置指了出来：路径的回程是去程倒着走，免费得到，沿它运输把去程的加一撤销；箭头没有这种倒着走，回程是另一个事件。

## 禁止外推

- 相对于显式接口：不构造 S，不重放 GWB 的 TT_□（带模态与新增推理原则的系统），不给出具体的 `Nat ∈ S` 或 `Gl(Nat, Nat, suc)` 见证。接口一致即这样的 `S`、`El` 存在，是 GWB 的定理（来源，未重放）。
- `φ`、`ψ` 的存在是箭头分支的假设；本包证明的是“有了它们，停机合同成立”，以及“路径分支对一切 `p` 都不成立”。
- (c) 的复合假设代替 GWB 引理 6.16 与推论 6.17，本包没有证明它们。
- 不涉及现实行走；“镇”“步”“停机”是解释标签。数学内容标准，**不主张原创**。
