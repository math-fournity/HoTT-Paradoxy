# R09首次checkpoint预检查失败

`python3 第三轮机器统观/Session-A/证据/W3-R09/checkpoint_r09.py`首次退出1，停在第113行的 `_audit_v1_kc_rows(audit)` 顺序断言。canonical兼容解析器要求表格行以 `| ` 后接KC编号开头，而本次人工分片写成无空格开头，导致未识别任何KC行。

此时尚未调用 `rt.checkpoint`，没有应用STATE写入。修正只给人工审计48行补该空格，未改KC判断、数量、解析器或验收标准。原始异常由本次工具轨迹保留；本页是事后说明，不伪称原始stderr文件或历史事务收据。

第二次dry-run已进入canonical prepare，因将PDF放进只接受UTF-8文本的full_sources/source_hashes而得到`NOT_UTF8: 第三轮机器统观/Session-A/证据/W3-R09/source/directed-1705.07442v5.pdf`。仍未apply，STATE保持277。未应用proposal/source-script/plan已逐字保全于checkpoint-proposal-001。

修正：文本水合只加载固定SOURCE-MANIFEST，PDF另列binary_sources并要求每次消费显式hash重核；本writer仍直接核两个PDF字节，最终seal也必须含PDF。没有放宽runtime UTF-8检查、没有伪造PDF文本、没有把manifest hash单独说成PDF当前身份。runtime不会因PDF单独变化自动传播stale，此工具边界在本次记录中明确保留。
