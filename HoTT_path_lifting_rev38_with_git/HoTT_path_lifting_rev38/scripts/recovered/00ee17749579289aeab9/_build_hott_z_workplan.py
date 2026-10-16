from __future__ import annotations
import json, os, re, hashlib, zipfile
from pathlib import Path
from datetime import datetime

ROOT = Path('/mnt/data')
DATE = '2026-08-31'

STATUS_VOCAB = {
    'BASELINED': '定义、边界或治理规则已经稳定，仍需维护',
    'PAPER_PROVED': '已有可审查的纸笔证明，尚未达到证明助理等级',
    'PAPER_PROVED_CONDITIONAL': '在明确假设下已有纸笔证明',
    'ACTIVE': '当前关键路径正在执行',
    'READY': '依赖已满足，可立即进入执行',
    'BLOCKED': '缺少必要定义、工具、证据或前置结果',
    'BACKGROUND': '作为已知背景或支撑，不作为原创主结果',
    'PARKED': '保留但不进入当前主线',
    'EXTERNAL_GATE': '需要独立专家或同行反馈才能关闭',
}

VERIFY_LEVELS = [
    ('V0', '思想/来源线索', '仅说明研究动机，不构成数学证据'),
    ('V1', '良构形式陈述', '量词、类型、目标语义和边界均已固定'),
    ('V2', '纸笔证明', '证明可逐步检查，已通过内部红队'),
    ('V3', '有限模型/程序核验', '用于错误探测；不得替代无界证明'),
    ('V4', '证明助理编译', '固定版本、源码、命令、退出码和日志'),
    ('V5', '第二实现或独立复核', '另一证明助手、另一模型或独立专家复核'),
    ('V6', '同行评审/公开复现', '外部读者可复现，主张经公开审查'),
]

# Work package helper
wps: list[dict] = []
def wp(id, title, stream, mechanism, priority, status, objective, basis, sources, claims, proofs, results,
       deps, tasks, deliverables, acceptance, failure, outputs):
    wps.append({
        'id': id, 'title': title, 'stream': stream, 'mechanism': mechanism,
        'priority': priority, 'status': status, 'objective': objective,
        'current_basis': basis, 'source_refs': sources, 'claim_refs': claims,
        'proof_refs': proofs, 'result_refs': results, 'dependencies': deps,
        'tasks': tasks, 'deliverables': deliverables,
        'acceptance_criteria': acceptance,
        'failure_or_split_conditions': failure,
        'target_outputs': outputs,
    })

# 0. Governance
wp('WP-000','规范基线与术语冻结','S0 治理','GOV','P0','ACTIVE',
   '建立后续研究唯一可引用的范围、术语、状态词与版本基线，防止“相对不完备/内部不一致/不可表达/不可判定”继续混用。',
   'AGENTS §25、CURRENT_RESEARCH_INDEX 已提供大部分边界，但尚缺统一工作包基线。',
   ['SRC-Z-001','SRC-META-001'],['Z-36','Z-62'],[],[],[],
   ['冻结“HoTT 不完备性”的四类含义及允许标题','固定 bare HoTT、SIP-structure、directed/linear/guarded enrichment 的术语','建立版本变更与废弃规则'],
   ['PROGRAM_BASELINE 区块','术语表','禁止性主张清单'],
   ['所有活动文档使用同一术语','主结论明确不是 HoTT⊢⊥','所有旧错误公式有替代式'],
   ['若无法给出目标现实域、抽象映射、命题域和富化政策，则候选主张降级为哲学动机'],
   ['所有论文','所有形式化包'])
wp('WP-010','来源谱系、去重与证据独立性','S0 治理','GOV','P0','BASELINED',
   '保证长对话、分支、摘录、戏剧重述和字节副本不被重复计为独立证据。',
   'HOTT_Z_SOURCE_REGISTRY.json 已登记 27 个来源节点及重复关系。',
   ['SRC-META-001','SRC-FINAL-001','SRC-Z-001'],[],[],[],['WP-000'],
   ['补齐每个来源到工作包/主张的双向链接','为新上传材料计算哈希并登记家族','把 AI 角色扮演赞同永久标为非证据'],
   ['更新后的来源注册表','来源—WP—Claim 交叉索引'],
   ['字节重复只计一次','每个来源有 status/priority/use/linked_work_packages','缺失原始文件时明确说明替代材料'],
   ['来源无法追溯时，不得用于原创性或归属主张'],
   ['文献附录','可复现包'])
wp('WP-020','Claim/Proof/Result/Work-Package 编号治理','S0 治理','GOV','P0','ACTIVE',
   '把现有 Z、PA、R、LIT 编号与新 WP 编号统一管理，并阻止并行写入冲突。',
   '当前活动编号唯一，但历史上出现过并行重复，已有归档。',
   ['SRC-META-001'],[],[],[],['WP-000','WP-010'],
   ['建立 WBS JSON 作为唯一 WP 注册表','扩展完整性脚本检查 WP 依赖闭包和引用存在性','所有新定理先取得 Claim ID，再进入 Proof/Result'],
   ['HOTT_Z_WBS_REGISTRY_v1.json','WBS 完整性检查日志'],
   ['WP ID 唯一','依赖指向存在','每个论文结论可回溯到 Claim/Proof/Result/Source'],
   ['出现冲突编号时移入归档，不静默覆盖'],
   ['研究治理','发布包'])
wp('WP-030','旧攻击红队回归套件','S0 治理','GOV/REDTEAM','P1','READY',
   '把已经识别的错误路线转化为自动/人工回归测试，避免论文修订时重新引入。',
   '旧 Modus Tollens、一次性 transport、Map(1,G)、宇宙等价、观察者维度和量子 successor 均已隔离。',
   ['SRC-FINAL-001','SRC-HEEL-001','SRC-GODEL-001','SRC-CANTOR-001','SRC-EXP-001','SRC-OBSERVER-001','SRC-QUANTUM-001'],
   ['Z-01','Z-02','Z-03','Z-05','Z-10'],[],[],['WP-000','WP-020'],
   ['为每种错误写“触发模式—反例—允许替代”测试卡','在主稿 lint 中搜索禁用句式','每轮写作运行回归检查'],
   ['RED_TEAM_REGRESSION.md','文本 lint 脚本与日志'],
   ['所有禁用论证均有机器或人工触发器','主稿不得出现未限定的“HoTT 一切箭头可逆/完全不能表示时间”等句式'],
   ['若新论证无法通过回归检查，不进入活动台账'],
   ['所有论文'])

# 1. Core Z framework
wp('WP-100','完备性分类与目标语义规范','S1 Z 核心','M1','P0','BASELINED',
   '给出统一的目标相对完备性定义，区分句法完备、语义表达充分、自然性完备、有效判定完备和物理本体充分。',
   'AGENTS、v4 候选稿已经给出四类/七层区分。',
   ['SRC-Z-001','SRC-FINAL-EX-001'],['Z-36','Z-37','Z-62'],[],[],['WP-000'],
   ['定义研究对象六元组 (W,M,α,Φ,J,E)','定义 Complete_Φ、Recoverable_Φ、NaturalComplete_Φ、EffectiveComplete_Φ','建立术语到论文标题的许可矩阵'],
   ['DEFINITIONS.md 中的规范定义','论文 I 第 2 节'],
   ['每个“不完备”结论必须实例化六元组','同一结论不得跨完备性种类偷换'],
   ['无法实例化目标语义者降级为非数学陈述'],
   ['论文 I','论文 II'])
wp('WP-110','Z 真值谱因子分解定理','S1 Z 核心','M1','P0','PAPER_PROVED',
   '稳定并形式化“同一抽象纤维内目标真值变化 ⇒ 无精确恢复器”的核心定理。',
   '已有 PA-22/R-20 及多个专门化证明。',
   ['SRC-Z-001'],['Z-16','Z-25','Z-31','Z-62'],['PA-01','PA-22'],['R-01','R-20'],['WP-100'],
   ['写出集合、HoTT/hProp、范畴三个版本','明确因子化充分性只在像/满射/商条件下成立','统一等式、等价和逻辑同值的层级'],
   ['核心定理纸笔定稿','Agda/Cubical 定理 fiberTruthInvariant'],
   ['V2 证明无遗漏','不存在对任意余域的错误充分性陈述','至少一个机器化版本达到 V4'],
   ['若 HoTT 内部 hProp 版本引入额外选择，则退回像/商版本'],
   ['论文 I','理论工具库'])
wp('WP-120','Z 损失谱与表示精化单调性','S1 Z 核心','M1','P1','PAPER_PROVED',
   '把“不完备”量化为 Loss_Φ(α)，并证明表示精化使损失谱反向单调。',
   '已有 Z-125、PA-57、R-53，集合级完成。',
   ['SRC-Z-001','SRC-SEM-001'],['Z-125'],['PA-57'],['R-53'],['WP-100','WP-110'],
   ['规范定义 Loss_Φ 与 Recoverable_Φ','证明 α=h∘β 时 Loss_Φ(β)⊆Loss_Φ(α)','给出时间/历史/角色/成本实例'],
   ['损失谱定理','表示比较示例库'],
   ['定理对命题域变化保持明确','所有实例标明命题域','机器化有限原型通过'],
   ['若不同 Φ 间比较无自然翻译，则禁止直接比较损失集合'],
   ['论文 I','论文 II'])
wp('WP-130','最小充分真值商及其泛性质','S1 Z 核心','M1','P1','PAPER_PROVED',
   '把按完整目标真值谱取商的表示证明为最粗充分抽象，并研究 HoTT quotient/HIT 实现。',
   '集合级结论已有；HoTT quotient/HIT 版本未完成。',
   ['SRC-LAST-001','SRC-Z-001'],['Z-125'],['PA-57'],['R-53'],['WP-110','WP-120'],
   ['定义 w~_Φw′ 当且仅当所有目标命题同值','证明 q_Φ 的充分性和最粗泛性质','选择 set-quotient 或 HIT 形式化路径'],
   ['集合级正式证明','HoTT quotient/HIT 代码','最小充分抽象案例'],
   ['泛性质量词完整','不依赖全局选择','V4 机器化至少完成有限/集合截断版本'],
   ['若高阶命题谱需要更高商，拆分为 set-level 与 higher-level 两稿'],
   ['论文 I 或独立理论短文'])
