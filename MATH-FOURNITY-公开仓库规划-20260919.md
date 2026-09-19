# MATH-FOURNITY 公开仓库规划方案（2026-09-19）

> 任务（用户指令）：`/Users/aurolafly/MATH-FOURNITY` 为未来推送 GitHub 的公开 repo
> （中文为主 + 法语/英语双 README），以 git repo 形式公开。本文件 = 本地工作成果
> 调查 + 内容规划方案。**本轮不向 MATH-FOURNITY 放任何东西。**

## 0. 目标 repo 现状（实测）

- 已初始化：git repo，1 个 initial commit；**LICENSE = MIT**（已选定）；
  README.md = 占位（`# MATH-FOURNITY` / `四弹一体`）——名字含义已由占位确认。
- 公开动作 = 本项目 G3 闸门时刻（push 需用户明确授权，方案不改变该纪律）。

## 0.5 交付原则（用户裁定，2026-09-19，最高优先级）

> **交付结果，不交付过程。** 用户与 AI 的讨论内容（含用户早期不够精确、后被
> 精化的表述）只有真正作为**结果**的部分才进入 MATH-FOURNITY；不浪费读者时间。
> 本原则直接裁定 §5/§8 的全部待决项（见各表「结果原则裁定」列）。



| 资产类 | 数量/规模 | 状态 | 公开适配度 |
|---|---|---|---|
| 形式化模块（.agda） | 20 个（dedekind-omega-missile 全家族） | 10 核心收据 canonical-green；全部可 `compile.sh` 复现 | **核心收录** |
| 运行收据（runs/） | 91 个 run 目录（9.4MB） | 10 个 `--rerun` 双重验证逐位一致 | **核心收录**（至少 10 核心；可选全量） |
| 证据索引 | `CLAIM_EVIDENCE_MATRIX.md`（844 行） | 判词分级 + 禁止外推四栏 | **核心收录**（需按 B3 基准清洗措辞） |
| 发射包文档 | CLAIM-PACKAGE ×6（GOLD/M2/M3/M3-UNC/REAL-LAYER/总包） | 含 Book 逐字引用（短引文+出处） | **收录**（引文注明 CC BY-SA 出处） |
| 方案/学说链 | 修订片 30 片（022–030 为四弹线） | 含治理内部语汇 | **选录**（030 收官判定 + 029 + 027 学说节，改写为公开语体） |
| 对话档案 | 四弹讨论完整档案（13 分片，三会话闭环） | dev-notes 0032–0035 的产物 | **待裁定**（用户个人科研叙事，含大量内部语汇；建议精编附录或暂缓） |
| dev-notes | 67 篇 | 会话工作日志 | **不收录**（工作日志性质；精选结论已进矩阵/修订片） |
| 四件套（核心认知等） | 4 个逻辑文档 | 用户悖论/元数学原文权威 | **待裁定**（用户一手思想，公开=重大决定；建议：不放或仅放授权节选） |
| 理论上游快照 | HoTT Book 源码（book-578b85cc） | **CC BY-SA 3.0** | **不整树收录**（与 MIT 混装有许可证冲突；以短引文+出处方式引用即可） |
| 治理内部 | `.codex`（218MB）/ STATE / checklist / 审计 map | 项目内部治理 | **不收录**（审计 map 可清洗后收录） |
| 私有数据 | private-audit（74MB）/ AI对话录（17MB 嵌套 repo）/ trajectory | 原始轨迹 | **绝不收录** |

**可在公开 repo 中如实主张的全部数学内容**（判词分级已保守到收据级）：
10 个机器收据（过程层/声明层/识别层/金形态四条件/ℝ层充裕性/反弹消毒/必要性-经典侧/
stuckness 三族）+ B0 精确收费命题 + 诚实开放表（B1b′ CONJECTURE / B2 QUESTION /
Huber SOURCE_REPORTED / 币种不确定）。

## 2. 定位（一句话 + 边界）

