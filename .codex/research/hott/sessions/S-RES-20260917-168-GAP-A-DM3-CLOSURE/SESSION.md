# S-RES-20260917-168-GAP-A-DM3-CLOSURE

身份：PREMISE-001 step-5 **缺口 A 闭合单元（DM3 分支）**——修订片 018 §3(A) 登记的
缺口 A 在 DM3 分支上的闭合；修订片 019（commit `7984892`）验收收据化；
修订片 020（commit `221936a`）自我审计合同的**首次执行**。
角色：AI 全自动执行（修订片 009/017）+ 强制审计层；外部 AI 追溯审计为终局复核。
**不邀请用户介入；本项目禁止启动任何 Sub Agent**（用户 2026-09-17 裁定，commit `679a016`）。

## 本单元产出

1. **文法冻结**（`machine-overview/grammars/v2-dm3-a-v1.json`，引擎 `776e6b7`）：
   backend `v2-dm3`；DM3 = 标准非布尔 De Morgan 三元链 `0<a<1`，`~a=a`，故 `a∧¬a=a≠0`；
   值 `ret(n,b,dm3,level)` 四轴，55 ground；op = `supply(d)` / `fill` / `tower(level)` /
   `between(a,b)`。**缺口 A 的 DM3 分支**= 把 V2 的 availability / level / density 三结构轴
   重新解释到 DM3 上，使分离可由原生核在非布尔 De Morgan 代数上确认。
2. **SEARCH run `SEARCH-GAP-A-DM3-001`**（引擎 `776e6b7`）：40 contexts × 1,404 等价对
   = **56,160 pair-context checks**，`complete_within_declared_grammar=true`、
   `grammar_violations=0`、**remainder=0**、双种子 `order_independent=true`；**9,720** 原始分离
   → **396** 规范归约见证（availability 1,944 / density 2,592 / level 5,184）；
   校准 `ALL_PRESENT`（WV-A-availability / WV-L-level / WV-D-density 全部出现且
   `all_match=true`，两个同值控制正确判不分离）。
3. **越界（作用域化，011/012）**：**392/392** 作用域内见证被 **8 个既有文法**
   （7 delay + 1 点集 V2）全拒，**族内拒因唯一**（delay：`UNKNOWN_OP:supply` 216 / `tower` 104 /
   `between` 72；点集：`VALUE_OUT_OF_DECLARED_RANGE:left` 312 / `:right` 80）；跨族拒因不同
   （不可解析 op vs 不可表示 DM3 坐标），故 `scoped_all_reasons_unique=false`
   ——**更强**而非更弱。4 条 level-ingress 如实登记（共享 `tower` 机制，L1 不可见但点集可复现，
   不计入越界分母）。
4. **非嵌入 omission 检查**：16³ = **4,096** 候选函数穷举，保 meet 与 neg 的
   DM3→点集面格嵌入 = **0**（`model_exhaustive_negative_check`，作用域 = 两个被声明的有限结构，
   **不是**关于区间 I 的命题）。
5. **四路原生核校验全部 `KERNEL_FOUR_WAY_PASS`**（`v2_dm3_verify.py`，引擎 `776e6b7`；
   mirror `formal/V2DM3.agda`，Cubical Agda 2.8.0 + cubical v0.9）：
   `VERIFY-GAP-A-DM3-WV-0230`（availability）/ `-WV-0041`（level）/ `-WV-0158`（density）/
   `-WV-0001`（level 第四见证）——verify KERNEL_ACCEPTED exit 0 / controls ACCEPTED /
   negative-control KERNEL_REJECTED_AS_EXPECTED **exit 42** / verify-replay
   `EXACT_EXIT_STDOUT_STDERR_MATCH`；`cross_check`（`DENOMINATOR_SINGLE_SOURCE`）在任何
   kernel 运行前先重算并断言；每个 RUN.json 含 `model_dependency_audit` / `oracle_scope` /
   `key_adjudication_audit_trail`。
6. **判词 `DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT`**（`interval_i_confirmed=false`）。
   **核心新事实 = BLI 单元 `VERIFY-GAP-A-DM3-BLI-001`（`KERNEL_BLI_PASS`）：布尔律
   `x ∧ ¬x = 0` 对三个结构性分离非必需**——density 分离在 DM3 中成立，同时
   `dm3Meet da (dm3Neg da) = da ≠ d0`，二者皆经核确认。这是**否定性**机械事实，
   作用域 = `formal/V2DM3.agda` 定义的 DM3；falsifier = kernel ACCEPT `BLIFalsify.agda`。
7. **判词分级**（015 §5 强制披露的执行；018 §4 排序教训的首次正面应用）：
   availability / level 从 `POINT_SET_MIRROR_MODEL_KERNEL_CONFIRMED` 升级为**解释无关结构层**；
   **density 分裂**——DM3 实例被核确认，但链序**仍是模型层**（DM3 是 I 的一个模型，不是 I）。
