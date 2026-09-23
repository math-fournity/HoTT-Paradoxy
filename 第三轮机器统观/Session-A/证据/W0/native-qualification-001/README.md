# MO3原生工具资格化

本目录核查本机Cubical Agda对两个固定Path样例的接受/拒绝及换路径复跑能力；不登记新数学定理。正负源码逐字复制自整备qualify-002，实际运行是Session A的新运行。

`RESULT.json`记录工具身份、库树重算、每次argv/退出/输出散列；各子目录`RUN.json`、stdout/stderr为原始运行。观察窗180秒；本次各控制均在约3秒完成。错误实例的exit42是预期拒绝，不是理论矛盾。

执行时复用`第三轮机器统观/整备/qualify_preparation.py`的run函数和`scripts/audit/verify_formal_proof_run.py`的deterministic_tree；先核TOOLCHAIN所列binary/库树，复制库及XDG内建源码到独占临时目录，再按RESULT的三组命令运行。临时路径已清理；重放时创建新独占目录并按同一映射替换argv中的临时前缀，原始证据不改写。也可运行原整备qualification脚本到一个全新获准目录重建这三个控制；该脚本会额外执行其整备接口检查，不能称为本目录的逐字命令重放。

后续数学结果必须使用正式capture管线，保存精确命题、完整依赖、公理边界与索引；本工具资格收据不能替代这些义务。
