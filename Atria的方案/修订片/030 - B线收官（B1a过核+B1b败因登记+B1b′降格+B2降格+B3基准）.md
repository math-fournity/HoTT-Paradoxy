<!-- governance-shard:v2
logical_id: ATRIA-MACHINE-OVERVIEW-PLAN-REVISION
shard_id: 030
index: ../修订片.md
-->

# B线收官（B1a过核+B1b败因登记+B1b′降格+B2降格+B3基准）

> 2026-09-18 晚（ZCode Session，用户指令「/goal 全部做完」）。本片执行 029 §2 的
> 「两个都要」合同的收官侧：主交付的 (a) 已过核，(b) 诊断绕过与 (b′) 必要性按
> 结局如实登记，B2/B3 按 028 修复清单收口。所有元层论断显式标注，不冒充内核证明。

## 0. 事实基线（本轮现场核验，HEAD `085ed2f` 起）

- **B1a 已过核**：`sufficiency : (ℓ : Level) → SingleOmega ℓ → ℝLayerAt ℓ`，
  run `20260918-MP-DEDEKIND-OMEGA-REAL-LAYER-02`（`PASS_WITH_SCOPE` +
  `EXACT_INDEX_SNAPSHOT_MATCH` + 双重 `--rerun` 逐位一致；无 postulate）。
- **B0 双勘误已登记**（dcut `∥_∥₁` 截断 + Sufficiency 假设 `PropResizing→SingleOmega`），
  见 `CLAIM-PACKAGE-REAL-LAYER.md §3-E` 与矩阵 REAL-LAYER 节头。
- **E1 核心重放收尾**：六核心收据（GOLD-02 / M2-01 / M3-01 / M3-UNC-01 / BP-01 /
  TA-01）全部 `--rerun` 通过（`EXACT_EXIT_STDOUT_STDERR_MATCH`）。GOLD-02 附带修复：
  fedd70e 写坏的 `index-row-manifest.json`（快照哈希错 + 身份字段缺）已按 RUN.json
  的 `index.sha256`（= fedd70e 版矩阵）重建；矩阵 GOLD 两节的历史行降格（-01 行
  改非身份前缀，-02 行为唯一 proof 身份行）。
- **PENDING_KERNEL 已核实为已完成**（9/17，`MissileThreeUnconditional.agda` +
  M3-UNC-01 `--rerun` 通过）：判定表无 LEM，`M3-L1-unc : ¬(Spec_A ≃ Spec_B)` 无条件。
- **金形态已完成**（GOLD-02 四条件完整 + 本轮 `--rerun`）：0026 交接时「金形态
  cut 未做」的记忆已过时。

## 1. B1a（充裕性）：MACHINE_PROVED_WITH_SCOPE —— 已收官

构造（代理空间 + 显式逐点 λ 载体 iso + 跨层自克隆 `Σ-cong-iso-fst-cross` +
`isoToEquiv`）与两项 B0 勘误的登记见 0026/dev-notes 与矩阵 REAL-LAYER 节，此处
不重复。**边界重申**：证明的是「付费即得」，不是「必付费」。

## 2. B1b（诊断绕过）：结局 = **零付费失败；换币付费存在**（混合结局，如实登记）

