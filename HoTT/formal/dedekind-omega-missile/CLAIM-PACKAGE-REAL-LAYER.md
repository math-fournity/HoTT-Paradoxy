# CLAIM-PACKAGE-REAL-LAYER（B0 陈述精确化 + B1a 充裕性证明）

> claim id : `CAND-F2-7-REAL-LAYER`（candidate；`registers_new_claim:false`——本包钉死命题形态、登记可行性裁定并证明 (a) 方向，不交付 (b′) 未证主张）
> proof id : `MP-DEDEKIND-OMEGA-REAL-LAYER`（**statement + B1a 证明阶段**：`CutRealLayer.agda` 过核 `AGDA_EXIT=0`；(a) 充裕性 `sufficiency` 已证（run `-02`），run `-01` 的源 hash 因 §3-E 两项勘误过期；**(b) / (b′) 尚无证明**）
> 任务来源：修订片 029 §4.1（第一前置任务：陈述精确化，不可跳过）。
> 验收仪器：`HoTT/verification/REMEDIATION-CHECKLIST-20260918.md` 的 B0 / B1a 行。

---

## §1 Book §11.2 逐字原文

来源：`HoTT/theory-schema/upstream/book-578b85cc/reals.tex`（HoTT Book, §11.2 Dedekind reals）。
以下为**逐字转写**（LaTeX 源码原文，未改写、未翻译、未摘要）。

### 1.1「单一命题类型 Ω」的四种取法（收费位置的自陈）

> We might naively translate the informal definition into type theory by saying that a cut
> is a pair of maps $L, U : \Q \to \prop$. But we saw in \cref{subsec:prop-subsets} that
> $\prop$ is an ambiguous notation for $\prop_{\UU_i}$ where~$\UU_i$ is a universe. Once we
> use a particular $\UU_i$ to define cuts, the type of reals will reside in the next
> universe $\UU_{i+1}$, a property of reals two levels higher in $\UU_{i+2}$, a property of
> subsets of reals in $\UU_{i+3}$, etc. In principle we should be able to keep track of the
> universe levels, especially with the help of a proof assistant, but doing so here would
> just burden us with bureaucracy that we prefer to avoid. We shall therefore make a
> simplifying assumption that a single type of propositions $\Omega$ is sufficient for all
> our purposes.
>
> In fact, the construction of the Dedekind reals is quite resilient to logical
> manipulations. There are several ways in which we can make sense of using a single type
> $\Omega$:
>
> 1. We could identify $\Omega$ with the ambiguous $\prop$ and track all the universes
>    that appear in definitions and constructions.
>
> 2. We could assume the propositional resizing axiom, as in \cref{subsec:prop-subsets},
>    which essentially collapses the $\prop_{\UU_i}$'s to the lowest level, which we call $\Omega$.
>
> 3. A classical mathematician who is not interested in the intricacies of type-theoretic
>    universes or computation may simply assume the law of excluded middle for
>    mere propositions so that $\Omega \jdeq \bool$. This not only eradicates questions about
>    levels of $\prop$, but also turns everything we do into the standard classical
>    construction of real numbers.
>
> 4. On the other end of the spectrum one might ask for a minimal requirement that makes
>    the constructions work. The condition that a mere predicate be a Dedekind cut is
>    expressible using only conjunctions, disjunctions, and existential quantifiers over~$\Q$,
>    which is a countable set. Thus we could take $\Omega$ to be the initial \emph{$\sigma$-frame},
>    i.e., a lattice with countable joins in which binary meets distribute over countable
>    joins. (The initial $\sigma$-frame cannot be the two-point lattice $\bool$ because
>    $\bool$ is not closed under countable joins, unless we assume excluded middle.) This
>    would lead to a construction of~$\Omega$ as a higher inductive-inductive type, but one
>    experiment of this kind in \cref{sec:cauchy-reals} is enough.
>
> In all of the above cases $\Omega$ is a set.

**层级事实（本包的核心）**：Book 自陈「the type of reals will reside in the next universe
$\UU_{i+1}$」（取法 1 = 层级追踪，免费但上升），而「single type of propositions $\Omega$」的
低层化（取法 2 = resizing；取法 3 = LEM 使 Ω≡Bool；取法 4 = 初始 σ-frame）是**付费/构造**动作。

### 1.2 Defn 11.2.1 四条件（逐字）

