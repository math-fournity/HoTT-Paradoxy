# 第三轮机器统观：原A阶段成果与C/D续做

原A final-002保存已选工作集的阶段成果；父范围全面覆盖的完成资格尚未建立，见[专项复核](../audit/第三轮机器统观全面覆盖与完成资格专项复核-20260924.md)。当前接续方案是新Session C使用Goal7完成同一第三轮，再由新D审计；不称第四轮，不改旧seal。新包已准备，实际启动及进度由用户/STATE和对应实物拥有。

**现在交给新Session的材料：**

|用途|当前续做入口|
|---|---|
|接续选择与工作方案|[续做整备/接续方案.md](续做整备/接续方案.md)|
|C单体SOP/开工闭包|[goal-7.md](../goal-7.md)|
|C的/goal后提示词|[Session-C-Goal7启动词.txt](续做整备/Session-C-Goal7启动词.txt)|
|D单体审计SOP/闭包|[goal-7-audit.md](../goal-7-audit.md)|
|D的/goal后提示词|[Session-D-Goal7审计启动词.txt](续做整备/Session-D-Goal7审计启动词.txt)|
|准备范围与验证边界|[整备验收](续做整备/整备验收.md)|

以下为原A/B阶段入口，供追溯或用户明确指定旧任务时使用；不作为C的新完成标准。

|用途|当前入口|
|---|---|
|项目治理化方案|[完整方案](../dev-docs/Goal任务项目治理化与全局复用方案-20260923.md)|
|A单体开工闭包|[goal-6.md](../goal-6.md)|
|A执行Skill|[hott-machine-overview-execution](../.codex/skills/hott-machine-overview-execution/SKILL.md)|
|A短提示词|[治理整备/Session-A-goal提示词.txt](治理整备/Session-A-goal提示词.txt)|
|B单体开工闭包|[goal-6-audit.md](../goal-6-audit.md)|
|B审计Skill|[hott-machine-overview-audit](../.codex/skills/hott-machine-overview-audit/SKILL.md)|
|B短提示词|[治理整备/Session-B-goal提示词.txt](治理整备/Session-B-goal提示词.txt)|
|新接入与验证范围|[治理化验收](治理整备/治理化验收.md)|
|当前候选独立性修订及方法审计|[去锚定修订与审计](../audit/第三轮机器统观去锚定修订与审计-20260923.md)|

下表为可按范围复用的领域纪律与旧工具闭包。当前C/D启动使用上方Goal7提示词；原A/B仍按Goal6/5的当时范围读取。

|用途|入口|
|---|---|
|A 完整研究 SOP|[goal-5.md](../goal-5.md)|
|A 工作闭包|[Session-A-工作闭包](整备/Session-A-工作闭包.md)|
|A `/goal` 后粘贴的完整文本|[Session-A-goal提示词.txt](整备/Session-A-goal提示词.txt)|
|B 完整审计 SOP|[goal-5-audit.md](../goal-5-audit.md)|
|B 工作闭包|[Session-B-工作闭包](整备/Session-B-工作闭包.md)|
|B `/goal` 后粘贴的完整文本|[Session-B-goal提示词.txt](整备/Session-B-goal提示词.txt)|
|实际整备验收、局限和未启动状态|[整备验收](整备/整备验收.md)|

提示词文件只含需粘贴正文，不含`/goal`本身，各≤4000 Unicode字符。续做先在新C使用Goal7执行词；C交付后新D使用审计词。审计固定字节，不跟随研究者后续修改；旧B如审旧A，须保持原交付身份。

A提示词明确包含本轮精确本地Git提交和canonical checkpoint授权，用于满足既有search SOP；不含push/tag或全库提交。B只写自己的审计目录、获准自身session记录和强制对话归档，不修改研究结果。方法维护者不推进A队列；A实际启动与后续进展回STATE，不从早期整备未启动状态推断。

当前最高指示第七稿继续保候选独立性与多尺度；执行/审计Skill1.3.0新增C/D分支。Goal7先父范围充分性再研究结案；旧pin、快照与当时回答保留，方法变化不冒充已被研究者消费。

所有叙事/SOP/闭包为HUMAN_EDITED。`整备/handoff_snapshot.py`产生的是一次性交接证据（MANIFEST/SEAL/文件副本），不是研究数据库；唯一producer为该脚本，schema `mo3-handoff/v1`。不可手改既有seal代次，修订以新目录重做。脚本校验字节完整性，不验证数学、遗漏或用户原意。`整备/验证/`由资格化脚本生成，保留真实输出，不手填PASS。

多尺度基础方法见Goal5及此前[方案](../dev-docs/第三轮机器统观多尺度覆盖改进工作方案-20260923.md)/[自审](../audit/第三轮机器统观多尺度覆盖再次自审-20260923.md)；新C/D的范围与完成条件由Goal7系列拥有。五种方式不是固定五层，脚本控制不是AI自主发现证明。