wp('WP-140','无免费富化与富化让步原则','S1 Z 核心','M1/M2','P0','PAPER_PROVED',
   '证明任何修复旧纤维真值差异的新增字段必须实际区分该纤维；区分“可富化”与“裸层已包含”。',
   '历史、时间、品牌、clock、Step 的实例已有。',
   ['SRC-ID-001','SRC-SEM-001','SRC-FINAL-EX-001'],['Z-110','Z-124','Z-137'],['PA-56','PA-62'],['R-52','R-58'],['WP-110'],
   ['定义 enrichment β 与 forgetful projection','证明有效修复必须在冲突纤维上分离','区分任意选择、自然选择和物理测量提供的信息'],
   ['No-Free Enrichment 定理','Enrichment Concession 原理','实例矩阵'],
   ['定理不把合法富化称为矛盾','每个修复说明新增信息来自何处'],
   ['若富化可从 M 内部自然导出，则将该实例移出“新增信息”类别'],
   ['论文 I','论文 II'])
wp('WP-150','表示精化—可观察代数的 Galois/格结构','S1 Z 核心','M1','P2','READY',
   '探索表示按因子化排序、命题按可恢复性排序之间的反变对应，争取形成真正一般且可能有原创性的理论。',
   'Loss_Φ 单调性和最小充分商提供起点，尚未形成完整定理。',
   ['SRC-Z-001'],['Z-125'],['PA-57'],['R-53'],['WP-120','WP-130','WP-140'],
   ['定义表示预序 Rep(W) 与可观察子代数 Obs(M)','构造 closure/interior 运算并检查 Galois connection','研究最小富化/充分统计量的唯一性和合成'],
   ['探索稿','定理候选与反例','是否独立投稿的决策书'],
   ['至少得到一个非平凡泛性质或明确反例','与统计充分性、abstract interpretation、institution/model theory 比较'],
   ['若仅重述标准核/商因子化，则作为统一语言而非原创主结果'],
   ['独立理论论文候选','论文 I 理论背景'])

# 2. HoTT temporal
wp('WP-200','固定点自由 monodromy 导致无截面的一般引理','S2 HoTT 时间','M2','P0','PAPER_PROVED',
   '建立依赖族沿基空间环路作用无固定点时不存在全局截面的通用 HoTT 引理。',
   '纸笔证明和 Cubical Agda 伪代码已存在。',
   ['SRC-SEM-001'],['Z-124'],['PA-56'],['R-52'],['WP-110'],
   ['定稿 noSectionFromFixedPointFreeMonodromy','核对 universe levels、transport 和 apd','把单价只放在实例化环路的步骤'],
   ['一般引理代码','纸笔引理'],
   ['V4 编译','不把单价作为不必要的前提','可被 WP-210/220/310 复用'],
   ['若库中已有同型引理，改为复用并只保留应用'],
   ['论文 I','形式化库'])
wp('WP-210','裸二事件无规范较早事件','S2 HoTT 时间','M2','P0','ACTIVE',
   '在固定 Agda-unimath commit 上证明所有无标签二点类型不存在等价自然的“较早事件”选择。',
   '纸笔 PA-32/R-29 完成，Agda-unimath API 已定位，尚无编译回执。',
   ['SRC-Z-001','SRC-FINAL-EX-001'],['Z-124'],['PA-32'],['R-29'],['WP-200','WP-600'],
   ['实现 TemporalOrientation X = underlying X','复用 symmetric element/fixed-point 库桥梁','记录完整构建命令和退出码'],
   ['no-canonical-earlier-event.agda','编译日志','依赖锁定文件'],
   ['固定版本通过 type-check','无新增等价目标的公理','定理量化所有 2-Element-Type','解释层与机器类型逐项对应'],
   ['若 API 阻塞，先在 Cubical Agda 完成自足版本，再回迁 Agda-unimath'],
   ['论文 I 中央机器证书'])
wp('WP-220','严格时间序与 n≥2 一般化','S2 HoTT 时间','M2','P1','READY',
   '从无规范较早事件推出二点严格总序无规范选择，并研究所有 n≥2 的版本。',
   '方案和有限 n=2..8 检查已完成，正式机器化待开始。',
   ['SRC-Z-001'],[],[],[],['WP-210'],
   ['形式化 StrictTemporalOrder X 与 least-event','证明二点严格序与选点的等价/映射','一般 n 通过全局最小元或 transposition 障碍'],
   ['no-canonical-temporal-order.agda','n≥2 定理或明确阻碍报告'],
   ['二点版本 V4','一般版本若未成必须给出精确缺口','不依赖预设标准顺序'],
   ['若一般 n 仅为已知 no-global-choice 推论，则降为 corollary，不独立宣称'],
   ['论文 I'])
wp('WP-230','群胚 core 与时间反演盲性','S2 HoTT 时间','M1','P0','PAPER_PROVED',
   '证明 process category 与反范畴可有相同/等价 groupoid core，却在不可逆方向命题上真值相反。',
   'walking-arrow、满忠实群胚障碍和时间反演奇观察量纸笔完成。',
   ['SRC-NARR-001','SRC-Z-001'],['Z-33','Z-34','Z-39'],['PA-09','PA-11','PA-33'],['R-08','R-10','R-30'],['WP-110'],
   ['定稿 walking-arrow 最小反例','证明 Core(C^op)≃Core(C)','定义 time-reversal-odd predicate 并应用因子化定理'],
   ['范畴论定理组','机器化有限范畴版本'],
   ['明确只攻击 identity/core 信息','承认普通函数/Hom 可非可逆','V2 完整且至少有限版本 V4'],
   ['若一般 core 等价需额外小范畴假设，显式限定'],
   ['论文 I'])
wp('WP-240','有向/时态富化的充分性与非保守性边界','S2 HoTT 时间','M1/M2','P1','READY',
   '精确比较 directed interval、Hom-types、Step、clock、later 等富化到底恢复哪些命题，以及是否为保守扩展。',
   '已有文献地图与概念边界，但缺统一 adequacy 表。',
   ['SRC-NARR-001','SRC-SELF-001'],['Z-29','Z-30','Z-35'],['PA-12'],[],['WP-140','WP-230','WP-440','WP-700'],
   ['建立富化—可恢复命题矩阵','区分 expressibility、faithfulness、fullness、conservativity','挑选 2–3 个正式时间理论作比较'],
   ['TEMPORAL_ENRICHMENT_ADEQUACY.md','论文 I 相关工作节'],
   ['每个框架仅作来源支持的主张','不把存在富化误写成裸层完备','明确模型/语法版本'],
   ['文献不足时只给开放问题，不给否定性结论'],
   ['论文 I','综述附件'])
wp('WP-250','HoTT 时间—历史相对不完备主定理组装','S2 HoTT 时间','M1/M2','P0','READY',
   '把 Z 因子化、群胚 core、单价无方向、历史约化和富化原则组装成窄而可投稿的主定理。',
   'v3 主稿和 v4 候选已有，但结构尚需压缩。',
   ['SRC-Z-001','SRC-ID-001','SRC-SEM-001'],['Z-37','Z-120','Z-144'],['PA-53'],['R-49'],['WP-110','WP-140','WP-210','WP-230','WP-300','WP-700'],
   ['固定主定理最小假设','删除与主证明无关的极限/LLM/反射支线','给出强本体论解释的形式化目标而非归因性稻草人'],
   ['Main Theorem Package','论文 I 定理依赖图'],
   ['核心定理链无未定义概念','至少一项中央 HoTT 定理 V4','每个哲学解释可追溯到数学命题'],
   ['若过宽导致原创性/可读性下降，拆为核心定理短文与哲学解释文'],
   ['论文 I'])

# 3. History, semantics, evidence
wp('WP-300','快照—历史来源不可定义','S3 历史语义','M1','P1','PAPER_PROVED',
   '证明相同当前结构允许不同 provenance/因果史时，原作性和历史命题不由快照定义。',
   'Z-109/110、PA-47、R-45/R-50 已完成纸笔。',
   ['SRC-ID-001','SRC-SEM-001'],['Z-109','Z-110'],['PA-47'],['R-45','R-50'],['WP-110','WP-140'],
   ['定稿模型论约化定理','构造 Snapshot=Unit, Provenance=Fin2 最小模型','给出 displayed structure/Σ-type 版本'],
   ['snapshot-provenance-counterexample.agda','论文 I 历史实例'],
   ['V2 证明','最小模型 V4','明确“加入 provenance”是富化而非 HoTT 失败'],
   ['若“现实原作性”需要经验假设，数学定理只陈述条件形式'],
   ['论文 I'])
wp('WP-310','语义角色、品牌与 SIP 相对不完备','S3 历史语义','M1/M2','P1','PAPER_PROVED',
   '证明未编码的用途/意图不是裸结构的等价不变量，并用 SIP 给出 HoTT 特定版本。',
   'Nat/Nat′ 材料已重构为 role forgetful map；Z-135/PA-62/R-58/R-67。',
   ['SRC-SEM-001'],['Z-134','Z-135','Z-137'],['PA-62','PA-69'],['R-58','R-67'],['WP-110','WP-140','WP-200'],
   ['定义 Role、BrandedNat 和 forget-role','证明 role 不因子化','证明内部 hProp 经 SIP 必须结构等价不变','区分 path equality 与 judgmental equality'],
   ['intent-does-not-factor.agda','Z–SIP 定理稿'],
   ['无“任意外部意义皆不可形式化”过度主张','机器化至少完成有限品牌实例','与 representation independence 文献对照'],
   ['若 SIP 一般定理完全标准，原创性聚焦统一框架和应用'],
   ['论文 II'])
