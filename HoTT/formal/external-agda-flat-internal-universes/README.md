# LOPS 2018 internal-universe no-go 与 crisp classifier 外部重放

本目录保存 Licata–Orton–Pitts–Spitters 2018 *Internal Universes in Models of Homotopy Type Theory* 的官方 Agda 补充源码，以及本项目对 Agda-flat modal typing 的一正一负控制。

- paper DOI：`10.4230/LIPIcs.FSCD.2018.22`
- dataset DOI：`10.17863/CAM.22369`
- dataset：Cambridge repository item `c9612c2f-f011-417b-96a0-6223f23e34fb`
- license：repository metadata 声明 CC BY 4.0
- upstream source：`upstream/`，13 个 `.agda` 文件、44,374 bytes，全部从官方 ZIP 逐字复制并由 `SOURCE_TREE_MANIFEST.json` 固定
- proof ID：`MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001`

`upstream/README.agda` 同时导入普通内部 weak classifier 的 Theorem 3.1、crisp/tiny interval 下 classifier 的 Theorem 5.2、相对版本与 Proposition 6.2。`controls/` 验证 Agda-flat 的核心支付：crisp 函数接受 crisp argument，拒绝依赖普通 local variable 的相同调用。

完整 claim、显式 postulate 边界和禁止外推见 `CLAIM-INTERNAL-UNIVERSE-CRISP.md`。本目录不会把 postulate-loaded 外部源码写成无条件 HoTT 定理，也不会把 crisp 修复隐藏为实现细节。
