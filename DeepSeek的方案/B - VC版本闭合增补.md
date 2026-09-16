# B - VC 版本闭合增补

> 对应 GPT 原片：`../GPT的方案/HoTT机器统观后续工作方案/003 - FR来源身份重建与版本闭合.md` §9。
> 修改性质：上调紧急度；把 VC-001 从"PLANNED / REQUIRES_MATCHING_GIT_AUTHORIZATION"改为
> "URGENT / 单一副本风险在累积"。

## B1. 紧急度上调

003 片 §9 把 VC-001 列为 `PLANNED / REQUIRES_MATCHING_GIT_AUTHORIZATION`。本增补将其紧急度
上调为：

```text
VC-001 = URGENT_SINGLE_COPY_RISK_ACCUMULATING
```

依据（observed）：`git status --porcelain` 显示 216 个 changed 路径（GLM 快照时 199，现增长 216），
含 807 文件 Coq 归档等不可再生重建证据，且九轮互审的全部文档（GLM独立审计/建议方案/回应、
GPT 回应/方案）也都未提交——即**审计证据链本身**处于单一副本风险。

## B2. 精确授权请求（给所有者）

在 FR-001 完成或并行推进的前提下，向所有者提出一条明确的 commit 授权请求，附：

1. 完整路径清单（`git status --porcelain=v1 -uall` 冻结）；
2. 分批方案：proof package（source/run/index/dependency）逐包枚举所有权 → closure verifier →
   `git diff --check` → 精确 stage → 回读 tree；
3. 审计批次（GLM/GPT/DeepSeek 全部审计文档 + 两个 owner-baseline）独立成批，不与数学包混交；
4. 历史无 receipt 项证据等级不变的声明。

## B3. 与 003 片 §9 的关系

003 片 §9 的分批方法全部保留；本增补只改变紧急度与授权请求的**主动性**（从"等授权"改为
"主动向所有者提出带路径清单的授权请求"）。

## B4. 采纳判据

- [ ] VC-001 状态标为 `URGENT_SINGLE_COPY_RISK_ACCUMULATING`；
- [ ] 已向所有者提交带路径清单的分批 commit 授权请求；
- [ ] 授权后按 003 §9 分批方法执行，不接受目录级 stage。
