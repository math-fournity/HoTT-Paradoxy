#!/usr/bin/env python3
"""Preserve R030 papers, tests and cognition scope using the existing manager."""
from pathlib import Path
import copy, hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
R=P+'reviews/SELF-REFERENCE-002/'
SID='S-RES-20260911-030-REFLECTION-DOMAIN'
O=ROOT/'artifacts/r030'
def sha(b):return hashlib.sha256(b).hexdigest()
def js(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def save(rel,x):
 p=ROOT/rel
 if p.exists():raise FileExistsError(p)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(x if isinstance(x,str) else js(x))
def main():
 state0=json.loads((ROOT/(P+'STATE.json')).read_text());assert state0['revision']==29
 owner='HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md'
 old=(ROOT/owner).read_text()
 section='''\n## 9. 2026-09-11 R030：一个具体的两层反射提案\n\n当前记录：`.codex/research/hott/reviews/SELF-REFERENCE-002/PROOF_NOTE.md`。旧§8对角界限不改；本轮将代码与覆盖义务实际具体化。L₀为有限布尔/自然数表达式，L₁增加调用固定旧版E₀的节点。d₀(x)=not(E₀(x,x))的实际自然数代码为207；旧合法性检查拒绝它，新层合法且能返回。没有任何逐输入等价的旧代码可替代d₀，也没有保语义的L₁→L₀全回译。证明只对这套具体语言和联合要求，非整个HoTT自解释不可能。\n\n正向分阶段语义以(层,子代码)的良基递减保证有限任务完成，无需无限宇宙攀爬。将同一调用明确改成“当前评价器”时有(207,207,k)→(16,207,k+1)→(207,207,k+1)的无限运行不变量；这是另一个自建操作语义，不冒称HoTT核心许可它作为总函数。\n\n机器状态：13项修正后有限测试通过；首轮缓存将Python bool/int视为同键的缺陷与源码保留。共享类型论的Agda无postulate/无sorry草稿未编译；完整语法/语义的HoTT内化未完成。完整321文档加载未通过，本轮为有界局部接续，不以测试或文件检查认证全业务认知。\n\n下一项不再给旧对角换例子：比较具体有限证明检查与全局可靠性反射的类型/范围，保留R026规约、R027全局环境与RP-B01的真实工程缺口。\n'''
 save('artifacts/r030/before/'+owner,old)
 (ROOT/owner).write_text(old.replace('SELF-REFLECTION PRIORITY (R029)','SCOPED REFLECTION CONSTRUCTION (R030)',1).replace('当前问题校准：2026-09-11（§8）','当前问题校准：2026-09-11（§8—9）',1)+section)
 readme=ROOT/'scripts/README.md';before=readme.read_text();save('artifacts/r030/before/scripts/README.md',before)
 readme.write_text(before+'''\n## R030 · 分阶段反射的具体代码与不可回译\n\n- `research/r030_staged_reflection.py`：有明确自然数编码/合法性/固定旧版调用的实验语言，不是HoTT内核。\n- `tests/test_r030_staged_reflection.py`：13项有限检查；首轮失败和typed-cache修复都有源码/Git。\n- `research/r030_formal/ReflectionBoundary.agda`：共享强度的条件对角/回译/Unknown引理，未编译，不含解释器的全部原生形式化。\n- `session/r030_context.py`、`r030_load_range.py`：实际动态加载计划与输出记录，未完成全量接收。\n- `session/r030_fix_cache.py`：保留首次源码后修复bool/int缓存别名。\n- `session/r030_native_probe.py`：本轮实际PATH探测，没有安装或伪造原生运行。\n- `session/r030_checkpoint.py`：原治理器交接，原研究/来源保全。\n- `tools/r030_verify.py`：文件、动态路由与证据身份验证，不证明数学。\n''')
 spec=importlib.util.spec_from_file_location('r030_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
 rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
 base=rt.plan(ROOT);state=copy.deepcopy(state0);state['revision']=30;state['latest_session']=SID
 for rid in base['review_required']:
  state['records'][rid]['status']='review_required'
  state['records'][rid]['dependency_change_note']='R030 adds current owner scope; old mathematical evidence is preserved, not recertified.'
 docs=[R+n for n in ['REQUEST.md','PROOF_NOTE.md','PLAN.md','SOURCES.md']]
 evidence=['scripts/research/r030_staged_reflection.py','scripts/tests/test_r030_staged_reflection.py','scripts/research/r030_formal/ReflectionBoundary.agda','artifacts/r030/RESULTS_FIXED.json','artifacts/r030/EXECUTION_FIXED.json','artifacts/r030/NATIVE_STATUS.json','artifacts/r030/CACHE_CORRECTION.json']
 hs=lambda paths:{p:sha((ROOT/p).read_bytes()) for p in paths}
 rid='P-SELF-REFLECTION-DOMAIN-030'
 state['records'][rid]={'kind':'scoped_research','path':R+'PLAN.md','status':'review_required','depends_on':['P-SELF-REFERENCE-001'],'full_sources':docs+evidence,'source_hashes':hs(docs+evidence),'scope':'Explicit staged object-language construction; no old representative or faithful back-translation; conditional nonstaged divergence','formal_status':'NOT_RUN','workflow_status':'FULL_COGNITION_INCOMPLETE_PROVISIONAL_LOCAL_CONTINUATION','reality_bridge':'SELF_CONSTRUCTED_INTERFACE_ONLY'}
 sp=P+'sessions/'+SID+'/SESSION.md'
 state['records'][SID]={'kind':'session','path':sp,'status':'review_required','depends_on':[rid,state0['latest_session']],'full_sources':docs+evidence,'source_hashes':hs(docs+evidence)}
 state['active']=list(dict.fromkeys([rid]+state['active']))
 state['review_due']=list(dict.fromkeys(state['review_due']+[rid,SID]))
 state['local_git'].update(inherited_head='38e729ce48aef687439365e96eeef68ce058e0d1',pre_checkpoint_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),final_head='See actual Git HEAD and R030 delivery verification')
 mem=f'''# MEMORY · revision30\n\n当前工作副本 `{ROOT}`，继承revision29完整Git；最新Session {SID}。没有新Gemini来信或发信。\n\n## 本轮实际研究\nR029条件对角已具体化为L₀/L₁对象语言：固定旧版E₀可被新层调用；d₀(x)=not(E₀(x,x))具有实际代码207。旧checked入口拒绝它，新层返回true。更强结论：d₀没有任何行为相同的旧程序，故不存在保语义全回译。不是仅仅旧解析器不认识标签。语义以(层,子代码)递减，不需要无限宇宙运行。\n\n单独把调用从固定旧版改绑当前自身，有明确无限执行不变量；这改变了语义，不是标准HoTT已允许的总函数，也不能用它宣称安全分阶段d₀不可计算。三值Unknown可以是诚实有限响应，不等于已解决布尔任务。\n\n## 证据\n完整纸笔定义/证明在reviews/SELF-REFERENCE-002/PROOF_NOTE.md。13项有限测试在修复cache typed键后通过；首轮失败、原代码和修复收据保留。Agda条件草稿无postulate/sorry，但本机无Agda/Lean/Rocq，未编译；不认证原生HoTT解释器。一般结论不从有限计数推出，已知对角机制不认领原创。\n\n## 连续性与加载范围\n保留原71条records及R001来源缺口、R014/015、R016/017、RP-B01和R026—029的所有正反证据。原321文档动态计划未完成，初次合并输出发生真实截断，不冒称全Skill全文gate通过，也不虚构压缩事件。本轮属于有界局部接续，数学/执行/治理状态分开。\n\n## 下一动作\n按新PLAN比较有限证书checker与全局可靠性反射，不重复相同层级d或Trap枚举；仍需具体checker/语法/规格，不以“能谈论自身”推全能反射。R026规约/环境继承、RP-B01原生模型继续保留，同行意见不是继续工作的条件。\n'''
 frontier='''# HoTT前沿 · revision30\n\n## 已推进：自指覆盖有了具体对象语言\nR029的真实代码/覆盖缺口已在L₀→L₁中定位，d₀代码207合法于新层、不属于旧层且没有任何忠实旧替代。固定旧版调用有限完成；当前自调用另有明确不返回不变量。详见SELF-REFERENCE-002/PROOF_NOTE。未找到标准HoTT强制错误改绑的证据，主目标实例仍开放。\n\n## 下一探索\n固定有限证明检查器及一份固定自描述任务，区分有限校验、语义正确性、uniform reflection。先检查确切范围继承，不先新建整个HoTT编译器，不重复同类对角/有限计数。\n\n## 其他前沿保留\nRP-B01的原生模型内化仍OPEN；R026规约/资源与R027Σ继承继续。R014/015正反例、R016归约校准不因本轮变化自动重开。全文输入仍未完成，记录不得升级全业务验证。\n'''
 lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''\n## R030 · 反射引用的版本也是其语义的一部分\n\n- 老评价器的原始域与新增评价器调用的语言分开；同样都是自然数代码，不证明同样的有效范围。\n- 旧入口对不支持代码的默认false不是合法评价证书；checked拒绝与布尔false分开。\n- 无忠实回译的对角证明排除“换个旧程序就行”，比解析失败更强。\n- 阶段索引是语义/覆盖版本，不是每次执行升宇宙或物理时刻。固定旧版能完成，改成当前自身是另一个合同。\n- 自调用轨迹具有不断增长的未执行Not栈，不是完整状态固定点；不从有限24步推非停机。\n- Python缓存typed=False可令bool/int键别名绕过输入检查；本轮实际发现，保留旧源码后改typed=True。这是本模型实现错误，不归罪于HoTT。\n- 无法一次读完全历史时不声称完成；本轮读取门禁未通过。代码和推导逐项保全，不伪造压缩事件或把receipt当理解。\n'''
 resume=f'''# 接续 revision30\n\n最新{SID}。每次仍按原全文协议恢复，本页不能代替正文。\n\nR029的下一动作已经在SELF-REFERENCE-002实做：代码207、分阶段解释、保守扩展、无旧代表/无回译、明确自调用发散正反对照。读PROOF_NOTE和RESULTS_FIXED，不把最初RESULTS(FAIL)当最终，也不删除它。Agda未编译，全321文件门禁未过。\n\n下一项是有限checker与完整reflection的准确类型和保证覆盖范围，不再发信或重做相同trap测试。R026/027/028/029及RP-B01原有结果/未知继续在STATE中。scripts先存再调、Git本地且不push。\n'''
 session=f'''# {SID}\n\n## 输入与工作范围\n用户“继续”，接续R029优先自指提案。恢复了rev29完整Git，保留原HEAD与所有来源。先读取实际AGENTS、双方Skill、协议、MEMORY/FRONTIER/RESUME、R029整套说明及self-reference owner和Schema。完整动态计划321文件/2,678,931字节/193页；只发出前三页且聚合输出截断，未完成全文gate，记录为有界局部接续而非完整Skill认证；没有虚构压缩事件。\n\n## 实质差量\n定义带自然数编码的L_k和E_k。d₀代码207可运行；无任何等价旧程序及全回译的证明。另给改绑当前自身后的精确步进和无限运行不变量；UNKNOWN的严格边界。共有13项有限测试修复后通过；首轮cache类型别名失败完整保留。所有代码先保存scripts后调用，实际日志保留。\n\n## 前提与范围\n用于定义对象语言和纸笔论证的基础为自然数、有限类型、函数、Σ和递归，非HoTT全部语法；没有LEM/神谕。分层不是物理时钟。共享Agda片段未编译，实际原生检查器不存在于PATH，不重复安装。网页仅回查一手规则/已知对角背景，不归属原创。\n\n## 治理\n原文、旧证明/代码保持不变；owner增加R030当前入口，当前记忆由原checkpoint提交。原记录保留，相关源变化标待复核，不提升旧证据。交接完整性与数学真理分离。\n\n## 下一步\n有限checker的自检查与全域可靠性反射，查具体语法/规格/范围。不依赖下一封Gemini信件。\n'''
 vals={'MEMORY.md':mem,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':js(state),sp:session}
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'authorization':'User continues existing research and established scripts-first local-Git save/delivery workflow; no external writes or agents','files':[{'path':p,'text':t,'expected_sha256':sha((ROOT/p).read_bytes()) if (ROOT/p).exists() else None} for p,t in vals.items()]}
 save('artifacts/r030/checkpoint/BASE.json',base);save('artifacts/r030/checkpoint/PAYLOAD.json',payload)
 save('artifacts/r030/checkpoint/DRY.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False))
 res=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True);save('artifacts/r030/checkpoint/COMMIT.json',res)
 after=rt.plan(ROOT);save('artifacts/r030/checkpoint/AFTER.json',after)
 required=set(docs+evidence+[sp,'MEMORY.md',P+'reviews/SELF-REFERENCE-001/PROOF_NOTE.md',P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md'])
 assert required<={d['path'] for d in after['documents']}
 try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
 except rt.CognitionError as e:
  assert str(e)=='STALE_BASE';save('artifacts/r030/checkpoint/STALE.json',{'status':'REJECTED','error':str(e)})
 else:raise AssertionError('Stale write accepted')
 summary={'status':res['status'],'revision':after['revision'],'prior_records':len(state0['records']),'current_records':len(state['records']),'all_prior_ids_retained':set(state0['records'])<=set(state['records']),'dynamic_documents':len(after['documents']),'required_paths':sorted(required),'full_cognition':'INCOMPLETE','native_proofs':'NOT_RUN'}
 save('artifacts/r030/CHECKPOINT_SUMMARY.json',summary);print(js(summary))
if __name__=='__main__':main()
