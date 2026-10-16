# Quality

职责：测试、eval、验收、golden、故障注入、性能和直接证据。

HoTT 当前验证入口为 `../../HoTT/verification/VERIFICATION_REPORT.md`。最低要求是：来源哈希与
移动可追溯；主张状态不高于证据；Agda/Lean 记录版本、锁定源和 exit；有限枚举不冒充无界证明；
内部 AI 红队不冒充独立外审。交接包的当前 lint false positive 和原 Agda build 失败必须保留为
负证据，不能只报告修正后的绿色结果。

HoTT 逐字讨论语料还必须通过 `python3 HoTT/tools/hott_discussion_corpus.py validate`：复算全部源
inventory 与 SHA，逐条核对连续原文字节和 excerpt SHA，检查锚点覆盖、孤儿/重叠，并分别核对
问答、标题正文和无标题正文统计。抽取完整性只相对于 v1 锚点；全量 PASS 不得改写为语义全覆盖或
数学正确性验证。

Matrix 悖论原文资产必须通过 `python3 HoTT/tools/matrix_book_paradox_extract.py validate`：当前外部源
SHA/行数必须匹配，全文快照逐字相等，10 个连续行片段与逐字 SHA 一致，84 张图片无缺失/孤儿，
Markdown 图片引用可解析，显式悖论族命中全部进入正文或有 navigation/incidental 排除原因。
`uncovered=0` 只证明词表和人工解答链覆盖，不得升级为全书语义穷尽或原文解答正确。
