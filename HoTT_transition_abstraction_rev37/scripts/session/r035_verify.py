"""Verify persisted pause, unchanged history and reload routing; not model understanding."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
SID='S-PAUSE-20260911-035-COMPUTATION-BOUNDARY'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--fresh',action='store_true');args=parser.parse_args()
    baseline=json.loads((ROOT/'artifacts/r035/RESTORE.json').read_text())
    old=json.loads((ROOT/'artifacts/r035/checkpoint/STATE_BASE.json').read_text())
    state=json.loads((ROOT/(P+'STATE.json')).read_text())
    assert state['revision']==35 and state['latest_session']==SID
    assert state['execution_control']['status']=='PAUSED_BY_USER'
    assert all(state['records'][k]==v for k,v in old['records'].items())
    assert state['active']==old['active'] and state['unresolved']==old['unresolved']
    allowed={'README.md','MEMORY.md',P+'STATE.json',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md','.codex/cognition/HEAD.json'}
    same=[];changes=[]
    for rel,original in baseline['source_files'].items():
        f=ROOT/rel
        assert f.is_file(), 'Missing inherited file: '+rel
        (same if digest(f)==original else changes).append(rel)
    assert set(changes)<=allowed, set(changes)-allowed
    spec=importlib.util.spec_from_file_location('r035_verify_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    plan=rt.plan(ROOT);routes={d['path'] for d in plan['documents']}
    rec=state['records'][SID]
    assert all(digest(ROOT/rel)==h for rel,h in rec['source_hashes'].items())
    assert set(rec['full_sources']+[rec['path'],'MEMORY.md'])<=routes
    identity=json.loads((ROOT/'artifacts/r035/REQUEST_IDENTITY.json').read_text())
    assert digest(ROOT/identity['request_path'])==identity['sha256']
    assert json.loads((ROOT/'artifacts/r035/checkpoint/STALE.json').read_text())['error']=='STALE_BASE'
    assert json.loads((ROOT/'artifacts/r035/checkpoint/COMMIT.json').read_text())['status']=='CHECKPOINT_COMMITTED'
    assert 'PAUSED_BY_USER' in (ROOT/'README.md').read_text()
    assert 'PAUSED_BY_USER' in (ROOT/'PAUSE_HANDOFF.md').read_text()
    assert not git('remote')
    if args.fresh:assert not git('status','--porcelain')
    result={'status':'PASS_PAUSE_PRESERVATION_AND_ROUTING','revision':35,'pause_status':'PAUSED_BY_USER',
      'previous_records_unchanged':len(old['records']),'records':len(state['records']),
      'inherited_files_unchanged':len(same),'changed_inherited_files':changes,
      'old_active_and_unresolved_preserved':True,'new_request_hash_matches':True,
      'runtime_routed_documents':len(plan['documents']),'snapshot':plan['snapshot'],
      'all_new_sources_in_loading_plan':True,'stale_write_rejected':True,
      'git_head_at_verification':git('rev-parse','HEAD'),'git_clean':not git('status','--porcelain'),
      'read_scope':'bounded pause assessment; full business cognition not certified',
      'mathematical_experiments':0,'native_formal_runs':0}
    if not args.fresh:
        f=ROOT/'artifacts/r035/VERIFICATION.json'
        if f.exists():raise FileExistsError(f)
        f.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        (ROOT/'artifacts/r035/REPORT.md').write_text('''# R035 暂停保全与认识校准

用户要求暂停。最后实际研究为R034；本轮proof_delta=0，无新实验/原生验证/其他AI。

原用户消息已独立保全，新解释不改写原话。旧81条记录逐值不变；active/unresolved不删除。STATE显式暂停，最新MEMORY/FRONTIER/RESUME同步；暂停不等于关闭课题。旧文件仅更新README过期指针与五状态、HEAD；其余逐文件哈希保留。

首次checkpoint因session kind不正确被拒绝，未写入状态；原脚本与载荷保留，修正后的调用由原治理器提交。旧基线回写已拒绝。原第五闭包、三问、Skills、Theory Schema、主张矩阵及所有旧研究和代码不改。

验证的是文件、路由与版本，不是AI永不遗忘或完整业务全文理解，也不是数学结论真实性。最终Git/ZIP/bundle恢复报告在包外delivery_verification，避免自指哈希。
''',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