wp('WP-320','无语境完美形式化器与规约欠定','S3 历史语义','M1','P1','PAPER_PROVED',
   '把“表达之踵”修复为：同一表面文本在不同语境对应不同规约时，不存在只读文本的普遍正确单值翻译器。',
   'PA-71/R-69 纸笔完成；不可判定加强版尚未建立。',
   ['SRC-HEEL-001','SRC-Z-001'],['Z-05','Z-154'],['PA-71'],['R-69'],['WP-100','WP-110'],
   ['定义 SurfaceText、Context、Spec 和 Correct relation','证明有限最小反例','研究多值/交互式/贝叶斯形式化器的替代','仅在正式编码后探索不可判定性'],
   ['context-free-translate-impossible.agda 或有限证明','论文 II 规约章节'],
   ['清楚区分欠定与不可计算','不使用未定义 InformalProblem','给出允许询问上下文后的恢复条件'],
   ['若无法建立强不可判定归约，保留欠定定理，不夸大'],
   ['论文 II'])
wp('WP-330','断言—mere existence—具体 witness 三层障碍','S3 历史语义','M1/M2','P1','PAPER_PROVED',
   '形式化二值/概率断言、命题截断和具体等价见证之间的严格差别。',
   'Agda-unimath no-global-choice 提供正式库桥梁；本项目专门化未编译。',
   ['SRC-PROB-EX-001','SRC-PROB-001'],['Z-112','Z-113','Z-129'],['PA-49','PA-59'],['R-47'],['WP-200','WP-600'],
   ['定义 assertion soundness 与 witness extraction 两个独立接口','复用 no-global-choice','构造 Equiv witness 专门化','区分局部可判定类型与全局宇宙'],
   ['no-uniform-witness-extractor.agda','论文 II 证据章节'],
   ['V4 专门化','不把 LLM 输出当作已证明 ‖E‖','明确全局选择假设边界'],
   ['若专门化只是库定理一行推论，作为支撑而非原创结果'],
   ['论文 II'])
wp('WP-340','表示独立性与签名相对完备边界','S3 历史语义','M1','P2','READY',
   '把“结构就是一切”精确改写为“相对于选定签名与等价概念的不变量”，并给出 signature change 的判定谱变化。',
   'SIP、displayed structures、representation independence 文献已映射，缺统一定理。',
   ['SRC-SEM-001','SRC-ID-001'],['Z-134','Z-144'],[],[],['WP-120','WP-310','WP-700'],
   ['定义 signature inclusion/reduct/expansion','证明可定义命题在约化下的保持/丢失条件','比较 institution、logical relations 和 SIP'],
   ['Signature-Relative Completeness 定理候选','论文 II 理论主轴'],
   ['至少一个非平凡 signature change 定理','不把人类意义当作无形式对象直接量化'],
   ['若仅重述经典模型论约化，则强调 HoTT/SIP 版本或降为背景'],
   ['论文 II'])

# 4. Operational/computability/dynamics
wp('WP-400','外延函数不决定操作成本','S4 操作有效性','M1','P1','PAPER_PROVED',
   '证明同 denotation、不同 cost/trace 的实现使成本无法经纯外延函数语义下降。',
   'Z-156、PA-73、R-71 已完成。',
   ['SRC-HEEL-001'],['Z-138','Z-156'],['PA-64','PA-73'],['R-60','R-71'],['WP-110','WP-140'],
   ['给出最小程序对','区分 extensional equality、program identity、cost semantics','与 cost-aware/graded type theory 比较'],
   ['extensional-cost-does-not-descend 定理','论文 II 操作章节'],
   ['V2 证明','至少一个形式化实例','明确 cost 可由富化表达'],
   ['若程序模型争议，采用抽象 Sem/Cost 条件定理并附具体模型'],
   ['论文 II'])
wp('WP-410','Cartesian—linear/quantitative 结构制度障碍','S4 操作有效性','M1/M2','P1','PAPER_PROVED_CONDITIONAL',
   '把旧资源之踵改写为结构保持问题：cartesian context 的复制/丢弃结构不能在要求非可复制资源的语义中被强单态保留。',
   '概念和纸笔论证已有，范畴库机器化未完成。',
   ['SRC-HEEL-001','SRC-NARR-001'],['Z-08','Z-136'],['PA-63'],['R-59'],['WP-000','WP-400'],
   ['固定对称幺半闭/线性范畴语义','陈述强幺半函子保留对角/终止映射的障碍','给出不可复制资源反例'],
   ['Cartesian–Linear Obstruction 定理','范畴库形式化计划'],
   ['不复用错误一次性 transport','前提中明确结构保持强度','与 linear dependent type theory 对照'],
   ['若一般定理过于标准，作为资源实例和修复分析'],
   ['论文 II'])
wp('WP-420','总而完备的 inhabitant synthesizer 不可能','S4 操作有效性','M3','P1','PAPER_PROVED_CONDITIONAL',
   '固定有效演算，在 checking 可判定、inhabitation 不可判定时排除返回 witness 或 emptiness certificate 的总算法。',
   'PA-72 与条件性 Claim 已完成，尚未固定唯一演算和机器化归约。',
   ['SRC-HEEL-001','SRC-Z-001'],['Z-04','Z-137'],['PA-64','PA-72'],[],['WP-100','WP-600','WP-700'],
   ['选择具体演算/编码','形式化 halting→inhabitation 映射','证明 solver 将判定 halting','标明适用于所有充分强系统'],
   ['正式归约稿','可执行编码或证明助手文件'],
   ['演算、编码、soundness/completeness 全部显式','V4 或可机械核验归约','不声称 HoTT 独有'],
   ['若所选 HoTT 核心的 inhabitation 状态不清，改用已知子语言嵌入'],
   ['论文 II'])
wp('WP-430','未来最终稳定性的停机障碍','S4 操作有效性','M3','P1','PAPER_PROVED',
   '证明统一判定任意可计算时间过程是否最终稳定至少与停机问题同样困难。',
   'PA-15/R-14 已完成。',
   ['SRC-Z-001'],['Z-46','Z-59'],['PA-15'],['R-14'],['WP-100'],
   ['定稿二值序列归约','区分单个可分析过程与统一判定问题','与 temporal logic/model checking 边界比较'],
   ['Stabilization Hardness 定理','论文 I/II 辅助结果'],
   ['归约双向条件正确','算法模型明确','不把非停机直接等同不一致'],
   ['若主论文过宽，移至论文 II 或附录'],
   ['论文 I 附录或论文 II'])
wp('WP-440','Guard erasure 与固定点障碍','S4 操作有效性','M1','P1','PAPER_PROVED',
   '证明把跨阶段递推无损压成单一静态值且保持更新律时必须产生固定点；无固定点系统只能保留轨道而非静态解。',
   'Z-41/42、PA-13/14/74、R-12/13/72 已完成。',
   ['SRC-SELF-001'],['Z-41','Z-42','Z-43'],['PA-13','PA-14','PA-74'],['R-12','R-13'],['WP-110','WP-240'],
   ['定稿 Fix(F) 与 Traj(F,s0)','形式化 Bool not 反例','比较 later/clock/guarded recursion','研究一般 coalgebra 版本'],
   ['guard-erasure-implies-fixed-point.agda','论文 II 动态章节'],
   ['V4 最小实例','清楚区分时间下标与真正 delay','承认 coinduction/guarded 修复'],
   ['若一般 coalgebra 版本需要大量理论，先发布最小定理'],
   ['论文 II'])
wp('WP-450','极限、闭包、可达性与芝诺完成语义','S4 操作有效性','M1','P2','PAPER_PROVED_CONDITIONAL',
   '把极限批判限制为闭包点、有限步可达、有限时间可达和极限阶段状态之间的非等价。',
   'PA-17–21、R-16–19 已给出多个严格反例。',
   ['SRC-FINAL-EX-001','SRC-Z-001'],['Z-48','Z-50','Z-51','Z-52','Z-53','Z-60','Z-61'],['PA-17','PA-18','PA-19','PA-20','PA-21'],['R-16','R-17','R-18','R-19'],['WP-100','WP-110'],
   ['定义 Reach_fin、Reach_time、Closure、LimitStageState','证明各蕴含的反例和所需附加公理','建立离散任务模型与连续轨迹模型的双语义'],
   ['ZENO_OPERATIONAL_SEMANTICS.md','哲学论文数学附录'],
   ['不声称极限定义非法','每个“完成”词都有明确定义','物理本体结论标为条件性'],
   ['若无法连接 HoTT 特定主线，则不进入论文 I'],
   ['论文 IV/哲学稿','背景附录'])
wp('WP-460','有效极限、Specker 序列与信息完成度','S4 操作有效性','M3','P2','BACKGROUND',
   '提供“经典存在/外延完成不等于有效可计算完成”的标准计算分析支撑。',
   'Specker、收敛模、lim/Turing jump 文献已整理。',
   ['SRC-Z-001'],['Z-13','Z-14','Z-19','Z-20','Z-59'],['PA-02','PA-03','PA-20'],['R-02','R-03'],['WP-450','WP-700'],
   ['复核标准定义和引用','给出可计算收敛模的良性对照','禁止把一般 lim 障碍推广到每个具体极限'],
   ['计算分析背景节','可运行示例'],
   ['所有结果标为已知文献','引用原始/权威来源','不作为 HoTT 原创性'],
   ['若篇幅过大移入哲学稿附录'],
   ['论文 IV/背景'])

# 5 Reflection
wp('WP-500','Lawvere/Gödel 反射支线的正确重建','S5 反射宇宙','M4','P3','BLOCKED',
   '废弃错误 G≃Map(1,G) 后，从真实语法编码、评价与可证明性谓词建立 HoTT/UF 中的对角化研究。',
   '源材料只提供动机且含定义错误；当前无正式对象理论。',
   ['SRC-GODEL-001','SRC-MIRROR-001','SRC-MIRROR-EX-001'],[],[],[],['WP-000','WP-510','WP-700'],
   ['选择对象理论与元理论','编码 syntax/substitution/evaluation/provability','精确陈述 Lawvere 条件','区分内部定理与元定理'],
   ['REFLECTION_FOUNDATIONS.md','真正的定理候选'],
   ['Map(1,G) 错误不再出现','所有 Gödel 条件显式','至少一个标准结果完整重建后才谈新贡献'],
   ['在缺少语法/可证明性编码时保持 BLOCKED'],
   ['论文 III'])
