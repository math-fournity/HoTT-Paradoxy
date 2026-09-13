# HoTT 专题：来源、审计与纠错后的形式化核心

本目录是当前 HoTT–Z 研究的唯一活动入口。历史 AI 文本保留原貌，但不作为当前数学真值；当前
结论由审计报告、主张矩阵和机器证据共同限定。

## 当前持续研究主题

[Theory Schema](THEORY_SCHEMA.md)（v0.2，2026-09-09）提供固定一手版本的理论地图：核心规则、
派生数学、语义/相干性、跨呈现计算、扩展/元理论分界、时间审查接口及来源覆盖。用于核对被审视的理论，不替代用户
原文和 Z 研究目标；结构覆盖不等于所有定理、变体或悖论已经证明。

通透论述入口：[HoTT 研究三问：找什么、怎么找、凭什么](HoTT研究三问-找什么-怎么找-凭什么-20260909.md)
（2026-09-09）。用于理解研究主线、时间与准入问题、候选证据链及哲学/数学依据的区别；不取代
下列 current owners，不代表具体 HoTT 悖论已经证明。

第一顺位是“Z 铁律下的 HoTT 现实相对时间悖论”：不是优先寻找 `HoTT ⊢ ⊥`，而是寻找合法 HoTT
推演在被解释为现实过程、结论或现象时产生的非现实性。根表达是：有效现实前提 `T` 被理论
否定或删除后，对 `T` 本质敏感的推演效应必改变，因而现实完整过程—结论—现象谱 `X` 与理论谱
`Y` 分岔；命题—判定集合只是二值特例。`Z_LAW_REALITY_RELATIVE_PARADOXES.md`
拥有研究目标、计算合法性、用户参照悖论和候选排序；`INTRINSIC_TEMPORALITY_OF_HOTT.md` 拥有
具体演算的对象时间、弱操作时间、强内生时态与变体比较。当前第一候选为“同函数异时”，最重要
开放目标为 Guard-Erasure 的 HoTT 特定 forgetful translation。R-011 中“希望由 HoTT 结果支持一般
抽象结论”的任务经 R-012、R-014 最终定性为：`Z_STRONG_PHILOSOPHICAL_LAW` 就是“理论抽象必然
导致悖论”；技术非因子化／潜势／显现分层服务于证明和找实例，不能降低最高判断。HoTT 的任务
是严格发现一个尤其涉及时间否定的具体悖论。当前同函数异时和 Guard-Erasure 都仍只是优先候选。

Russell 是当前时间构造的中心校准器：把 `S` 的自成员资格写成阶段程序得到
`rₙ₊₁=¬rₙ`，构造反复拿入／拿出而不落定；合法 validator 应在成员／真值计算前拒绝形成，朴素
无限制集合本体的失败是把未落定 specification 先提升成完成集合。相关研究必须采用
`USER_MATH_PHILOSOPHY_FIRST / EVIDENCE_CRITICAL`：先在用户数学哲学内部完整重建，再分列
标准／外部比较，不能让 LLM 训练 prior 预先覆盖问题，也不能把用户主张当免证定理。

朴素集合论的最高定性是：它妄图用静态集合／关系抹掉现实形成时间，把可描述性、可构造性和
存在性合一。用户深切怀疑 HoTT 受到同一无时间化认知惯性／路径依赖支配；该怀疑须检查具体
formation、identity、judgmental equality、univalence/funext 的 stage/settlement/trace 擦除，当前
仍是 active hypothesis，不是已证结论。

## 相关 Session 的强制读取顺序

凡涉及 HoTT、时间维度、Z 铁律、抽象、悖论、芝诺、圆环、Russell 或自指，未来 AI 必须：

