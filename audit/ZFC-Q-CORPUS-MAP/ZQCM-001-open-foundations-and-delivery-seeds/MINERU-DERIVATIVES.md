# ZQCM-001 MinerU Derivatives

> **本地 runtime 已资格化到版本信息：** MinerU 4.0.8 / Python 3.11.15。
>
> **远程质量通道：** ZCode 专用 Skill 记录了 direct remote standard 先例；本批的Grayson kit请求已停止为`REMOTE_RESPONSE_STALLED`，而direct CLI被`server_not_running`阻断。当前无正在运行的远程导出，未改变本地App daemon。
>
> **视觉核验合同：** 每份成功远程派生物必须经过150dpi二值页图逐页视觉核验；Q相关／异常位置另行300dpi复核。详见本批[`VISUAL-REVIEW.md`](VISUAL-REVIEW.md)。
>
> **状态：** REMOTE_DERIVATIVE_NOT_QUALIFIED / W005_SOURCE_VISUAL_REVIEW_COMPLETE。

| MIN ID | ACQ ID | 输入哈希 | 命令／版本 | 页范围 | 派生路径 | 结果／限制 |
|---|---|---|---|---|---|---|
| MIN-LOCAL-001 | ACQ-001 | 3b2d4c6585ba36d46875ad499feacf7a36c00675af43d3e76a4682935368bc71 | mineru-kit 4.0.8 / local basic | all 33 | derived/mineru-basic/ (aborted output) | `STOPPED_BY_USER_NOT_CONSUMED`。2026-10-03 用户指定不再使用本地basic；其partial Markdown不进入阅读、引用、视觉核验或Q判断。 |
| MIN-REMOTE-001 | ACQ-001 | 3b2d4c6585ba36d46875ad499feacf7a36c00675af43d3e76a4682935368bc71 | mineru-kit 4.0.8 / direct remote standard | default all | derived/mineru-remote-standard | `REMOTE_RESPONSE_STALLED`：已建立TLS连接、14分钟未创建输出；只读sample显示客户端在sleep／SSL read循环，故终止，不把运行事实当parse成功。 |
| MIN-REMOTE-QUAL-002 | ACQ-003 | 4bbed1b843f46be19b6226481faf55445efaf57bcde6b208a4ac9363da862ba3 | mineru 4.0.8 / `parse --remote --json` | all | — | `FAILED_SERVER_NOT_RUNNING`：本机当前CLI要求本地MinerU服务运行；为避免改变与App共享的服务，未启动服务。 |
| MIN-W005-SOURCE-ONLY-001 | ACQ-005 | 14d9048798f365b0d9a4837dc75d96ab828629e32d3acdf5fe8938760e7faa8d | Ghostscript `pngmono` + actual visual inspection | PDF pp.1–13 | visual/W-005/ | `SOURCE_ONLY_VISUAL_CHECK_COMPLETE`：所有13页150dpi；pp.1/5/7/9/11/12/13另有300dpi。没有remote MinerU输出，不能称其通过MinerU核验。 |
| MIN-W010-SOURCE-ONLY-001 | ACQ-010 | eb3c8aa6e95e5fcb289083d9a3af511578304e739b2a978a1f6fe0e1c7ddf3d5 | Ghostscript `pngmono` + actual visual inspection | PDF pp.1,16–17 | visual/W-010/ | `SOURCE_ONLY_TARGETED_CHECK`：p.1、16、17的150dpi及300dpi控制页已核；其余页面尚未逐页视觉阅读，不能称整章已完成视觉核验。 |
