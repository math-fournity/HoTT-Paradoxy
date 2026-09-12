#!/usr/bin/env python3
"""Record a real post-draft compaction and update non-state delivery indexes.
All edits are explicit and source-first; prior draft bytes are retained in Git.
Does not alter the mandatory load policy or mutable governance state.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
DRAFT = ROOT / 'artifacts/r017/draft'

def main():
    evidence_path = DRAFT / 'LOADING_EVIDENCE.json'
    evidence = json.loads(evidence_path.read_text())
    if evidence.get('post_draft_compaction_observed'):
        raise SystemExit('Already finalized; refusing duplicate historical annotation')
    evidence['initial_draft_reason'] = evidence['reason']
    evidence['post_draft_compaction_observed'] = True
    evidence['post_compaction_full_reload'] = 'NOT_COMPLETED'
    evidence['reason'] = ('After first draft and core full-text emission, actual context compaction occurred. '
                          'The 122-document dynamic set was never fully emitted, and no full reload '
                          'was completed after compaction. Gate remains NOT_PASSED.')
    evidence['no_claim_of_capacity_measurement'] = True
    evidence_path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + '\n')
    proof_path = DRAFT / 'PROOF_NOTE.md'
    proof = proof_path.read_text()
    old = '工具不认证模型完整性，不伪报发生了本轮未观测的压缩。'
    if old not in proof:
        raise SystemExit('Draft wording changed; refusing blind edit')
    proof = proof.replace(old, '初稿生成时尚未观测到该轮压缩；初稿之后实际发生上下文压缩，且未完成压缩后的全文重新加载。工具的历史输出记录不认证当前模型完整性，也没有测得宿主的精确上下文容量。', 1)
    proof = proof.replace('全球域函数接口', '全域函数接口')
    proof_path.write_text(proof)
    claims_path = DRAFT / 'CLAIMS.json'
    claims = json.loads(claims_path.read_text())
    claims['full_business_cognition'] = 'NOT_PASSED_DYNAMIC_SET_INCOMPLETE_AND_POST_DRAFT_COMPACTION'
    claims_path.write_text(json.dumps(claims, ensure_ascii=False, indent=2) + '\n')
    code_path = DRAFT / 'CODE_AND_RUNS.json'
    code = json.loads(code_path.read_text())
    code['post_draft_annotation_script'] = {
        'path': 'scripts/session/finalize_r017_record.py',
        'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'reason': 'Real compaction after original draft; source and historical draft retained in Git.'
    }
    code_path.write_text(json.dumps(code, ensure_ascii=False, indent=2) + '\n')

    index = ROOT / 'scripts/README.md'
    current = index.read_text()
    if '## R017：' in current:
        raise SystemExit('R017 index already exists')
    index.write_text(current + '''\n\n## R017：所有代码先保存，再执行；局部证书与全域总性\n\n根AGENTS已明确禁止inline代码，包括临时诊断、数据和文档操作；先保存到scripts再按路径调用。仅用于写文件的heredoc不是执行，解释器stdin/c/e和临时shell算法不再使用。\n\n| 路径 | 本轮实际用途 |\n|---|---|\n| `tools/restore_rev16.py` | 安全恢复带.git的rev16 ZIP到新可写目录，继承原4个commit |\n| `session/register_scripts_only_policy.py` | 原位修订AGENTS并保存改前字节、diff和完整指令 |\n| `session/r017_cognition.py` | 解析真实加载集合、连续发出正文、记录缺块；不伪造认识通过 |\n| `research/r017_local_execution.py` | 有限寄存器语法、有界模拟、当前执行证书及显式自环；不是全域停机判定器 |\n| `tests/test_r017_local_execution.py` | 42项实际测试，含错误证书、fuel边界与源先行政策 |\n| `session/prepare_r017_record.py` | 保存初稿、直接规则摘录、来源hash和有限结果 |\n| `session/finalize_r017_record.py` | 保存初稿后真实压缩这一事实，更新交付索引，不改强制加载政策 |\n| `session/finish_r017_checkpoint.py` | 使用既有事务API保存revision17，核新加载集合与旧快照拒绝 |\n| `tools/audit_r017.py` | 对比继承Git基线、校验脚本和结果、检查新代码仅在scripts |\n| `tools/package_workspace.py` | 复用已保存的打包工具，输出.git ZIP与bundle并实际恢复验证 |\n\n实际运行记录在`artifacts/r017/execution/`；当前推导见R017 Session；初稿及后续修订版本在Git中，不删除失败/变更历史。\n\n```bash\npython3 -B scripts/tests/test_r017_local_execution.py\npython3 -B scripts/research/r017_local_execution.py --output /tmp/hott-r017-new-result.json\n```\n\n输出使用新路径，拒绝覆盖原实验。实际9216次包装运行仅为声明有限模型；全域批准器不可能性是另写的带有效通用性/语义可靠性前提的纸笔证明，未运行HoTT内核。\n''')
    delivery = '''# HoTT 工作目录交付 · revision17\n\n工作副本为`/mnt/data/HoTT_workspace_rev17`；由完整rev16 ZIP安全恢复并继承其`.git`，不是重新git init。旧上传目录未改。\n\n## 用户要求的实际变更\n\n根AGENTS禁止新增inline代码，覆盖临时诊断、测试、文档更新、状态保存及打包；所有代码先保存到scripts，再按路径调用。旧“临时执行后再补存”例外删除。先行政策commit是b3575a8；有限研究代码与初稿commit是6c1c528。最终HEAD以本仓库和包外验证报告为准，避免自引用。\n\n## 代码和证据\n\n68份回收源码及300来源映射仍然完整保留，R001缺失源码仍明确缺失。所有本轮程序在scripts下，运行stdout/stderr/argv/时间/退出状态在artifacts/r017/execution。\n\n- `scripts/research/r017_local_execution.py`：确定性机器、有限执行验证、P_(M,u)包装。\n- `scripts/tests/test_r017_local_execution.py`：42项单元测试。\n- `artifacts/r017/RESULTS.json`：256程序×4固定输入×9包装输入＝9216次运行。\n- `.codex/research/hott/sessions/S-ANS-20260910-017-LOCAL-EXECUTION/PROOF_NOTE.md`：完整纸笔论证与范围。\n- `scripts/README.md`：所有历史和新工具的来源/用途。\n\n## 数学结果边界\n\n当前有限执行证书足以核查并交付；HoTT可以形成Dom(p)=Σx Conv(p,x)，并由确定性/唯一输出构造evalOnDom。原始证书不必唯一，只能说输出图为命题。\n\n构造P_(M,u)(0)一步返回，而Tot(P_(M,u))当且仅当M(u)不停机。不存在有效、可靠且最终批准全部真Tot的统一审批器（通用有效语义与相关可靠性为明示前提）；这不由有限实验认证。\n\n没有发现标准HoTT强制把这项坏全域要求用于当前调用。局部Σ输入域是成功对照，所以不宣称找到原创HoTT悖论。下一步应查真实定义/递归准入，而非再添加一个人为万能Gate。\n\n## 认识及权限\n\n第五闭包2416行与三问619行曾完整输出；122文档/1546017字节动态集合未完整输出，初稿后实际发生压缩且未完成重新全文恢复。业务gate未通过，本轮数学继续为待复核局部记录。没有删减强制加载、关闭旧开放事项、运行Lean/Agda、启动其它AI、改模型、访问旧主机或联网搜索。\n\n## Git与恢复\n\nmain，无remote/push。旧4个commit与本轮全部提交可由`git log --oneline`审查。完整ZIP带.git；独立bundle可clone。最终提交后必须干净工作树、git fsck通过、ZIP逐成员回读与另目录恢复、bundle clone恢复相同HEAD。验证写包外JSON，不用提交记录冒充数学认证。\n\n## 自行重放\n\n```bash\npython3 -B scripts/tests/test_r017_local_execution.py\npython3 -B scripts/research/r017_local_execution.py --output /tmp/hott-r017-new.json\n```\n\n标准库即可。后续新增程序遵守scripts-first；保留原输出，别覆盖历史收据。完整会话恢复仍按AGENTS，不将此交付说明冒充必读全文。\n'''
    (ROOT / 'DELIVERY_README.md').write_text(delivery)
    print(json.dumps({'status': 'UPDATED_WITH_POST_DRAFT_COMPACTION_DISCLOSURE',
                      'full_business_gate': 'NOT_PASSED', 'source_scripts_first': True,
                      'mandatory_loading_policy_changed': False}, ensure_ascii=False))

if __name__ == '__main__':
    main()
