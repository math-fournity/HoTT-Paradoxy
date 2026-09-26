#!/usr/bin/env python3
"""Register bounded proof-evidence repair without claiming the mathematical Goal complete."""
import argparse,importlib.util,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SID="S-GOV-20260919-ASTRA-PROOF-WIRING"
BASE=".codex/research/hott/sessions/"+SID+"/"
REPORT="Astra继续尝试/断点与证明机制系统检查/第三轮执行报告.md"
s=importlib.util.spec_from_file_location("runtime",ROOT/".codex/tools/cognition_runtime.py");R=importlib.util.module_from_spec(s);s.loader.exec_module(R)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    p=R.plan(ROOT,profile='governance');assert p['revision']==176
    state=json.loads((ROOT/R.STATE).read_bytes());state['revision']=177;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'SOFTWARE_CHECKS_VERIFIED_WITH_SCOPE / NO_NEW_MATH_THEOREM','status':'complete','depends_on':[],'related_records':['S-RES-20260919-ASTRA-POINT-RESTORATION'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
    state['records']['R-ASTRA-PROOF-WIRING-20260919']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'28_TESTS_PASS / 15_SELECTED_PACKAGES_DUAL_LOCAL_CHECK_PASS','status':'complete_with_scope','depends_on':[],'related_records':[SID],'full_sources':[REPORT,'audit/astra-proof-wiring-20260919/acceptance.json','audit/astra-proof-wiring-20260919/literal-options-regression.json'],'scope':'Frozen-prefix repair, legacy identifiers/current primary, exact local/external dependency paths and string-literal pragma qualification. Default global Git/history closure remains open; no HoTT defect or geometry proof.'}
    issue=state['records']['G-ASTRA-PROOF-EVIDENCE-WIRING-001'];issue['lifecycle_status']='CLOSED';issue['status']='closed_with_scope';issue['evidence_status']='VERIFIED_WITH_SCOPE'
    issue['resolution']={'reason':'Original three concrete relation issues repaired; source-option string false positive also repaired. Local per-claim checking remains paired with formal-run qualification; no global PASS claimed.','evidence':[REPORT,'audit/astra-proof-wiring-20260919/acceptance.json','audit/astra-proof-wiring-20260919/tests-final.stderr.txt'],'reopen_if':'A selected source/run/index/dependency counterexample defeats the repaired checks or those contracts change.'}
    state['records']['G-ASTRA-LEGACY-PROOF-QUALIFICATION-001']={'kind':'issue','path':'Astra继续尝试/断点与证明机制系统检查/第三轮执行报告/004 - 遗留范围、治理与返回数学主线.md','lifecycle_status':'OPEN_ISSUE','evidence_status':'OBSERVED_WITH_SCOPE','status':'open','depends_on':[],'related_records':[SID],'full_sources':['audit/astra-proof-wiring-20260919/all-package-relationships-after.json'],'scope':'Seven indirect-driver command bindings, one auxiliary document hash drift, old T3 theory-label mismatch, and full main Git closure. Must be qualified when consumed; unrelated historical failures do not certify or negate the selected native packages.'}
    for key in ['R-ASTRA-BREAKPOINT-20260919','R-ASTRA-POINT-RESTORATION-20260919']:
        state['records'][key]['evidence_status']='SELECTED_LOCAL_FORMAL_AND_RELATION_CHECKS_VERIFIED / GEOMETRY_OPEN / GLOBAL_VERSION_NOT_CLOSED'
        state['records'][key]['related_records'].append('R-ASTRA-PROOF-WIRING-20260919')
    ec=state['execution_control'];ec['status']='ASTRA_PROOF_WIRING_REPAIRED_RETURN_TO_GEO';ec['last_checkpoint_session']=SID;ec['checkpoint_result']='.codex/cognition/checkpoints/'+SID+'/result.json'
    ec['next_minimal_verification']='返回GEO-01/02：资格化真实实数拓扑圆去点与开区间、端部/环境模型。已定位Mathlib.Geometry.Manifold.Instances.Sphere的stereographic与source/target接口（仅SOURCE_INSPECTED_NOT_REPLAYED），先固定可用Lean/mathlib版本和本地重放环境，再给几何正控制与环境端部保持反控制；辅助Lean结果不自动成为原生HoTT结论。继续GEO-03/04及完整四弹U00–U09、G01–G06，线程Goal保持ACTIVE。历史证明命令/文档/标签与全局Git问题另有开放issue，消费相应包时处理，不无界取代数学主线。'
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260919-'+kind+'-177'
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证后端路由
- tier: T3 project-local evidence checker maintenance
- role: 当前用户Goal的canonical状态维护；并行数学/审计路径不改
- load_receipt: audit/astra-breakpoint-20260919/tracking-recovery/LOAD-RECEIPT-final.json + 175/176事务差异及本轮同档复认
- status: ORIGINAL_RELATION_ISSUE_CLOSED_WITH_SCOPE / FULL_GOAL_ACTIVE

