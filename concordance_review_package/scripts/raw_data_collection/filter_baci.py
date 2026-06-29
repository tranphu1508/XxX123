#!/usr/bin/env python3
"""
filter_baci.py — Lọc dữ liệu BACI cho đề tài EU MRL & ASEAN agri-food exports
=================================================================================
Lọc theo: 5 nước ASEAN xuất khẩu × 43 thị trường đích × sản phẩm HS 07-10 + placebo
Tạo thêm cột phân loại: sample_role, hs2, dest_group, eu_dummy, asean_intra

CÁCH DÙNG:
    python filter_baci.py <đường_dẫn_thư_mục_BACI> <đường_dẫn_output>

VÍ DỤ:
    python filter_baci.py "D:\\Research\\...\\BACI_HS12_V202601" "D:\\Research\\...\\BACI_filtered_full.csv"
"""

import csv
import os
import sys
import time

# ============================================================
# 1. ĐỊNH NGHĨA CÁC BỘ LỌC
# ============================================================

# --- Nước xuất khẩu: ASEAN-5 ---
ASEAN5 = {
    704: 'VNM',   # Việt Nam
    360: 'IDN',   # Indonesia
    764: 'THA',   # Thái Lan
    458: 'MYS',   # Malaysia
    608: 'PHL',   # Philippines
}

# --- Thị trường đích: EU-27 ---
EU27 = {
    40: 'AUT', 56: 'BEL', 100: 'BGR', 191: 'HRV', 196: 'CYP',
    203: 'CZE', 208: 'DNK', 233: 'EST', 246: 'FIN', 251: 'FRA',
    276: 'DEU', 300: 'GRC', 348: 'HUN', 372: 'IRL', 380: 'ITA',
    428: 'LVA', 440: 'LTU', 442: 'LUX', 470: 'MLT', 528: 'NLD',
    616: 'POL', 620: 'PRT', 642: 'ROU', 703: 'SVK', 705: 'SVN',
    724: 'ESP', 752: 'SWE',
}

# --- Thị trường đích: Ngoài EU ---
NON_EU = {
    842: 'USA',   # Mỹ (baseline Mô hình 2)
    156: 'CHN',   # Trung Quốc
    699: 'IND',   # Ấn Độ
    392: 'JPN',   # Nhật Bản
    410: 'KOR',   # Hàn Quốc
    36:  'AUS',   # Úc
    554: 'NZL',   # New Zealand
    124: 'CAN',   # Canada
    643: 'RUS',   # Nga
    144: 'LKA',   # Sri Lanka
    784: 'ARE',   # UAE
}

# Toàn bộ thị trường đích (bao gồm ASEAN nội khối)
ALL_IMPORTERS = set(EU27.keys()) | set(NON_EU.keys()) | set(ASEAN5.keys())
ALL_EXPORTERS = set(ASEAN5.keys())

# Lookup ISO3 cho tất cả nước
ALL_ISO3 = {}
ALL_ISO3.update(ASEAN5)
ALL_ISO3.update(EU27)
ALL_ISO3.update(NON_EU)

# --- Nhóm thị trường đích (dest_group) ---
def get_dest_group(j):
    if j in EU27:
        return 'EU'
    if j == 842:
        return 'USA'
    if j == 156:
        return 'CHN'
    if j == 699:
        return 'IND'
    if j in (392, 410):
        return 'JPN_KOR'
    if j in (36, 554, 124):
        return 'AUS_NZL_CAN'
    if j in (643, 144, 784):
        return 'RUS_LKA_ARE'
    if j in ASEAN5:
        return 'ASEAN_intra'
    return 'OTHER'

# --- Sản phẩm ---
HS_MAIN = {'07', '08', '09', '10'}        # Mẫu chính
HS_EXTENSION = {'12', '15'}               # Mở rộng (robustness)

# Placebo: cao su (4001-4005), mây/tre/lá (1401-1404, 4601-4602), sợi (5305, 5308)
PLACEBO_HS4 = {'4001','4002','4003','4004','4005',
               '1401','1402','1403','1404',
               '4601','4602',
               '5305','5308'}

def classify_product(k_str):
    """Phân loại sản phẩm. Trả về (sample_role, hs2) hoặc (None, None) nếu loại."""
    hs2 = k_str[:2]
    hs4 = k_str[:4]

    if hs2 in HS_MAIN:
        return 'main', hs2
    if hs2 in HS_EXTENSION:
        return 'extension', hs2
    if hs4 in PLACEBO_HS4:
        return 'placebo', hs2
    return None, None

# --- Năm ---
YEARS = set(range(2015, 2025))  # 2015–2024

# ============================================================
# 2. XỬ LÝ CHÍNH
# ============================================================

