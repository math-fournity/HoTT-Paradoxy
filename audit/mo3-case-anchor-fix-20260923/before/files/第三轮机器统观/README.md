# 第三轮机器统观：A 执行、B 独立审计

本目录保存HoTT理论检视的整备、未来执行实物和独立审计。当前使用治理化的Goal6开工入口；是否找到现实相对悖论由未来实际研究与证据决定。旧`整备/`及其seal保存Goal5时期的接口检查，不覆盖或刷新为新版本。

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

A提示词明确包含本轮精确本地Git提交和canonical checkpoint授权，用于满足既有search SOP；不含push/tag或全库提交。B只写自己的审计目录和强制对话归档，不修改研究结果。准备者未创建或运行A/B，未启动Sub Agent，未改项目当前STATE队列。

所有叙事/SOP/闭包为HUMAN_EDITED。`整备/handoff_snapshot.py`产生的是一次性交接证据（MANIFEST/SEAL/文件副本），不是研究数据库；唯一producer为该脚本，schema `mo3-handoff/v1`。不可手改既有seal代次，修订以新目录重做。脚本校验字节完整性，不验证数学、遗漏或用户原意。`整备/验证/`由资格化脚本生成，保留真实输出，不手填PASS。
