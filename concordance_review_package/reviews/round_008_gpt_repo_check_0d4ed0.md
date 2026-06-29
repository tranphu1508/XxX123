# Round 008 — GPT repo check @0d4ed0 (verdict, do cowork ghi lại từ phản hồi GPT)
- main `concordance_release_long.csv`: **ACCEPT / analysis-ready.**
- `concordance_release_core_rac.csv`: NEAR-READY — sửa first-token errors: Wheat 0500090 100111→**100199**; Cotton 0401090 120721→**120729**. Rice 100610 OK nếu định nghĩa CORE_RAC=strict-raw (cần ghi rõ).
- Governance/logs: ACCEPT; nên thay "57f0722→(next)" bằng commit thật 0d4ed0.
- CI: chưa có GitHub Actions; nên thêm (không chặn).