对「不用任何塌缩结构做出 `ℝLayerAt ℓ₀`」的三条朴素路线逐一考察（元层分析，
未机械化，标注 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`）：

1. **直接构造（失败）**：载体 `(ℚ → hProp ℓ₀)` 活在 `Type (ℓ-suc ℓ₀)`（宇宙算术，
   `CutRealLayer.agda` 内核可查）。任何使 cut 载体降到 ℓ₀ 的 `Ω : Type ℓ₀`
   若具 hProp 全能力即 `SingleOmega ℓ₀` 本身——免费路线恰是收费命题。
   **= 尺码墙，必要性证据。**
2. **σ-frame（Book 取法 4，换靶不免费）**：取 Ω := 初始 σ-frame（HIT-II）可构造性
   地得到一个 base 层 set，但那是 **σ-frame-值 cut 的另一套实数**，不是本线钉死的
   `DedekindReals`（Ω 固定为 `hProp ℓ`）；且「初始 σ-frame ≃ hProp」本身又是一句
   塌缩强度的话。Book 自陈该 HIT 实验一处即够（§11.2 取法 4 逐字，CLAIM-PACKAGE
   §1.1）。**= 换靶 + 新费（HIT-II 结构与比较义务），非绕过。**
3. **Cauchy（换币付费）**：Cauchy 实数 `ℝC`（ℚ-序列 + 集商）**免费**活在
   `Type₀`；但 `ℝLayerAt ℓ₀` 要求 `≃ DedekindReals ℓ₀`，而 Dedekind→Cauchy
   方向需从截断存在量词中反复提取具体有理数 = **可数选择（CC）类原则**（标准
   构造性事实，元层引述未机械化）。**= 付费存在，但币种是 CC 不是 resize。**

**结局登记（029 §2 合同执行）**：
- (b) 的零付费读法**失败** → 「某种原则必付」的必要性**证据（非证明）**，加强 (a)；
- (b) 的换币读法**原则上成功**（CC ⇒ `ℝLayerAt ℓ₀`，元层未机械化）→ 对
  「SingleOmega 型收费为必要」是**负结果**：收费存在但**不必然是 SingleOmega**。
- 与 M3-UNC 的先例同构：精确化会把「LEM 账单」改写成「某原则账单」（027 §5 预言
  的二次应验）。

## 3. B1b′（必要性）：路径 1 失败分析 + 路径 2 缺模型 + **路径 3 降格 `CONJECTURE`（执行 029 §2 硬条款）**

- **路径 1（反向蕴含）失败分析**（元层）：从 `R : Type ℓ` + `R ≃ DedekindReals ℓ`
  造 `Ω ≃ hProp ℓ` 的自然路线是把每个 `P : hProp ℓ` 编码为 0/1-cut 再拉回 R；
  该 cut 的 locatedness 在窗口 `0 ≤ q < r ≤ 1` 内要求 `L q ∨ U r`，恰好等价于
  判定 `P ∨ ¬P`——**LEM 恰在此处被需要**。从任意 R 无典范手段刻出 Ω。
- **观察一（Book 取法 3 逐字在库）**：LEM 下 `Ω ≡ Bool`（CLAIM-PACKAGE §1.1），
  即 `LEMProp ℓ → SingleOmega ℓ`（后件免费成立）⇒ 必要性问题**无经典内容**，
  全部重量在构造性片段。
- **观察二（CC 反例候选）**：若存在 `HoTT + CC + ¬SingleOmega` 的模型，则其中
  `ℝLayerAt` 真（§2 路线三）而后件假 ⇒ `Necessity` 在其中**假** ⇒ 不可证。
  该模型的存在性本轮**未论证**（元层 QUESTION；立方模型中 CC 与 resizing 的
  独立组合属文献级问题）。若成立，则 Necessity 既不可证也可能不可反驳——
  真值依赖模型。
- **观察三**：`SingleOmega ↔ PropResizing` 蕴含方向仍未论证（B0 深化遗留，开放）。
- **降格登记**：`Necessity ℓ = ℝLayerAt ℓ → SingleOmega ℓ` 维持并**正式确认**
  `CONJECTURE`（029 §2：「绝不允许把充裕性 (a) 冒充必要性 (b′)」；且本片 §2/§3
  表明该猜想真值本身可疑——「必付费」若真，其精确币种也未知）。

## 4. B2（靶 A「不可归约」）：对象层不可内证 → **矩阵显式 `QUESTION` 降格**

- `n-lem` 的定义是 `with (LEM ℕ) … | inl x = x`（inl 见证**任意**）。
  存在声模型族：`LEM ℕ ↦ inl zero` 使 `n-lem ≡ zero` 成立；`↦ inl (suc zero)`
  使其否成立（postulate 的解释自由）。**两个方向的等式都有支持模型 ⇒ 对象层
  「不可归约」命题（任一方向）都不可能内部证明**（可靠性论证，元层）。
- 已机械化的部分**不变**：语法层 canonicity 失败——闭 ℕ 项头部为公理应用、
  refl 被核拒绝、内核亲印卡住范式（TA/TA-AC/TA-LEM 系列收据，exit≠0 即收据）；
  Huber 完整结果维持 `SOURCE_REPORTED_NOT_REPLAYED`。
- `MissileFourChargeDemo.agda` 头注的预登记（「不给出不可归约的内部证明（那是
  元层性质）」）由本片**兑现为正式状态**：B2 以 `QUESTION` 收口，非 `CONJECTURE`
  （对象层命题在声模型下有真有假，不是稳定猜想，是「依赖解释的伪命题」——
  元层 canonicity 现象才是稳定表述）。

## 5. B3（范围诚实性）：**对照基准落盘；当前无公开稿文本（空集事实登记）**

- repo 内**不存在**公开稿标题/摘要文本（028 是修复方案非公开稿；文献 PDF 属
  sources）。三方对照（标题 ↔ 摘要 ↔ 矩阵判词）当前对「公开稿」一侧为**空集**，
  对照今日**平凡成立**且不冒充已做实质对照。
- **判词基准（公开稿产生时强制执行，写入 audit map §5）**：
  1. 标题/摘要不得出现「击落 HoTT / HoTT 不一致」作数学主张；
  2. 最高强度措辞 =「非现实性机械锚定 + 逼选结构（六个正向收据 + 三族负向探针）」；
  3. 「收费」表述必须保留币种不确定性（§2/§3：某种原则必付 ≠ SingleOmega 必付）；
  4. B1b′=CONJECTURE、B2=QUESTION、Huber=SOURCE_REPORTED 三等级不得升格。
- 公开稿产生之日重跑三方对照并落盘对照表（B3 从「基准就绪」转为「对照执行」）。

## 6. 四弹一体收官判定（兑现 9/17 登记的「028/027 增补」待办）

| 弹 | 机械层 | 元层遗留 |
|---|---|---|
| M1 过程层 | `M1-04` 收据 + 本轮 `--rerun` ✅ | — |
| M2 声明层 | `M2-01` 收据 + `--rerun` ✅ | — |
| M3 识别层 | `M3-01` + **`M3-UNC-01`（去 LEM 无条件版）** `--rerun` ✅ | — |
| BP 副产品 | `BP-01` `--rerun` ✅ | — |
| 第四弹·靶 A | TA 族负向探针（exit≠0 即收据）+ `TA-01` `--rerun` ✅ | B2=QUESTION（§4）；Huber `SOURCE_REPORTED` |
| 第四弹·靶 B | B0+B1a（`REAL-LAYER-02` 双 replay ✅）+ GOLD-02 四条件 `--rerun` ✅ | B1b′=CONJECTURE（§3）；币种不确定（§2） |

**收官判词**：四弹的**机械核全部成立并具最强重放证据**；攻击形态 = 构造式拒绝
证书 + 收费账单的精确化与部分机械化，非内部矛盾。语义边界与 027 §2/§8、
矩阵判词等级一致：不声称 HoTT 不一致；「击落」= 非现实性机械锚定。

## 7. 028 片状态更新

- 028 §1（第 0 层）：B1 分叉已由 029 裁定、B1a/B1b/B1b′ 由本片收官；B2 由本片
  §4 降格收口；B3 由本片 §5 基准落盘。028 的「不修完不能公开」清单中
  AI_SELF 可执行部分**全部非 OPEN**；剩余 G2（外部审计执行）、G3（push）为
  用户/外部闸门，G1（STATE checkpoint 裁定）为用户闸门。
- 028 §4 执行顺序中 B 线已走完（B0→B1a→B1b→B1b′降格）。

## 8. 边界（不漂移）

- 本片 §2/§3 的 CC、模型族、locatedness-LEM 论断全部为**元层分析**
  （`AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`），不是内核收据；不据此交付任何
  数学结论。
- `Necessity` 不升级；收费位置判词在 (b′) 证明出现前不得 `MACHINE_PROVED`；
  B2 的 QUESTION 不因探针收据升格。
- 不声称 HoTT 不一致；不声称等价定理已证；`registers_new_claim:false`。

## 未闭合项

- G2：外部追溯审计（角色 D）**实际执行**——材料已备（audit map 含本轮更新）。
- G3：push / VERSION_CLOSED——待用户授权。
- G1：STATE checkpoint 事务 S170–S176——待用户裁定（沿 170–176 模式不伪造）。
- B1b′ 真值（CONJECTURE）、B2 对象层命题（QUESTION）、`SingleOmega↔PropResizing`、
  δ 路线完备性（金形态 §5 缺口 9）、Huber 重放——维持各自等级，不自动重开。
