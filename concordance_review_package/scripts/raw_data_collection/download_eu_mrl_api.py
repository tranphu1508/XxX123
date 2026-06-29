#!/usr/bin/env python3
"""
Tải snapshot MRL từ EU Pesticides Database (API v3.0, datalake SANTE).

QUAN TRỌNG: DB cập nhật liên tục, KHÔNG có mã phiên bản → NGÀY TẢI = phiên bản.
Lưu nguyên raw JSON (NDJSON) = artifact đóng băng. Tải lại sẽ ra dữ liệu khác.
Không cần đăng nhập/đồng ý điều khoản. DB "không có giá trị pháp lý" → đối chiếu EUR-Lex (task sau).

Cách chạy:  python download_eu_mrl_api.py <thư_mục_đích>
"""
import requests, hashlib, datetime, os, sys, time

BASE = "https://api.datalake.sante.service.ec.europa.eu/sante/pesticides"
# Bulk MRL = toàn bộ lịch sử + hiện hành + tương lai.
# LƯU Ý: param đúng là 'language_code' (param 'language' từng trả HTTP 400).
MRL_URL        = f"{BASE}/pesticide-residues-mrls-download?language_code=EN&format=json&api-version=v3.0"
PRODUCTS_URL   = f"{BASE}/pesticide-residues-products?language_code=EN&format=json&api-version=v3.0"
SUBSTANCES_URL = f"{BASE}/active-substances-download?format=json&api-version=v3.0"

def fetch(url, out, retries=3):
    for a in range(1, retries + 1):
        try:
            r = requests.get(url, stream=True, timeout=900)
            r.raise_for_status()
            with open(out, "wb") as f:
                for ch in r.iter_content(1 << 20):
                    if ch:
                        f.write(ch)
            return True
        except requests.RequestException as e:
            print(f"  thử {a}/{retries} lỗi: {e}")
            time.sleep(5 * a)
    return False

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def main(dest="."):
    os.makedirs(dest, exist_ok=True)
    snap = datetime.date.today().isoformat()      # NGÀY SNAPSHOT = phiên bản
    out = os.path.join(dest, f"eu_mrl_bulkdownload_snapshot_{snap}.json")
    print(f"[Snapshot {snap}] Tải MRL bulk:\n  {MRL_URL}")
    if not fetch(MRL_URL, out):
        raise SystemExit("DỪNG: tải MRL thất bại (thử lại sau / kiểm endpoint).")
    n = sum(1 for _ in open(out, encoding="utf-8"))
    print(f"  {os.path.getsize(out):,} bytes | {n:,} record (NDJSON) | SHA-256 {sha256(out)}")
    print("  -> Copy vào 01_raw_data_frozen/european_union_maximum_residue_level_snapshot/,")
    print("     ghi checksums_<snap>.txt và NGÀY SNAPSHOT (đây là phiên bản của nguồn này).")
    print("Tùy chọn (cây sản phẩm + metadata hoạt chất):")
    print(f"  PRODUCTS:   {PRODUCTS_URL}")
    print(f"  SUBSTANCES: {SUBSTANCES_URL}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
