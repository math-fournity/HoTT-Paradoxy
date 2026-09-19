# Audit sharding writer limitation

The current checkpoint runtime only authorizes new session files directly under the session directory. It rejects nested `CORE_COGNITION_AUDIT/` shard paths, so this checkpoint uses the supported monolithic audit table. The v3 touched-set contract remains documented in `PROTOCOL.md`; no runtime change is authorized in this v5 migration.
