# Development

职责：代码组织、依赖、构建、工具链、评审和 Git 流程。修改现有文件前先检查
tracked/dirty/commit/tag，Git 只 stage 精确路径。

HoTT 最小工具链为 Agda 2.8.0、`agda-unimath` commit
`88cfce0ce195ae3b64a9e73e8ec744ae64b4006b`，以及可选 Lean 4.33.1。构建入口是
`../../HoTT/formal/build.sh`；来源扫描入口是 `../../HoTT/verification/discover_sources.sh`。
依赖锁和已知构建差异在验证报告中，不把临时下载、`.agdai` 或 Docker cache 提交为源文件。
