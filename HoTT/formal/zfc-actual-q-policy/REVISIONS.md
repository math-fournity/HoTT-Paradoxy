# Q／P／A／B／ZFC-1 形式化包的修订与失败谱系

## 2026-10-04：第一份 Lean 草稿被拒绝，改用语义任务等价

保留文件 [ZFC1IllusionPolicy.lean](ZFC1IllusionPolicy.lean) 是初始草稿，proof id 为 `MP-ZFC-ACTUAL-Q-POLICY-001` 的开发身份。其 `same_Q_transports_P_to_HoTT` 试图从 `QFingerprint` 的来源字段等式运输 policy；Lean 实际在该处报 `Application type mismatch`，后继使用 `sorry` 的输出不能充当成功证明。

这不是可忽略的语法问题。即使把该行改到能通过，`SOURCE_UNOBSERVED` 等证据标签的相等也不构成两个任务相同。修复不是在原 proof 上补洞，而是新增 [ActualQPolicy.lean](ActualQPolicy.lean)：

```text
SameActualQ = Nonempty TaskEquiv
TaskEquiv preserves State/input/step/observe/formalDone/originDone.
```

当前 delivery 只使用 `MP-ZFC-ACTUAL-Q-POLICY-002`。第一稿和其拒绝 run 保留为失败证据，不能用 `#print axioms` 的后续输出掩盖编译失败。

## 2026-10-04：将严格任务等价从唯一入口改为反类比控制

上一版把 `SameActualQ = Nonempty TaskEquiv` 当作强 P 可以跨案例运输的唯一入口。它正确阻止了“字段标签相同”被误报为同一个任务，却对圆环、Zeno 运动与 HoTT 程序这样的跨领域比较过强：它们未必有可逆的状态空间等价，不能因为缺少这种等价就预先把一切来源级比较关掉。

修复不是降低证据门槛，而是把两个义务分开：

```text
TaskEquiv
  = 最强的反类比控制；它给出 PolicyScopeWitness 的一个充分实例。

PolicyScopeWitness
  = formalDone 的强 P 已在 Zeno 侧获准时，为什么 P 也可在 HoTT 侧适用。
```

`PolicyScopeWitness` 在 Lean 中只是一个范围蕴含，不含书目、作者、历史接受或现实语义；它能被称为“来源归属”只有在独立 source card 给出相称证据时。`source_scoped_P_with_B_is_inconsistent` 将它和 B 明确列为前提，`zfc1_same_actual_Q_P_with_B_is_inconsistent` 保留为严格 `TaskEquiv` 的特例。新收据 `20261004-MP-ZFC-ACTUAL-Q-POLICY-002-06` 在澄清该来源边界后重新捕获并精确重放。

## 2026-10-04：把“ZFC 缺少时间观察”收紧为语言与桥接边界

“ZFC 缺少时间维度”若被写成“ZFC 不能表示时间、自然数步骤或计算”，既不忠实于集合论的表达能力，也无法由本项目现有来源或 Lean 内核证明。为保住用户所指的真正问题，同时避免这个过强说法，本轮新增 [ZFCObservationLanguage.lean](ZFCObservationLanguage.lean)。

它把 base theory 的输入固定为 membership model，另把 `originDone` 放进 expansion。内核证明：在已有 base model 的条件下，任意指定状态可以有 membership 不变而 Done 相反的两个扩张；但一旦指定 `CompletionBridge`，该 bridge 会唯一决定 Done。它因此精确支持“未付 completion bridge 时，基础语言不会替使用者决定原过程完成”，而不是“ZFC 绝对没有时间”。

该文件的 `MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001` 是 C-362 的独立 proof package；它是 C-359 的解释性中间边界和正控制，不把 `ZFCOneUse` 的来源前提自动变成实际事实。

## 2026-10-04：把“同一 Q 异判”从口头结论固定成条件性政策 theorem

研究发起人的终局逻辑并不止于“ZFC 没有决定 Done”。还包括：若同一个完整 Q 在芝诺侧被判原任务已解决，在 HoTT 侧又被判必须补 bridge，则同一基础观察政策无法保持统一。候选 worktree 中已有同形 Lean 代码，但它仍是 `CANDIDATE_NOT_CURRENT`，并且不能直接替代本分支的证据闭环。

本分支因此重建并独立运行 [ZFCCompletionPolicyUniformity.lean](ZFCCompletionPolicyUniformity.lean)。C-363 明确给出 full profile equality、两个 judgment 与 `QUniform` 的条件 theorem，也保留“只共享 requiresBridge 时可以合理异判”的反控制。它不把当前 IEP、SEP、Norton、圆环或 Cubical Agda 来源字段填成 true／false；实际映射仍须由 source card 支付。

## 2026-10-04：从“未定义 Done”深化为“未付 P 有保字段反模型”

C-362 说明 membership-only base theory 不会决定一个外加 Done；但用户的目标还要求解释为什么 `P := Done_formal → Done_origin` 不是能从子理论数学结论自动得到的前提。本轮新增 [ZFCUnpaidCompletionPromotion.lean](ZFCUnpaidCompletionPromotion.lean)，让 interface 保留 `member/input/step/observe/formalDone` 全部字段，再把 `originDone` 留在 expansion。

C-364 证明：只要出现 formal-completion witness，就能把 `originDone` 设为 false 而保留 base/subtheory model、所有公开字段和 formal witness；该 expansion 反驳 P，并显示 base/subtheory 不能语义蕴含该 promotion。相反，显式 bridge 加上 formal adequacy 可以推出 P。它将“ZFC-1 是加上 P 的使用扩张”从命名变为反模型与正控制兼具的机器结论。

