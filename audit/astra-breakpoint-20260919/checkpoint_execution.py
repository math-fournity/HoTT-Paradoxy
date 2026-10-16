#!/usr/bin/env python3
"""Canonical checkpoint of the bounded execution; no promotion of the open HoTT claim."""
import argparse
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = "S-RES-20260919-ASTRA-BREAKPOINT-01"
BASE = ".codex/research/hott/sessions/" + SID + "/"
REPORT = "Astra继续尝试/断点与证明机制系统检查/第一轮执行报告.md"
spec = importlib.util.spec_from_file_location("cognition", ROOT / ".codex/tools/cognition_runtime.py")
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

# Human-authored semantic review, in exact KC order; not inferred by keywords.
REVIEWS = [
("ALIGNED", "保留三问的研究姿态；本轮只回答声明的表示/规则样例，不以无命中排除全部HoTT问题。", "报告001/006；出现同一规格的反例时重开候选。"),
("DEEPENED", "固定原生Path、集合层、宇宙与公设控制，阻止只按HoTT名称合并不同演算。", "源码头与CLI资格；若导入规则超出声明则重核整个受影响包。"),
("NOT_TOUCHED", "未建稠密空间中合取过程模型；不能把连接控制当该问题的答案。", "报告006未覆盖轴；有具体过程语义时再触及。"),
("NOT_TOUCHED", "未核运动量子化或一般悖论反证；仅保存本轮有界运行。", "报告004；出现运动模型与相同完成标准后再检。"),
("ALIGNED", "先让具体候选实际运行，再分类表示失配、正常边界或待证；没有事先判HoTT必然正确。", "九个拒绝诊断及两条删点路线；异常合法消费者可改变分类。"),
("ALIGNED", "未把时间约化为稠密性或工具运行时长；现实时间问题仍未触及。", "报告006；若用耗时推出运动定理则本立场失效。"),
("ALIGNED", "使用固定上游源码和实际内核，未以LLM一致性认证理论。", "绕数holdout及run；如source与解释不同则返工。"),
("NOT_TOUCHED", "未展开历史时间悖论全集，只保留启发角色。", "本轮有限包络；新时间构造进入才回评。"),
("NOT_TOUCHED", "未定位HoTT全部时间设定。", "报告006；具名时间机制出现后另立规格。"),
("ALIGNED", "现实相对失配仍是目标，不把必须内部矛盾设成所有问题的唯一标准。", "报告004的四种归因；若排除表示失配的独立价值则修正。"),
("NOT_TOUCHED", "未把理论推演与程序时序做保真比较。", "显式未覆盖；出现对应翻译后再核。"),
("DEEPENED", "通过缺bridge、面条件和消去资格检查ASK前提是否被漏掉；未等同一般ASK决策。", "Path/Local/Elimination控制；合法项漏检将推翻目前解释。"),
("ALIGNED", "让下游输出要求参与判断，常值观察与原见证恢复分开。", "EliminationControls；发现同要求合法恢复会改变相关否定候选。"),
("ALIGNED", "同时保留理论许诺现实能力的B方向，没有把存在声明直接作实际制造。", "报告004；若实际能力与理论输出完成条件闭合则可重新裁决。"),
("TENSION", "认真调查抽象省略，但本轮没有把每次抽象都确认为否定现实；回航到具体任务保真。", "FixedFrame/BoundaryIncidence；GEO-01至04出现完整失配可改变立场。"),
("NOT_TOUCHED", "没有重建Russell的构造过程或形式化其计算合法性。", "报告006自指轴未覆盖；对象语言构造给出后再触及。"),
("ALIGNED", "把最强替代解释加入正控制，避免训练先验直接排除用户问题。", "报告003/006；若忽略合法新现实解释则必须重开。"),
("NOT_TOUCHED", "未证Z铁律对全部理论或时间的全称结论。", "报告004；明确量词与现实任务后再检。"),
("NOT_TOUCHED", "没有把有限Bool合取当稠密空间完成问题。", "QCircle边界声明；建立连续过程模型后再检。"),
("NOT_TOUCHED", "未推出运动离散化或时间悖论。", "本轮源码没有该规格；新模型才触发。"),
("ALIGNED", "原生内核实际运行并保存28次接受/拒绝/失败记录，公开证据门禁失败不隐藏。", "run目录与delivery-verification；哈希或argv不符将撤回对应运行主张。"),
("ALIGNED", "A/B两类方向均保留；不把所有问题都筛成社区软件误用。", "报告004两入口；理论规则反例即使无软件案例也应受理。"),
("NOT_TOUCHED", "没有定位所有时间时序处理位置。", "报告006；具名处理机制出现后再检。"),
("NOT_TOUCHED", "没有求解一般HoTT搜索或两类时序悖论。", "60成员不是该分母；新的搜索规格才触及。"),
("NOT_TOUCHED", "未构造自指编码或证明其难度。", "报告006；真实quotation/证明谓词出现时再触及。"),
("NOT_TOUCHED", "未证明HoTT自身自指的不可越过界限。", "报告006；精确反射体系出现时另检。"),
("NOT_TOUCHED", "未作程序自反到HoTT的保真迁移。", "本轮不涉及该翻译；给出翻译契约后再检。"),
("NOT_TOUCHED", "未研究给定自馈回环的永久不停机。", "无超时外推；固定对象程序后再检。"),
("NOT_TOUCHED", "未实现经济收益自馈回环。", "本轮有限消费者不是自反；有相应机制再触及。"),
("NOT_TOUCHED", "未穷尽历史理论经济学知识谱。", "有限库版本与源码范围已声明；新增来源促重评。"),
("ALIGNED", "拒绝不是不可表达的充分证据；改用参照与端部映射给出结构化表达控制。", "FixedFrame/BoundaryIncidence；若实际任务仍无法被该结构表达则转OPEN而非宣告覆盖。"),
("NOT_TOUCHED", "没有把删点控制当一般稠密性否定的存在定理。", "报告002；具体存在性命题出现后再检。"),
("NOT_TOUCHED", "未重证Russell的无时序前提分析。", "报告006自指未覆盖；具名形式语言后再检。"),
("ALIGNED", "把不存在、无原恢复函数、未找到与校验失败区分，保留显式量词。", "源码签名/九诊断/门禁分层；出现混用则纠正判词。"),
("DEEPENED", "HoTT表达原问题仍待保真，但已实际构造参照、端部交换图与操作语言。", "报告004；完整M/N映射通过才能扩大表达范围。"),
("NOT_TOUCHED", "未把库绕数检查当Gödel或自馈研究。", "报告006；需新的对象语言编码与导出条件。"),
("TENSION", "原始圆环直觉未在本轮成为缺陷证据；不能用小模型遮蔽实际M/N。", "报告004；回航到GEO四义务，保真反例将改变结论。"),
("TENSION", "尚未定位作者思路的具体错误；仅凭表示差异不足。", "报告001/004；若给出同规格错误推导则重开。"),
("TENSION", "本轮仍无HoTT缺陷，不能用28次运行制造发现进展的错觉。", "报告006；下一单元必须新增模型或具体失配，不重复同形控制。"),
("ALIGNED", "先验知识只用于生成候选；独立来源消费者与实际内核负责校验。", "holdout和60成员；新的机制维度应进入后继而非被旧分类排除。"),
("ALIGNED", "既使用AI辅助形式化，也记录其实现错误和未完成事项。", "LOCAL/BOUNDED失败史；若错误被藏则此判定失效。"),
("ALIGNED", "不因工具熟悉而让所有问题变成Bool模型；实际几何被单列OPEN。", "报告002/004；新几何证据优先于现有模板复跑。"),
("ALIGNED", "设置最强反解释及停止条件，阻止凭已投入成本继续同类检查。", "报告006；出现域外反例则调整分类。"),
("ALIGNED", "承认现实及假想现实的解释价值；不以没有现成库模型否定问题。", "报告004；若模型保真义务被无理由删除则回航。"),
("DEEPENED", "用实际参照与端部映射定位可能被舍弃的条件；仍要求同任务比较。", "C-252/C-260源码与GEO-04；若条件并非原任务必需则撤回缺陷解释。"),
("ALIGNED", "执行具体规则和现实结构候选，而非只谈AI能力；实际物理解释仍待完成。", "11包与报告004；若后继再次只有抽象重述，应返回具体M/N模型。"),
]

