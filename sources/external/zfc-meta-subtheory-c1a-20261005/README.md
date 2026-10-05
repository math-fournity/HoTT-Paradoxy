# C1A 外部原典快照：集合论基础、实分析与极限（2026-10-05）

> **身份：** `SOURCE_SNAPSHOT_MANIFEST / C1A_INPUT / NOT_A_CORE_VERDICT`。
>
> **消费者：** [C1A foundation–subtheory–theorem card](../../../audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C1A-FOUNDATION-THEOREM-CARD.md)。

本目录冻结了 C1A 读取时可取得的公开原件。下载本身不表示来源之间已经建立同一理论、同一任务或同一完成合同。

| 文件 | 原始 URL | 抓取身份与 SHA-256 | C1A 用途 |
|---|---|---|---|
| `IEP-Zenos-Paradoxes.html` | `https://iep.utm.edu/zenos-paradoxes/` | 2026-10-05 public-page snapshot; `800d5ea841493faa6c73b5704b37f353ec0874b3fe072f17b7a03ef22d840b7e` | 标准解法把 ZFC-with-Choice、标准实分析、有限时间到达与“解决芝诺”置于同一应用叙述；它也是 P 的实际来源。 |
| `MML-tarski_0.miz` | `https://mizar.uwb.edu.pl/version/current/mml/tarski_0.miz` | current-endpoint snapshot; `6adae7297e59304282567735e662d50a85e27b4e0cf2538b1403a0c60a1dfe2e` | Mizar 当前库的 Tarski–Grothendieck 公理原件。 |
| `MML-numpoly1.miz` | `https://mizar.uwb.edu.pl/version/current/mml/numpoly1.miz` | current-endpoint snapshot; `31688b54eae4636f1bd2de7756c02ae8bd5901e792ed1629648fe20dbfcc1b22` | `SumsReciTriang` 和 `Th87` 的具体实数序列收敛／极限 theorem。 |
| `Brown-Pak-A-Tale-of-Two-Set-Theories.pdf` | `https://alioth.uwb.edu.pl/~pakkarol/articles/CBKP-CICMMKM2019TechReport.pdf` | 2019 technical report snapshot; `1686cd8f598d0b930cbb87e38ac902d3a4f1649ca28d9f926bcfb6a61e6bd078` | 说明 MML 的 FOTG 基础、它与 ZFC 的非保守扩张关系，以及 Choice 在该基础中的位置。 |

## 严格边界

- `MML-numpoly1.miz` 的 `Th87` 是一个真实的收敛 theorem，但它的序列是 `SumsReciTriang(n) = 2 - 2/(n+1)`，不是 IEP 叙述的 Achilles／Dichotomy 的 exact subpath sequence。
- Mizar 的基础是 FOTG（并有全局选择相关的实现讨论），不是 bare ZFC。它能成为“明确 ZFC-founded foundation context”的候选，却不能被静默改名成 bare ZFC。
- 本机没有已资格化的 Mizar checker，因此这组 `.miz` 原件的 theorem 身份目前是 `SOURCE_REPORTED_FORMAL_THEOREM_UNREPLAYED`；它不是本项目重新运行后的 kernel receipt。
- IEP 没有引用上述 Mizar theorem；因此这里没有 `actual M/S/Q/P/Bridge/Adequacy` 的单一合同，也没有 core machine-proof verdict。
