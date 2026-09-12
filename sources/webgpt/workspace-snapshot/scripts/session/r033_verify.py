"""Check inherited bytes, source routing and recorded results. Not a math kernel."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
R=P+'reviews/SELF-REFERENCE-005/'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def runtime():
    spec=importlib.util.spec_from_file_location('r033_verify_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--fresh',action='store_true');a=parser.parse_args()
    rt=runtime();plan=rt.plan(ROOT);state=json.loads((ROOT/(P+'STATE.json')).read_text())
    base=json.loads((ROOT/'artifacts/r033/checkpoint/STATE_BASE.json').read_text())
    required={R+'PROOF_NOTE.md',R+'PLAN.md',R+'SOURCES.md',R+'CLAIMS.json',
      P+'reviews/SELF-REFERENCE-004/PROOF_NOTE.md',P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md','MEMORY.md'}
    routed={d['path'] for d in plan['documents']}
    assert required<=routed and state['revision']==plan['revision']==33
    assert all(state['records'][k]==v for k,v in base['records'].items()),'old record metadata unexpectedly rewritten'
    rec=state['records']['P-DEPENDENT-MIGRATION-033']
    assert all(sha(ROOT/p)==h for p,h in rec['source_hashes'].items())
    clean=subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True)
    basic={'revision':33,'old_records_unchanged':len(base['records']),'new_record_count':len(state['records']),
       'documents':len(plan['documents']),'snapshot':plan['snapshot'],'required_routes_present':True,
       'all_current_source_hashes_match':True,'git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
       'clean_worktree':not clean.strip(),'native_formal':'NOT_RUN','full_cognition':'INCOMPLETE'}
    if a.fresh:
        assert not clean.strip(),'fresh restore dirty'
        print(json.dumps(basic,ensure_ascii=False,indent=2));return
    original=json.loads((ROOT/'artifacts/r033/RESTORE.json').read_text())['files']
    allowed={'MEMORY.md',P+'STATE.json',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md',
             '.codex/cognition/HEAD.json','HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md'}
    changed=[];same=[]
    for row in original:
        rel=row['path']
        if rel.startswith('.git/'):continue
        p=ROOT/rel
        assert p.is_file(),'missing inherited file '+rel
        if sha(p)==row['sha256']:same.append(rel)
        else:changed.append(rel)
    assert set(changed)<=allowed, 'unapproved modification '+repr(set(changed)-allowed)
    for rel in ['HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md',P+'LESSONS.md']:
        previous=ROOT/'artifacts/r033/checkpoint/originals'/rel
        assert (ROOT/rel).read_bytes().startswith(previous.read_bytes()),'old text not retained '+rel
    for name in ['TEST_EXECUTION.json','CONSTRUCTION_EXECUTION.json','CHECKPOINT_EXECUTION.json']:
        d=json.loads((ROOT/'artifacts/r033'/name).read_text())
        assert d['exit_code']==0 and not d['timeout']
    t=json.loads((ROOT/'artifacts/r033/TEST_EXECUTION.json').read_text())
    assert 'Ran 29 tests' in t['stderr'] and '\nOK' in t['stderr']
    results=json.loads((ROOT/'artifacts/r033/RESULTS.json').read_text())
    assert sum(i['natural'] for i in results['same_swap_family'])==2
    assert sum(i['natural'] for i in results['trivial_to_swap'])==0
    assert results['order']['on_0_first_order']==2 and results['order']['on_0_reverse_order']==1
    stale=json.loads((ROOT/'artifacts/r033/checkpoint/STALE.json').read_text())
    assert stale['error']=='STALE_BASE'
    result=basic|{'status':'PASS_ARCHIVE_AND_ROUTING_CHECKS','inherited_files_unchanged':len(same),
                  'changed_inherited_files':changed,'test_count':29,'old_record_values_unchanged':True,
                  'prefix_preservation':True,'stale_write_rejected':True,
                  'scope':'These are archival and program-result checks, not independent mathematics verification'}
    dest=ROOT/'artifacts/r033/VERIFICATION.json'
    if dest.exists():raise FileExistsError(dest)
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    report=f'''# R033 · 实施与验证报告

状态：PASS_ARCHIVE_AND_ROUTING_CHECKS。数学身份仍为纸笔推导与有限模型检查，原生HoTT/Agda未执行。

- 用户“继续”接续R032的依赖上下文问题，实际得到Σ迁移条件、自然性、路径作用不可无损擦除及set值安全擦除判据。
- Python 29项测试通过；4张局部自表中2张自然，平凡到翻转族0张，两个对象16组表中2组相容，18个有限回路作用核查。
- 原{len(base['records'])}项记录内容逐项未变，当前{len(state['records'])}项。
- 原{len(same)}份非Git文件保持原字节，仅{len(changed)}项既有文件修改，详见VERIFICATION.json。专题/脚本索引/LESSONS为追加，历史前缀保留。
- 新证据source_hashes全部匹配，新进程动态路由包含R026/R032/R033。旧快照重试实际被拒绝。
- 先有保全提交，最终HEAD与干净状态由交付脚本在最终提交后认证，当前报告不虚构未来commit。
- 本轮全文核心读出之后真实压缩，动态全集未完成；有界局部接续，不认证完整业务Skill。
- 没有新Gemini信、未启动其他AI、无远端或push；所有新算法代码先保存scripts再执行。
'''
    (ROOT/'artifacts/r033/REPORT.md').write_text(report,encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