**MATH-FOURNITY = "理论-引擎对齐"（theory-engine alignment）的形式化研究包：
以 Cubical Agda 为引擎，对 HoTT Book §11.2 实数层的经典理想元素逐项开出收费单，
并附每个命题的机器收据与诚实分级。**（"四弹一体"= 四层调查结构：过程层→声明层→
识别层→元层，作为内部方法论名保留在中文 README 的方法论节。）

**边界（B3 判词基准，写进三语 README 的显著位置）**：
1. 不出现"击落 HoTT / HoTT 被推翻/HoTT 不一致"作数学主张；
2. 最高强度措辞 =「非现实性机械锚定 + 逼选结构」；
3. 收费表述保留币种不确定性（"某种原则必付" ≠ "SingleOmega 必付"）；
4. 三个等级（CONJECTURE/QUESTION/SOURCE_REPORTED）不得升格。

## 3. 目录结构方案

```
MATH-FOURNITY/
├── README.md            # 中文主入口（见 §4）
├── README.en.md         # English mirror
├── README.fr.md         # Miroir français
├── LICENSE              # MIT（已定）
├── CITATION.cff         # 引用元数据（作者身份待用户定）
├── formal/              # 全部 .agda 模块 + compile.sh + AGDA_LIBRARIES + TOOLCHAIN.json
│   └── …                #   （20 模块；含 ReboundDisarm / NecessityLEM / CutRealLayer 等）
├── receipts/            # 10 个核心 run 收据（RUN.json + 五件套 + index manifest）
│   └── …                #   目录名保留 2026xxxx-MP-… 原名（可追溯）
├── evidence/
│   ├── CLAIM-MATRIX.md  # 清洗后的证据矩阵（B3 基准版）
│   └── claim-packages/  # 6 个 CLAIM-PACKAGE（Book 引文加 CC BY-SA 出处标注）
├── docs/
│   ├── overview-zh.md   # 四层调查综述：只写定稿结论（含被精化后的最终表述，不引对话过程）
│   ├── charge-statement.md  # B0 精确收费命题 + B1a 充裕性定理说明
│   ├── open-problems.md # 诚实开放表（CONJECTURE/QUESTION/SOURCE_REPORTED）
│   └── methodology.md   # 判词分级语义 + 逐实例证书记分牌方法论（作为结果陈述）
├── .github/workflows/
│   └── replay.yml       # CI：下载钉死工具链→重放 10 核心 run→逐位比对（见 §6）
└── paper/               # （Phase 3）公开稿工作目录
```

## 4. 三 README 方案

**README.md（中文，主入口）大纲**：
1. 这是什么：一句话定位 + 一页地图（四层调查 × 10 收据的表）；
2. 核心结果速览：三个机器定理（`sufficiency`：SingleOmega→ℝLayerAt；
   `M3-L1-unc`：读出≠算出；`LEM→Necessity`：必要性=纯构造性问题）+ 金形态四条件
   + 消毒收据；
3. 判词分级表：MACHINE_PROVED / CONJECTURE / QUESTION / SOURCE_REPORTED 的语义
   与当前记分牌；
4. 复现指南：`compile.sh` 一键重放 + CI 状态徽章；
5. **边界声明**（B3 四条，显著位置）；
6. 引用与致谢（HoTT Book CC BY-SA 3.0 短引文说明；Huber 结果 = SOURCE_REPORTED）；
7. 开放问题列表（邀请同行参与 B1b′/模型论证）。

**README.en.md / README.fr.md**：结构镜像；法语版含数学术语对照表
（dépassement non réaliste / obligation d'achèvement / élément idéal classique 等
术语的定名，Phase 2 由双语审校完成）。

## 5. 收录/排除清单（筛查表）