wp('WP-510','宇宙、resizing、predicativity 与变体审计','S5 反射宇宙','M4','P2','READY',
   '固定不同 HoTT/UF 变体的宇宙假设，防止由角色相似或单个 lift 推出错误的宇宙结论。',
   'Cantor/表达性坍缩材料已作为负面案例；文献初步具备。',
   ['SRC-CANTOR-001','SRC-EXP-001','SRC-UNIV-001'],['Z-143','Z-147'],['PA-68'],['R-65'],['WP-000','WP-700'],
   ['建立 axiomatic/cubical、cumulative/noncumulative、resizing 假设矩阵','复核内部 universe 和 impredicativity 模型','为 WP-500 选定安全设置'],
   ['UNIVERSE_VARIANT_MATRIX.md','论文 III 前置审计'],
   ['每条结论绑定具体变体','不从 lift 失败推出不存在任何 equivalence','不假设同层全集'],
   ['无法统一时按变体分支，不强求单一结论'],
   ['论文 III','所有论文红队'])

# 6 Formalization
wp('WP-600','证明助理工具链锁定与可复现环境','S6 形式化','FORMAL','P0','READY',
   '固定首选证明助手、库 commit、构建命令和依赖，形成可复现机器证书环境。',
   '当前只有伪代码和库接口定位，尚无本地 Agda/Lean/Coq 回执。',
   [],[],[],[],['WP-000'],
   ['选择 Agda-unimath 为首选、Cubical Agda 为备选/交叉验证','记录版本和 commit','创建最小 smoke test','禁止隐式新增公理'],
   ['toolchain.lock.md','环境检查日志','最小编译样例'],
   ['从干净环境可执行同一命令','日志包含退出码','依赖哈希可核验'],
   ['若环境无法安装，完整记录阻碍并使用容器/本地替代；不得伪造回执'],
   ['所有 V4 证明'])
wp('WP-610','Agda-unimath：无规范较早事件','S6 形式化','FORMAL/M2','P0','ACTIVE',
   '完成当前唯一关键路径机器化目标。',
   '形式化计划已定位 symmetric-elements/involutive-types/2-element-types。',
   [],['Z-124'],['PA-32'],['R-29'],['WP-200','WP-210','WP-600'],
   ['实现源码','解决 API 名称和 universe level','运行 type-check','保存 stdout/stderr/exit code'],
   ['formal/no-canonical-earlier-event.agda','formal/build.log'],
   ['达到 V4 全部六项验收','代码不含 postulate/unsafe 替代目标'],
   ['若 Agda-unimath API 不稳定，转 WP-640 自足 Cubical 版本后再回迁'],
   ['论文 I Gate G2'])
wp('WP-620','机器化严格时间序与一般无自然定向','S6 形式化','FORMAL/M2','P1','READY',
   '在 WP-610 基础上证明严格时间序推论和可复用无截面接口。',
   '纸笔方案已完成。',
   [],[],[],[],['WP-610','WP-220'],
   ['定义 least-event','导出二点严格序不可能','评估 n≥2 一般版'],
   ['formal/no-canonical-temporal-order.agda','一般化说明'],
   ['二点定理 V4','一般版或明确不完成原因','与纸笔定理同义'],
   ['若一般版成本过高，不阻塞论文 I'],
   ['论文 I'])
wp('WP-630','机器化 Z 因子化、core、provenance 与 witness 实例','S6 形式化','FORMAL','P1','READY',
   '为核心论文提供多条相互独立的机器证书，而非只验证单一二点例。',
   '蓝图已有，尚未执行。',
   [],['Z-62','Z-109','Z-112'],['PA-22','PA-47','PA-49'],['R-20','R-45','R-47'],['WP-600','WP-110','WP-230','WP-300','WP-330'],
   ['实现 fiberTruthInvariant','机器化 walking arrow/core 有限模型','机器化 Snapshot×Fin2','连接 no-global-choice'],
   ['formal/core_suite/*','各定理构建日志'],
   ['至少三项达到 V4','共享定义不引入循环依赖','定理与论文编号对应'],
   ['个别目标若库缺失，可分批完成，不阻塞 WP-610'],
   ['论文 I/II'])
wp('WP-640','第二证明助手或自足 Cubical Agda 交叉验证','S6 形式化','FORMAL','P2','READY',
   '降低对单一库 API 和隐藏公理的依赖，获得 V5 级交叉验证。',
   'Cubical Agda 伪代码已有。',
   [],[],[],[],['WP-610'],
   ['选择 Cubical Agda/Rocq/Lean 之一','重写中央无截面定理','比较公理/计算规则'],
   ['第二实现源码与差异报告'],
   ['中央定理在第二设置通过或给出清晰语义差异','不复制第一实现的未证明假设'],
   ['若无第二工具链，转为独立手工 proof audit，不虚称 V5'],
   ['论文 I 附件'])
wp('WP-650','验证回归、清单与发布 CI','S6 形式化','FORMAL/GOV','P1','ACTIVE',
   '统一有限检查、ID 完整性、禁用论证 lint、证明助手日志和哈希清单。',
   '已有 round1–round3 Python 检查与 manifests，尚无统一 CI。',
   [],[],[],[],['WP-020','WP-030','WP-600'],
   ['合并现有验证脚本','新增 WBS/引用/禁用句式检查','生成每次发布 manifest','区分 V3 与 V4'],
   ['verification/run_all.sh','verification/report.json','manifest.sha256'],
   ['一条命令执行全部非交互检查','失败返回非零','报告不把有限枚举冒充证明'],
   ['工具缺失时报告 SKIPPED_WITH_REASON，不标 PASS'],
   ['所有发布包'])

# 7 Literature/red team
wp('WP-700','系统文献检索与现有工作映射','S7 文献红队','LIT','P0','ACTIVE',
   '系统查明每个基础组件、组合框架和术语是否已有先例，并优先使用原始论文/官方文档。',
   'LIT-01–63 已初步覆盖，但尚不够支持原创性声明。',
   [],[],[],[],['WP-000','WP-010'],
   ['为 M1–M4 分别设计检索式与纳排标准','覆盖 univalence/SIP/no natural choice/directed/linear/guarded/cost/abstract interpretation/definability','记录负面检索但不把未找到当作不存在'],
   ['SYSTEMATIC_LITERATURE_REVIEW.md','search_log.json','文献—定理对照表'],
   ['每个主定理有最接近工作','至少半数关键引文来自原始/官方来源','检索日期和查询可复现'],
   ['若发现主定理已完全存在，调整贡献为应用/统一框架或停止原创性主张'],
   ['所有论文'])
wp('WP-710','原创性矩阵与主张校准','S7 文献红队','LIT/GOV','P0','READY',
   '把“已知基础组件、项目重构、可能原创组合、尚未证明”逐项分开。',
   '已有原创性审计，但需随 v4 和机器化更新。',
   [],[],[],[],['WP-700','WP-250','WP-340'],
   ['建立 theorem-by-theorem nearest-prior-art 矩阵','标记 novelty type：new theorem/new synthesis/new interpretation/new formalization','生成允许的摘要/标题措辞'],
   ['ORIGINALITY_MATRIX_v2.md','CLAIM_CALIBRATION.md'],
   ['每个摘要性主张有状态与证据','禁止“首次/推翻”无依据表述','冲突文献有双向讨论'],
   ['原创性不足时缩窄或改投哲学/综述方向'],
   ['论文 I/II/III'])
wp('WP-720','内部对抗性审稿与反例搜索','S7 文献红队','REDTEAM','P0','READY',
   '以 HoTT 专家、范畴论家、计算理论家和数学哲学家四个角色逐条攻击当前定理与解释。',
   '已有零散红队规则，缺统一审稿报告。',
   ['SRC-BASE-003','SRC-EXP-001','SRC-CANTOR-001'],[],[],[],['WP-030','WP-250','WP-700'],
   ['攻击量词、类型、自然性、变体、原创性和归因','尝试构造反例/反富化','逐条记录接受、修订、驳回'],
   ['INTERNAL_REFEREE_REPORTS/','反例数据库'],
   ['每个主定理至少经过两种独立攻击模板','所有严重意见有 disposition','未解决重大问题阻塞投稿'],
   ['若中央定理被反例击穿，保留失败史并重构，不掩盖'],
   ['论文 Gate G4'])
wp('WP-730','独立专家复核与外部可复现性','S7 文献红队','REVIEW','P1','EXTERNAL_GATE',
   '获得至少一名不参与当前推导者对数学陈述、形式化代码和归属边界的独立审查。',
   '尚未完成。',
   [],[],[],[],['WP-610','WP-700','WP-720'],
   ['准备匿名短稿和最小代码包','收集逐条意见','公开 disposition 与修订记录'],
   ['EXTERNAL_REVIEW_LOG.md','修订差异'],
   ['复核者能从锁定环境复现中央定理','重大异议关闭或公开保留'],
   ['无法获得外部复核时，稿件必须明确仍未经独立专家验证'],
   ['投稿前质量门'])

# 8 publication
wp('WP-800','论文 I：No-Free Temporal and Historical Enrichment','S8 写作发布','PUB','P0','BLOCKED',
   '产出窄、HoTT 特定、可机器验证的主论文，聚焦时间方向、群胚 core、历史来源和无免费富化。',
   'v3 主稿为规范稿，v4 为候选整合稿。',
   ['SRC-Z-001','SRC-ID-001','SRC-SEM-001'],['Z-37','Z-109','Z-124','Z-125'],[],[],['WP-250','WP-610','WP-630','WP-700','WP-710','WP-720'],
   ['重写摘要和引言','只保留中央定理依赖','加入机器证明与局限','准备英文数学稿'],
   ['paper1/main.tex 或 .md','supplement/formal-code','cover letter'],
   ['G1 范围、G2 机器化、G3 原创性、G4 红队全部通过','标题不暗示 HoTT 内部不一致','所有外部事实有可靠引文'],
   ['若机器化或原创性不过门，发布技术报告而非声称投稿级突破'],
   ['主论文'])
