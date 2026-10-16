# 固定环境重放

本流程重新检查精确Agda源项。成功意味着在声明环境内接受五个入口并按预期拒绝四个固定错误项，且源码未变、基础源码哈希与原依赖图一致；不把运行成功提升为原广义现实任务或全理论结论。

## 前提

需要Python 3.10或更新版本（只使用标准库）、足够临时磁盘空间和macOS arm64上的固定Agda二进制。其他平台未资格化。编译器不在本源码包中；可从manifest中固定的官方v2.8.0 release URL取得对应macOS arm64归档。

- Agda归档SHA-256：`9a35071eb9747f984177f48e1ba7008a9cebccfc259a40a0a84b29ffc2ec2db6`。
- 提取后agda二进制SHA-256：`ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e`。
- 二进制身份与精确基础源码均会由脚本再次核对；名称相同、版本号相同不足以绕过。

库源码随包携带，毋须访问原作者机器上的`/Volumes/D/...`路径。no-erasure派生库的两文件差异和父版本信息均随包保存。重放不下载网络内容；这不等于已建立OS禁网或文件访问沙箱。

## 命令

先在一个新的目录解开本地归档，然后从任意cwd执行。以下路径是示例，替换为自己的真实位置；空格保留引号：

~~~sh
tar -xzf four-stage-review.tar.gz -C "/path/to/new review directory"
python3 "/path/to/new review directory/four-stage-review/tools/replay.py" \
  --agda "/path/to/agda" \
  --out "/path/to/new results directory" \
  --all --jobs 2
~~~

只运行一个入口可将`--all`改为`--case geometry`；其余key为source、sqrt2、s1、quotient、SC01、SC02、SC03、SC04。`--jobs`只能为1或2。默认单项观察窗1800秒，可用`--timeout`调整；超时记录该观察未完成，不推永不终止。

输出目录必须原先不存在，且不在解包目录内。每项各有新的源码/库工作副本、XDG数据目录、库登记和临时目录；不会覆盖前一次结果。脚本对输入包先后核所有文件hash，并使用`--ignore-interfaces`与`--no-default-libraries`。不运行全局Agda库默认设置。

Agda用`--setup`生成全新的基础文件，脚本核对它们与原主run固定的36份`.agda`源码hash。每次编译前记录无接口缓存；编译后核源文件不变。五个正入口还比较依赖图的具名节点和边，避免只凭exit0声称重放了原入口。

## 读取结果

总结果在输出目录`RESULT.json`；各case包含START.json、RUN.json、stdout.txt、stderr.txt、setup输出及成功入口的imports.dot。PASS需要预期退出码、指定错误诊断（控制项）、源字节未变、观测导入路径在本次工作/runtime内，以及正入口图一致。

`START.json`只记录开始，不证明当前进程仍在运行。`RESULT.json`失败、缺失或观察超时都不能当PASS；保留该目录后修复环境/接线，另选新输出目录重试，不覆盖原失败。异常会在总结果中列出。

`origin-primary-runs/`的历史原命令含作者机器绝对路径，供来源追溯；请用此重放脚本取得新的动态路径，不直接复制旧RUN的argv。原源码及历史主run身份由MANIFEST连回exact Git source commit。

本机重定位检查不替代另一机器实测、OS文件访问追踪、独立审稿或所有系统版本支持。使用不同Agda二进制需要另立资格结果；不能去掉hash检查后沿用本包PASS。
