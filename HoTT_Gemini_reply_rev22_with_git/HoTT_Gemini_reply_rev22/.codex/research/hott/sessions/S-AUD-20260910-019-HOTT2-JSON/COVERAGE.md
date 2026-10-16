# 全部chunk与审计定位

编号从0开始，text与parts不重复；内部草稿/签名保留身份，不作为公开论证。

|chunk|身份|审计处理|
|---|---|---|
|c000|外部Drive引用|正文未嵌入，未推测其内容|
|c001|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c001.md`；REVIEW相应阶段|
|c002|thought元数据|原JSON保全；不作证明依据|
|c003|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c003.md`；REVIEW相应阶段|
|c004|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c004.md`；REVIEW相应阶段|
|c005|thought元数据|原JSON保全；不作证明依据|
|c006|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c006.md`；REVIEW相应阶段|
|c007|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c007.md`；REVIEW相应阶段|
|c008|thought元数据|原JSON保全；不作证明依据|
|c009|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c009.md`；REVIEW相应阶段|
|c010|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c010.md`；REVIEW相应阶段|
|c011|thought元数据|原JSON保全；不作证明依据|
|c012|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c012.md`；REVIEW相应阶段|
|c013|Python源码|原样重跑及诊断；代码与行号保存|
|c014|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c015|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c015.md`；REVIEW相应阶段|
|c016|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c016.md`；REVIEW相应阶段|
|c017|thought元数据|原JSON保全；不作证明依据|
|c018|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c018.md`；REVIEW相应阶段|
|c019|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c019.md`；REVIEW相应阶段|
|c020|thought元数据|原JSON保全；不作证明依据|
|c021|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c022|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c023|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c024|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c025|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c026|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c027|thought元数据|原JSON保全；不作证明依据|
|c028|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c029|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c030|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c031|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c032|thought元数据|原JSON保全；不作证明依据|
|c033|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c034|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c035|base64 Python附件|解码、AST检查、与内嵌脚本比对；未执行|
|c036|thought元数据|原JSON保全；不作证明依据|
|c037|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c037.md`；REVIEW相应阶段|
|c038|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c038.md`；REVIEW相应阶段|
|c039|thought元数据|原JSON保全；不作证明依据|
|c040|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c041|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c042|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c043|执行记录|记录状态 `OUTCOME_FAILED`；与实际子操作分开|
|c044|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c045|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c046|base64 Python附件|解码、AST检查、与内嵌脚本比对；未执行|
|c047|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c048|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c049|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c050|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c051|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c052|执行记录|记录状态 `OUTCOME_FAILED`；与实际子操作分开|
|c053|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c054|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c055|Python源码|静态审查；c055另受控故障注入；代码与行号保存|
|c056|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c057|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c057.md`；REVIEW相应阶段|
|c058|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c058.md`；REVIEW相应阶段|
|c059|thought元数据|原JSON保全；不作证明依据|
|c060|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c060.md`；REVIEW相应阶段|
|c061|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c061.md`；REVIEW相应阶段|
|c062|thought元数据|原JSON保全；不作证明依据|
|c063|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c063.md`；REVIEW相应阶段|
|c064|Python源码|原样重跑及诊断；代码与行号保存|
|c065|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c066|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c066.md`；REVIEW相应阶段|
|c067|user公开文字|全文 `artifacts/r019/messages/PUBLIC_c067.md`；REVIEW相应阶段|
|c068|thought元数据|原JSON保全；不作证明依据|
|c069|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c069.md`；REVIEW相应阶段|
|c070|Python源码|原样重跑及诊断；代码与行号保存|
|c071|执行记录|记录状态 `OUTCOME_OK`；与实际子操作分开|
|c072|model公开文字|全文 `artifacts/r019/messages/PUBLIC_c072.md`；REVIEW相应阶段|