wp('WP-810','论文 II：Signature-Relative Incompleteness','S8 写作发布','PUB','P1','READY',
   '聚焦语义角色、语境、证据、资源成本和证明搜索的签名相对不完备。',
   '专题稿已存在，需避免范围过散。',
   ['SRC-SEM-001','SRC-HEEL-001','SRC-PROB-EX-001'],['Z-135','Z-138','Z-154','Z-156'],[],[],['WP-310','WP-320','WP-330','WP-400','WP-410','WP-420','WP-340','WP-700'],
   ['选择单一中心（签名约化/操作语义）','把其余结果降为实例','至少机器化一个非时间实例'],
   ['paper2 草稿','实例代码'],
   ['有一个明确主定理而非案例堆积','与 Paper I 无重复贡献','M1/M2/M3 层次清晰'],
   ['若无法形成统一主定理，拆成两篇短文或仅作附录'],
   ['次论文'])
wp('WP-820','论文 III：Reflection and Diagonalization','S8 写作发布','PUB','P3','BLOCKED',
   '在正确对象理论/元理论设置下研究单价基础中的反射、对角化和宇宙边界。',
   '当前仅有动机和错误攻击的负面素材。',
   ['SRC-GODEL-001','SRC-CANTOR-001','SRC-MIRROR-001'],[],[],[],['WP-500','WP-510','WP-700'],
   ['先复现标准 Lawvere/Gödel 结果','再寻找 HoTT 特定现象','严格隔离时间论文'],
   ['paper3 研究稿'],
   ['对象理论编码完整','无 Map(1,G) 错误','至少一项非平凡新结果或明确综述价值'],
   ['无新结果时只发布研究笔记，不包装成悖论'],
   ['长期论文'])
wp('WP-830','哲学综合：Being、Becoming、Zeno 与模型边界','S8 写作发布','PUB/PHIL','P2','READY',
   '保留原文最有力的哲学洞察，同时把所有数学主张与已证明结果分层。',
   '原判决书、戏剧稿、极限讨论提供丰富动机，但含大量过度主张。',
   ['SRC-FINAL-001','SRC-NARR-001','SRC-FINAL-EX-001','SRC-Z-001'],[],[],[],['WP-000','WP-450','WP-460','WP-700'],
   ['重写 Z 铁律哲学版与数学版','讨论外延完成/操作完成','明确模型成功≠本体镜像','附数学事实核验框'],
   ['philosophy manuscript','面向非专业读者的说明'],
   ['每个数学断言可回溯','修辞不冒充证明','明确连续轨迹与离散任务两种模型'],
   ['若物理本体论缺乏证据，以开放问题呈现'],
   ['哲学论文/专著章节'])
wp('WP-840','可复现研究发布包','S8 写作发布','PUB/GOV','P1','READY',
   '把主稿、形式化源码、验证日志、来源索引、台账和哈希清单打包成可审计发布物。',
   '已有多轮 zip 和 manifest，需建立最终规范结构。',
   [],[],[],[],['WP-020','WP-650','WP-800'],
   ['定义 release 目录结构','排除非规范并行稿或明确归档','生成 SPDX/许可证和引用说明','计算 SHA-256'],
   ['release.zip','MANIFEST.sha256','REPRODUCE.md'],
   ['从包内说明可复现 V3/V4 检查','所有规范/归档状态清楚','无未授权或无来源材料冒充论文证据'],
   ['若 Paper I 未过门，可发布“研究工作区快照”而非“最终证明”'],
   ['公开研究包'])

# Validate unique IDs and dependencies
ids = [w['id'] for w in wps]
assert len(ids) == len(set(ids)), 'duplicate WP id'
ids_set = set(ids)
for w in wps:
    missing = [d for d in w['dependencies'] if d not in ids_set]
    assert not missing, (w['id'], missing)

# Existing ID validation (allow only listed IDs actually present)
claim_text = (ROOT/'CLAIM_LEDGER.md').read_text(encoding='utf-8')
proof_text = (ROOT/'PROOF_ATTEMPTS.md').read_text(encoding='utf-8')
result_text = (ROOT/'RESULTS.md').read_text(encoding='utf-8')
claim_ids = set(re.findall(r'\bZ-\d+\b', claim_text))
proof_ids = set(re.findall(r'\bPA-(?:\d+|ABS-\d+)\b', proof_text))
result_ids = set(re.findall(r'\bR-\d+\b', result_text))
validation_warnings=[]
for w in wps:
    for c in w['claim_refs']:
        if c not in claim_ids: validation_warnings.append(f"{w['id']}: missing claim {c}")
    for p in w['proof_refs']:
        if p not in proof_ids: validation_warnings.append(f"{w['id']}: missing proof {p}")
    for r in w['result_refs']:
        if r not in result_ids: validation_warnings.append(f"{w['id']}: missing result {r}")

streams = [
    ('S0 治理','保证证据、编号、范围与失败史可追踪'),
    ('S1 Z 核心','建立一般相对不完备与无免费富化理论'),
    ('S2 HoTT 时间','产出最 HoTT 特定的时间方向 no-go'),
    ('S3 历史语义','处理 provenance、role、context 与 witness'),
    ('S4 操作有效性','处理 cost、resource、search、stability、limit'),
    ('S5 反射宇宙','独立研究 Gödel/Lawvere/universe，不污染时间主稿'),
    ('S6 形式化','获得 proof-assistant 证书和可复现构建'),
    ('S7 文献红队','原创性、变体和专家审查'),
    ('S8 写作发布','论文分流和发布包'),
]

milestones = [
    {
        'id':'MS-0','title':'规范基线冻结','dependencies':['WP-000','WP-010','WP-020'],
        'exit_criteria':['WBS 注册表通过完整性检查','术语/禁用结论/来源谱系统一','所有活动稿指向同一规范入口'],
        'unlocks':['全部数学与写作包']},
    {
        'id':'MS-1','title':'Z 核心定理套件稳定','dependencies':['WP-100','WP-110','WP-120','WP-130','WP-140'],
        'exit_criteria':['核心定义无偷换','因子化、损失谱、最小商、富化定理均达到 V2','至少一个核心定理进入 V4 队列'],
        'unlocks':['HoTT/历史/语义实例统一写作']},
    {
        'id':'MS-2','title':'首个 HoTT 特定机器定理','dependencies':['WP-200','WP-210','WP-600','WP-610'],
        'exit_criteria':['no-canonical-earlier-event 固定 commit 编译通过','源码和日志落盘','无额外公理'],
        'unlocks':['论文 I 机器证书门','严格时间序形式化']},
    {
        'id':'MS-3','title':'时间—历史主定理包','dependencies':['WP-220','WP-230','WP-250','WP-300','WP-630'],
        'exit_criteria':['中央定理链纸笔完整','至少两类独立实例 V4','富化边界完整'],
        'unlocks':['论文 I 完整初稿']},
    {
        'id':'MS-4','title':'原创性与对抗审查通过','dependencies':['WP-700','WP-710','WP-720'],
        'exit_criteria':['nearest-prior-art 矩阵完成','中央主张通过内部红队','所有“首次/推翻”措辞有明确处置'],
        'unlocks':['投稿级定位']},
    {
        'id':'MS-5','title':'论文 I 可投稿基线','dependencies':['WP-800','WP-730'],
        'exit_criteria':['数学、形式化、文献和局限四项完成','独立复核意见有 disposition','复现包可构建'],
        'unlocks':['正式投稿/公开预印本']},
    {
        'id':'MS-6','title':'论文 II 定稿门','dependencies':['WP-310','WP-320','WP-330','WP-400','WP-410','WP-420','WP-810'],
        'exit_criteria':['形成单一主定理','至少一个非时间实例 V4','与论文 I 无贡献重复'],
        'unlocks':['第二论文']},
    {
        'id':'MS-7','title':'反射支线准入','dependencies':['WP-500','WP-510'],
        'exit_criteria':['对象理论/元理论固定','标准对角化可重建','所有旧定义错误删除'],
        'unlocks':['论文 III']},
]

gates = [
    {'id':'G1','name':'范围门','question':'结论是否明确是目标相对表示/自然性/有效性不完备，而非 HoTT 内部不一致？','failure_action':'降级或重写标题、摘要和定理。'},
    {'id':'G2','name':'机器化门','question':'至少一个中央 HoTT 特定定理是否达到 V4？','failure_action':'只能称纸笔技术报告，不称完成形式化。'},
    {'id':'G3','name':'原创性门','question':'每个主贡献是否与最近工作逐项比较？','failure_action':'改称综合框架、应用或形式化，不使用首创措辞。'},
    {'id':'G4','name':'红队门','question':'是否回答“HoTT 可用函数/Step/clock/brand 表达”的反驳并精确解释富化？','failure_action':'阻塞论文。'},
    {'id':'G5','name':'变体门','question':'是否区分 axiomatic HoTT、cubical、directed、linear、guarded 等变体？','failure_action':'缩小适用范围。'},
    {'id':'G6','name':'现实桥梁门','question':'涉及物理时间或现实语义时，是否给出明确表示假设而非从数学直接越界？','failure_action':'改为条件性哲学解释。'},
    {'id':'G7','name':'复现门','question':'源码、依赖、命令、日志与哈希是否齐备？','failure_action':'不得发布为机器验证成果。'},
]

