# HoTT 工作目录交付 · revision17

工作副本为`/mnt/data/HoTT_workspace_rev17`；由完整rev16 ZIP安全恢复并继承其`.git`，不是重新git init。旧上传目录未改。

## 用户要求的实际变更

根AGENTS禁止新增inline代码，覆盖临时诊断、测试、文档更新、状态保存及打包；所有代码先保存到scripts，再按路径调用。旧“临时执行后再补存”例外删除。先行政策commit是b3575a8；有限研究代码与初稿commit是6c1c528。最终HEAD以本仓库和包外验证报告为准，避免自引用。

## 代码和证据

68份回收源码及300来源映射仍然完整保留，R001缺失源码仍明确缺失。所有本轮程序在scripts下，运行stdout/stderr/argv/时间/退出状态在artifacts/r017/execution。

- `scripts/research/r017_local_execution.py`：确定性机器、有限执行验证、P_(M,u)包装。
- `scripts/tests/test_r017_local_execution.py`：42项单元测试。
- `artifacts/r017/RESULTS.json`：256程序×4固定输入×9包装输入＝9216次运行。
- `.codex/research/hott/sessions/S-ANS-20260910-017-LOCAL-EXECUTION/PROOF_NOTE.md`：完整纸笔论证与范围。
- `scripts/README.md`：所有历史和新工具的来源/用途。

## 数学结果边界

当前有限执行证书足以核查并交付；HoTT可以形成Dom(p)=Σx Conv(p,x)，并由确定性/唯一输出构造evalOnDom。原始证书不必唯一，只能说输出图为命题。

构造P_(M,u)(0)一步返回，而Tot(P_(M,u))当且仅当M(u)不停机。不存在有效、可靠且最终批准全部真Tot的统一审批器（通用有效语义与相关可靠性为明示前提）；这不由有限实验认证。

没有发现标准HoTT强制把这项坏全域要求用于当前调用。局部Σ输入域是成功对照，所以不宣称找到原创HoTT悖论。下一步应查真实定义/递归准入，而非再添加一个人为万能Gate。

## 认识及权限

第五闭包2416行与三问619行曾完整输出；122文档/1546017字节动态集合未完整输出，初稿后实际发生压缩且未完成重新全文恢复。业务gate未通过，本轮数学继续为待复核局部记录。没有删减强制加载、关闭旧开放事项、运行Lean/Agda、启动其它AI、改模型、访问旧主机或联网搜索。

## Git与恢复

main，无remote/push。旧4个commit与本轮全部提交可由`git log --oneline`审查。完整ZIP带.git；独立bundle可clone。最终提交后必须干净工作树、git fsck通过、ZIP逐成员回读与另目录恢复、bundle clone恢复相同HEAD。验证写包外JSON，不用提交记录冒充数学认证。

## 自行重放

```bash
python3 -B scripts/tests/test_r017_local_execution.py
python3 -B scripts/research/r017_local_execution.py --output /tmp/hott-r017-new.json
```

标准库即可。后续新增程序遵守scripts-first；保留原输出，别覆盖历史收据。完整会话恢复仍按AGENTS，不将此交付说明冒充必读全文。
