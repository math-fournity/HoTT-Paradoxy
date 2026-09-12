# R018 来源

本轮是用户明确要求的外部观点验证，因此除附件及既有项目源外，核对了下列一手材料。网页取得的是本轮工具返回，不声称已经独立下载签名全部远端原件。

| 身份 | 来源 | 直接用途 |
|---|---|---|
| 被审输入 | `HoTT/sources/external-audits/HoTT.json` | 16 chunks；公开消息与真实Python执行；2段未执行Lean文本 |
| 项目固定HoTT Book | `HoTT/theory-schema/upstream/book-578b85cc/logic.tex` §3.7/§3.9 | 截断构造、消去与唯一选择两项输入条件 |
| 同上 | `basics.tex` 1740—1788 | 完整UA、命题性计算；不是只有Equiv→Eq的类型 |
| 同上 | `formal.tex` 984—1011 | 公理常量不自动引入新判断等式 |
| 同上 | `hits.tex` 1222—1238 | 商下降计算，不要求枚举等价类 |
| 先前R016 | `.codex/research/hott/sessions/S-ANS-20260910-016-AXIOMATIC-COMPUTATION/PROOF_NOTE.md` | 已有限定的非规范正常形与正向证书结果，非新内核认证 |
| HoTT Book 在线一手源 | https://github.com/HoTT/book/blob/master/logic.tex | 交叉核对unique choice和isProp含义 |
| Lean官方教程 | https://docs.lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/ | Prop中proof irrelevance及定义等同性 |
| Lean官方教程 | https://leanprover.github.io/theorem_proving_in_lean4/axioms_and_computation.html | #reduce/#eval、choice与noncomputable、Quot.lift |
| Mathlib官方API | https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Quot.html | Trunc.recOnSubsingleton、Trunc.out、unsafe Quot.unquot区分 |
| Mathlib官方API | https://leanprover-community.github.io/mathlib4_docs/Mathlib/Logic/Equiv/Defs.html | Equiv结构及其与普通Eq的区别 |
| CCHM原论文 | https://arxiv.org/abs/1611.02108 | Cubical Type Theory的单价性构造性解释；本轮摘要范围核对 |
| Huber原论文 | https://arxiv.org/abs/1607.04156 | 该cubical系统自然数规范性；本轮摘要范围核对，不泛化到所有变体 |
| Coquand–Huber–Sattler原论文 | https://arxiv.org/abs/1902.06572 | homotopy canonicity与judgmental canonicity的区别；摘要核对 |

本轮未分析PDF图表，未作OCR。不是全HoTT文献综述，也没有把历史规范性开放问题当作当前领域状态。

Lean访问尝试：环境未预装lean；zstandard模块缺失，随后官方Linux ZIP下载因DNS失败；container下载也失败。未安装系统依赖，未运行Lean。证据见LEAN_ACCESS_attempt1.json、LEAN_ACCESS.json。不能用本地Python检查替代Lean。