risks = [
    ('RK-01','核心 no-section/因子化定理已知，原创性不足','高','WP-700/710 逐定理比对；把贡献移到统一框架、最小富化或新应用。'),
    ('RK-02','攻击对象是稻草人：HoTT 创建者未声称完整物理本体论','高','主定理使用条件性强主张；归属性陈述必须有一手引文。'),
    ('RK-03','结果过于一般，不够 HoTT 特定','高','强化 SIP/univalence/automorphism 版本并提供 proof-assistant 实例。'),
    ('RK-04','“时间”含义漂移','高','每个定理固定 order/direction/duration/causality/clock/stability 中具体一项。'),
    ('RK-05','编码与内生恢复再次混淆','高','所有富化通过显式 forgetful map 和新增字段说明。'),
    ('RK-06','Agda-unimath API 或环境阻塞','中','先锁定工具链；Cubical Agda 自足版本作为备份；如实记录失败。'),
    ('RK-07','有限模型被误写成无界证明','高','V3/V4 分级和 CI 强制标签。'),
    ('RK-08','宇宙/计算性结论跨变体泛化','高','WP-510 变体矩阵；所有定理绑定具体系统。'),
    ('RK-09','自然语言形式化不可判定性没有正式归约','高','只保留欠定定理；强版本由 WP-420 式严格编码驱动。'),
    ('RK-10','物理芝诺立场缺乏经验基础','中','区分离散任务与连续轨迹；不把开放本体论写成数学定理。'),
    ('RK-11','AI 对话来源可信度低且重复','高','来源只作思想史；数学事实由证明/一手文献承担。'),
    ('RK-12','范围膨胀导致一篇论文无法聚焦','高','论文 I/II/III/哲学稿分流；WP-250 强制窄化。'),
    ('RK-13','编号与并行稿再次冲突','中','WP-020 注册表和 CI；任何冲突归档。'),
    ('RK-14','外部专家无法复现','中','WP-600/650/840 提供最小容器化说明与完整日志。'),
]

critical_path = ['WP-000','WP-100','WP-110','WP-200','WP-210','WP-600','WP-610','WP-250','WP-700','WP-710','WP-720','WP-800','WP-730','WP-840']

# Build markdown
lines=[]
add=lines.append
add('# HOTT–Z 后续工作总方案与工作包分解（WBS v1.0）')
add('')
add(f'**基线日期**：{DATE}  ')
add('**状态**：CANONICAL PROGRAM PLAN  ')
add('**研究对象**：Z 铁律启发下，HoTT/单价基础相对于时间、历史、语境、资源、证据与有效求解目标的表示不完备、自然性障碍和不可总判定边界。  ')
add('**明确非目标**：本文档不把当前成果表述为 `HoTT ⊢ ⊥`，不声称 HoTT 完全不能编码时间，也不把所有逻辑悖论归因于时间缺失。')
add('')
add('---')
add('')
add('## 0. 执行摘要')
add('')
add('本项目后续工作的唯一主线是：把原材料中的 Being/Becoming、照片/电影、三大阿喀琉斯之踵、Zeno/极限与“结构等价但意义不同”等思想，重构为可审查的四类数学机制：')
add('')
add('1. **M1 非因子化/不可定义**：抽象合并了目标真值不同的现实状态；')
add('2. **M2 无截面/无自然选择**：自同构作用在候选富化上无固定点；')
add('3. **M3 不可总判定/不可总合成**：假定总算法会判定停机、inhabitation 或其他已知不可判定问题；')
add('4. **M4 反射/元理论开放性**：必须先固定语法、评价、可证明性和元理论，不允许用错误的几何类比替代 Gödel 条件。')
add('')
add('项目的关键产出不是一句“HoTT is gone”，而是一组分层、可证、可机器检查的 no-go 定理，以及对合法富化的精确说明。最优先成果为：')
add('')
add('- `no-canonical-earlier-event` 的 Agda-unimath 编译；')
add('- 群胚 core 的时间反演盲性；')
add('- 历史来源、语义角色和具体 witness 的非因子化/无截面；')
add('- No-Free Temporal and Historical Enrichment 主论文；')
add('- 独立的签名相对不完备论文；')
add('- 与主线严格隔离的 Reflection/Diagonalization 长期项目。')
add('')
add('### 0.1 当前关键路径')
add('')
add('```text')
add('WP-000 → WP-100 → WP-110 → WP-200 → WP-210 → WP-600 → WP-610')
add('       → WP-250 → WP-700 → WP-710 → WP-720 → WP-800 → WP-730 → WP-840')
add('```')
add('')
add('并行支线：`WP-230 + WP-300 + WP-630` 为论文 I 提供第二、第三组独立证据；`WP-310–440` 汇入论文 II；`WP-500–510` 在满足准入条件前不得进入论文 I。')
add('')
add('---')
add('')
add('## 1. 方案依据与证据分层')
add('')
add('### 1.1 原材料直接支持的研究动机')
add('')
add('- Z 铁律的原始直觉：理论删除现实核心属性后，不能无需外部补充而完整再现该属性；')
add('- HoTT 的类型、路径、函数作为完成对象与现实生成过程之间的 Being/Becoming 张力；')
add('- 资源、未知、模糊性三条“阿喀琉斯之踵”作为问题发现器；')
add('- `Nat/Nat′`、原作/复制品、概率断言/证明见证、自指循环和宇宙分层等案例。')
add('')
add('### 1.2 项目重构后可进入数学主线的内容')
add('')
add('- Z 真值谱因子分解；')
add('- Loss 谱、精化单调性、最小充分真值商；')
add('- 无免费富化；')
add('- 单价/自同构下无规范时间方向；')
add('- groupoid core 的时间反演盲性；')
add('- 历史/角色/语境/成本/witness 的非因子化；')
add('- proof synthesis、future stabilization 的严格不可判定归约；')
add('- guard erasure 的固定点障碍。')
add('')
add('### 1.3 只能保留为失败史或红队案例的内容')
add('')
add('- 旧 `¬P→¬R` 单命题公式与错误的 Modus Tollens 应用；')
add('- 一次性 transport；')
add('- 未定义 `InformalProblem` 后直接调用停机问题；')
add('- `Map(1,G)` 被误认作环空间；')
add('- 单一“所有类型宇宙”、相邻宇宙角色相似即等价；')
add('- proof 必须唯一、观察者必须高一维、量子 successor/EPR 等路线。')
add('')
add('---')
add('')
add('## 2. 项目目标树')
add('')
add('### O0 总目标')
add('')
add('建立一套对 HoTT/单价基础的**目标相对不完备性理论**：明确哪些现实命题在何种遗忘、群胚化、对称化、截断或外延化之后无法恢复；明确哪些富化足以恢复；并区分表示缺口、自然性障碍、算法边界与元理论反射边界。')
add('')
add('### O1 数学核心')
add('')
add('形成 Z 因子化、损失谱、最小充分商、无免费富化和表示格/反变结构。')
add('')
add('### O2 HoTT 特定结果')
add('')
add('以 univalence/SIP、自同构不变性、二点无规范选择、groupoid core 为技术核心，证明裸 identity/core 层不能自然恢复一般时间方向。')
add('')
add('### O3 操作与有效性')
add('')
add('把资源、未知、形式化入口和非停机直觉修复为成本非因子化、结构制度不匹配、无总 proof synthesizer、稳定性不可判定和 guard erasure。')
add('')
add('### O4 反射与宇宙')
add('')
add('另立对象理论/元理论项目，正确重建 Lawvere/Gödel/宇宙边界，绝不复用错误“哥德尔空间”。')
add('')
add('### O5 可复现与发表')
add('')
add('中央定理至少达到 V4，主稿通过文献、红队和外部复核门，再形成论文 I；其余成果按论文 II/III/哲学稿分流。')
add('')
add('---')
add('')
add('## 3. 验证等级与全局 Definition of Done')
add('')
add('| 等级 | 名称 | 含义 |')
add('|---|---|---|')
for v,n,d in VERIFY_LEVELS:
    add(f'| {v} | {n} | {d} |')
add('')
add('任一新定理只有同时满足下列条件，才可进入论文主结果：')
add('')
add('1. 类型/语言良构，量词和 universe level 明确；')
add('2. 固定现实域、抽象映射、目标命题域与允许富化；')
add('3. 提供纸笔证明或反例，并通过旧攻击回归测试；')
add('4. 标明最接近文献及原创性类别；')
add('5. 若是中央 HoTT 结果，至少达到 V4；')
add('6. 解释不超过定理：相对不完备不写成内部不一致；')
add('7. Claim、Proof、Result、Source 和 WP 互相可追踪。')
add('')
add('---')
add('')
add('## 4. 工作流总览')
add('')
for s,d in streams:
    add(f'- **{s}**：{d}。')
add('')
add('### 4.1 工作包状态词')
add('')
for k,v in STATUS_VOCAB.items():
    add(f'- `{k}`：{v}。')
add('')
add('---')
add('')
add('## 5. WBS 总表')
add('')
add('| WP | 标题 | 流 | 机制 | 优先级 | 当前状态 | 主要输出 |')
add('|---|---|---|---|---|---|---|')
for w in wps:
    out='；'.join(w['target_outputs'][:2])
    add(f"| {w['id']} | {w['title']} | {w['stream']} | {w['mechanism']} | {w['priority']} | {w['status']} | {out} |")
add('')
add('---')
add('')
add('## 6. 工作包详细卡')
add('')
for w in wps:
    add(f"### {w['id']} — {w['title']}")
    add('')
    add(f"- **流/机制**：{w['stream']} / {w['mechanism']}")
    add(f"- **优先级/状态**：{w['priority']} / `{w['status']}`")
    add(f"- **目标**：{w['objective']}")
    add(f"- **当前基础**：{w['current_basis']}")
    add(f"- **依赖**：{', '.join(w['dependencies']) if w['dependencies'] else '无'}")
    add(f"- **来源索引**：{', '.join(w['source_refs']) if w['source_refs'] else '以规范研究文件为主'}")
    refs=[]
    if w['claim_refs']: refs.append('Claims '+', '.join(w['claim_refs']))
    if w['proof_refs']: refs.append('Proofs '+', '.join(w['proof_refs']))
    if w['result_refs']: refs.append('Results '+', '.join(w['result_refs']))
    add(f"- **现有台账链接**：{'；'.join(refs) if refs else '执行时分配/补齐'}")
    add('- **任务**：')
    for x in w['tasks']: add(f'  1. {x}')
    add('- **交付物**：')
    for x in w['deliverables']: add(f'  - `{x}`' if any(ch in x for ch in './_*') else f'  - {x}')
    add('- **验收标准**：')
    for x in w['acceptance_criteria']: add(f'  - {x}')
    add('- **失败/拆分条件**：')
    for x in w['failure_or_split_conditions']: add(f'  - {x}')
    add(f"- **进入产物**：{', '.join(w['target_outputs'])}")
    add('')
