#!/usr/bin/env python3
"""Apply R040 handoff state using the original runtime, preserving all prior record values."""
from pathlib import Path
import copy,hashlib,json,subprocess
from govern import load
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'artifacts/r040';P='.codex/research/hott/';SID='S-HANDOFF-20260911-040-CHECKPOINT';S=P+'sessions/'+SID+'/'
def enc(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x):
 p=OUT/name
 if p.exists():raise FileExistsError(p)
 p.write_text(enc(x))
def main():
 rt=load(ROOT);base=rt.plan(ROOT);old=json.loads((ROOT/(P+'STATE.json')).read_text());assert old['revision']==39
 state=copy.deepcopy(old);state['revision']=40;state['latest_session']=SID
 paths=['governance/ENTRYPOINT.md','governance/PATHS.json','governance/WORKFLOW.md','governance/EXCHANGE_PROTOCOL.md','governance/HANDOFF_RESEARCH_STATUS.md','governance/VERSION_NOTES.md','governance/FRAMEWORK_MANIFEST.json','governance/HANDOFF_README.md','exchange/README.md','exchange/BASELINE.json','artifacts/r040/DELTA_TEST_EXECUTION.json','artifacts/r040/LEGACY_TEST_EXECUTION.json','artifacts/r040/FRAMEWORK_TESTS.json',P+'sessions/S-HANDOFF-20260911-040-CROSS-AI/REQUEST.md',P+'sessions/S-HANDOFF-20260911-040-CROSS-AI/SESSION.md']
 paths += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/'scripts/handoff').glob('*.py'))]
 session='''# R040 跨AI完整交接 checkpoint\n\n用户明确请求保全全部材料、完整治理说明、百万上下文导览和每次增量审计ZIP。最后数学研究仍R039，没有新增数学定理或实验。\n\n当前项目从最新R039完整Git包恢复；所有既有研究record逐值保留。增加中立governance入口但原.c​odex只是兼容物理目录，仍只有一套cognition_runtime；exchange为默认独立交流总目录。所有新代码先存scripts再执行。\n\n保全以当前/mnt/data初始实物清单为范围：324份文件，52个ZIP，总748544776字节，经原压缩字节去重为217002151字节；全部原件重建SHA一致。外层README和清单说明未挂载/过期源不被伪造补齐。\n\n16项新增传输测试通过；原73项治理测试70通过3个旧断言失败，失败与原源码保留。原运行器56项通过，另测当前多页完整读出、当前政策和替代目录入口。新AI理解、原生数学和所有历史结论均未因此认证。\n\n该Session是不可覆盖的交接记录；后续真实接手和研究需要新Session，不重写本轮。最终Git和包哈希在外层交付清单，避免提交哈希自引用。\n'''.replace('\u200b','')
 state['records'][SID]={'kind':'session','path':S+'SESSION.md','status':'review_required','depends_on':[old['latest_session']],'full_sources':paths,'source_hashes':{p:sha(ROOT/p) for p in paths},'scope':'Portable full handoff and incremental audit tooling, no new mathematics','cognition_status':'BOUNDED_HANDOFF_GOVERNANCE_REVIEW_NOT_FULL_RESEARCH_COGNITION','mathematical_status':'UNCHANGED_FROM_R039'}
 state['review_due']=list(dict.fromkeys(old['review_due']+[SID]))
 state['execution_control'].update(status='HANDOFF_READY',request_path=P+'sessions/S-HANDOFF-20260911-040-CROSS-AI/REQUEST.md',last_research_session=old['latest_session'],reason='User requested complete transfer to another AI; no new research in R040.',background_work=False,execution_at_delivery='CHECKPOINTED_NOT_RUNNING_BACKGROUND')
 state['local_git'].update(inherited_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),history_origin='Inherited R039 complete Git history; no reinitialization',final_head='Resolve handoff-r040 and manifests/HANDOFF_IDENTITY.json in the full handoff package')
 memory='''# MEMORY · revision40 · 完整跨AI移交\n\n状态 HANDOFF_READY。最后实际数学工作为R039。当前项目根由governance/PATHS.json和scripts入口解析，不使用旧/mnt/data绝对根。完整交接包外层README为接手总说明；本记忆不替代原文。\n\n## 共同认识和成果不变\nHoTT的已有能力、共享计算界限与具体理论化新增失真分开；保留双向现实相对目标、ASK与Z原话、正反例和独立思考。原89项records逐值保留，原生证明/完整认知的历史未验收状态不升级。\n\n## R039回源\n`.codex/research/hott/reviews/SILENT-STEPS-001/PROOF_NOTE.md`：普通弱互模拟本例保may不保must；无限单边Bad不传递；正确Delay和有限跳过预算为正向对照。R038当前态提升迁移Acc、有限前缀不保证无限相容、R036抽象假路径、R033—34路径作用、R029—32反射、RP-B01和R026均沿旧链保留。\n\n## R040实际新增\n平台中立governance入口不依赖Codex插件，原.c​odex物理存储与唯一原引擎保留。exchange/是默认增量目录，用户指示时从共同Git基线导出；hash/patch/payload/薄bundle共同校验，导入只建隔离副本，不自动合并或接受审计。完整日常流程在governance/WORKFLOW.md，协议在EXCHANGE_PROTOCOL.md。\n\n324份当前挂载原件全部无损保全，原ZIP可按原SHA重建；原机和过期会话缺件不伪造。大上下文接手看外层onboarding有序全文卷，实际容量/读入由新AI确认，不因哈希或EOF认证理解。\n\n## 检查边界\n16项增量传输测试通过。旧治理73项中70通过3项陈旧断言失败；原运行器56项全部通过，新增当前分页/增长/入口检查通过；VERSION_NOTES记录原因，失败日志保留。没有原生HoTT内核执行，没有新数学研究。\n\n## 后续\n新AI完成真实全文恢复和工具验收后自主继续。下一未执行候选为Delay结果等价上的bind与race/timeout的下降条件；不要重复R039自环枚举。不等待Gemini，不凭历史权限自动push/发信/改模型。\n'''.replace('\u200b','')
 frontier=(ROOT/(P+'FRONTIER.md')).read_text().replace('# FRONTIER · revision39','# FRONTIER · revision40 · 交接／数学前沿仍R039',1)+'\n当前为用户要求的跨AI交接，下一数学动作未执行。接手按governance/ENTRYPOINT.md、外层README和当前全文计划恢复；增量交流按exchange/。\n'
 lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''\n## R040 · 完整交接与增量审计\n\n- .codex是物理兼容路径，不是跨平台AI必须识别的入口；一套状态、显式路径映射，不能克隆两份可变memory。\n- 原Zip包含全部字节但并非平台全聊天导出；当前挂载与历史引用分开。无损去重必须能重建每份原ZIP相同SHA，不能只重压缩猜同一文件。\n- 增量包绑定base/head和删除清单；已导出不等于已审计，不推进共同基线；接收在独立副本验证。\n- 旧单页测试的预算会随文件增长失效，旧MANIFEST可能未更新；保留失败并用当前语义复核，不能篡改历史为PASS。\n- 更大上下文不自动等于全文已经读入；生成卷/哈希/EOF不是认知收据。\n'''
 resume='''# RESUME · revision40\n\n先读完整包外层README、项目AGENTS与governance/ENTRYPOINT.md。通过scripts/handoff/govern.py生成当前全文计划，先第五闭包再三问并读所有实际依赖；必要时一次载入onboarding核心全文卷并核快照。不要把旧报告中的根路径当当前根。\n\n原最后研究R039；新AI如需继续，从原STATE/FRONTIER列出的Delay结果等价与race/timeout选有判别力的动作。原89条记录未删。R040只交接，没有新数学。\n\n默认exchange/rounds/<id>独立存用户请求、实际增量、审计问题和运行账本；用户要求时commit后导出，仅传共同基线后的变更。首次共同基线tag为handoff-r040，实际HEAD见外层manifest。导出不自动认可，接收不自动合并。\n\n已知旧治理测试3处陈旧断言失败见VERSION_NOTES；不要复制为新错误或伪称历史全部通过。R001原源缺口和原生工具未运行状态继续保留。\n'''
 files={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':enc(state),S+'SESSION.md':session}
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'authorization':'Current user explicitly requests full cross-AI handoff, portable governance and incremental ZIP audit tooling; preserve all research records.','files':[{'path':p,'expected_sha256':sha(ROOT/p) if (ROOT/p).exists() else None,'text':t} for p,t in files.items()]}
 save('CHECKPOINT_BASE.json',base);save('CHECKPOINT_PAYLOAD.json',payload);save('CHECKPOINT_DRY_RUN.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False));result=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True);save('CHECKPOINT_RESULT.json',result)
 new=json.loads((ROOT/(P+'STATE.json')).read_text());assert all(new['records'][k]==v for k,v in old['records'].items());assert new['unresolved']==old['unresolved']
 after=rt.plan(ROOT);save('CHECKPOINT_AFTER_PLAN.json',after)
 try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
 except rt.CognitionError as e:assert str(e)=='STALE_BASE';stale=True
 else:raise AssertionError('Old snapshot was accepted')
 save('CHECKPOINT_VERIFICATION.json',{'status':result['status'],'revision':40,'old_records_preserved':len(old['records']),'current_records':len(new['records']),'unresolved_preserved':True,'stale_base_rejected':stale,'new_documents_routed':set(paths+[S+'SESSION.md'])<={d['path'] for d in after['documents']},'mathematics_unchanged':True,'model_understanding':'NOT_CERTIFIED'})
 print((OUT/'CHECKPOINT_VERIFICATION.json').read_text())
if __name__=='__main__':main()
