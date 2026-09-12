# 全部原始输入的无损存储

STORE.json映射本次开始时324份实际挂载文件；objects.pack存原字节的有序块。ZIP文件按原header与compressed-stream分段，未重压缩原件；bundle与非ZIP按64KiB分段。原名称和完整SHA保存。

恢复全部或一份：从包根调用 `python3 -B workspace/scripts/handoff/archive_store.py restore --destination <新目录> [--relative Archive.zip]`。

验证：`python3 -B workspace/scripts/handoff/archive_store.py verify`（输出逐文件哈希，可能很长）。本次已验证全部原件的重建流与原始哈希一致；validation/SOURCE_STORE_VERIFICATION.json是收据。

这里是历史保全，不是另一套当前工作树。不要直接执行里面的脚本或拿旧AGENTS覆盖workspace。