1. 先读 `sources/user-originals/Better-Best悖论-原文.md`；
2. 再读 `sources/user-originals/Z铁律-抽象-圆环-时间维度-用户原始论述-20260901.md`；
3. 读 `../认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md`：
   Z 最终强律、朴素集合论的时间否定、Russell／说谎者／Better Best 程序族、HoTT 认知惯性怀疑、
   技术核心、证据、冲突、未知和当前 Verdict；它不能替代原文或 owner；
4. 按问题读 `sources/user-originals/matrix-book-paradoxes/` CURRENT INDEX 中对应的独立逐字原文；
5. 读 `Z_LAW_REALITY_RELATIVE_PARADOXES.md`：当前目标、规范定义、候选和禁区；
6. 读 `INTRINSIC_TEMPORALITY_OF_HOTT.md`：具体 HoTT 变体的时间结构；
7. 读 `CLAIM_EVIDENCE_MATRIX.md`：当前主张证据边界；
8. 若要恢复过去讨论或声称“旧文档没有/已经全覆盖”，先查询
   `sources/aistudio-discussions/` 的 CURRENT manifest/INDEX，再回到源行区间；
9. 按问题选择 `USER_CORE_DOUBT.md`、`SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md` 或
   `AUDIT_AND_RECONSTRUCTION.md`；
10. 声称实现/验证时再读 `verification/VERIFICATION_REPORT.md` 和形式化源；
11. 来源谱系与旧 WBS 分别读 `SOURCE_REGISTRY.md`、`WBS_AUDIT.md`。

原文是用户原意和研究方法的一手来源，不是数学证明；AI 摘要不得替代原文。没有完成上述最小
读取，不得扩写论文、工作包或宏大判决。

## 目录地图

| 路径 | 身份 | 用途 |
|---|---|---|
| `sources/aistudio-docs/` | `HISTORICAL_SOURCE` | 从 `aistudio-docs` 迁入的 16 份原始 AI 文档；内容可能错误 |
| `sources/aistudio-discussions/` | `MACHINE_MANAGED_DERIVED` | 从全部归档生成的高召回逐字 HoTT 讨论视图；含问答、章节和无标题正文，不能当数学真值 |
| `sources/user-originals/` | `USER_PRIMARY_SOURCE` | Better Best 及本轮用户对 Z 铁律、圆环、时间和交接的逐字原文；先于 AI 解释读取 |
| `sources/user-originals/matrix-book-paradoxes/` | `USER_PRIMARY_SOURCE_DERIVED_VERBATIM_VIEW` | 《宇宙编程学》第三版全文、84 张图和 10 份悖论/解答链独立原文；原作主张不自动升级 |
| `../认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md` | `AUDITABLE_COGNITIVE_CLOSURE` | 当前 successor；Z 最终强律、时间否定、朴素集合论、HoTT 认知惯性怀疑、证据和可执行边界；不替代 current owners |
| `ChatGPT-🌟 Z铁律论证HoTT缺乏时间维度-完整提取-20260831-1745.md` | `USER_PROVIDED_TRAJECTORY` | 用户与另一 AI 的完整对话；用于重建意图和论证演化 |
| `formal/` | `CURRENT_IMPLEMENTATION` | 数学证明源码的权威根；当前 17 个 proof package 覆盖 Lean 通用因子化、原生 Cubical Agda 边界族和固定 agda-unimath C-05 外部重放；新结论按 topic/claim 保存，不以 `/tmp` 或聊天代码替代 |
| `verification/` | `CURRENT_EVIDENCE` | 来源发现与形式化验证；`runs/` 保存全部 final/superseded/失败 run。当前矩阵为 17 个 current package + 3 legacy proof 行、C-01–C-148；每个 run 只支持其精确命题与导入闭包 |
| `USER_CORE_DOUBT.md` | `ACCEPTED_USER-INTENT_INTERPRETATION` | 用户核心怀疑的当前哲学解释；不替代数学审计 |
| `Z_LAW_REALITY_RELATIVE_PARADOXES.md` | `ACTIVE_CANONICAL_RESEARCH_OWNER` | Z 铁律、计算合法性、现实相对悖论、同函数异时和 Guard-Erasure 当前目标 |
| `SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md` | `CURRENT_HISTORICAL_RECOVERY` | “直指/自指”、self-metatheory 和反射支线的来源与技术裁决 |
| `INTRINSIC_TEMPORALITY_OF_HOTT.md` | `ACTIVE_CANONICAL_RESEARCH_OWNER` | “研究时间”与“理论自身工作时间”的分层和变体比较 |
| `AUDIT_AND_RECONSTRUCTION.md` | `CURRENT_TRUTH_OWNER` | 当前研究结论和开放边界 |

