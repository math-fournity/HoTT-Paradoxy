import Cache.Hashing
import Cache.Requests

/- Generate the pinned upstream cache's dependency map. No network or theorem claims. -/
open Lean Cache Cache.IO Cache.Hashing Cache.Requests

def main (args : List String) : IO Unit := CacheM.run do
  let roots ← parseArgs ("get" :: args)
  if roots.isEmpty then throw <| IO.userError "Explicit roots required"
  let memo ← getHashMemo roots
  let hashes ← memo.filterByRootModules roots.keys
  let master ← Container.master.getURL
  let legacy ← Container.legacy.getURL
  let entries := hashes.toArray.map fun (mod, hash) => Lean.Json.mkObj [
    ("module", toJson mod.toString),
    ("file", toJson hash.asLTar),
    ("url", toJson (mkFileURL (some .master) MATHLIBREPO master hash.asLTar none)),
    ("legacy_url", toJson (mkFileURL (some .legacy) MATHLIBREPO legacy hash.asLTar none))]
  let unpack ← mkLeanTarConfig hashes
  IO.println <| Lean.Json.compress <| Lean.Json.mkObj [
    ("entries", .arr entries), ("unpack", .arr unpack),
    ("roots", toJson (roots.keys.map toString))]
