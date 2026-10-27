#!/usr/bin/env bash
# ⑮ 判语交付检查（v2.19.25）：凡对「档 / 参数 / 画风 / 年龄」下判语，交付物必须带**出图元数据四核**
#   用法: bash tools/check-verdict.sh <交付文本.md>
#   起因（2026-10-01）：助手把用户的官方 Turbo（krea2_turbo_fp8_scaled）当成 ray 判「偏老」，
#   全库 grep 命中 0 —— 无据推测。规矩：**拿不出四核，就不许开口**。
set -u
F="${1:-}"
[ -z "$F" ] && { echo "用法: bash tools/check-verdict.sh <交付文本.md>"; exit 2; }
[ -f "$F" ] || { echo "找不到文件: $F"; exit 2; }
fail=0
echo "── 判语交付四核自查：$F"
echo
for k in 底模 LoRA 参数 提示词; do
  if grep -qE "(^|[^A-Za-z])${k}[=:：]" "$F"; then
    echo "✅ ⑮ 有「${k}」行"
  else
    echo "❌ ⑮ 缺「${k}」行"
    fail=1
  fi
done
echo
if [ "$fail" -eq 0 ]; then
  echo "── 结论：四核齐，可以下判语"
else
  echo "── 结论：**缺四核 → 不许下「档 / 参数 / 画风 / 年龄」类判语**（v2.19.25）"
fi
exit $fail