def process_file(filepath, writer, stats):
    """Đọc 1 file BACI, lọc và ghi ra output."""
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stats['total'] += 1

            i = int(row['i'])
            if i not in ALL_EXPORTERS:
                continue

            j = int(row['j'])
            if j not in ALL_IMPORTERS:
                continue

            # Loại dòng ASEAN xuất cho chính mình
            if i == j:
                continue

            k_str = row['k'].strip().zfill(6)
            sample_role, hs2 = classify_product(k_str)
            if sample_role is None:
                continue

            stats['matched'] += 1
            stats[sample_role] = stats.get(sample_role, 0) + 1

            # Tính thêm các cột
            t = int(row['t'])
            v = row['v'].strip()
            q = row['q'].strip()
            eu_dummy = 1 if j in EU27 else 0
            asean_intra = 1 if j in ASEAN5 else 0
            dest_group = get_dest_group(j)
            exporter_iso3 = ASEAN5.get(i, '')
            importer_iso3 = ALL_ISO3.get(j, str(j))

            writer.writerow([
                t, i, j, k_str, v, q,
                exporter_iso3, importer_iso3,
                hs2, sample_role, dest_group,
                eu_dummy, asean_intra
            ])

def main():
    if len(sys.argv) < 3:
        print("Cách dùng: python filter_baci.py <thư_mục_BACI> <file_output>")
        print("Ví dụ:     python filter_baci.py D:\\Data\\BACI D:\\Output\\BACI_filtered.csv")
        sys.exit(1)

    baci_dir = sys.argv[1]
    output_path = sys.argv[2]

    # Tìm tất cả file BACI cho 2015–2024
    baci_files = []
    for year in sorted(YEARS):
        fname = f"BACI_HS12_Y{year}_V202601.csv"
        fpath = os.path.join(baci_dir, fname)
        if os.path.exists(fpath):
            baci_files.append((year, fpath))
        else:
            print(f"  [CẢNH BÁO] Không tìm thấy file: {fname}")

    if not baci_files:
        print("KHÔNG tìm thấy file BACI nào! Kiểm tra đường dẫn.")
        sys.exit(1)

    print(f"Tìm thấy {len(baci_files)} file BACI (2015–2024)")
    print(f"Output: {output_path}")
    print()

    # Header output
    header = [
        't', 'i', 'j', 'k', 'v', 'q',
        'exporter_iso3', 'importer_iso3',
        'hs2', 'sample_role', 'dest_group',
        'eu_dummy', 'asean_intra'
    ]

    stats = {'total': 0, 'matched': 0}
    t0 = time.time()

    with open(output_path, 'w', newline='', encoding='utf-8') as out:
        writer = csv.writer(out)
        writer.writerow(header)

        for year, fpath in baci_files:
            t1 = time.time()
            year_stats = {'total': 0, 'matched': 0}
            process_file(fpath, writer, year_stats)

            elapsed = time.time() - t1
            stats['total'] += year_stats['total']
            stats['matched'] += year_stats['matched']
            for k_role in ('main', 'extension', 'placebo'):
                stats[k_role] = stats.get(k_role, 0) + year_stats.get(k_role, 0)

            print(f"  {year}: {year_stats['total']:>10,} dòng đọc → "
                  f"{year_stats['matched']:>6,} giữ "
                  f"(main={year_stats.get('main',0):,}, "
                  f"ext={year_stats.get('extension',0):,}, "
                  f"placebo={year_stats.get('placebo',0):,}) "
                  f"[{elapsed:.1f}s]")

    total_time = time.time() - t0

    print()
    print("=" * 60)
    print(f"TỔNG KẾT")
    print(f"  Tổng dòng đọc:    {stats['total']:>12,}")
    print(f"  Tổng dòng giữ:    {stats['matched']:>12,}")
    print(f"    - main (HS07-10):  {stats.get('main',0):>10,}")
    print(f"    - extension (12,15): {stats.get('extension',0):>8,}")
    print(f"    - placebo:         {stats.get('placebo',0):>10,}")
    print(f"  Thời gian:         {total_time:.1f} giây")
    print(f"  File output:       {output_path}")
    print()

    # Thống kê bổ sung
    print("Bộ lọc đã áp dụng:")
    print(f"  Exporters:  {len(ASEAN5)} nước ASEAN (VN, ID, TH, MY, PH)")
    print(f"  Importers:  {len(ALL_IMPORTERS)} thị trường "
          f"(EU-27 + 11 non-EU + 5 ASEAN nội khối)")
    print(f"  Products:   HS 07-10 (main) + HS 12,15 (extension) + placebo")
    print(f"  Years:      2015–2024")


if __name__ == '__main__':
    main()
