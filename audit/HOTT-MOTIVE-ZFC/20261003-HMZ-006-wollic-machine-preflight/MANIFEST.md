# HMZ-006：Voevodsky 2011 WoLLIC 机器基础动机预检

> **身份：** `SOURCE_PREFLIGHT / NEW_AUTHOR_MOTIVE / PAIRING_SOURCE_FOUND_IN_HMZ-007 / HISTORICAL_REFERENT_UNRESOLVED / NOT_A_FULL_DENOMINATOR_RUN`。

## 预检问题

Voevodsky 在 WoLLIC 2011 将“以 ZFC 为基础、在 Coq 等证明助手中形式化数学”的历史尝试称为导致“不自然构造”。这个作者原典是否已经给出可进入 `R_i → Z_i → Q_i` 的同一 ZFC-side 对象、formation、consumer 与 Done，还是只能成为一张需要配对来源的动机卡？

## 冻结来源

| ID | 来源 | 原件／哈希 | 实读范围 |
|---|---|---|---|
| `HMZ-S-021` | Vladimir Voevodsky, *Univalent Foundations are*, Talk at WoLLIC, UPenn, May 2011；IAS 公开 PDF。 | `originals/HMZ-S-021-Voevodsky-2011-WoLLIC.pdf`; SHA-256 `0afa5e2825480f63c04778753db9cebf99323ba6c60916cde3882a0863624159`. | 全部 9 张 slide；派生全文在 `derived/`。 |

## 来源支持的 R

```text
HMZ-R-014 (SOURCE_REPORTED):
  The source explicitly names ZFC as an existing foundation and reports that
  attempts to base proof-assistant formalization (such as Coq) on it led to
  “very unnatural constructions.”

Scope boundary:
  The source does not name those attempts, define “unnatural construction,”
  specify their ZFC encoding, or provide a ZFC-side consumer / I/O / Done.
```

同一讲演还报告：Coq 的 universe management 对某些 univalent applications 不够灵活，作者当时用了会关闭 universe-consistency verification 的 patch。这个事实禁止把该讲演读成“HoTT 已无条件解决形式化自然性”的证明。

## 准入裁定

```text
R novelty over HMZ-001: YES — 直接点名 ZFC + proof-assistant formalization 的历史动机。
ZFC-side u/F/C/I/O/Done: NOT SUPPLIED.
P1/P2/P3: NOT TESTABLE YET.
H0→Z0: NOT FORMED.
SUCCESSOR RUN: HMZ-007 CLOSED WITH A COMPARABLE PAIR; HISTORICAL ATTRIBUTION REMAINS UNRESOLVED.
```

完整收据见 [SOURCE-CATALOG](SOURCE-CATALOG.md)、[COVERAGE](COVERAGE.md) 与 [FINDINGS](FINDINGS.md)。
