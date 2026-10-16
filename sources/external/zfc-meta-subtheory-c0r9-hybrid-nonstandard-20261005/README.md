# Benveniste et al. 2012：ZFC extension、hybrid operational semantics 与 Zeno source snapshot

> **身份：** `PRIMARY_PUBLISHED_SOURCE_SNAPSHOT / C0R9_COMPARATIVE_EXTENSION_CONTROL / NOT_A_BARE_ZFC_VERDICT`。

## 原件

| field | value |
|---|---|
| authors | Albert Benveniste, Timothy Bourke, Benoît Caillaud, Marc Pouzet |
| title | *Non-Standard Semantics of Hybrid Systems Modelers* |
| publication | *Journal of Computer and System Sciences* 78(3), 877–910 (2012), DOI `10.1016/j.jcss.2011.08.009` |
| source URL | `https://www.tbrk.org/papers/jcss2012.pdf` (author-hosted paper PDF) |
| PDF | `Benveniste-et-al-2012-NonStandard-Semantics-Hybrid-Systems-Modelers.pdf`; PDF 1.4; 54 pages; SHA-256 `86d0fe01e2648ab09dd787d38595b831c09967dc63c45e062d74ee2d702920dd` |
| derived text | `Benveniste-et-al-2012-NonStandard-Semantics-Hybrid-Systems-Modelers.txt`; `pdftotext` reading aid; SHA-256 `3c3b9479890dfef004ce0b083ffcfae71b35be125c3a5f18bab55edd11dfe367` |

## Original-page visual checks

| PDF page | verified source content |
|---|---|
| p.4 | a formally sound executable semantic map faces three tensions: static definability, a computer’s discrete steps, and adaptive discretization fixed at run time. |
| p.10 | zero-crossing order can determine later mode activation; adaptive discretization cannot simply be included in static standard semantics; authors propose non-standard analysis as semantic domain. |
| p.25 | authors fix an infinitesimal base step, replace ordinary time by `T={n∂ | n∈*N}`, define predecessor/successor, and say `T` can be treated as discrete and totally ordered while dense in standard time. |

## Boundary

The paper says Robinson’s non-standard analysis adds three axioms to a basic ZFC framework. It is therefore evidence about a **ZFC extension** used to furnish an operational temporal semantics. It does not establish that bare ZFC cannot host any equally adequate semantics, that standard analysis is inconsistent, or that a physical Zeno task has the same completion predicate as a SimpleHybrid execution task.