8. **修订片 019**（commit `7984892`）：验收收据化 + 判词分级 + 「缺口」与「单元」
   分开记账 + 本单元 reflection。
9. **修订片 020**（commit `221936a`）+ **AGENTS「禁止 Sub Agent」**（commit `679a016`）：
   自我审计升级为分片化论证合同（核心认知 46 条五元组 / 扩展认知 8 片逐段落 / 航向复盘 /
   偏航裁决），并禁止任何 Sub Agent。
10. **第一份 020 合同审计集**（本 session 目录 `CORE_COGNITION_AUDIT.md` 索引 + 8 分片）：
    核心认知 46 条 = 对齐 11+1 双层 / 深化 6 / 张力 6 / 未触及 11；扩展认知 8 片 32 个小节判断；
    **分片 008 裁决首次改变下一单元的选择**（改道至 SUPPLY-010，见下）。
11. **校验器升级**（commit `02a6b4a`）：`cognition_runtime.validate_session_bundle`
    支持 020 分片合同——索引为 v2 时 KC 条目从分片按表顺序收集（小节式标题，合并条目计多条）、
    覆盖校验改为精确集合、relation 从 `- relation:` 提取并校验、条目至少 4 条子弹、
    缺片 fail-closed；必填字段正则容许加粗；v1 单文件审计向后兼容（S-167 仍 PASS）。
    负控制：缺片 / 坏关系 / 破坏覆盖 / 薄条目 / 缺字段全部 fail-closed。

## 分片 008 裁决（本审计对队列的实质变更）

下一单元序列**经审计改道**：(1) 区间 I 设计探针（不变；措辞修正——探针的两种结论都是
正面信息，「不可写」是表达界限的正面结论，不是失败）；(2) **SUPPLY-010 知识谱反观 +
现实对齐断裂供给单元**（改道自原指针 V2-G-c，后者降级为回退）——目标 = F2 缺口层 7 个
来源在手、分母零条的层（PAT / LEM / resizing / AC / unique choice / 截断时机判据 /
Dedekind-Ω）；(3) EXP-001 并入 (1) 收尾；(4) B 侧新族登记为长期节点，先设计 B 侧机械判据；
(5) 缺口 B 不阻塞。理由：分片 007 复盘判据一表明 167/168 已现**同形重复**（分母内干净负结论
不能继续替代发现），方向 5 是唯一能改变发现侧零产出状态且成本最低的动作。

## 纪律

- **不是数学结论**（F-011 / `MATH_PROOF_BEFORE_DELIVERY_V1`）：本单元验收的是缺口 A 的
  **DM3 分支**闭合，不是「该前提非现实」的证明，也不是关于真实区间 I 的结论。
  `registers_new_claim:false`，不进 `HoTT/CLAIM_EVIDENCE_MATRIX.md`；唯一登记 = 布尔律非必需
  这一否定性机械事实，作用域 = DM3。
- **不是「引擎自主发现了新方向」**：任务族与文法由 AI 冻结供给（003 §5 角色纪律）；
  LLM 的模式匹配只准在供给层使用，判断层一律由原生核承担（KC-000007 / KC-000017 张力的执行解）。
- **作用域边界**：`interval_i_confirmed=false` 全程成立——I 的相等不可判定，无法写返回 Bool
  的 `separates`；DM3 结果是否提升回真实区间 I **仍开放**，登记为下一单元（设计探针）。
  越界机械检查覆盖 8 个既有文法；12 个 symbolic-horn 为 schema 级 `BACKEND_MISMATCH` 未跑
  （缺口 B，不阻塞）。
- **`DENOMINATOR_SINGLE_SOURCE`（016）**：所有期望字面量由 `v2_dm3*.py` 计算，
  与产生 search run 的同一 canonical 来源；`cross_check` 在任何 kernel 运行前先重算并断言。
- **017 全面自动化纪律第三次完整跑通**（门槛 / 作用域化 / 判词分级 / 非嵌入 omission /
  分片审计 / checkpoint），无 `AUTOMATION_BLOCKED_EVIDENCE_GAP`，证据标准一字未改；
  审计改道队列这一动作本身也留痕（分片 008 + 本 SESSION + STATE NEXT 段）。
- **禁止 Sub Agent**：本单元全部工作由主 Agent 独立完成；无 spawn、无提案、无等待。
- Git：引擎 `776e6b7`；主 repo `1378363`（交付物）；`7984892`
  （修订片 019）；`221936a`（修订片 020）；`679a016`（AGENTS）；`02a6b4a`（校验器）；
  本 checkpoint revision 167->168。不 push、不 tag。