| 项 | 决定 | 理由 |
|---|---|---|
| formal 模块 + compile 工具链 | ✅ 全收 | 复现的根基；8.1MB 无隐私 |
| 10 核心 run 收据 | ✅ 全收 | 每张收据自带重放 argv；91 全量含历史失败 run（M1-01..03 等），建议 Phase 1 先收 10 核心 + 失败轨迹说明，Phase 2 视需求补全量 |
| CLAIM 矩阵 + 发射包 | ✅ 收（清洗） | 矩阵中"击落/导弹"战争语汇按 B3 改写为四层调查语体 |
| 修订片 022–030 | ⚠️ 只取结果 | 其**定稿结论**（四层结构/收费定位/拒签≠自毁/病灶在 Ω/现实同一性属判词层）并入 docs/overview；作为过程的讨论与治理语汇不出现 |
| 四弹讨论档案（13 分片） | ❌ 不收（结果原则） | 过程非结果：用户-AI 讨论全程、含被精化的早期不精确表述，读者无需也不应消费 |
| 四件套（核心认知等） | ❌ 不收（结果原则） | 原始输入/思想草稿；其被精化后的结论已作为结果进入 docs/ |
| HoTT Book 源码快照 | ❌ 不收 | CC BY-SA 3.0 与 MIT 混装风险；短引文（CLAIM-PACKAGE 内）已符合引用规范并注明出处 |
| .codex / STATE / checklist / 审计交接包 | ❌ 不收 | 内部治理；FOUR-MISSILES-AUDIT-MAP 可清洗为 `docs/verification-map.md` 收录 |
| private-audit / AI对话录 / 全部 trajectory | ❌ 绝不收 | 原始轨迹含完整上下文 |
| dev-notes 67 篇 | ❌ 不收（结果原则） | 过程日志；结论已被结果层吸收 |
| 失败 run 轨迹（M1-01..03 等 81 个非核心 run） | ❌ 不收（结果原则） | 迭代过程；收据范围定为 **10 核心**（一句话说明迭代历史即可，不搬失败工件） |

## 6. CI 重放方案（公开 repo 的杀手锏）

收据的确定性设计使 GitHub Actions 可全自动复现：workflow 拉取钉死的
Agda 2.8.0-3d04bac + cubical v0.9（TOOLCHAIN.json 内含 publisher SHA-256），
按各 RUN.json 的 `command_argv` 重放 10 核心 run，exit/stdout/stderr 与收据
**逐位比对**——README 挂徽章：*"Every machine-checked claim on this page
replays bit-for-bit in CI."* 这一条同时就是 G2 外部审计的机器部分自动化。

## 7. 分阶段路线

| 阶段 | 内容 | 前置 |
|---|---|---|
| Phase 0 | 本方案（已交付）+ 用户裁定开放决策点 | — |
| Phase 1 | 资产清洗导出：formal/ + receipts×10 + 矩阵 B3 版 + 发射包标注；筛查表逐项过 | 用户裁定 §5 两个 ❓ + §8 决策点 |
| Phase 2 | 三语 README + docs/ 四件（只写定稿结论）+ CI replay workflow | Phase 1 |
| Phase 3 | paper/ 公开稿（对应 C1+C2：写稿+文献对冲） | Phase 2 |
| Phase 4 | push（= G3 授权时刻）；建议同时放 G2 外部审计进场 | 用户 |

## 8. 开放决策点（需要用户裁定）

1. ~~作者/署名~~ **已裁定**：Math Manify <mathmanify@protonmail.com>（仓库级 git 配置已钉定，2026-09-19）。
2. ~~四弹讨论档案~~ **已裁定（结果原则）**：不收。
3. ~~四件套~~ **已裁定（结果原则）**：不收。
4. ~~收据范围~~ **已裁定（结果原则）**：10 核心；失败轨迹不搬。
5. repo 一句话描述（GitHub About）：建议
   "Machine-checked charge statements for classical ideal elements in HoTT's
   real-number layer — a theory-engine alignment study (Cubical Agda)"，中文主。
6. 是否在 Phase 4 同步开启 Issues/Discussions（同行评审入口）。

## 9. 与本项目闸门的关系

- Phase 4 的 push = G3 授权执行；建议 G2（外部审计）在 push 前进场（材料已备，
  §6 的 CI 会替代其机器部分的大部分）。
- 公开稿完成前，B3 三方对照空集状态维持；README 即首个"公开稿级"文本，
  完成时执行 B3 对照并落盘。
