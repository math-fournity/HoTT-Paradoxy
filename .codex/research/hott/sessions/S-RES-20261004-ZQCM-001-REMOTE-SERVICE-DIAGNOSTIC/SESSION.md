# S-RES-20261004-ZQCM-001-REMOTE-SERVICE-DIAGNOSTIC

> **角色／档位：** `MECHANICAL_CONTEXT / T1 / REMOTE_MINERU_RUNTIME_DIAGNOSTIC`。
>
> **触发：** 研究发起人指出仅有`server_not_running`收据的处理链尚未完成，并要求修复。
>
> **分支身份：** `CANDIDATE_NOT_CURRENT`；本单元记录运行环境和派生证据状态，不改写数学 STATE、Q 资格或 canonical `dev` current truth。

## 已修复的本机阻塞

运行前 MinerU 4.0.8 document-library server 为`running:false`。在用户本轮授权下执行`mineru server start`，获得后台PID 59538；随后`server status --json`确认UDS服务运行、scan/ingest/parse workers运行、remote `https://mineru.net/api` health为true并支持`standard` tier。服务继续运行，未执行stop/restart/config write/model download。

## 真实远程 smoke 结果

选择公开的W-001 arXiv PDF前10页作为受授权的非敏感测试输入。`mineru parse --remote --tier standard --pages 1-10 --json --wait 60`使远程分析完成，但在结果下载的3次内部transport尝试后返回`remote_unreachable / ConnectError`。为分辨输出格式因素，单次改用`mineru-kit parse --remote --tier standard --pages 1-10 --format zip`，得到相同的`output download / ConnectError`。两次均无可消费JSON、Markdown或zip。

## 根因定位与边界

本机server、官方API health、匿名usage、上传和远程分析均工作。App历史还显示此前成功任务可`unzipped`，而两份10月的新任务为`download-failed`，其结果宿主均为`cdn-mineru.openxlab.org.cn`。对最新失败结果的无正文单字节读取返回`ConnectError`；该CDN当前IPv4/IPv6连接后的TLS验证报`certificate has expired`，而`https://mineru.net/api/v1/tiers`返回HTTP 200。

故剩余问题是官方结果CDN的证书，不是本机mineru service、PDF、API健康、账户配额或输出格式。不会通过`--insecure`、关闭证书校验、泄露/替换凭据或写入全局配置绕过该边界。原PDF页级视觉记录仍是本批唯一可用的阅读证据；远程服务恢复后再有有效证书时，按`MINERU-DERIVATIVES.md`重开派生资格化。