> A \emph{Dedekind cut} consists of a pair $(L, U)$ of mere predicates $L : \Q \to \Omega$ and
> $U : \Q \to \Omega$ which is:
>
> 1. \emph{inhabited (i.e., bounded):} $\exis{q : \Q} L(q)$ and $\exis{r : \Q} U(r)$,
> 2. \emph{rounded:} for all $q, r : \Q$,
>    $L(q) \Leftrightarrow \exis{r : \Q} (q < r) \land L(r)$ and
>    $U(r) \Leftrightarrow \exis{q : \Q} (q < r) \land U(q)$,
> 3. \emph{disjoint:} $\lnot (L(q) \land U(q))$ for all $q : \Q$,
> 4. \emph{located:} $(q < r) \Rightarrow L(q) \lor U(r)$ for all $q, r : \Q$.
>
> We let $\dcut(L, U)$ denote the conjunction of these conditions. The type of
> \emph{Dedekind reals} is $\RD \defeq \setof{ (L, U) : (\Q \to \Omega) \times (\Q \to \Omega) | \dcut(L,U)}$.
>
> It is apparent that $\dcut(L, U)$ is a mere proposition, and since $\Q \to \Omega$ is a
> set the Dedekind reals form a set too.

**注意**：CutGoldForm 的 disjoint 用了更强的工作形态 `L q → U r → q < r`（蕴含 located 的
强化版），与本处的 `¬ (L(q) ∧ U(q))` 不冲突（强形态蕴含弱形态）；金形态的 rounded 是双向
（⇔），与本处一致。四条件的**命题内容**在 ℚ 层全部可构造（GOLD-02 收据）。

---

## §2 精确命题（`CutRealLayer.agda` 的逐项对照）

| Book §11.2 原文 | `CutRealLayer.agda` 中的精确形态 | 宇宙层级 |
|---|---|---|
| 「a pair of maps $L, U : \Q \to \Omega$」+「$\Omega$ is a set」+ 各 inhabitant 是 mere proposition | `ΩOf ℓ = hProp ℓ`；`isSetHProp : isSet (hProp ℓ)`（库） | `ΩOf ℓ : Type (ℓ-suc ℓ)` |
| 取法 2（propositional resizing axiom） | `PropResizing ℓ = (A : Type (ℓ-suc ℓ)) → isProp A → Σ[ B ∈ Type ℓ ] (isProp B × (A ≃ B))` | `Type (ℓ-suc (ℓ-suc ℓ))` |
| 取法 3（LEM for mere propositions，Ω ≡ Bool） | `LEMProp ℓ = (A : Type (ℓ-suc ℓ)) → isProp A → A ⊎ (¬ A)` | `Type (ℓ-suc (ℓ-suc ℓ))` |
| 「a single type of propositions $\Omega$ is sufficient」+「collapses the $\prop_{\UU_i}$'s to the lowest level」 | `SingleOmega ℓ = Σ[ Ω ∈ Type ℓ ] (isSet Ω × (Ω ≃ hProp ℓ))` | `Type (ℓ-suc ℓ)` |
| Defn 11.2.1 四条件（$\dcut$） | `dcut L U` = inhabited×2 × rounded×2 × disjoint × located，量词全部显式 | `Type ℓ` |
| 「the type of Dedekind reals $\RD$」+「the Dedekind reals form a set」 | `DedekindReals ℓ = Σ[ LU ∈ (ℚ → ΩOf ℓ) × (ℚ → ΩOf ℓ) ] dcut (fst LU) (snd LU)` | `Type (ℓ-suc ℓ)` |
| 「the type of reals will reside in the next universe $\UU_{i+1}$」= 收费位置的精确化 | `ℝLayerAt ℓ = Σ[ R ∈ Type ℓ ] (isSet R × (R ≃ DedekindReals ℓ))` —— **实数作为基层级 ℓ 上已完成的集合对象** | `Type (ℓ-suc ℓ)` |

**免费层 vs 收费层（不可漂移）**：
- **免费（ℚ 层）**：`DedekindReals ℓ` 对**每个**层级 ℓ 都是一个 set（Book 自陈；因为
  `hProp ℓ` 是 set、`ℚ` 是 set、`dcut` 是 mere proposition）。代价只是对象活在 `ℓ-suc ℓ`。
  这与 M3-UNC 的「ℚ 层免费」、GOLD-02 的「四条件全部可构造无假设」一致。
- **收费（ℝ 层）**：`ℝLayerAt ℓ₀` 要求把 `DedekindReals ℓ₀`（活在 `ℓ-suc ℓ₀`）塌缩到
  基层级 `ℓ₀`。这正是「把 cut 取等价类、把 ℝ 取值命题塌缩到单一 Ω 的下一升格」。