add('---')
add('')
add('## 7. 里程碑与决策门')
add('')
for m in milestones:
    add(f"### {m['id']} — {m['title']}")
    add('')
    add(f"- **依赖**：{', '.join(m['dependencies'])}")
    add('- **退出标准**：')
    for x in m['exit_criteria']: add(f'  - {x}')
    add(f"- **解锁**：{', '.join(m['unlocks'])}")
    add('')
add('### 7.1 投稿/发布决策门')
add('')
add('| Gate | 名称 | 核心问题 | 失败动作 |')
add('|---|---|---|---|')
for g in gates:
    add(f"| {g['id']} | {g['name']} | {g['question']} | {g['failure_action']} |")
add('')
add('---')
add('')
add('## 8. 风险登记册')
add('')
add('| 风险 | 内容 | 严重度 | 缓解措施 |')
add('|---|---|---|---|')
for rid,content,severity,mit in risks:
    add(f'| {rid} | {content} | {severity} | {mit} |')
add('')
add('---')
add('')
add('## 9. 论文与成果分流')
add('')
add('### 论文 I — No-Free Temporal and Historical Enrichment in Univalent Foundations')
add('')
add('只收：WP-100–140 的必要核心、WP-200–250、WP-300、WP-610/630、相关文献与红队。极限、LLM、资源、Gödel 只作一句边界或完全移出。')
add('')
add('### 论文 II — Signature-Relative Incompleteness: Context, Intent, Evidence, and Resource Regimes')
add('')
add('主轴候选为 WP-310/340 的签名相对不完备；WP-320/330/400/410/420/440 作为实例或分拆短文。')
add('')
add('### 论文 III — Reflection and Diagonalization in Univalent Type-Theoretic Foundations')
add('')
add('只在 WP-500/510 通过 MS-7 后启动；不得以原“哥德尔空间”作为已成定理。')
add('')
add('### 哲学稿 — Z 铁律、Being/Becoming 与外延—操作完成之分')
add('')
add('承载 WP-450/460 和原判决书的哲学动机；所有数学断言引用论文 I/II 的正式定理。')
add('')
add('---')
add('')
add('## 10. 立即执行批次')
add('')
add('### Batch A — 不得分散的 P0 批次')
add('')
add('1. WP-600：锁定 Agda-unimath 工具链和 smoke test；')
add('2. WP-200：把一般无截面引理整理成实际库接口；')
add('3. WP-210/WP-610：完成 `no-canonical-earlier-event` 编译；')
add('4. WP-650：把构建日志纳入统一验证报告；')
add('5. WP-700：只检索与该中央定理最接近的 no canonical choice / univalence / finite types 文献；')
add('6. WP-710：据检索结果校准贡献；')
add('7. WP-250/WP-800：只在前六项通过后重写论文 I 摘要。')
add('')
add('### Batch B — P1 独立证据批次')
add('')
add('1. WP-230：walking-arrow/core 机器化；')
add('2. WP-300：Snapshot×Provenance 最小模型；')
add('3. WP-330：no-global-choice 到 witness 障碍的专门化；')
add('4. WP-620/630：统一编译。')
add('')
add('### Batch C — 论文 II 定向批次')
add('')
add('按 `WP-310 → WP-340 → WP-400/410 → WP-420/440` 执行。先决定主定理，再吸收实例，禁止直接把所有案例堆入一篇文章。')
add('')
add('### Batch D — 长期探索')
add('')
add('WP-150 与 WP-500/510 可并行做探索性笔记，但不得打断 Batch A 的中央机器化。')
add('')
add('---')
add('')
add('## 11. 每轮研究的强制落盘协议')
add('')
add('每个工作包发生实质变化时，按顺序更新：')
add('')
add('1. `RESEARCH_LOG.md`：做了什么、发现什么、失败在哪里；')
add('2. `CLAIM_LEDGER.md`：新增或改变真理状态；')
add('3. `PROOF_ATTEMPTS.md`：完整证明或失败步骤；')
add('4. `RESULTS.md`：只有稳定结果才进入；')
add('5. `LITERATURE_MAP.md`：最近工作和边界；')
add('6. `HOTT_Z_WBS_REGISTRY_v1.json`：状态、依赖、产物；')
add('7. `CURRENT_RESEARCH_INDEX.md`：只有阶段/入口改变时更新；')
add('8. `verification/`：脚本、日志和哈希。')
add('')
add('禁止只在对话里保留新定义、反例、失败或来源判断。')
add('')
add('---')
add('')
add('## 12. 当前计划的最强结论')
add('')
add('后续研究应以如下联合不相容为主线，而不是以“HoTT 内部爆炸”为目标：')
add('')
add('```text')
add('Target-sensitive information erasure')
add('∧ equivalence/naturality invariance')
add('∧ no genuine enrichment')
add('∧ universal exact recovery')
add('∧ (where claimed) total effective decision')
add('→ contradiction.')
add('```')
add('')
add('数学任务是逐项定义这些谓词、给出最小反例、刻画修复所需的新增结构，并在单价基础中机器验证至少一个 HoTT 特定实例。')
add('')
add('---')
add('')
add('## 13. 机器注册表和依赖图')
add('')
add('- `HOTT_Z_WBS_REGISTRY_v1.json`：全部工作包、依赖、状态、验收和风险的机器可读版本；')
add('- `HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd`：Mermaid 依赖图；')
add('- `HOTT_Z_下一执行批次_P0P1.md`：从本方案抽取的立即执行清单。')
add('')
if validation_warnings:
    add('## 附录 A：注册表生成时的台账引用警告')
    add('')
    for x in validation_warnings: add(f'- {x}')
else:
    add('## 附录 A：台账引用完整性')
    add('')
    add('生成时已核对本计划引用的 Claim/Proof/Result ID 均存在于当前活动台账。')
add('')

master_path = ROOT/'HOTT_Z_后续工作总方案与WBS_v1.md'
master_path.write_text('\n'.join(lines)+'\n', encoding='utf-8')

registry = {
    'schema_version':'hott_z_wbs.v1.0',
    'generated_at':DATE,
    'program_name':'HOTT–Z Relative Incompleteness Research Program',
    'canonical_plan':master_path.name,
    'scope':{
        'positive':'Target-relative representational, naturality, and effective-decision incompleteness in HoTT/univalent foundations and related abstractions.',
        'negative':['No proof that HoTT derives contradiction','No claim that HoTT cannot encode time','No claim that every paradox is caused by erasing time']
    },
    'status_vocabulary':STATUS_VOCAB,
    'verification_levels':[{'id':v,'name':n,'definition':d} for v,n,d in VERIFY_LEVELS],
    'streams':[{'id':s.split()[0], 'name':s, 'purpose':d} for s,d in streams],
    'critical_path':critical_path,
    'milestones':milestones,
    'gates':gates,
    'risks':[{'id':a,'risk':b,'severity':c,'mitigation':d} for a,b,c,d in risks],
    'work_packages':wps,
    'validation_warnings':validation_warnings,
}
reg_path=ROOT/'HOTT_Z_WBS_REGISTRY_v1.json'
reg_path.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Mermaid graph
m=[]
m.append('flowchart TD')
# nodes
for w in wps:
    label=f"{w['id']}\\n{w['title']}"
    safe=label.replace('"','\\"')
    m.append(f'  {w["id"].replace("-","_")}["{safe}"]')
# dependencies
for w in wps:
    for d in w['dependencies']:
        m.append(f'  {d.replace("-","_")} --> {w["id"].replace("-","_")}')
# milestone dotted connections
for ms in milestones:
    mn=ms['id'].replace('-','_')
    m.append(f'  {mn}{{"{ms["id"]}\\n{ms["title"]}"}}')
    for d in ms['dependencies']:
        m.append(f'  {d.replace("-","_")} -.-> {mn}')
# styles by status
status_class={
 'ACTIVE':'active','READY':'ready','PAPER_PROVED':'proved','PAPER_PROVED_CONDITIONAL':'proved','BASELINED':'base','BLOCKED':'blocked','BACKGROUND':'background','EXTERNAL_GATE':'external'
}
for w in wps:
    cls=status_class.get(w['status'],'ready')
    m.append(f'  class {w["id"].replace("-","_")} {cls}')
m += [
 '  classDef active stroke-width:3px;',
 '  classDef ready stroke-dasharray: 5 5;',
 '  classDef proved stroke-width:2px;',
 '  classDef base stroke-width:2px;',
 '  classDef blocked stroke-dasharray: 2 2;',
 '  classDef background stroke-dasharray: 8 4;',
 '  classDef external stroke-width:3px,stroke-dasharray: 4 3;',
]
graph_path=ROOT/'HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd'
graph_path.write_text('\n'.join(m)+'\n',encoding='utf-8')