## 2026-10-04：把成员语言边界从接口约定推进到公式语义

C-362/C-364 的 base interface 已经精确表达“外加 Done 不在公开字段中”，但仍可能被误读为只是一项建模约定。为排除这一歧义，本轮新增 [ZFCMembershipLanguageBoundary.lean](ZFCMembershipLanguageBoundary.lean)：它明写 `=`、`∈`、蕴含和全称量词的 de Bruijn formula 片段及其满足关系，并用公式归纳证明 external Done 不影响其中任一公式或 theory 的满足。

C-365 因而提供语言级的理由：成员语言公式不携带 `originDone`，便不能凭同一 membership satisfaction 自动决定它。它不把该 minimal fragment冒充完整 ZFC schema；完整 schema 的编码仍是未来可替换输入，但只要它保持该语言边界，语义不变性 theorem 适用。

## 2026-10-04：HoTT wrapper 的初始导入失配与最小修复

[HoTTCounterexample.agda](HoTTCounterexample.agda) 初版在使用空类型 `⊥` 时漏导入 `Cubical.Data.Empty`，因此首次尝试只得到 `Not in scope: ⊥`。该错误尚未触及所需的 completion-reflection 命题，不能被报告为数学反例。

修复只加入：

```agda
open import Cubical.Data.Empty as ⊥ using (⊥)
```

正运行随后必须通过；[WrongHoTTCounterexample.agda](WrongHoTTCounterexample.agda) 则必须在它伪造的 original halt witness 上被拒绝。这个区分保证“负控制失败”是目标命题的类型拒绝，而非导入事故。

## 2026-10-04：C-361 的来源与独立重放

`ZenoLimitControl.lean` 的受控命题来自共享 canonical `dev` 中一个同主题但尚未提交的候选。它不是按对方的 status 直接接受：本 worktree 先用其固定 Lean 4.34.0／Mathlib 环境独立执行 source，得到 exit `0` 和声明的三项经典／商公理依赖，随后将 source 与专用 capture 器纳入本分支。其命题只针对明确的 `StrictSequentialDone` 控制，不把这个严格完成谓词塞回 Standard Solution。

首次本地 C-361 capture 的 Lean 执行成功，但把 `LEAN_PATH` 只留在进程环境而没有写进 `command_argv`，因而 generic verifier 的精确重放得到 `REPLAY_EXIT_MISMATCH`。`...-02` 把 `LEAN_PATH=...` 放入 `/usr/bin/env` 命令本身，但其 manifest 仍把随后修订的 CLAIM/README 当成编译输入，故 `...-03` 仍会因文档哈希漂移失效。最终 `...-04` 只 pin Lean source、toolchain、Lean path 与 capture contract；它是 current primary。`...-01` 至 `...-03` 均保留为收据合同的历史失败，不作主证据。

## 当前版本选择

`20261004-MP-ZFC-ACTUAL-Q-POLICY-002-02` 首先修复了 linked-worktree 捕获器和 Lean 二进制 pin，`...-03` 加入“metadata 相等不足以证明同一个实际 Q”的 Bool／Unit 内核反控制；`...-04` 又加入“ZFC-1 use-model 不会靠逻辑自动生成 B”的 vacant-formal control；`...-05` 将 `TaskEquiv` 保留为强控制，并加入范围 witness 的实际来源入口；`...-06` 明确该 witness 不携带书目归属，须由 source card 在内核外资格化。前五份的 source hash 均为历史快照，不能再作 current delivery basis；`...-06` 是 current primary。

| 资产 | 可作交付依据？ | 原因 |
|---|---|---|
| `ZFC1IllusionPolicy.lean` | 否 | 预备草稿被 Lean 拒绝，且同 Q 概念不充分。 |
| `ActualQPolicy.lean` | 是，`20261004-MP-ZFC-ACTUAL-Q-POLICY-002-06` 是 current primary | 以严格任务等价阻止 metadata 类比，同时单列必须由来源审计支付的政策范围；明确 Lean 字段不伪称来源归属；证明 use-model 不自动制造 B；全部交付定理无 `sorry`、无额外公理。 |
| `ZFCObservationLanguage.lean` | 是，`20261004-MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001-01` 是 C-362 primary | 对任何 membership-only theory 形式化外加 Done 的不决定性与 explicit bridge 正控制；不编码 ZFC 公理或其模型。 |
| `ZFCCompletionPolicyUniformity.lean` | 是，`20261004-MP-ZFC-COMPLETION-POLICY-UNIFORMITY-001-01` 是 C-363 primary | 对完整 QProfile 下的 O3–O5 adequacy 与 Q-uniformity给出条件 theorem 和粗字段反控制；不填实际来源 profile。 |
| `ZFCUnpaidCompletionPromotion.lean` | 是，`20261004-MP-ZFC-UNPAID-COMPLETION-PROMOTION-001-01` 是 C-364 primary | 对 base/subtheory 的公开字段给出未付 P 反模型、非蕴含 theorem 与 paid bridge 正控制；不编码实际 ZFC。 |
| `ZFCMembershipLanguageBoundary.lean` | 是，`20261004-MP-ZFC-MEMBERSHIP-LANGUAGE-INVARIANCE-001-01` 是 C-365 primary | 对最小一阶成员 language 的外加 Done 不变性、theory 不变性与相反 Done expansion 作归纳证明；不编码完整 ZFC schema。 |
| `HoTTCounterexample.agda` | 是，`20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-01` 已索引并精确重放 | 固定 native Cubical Agda Q 的强 P 反例。 |
| `WrongHoTTCounterexample.agda` | 是，作为已捕获的负控制 | `...NEG-001-01` 在 `nothing != just 1` 处拒绝伪 witness。 |