---

## §3 (b′) 路径 1 的可行性裁定（本包的关键结论）

029 §4.1 第 2 步要求判断「(b′) 走路径 1（反向蕴含 `ℝ层陈述 → 某形式 LEM/resizing`）是否可能」。

**裁定：直接形态被 Book 自身证伪；精确目标必须收窄，且收窄后仍需独立证明。理由：**

1. **「⇒ LEM 或 resizing」是假命题**：Book §11.2 §1.1 取法 4 明确给出第三条出路——
   把 Ω 取为**初始 σ-frame**（higher inductive-inductive type）。这是一条既非 LEM、
   也非 propositional resizing 的构造路线。故「ℝ 层成立 ⇒ LEM 或 resizing」的
   直接反向蕴含不可能成立（Book 自身提供了反例路线）。
2. **正确的必要性目标**：`ℝLayerAt ℓ₀` 至少要求「基层级 ℓ₀ 上存在与 `hProp ℓ₀`
   等价的 set」，即 `SingleOmega ℓ₀`。`CutRealLayer.agda` 因此把 `Necessity ℓ`
   声明为 `ℝLayerAt ℓ → SingleOmega ℓ`（而非 `→ PropResizing ℓ ⊎ LEMProp ℓ`）。
3. **`SingleOmega ℓ₀` 与 `PropResizing` 的关系需要独立论证**：`SingleOmega ℓ₀`
   直觉上等价于「`hProp ℓ₀` 本质小」，这与 `PropResizing` 的形态高度接近但**不等同**
   （前者只塌缩 `hProp ℓ₀` 自身，后者塌缩所有 `ℓ-suc ℓ₀` 层 prop 到 `ℓ₀`）。
   这一等价（或蕴含方向）**尚未证明**。
4. **即使 `Necessity` 成立，也不给出「击落」**：`SingleOmega` 可能由
   初始 σ-frame 路线满足（取法 4），而那是一条**构造性**路线——「不可免费」的
   正确表述是「需要基层级命题塌缩结构（构造或公理）」，不是「必须接受 LEM/resizing 公理」。

**状态登记**：`(b′) 路径 1` = `CONJECTURE`（029 §2 降格条款生效）：
  - `Necessity ℓ` 的类型形态已钉死并过核；
  - 证明未做，且**不预设可行**；
  - 在证明出现前，绝不以「击落 / 不可免费 / 等价定理已证」交付。

---

## §3-E 勘误（2026-09-18，两项 B0 陈述修正 + B1a 完成）

B0 收据（run `20260918-MP-DEDEKIND-OMEGA-REAL-LAYER-01`，提交 `a7eeab4`）固定的源码
在后续工作（提交 `b9b2e8c` 起）中发生**两项陈述层修正**。两者均使 `-01` 的
`source-manifest.json` 源 hash 过期；修正后的全部陈述由 run
`20260918-MP-DEDEKIND-OMEGA-REAL-LAYER-02`（B1a 证明体全量重查）背书。

**勘误 1 · `dcut` 存在量词忠实化（命题截断）**。
Book §11.2 Defn 11.2.1 逐字原文的 `\exis` 在 HoTT 中是命题截断（`∥_∥₁`），而
B0 版 `dcut` 的 inhabited×2 / rounded×2 写成了裸 `Σ`。这不忠实，且对非平凡 cut
不可满足：向下封闭的 `L` 有无穷多 `r > q` 见证，裸 `Σ` 非 mere proposition，
却被 rounded 的 `≃`（props 之间的等价）强制为 prop。修正后六分量皆 mere
proposition 或 set（located 的 `L q ⊎ U r` 在 `q < r` 时可同时成立——`q < x < r`——
故是 set 而非 prop，用 `isSet⊎`），「Dedekind reals form a set」由 `isProp→isSet` /
`isSetΣ` 链得到（`isSetDCut`、`DedekindReals-isSet`）。

**勘误 2 · `Sufficiency` 付费假设深化（`PropResizing ℓ →` 改 `SingleOmega ℓ →`）**。
B0 版把 (a) 的付费假设定为 pointwise `PropResizing ℓ`。深化裁定：pointwise
resizing（搬单个 prop 到基层级）**不蕴含** `SingleOmega ℓ`（整个 `hProp ℓ` 塌缩到
ℓ 层的 set）；Book §11.2 取法 2 原文「assume the propositional resizing axiom …
which essentially collapses the $\prop_{\UU_i}$'s to the lowest level, which we
call $\Omega$」的忠实形态是「存在低层级 Ω」，即 `SingleOmega`。故充裕性的付费假设
收窄为 `SingleOmega ℓ`（与 (b′) 的 `Necessity` 目标对称）；`PropResizing` 保留为
公理候选登记，二者蕴含/等价方向**未论证**（遗留）。`Necessity` 侧不受影响（B0 时
已是 `ℝLayerAt ℓ → SingleOmega ℓ`）。本包 §4.1 的旧表述
「证明 `Sufficiency ℓ = PropResizing ℓ → ℝLayerAt ℓ`」自本节起废止。

