# HoTT 工作目录交付 · revision16

本目录是从用户提供的revision15包恢复出的新可写工作副本。它保存前序研究、当前治理、来源文件、历史代码与本轮研究。不是全部Archive.zip的重新解压，也不是旧主机Git历史的克隆。

## Git

真实本地仓库在`.git/`，branch `main`，没有remote或push。历史从`checkpoint-rev15-import`标签开始；之后的代码回收、研究、checkpoint和交付准备以实际commit保留。解压后可直接执行`git log --oneline`、`git status`、`git fsck --full`。

完整ZIP带.git；独立.bundle也可用`git clone <bundle> <new-directory>`恢复所有分支/标签和提交。最终HEAD与制包校验位于包外delivery_verification.json，避免把自身commit hash循环写进被跟踪文件。

## 代码

- `scripts/README.md`：索引与运行说明。
- `scripts/RECOVERY_MANIFEST.json`：14个顶层ZIP、10个嵌套ZIP与挂载源码，300来源边对应68份独特源码/扩展副本。
- `scripts/recovered/`：历史逐字节代码，原位置继续保留，默认只归档。未经审查不要批量运行。
- `scripts/research/r016_axiomatic_transport.py`：声明片段的typed operational calibration。
- `scripts/tests/test_r016_axiomatic_transport.py`：36项实际单元测试。
- `scripts/session/`：恢复、读源、日志、复放与checkpoint工具。
- `scripts/tools/`：回收、打包、完整性审查。

R001的原始实验源码仍未在附件中取得，不能声称其代码或实验已完整复现。没有把聊天里的短片段重构后伪装成原实验。

## 本轮实际研究

直接阅读`.codex/research/hott/sessions/S-ANS-20260910-016-AXIOMATIC-COMPUTATION/PROOF_NOTE.md`。

原书的命题计算等式不自动变成基本归约。opaque-ua小片段中，Bool transport可成为非规范正常形，但没有证明不可停机。直接等价应用、refl、丢弃未用参数和显式定理改写均给出成功对照。任意有限已知等价链还有可计算的值/证明恢复。

实验包含254个有限运输链输入（252个非空链在BASIC中非规范，定理改写下全部正确返回）；另按原源码和字段重放R015七组有限结果。全部为明确片段/样本，非完整HoTT内核、非独立专家或原创性认证。主目标仍OPEN。

## 重放示例

以下是用户在实际可执行环境中的命令。输出用新的路径，脚本拒绝覆盖已有结果：

```bash
python3 -B scripts/tests/test_r016_axiomatic_transport.py
python3 -B scripts/research/r016_axiomatic_transport.py --out /tmp/hott-r016-new.json
python3 -B scripts/session/replay_r015.py --out /tmp/hott-r015-replay-new.json
```

均仅需Python标准库。本轮未安装或调用Lean/Agda/Coq，也没有声称自建type checker就是HoTT kernel。

## 研究接续与权限

根AGENTS管理两个具名Skill，MEMORY、STATE、前沿与resume指向revision16。用户本轮新增本地Git与脚本回收授权，不包含远端发布、其他AI或修改原主机。数学记录仍待复核，全文动态加载被压缩打断的边界保留，未暗改加载规则。

历史包中的MANIFEST/checksum/install receipt保留为各自版本的证据，不伪装成本轮重跑。当前交付的字节范围、Git状态与恢复结果以包外delivery_verification.json及SHA文件为准。
