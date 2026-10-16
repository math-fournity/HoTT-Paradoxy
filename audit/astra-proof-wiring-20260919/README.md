# HoTT证明证据关系修复：范围、合同与验收

本单元修复形式证明证据校验中的身份、依赖和版本范围问题，不改数学命题。输入为当前源码、原始run、registry、冻结矩阵与本地依赖树；方法为逐包复现、隔离错误实例、真实数据复核及必要的新run。Python测试只认证校验行为，不能代替Agda/Coq/Lean内核。

## 基线与职责

- 项目根为HoTT顶层repo；启动HEAD=`a799e50de80570b9703c539ee16d0b57036fb5ce`，STATE176。
- 当前Goal仍ACTIVE；直接任务为`G-ASTRA-PROOF-EVIDENCE-WIRING-001`，完成后回GEO拓扑/同任务问题。
- 不使用Sub Agent，不写共享治理主库/Host配置，不发布、不push/tag。
- 共享主库main为dirty研究快照；只读其身份并按有效`governance-v3.23.1`读取AGENTS、README、MEMORY index与当前/append owners、system/detailed、manual限制与不变量、truth-sync及Git/tag合同。未将main研究分支当发布真值。
- 本轮已加载closure/governance/verification/detailed-design/requirements Skills及工作流，项目恢复采用同档receipt复认；core generation7、46KC不变。

## C01–C10影响闭包

| 组 | 处置与理由 |
|---|---|
| C01 | UPDATE项目F-011实现/验证状态；保留ruling15每个精确命题先机器证明的要求，不降低门槛 |
| C02 | UPDATE项目证据合同的CLI/范围说明；共享system/design/ADR NO_CHANGE，业务证据实现由本repo拥有 |
| C03 | NO_CHANGE共享workflow和runtime Skill；无需同步新的通用方法 |
| C04 | NO_CHANGE全局/项目AGENTS、加载顺序、core和权限；不以修校验器修改研究成功标准 |
| C05 | UPDATE当前项目Feature/必要README/MEMORY/状态入口；不动其它repo模板 |
| C06 | UPDATE本项目proof validators及确定性负例；不运行fresh AI/模型测试，不把本轮当其证据 |
| C07 | NO_CHANGE config、模型、Hook、Plugin、凭据与访问权限 |
| C08 | NOT_APPLICABLE，无OpenCode或其它Host adapter变化 |
| C09 | UPDATE项目本地实现/方案提交与可恢复快照；不发布共享治理新版本或新tag |
| C10 | UPDATE本单元失败、修复、范围与遗留项；原run/冻结前缀原文不可覆盖 |

remainder=0。此表是影响判断，不是测试PASS。Git存在并发写者：新资产使用独立索引恢复快照；main上的已跟踪目标如需提交使用精确pathspec，不反复占用共享暂存区，不reset他人历史。

## 已复现基线

全局checker先报CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR。继续独立检查40个later包：11 PASS、20个外部模块被报为本地依赖缺口、7个非直接Agda命令被报source mismatch、1个随包文档hash漂移、1个CAND ID解析失败。这些不是全部同一原因；前三个原问题之外的新遗留项也要保留。

当前修复边界：

1. 将被插入冻结前缀的M1行移回追加区，行字节保持；冻结210行必须逐字恢复，不能修改checker放过前缀漂移。
2. 正确解析既有CAND原子ID；统一mark/freeze/closure的身份规则。CAND不自动成为新增C-n数学claim，不虚增numeric计数。
3. 依实际stdout路径区分本地源码和已哈希固定的外部树；本地缺漏、同名不同路径、错误树哈希、symlink逃逸仍必须拒绝。
4. 修复已经发现的字符串伪OPTIONS问题；合法pragma不能从注释或字符串获得。

REAL-LAYER登记仍指旧-02，而当前源码/矩阵已到-03；必须按真实源/run重新资格化并保存primary替代来源，不能重绑旧run哈希。其它Coq/Agda-flat执行合同和文档漂移作为独立遗留问题，不按skip伪称全项目通过。

## 检查范围的准确接口

每条新数学结论的本地证据检查与整个历史registry的Git版本闭合是两种主张。保持默认全局检查的失败行为；增加显式proof ID选择及本地证据模式时，输出必须列准确proof/claim分母、逐包检查、排除范围和Git未认证状态。它仍需完整源码/依赖/身份/冻结行/实际选项检查，不能只跑容易的部分；不能把选定包PASS改称整个repo PASS。

本次研究继续保存全局失败，原总Goal不以局部校验通过而完成。本地模式是实现ruling15与既有LOCAL_UNCOMMITTED状态所需的证据范围区分，不授予修改数学假设或忽略所选包失败的权利。

## 验收与返回条件

- 使用已固定的历史测试fixture避免当前未提交或其它演算包遮蔽目标负例；原11类身份/重放/例外控制不删除。
- 增加真实外部树/错误树/同basename错路径/未列本地模块/symlink、CAND错误输入、字符串/注释伪pragma、选择不存在ID与排除项披露、版本模式不冒充本地模式等控制。
- 重核本线程全部14个主包及其实际导入；必要legacy修复用新run，旧失败保留。
- 只在相应验收实际通过后更新状态；全局其余失败逐项定位，不能靠删除registry项求绿。
- 回GEO模型，不把校验器修复包装成数学发现。