**B1a 完成（同一 run `-02`）**：`sufficiency : (ℓ : Level) → SingleOmega ℓ →
ℝLayerAt ℓ` 已过核（`--safe --cubical`，exit 0，无 postulate）。构造：代理空间
`DedekindReals*`（Ω*-值 cut 的子集型，纤维经 `e` 逐点搬运后取 `dcut`）活在 ℓ 层、
是 set、且 `≃ DedekindReals ℓ`。跨层（`Type ℓ` ↔ `Type (ℓ-suc ℓ)`）的 Σ-cong
由自克隆 `Σ-cong-iso-fst-cross` 承担（库版 `Σ-cong-iso-fst` / `Σ-cong-equiv-fst`
经 private variable 块把 `A A'` 钉同层，实测报 `UnequalLevel`；`isoToEquiv` 本身
跨层，`ProbeCrossIso.agda` 探针验证）。证明形态为「付费假设作为显式前提的构造性
蕴含」，偏离 checklist 原计划的 postulate 形态（`AXIOM_CHARGED`）——属**加强**：
无公理注入，(a) 是纯 cubical Agda 定理。

---

## §4 后续（B1 执行规格，按 029 §4 顺序；2026-09-18 B1a 完成后修订）

1. ~~**B1a（充裕性）**~~ **DONE（2026-09-18，run `-02`）**：实际证明形态
   `sufficiency : (ℓ : Level) → SingleOmega ℓ → ℝLayerAt ℓ`（付费假设为显式
   前提而非 postulate，见 §3-E 勘误 2 与 B1a 段）。
2. **B1b（诊断绕过）**：**DONE（2026-09-18，混合结局如实登记，修订片 030 §2）**——
   零付费读法败：直接构造撞尺码墙（`Ω : Type ℓ₀` 具 hProp 全能力即 `SingleOmega`
   本身）；σ-frame（取法 4）是换靶（σ-frame-值 cut 的另一套实数，非钉死的
   `DedekindReals`）+ 新费（HIT-II 与「初始 σ-frame ≃ hProp」比较义务）。换币读法
   原则上存在：Cauchy 实数免费活在 `Type₀`，但 `≃ DedekindReals` 需可数选择类
   原则（元层引述未机械化）。结局 = 「某种原则必付」的必要性证据 +
   「SingleOmega 型收费必付」的负结果（币种不确定）。
3. **B1b′（必要性）**：**DONE（降格收口，修订片 030 §3）**——`Necessity ℓ =
   ℝLayerAt ℓ → SingleOmega ℓ` 正式确认 `CONJECTURE`：路径 1 失败（0/1-cut 编码
   的 locatedness 在 `0≤q<r≤1` 窗口强制 `P ∨ ¬P`）；路径 2 缺模型
   （`HoTT+CC+¬SingleOmega` 模型存在性未论证，若成立则不可证且可能不可反驳）；
   LEM 下后件免费（取法 3 逐字）⇒ 必要性问题纯属构造性片段。

---

## §5 边界（不漂移）

- `registers_new_claim:false`——本包是陈述精确化、可行性裁定与 (a) 方向证明，非新数学主张。
- **不声称**：HoTT 不一致；等价定理已证；resizing/LEM 必要性已证；ℝ 层完备性已证。
- **B1a 证明的只是「付费即得」（(a) 充裕性）**，不是「必付费」——收费位置判词
  （不可免费 / 击落）在 (b′) `Necessity` 证明出现前不得升级为 `MACHINE_PROVED`。
- **确认**：ℚ 层四条件已机器证明（GOLD-02，`EXACT_EXIT_STDOUT_STDERR_MATCH`）；
  (a) 充裕性已机器证明（run `-02`）；`CutRealLayer.agda` 的全部陈述被 Cubical Agda
  内核接受为类型。
- `SingleOmega` 与 `PropResizing` 的蕴含/等价方向未论证（§3-E 勘误 2 遗留）。
- 前提判定全部 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`；外部追溯审计（角色 D）是用户闸门。