上一Goal单元为PROGRESS。当前176及tracked hashes与上一单元一致；core generation7/46KC未变，使用PROTOCOL v3收据复认及逐KC立场，不虚称重新全文读全部STATE。当前任务从G-ASTRA-PROOF-EVIDENCE-WIRING-001恢复；pure-governance profile不复活旧数学队列。
本轮完整加载closure/governance/verification/detailed-design/requirements Skills与工作流，并按有效shared governance-v3.23.1读取AGENTS/README/MEMORY index与相关owner/append、current system/detailed、manual限制/不变量、truth-sync/Git/tag合同。共享main dirty研究快照只读，不改runtime/config/Skills。C01–C10在audit/astra-proof-wiring-20260919/README.md，remainder0。项目AGENTS/rulings/Feature的原F-011要求不降低。

## 实际修复

M1原行移出冻结前缀且原行SHA不变；CAND身份共用解析，REAL-LAYER同当前源码重新捕获-04并登记新primary，旧run不重绑；依赖从basename匹配改为实际路径与哈希固定外部树；伪OPTIONS字符串不再授予safe资格。实际错误源码经非safe内核运行，再在临时合成index fixture中比较旧PASS与新拒绝，未造真实数学收据。
28项测试通过；本线程14主包/C-250–C-264与REAL-LAYER-04共15包分别通过formal-run与本地关系检查。全40 later包关系由11 PASS/20依赖/7命令/1文档/1ID变为32 PASS/7命令/1文档。旧T3错误理论标签被单列；不把32关系PASS当32数学资格。全局Git仍因main未集成新源正确阻塞。
第一次候选接口回归26项6失败；原因和未保存原stderr的边界保留，最终28项原始输出留存。分离两个checker的职责不豁免任一个：当前交付包必须同时过两项；未选择范围不被认证。

## 并发与返回

本轮main继续被并行数学会话推进，涉及矩阵及捕获器；重新检查本方行/源/哈希，不reset他人变化，不发送未授权消息。新资产用独立索引恢复版本；不push/tag/发布。没有新的HoTT缺陷或现实对应结论，下一步实际几何模型，Scope与未完成父目标见策略010。

## element_usage / 影响

closure与baseline定位职责；shared Gate只读限定C01–C10；proof脚本负例和实际15包证明真实修复；canonical checkpoint只写实际状态；Sub Agent未用。T01–10保持原需求，澄清两个checker与本地/Git范围；T11–17项目校验代码/测试/证据；T18–21不部署外发；T22–24正确owner与残余issue；T25不改AI运行；T26并发Git隔离。按PROTOCOL §5兼容legacy全46KC审计，未声称审计分片已原子写入。
'''
    audit=f'# {SID} 核心认知复认\n\ncore-cognition-generation-7；46条。纯证据软件单元，不新增数学理论结论。\n\n- core_change: NO\n- direction_change: RETURN_TO_GEOMETRY\n- panorama_change: EVIDENCE_REPAIR_RESULT\n- essay_change: NO\n- update_decision: 关闭原三处有界问题，历史残余另列，回数学。\n- cross_conflicts: 局部证据通过与全局版本失败分别记录。\n- unresolved: 真实几何/现实桥梁、历史驱动资格、main版本集成。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、后继与反证条件 |\n|---|---|---|---|---|\n'
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
    touched={1:'ALIGNED',2:'ALIGNED',5:'ALIGNED',7:'ALIGNED',17:'ALIGNED',21:'CORRECTED',34:'ALIGNED',37:'TENSION',38:'TENSION',39:'TENSION',41:'ALIGNED',42:'ALIGNED',43:'ALIGNED',44:'ALIGNED',45:'ALIGNED',46:'ALIGNED'}
    for n,(kc,title) in enumerate(headings,1):
        rel=touched.get(n,'NOT_TOUCHED')
        if n==21:why='修复真实资格误接受并让源码、依赖和索引可逐项核；不以exit0或字符串授予safe。'
        elif rel=='TENSION':why='本轮改善证据工程而未找到HoTT缺陷；回航到实际几何，不能用28测试或15包替代发现。'
        elif rel=='NOT_TOUCHED':why='该具体数学、时间、自指或元理论命题本轮未研究；软件校验结果不回答它。'
        else:why='保持精确问题、来源与可证范围；用户原意不由工具绿灯替代，原目标不缩小。'
        ev='第三轮报告、acceptance、真实字符串对照及测试；若所选包有源/依赖/身份反例立即重开；若治理继续取代几何则回航。' if rel!='NOT_TOUCHED' else '第三轮报告的范围；该主题出现具名构造或直接新证据才重新进入。'
        audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
    audit+='''
