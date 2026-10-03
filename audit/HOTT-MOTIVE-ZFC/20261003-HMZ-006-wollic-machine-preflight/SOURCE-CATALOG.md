# HMZ-006：来源目录与精确 locator

| 文件 | SHA-256 | 角色 |
|---|---|---|
| `originals/HMZ-S-021-Voevodsky-2011-WoLLIC.pdf` | `0afa5e2825480f63c04778753db9cebf99323ba6c60916cde3882a0863624159` | IAS 公开原件；PDF 1.5、9 页、CreationDate 2011-05-17。 |
| `derived/HMZ-S-021-Voevodsky-2011-WoLLIC.txt` | `628d27fc351a8d01118871503c25127f6f5d9c4964c285684d2f0b7f53be7c1c` | `pdftotext -layout` 派生定位文本；关键措辞回原 PDF 核对。 |

## 相关页面

| PDF slide | 来源事实 | HMZ 作用 |
|---:|---|---|
| 1 | UF 的四项特征：构造性／非构造性、categorical thinking、可在 Martin-Löf type systems 形式化、直接公理化 homotopy types。 | 与 HMZ-001 的 R-002／R-005 有重叠；不单独构成 Q。 |
| 2 | 明确提及：多次把 ZFC 用作 Coq 等 proof assistant 的形式化基础的尝试导致“不自然构造”。 | 新的、作者直接的 `R-MACHINE` 表述；但没有具名实现。 |
| 3–7 | univalent model、h-level、univalence、computation conjecture。 | HoTT 侧技术背景；没有 ZFC-side同一 task。 |
| 8–9 | Coq universe management 的局限、临时关闭 consistency verification 的 patch、true set-quotients。 | HoTT 自身实现代价的反控制；不能把动机写成“一边完美、一边失败”。 |

### 访问边界

原件取得自 <https://www.math.ias.edu/vladimir/sites/math.ias.edu.vladimir/files/2011_WoLLIC.pdf>，2026-10-03，无登录、付费或远程 OCR。该讲演是作者报告，不是 ZFC 的公理／语义原典，也不是一个 Coq/ZFC 实现的运行收据。
