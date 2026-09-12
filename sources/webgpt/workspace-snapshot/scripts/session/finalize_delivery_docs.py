#!/usr/bin/env python3
"""Assemble final deliverable evidence using actual run receipts, without new math claims."""
from pathlib import Path
import hashlib, json, subprocess
ROOT=Path(__file__).resolve().parents[2]

def main():
    audit=json.loads((ROOT/'artifacts/r016/FINAL_AUDIT.json').read_text())
    checkpoint=json.loads((ROOT/'artifacts/r016/checkpoint/COMMIT.json').read_text())
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    results=json.loads((ROOT/'artifacts/r016/RESULTS.json').read_text())
    replay=json.loads((ROOT/'artifacts/r016/R015_REPLAY.json').read_text())
    assert audit['status']=='PASS_DEFINED_SCOPE' and state['revision']==16
    assert checkpoint['status']=='CHECKPOINT_COMMITTED'
    assert results['family_inputs']==254 and replay['result']['group_count']==7
    verification=ROOT/'.codex/verification/scripts-git-r016';verification.mkdir(parents=True,exist_ok=True)
    path=verification/'REPORT.md'
    if path.exists():raise SystemExit('Refusing overwrite')
    scripts=[p for p in sorted((ROOT/'scripts').rglob('*')) if p.is_file()]
    listing={'schema_version':'hott-scripts-inventory/v1','scope':'Current scripts directory, including documentation/manifests',
       'files':[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in scripts]}
    (verification/'SCRIPTS_INVENTORY.json').write_text(json.dumps(listing,ensure_ascii=False,indent=2)+'\n')
    commits=subprocess.run(['git','log','--format=%H %s'],cwd=ROOT,text=True,capture_output=True,check=True).stdout
    report=f'''# scripts回收、Git管理与R016研究交付

## 已完成事项

从提供的revision15完整检查点恢复新目录`/mnt/data/HoTT_workspace_rev16`；先真实Git导入，再代码回收，两个提交后继续研究。原根AGENTS新增本地代码/Git保全条款；未更改Skills、全文加载规则、闭包、三问、Schema或原始数学主张。

回收68份不同源码/扩展payload、300条来源关系，来自14顶层ZIP、10嵌套ZIP及挂载源码。所有payload哈希复查一致；原路径和历史代码未删除。R001原实验仍缺件，未伪造补码。后续新采用代码先写scripts后运行，所有主要运行保留argv/cwd/stdout/stderr/exit/time。

## 实际研究和验证

- 声明Bool/lambda/opaque-ua操作片段，非完整HoTT kernel或cubical实现。
- 36项单元测试通过；254个有限运输链样例：BASIC有2个规范值和252个非规范正常形，显式命题改写254个均正确。
- 无redex与发散分开；没有从FUEL_EXHAUSTED推导不停止。有限链可构造值与等于原项的证书。
- R015原纯脚本7组有限结果实际复现，所有run字段一致；旧无界证明没有因此升级。
- 指定强凭据模式扫描未命中；这不是全量安全认证。未批量执行回收代码。
- 新Python AST检查通过；原导入基线{audit['original_import_files']}个已跟踪文件，变化仅为本轮明确授权的AGENTS与当前治理状态，未发现其它原文件变化。

完整纸笔、源区间、结果、模型边界见`.codex/research/hott/sessions/S-ANS-20260910-016-AXIOMATIC-COMPUTATION/`。

## 实际治理状态

checkpoint已从15提交到16，latest_session为{state['latest_session']}；新进程计划含最新记录、模型源码和结果，旧snapshot写回实际得到STALE_BASE。该检查保证文件路由，不证明完整模型认知。

当前完整业务gate仍NOT_PASSED：闭包内容和三问分段输出后发生真实上下文压缩，动态全集没有完成。本轮数学是有界待复核记录，维护结果已实际完成；没有伪造完整Skill执行或独立Fresh验收。

## Git及交付

到生成本报告之前已存在以下提交（之后还有最终交付commit，见包外验证报告）：

```text
{commits.rstrip()}
```

分支main、无remote、不push；本地历史始于本次导入，不是原主机历史。最后提交后，使用已保存的`tools/package_workspace.py`检查工作树干净、fsck、bundle verify、完整ZIP逐文件哈希、解压后Git和bundle clone。最终结果在包外`HoTT_workspace_rev16_delivery_verification.json`，不会为记录自身HEAD反复修改被跟踪文件。

完整ZIP包含本工作目录及.git，另提供独立.bundle和SHA256。不是把全部Archive.zip多余语料复制一遍；当前研究所需固定资料、治理、旧研究、回收代码、最新结果和Git都在工作包里。
'''
    path.write_text(report)
    print(json.dumps({'report':str(path.relative_to(ROOT)),'script_directory_files':len(scripts),'revision':state['revision']},ensure_ascii=False))
if __name__=='__main__':main()