外部只读证据快照位于 `/Volumes/D/ALL-Markdown/HOTT_Z_AI_HANDOFF_20260831`；其他 AI 整理的证明
位于 `/Volumes/D/ALL-Markdown/proofs`；整理过程文档位于 `/Volumes/D/ALL-Markdown/dev-docs`。

## 当前一句话结论

当前 **17 个冻结 proof package** 在各自固定命题、工具链和 run 范围内形成机器证据，并由 `verification/PROOF_VERSION_CLOSURE.json` 绑定到 exact commit `d3dfb0e…`；其后 `later_packages` 追加登记了 `MP-VERIFICATION-EVENT-001`（外部来源、项目内重放，C-149–C-156）与 `MP-ERCF3-T3-JOINT-001`（T3 编码层联合递归，C-157–C-159），当前 package 总数为 19、claims 为 90 + 11。当前状态为 `MACHINE_PROVED_VERSION_CLOSED`（冻结部分），C-05 为 scoped external replay。上表 frozen claim 行仍保留 run 建立时的 local-uncommitted 文本，以维持 index-row manifests；Git 维度由追加登记解释。它们没有建立 E6 自然消费者、现实桥梁、`NATURAL_USAGE_MISMATCH` 或 HoTT 内部矛盾。当前研究首选仍是下游入口（门 A/门 B：可对象化规格或同层自我担保消费者）；**T3 编码层义务已闭合**，下一义务是证明谓词表示性、反射与对角不动点（ERCF-3 保持 `GATED`）。

## 快速验证

```bash
bash HoTT/verification/discover_sources.sh

python3 HoTT/tools/hott_discussion_corpus.py stats
python3 HoTT/tools/hott_discussion_corpus.py query --topic time_process --limit 20
python3 HoTT/tools/hott_discussion_corpus.py validate

AGDA=/path/to/agda-2.8.0 \
AGDA_UNIMATH_ROOT=/path/to/agda-unimath-at-88cfce0ce195ae3b64a9e73e8ec744ae64b4006b \
LEAN=/path/to/lean \
bash HoTT/formal/build.sh

python3 -B scripts/audit/verify_math_proof_delivery_governance.py
python3 -B scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/20260912-MP-ERCF-001-02 --rerun
python3 -B scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/20260912-MP-ERCF-TRUNC-001-01 --rerun
python3 -B scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/20260913-MP-NOCANONICAL-001-02 --rerun
python3 -B scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/20260913-MP-UNIMATH-NOSECTION-REPLAY-02 --rerun
python3 -B scripts/audit/scan_agda_unimath_e6.py
```

本机验证状态为 `VERIFIED_LOCAL_WITH_SCOPE`。没有独立专家复核或外部干净环境收据，因此不得标为
同行评审完成或发表就绪。

新的当前 AI 数学结论还受根 `AGENTS.md` 的 `MATH_PROOF_BEFORE_DELIVERY_V1` 约束：证明源码位于 `formal/`，运行原件位于 `verification/runs/`，唯一 claim/proof/run 快速索引位于 `CLAIM_EVIDENCE_MATRIX.md`。无法完成相称机器证明时只能保留为问题、猜想、启发、纸笔候选或未重放来源，不得交付为已成立结论。
