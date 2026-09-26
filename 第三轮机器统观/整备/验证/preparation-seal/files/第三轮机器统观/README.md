# 第三轮机器统观：A 执行、B 独立审计

本目录保存本轮HoTT理论检视的整备、未来执行实物和独立审计。当前阶段是交接准备；是否找到现实相对悖论必须由未来实际研究及相称证据决定。

|用途|入口|
|---|---|
|A 完整研究 SOP|[goal-5.md](../goal-5.md)|
|A 工作闭包|[Session-A-工作闭包](整备/Session-A-工作闭包.md)|
|A `/goal` 后粘贴的完整文本|[Session-A-goal提示词.txt](整备/Session-A-goal提示词.txt)|
|B 完整审计 SOP|[goal-5-audit.md](../goal-5-audit.md)|
|B 工作闭包|[Session-B-工作闭包](整备/Session-B-工作闭包.md)|
|B `/goal` 后粘贴的完整文本|[Session-B-goal提示词.txt](整备/Session-B-goal提示词.txt)|
|实际整备验收、局限和未启动状态|[整备验收](整备/整备验收.md)|

两个提示词文件只含需要粘贴的正文，不含`/goal`本身，各不超过4000个Unicode字符（包括标点、空白与英文，按更严格口径计）。用户先在A粘贴A文本；A交付封存包后，再在独立B粘贴B文本。B从包内固定字节审计，不跟随A工作树的后续改动。

A提示词明确包含本轮精确本地Git提交和canonical checkpoint授权，用于满足既有search SOP；不含push/tag或全库提交。B只写自己的审计目录和强制对话归档，不修改研究结果。准备者未创建或运行A/B，未启动Sub Agent，未改项目当前STATE队列。

所有叙事/SOP/闭包为HUMAN_EDITED。`整备/handoff_snapshot.py`产生的是一次性交接证据（MANIFEST/SEAL/文件副本），不是研究数据库；唯一producer为该脚本，schema `mo3-handoff/v1`。不可手改既有seal代次，修订以新目录重做。脚本校验字节完整性，不验证数学、遗漏或用户原意。`整备/验证/`由资格化脚本生成，保留真实输出，不手填PASS。
