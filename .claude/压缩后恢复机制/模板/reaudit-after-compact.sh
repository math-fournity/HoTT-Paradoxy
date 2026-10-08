#!/bin/sh
# SessionStart(compact) hook: print a short reload card for the GUI re-audit.
# The marker file audit/GUI-ASSET-REAUDIT/ACTIVE turns the hook on (CL-A2) and off (TOTAL_CLOSED).
# Prints nothing when the marker or the SOP folder is missing.
ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
WS="$ROOT/audit/GUI-ASSET-REAUDIT"
SOP="$ROOT/dev-docs/GUI导出全量复算重读审计SOP"
cat > /dev/null 2>&1
[ -f "$WS/ACTIVE" ] || exit 0
[ -d "$SOP" ] || exit 0
echo "【压缩后恢复：GUI 导出复算】"
echo "压缩已经发生。不要凭记忆写路径，也不要先写入。按顺序恢复："
echo "1. 整读闭包：认知闭包/GUI-ASSET-REAUDIT-001.md"
echo "2. 整读规范索引：dev-docs/GUI导出全量复算重读审计SOP.md"
echo "3. 整读本规范全部分片（全名，逐字使用；006 为 v2 修订，优先）："
ls "$SOP" | grep -E '^[0-9]{3} - .*\.md$' | sort | while IFS= read -r f; do
  echo "   - dev-docs/GUI导出全量复算重读审计SOP/$f"
done
echo "4. 整读 audit/GUI-ASSET-REAUDIT/SESSION-REAUDIT.md、seal-log.jsonl、STATUS.md。"
echo "5. 按 SOP 005 §4 执行 CL-BR2（v2 见 006 §3、§5、§8）。全部通过前不写入任何东西。"
echo "语料路径只从 audit/GUI-ASSET-REAUDIT/manifest2.json 取。"
