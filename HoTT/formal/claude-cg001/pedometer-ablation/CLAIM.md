# 计步器的消融：沿路径携带的变化都能被撤销，而有向模型里的计步器会停

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：回信 008 §5（CN-028 §4.4）写了一个有向预测：在有向理论里，往回走是一支新箭头而不是逆，随身之物写成协变族，计步器就应该能数到 2，往返计步的停机过程就会停。我当时说“现在还做不了，因为 Rzk 0.11.3 没有有向单价性”。用户【原话】：“我认为这样停下来，不是理由，Rzk，我们难道不能用其他的机器证明系统证明吗？难道我们不能想其他的机器证明方法吗？不过就是写代码，让Terra和你互相审计嘛。”本包是其中的 Cubical Agda 部分。同一消融另有两个兄弟包：
> - `pedometer-ablation-lean/`：C-52，用 Lean 4 作第二个独立内核，重证 C-51；
> - `pedometer-ablation-rzk/`：C-53，在有向类型论 sHoTT 自身中（Rzk）重证 C-49 的核心，并证明离散底上的协变运输同样可逆。
>
> - proof id：`MP-CG001-PEDOMETER-ABLATION-001`（主包）；负控制 `MP-CG001-PEDOMETER-ABLATION-NEG-001`、`-NEG-002`、`-NEG-003`。
> - claim：`CG001-C-49`、`CG001-C-50`、`CG001-C-51`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`。源码选项 `--safe --cubical --guardedness`，无公设，不加公理，零警告。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §12（GOAL_LOCAL_INDEX_ONLY）。思考记录：CN-029。

## 过程（现实侧）

与 C-47 相同：一个人在两镇之间的一条路上来回走，身上带着计步器；计步器比出发时多了 2 步就停下。现实中，他走完一个来回就停；计步器只增不减。

## 命题全文

量词与假设照实写。

### C-49（HoTT：沿路径携带的变化，都能沿另一条路径撤销）

设定：任意类型 `A`，任意族 `B : A → Type`；“携带”指沿路径的运输 `subst B`。

- **(a) 前进迫使后退**（`advanceForcesRetreat`）：
  - 对任意读数 `r : (x : A) → B x → ℕ`、路径 `p : x ≡ y`、`u : B x`、`k : ℕ`：
  - 若 `r y (subst B p u) ≡ k + r x u`，则 `r y (subst B p u) ≡ k + r x (subst B (sym p) (subst B p u))`。
  - 也就是说，把携带的结果沿 `sym p` 带回去，读数正好低 `k`。所依据的是 `thereAndBack : subst B (sym p) (subst B p u) ≡ u`。
- **(b) 只增不减即不变**（`Monotone.monotoneIsInvariant`）：
  - 对任意类型 `N`、任意满足反对称的关系 `_≼_`、任意读数 `r : (x : A) → B x → N`：
  - 若对一切路径 `p` 与 `u` 都有 `r x u ≼ r y (subst B p u)`（没有携带使读数降低），则对一切 `p` 与 `u` 都有 `r y (subst B p u) ≡ r x u`（读数从不改变）。
  - ℕ 与 `≤` 的实例：`monotoneIsInvariantℕ`。推论 `noMonotoneAdvance`：在此假设下，没有路径使读数加一。
- **(c) 没有双向计步器**（`noTwoWayPedometer`）：
  - 对任意路径 `p : a ≡ b`、读数 `ra : B a → ℕ`、`rb : B b → ℕ`，以及任意 `start : B a`：
  - 不可能同时有 `∀ u → rb (subst B p u) ≡ suc (ra u)`（沿路走一步加一）与 `∀ v → ra (subst B (sym p) v) ≡ suc (rb v)`（沿同一条路走回来也加一）。
- **(d) 没有不可逆的一步**（`noIrreversibleStep`、`noSucPath`）：
  - 对任意路径 `p : a ≡ b`、读数 `ra`、`rb`，只要终点处读数 0 出现过（有 `v₀ : B b` 使 `rb v₀ ≡ 0`），就不可能有 `∀ u → rb (subst B p u) ≡ suc (ra u)`。
  - 特例：宇宙中没有从 `ℕ` 到 `ℕ` 的路径，其运输作用为 `suc`：`¬ (Σ[ P ∈ ℕ ≡ ℕ ] ((n : ℕ) → transport P n ≡ suc n))`。
- **(e) 两段都计数，就逼出一次反向行走**（`countingForcesAntiWalk`）：
  - 对路径 `go : a ≡ b`、`back : b ≡ a`、族 `B`、读数 `ra`、`rb`：若沿 `go` 与沿 `back` 携带都使读数加一，则：
    1. 只要 `B a` 非空，`back` 就不等于 `sym go`；
    2. 对每个 `v : B b`，`rb v ≡ suc (ra (subst B (sym go) v))`，即沿 `sym go` 携带使读数减一。

### C-50（HoTT 内部的出路：往回走是另一条独立的路径）

设定：高阶归纳类型 `Escape.Places`，含两点 `west`、`east`，两条路径 `go : west ≡ east`、`back : east ≡ west`；族 `Ped` 的纤维为 `ℤ`，并规定 `Ped (go i) = Ped (back i) = sucPathℤ i`（两条路都加一）。

- **(a) 能数，能停**：
  - `goAdds`、`backAdds`：沿 `go`、沿 `back` 各加一（`refl`，即计算）；
  - `roundTripAddsTwo`：`subst Ped (go ∙ back) (pos 0) ≡ pos 2`（`refl`）；
  - `halts`：对 `n` 个来回 `rounds n` 的停机时间搜索在燃料 1 时返回 `just 1`（由 `haltsAtOne`，前提是 `notAtStart` 与 `afterOne`）。
- **(b) 代价**：
  - `antiWalk`：理论同时给出路径 `sym go`（从 `east` 到 `west`），沿它携带，读数从 0 变为 `negsuc 0`，即 −1（`refl`）；
  - `roundTripIsNotStaying`：`¬ (go ∙ back ≡ refl)`；
  - `backIsNotTheReverse`：`¬ (back ≡ sym go)`；
  - `placesAreNotASet`：`¬ isSet Places`。

### C-51（有向模型，集合层）

设定：图 `west —go→ east —back→ west` 上的自由范畴。
- `Town`；`Step`（`go : Step west east`、`back : Step east west`）；
- `Walk`（`stay`、`_then_`），复合为 `_++_`。

命题：
- **(a) 范畴律**：`stay ++ w = w` 按定义成立；`++-stay`；`++-assoc`。
- **(b) 计步器**：
  - `carry : Walk x y → ℕ → ℕ`，定义为 `carry stay n = n`、`carry (s then w) n = carry w (suc n)`；
  - 函子性 `carryFunctor : carry (w ++ v) n ≡ carry v (carry w n)`；
  - 一维意义下的协变（提升唯一）`uniqueLift : isContr (Σ[ m ∈ ℕ ] carry w n ≡ m)`。
- **(c) 只增、按步数增**：
  - `carryIsLength : carry w n ≡ length w + n`；
  - `neverLowers : n ≤ carry w n`；
  - `everyStepRaises : n < carry (s then w) n`；
  - `roundTripAddsTwo : carry roundTrip n ≡ 2 + n`（`refl`）。
- **(d) 停机**：`halts : run 1 ≡ just 1`（`refl`）。
- **(e) 没有逆**：
  - `goHasNoInverse : ¬ (Σ[ w ∈ Walk east west ] (go then w) ≡ stay)`；
  - `roundTripIsNotStaying`。
- **(f) 与 C-50 的对照**（`realiseCarry`）：
  - 把 `go`、`back` 分别送到 `Escape.go`、`Escape.back`，把每条有向行走实现为 `Places` 中的路径；
  - 对每条有向行走 `w` 与每个 `n`：`subst Escape.Ped (realise w) (start x n) ≡ start y (carry w n)`。

### 负控制

内核应拒绝，实际均被拒绝。
- `WrongTwoWayRoad.agda`（`-NEG-001`，对应 C-49）：
  - 只有一条路径 `go` 的道路 HIT，族沿 `go` 加一；
  - 以 `refl` 断言走回来也加一：`subst Ped (sym go) (pos 1) ≡ pos 2`；
  - 被拒：`0 != 2`，内核把走回来算成了 0。
- `WrongDirectedStays.agda`（`-NEG-002`，对应 C-51）：以 `refl` 断言 `carry roundTrip 0 ≡ 0`，被拒：`2 != 0`。
- `WrongAntiWalkAdvances.agda`（`-NEG-003`，对应 C-50）：以 `refl` 断言 `subst Ped (sym go) (pos 0) ≡ pos 1`，被拒：`negsuc zero != pos 1`。

## 解读【解释】

身份：以下是 AI 解释，归因讨论见 CN-029。

1. **自查所得的修正**：C-47 的不停机还依赖一个当时没有写出的前提 P-rev，即“沿同一条路走回来，就是逆路径 `sym p`”。C-50 表明，在 HoTT 之内，只要把往回走建模成另一条独立的路径，一个可逆的计数器（ℤ）就能数出来回，停机过程也会停。所以 A6″ 的不停机成立于 P-rev 之下，不是对一切 HoTT 建模都成立。
2. **哪种 HoTT 建模都躲不开的一点**（C-49）：沿路径携带的任何变化，都能沿另一条路径撤销。由此：
   - 不可逆的计数（ℕ 上的 `suc`）不能是任何路径的运输，见 (d)；
   - 只增不减的随身读数必然不变，见 (b)；
   - 两段都计数时，去程的逆就成了一次让步数减少的“反向行走”，见 (e)；在 C-50 中，它就是读数为 −1 的 `sym go`。
3. **两难**：若把每条路径都读作一次行走（P-proc），则要么往回走就是去程的逆，计步器永不前进（C-47）；要么往回走是另一条路，过程会停，但理论里同时有一次从东到西、步数为 −1 的行走（C-50）。若只承认一部分路径是真实的行走，就要在路径结构之外另加一个挑选；而运输机制不尊重这个挑选（C-49 (a)）。
4. **有向模型**（C-51）：
   - 两段行走都是箭头，箭头没有逆；
   - 计步器是 ℕ 上不可逆的计数，每次行走按其步数增加，停机过程在燃料 1 时停。
   - (f) 显示，C-50 的出路在真实行走上与有向模型完全一致；HoTT 多出来的，恰恰是那些逆。
5. **通往 TT_□ 的桥（来源，未重放）**：
   - Gratzer–Weinberger–Buchholtz（arXiv:2407.09146，经 sciverse 全文 §6.2，第 29 页）的定理 6.13（有向单价性）说：`mor2fun : (𝕀 → S) → Σ A B : S, A → B` 是等价。
   - 定义 6.14 与引理 6.15 给出 `Gl(A, B, f) : 𝕀 → S`，其 `coe` 为 `f`。所以在 TT_□（附加 GWB 的公理）中，`Gl(ℕ, ℕ, suc)` 是离散类型宇宙 S 中一支运输作用为 `suc` 的箭头。
   - 对照 C-49 (d) 的 `noSucPath`：在带单价性的 HoTT 中，宇宙里没有任何路径作用为 `suc`。

## 禁止外推

- C-51 是关于一个**模型**（自由范畴，即有向类型论预期的范畴语义：类型为范畴，协变族为函子）的命题。它不是某个有向类型论内部的定理，也不是对 GWB 的重放。
- 不说 HoTT 不能数步数：C-50 用 ℤ 数出了来回，C-47 (c) 用列表数出了步数。
- C-49 讲的是**沿路径的运输**（`subst`），不涉及作为数据的编码（列表、台账）。
- C-50 的“代价”是形式事实（`antiWalk` 等）；说它是“非现实”，是解释，身份见 CN-029。
- “步行”“路”“计步器”“停下”是解释标签，不说明任何物理事实。
- 数学内容是标准事实（群胚律、运输、自由范畴），**不主张原创**。
