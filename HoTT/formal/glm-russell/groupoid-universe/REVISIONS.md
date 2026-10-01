# groupoid-universe 包修订记录（M1c 探索史与落地）

## 2026-09-27：修订三（Cloud-Opus 审计，审计者写入；不改下文任何一句）

> 依据：委托工作单 `GLM-5.3-Flash/审计请求/20260927-委托工作单-审计修正补完交付最终卷宗.md` §3（R1、R2、Q7）与 §6 写入权限。审计全文：`Cloud-Opus审计并补完GLM/02-断裂审计-逐命题（D1）.md` §2.6、`03-R1-HIT依赖闭包判定.md`、`04-Q7-数学终审逐行核验.md`、`05-R2至R8处置.md` R2。

**形式层不变**【数学事实】：`¬universeIsGroupoid : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero))` 在 Linux 复现中被内核接受（运行 `20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-01`）；Q7 逐行终审把每个中间步骤带显式类型重述并由内核接受（COPUS-Q7-C01，运行 `20260927-COPUS-GLM-REPAIR-Q7-01`），无空洞、无方向错误。

1. **措辞更正一是过度更正，撤回；恢复"KS 定理 5.9 在 n = 1 情形的忠实 cubical 重放"。** 对照 KS 原文（arXiv:1311.4002v3 §5）：Lemma 5.8 的归纳步定义 ξ := λ(X,q).(q, d_q)，m = 0 时 d_q 的类型是 q_*(q) = q，写成 q⁻¹·q·q 即可见其有居民；n = 0 的"归纳假设"就是 2 上的 swap 及其不等于 refl 的论证。本包逐项对应：`D` = d_q，`FAM` = ξ，`(c₀ , τ)` + `τ≠refl` = 基例的非平凡元素，`forceEquivLoop` = 定理 5.9 的"would be propositional"。所以"非平凡性机制不同（具体对合 + uaβ + 集合压平，非 IH 传播）"不成立——在 n = 1 情形，KS 的 IH 本身就是一个具体对合加 uaβ 式的非平凡性论证。真正的差别只有两处：基环取 Bool×Bool 上的对合 `a`，而不是 2 上的 swap；local-global 只用了所需的一个方向。

2. **措辞更正二（"一般 n 是否可均匀化未知"）已解决。** 一般 n 已机器证明：`KS-Theorem-5-9 : (n : ℕ) → ¬ isOfHLevel (2 + n) (Type (lvl n))` 与工作单原式 `workOrderForm : (n : ℕ) → ¬ isOfHLevel (n + 2) (Type (iterSuc n ℓ-zero))`（COPUS-KS-C01/C02，`HoTT/formal/cloud-opus-glm-audit/ks-universe-tower/`，运行 `20260927-COPUS-KS-UNIVERSE-TOWER-01`）。本包的机制可以均匀化：通用归纳步 `step : NT L k → NT (ℓ-suc L) (suc k)` 用的正是本包的 `D`（m = 0 时）与 ξ 族，外加带点的 local-global（`localGlobal∙`）和 KS Lemma 5.1（`ΩΣtrunc`）；`instance-n1 = KS-Theorem-5-9 1` 与本包定理是同一命题。

3. **边界声明中"HIT-free……未进入本证明的任何构造"现有名称级机器证书。** `¬universeIsGroupoid` 的名称级依赖闭包 251 名，无 HIT；数据类型只有 `I、ℕ、⊥、Bool`，公理叶子只有 cubical 内建的 `1=1、IsOne、inS、Sub、Level、PathP`（COPUS-R1-C01，运行 `20260927-COPUS-HITSCAN-CERT-GLM-01`）。原边界声明对导入闭包含 PropositionalTruncation 模块的说明是如实的。

4. **负控制 `WrongGroupoidWitness.agda` 没有检验它声称检验的东西。** 该文件只导入 `Cubical.Foundations.Prelude` 与 `a`，`true` 不在作用域；Agda 在**作用域检查**阶段报 `[NotInScope] true` 并以 42 退出，从未进入类型检查。GLM 自己的收据 `20260926-GLM-GROUPOID-UNIVERSE-NEG-01/stdout.txt` 末尾就是这条错误，但 RUN.json 写 `KERNEL_REJECTED_AS_EXPECTED`，工作日志写"负控制（exit 42，正确理由拒绝）"——两处均不成立。修复：
   - `HoTT/formal/cloud-opus-glm-audit/glm-repairs/GroupoidNegFixed.agda`：补上 `true/false` 的导入，同一断言 `a (true , true) ≡ (true , true)` 被类型检查器以 `false != true` 拒绝（运行 `20260927-COPUS-GLM-REPAIR-NEG-01`）；
   - 近失控制 `GroupoidNegTrivialLoop.agda`：同一 τ≠refl 脚本作用于恒等等价给出的平凡环，被以 `true != false` 拒绝（运行 `20260927-COPUS-GLM-REPAIR-NEG-02`），说明证明确实依赖 `a` 的非平凡性。
   Linux 复现 `20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-NEG-01` 如实记为 `REJECTED_BEFORE_TYPE_CHECKING`。