SESSION = """# Astra 断点与证明机制第一轮有界执行

- session_id: S-RES-20260919-ASTRA-BREAKPOINT-01
- host: Codex desktop local
- model: GPT-6-based Codex；不独立认证后端路由
- tier: T3 research and checkpoint
- role: 用户授权本专题执行及加载修复的当前集成者；其他AI资产保留
- load_receipt: audit/astra-breakpoint-20260919/tracking-recovery/LOAD-RECEIPT-final.json
- authorization: 用户要求更新方案并继续尝试，随后明确“先修复全项目加载与检查点，再执行”
- git_base: 40b1ca78fe0e391201848923e09423808a2178ee
- status: BOUNDED_PASS_EXECUTED / REALITY_BRIDGE_OPEN / GLOBAL_DELIVERY_GATE_PARTIAL

## 实际结果与限制

先恢复加载登记并完成revision172/173真实checkpoint；再执行11个safe主包、9个类型拒绝、明确公设控制、60个生成成员与CLI强制safe资格。28次运行均保留，含4次非预期实现/聚合失败。没有取得HoTT缺陷证据。
C-250–C-260已加入唯一矩阵及registry，主run形式验证11/11通过；包关系函数11/11仍因外部库模块登记规则报错，全局版本与旧claim标识问题未修复。因此不把运行事实升级为完整F-011数学交付完成，不关闭原始现实桥梁。
研究正文与代码/run索引在七分片第一轮执行报告。当前有界pass完成，原始“击落HoTT”目标未实现；不启动无限搜索、旧SUPPLY队列、Sub Agent或发布。

## 压缩复认与来源

T3首次全文读四件套25物理文件、STATE11990行及research其余26文件；截断块曾分块重读。压缩恢复核52文件hash，仅发现revision173事务产生的四处已知变化（两个投影索引、方向主题来源行、STATE），tracked mismatch为0；core generation7/46KC/hash不变，逐KC复认见同事务audit，抽查KC-37至46原文。工具字节覆盖不能认证模型理解。
本轮没有重新解析ZCode历史；使用本专题已完整归档对话和外部AI原件，不把历史指令当新指令。未更新27条历史原文快照的截止范围。

## 授权与治理边界

本轮独立专题不是继续PREMISE-001/GEN-001的canonical步骤；未改其修订片/步骤指针。方案v1.1原件已留存，v1.2与本轮执行未Git提交，不宣称完成SOP的Git版本闭合。未stage/commit/tag/push。
按PROTOCOL §5兼容例外，canonical writer使用完整单文件46-KC audit；登记G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001，不伪称审计分片已原子写入。用户交付报告本身为七分片。

## element_usage 与影响

| 元件 | 实际作用 |
|---|---|
| closure/四件套/STATE | 区分用户原意、历史方向与本轮任务，实际全量读取及复认 |
| research/完备性计划 | 固定八轴、14模板与60成员；开放世界不被有限无命中关闭 |
| proof capture/native kernel | 保存接受、拒绝、实现失败；不把Python计数当原生证明 |
| F-011/版本关系 | 公开真实PARTIAL，不把失败改成PASS |
| canonical checkpoint | 只登记本轮实物与范围，真实事务为应用依据 |
| dev-notes | final前尝试归档；旧重复编号问题独立披露 |
| Sub Agent | 未用，遵守用户禁止 |

T01–T05仅补充当前研究结果与原意解释；T06–T10方案状态/范围更新，无新通用架构或数据库；T11–T12独占Agda源码与有限脚本，固定工具链；T13–T17运行及证据校验，无安全规则改动；T18–T21不部署/发布；T22–T24专题索引、MEMORY当前入口、STATE和投影同事务；T25不修改AI机制；T26精确保留dirty和Git未提交状态。
"""

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--apply",action="store_true");a=ap.parse_args()
    plan=R.plan(ROOT,profile="research")
    assert plan["revision"]==173
    state=json.loads((ROOT/R.STATE).read_bytes())
    old=state["latest_session"];state["revision"]=174;state["latest_session"]=SID
    state["records"][SID]={"kind":"session","path":BASE+"SESSION.md","lifecycle_status":"HISTORICAL","evidence_status":"RUN_OBSERVED_WITH_SCOPE / GLOBAL_DELIVERY_GATE_PARTIAL","status":"complete","depends_on":[],"related_records":[old],"full_sources":[BASE+"SESSION.md",BASE+"RUNS.json",BASE+"CORE_COGNITION_AUDIT.md"]}
    state["records"]["R-ASTRA-BREAKPOINT-20260919"]={"kind":"result","path":REPORT,"lifecycle_status":"CURRENT","evidence_status":"KERNEL_RUNS_ACCEPTED / REALITY_BRIDGE_OPEN / GLOBAL_DELIVERY_GATE_PARTIAL","status":"bounded_pass_complete","depends_on":[],"related_records":[SID],"full_sources":[REPORT,"audit/astra-breakpoint-20260919/delivery-verification.json"],"scope":"11 native packages, 9 type rejections and 60 bounded consumers; no HoTT defeat or completed geometric bridge; global proof gate remains partial."}
    headers=re.findall(r"^### (KC-\d+) · .*? · .*? · (.+)$",(ROOT/"核心认知.md").read_text(),re.M)
    assert len(headers)==len(REVIEWS)==46
    audit="# 核心认知逐条回评：Astra第一轮执行\n\ncore-cognition-generation-7；46条，顺序与manifest一致。单文件为PROTOCOL §5明确兼容路径，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001仍开放。\n\n"
    audit+="- session_id: "+SID+"\n- core_change: NO\n- direction_change: ADD_BOUNDED_EXECUTION_LOCATOR\n- panorama_change: ADD_RUN_FACTS_WITH_OPEN_LIMITS\n- essay_change: NO\n- update_decision: 登记有界执行；不升级HoTT缺陷或完整数学交付。\n- cross_conflicts: 全局proof gate失败；旧理论收费叙述仍需历史审计，不因本checkpoint变为已证。\n- unresolved: GEO-01至04、历史版本与包关系校验问题、Git未提交。\n\n| KC | 主题 | relation | 工作姿态、实际行动、理由 | 证据、下一选择与反证条件 |\n|---|---|---|---|---|\n"
    for (kc,title),(rel,why,evidence) in zip(headers,REVIEWS):audit+=f"| `{kc}` | {title} | {rel} | {why} | {evidence} |\n"
    audit+="""
## 扩展认知逐节复认

| 片/小节 | 姿态、实际动作、偏航与下一选择 |
|---|---|
| 001/在回答以前，先让问题真正发生 | 从用户断点问题构造实际项；不得以接受/拒绝预设结局；新同规格反例会改变解释。 |
| 001/理论为什么要把世界变得简单 | 以参照忘却和商消去检验省略；经济性只是研究视角；若省略与任务无关则撤回缺陷解释。 |
| 002/被改变的前提，怎样在结果里重新出现 | nine negatives配合法母项，检查必要条件；不得把预期拒绝说成矛盾；合法恢复优先。 |
| 002/时间与时序 | NOT_TOUCHED具体时间理论；墙钟时间仅记运行；新的时间模型才触发。 |
| 003/芝诺与圆环 | 端部映射与有理点集已执行，实数几何OPEN；不拿小模型替代现实对象；下一步GEO。 |
| 003/ASK资格 | Path/Partial/消去前提实际消费；不称一般ASK已解；新合法反例会重开。 |
| 003/两种方向 | A/B都保留；没有完成现实桥梁；同任务规格必须补齐。 |
| 004/走进HoTT | 使用原生Cubical而非普通Lean Eq；精确变体不可外推全部HoTT；别的演算新证据可进入。 |
| 004/理论自反 | NOT_TOUCHED反射/Gödel；本轮不以一般循环冒充。 |
| 005/表达界限 | 结构可以进入类型的控制已执行；不是整个用户理论已被表达；GEO保真未完成。 |
| 005/文章作为起点 | 将文字方向落实为11包和60成员；停止重复同形样例；下一轮须有新增信息。 |
| 005/原文保全 | 27条归档保持既有截止，外部AI原件保留；未伪造新对话已经归档；后续扩大范围需canonical reader。 |
| 006/知识谱反观整片 | 上游绕数consumer提供不同来源视角；未证明全知识谱完备；新理论维度是域外入口。 |
| 007/助力与阻力整片 | 公开实现错误和期望未达，保留最强反解释；不让已投入控制数量决定结论。 |
| 008/现实骨架整片 | 保留n/m端部和环境解释；没有宣布现实不能数学化；要求同任务输入、观察、完成条件。 |

## 已走过的路

按原先十四模板广度执行；从PathComplement空性转向Q点集非空控制，从裸对象转向真实参照和端部映射；不是只重复“类型不同”。发现侧未取得HoTT缺陷；完成的是可复核表示/规则样例与精确开放义务。四次实现/聚合失败没有被计作理论反例。门禁出现三个差异，保留而未自行改治理求通过。

## 即将作出的选择

候选一：继续增加同类错误项——信息收益低，拒绝；会违背KC39/43的回航要求。候选二：给实际M/N建立GEO-01至04——服务KC37/44–46，保留OPEN后继；若同任务模型可合法恢复则撤回缺陷候选。候选三：修复历史proof证据门禁——服务KC21，但只改善可复核性，不替代数学发现；另立明确范围。候选四：原有SUPPLY/Gödel步骤——用户未要求本轮复活，保持原状态。当前有界pass到停止条件，不声称总体研究目标完成。

系统化回评：八轴与遗漏在报告006；60成员由冻结文法/逐层分母与独立计数核对，remainder=0仅该族。无限fairness、跨框架翻译、任意依赖项、完整物理操作未覆盖。唯一性恢复、常值商观察、原生闭计算、上游绕数及扩展Reach均为反解释/域外控制。没有发现HoTT essentiality反例，也没有完成现实对应。
"""
    runs={"schema_version":"hott-session-runs/v1","session_id":SID,"execution_report":REPORT,"verification":"audit/astra-breakpoint-20260919/delivery-verification.json","run_receipts":[str(p.relative_to(ROOT)) for p in sorted((ROOT/"HoTT/verification/runs").glob("20260919-*ASTRA-*/RUN.json"))],"mathematical_claim_delivery":"NOT_PROMOTED_GLOBAL_GATE_PARTIAL","git":"LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED"}
    files=[]
    for record,kind in [("I-DIRECTION-PORTFOLIO-20260912","direction"),("I-OUTCOME-PANORAMA-20260912","outcome")]:state["records"][record]["projection_generation"]="20260919-"+kind+"-174"
    direction="| `DIR-U-ASTRA-BREAKPOINT` | 断点、必要结构与证明机制的有界检查 | 用户当前直接指令；本专题对话原文 | `BOUNDED_PASS_COMPLETE / GEOMETRIC_BRIDGE_OPEN` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-BREAKPOINT-01` | 具体几何保真或新规则/消费者失配；不重复同形控制、不预认HoTT缺陷 | `"+REPORT+"` |\n"
    outcome="| `OUT-ASTRA-BREAKPOINT-01` | 11原生主包、9类型拒绝、60有限成员与CLI资格实跑 | `DIR-U-ASTRA-BREAKPOINT` | 本轮源码与28运行收据 | `KERNEL_RUNS_ACCEPTED / GLOBAL_DELIVERY_GATE_PARTIAL` | 本轮固定源码接受/拒绝与有限生成范围完成 | HoTT缺陷、真实圆环不可达、全局版本闭合及公开结论就绪 | `"+REPORT+"`；`audit/astra-breakpoint-20260919/delivery-verification.json` |\n"
    for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
        b=(ROOT/rel).read_bytes();body=b.decode()
        if rel==R.STATE:body=R.dump(state).decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r"(?m)^source_state_revision: 173$","source_state_revision: 174",body);assert n==1
            kind="direction" if rel==R.DIRECTION else "outcome"
            body,n=re.subn(r"(?m)^projection_generation: .+$","projection_generation: 20260919-"+kind+"-174",body);assert n==1
        if rel=="方向追踪/002 - 治理与用户方向.md":body=body.rstrip()+"\n"+direction
        if rel=="全景视野/003 - 当前机器证明包与原生重放.md":body=body.rstrip()+"\n"+outcome
        if rel=="MEMORY/001 - 当前执行队列.md":
            needle="## 当前执行队列（2026-09-16）"
            assert body.count(needle)==1
            body=body.replace(needle,"## 用户当前专题（2026-09-19）\n\nAstra断点机制第一轮有界执行已完成；11个原生主包、9类型拒绝、60生成成员与全部28次运行留存。完整现实桥梁和全局/包关系证据门禁仍OPEN/PARTIAL，没有取得HoTT缺陷证明。入口：`"+REPORT+"`；本轮只记录实际证据，不把旧SUPPLY/Gödel步骤复活为当前任务。加载修复在revision173已闭合，本次研究收尾走新的canonical checkpoint。未Git提交或发布。\n\n## 既有项目队列与历史进展（2026-09-16至19，逐项保留其原时间）")
        files.append({"path":rel,"expected_sha256":R.sha(b),"text":body})
    for name,body in [("SESSION.md",SESSION),("RUNS.json",R.dump(runs).decode()),("CORE_COGNITION_AUDIT.md",audit)]:files.append({"path":BASE+name,"expected_sha256":None,"text":body})
    payload={"schema_version":"cognition-checkpoint/v1","session_id":SID,"load_profile":"research","task_ids":[],"authorization":"用户要求继续尝试，并先修复全项目加载与检查点再执行；本事务仅登记本轮实际范围和未完成义务。","files":files}
    (OUT/"execution-checkpoint-payload.json").write_bytes(R.dump(payload))
    result=R.checkpoint(ROOT,plan["snapshot"],payload,apply=a.apply)
    (OUT/("execution-checkpoint-apply.json" if a.apply else "execution-checkpoint-dry-run.json")).write_bytes(R.dump(result))
    print(json.dumps({k:v for k,v in result.items() if k!="paths"},ensure_ascii=False))

if __name__=="__main__":main()
