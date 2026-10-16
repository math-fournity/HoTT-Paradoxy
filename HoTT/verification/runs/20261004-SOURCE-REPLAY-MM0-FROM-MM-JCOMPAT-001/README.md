# MM0 `from-mm` matching-runner source replay

This run records a source-execution result, not a mathematical theorem. The raw
`set.mm@160ebb…` input is preserved externally and fails the pinned `mm0-hs`
parser at modern double-quoted `$j` color metadata. A six-line `$j`-comment
derivative was accepted by the same source; the official Metamath verifier
accepted all its proofs; `mm0-hs from-mm` then produced a full MM0/MMB pair;
and `mm0-c` accepted that pair.

The generated 20 MiB MM0 and 41 MiB MMB artifacts remain outside Git at the
external path recorded in `RUN.json`, with their SHA-256 identities. The run
does not construct a ZF-internal `mFS` representation, an adequate `Prv`, a
diagonal sentence, or any parent completion bridge.