## 扩展认知复认

001问题发生/简化：实际诊断代码而非预设数学错误。002前提重现：safe资格从真实语法与运行取得；时间节NOT_TOUCHED。003芝诺/圆环/ASK/A-B：本轮只维护ASK证据前提，不宣称过程问题已解。004HoTT真实样子：核variant标签，不把普通Agda或额外公设混成native；自反NOT_TOUCHED。005表达边界/起点/原文：两个校验职责明确，原始run和旧报告不追改；源码资格不是数学新发现。006知识谱：新增历史命令/文档/标签残余进入unknown，不投票判定。007助力阻力：防止沉迷工具修复，限制三处问题及真实负例。008现实骨架：返回实际拓扑/环境/动作，而不是以形式校验闭合现实桥梁。各片内容不修改，source hash变化或新反例触发重评。

## 已走过的路与即将作出的选择

原接线问题确实阻塞了本方15包的相称验证；修复有真实错误实例和负向约束，没有删除历史包求绿。新局部模式公开分母与排除项，数学源码资格仍单独必需。全局其它问题继续OPEN，不把它们混成当前包失败或全部成功。
下一选择为具体实数拓扑模型资格化，支持KC35/37/39/43/44–46。继续无界修全部历史包会偏离父目标，只有后续真实消费时才扩大；不重复Bool/常值控制。Mathlib球面立体投影官方接口已定位但未下载/重放，不作为数学结论；Lean结果与原生HoTT连接仍要独立证明。Goal保持ACTIVE，未完成与未触达轴继续保留。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'software_acceptance':'audit/astra-proof-wiring-20260919/acceptance.json','tests':'audit/astra-proof-wiring-20260919/tests-final.stderr.txt','actual_native_runs':['HoTT/verification/runs/20260919-MP-DEDEKIND-OMEGA-REAL-LAYER-04','HoTT/verification/runs/20260919-QUALIFIER-LITERAL-CONTROL-01'],'new_mathematical_claims':0,'parent_goal':'ACTIVE'}
    files=[]
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260919-'+kind+'-177'
    for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
        b=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else b.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 176$','source_state_revision: 177',body);assert n==1
            k='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260919-'+k+'-177',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户本线程持续Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户本线程持续Goal仍ACTIVE。三处证明证据关系及字符串资格问题已在声明范围修复：28回归通过，本线程14主包与REAL-LAYER-04共15包分别过源码资格/本地关系检查，完整Git与历史驱动/文档/旧标签仍OPEN。当前下一步返回GEO-01/02实际实数拓扑圆/开区间与端部模型；已定位Mathlib Sphere立体投影接口但未重放，须先资格化精确依赖/工具链，辅助Lean不能冒充原生HoTT结论。GEO-03/04及四弹U00–U09/G01–G06全保留。入口：`'+REPORT+'`；旧SUPPLY队列不是本线程当前动作。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            ls=body.splitlines()
            for i,line in enumerate(ls):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):ls[i]='| `DIR-U-ASTRA-BREAKPOINT` | 完成断点检查并持续推进完整四弹策略 | 用户线程Goal | `ACTIVE_GOAL / LOCAL_EVIDENCE_REPAIRED` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-BREAKPOINT-01`、`OUT-ASTRA-RESTORATION-02`、`OUT-ASTRA-PROOF-WIRING-03` | 回GEO实际拓扑与端部/动作保真，不以工具修复代发现 | `Astra继续尝试/四弹一体完整研究策略/010 - 断点检查接入与总目标执行账本.md` |'
            body='\n'.join(ls)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-PROOF-WIRING-03` | 原三处证据关系与字符串资格修复 | `DIR-U-ASTRA-BREAKPOINT` | 实际28测试、15包双检查与真实错误控制 | `VERIFIED_WITH_SCOPE / GLOBAL_VERSION_OPEN` | 当前精确检查范围得到可靠证据核验 | 全历史包、Git发布、现实对应或HoTT缺陷 | `'+REPORT+'`；`audit/astra-proof-wiring-20260919/acceptance.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(b),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'governance','task_ids':[],'authorization':'用户持续Goal要求完成断点与四弹策略并维护治理，本事务登记精确修复范围及返回数学的后继。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,p['snapshot'],payload,apply=a.apply)
    (OUT/('checkpoint-apply.json' if a.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
