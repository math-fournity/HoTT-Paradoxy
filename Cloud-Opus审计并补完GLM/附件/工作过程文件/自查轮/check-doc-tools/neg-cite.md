# 负控制：check_doc_citations.py 必须抓到 4 处失败、1 处警告（预期退出码 1）

| 情形 | 引用的命题 | 文件:行 |
|---|---|---|
| 正确（必须通过） | `typeIsNotASet : ¬ isSet Type` | `HoTT/formal/claude-cg001/uip-escape/UIPEscape.agda:52` |
| 去掉了否定号（必须 FAIL：不是原文） | `typeIsNotASet : isSet Type` | `HoTT/formal/claude-cg001/uip-escape/UIPEscape.agda:52` |
| 行号超出文件末尾（必须 FAIL） | `typeIsNotASet : ¬ isSet Type` | `HoTT/formal/claude-cg001/uip-escape/UIPEscape.agda:5000` |
| 行号指错地方（必须 WARN） | `typeIsNotASet : ¬ isSet Type` | `HoTT/formal/claude-cg001/uip-escape/UIPEscape.agda:60` |
| 文件不存在（必须 FAIL） | `typeIsNotASet : ¬ isSet Type` | `HoTT/formal/claude-cg001/uip-escape/NoSuchFile.agda:52` |
| 用 … 合法省略（必须通过） | `typeIsNotASet : … isSet Type` | `HoTT/formal/claude-cg001/uip-escape/UIPEscape.agda:52` |
