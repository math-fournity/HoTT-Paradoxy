# Checkpoint retention archive

This directory holds checkpoint directories retired from the live
`.codex/cognition/checkpoints/` retention window by the v5 P3 migration. The
directory names, `transaction.json`, `result.json`, and before/after contents
are preserved byte-for-byte by Git move; the archive is a location change, not
evidence deletion or transaction reconstruction.

The live checkpoint root keeps the five lexicographically latest session
directories. Current STATE references to retired checkpoint receipts use this
`archive/` path. Historical documents and archived transaction payloads may
still spell their original root location because those strings describe the
path at the time of the original transaction; they are historical evidence, not
current routing instructions.

The v5 migration repaired the two known S168/S169 `after/` audit-shard gaps
from their tracked live session directories before retention. It also moved
S166 after the new v5 transaction was created, then updated the one current
STATE locator to this archive path with a verified STATE/HEAD backup. See
`治理框架v5设计方案/011 - 执行检查清单（自审计用）.md` and the v5 session
record for exact scope and remaining host-behavior gates.
