# CLAIM-PACKAGE-REAL-LAYER（B0 · 陈述精确化）

> claim id : `CAND-F2-7-REAL-LAYER`（candidate；`registers_new_claim:false`——本包只钉死命题形态并登记可行性裁定，不交付已证主张）
> proof id : `MP-DEDEKIND-OMEGA-REAL-LAYER`（**statement 阶段**：`CutRealLayer.agda` 过核 `AGDA_EXIT=0`，全部声明被编译器接受为类型；**尚无 Sufficiency / Necessity 的证明**）
> 任务来源：修订片 029 §4.1（第一前置任务：陈述精确化，不可跳过）。
> 验收仪器：`HoTT/verification/REMEDIATION-CHECKLIST-20260918.md` 的 B0 行。

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

## §4 后续（B1 执行规格，按 029 §4 顺序）

1. **B1a（充裕性）**：证明 `Sufficiency ℓ = PropResizing ℓ → ℝLayerAt ℓ`
   （`compile.sh CutRealLayer.agda` 补 `Sufficiency` 的构造子；run + 矩阵行）。
   预期形态：由 `PropResizing ℓ` 取 `Ω := Σ[ B ∈ Type ℓ ] ...` 的小型化代理，
   把 `DedekindReals ℓ` 的 carrier 塌缩到 `ℓ` 层。**不预设可行，逐段编译。**
2. **B1b（诊断绕过）**：朴素构造性尝试（不走 resizing/LEM 直接做出 `ℝLayerAt ℓ₀`），
   **如实报告结局**：成 → 登记负结果（本攻击方向失效）；败 → 必要性证据（非证明）。
3. **B1b′（必要性）**：按 §3 的收窄目标尝试 `Necessity ℓ`；不成则维持 `CONJECTURE`。

---

## §5 边界（不漂移）

- `registers_new_claim:false`——本包是陈述精确化与可行性裁定，非新数学主张。
- **不声称**：HoTT 不一致；等价定理已证；resizing/LEM 必要性已证；ℝ 层完备性已证。
- **确认**：ℚ 层四条件已机器证明（GOLD-02，`EXACT_EXIT_STDOUT_STDERR_MATCH`）；
  `CutRealLayer.agda` 的全部陈述被 Cubical Agda 内核接受为类型（`AGDA_EXIT=0`）。
- 前提判定全部 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`；外部追溯审计（角色 D）是用户闸门。
- 收费位置的判词不得在 (b′) 证明出现前升级为 `MACHINE_PROVED`。
