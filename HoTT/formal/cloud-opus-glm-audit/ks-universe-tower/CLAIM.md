# KS 宇宙塔一般 n 重放：第 n 个宇宙不是 n-型（COPUS-KS-C01–C05）

> 编号约定：本文的 C-63、C-67、C-71、C-72、C-75、C-76 指 Opus CG-001 目标内索引的 `CG001-C-NN`（`.claude/goals/CG-001-targeted-overview/证据索引.md`），不是 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 其它节里同号的 claim。

> 2026-09-27；Claude Code 云端会话（Cloud-Opus），受用户委托执行 `GLM-5.3-Flash/审计请求/20260927-委托工作单-审计修正补完交付最终卷宗.md` §4（一般 n 外归纳）。入口：`Cloud-Opus审计并补完GLM/README.md`。
> - proof id：`MP-COPUS-KS-TOWER-001`（`KSUniverseTower.agda`）；负控制 `MP-COPUS-KS-TOWER-NEG-001`（`KSNegTrivialBase.agda`）、`MP-COPUS-KS-TOWER-NEG-002`（`KSNegOvershoot.agda`）。
> - 工具链：Agda v2.8.0（Linux x86-64 release 资产）+ cubical v0.9（与冻结记录逐字节一致），`--safe --cubical --guardedness`，无公设。记录：`../TOOLCHAIN.linux-x86_64.json`。
> - 来源：Kraus–Sattler, *Higher Homotopies in a Hierarchy of Univalent Universes*, arXiv:1311.4002v3（2015-03-27），ACM TOCL 16(2)；2026-09-27 经 ar5iv 读 §5 全文与 §6。

## 1. 命题（逐字形式命题 ↔ 读法）

| claim | 形式命题（Agda，逐字） | 读法（数学事实） |
|---|---|---|
| COPUS-KS-C01 | `KS-Theorem-5-9 : (n : ℕ) → ¬ isOfHLevel (2 + n) (Type (lvl n))`，其中 `lvl zero = ℓ-zero`，`lvl (suc n) = ℓ-suc (lvl n)` | 对每个 n，第 n 个宇宙 U_n 不是 n-型（h-level n+2）。KS Thm 5.9。 |
| COPUS-KS-C02 | `workOrderForm : (n : ℕ) → ¬ isOfHLevel (n + 2) (Type (iterSuc n ℓ-zero))`，`iterSuc zero ℓ = ℓ`，`iterSuc (suc n) ℓ = iterSuc n (ℓ-suc ℓ)` | 工作单 §4 的目标命题原样。 |
| COPUS-KS-C03 | `KS-Theorem-5-10-U≤ : (n : ℕ) → isOfHLevel (3 + n) (T (lvl n) n) × (¬ isOfHLevel (2 + n) (T (lvl n) n))`，`T L k = TypeOfHLevel L (2 + k)` | U_n 中 n-型组成的子宇宙恰是 (n+1)-型、不是 n-型（严格 (n+1)-型）。KS Thm 5.10。 |
| COPUS-KS-C04 | `KS-Theorem-5-10-Loop : (n : ℕ) → isOfHLevel (3 + n) (Loop (lvl n) n) × (¬ isOfHLevel (2 + n) (Loop (lvl n) n))` | KS 的 Loop_n 是严格 (n+1)-型。KS Thm 5.10。 |
| COPUS-KS-C05 | `step : (L : Level) (k : ℕ) → NT L k → NT (ℓ-suc L) (suc k)`，`NT L k = Σ[ W ∈ T L k ] Σ[ q ∈ typ (P L k W) ] ¬ (q ≡ pt (P L k W))`，`P L k X = (Ω^ (suc k)) (T L k , X)` | KS Lemma 5.8 的归纳步，推广到**任意**宇宙层 L 与**任意**截断指标 k：若 L 层的 k-型子宇宙有非平凡 (k+1)-环，则上一层的 (k+1)-型子宇宙有非平凡 (k+2)-环（见证点就是 KS 的 (Loop, h)）。 |

实例锚点（同文件）：`instance-n0 : ¬ isSet (Type ℓ-zero)`（= C-63 的命题）、`instance-n1 : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero))`（= GLM-R3-C01 的命题）、`instance-n2 : ¬ isOfHLevel 4 (Type (ℓ-suc (ℓ-suc ℓ-zero)))`（新）。

**终局轮追加（2026-09-27）**：`CatalogOfSetsTwoSteps.agda`（proof id `MP-COPUS-KS-TOWER-002`，另一文件，导入本包，不改本包源码）。