# Immediate execution batch
next_lines = [
'# HOTT–Z 下一执行批次：P0/P1', '',
'**依据**：`HOTT_Z_后续工作总方案与WBS_v1.md`  ',
'**原则**：在中央 proof-assistant 定理完成前，不扩写新的宏大判决。', '',
'## A. P0 唯一关键路径', '',
'- [ ] WP-600：记录 Agda、Agda-unimath 版本与 commit；建立 smoke test。',
'- [ ] WP-200：把 `noSectionFromFixedPointFreeMonodromy` 对接实际 API。',
'- [ ] WP-210/WP-610：实现并编译 `no-canonical-earlier-event`。',
'- [ ] WP-650：保存命令、stdout、stderr、退出码、依赖哈希。',
'- [ ] WP-700：完成中央定理的最近工作检索。',
'- [ ] WP-710：更新原创性矩阵和允许表述。',
'- [ ] WP-720：执行两轮内部对抗审稿。', '',
'## B. P1 独立证据', '',
'- [ ] WP-230/WP-630：walking-arrow/core 时间反演最小模型机器化。',
'- [ ] WP-300/WP-630：`Snapshot := Unit`、`Provenance := Fin 2` 最小反例。',
'- [ ] WP-330/WP-630：`no-global-choice` 到 witness 提取障碍的专门化。',
'- [ ] WP-220/WP-620：二点严格时间序推论。', '',
'## C. 每项完成后的强制写回', '',
'1. `RESEARCH_LOG.md`；',
'2. `CLAIM_LEDGER.md`；',
'3. `PROOF_ATTEMPTS.md`；',
'4. `RESULTS.md`；',
'5. `LITERATURE_MAP.md`；',
'6. `HOTT_Z_WBS_REGISTRY_v1.json`；',
'7. `verification/` 日志与 manifest。', '',
'## D. 本批次退出条件', '',
'- `no-canonical-earlier-event` 达到 V4；',
'- 至少一个独立实例达到 V4；',
'- 中央定理的 nearest-prior-art 矩阵完成；',
'- 论文 I 的范围门、机器化门、原创性门和红队门可被逐项回答。',
]
next_path=ROOT/'HOTT_Z_下一执行批次_P0P1.md'
next_path.write_text('\n'.join(next_lines)+'\n',encoding='utf-8')

# Update AGENTS with a canonical section, replacing marker if present
agents_path=ROOT/'AGENTS.md'
agents=agents_path.read_text(encoding='utf-8')
marker_start='<!-- MASTER_WORKPLAN_V1_START -->'
marker_end='<!-- MASTER_WORKPLAN_V1_END -->'
section=f'''\n\n{marker_start}\n## 26. 后续工作总方案与工作包治理（WBS v1.0）\n\n### 26.1 规范入口\n\n- 总方案：`HOTT_Z_后续工作总方案与WBS_v1.md`；\n- 机器注册表：`HOTT_Z_WBS_REGISTRY_v1.json`；\n- 依赖图：`HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd`；\n- 当前执行批次：`HOTT_Z_下一执行批次_P0P1.md`。\n\n上述四个文件是后续工作包的规范入口。旧 `HOTT_Z_研究路线图_第三轮.md` 保留为历史路线图，但发生冲突时以 WBS v1.0 为准。\n\n### 26.2 工作包状态与更新纪律\n\n每个研究动作必须归属一个 `WP-xxx`。状态只能使用：`BASELINED`、`PAPER_PROVED`、`PAPER_PROVED_CONDITIONAL`、`ACTIVE`、`READY`、`BLOCKED`、`BACKGROUND`、`PARKED`、`EXTERNAL_GATE`。\n\n任何状态变化必须同时写入：\n\n1. `HOTT_Z_WBS_REGISTRY_v1.json`；\n2. `RESEARCH_LOG.md`；\n3. 若数学真理状态变化，再更新 `CLAIM_LEDGER.md`、`PROOF_ATTEMPTS.md`、`RESULTS.md`；\n4. 若入口或阶段变化，再更新 `CURRENT_RESEARCH_INDEX.md`。\n\n### 26.3 当前唯一关键路径\n\n```text\nWP-000 → WP-100 → WP-110 → WP-200 → WP-210 → WP-600 → WP-610\n       → WP-250 → WP-700 → WP-710 → WP-720 → WP-800 → WP-730 → WP-840\n```\n\n在 `WP-610` 未达到 V4 前，不得以扩写宏大判决替代中央机器化。\n\n### 26.4 投稿门\n\n论文 I 至少通过：范围门、机器化门、原创性门、红队门、变体门、现实桥梁门和复现门。未通过时，只能标记为研究稿或技术报告。\n\n### 26.5 论文分流\n\n- 论文 I：时间、历史、方向、单价无自然选择；\n- 论文 II：语义角色、语境、证据、成本、资源与求解；\n- 论文 III：反射、Lawvere/Gödel、宇宙；\n- 哲学稿：Being/Becoming、Zeno、外延完成与操作完成。\n\n各线不得用另一线尚未完成的主张作为已证前提。\n{marker_end}\n'''
if marker_start in agents and marker_end in agents:
    agents=re.sub(re.escape(marker_start)+r'.*?'+re.escape(marker_end),section.strip(),agents,flags=re.S)
else:
    agents=agents.rstrip()+section
agents_path.write_text(agents.rstrip()+'\n',encoding='utf-8')

# Update current index
index_path=ROOT/'CURRENT_RESEARCH_INDEX.md'
idx=index_path.read_text(encoding='utf-8')
idx=idx.replace('**当前阶段**：第三轮新增材料全量审计、编号治理与后续研究分流完成。',
                '**当前阶段**：第三轮材料审计之后，WBS v1.0、依赖图、里程碑、决策门与 P0/P1 执行批次已建立。')
insert='''\n## 0. 当前规范项目计划\n\n1. `HOTT_Z_后续工作总方案与WBS_v1.md`：后续工作的最高层执行方案；\n2. `HOTT_Z_WBS_REGISTRY_v1.json`：所有 WP、依赖、状态、验收和风险的机器注册表；\n3. `HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd`：完整依赖图；\n4. `HOTT_Z_下一执行批次_P0P1.md`：当前唯一执行清单。\n\n当前关键路径以 `WP-610 no-canonical-earlier-event` 的证明助理编译为中心；在其达到 V4 前，论文 I 不进入“投稿就绪”状态。\n\n---\n\n'''
if '## 0. 当前规范项目计划' not in idx:
    idx=idx.replace('---\n\n## 1. 从哪里开始', '---\n\n'+insert+'## 1. 从哪里开始')
index_path.write_text(idx,encoding='utf-8')

# Append research log
log_path=ROOT/'RESEARCH_LOG.md'
log=log_path.read_text(encoding='utf-8').rstrip()
log_entry=f'''\n\n## {DATE} — 建立 HOTT–Z 后续工作总方案与 WBS v1.0\n\n### 用户任务\n\n根据全部源材料、前三轮审计和既有研究结果，建立后续工作的完整方案与工作包分解，并保证未来可索引、可依赖、可验收。\n\n### 完成内容\n\n1. 建立 9 条工作流、{len(wps)} 个唯一工作包；\n2. 为每个工作包记录目标、当前基础、来源、Claim/Proof/Result、依赖、任务、交付物、验收标准、失败/拆分条件和论文去向；\n3. 建立 {len(milestones)} 个里程碑、{len(gates)} 个决策门和 {len(risks)} 项风险；\n4. 固定中央关键路径：`WP-000 → WP-100 → WP-110 → WP-200 → WP-210 → WP-600 → WP-610 → WP-250 → WP-700 → WP-710 → WP-720 → WP-800 → WP-730 → WP-840`；\n5. 固定论文 I/II/III/哲学稿分流，反射支线不得污染时间主稿；\n6. 建立机器可读 WBS 注册表和 Mermaid 依赖图；\n7. 更新 `AGENTS.md` 与 `CURRENT_RESEARCH_INDEX.md`。\n\n### 新建文件\n\n- `HOTT_Z_后续工作总方案与WBS_v1.md`；\n- `HOTT_Z_WBS_REGISTRY_v1.json`；\n- `HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd`；\n- `HOTT_Z_下一执行批次_P0P1.md`。\n\n### 当前判决\n\n中央 P0 目标仍是 `no-canonical-earlier-event` 的真实 proof-assistant 编译。工作包制度用于阻止范围漂移、证据重复和用修辞替代机器化。\n'''
if '建立 HOTT–Z 后续工作总方案与 WBS v1.0' not in log:
    log += log_entry
log_path.write_text(log.rstrip()+'\n',encoding='utf-8')

# Integrity report
report=[]
report.append('HOTT-Z WBS v1.0 integrity check')
report.append(f'date={DATE}')
report.append(f'work_packages={len(wps)} unique={len(ids)==len(set(ids))}')
report.append(f'dependency_references_valid=true')
report.append(f'claim_proof_result_reference_warnings={len(validation_warnings)}')
for x in validation_warnings: report.append('WARNING '+x)
report.append(f'critical_path_nodes={len(critical_path)}')
report.append(f'milestones={len(milestones)} gates={len(gates)} risks={len(risks)}')
report_path=ROOT/'verification'/'wbs_v1_integrity_check.txt'
report_path.parent.mkdir(exist_ok=True)
report_path.write_text('\n'.join(report)+'\n',encoding='utf-8')

# Manifest and zip
files_to_pack=[
 master_path, reg_path, graph_path, next_path,
 agents_path, index_path, log_path,
 ROOT/'HOTT_Z_SOURCE_REGISTRY.json', ROOT/'HOTT_Z_后续研究可用性总索引_第三轮.md',
 report_path,
]
manifest_path=ROOT/'HOTT_Z_WORKPLAN_V1_MANIFEST.sha256'
manifest_lines=[]
for p in files_to_pack:
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    manifest_lines.append(f'{h}  {p.relative_to(ROOT)}')
manifest_path.write_text('\n'.join(manifest_lines)+'\n',encoding='utf-8')
files_to_pack.append(manifest_path)
zip_path=ROOT/'HOTT_Z_workplan_WBS_v1_20260831.zip'
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in files_to_pack:
        z.write(p,arcname=str(p.relative_to(ROOT)))

print('created:')
for p in [master_path,reg_path,graph_path,next_path,report_path,manifest_path,zip_path]:
    print(p, p.stat().st_size)
print('validation_warnings', validation_warnings)
print('zip_sha256', hashlib.sha256(zip_path.read_bytes()).hexdigest())
