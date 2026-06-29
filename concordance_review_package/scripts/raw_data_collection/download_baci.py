#!/usr/bin/env python3
"""
Tải BACI (CEPII) bản đóng băng cho dự án — release 202601, HS revision HS12.
Tái lập hoàn toàn: GHIM version + URL canonical (KHÔNG lấy "latest").

Nguồn:   https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37
Licence: Etalab 2.0. Trích dẫn: Gaulier, G. & Zignago, S. (2010),
         BACI: International Trade Database at the Product-Level, CEPII WP N°2010-23.

Cách chạy:
    python download_baci.py <thư_mục_đích>
"""
import hashlib, sys, urllib.request, zipfile
from pathlib import Path

RELEASE = "202601"          # bản hiện hành, cập nhật 2026-01-22
HS = "HS12"                 # phủ 2012–2024 (phủ trọn cửa sổ 2015–2024)
URL = "https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS12_V202601.zip"
EXPECTED_SIZE = 1267950839  # bytes — bản đã kiểm 2026-06-26
# EXPECTED_SHA256 = "<điền từ checksums_2026-06-26.txt>"

def main(dest="."):
    dest = Path(dest); dest.mkdir(parents=True, exist_ok=True)
    zip_path = dest / f"BACI_{HS}_V{RELEASE}.zip"
    print(f"[1/3] Tải {URL}\n      -> {zip_path}")
    urllib.request.urlretrieve(URL, zip_path)

    size = zip_path.stat().st_size
    print(f"[2/3] Kích thước: {size:,} bytes (kỳ vọng {EXPECTED_SIZE:,})")
    if size != EXPECTED_SIZE:
        raise SystemExit("DỪNG: kích thước KHÔNG khớp — kiểm tra lại release/URL!")
    h = hashlib.sha256()
    with open(zip_path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    print("      SHA-256:", h.hexdigest())

    out = dest / f"BACI_{HS}_V{RELEASE}"
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(out)
        print(f"[3/3] Đã giải nén -> {out} ({len(z.namelist())} file)")
    print("XONG. Đây là artifact đóng băng — copy vào 01_raw_data_frozen/trade_data_baci/.")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