| claim | 形式命题（Agda，逐字） | 读法（数学事实） |
|---|---|---|
| COPUS-KS-C06 | `catalogOfSetsTwoSteps : isOfHLevel 3 (hSet ℓ-zero) × (¬ isSet (hSet ℓ-zero))`，证明为 `KS-Theorem-5-10-U≤ 0` | 装着一切集合的目录是群胚、不是集合：KS Thm 5.10 在 n = 0 的实例（`T (lvl 0) 0` 按定义即 `TypeOfHLevel ℓ-zero 2` = `hSet ℓ-zero`）。终局判词的邻近对照"两步就停"。运行 `20260927-COPUS-KS-CATALOG-OF-SETS-01`；负控制 `KSNegCatalogOfSetsIsSet.agda`（`MP-COPUS-KS-TOWER-NEG-003`，运行 `-NEG-01`：把 3 层读成 2 层，类型检查阶段 `[UnequalTerms]` 被拒）。 |

## 2. 与 KS 原文逐项对照

| KS | 本文件 | 说明 |
|---|---|---|
| Lemma 4.5（Ω 与 Σ• 交换） | `ΩΣ≃∙` | 带点等价；KS 在其设定下为判断性等式，cubical 中为库的 `ΣPathIsoPathΣ`（逆映射定义性保点） |
| Lemma 4.7（Ω 与 Π• 交换） | `ΩΠpt`、`Ω^Πpt` | 取自 Opus C-75 包 |
| Lemma 5.1（截断 Σ 分量被 Ω^n 中和） | `ΩΣtrunc` | 对 h-level 做归纳，完全按 KS 的证明链 |
| Lemma 5.2（local-global） | `localGlobal∙` | C-75 包 `localGlobal` 的**带点**版本（非平凡性经带点等价传递必需） |
| Lemma 5.4（⇒） | `hLevelΩ^` | 取自 C-75 包 |
| Lemma 5.5 | `hT`（库 `isOfHLevelTypeOfHLevel`） | |
| Cor 5.6（P_n 是集合族） | `isSetP`（经 `isOfHLevelΩ^`） | |
| Lemma 5.7（Loop 是 (n+1)-截断） | `hLoop` | |
| Lemma 5.8（非平凡元素） | `base`、`step`、`tower` | ξ := λ(X,q).(q,d_q)：m=0 时 d_q 是 q⁻¹·q·q = q 的方块（`D`，取自 GLM 包），m≥1 时由 `ΩΣtrunc` 以集合纤维典范给出；非平凡性由归纳假设在单点 (W, q̃) 处传播（`nt'`） |
| Thm 5.9 | `KS-Theorem-5-9`、`workOrderForm` | |
| Thm 5.10 | `KS-Theorem-5-10-U≤`、`KS-Theorem-5-10-Loop` | |

与 KS 的差异（均为形式化层面，不改数学内容）：① 归纳步对 (L, k) 一般化，塔是其 (lvl n, n) 实例；② local-global 与 Lemma 5.1 都以**带点等价**实现，以便"非平凡"可以沿等价传递；③ Loop₋₁ = 2 的基例写作 hSet₀ 中 (Bool, isSetBool) 处 ua notEquiv 的提升。

## 3. 机器证据

- 主运行：`HoTT/verification/runs/20260927-COPUS-KS-UNIVERSE-TOWER-01/`（exit 0 为预期）。
- 负控制：`-NEG-01`（平凡基环：同一非平凡性脚本作用于 refl，须被拒，理由 `false != true`）；`-NEG-02`（越级：用同一证书求"U_n 不是 (n+1)-型"，须被拒，理由 `NT (lvl n) n ≠ NT (lvl n) (suc n)`）。
- HIT 状态：名称级闭包无 HIT（`../hitscan/CertKS.agda`，claim COPUS-R1-C05；workOrderForm 闭包 364 名，数据类型仅 I、ℕ、⊥、Bool，公理叶子仅 cubical 内建 6 项）。注意：**导入闭包**含 35 个 `Cubical.HITs.*` 模块（经 `Cubical.Homotopy.Loopspace` 等），它们未进入任何被使用的名字。

## 4. 禁止外推

- 这是 **Kraus–Sattler 2015 的已知定理**在本仓库的机器重放，不是新数学定理；新增的只是：本仓库内的 cubical 一般 n 形式化、(L,k) 一般化的归纳步、名称级 HIT-free 机器证书。
- 不证明任何**固定**宇宙（如 Type₀）没有 h-level，也不证明无 HIT 时 Type₀ 不是群胚：KS §6 认为"每个 U_n 中的类型都是 n-截断"应当是相容的（原文：no published proof；模型草图），故无 HIT 时"U_n 是 (n+1)-型"不可反驳（按 KS 的相容性论断，【来源转述】）。
- `(n : ℕ) → …` 在 Agda 中是 Setω 中的单个内部命题（宇宙层依赖 n）；在书式 HoTT 中它只能作为对数字 n 的元层模式（外归纳）陈述。
- "永不停机""无限追溯""宇宙塔在任何有限层都落不定"等读法是**解释层**，不是本文件的形式命题；精确桥接见卷宗 `Cloud-Opus审计并补完GLM/07-悖论卷宗-最终完整版（D4）.md`。
- 工具链是 v2.8.0 的 Linux 资产（与冻结记录的 macOS 二进制不是同一文件）；cubical 逐字节一致。
