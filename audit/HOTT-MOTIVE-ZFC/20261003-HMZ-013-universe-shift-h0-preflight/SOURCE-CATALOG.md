# HMZ-013：来源目录与精确 locator

| ID | Source fact | Locator | Interpretation limit |
|---|---|---|---|
| `HMZ-S-012` | A Coq-style infinite \(U_i:U_{i+1}\) hierarchy is modelled relative to ZFC with \(\omega+2\) universes; \([U_i]\) consists of fibrations whose simplex sets lie in set-theoretic universe \(i\). | Slides 12–18; derived lines 173–263. | A model/consistency construction, not a bare-ZFC object-language consumer or a claim about a physical completion process. |
| `HMZ-S-010` | \(V_\kappa\) is a Grothendieck universe for inaccessible \(\kappa\); `ZFC+I` adds an inaccessible; changing the universe changes “small”; the same universe-relative object need not be preserved. | PDF pp. 15–17, 21–22; derived lines 740–814, 1045–1090. | Category-theory practice/control with an explicit large-cardinal scope; it cannot prove a fact about every ZFC consumer. |

## Exact source distinctions

1. “ZFC with \(\omega+2\) universes” is a strengthened/model-relative setting, not ordinary ZFC alone.
2. A Grothendieck universe is a \(V_\kappa\) under an inaccessible; Shulman states ordinary ZFC cannot prove that an inaccessible exists.
3. Switching universes changes the domain of “small” quantification. The source’s `G` example warns against carrying a universe-relative witness across that change as though it were automatically the same universal object.

These are source controls, not a derivation of a new mathematical conclusion.

`derived/LOCATORS.md` has SHA-256 `28baf3839852c69a359f554a1c2139a35decf47d8e1eccc403b51e9f72365f34`; it is a locator aid and cannot replace either referenced original.