5. **收据**：GLM 原收据哈希锁定，不改。原 `source-manifest.json` 不是 canonical schema（无工具链二进制与 cubical 树的外部依赖行）；canonical 形式的复现见上列运行，由 `Cloud-Opus审计并补完GLM/tools/verify_copus_run.py --rerun` 逐字节重放核验（结果：`Cloud-Opus审计并补完GLM/11-收据核验结果.json`）。

6. **引用本包时的标准措辞**：Type₁ 不是群胚（KS 定理 5.9 在 n = 1 的忠实 cubical 重放，基环取 Bool×Bool 上的对合；名称级闭包无 HIT，COPUS-R1-C01）；一般 n 见 COPUS-KS-C01/C02。

## 2026-09-27 凌晨：M1c 单元 2+3 落地（GLM-R3-C01 机器证明）

**`¬universeIsGroupoid : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero))` 编译通过**（运行 `20260926-GLM-GROUPOID-UNIVERSE-01` exit 0；负控制 exit 42 按预期拒绝）。

**关键突破（对上节侦察的三案之外的第四条路）**：
1. **边界实验更正了一个整晚的错误假设**：`PathP (λ i → r i ≡ r i) r r` 对抽象 r **完全合式**（cubical 的 PathP 边界检查接受环路端点；此前判"不合式"是错的——这正是库的 `ΣPathP` 能存在的原因）。
2. **自滑动方块的构造**：`D q := compPathL→PathP (纯路径代数 sym q ∙ q ∙ q ≡ q)`——用库的 `PathP→compPath`-族引理（Cubical.Foundations.Path:372），一切命题性，零定义性墙。
3. **KS ξ-族**：`FAM (b , q) := ΣPathP (q , D q)`——每个点自带环路数据成为该点处的环路。
4. **总装**：等值环 `loopE := equivEq (funExt FAML)`；群胚假设经 `univalence` 传递压平它；双层 `cong (cong ·)` 求值/投影到具体点 `(c₀ , τ)`；τ ≠ refl 由 `uaβ` + `a (tt,tt) = (ff,tt)` 的可计算差异给出（负控制正是它）。

**边界声明**：HIT-free 指证明的导入与构造不使用任何 HIT 类型；cubical 库的传递接口图（`--ignore-interfaces` 全量重检时）包含 `Cubical.HITs.*` 模块（如 PropositionalTruncation），属库基础设施，未进入本证明的任何构造。**（2026-09-27 措辞更正一）**RUN.json scope 中 "KS … n=1 instance, **replayed**" 应读作 "KS 策略 n=1 实例的**简化实现**"：种子形状（自指 Σ 构件）与 KS 相同，但非平凡性机制不同——KS 经归纳假设在单点传播（ξ 族 + IH），本包用具体对合 + uaβ + 集合压平。收据文件哈希锁定不改，以本条为准。**（措辞更正二）**"一般 n 的推广路径同时明朗"过于乐观：本包机制对一般 n 是否可均匀化未知；一般 n 应按 KS 原结构（Loopₙ 塔 + U_n^{≤n} + IH 单点传播）另行实施。

## 2026-09-26 深夜（会话尾）：单元 2 的路线侦察——三条死路（已被第四条路取代，留档）

1. 死路 A（可判定族）：死于层级混淆（FAM(L): L≡L 是环路不是 L；与熄火定理一致）。
2. 死路 B（sym-映射）：死于"对称群元素恒共轭于其逆"。
3. 死路 C（ξ-族朴素呈现）：当时判为不合式——**此判断已被上述边界实验更正**；真正的问题是"如何构造"，答案见上（compPathL→PathP）。死路 C 的教训保留：KS 依赖的判断性 Ω-律在 cubical 为命题性，所以必须走库的 PathP↔复合引理而非 KS 的定义性链。
