# 完整原文加载导览（revision 40）

先读外层README、项目AGENTS和治理入口。本目录是派生全文，不是新真值源。核心 **488份文件、3,522,185 UTF-8字节、20卷**，严格按原运行器当前计划顺序；第一份为第五闭包，第二份为三问。各卷按文件名顺序加载，不能只读标题或EOF。每段正文与对应原文件/行范围/哈希绑定，没有摘要替换。

补充 **353份不重复文档/源码、23卷**，包括核心之外的理论Schema原始材料、历史治理和研究脚本。其余全部文件有索引，原件未删：大量重复checkpoint、机器清单和原始取证JSON无需默认重复塞进一次窗口，但当本轮实际依赖时必须读回源文件。Archive.zip的大规模原始语料通过archive_store无损恢复，不能假定所有原语料都装入一百万tokens。

参考分词：NOT_AVAILABLE_OFFLINE; no target-token count claimed。核心参考tokens=None，补充=None。这不是新模型的精确分词器。留出系统输入和研究输出空间，不能因为号称百万窗口就忽略截断。容量不足必须记录未加载，不能伪造全业务认知通过。无需让当前Astra重新全文分析数学才能做这次保全。

本计划快照 `446bf75739e21b27a4de91bec5f64af375da0deaa329ece5fdc1bfe5a6801031`。后续修改任一必读来源后须重新生成到新目录或按govern.py重新读，不使用陈旧卷冒充最新输入。可运行：`python3 -B scripts/handoff/build_onboarding.py --destination <新的派生目录>`。

RECEIVER_ACK.template.md 是接手者真实读取后要填写的记录，不是已经完成的AI验收。
