<!-- governance-shard:v2
logical_id: ZFC_META_SUBTHEORY_ADEQUACY_FINAL
shard_id: 004
index: ../ZFC元理论子理论充分性最终闭环SOP.md
-->

# 总完成门、跨Session闭包与Goal启动词

## 1. 唯一跨 Session closure

`认知闭包/ZFC-META-SUBTHEORY-ADEQUACY-001.md` 是本方案唯一的活跃 closure。每次新 Session、压缩恢复、换 worktree、来源版本变化、C-id 切换或反例出现时，必须顺序加载：

1. 本 index 与 001–004 全部 shard；
2. 该 closure；
3. 本轮 primary user source、Feature、MEMORY、rulings；
4. `CoreAdequacyCandidateManifest`、当前 TaskCard 和上一个叶的 successor scan；
5. 相关原典、formal source、run receipt 和 Git status。

每个自然单元必须写回：当前 C-id、M/S/Q/P/Bridge/Adequacy、source denominator、形式 target、运行、controls、叶结论、下一自动后继、reopen 条件。只写报告或聊天不算持续执行。

## 2. 局部停止与总体停止的区别

```text
LOCAL_LEAF_CLOSED
    = 一个候选被 payment、source、task fidelity、formalization 或 run 证据排除。
    必须 successor scan；绝不结束 Goal。

CORE_GOAL_ACTIVE
    = 任何 C0–C6 候选仍未穷尽，或 actual core verdict 尚无 machine proof。

CORE_GOAL_COMPLETE
    = 仅在下列总门全部满足时成立。
```

## 3. 总完成门

不得调用 `update_goal complete`、不得写“当前核心问题已经收束”、不得用 final 回答结束研究，除非所有条件成立：

1. `C0` manifest 的所有 candidate family 都有明确 `examined / rejected / live / remainder`，且 remainder 为零，或每个 remainder 有版本固定外部不可取得条件；
2. 至少一个 actual M/S/Q/P contract 已经完成 C1–C5，而不是仅有 application-level、proof-checker 或 toy contract；
3. 对该 contract，C6 已有保存的 kernel proof，得到 `CORE_ADEQUACY_FAILURE_WITH_SCOPE` 或 `CORE_ADEQUACY_DEFENSE_WITH_SCOPE`；
4. `DifferentTaskControl`、`BridgePaidControl`、`Control+` 与 `Control−` 全部实际运行；
5. 若 H0 被用于结论，`SameQ_H0` 与 `UniformJudgment` 已支付；若未支付，H0 已从核心推论中排除；
6. 所有 `SOURCE_GAP`、`COMPILER_BLOCK`、`FORMAL_TARGET_UNDERDETERMINED` 都已触发并记录 successor scan，未被当作全局停机点；
7. Feature、MEMORY、closure、plan、evidence owner、claim matrix、runs 和精确 Git commit 已写回并在 clean target tree 重读；
8. 最终结论明确区分：bare ZFC object-language theorem、foundation adequacy critique、application-source task switch、HoTT comparison 与哲学解释。

如果任一项不成立，Goal 必须保持 active。用户不需要对每片 source gap 重新发出“继续”；Master 自动选择下一 C-id。

## 4. 唯一允许的暂停／阻塞

只有以下两种情况允许把 Goal 停为非 active：

- 研究发起人明确说“暂停”或“取消”；
- 系统真实预算／宿主硬阻塞使任何操作无法执行，且同一硬阻塞在三个连续 Goal turn 重复；此时记录 `BLOCKED` 的精确外部条件，不把它写成研究结论。

来源不足、一个 formalization 失败、单一 compiler 不可用、一个候选被拒绝、尚未得到正结果，均不构成暂停理由。

## 5. 确定性 `/goal` 启动词

~~~text
按照SOP=ZFC-META-SUBTHEORY-ADEQUACY-SOP，持续完成 bare ZFC 的核心理论精度判词，直到得到保存的、版本闭合的最终 machine-proof verdict；不得因任何局部 source gap、proof checker、toy fixture、编译器阻塞、条件性定理、已审来源分母或单个原子单元而停止、暂停或宣布完成。

先完整加载 ZFC-META-SUBTHEORY-ADEQUACY-001、本 SOP index 与全部分片、当前 Feature、MEMORY、rulings、当前 primary user source、CoreAdequacyCandidateManifest、当前 TaskCard、上一个 successor scan 与当前 worktree status。

核心靶固定为：ZFC 或明确 ZFC-founded foundation context M，支撑版本固定的连续统／极限子理论 S，对芝诺／圆环原任务 Q 给出 FormalDone；实际 promotion P 是否在未支付 Bridge 时把 FormalDone 升格为 OriginDone，以及 M 是否有应当要求／检验这一 Bridge 的 actual adequacy responsibility。

按 C0–C6 连续执行：冻结 candidate universe；固定 M→S；固定 Q/OriginDone 与 S/FormalDone；定位实际 promotion P；审计 Bridge；固定 Adequacy contract；最后以 source-to-spec fidelity table、DifferentTaskControl、BridgePaidControl、Control+、Control−和保存的 kernel run 完成 CORE_ADEQUACY_FAILURE_WITH_SCOPE 或 CORE_ADEQUACY_DEFENSE_WITH_SCOPE。H0 只有在 SameQ_H0 和 UniformJudgment 机器化／来源化后才可进入核心 consequence。

每个叶结束后必须做 successor scan，自动选择仍能改变 C0–C6 总判词的下一最小单元；source gap、task switch、run failure、环境缺失或现有控制成功只关闭该叶，绝不结束 Goal。每个自然单元把对象、来源、payment、失败、proof/run、控制、下一后继和重开条件写回唯一 owner、ZFC-META-SUBTHEORY-ADEQUACY-001、Feature、MEMORY、evidence owner 与 Git。

只有第004片总完成门的八项全部满足时，才可以调用 update_goal complete 或称研究完成。任何更早的“收束”只能标为局部控制，不得说 bare ZFC 已被证明有问题、没有问题、不能表示时间，或推出对象语言矛盾。
~~~
