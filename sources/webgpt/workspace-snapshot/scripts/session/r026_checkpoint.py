"""Save R026 bounded old-source assessment using the existing checkpoint manager."""
from __future__ import annotations
import copy
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
PREFIX = '.codex/research/hott/'
REVIEW = PREFIX + 'reviews/EARLY-GEMINI-001/'
OUT = ROOT / 'artifacts/r026'
SID = 'S-AUD-20260911-026-EARLY-GEMINI'
BASE = '0d7ef5e48c67ee3586606dc45fb9f4ef4a30a685'

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def serial(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2) + '\n'

def put(rel: str, obj) -> None:
    path = ROOT / rel
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(obj if isinstance(obj, str) else serial(obj), encoding='utf-8')

def hashes(paths):
    return {p: sha((ROOT / p).read_bytes()) for p in paths}

def backup(rel):
    dest = OUT / 'before' / rel
    if dest.exists():
        raise FileExistsError(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes((ROOT / rel).read_bytes())

def main():
    spec = importlib.util.spec_from_file_location('r026_runtime', ROOT / '.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load existing cognition manager')
    rt = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = rt
    spec.loader.exec_module(rt)
    before = rt.plan(ROOT)
    if before['revision'] != 25:
        raise RuntimeError('Expected revision25; refuse stale or different workspace')
    state = copy.deepcopy(json.loads((ROOT / (PREFIX + 'STATE.json')).read_text()))
    state.update(revision=26, latest_session=SID)
    state['local_git'].update(inherited_head=BASE, history_origin='Inherited revision25 complete Git archive',
        pre_checkpoint_head=BASE, final_head='Actual Git HEAD and external revision26 delivery receipt')
    impact = []
    for key in before['review_required']:
        rec = state['records'][key]
        if rec.get('status') != 'review_required':
            impact.append({'id':key, 'old_status':rec.get('status'), 'new_status':'review_required'})
            rec['status'] = 'review_required'
            rec['dependency_change_note'] = 'R026 updates audit explanations and evidence links only; dependent mathematical claims are not re-certified.'
    core = [REVIEW + n for n in ['ORIGINAL.md','USER_REQUEST.md','ESSAY_ONLY.md','PROVENANCE.json',
                                 'ASSESSMENT.md','PROOF_NOTE.md','PLAN.md','SOURCES.md','CLAIMS.json']]
    source_paths = ['HoTT/AUDIT_AND_RECONSTRUCTION.md','HoTT/CLAIM_EVIDENCE_MATRIX.md']
    state['records']['A-EARLY-GEMINI-001'] = {
        'kind':'historical_source_reassessment', 'path':REVIEW+'ORIGINAL.md', 'status':'review_required',
        'depends_on':['U-GOAL-20260910-001','U-ASK-20260910-001'],
        'full_sources':core[1:]+source_paths, 'source_hashes':hashes(core+source_paths),
        'source_author':'Gemini attribution by user; original composition date not verified',
        'scope':'Old essay, not IN-006. Six narrow checks and paper reconstruction; no new HoTT paradox or native proof.'}
    evidence = ['scripts/research/r026_early_ideas_checks.py','scripts/history/r026_early_ideas_checks_v0.py',
        'artifacts/r026/CHECK_V1_RESULTS.json','artifacts/r026/CHECK_V1_EXECUTION.json',
        'artifacts/r026/CHECK_RESULTS.json','artifacts/r026/CHECK_EXECUTION.json','artifacts/r026/ENVIRONMENT.json']
    state['records']['V-R026-EARLY-CHECKS'] = {
        'kind':'bounded_logic_resource_specification_checks', 'path':'artifacts/r026/CHECK_V1_RESULTS.json',
        'status':'review_required','depends_on':['A-EARLY-GEMINI-001'],
        'full_sources':evidence[:2]+evidence[3:]+[REVIEW+'PROOF_NOTE.md'],
        'source_hashes':hashes(evidence+[REVIEW+'PROOF_NOTE.md']),
        'native_hott_kernel':'NOT_RUN','scope':'Explicit small Python calculus and finite semantic controls; negative inputs tested; not independent certification.'}
    session_path = PREFIX+'sessions/'+SID+'/SESSION.md'
    state['records'][SID] = {
        'kind':'session','path':session_path,'status':'review_required',
        'depends_on':['A-EARLY-GEMINI-001','V-R026-EARLY-CHECKS','P-RP-B01'],
        'full_sources':core+['artifacts/r026/ENVIRONMENT.json'], 'source_hashes':hashes(core),
        'scope':'User-requested bounded historical-source review and document update; full business cognition not certified.'}
    state['review_due'] = list(dict.fromkeys(state['review_due']+['A-EARLY-GEMINI-001','V-R026-EARLY-CHECKS',SID]+[x['id'] for x in impact]))
    memory = f'''# MEMORY · revision26

当前目录 {ROOT}；继承revision25完整Git，基线{BASE}。最新Session：{SID}。

## 本轮用户要求与材料身份

用户上传一份早期Gemini《HOTT is GONE and GONE with the Wind》，要求考察思路、最好机器验证、有价值则更新文档。本次是历史材料审读，不是IN-006；GEMINI-001仍为IN-005已收到、OUT-005未直接发送，无新通信。

## 实际结果

旧稿的最终判决没有成立。有限性例混淆跨类型相等与元素相等，并误说两个独立线性资源不能各用一次；未知性把没有万能求解器扩大为不能探索；模糊性未定义语义与归约，就宣告Translate不可判定。否定后件本身有效，缺的是实际前提桥梁；不可导不等于否定。现有C-12—C-16早已记录这些错误，本轮不冒称首次发现。

保留的价值是三项不同责任：资源能否被再次兑现；规约到未知答案的发现；实际问题到形式规约的忠实性。当前建议恢复“问题形成与时序语境”的探索：证明a:A正确，不自动证明A忠实表达原问题。规则/需求改版后旧证书是否仍能用，应有真实映射或重新证明；不因日期更新而迁移结论。歧义不一概阻止工作，有共同正确答案可先交付。

## 机器核查

6组新检查实际通过：四行逻辑表、显式线性lambda片段、类型相等不决定选定元素相等的Bool实例、3个目标驱动证明合成、规约欠定/加强、有限有理代数。两份线性正推导通过，8种无效对象被拒；重复引用与独立资源分开。代码先scripts后执行；V0保留，增强后的V1及两次结果/收据均保留。原生Lean/Agda/Rocq/Coq与SMT工具未发现，未安装；没有HoTT内核证明，没有无界定理由有限测试得出。

## 下一动作与文档位置

收敛仍为RP-B01的ReachTrap与FixedPointNoReturn原生内化，不用旧稿替代。探索位可取一项真实的截止/许可需求，明确原任务后比较值规约与过程规约，查证省略影响。不要同时开三套平台，不以新哲学大纲代替构造。

旧稿全文与评估在 .codex/research/hott/reviews/EARLY-GEMINI-001/。HoTT/AUDIT_AND_RECONSTRUCTION的§3.5—3.7已更新；矩阵C-12—C-16仅补本轮证据链接，原数学标签不变。第五闭包、三问、AGENTS、Skills、Schema和此前研究保持原字节。所有原有开放事项保留。

## 范围

有界材料审读已完成；完整动态业务必读集合未全文加载，不声明全套Skill认知验收。文件回读与测试通过不证明模型永远记得全部正文。此次原文是外部AI历史意见，不直接进入第五闭包作为新的用户裁定。
'''
    frontier = '''# HoTT 研究前沿 · revision26

## 收敛位
RP-B01保持：条件对角定理与代码模型已有纸笔/有限证据；原生HoTT的ReachTrap、FixedPointNoReturn及编码对应仍待完成。Gemini同意不替代证明。

## 探索位
早期稿件提示把“问题形成/规约忠实性”恢复为独立切口。选择自然的截止或消费合同，保留原话和语境，比较最终值规约与过程规约；检验旧证明迁移到新规约的资格。先固定小任务，不新建万能翻译器或全能ASK门禁。

## 资源备选与已有失败
普通逻辑引用可以重复，不等于现实凭据可重复兑现。两个独立线性资源各用一次是正例；旧“线性逻辑禁止两证据共存”的错误不再使用。显式State/epoch与consume是正向对照。

## 状态纪律
旧稿三项定罪不成立，保留启发不提升悖论状态；检查、发现、执行三者不能互代。九类时间方向和双向目标不变。R001缺件及其他开放事项保留。IN-005/OUT-005台账本轮不改。
'''
    lessons = (ROOT/(PREFIX+'LESSONS.md')).read_text()+'''
## R026 · 历史思路回收不等于旧错误复活

- 两份线性资源可以各用一次；tensor的独立拥有不等于共享一个一次性许可。跨类型Id必须先满足形成条件，类型路径也不自动给指定元素相等。
- 给定P→R和¬R可以否定P；没有P→R的桥梁不能以哲学标签补足，不可导R也不等于可导¬R。明确联合假设不妨碍最终病因后置。
- 缺少所有问题的总求解器不等于没有任何证明搜索。有效候选枚举能在已有有限证书时成功；有限预算未找到必须记UNKNOWN。
- 翻译成良构语法不等于翻译忠实，不等于已解决问题。语境欠定是信息问题，不自动是停机定理。多个解释有共同答案时可以不等待唯一解释。
- 规约变强后旧证据需要适配或重新证明；形式核验只对明确的规约负责，不能替没有输入的真实意图作保证。
- 全称哲学断言、文学“判决书”、本轮有限模型、原生证明与物理事实分别保存。新增测试不是原作者机器证明，不更改既有研究认定。
'''
    resume = f'''# 接续 revision26

最新{SID}。先按AGENTS执行恢复，此文件不是指定全文的替代。

本轮审读的是旧《HOTT is GONE》，不是Gemini新来信。先读reviews/EARLY-GEMINI-001/ASSESSMENT.md和PROOF_NOTE.md，原文与重构分开。三项定罪已在旧矩阵C-12—C-16受限，本轮不重复认领；6组机器检查通过，原生内核NOT_RUN。

主线继续RP-B01最小模型内化；新探索位是规约忠实性/澄清时序，可用一项自然截止或一次性许可任务比较两份实际HoTT规约。不要只改写成“错误规约也能有正确证明”的口号。需说明省略的现实条件、实际映射、证书适用范围、同任务对照。

资源片段源码scripts/research/r026_early_ideas_checks.py，最新结果artifacts/r026/CHECK_V1_RESULTS.json。代码保存后运行；旧V0与输出不覆盖。别把拒绝一个线性语法树当完整线性HoTT不可能性证明。第五闭包/三问/Skills/Schema不改，现有核验标签不提升，不需要再等待Gemini额度。
'''
    session = f'''# {SID}

日期2026-09-11；实际UTC时间{datetime.now(timezone.utc).isoformat()}。

## 请求与来源
用户附件Pasted markdown(2).md的开头明确要求审视早期Gemini思路、最好机器验证、有用则更新文档。全文497行/32478字节，原始构作日期不明；来源副本ORIGINAL.md逐字节保全。不是当前K01—K03的新回复，不虚构IN-006。

## 实际工作
从rev25完整ZIP恢复可写目录{ROOT}，继承Git。完整读旧稿，回查现有审计owner/矩阵/相关规则，辨认旧结论早有纠错。公开核CMU线性逻辑规则与HoTT官方原文。源码落盘后执行6组检查，正例和故意无效对象并列；第一次执行后加强类型语法检查，保留V0与第一次收据，V1单独运行成功。

## 结论与未知
最终判决不能接受；资源使用、未知发现、模糊问题规约三个问题层次有价值。尤其可恢复规约忠实性与需求版本迁移研究，但没有声称HoTT核心必忽略外部语境。无新HoTT悖论、无原创性声明、无原生证明或外审。

## 变更
新增原文、评估、纸笔说明、计划、来源和代码。更新HoTT/AUDIT_AND_RECONSTRUCTION §3.5—3.7；矩阵C-12—C-16仅证据字段；脚本索引。同步MEMORY/FRONTIER/LESSONS/RESUME/STATE。历史输入和哲学认知owner未改写；原始代码与结果保留；无remote/push/其他AI。

## 读取责任
本轮是显式有界材料审读和文档维护，不是全面业务搜索。根AGENTS、两Skills、治理协议、MEMORY和直接依赖已读取；完整动态文档集合未全文加载，未认证全套业务认知。状态管理器的计划与哈希只验证路由/身份，不证明上下文理解。

## 下一步
继续RP-B01原生模型形成；探索一个原始要求到HoTT规约的具体时序对应案例。保持原输入、业务结果与时间/资源合同，区分表示局限、非法提升和理论正确保护。没有等待Gemini的依赖。
'''
    values = {'MEMORY.md':memory, PREFIX+'FRONTIER.md':frontier, PREFIX+'LESSONS.md':lessons,
        PREFIX+'RESUME.md':resume, PREFIX+'STATE.json':serial(state), session_path:session}
    for rel in values:
        if (ROOT/rel).exists():
            backup(rel)
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
        'authorization':'User requests assessment of the attached early essay, machine checking if useful, and related document updates; standing scripts-first and local Git preservation. No external AI communication.',
        'files':[{'path':p,'text':v,'expected_sha256':sha((ROOT/p).read_bytes()) if (ROOT/p).exists() else None} for p,v in values.items()]}
    put('artifacts/r026/checkpoint/BASE_PLAN.json', before)
    put('artifacts/r026/checkpoint/DEPENDENCY_IMPACT.json', {'newly_marked_review_required':impact,
        'existing_review_required':before['review_required'],'old_source_hashes_not_silently_refreshed':True})
    put('artifacts/r026/checkpoint/PAYLOAD.json', payload)
    put('artifacts/r026/checkpoint/DRY_RUN.json', rt.checkpoint(ROOT,before['snapshot'],payload,apply=False))
    commit=rt.checkpoint(ROOT,before['snapshot'],payload,apply=True)
    put('artifacts/r026/checkpoint/COMMIT.json', commit)
    after=rt.plan(ROOT)
    put('artifacts/r026/checkpoint/AFTER_PLAN.json', after)
    required=set(core+evidence+source_paths+[session_path])
    assert after['revision']==26 and required <= {d['path'] for d in after['documents']}
    try:
        rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)
    except rt.CognitionError as err:
        assert str(err)=='STALE_BASE'
        put('artifacts/r026/checkpoint/STALE_BASE.json',{'status':'REJECTED','error':str(err)})
    else:
        raise AssertionError('Stale checkpoint was accepted')
    summary={'status':commit['status'],'revision':26,'latest_session':SID,'snapshot':after['snapshot'],
        'documents':len(after['documents']),'total_bytes':after['total_bytes'],'required_new_paths_present':True,
        'full_business_cognition':'NOT_CLAIMED','native_hott_kernel':'NOT_RUN',
        'gemini_correspondence_changed':False,'dependency_status_changes':impact}
    put('artifacts/r026/CHECKPOINT_SUMMARY.json',summary)
    print(serial(summary))

if __name__=='__main__':
    main()
