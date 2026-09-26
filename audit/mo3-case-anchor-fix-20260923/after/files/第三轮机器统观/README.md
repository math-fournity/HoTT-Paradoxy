# 第三轮机器统观：A 执行、B 独立审计

本目录保存HoTT理论检视的整备、执行实物和独立审计。当前使用治理化的Goal6开工入口；研究进度由STATE和Session-A实物拥有。`整备/`中的SOP消费闭包与短提示词保持兼容更新，其已封存seal和历史接口检查保存当时字节，不刷新为新版本。

**现在交给新Session的材料：**

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

下表为继续复用的领域SOP与旧工具闭包。新启动请用上表两个提示词；Goal6明确要求实际读取Goal5领域细则，不将它降成可忽略历史。

|用途|入口|
|---|---|
|A 完整研究 SOP|[goal-5.md](../goal-5.md)|
|A 工作闭包|[Session-A-工作闭包](整备/Session-A-工作闭包.md)|
|A `/goal` 后粘贴的完整文本|[Session-A-goal提示词.txt](整备/Session-A-goal提示词.txt)|
|B 完整审计 SOP|[goal-5-audit.md](../goal-5-audit.md)|
|B 工作闭包|[Session-B-工作闭包](整备/Session-B-工作闭包.md)|
|B `/goal` 后粘贴的完整文本|[Session-B-goal提示词.txt](整备/Session-B-goal提示词.txt)|
|实际整备验收、局限和未启动状态|[整备验收](整备/整备验收.md)|

新旧提示词文件都只含需要粘贴的正文，不含`/goal`本身，各不超过4000个Unicode字符（包括标点、空白与英文）。用户先用上表治理整备A文本；A交付封存包后，再在独立B使用治理整备B文本。B审固定字节，不跟随A后续改动。

A提示词明确包含本轮精确本地Git提交和canonical checkpoint授权，用于满足既有search SOP；不含push/tag或全库提交。B只写自己的审计目录、获准自身session记录和强制对话归档，不修改研究结果。方法维护者不推进A队列；A实际启动与后续进展回STATE，不从早期整备未启动状态推断。

当前最高指示第六稿、Goal5系列1.1与A/B Skill1.1.0按相关性触发历史保真；新候选无须回接圆环，留出由未覆盖机制决定。旧方法pin变化按Goal6§8重读复核，旧快照和当时回答保留；文本已更新不代表运行中的A已经消费。

所有叙事/SOP/闭包为HUMAN_EDITED。`整备/handoff_snapshot.py`产生的是一次性交接证据（MANIFEST/SEAL/文件副本），不是研究数据库；唯一producer为该脚本，schema `mo3-handoff/v1`。不可手改既有seal代次，修订以新目录重做。脚本校验字节完整性，不验证数学、遗漏或用户原意。`整备/验证/`由资格化脚本生成，保留真实输出，不手填PASS。
