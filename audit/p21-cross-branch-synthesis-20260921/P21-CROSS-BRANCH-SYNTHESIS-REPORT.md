# P21-CROSS-BRANCH-SYNTHESIS-001：P1/P3/P4 综合与 Guarded Cubical 新入口

**状态：** `P3_PAUSED_SAME_CLASS / P1_MINIMAL_EXPRESSIBILITY_POSITIVE_CONTROL / P4_NOT_TRIGGERED_BY_TRANSLATION_GAP_ALONE / GUARDED_CUBICAL_TRANSLATION_CANDIDATE_SELECTED / P22_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM`

## 综合裁决

| 分支 | 当前证据 | 裁决 |
|---|---|---|
| P1 对象理论 | C-325 证明最小 source/boundary/trace/done 接口可在 native Cubical Agda 表达；bare forgetful 不能恢复两给定结构，完整结构可 transport。 | `MINIMAL_EXPRESSIBILITY_POSITIVE_CONTROL`；完整实际绑定仍开放。 |
| P3 实际消费者 | P15/P17 两个不同语料均显式保留任务结构且与 P13 task-different。 | `PAUSE_SAME_CLASS`；不再扩展相邻 consumer。 |
| P4 实现忠实性 | P20 只发现 C-320→C-325 保真翻译未登记；没有 required translation 被实际系统拒绝或错误执行的证据。 | `NOT_TRIGGERED_BY_GAP_ALONE`。 |

因此下一步不能把“缺 bridge”当作 P4 bug，也不能回到 P3 重复搜索。它应转向用户原始时间方向中有明确开放义务的 guarded/clocked → bare HoTT translation。

## 公开与本地侦察

- [Guarded Homotopy Type Theory 项目页](https://cs.au.dk/~birke/ghott/index.html) 与 [Guarded Cubical Type Theory 论文](https://arxiv.org/abs/1611.09263) 确认这是把 guarded recursion 与 cubical equality/HoTT 特征结合的独立理论线，而不是 bare HoTT 的一个未声明运行模式。
- 本地 `GuardErasure.agda` 已机器证明一个**显式源演算＋显式忘却翻译**下的固定点边界（C-92–C-95），但历史方向的实际缺口仍是“标准 guarded/clocked source 到 bare HoTT 的版本固定、字段明确的 translation”。

## P22 候选卡

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P22-GUARDED-CUBICAL-TO-BARE-HOTT-TRANSLATION-AUDIT-001` |
| Source theory | Guarded Cubical Type Theory / Guarded HoTT 的公开论文与项目来源 |
| Target | 固定 bare HoTT 或 native Cubical HoTT target；P22 必须先明确目标，而不能把名称相近的系统合并 |
| 核心问题 | 是否存在一个实际声明的 forgetful/translation route，如何处理 later/clock/guard、path、observable、completion 及其 preservation obligations |
| 正控制 | 若源理论保留 guard/clock 或 translation 明确带相应条件，应归为结构保留/任务不同 |
| 负控制 | 只有当实际 route 确实删除 stage/availability，却把输出作为同一完成任务，才有资格进入 Guard-Erasure 失配证明 |
| 停止 | P22 只读固定一手论文/项目说明与本地 GuardErasure 资产；不自行发明标准 translation、不把一般 lemma 冒充标准 HoTT 反例 |

## 波次定位

P21 的价值是把 P3 的重复风险、P1 的正控制和 P4 的证据门槛统一为一次 branch decision。它选择 P22 作为新的、与用户时间方向直接相连的 ingress，而不是宣称已经命中 HoTT。
