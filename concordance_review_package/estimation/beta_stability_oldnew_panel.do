*===============================================================
* beta_stability_oldnew_panel.do
*---------------------------------------------------------------
* MỤC ĐÍCH: Kiểm tra độ ổn định của β₁ (treatment = EU_MRL × eu_dummy)
*           khi chuyển từ panel CŨ (388.500) sang panel MỚI (292.500).
* Chạy đặc tả Đợt-1 M1 (market access) trên panel MỚI, đối chiếu β_cũ = -2,077.
* YÊU CẦU: Stata MP 17; ppmlhdfe, reghdfe, ftools (SSC).
*
* GHI CHÚ QUAN TRỌNG: Tên cột panel MỚI CHƯA được xác minh trong môi trường này.
*   -> Phần [2] BẮT BUỘC đối chiếu với `describe` ở [1] rồi sửa local cho khớp.
*   -> Nếu panel chưa có eu_dummy / EU_MRL thì [3] sẽ tạo/merge (kiểm khoá kỹ).
*===============================================================
clear all
set more off
version 17

*--- 0. ĐƯỜNG DẪN (sửa cho máy bạn) ----------------------------------
local panel_new "asean_baci_panel.csv"   // panel MỚI 292.500 dòng
local mrl_panel "asean_mrl_panel.csv"    // (tuỳ chọn) để merge MRL nếu panel chưa có
local outlog    "beta_stability_log.txt"

cap log close
log using "`outlog'", replace text

*--- Cài lệnh nếu thiếu ---------------------------------------------
foreach p in ftools reghdfe ppmlhdfe {
    cap which `p'
    if _rc ssc install `p', replace
}

*===============================================================
* [1] NẠP + SOI CẤU TRÚC  (đọc kỹ output trước khi sang [2])
*===============================================================
import delimited "`panel_new'", clear varnames(1) encoding("utf-8")
describe
count
list in 1/5, abbreviate(24)

*===============================================================
* [2] XÁC NHẬN TÊN CỘT — SỬA Ở ĐÂY cho khớp panel MỚI
*     (so với `describe` ở [1]; tên dưới đây CHỈ LÀ GIẢ ĐỊNH theo panel cũ)
*===============================================================
local v_year   "t"           // năm
local v_exp    "i"           // nước xuất  (exporter)
local v_dest   "j"           // nước đích  (importer/destination)
local v_hs6    "k"           // mã sản phẩm HS6
local v_value  "v"           // giá trị xuất khẩu (LEVEL — cho PPML)
local v_qty    "q"           // khối lượng (để kiểm M1-quantity nếu muốn)
local v_eudum  "eu_dummy"    // =1 nếu đích thuộc EU-27
local v_mrl    "eu_mrl_m1"   // chỉ số stringency theo (k,t)

*===============================================================
* [3] (NẾU THIẾU) tạo eu_dummy + merge MRL + dựng treatment
*===============================================================
* 3a. eu_dummy
cap confirm variable `v_eudum'
if _rc {
    di as error ">> Chưa có eu_dummy — tạo từ EU-27 (SỬA mã nước cho khớp `v_dest')."
    local EU27 "AUT BEL BGR HRV CYP CZE DNK EST FIN FRA DEU GRC HUN IRL ITA LVA LTU LUX MLT NLD POL PRT ROU SVK SVN ESP SWE"
    gen byte eu_dummy = 0
    foreach c of local EU27 {
        replace eu_dummy = 1 if `v_dest' == "`c'"
    }
    local v_eudum "eu_dummy"
    qui count if eu_dummy==1
    di ">> Số dòng EU = " r(N)
}

* 3b. MRL stringency: merge nếu panel chưa có
cap confirm variable `v_mrl'
if _rc {
    di as error ">> Chưa có EU_MRL — merge từ `mrl_panel' theo (hs6,year). KIỂM tên khoá!"
    preserve
        import delimited "`mrl_panel'", clear varnames(1)
        keep hs6 year eu_mrl_m1            // <-- SỬA cho khớp cột file MRL thật
        rename (hs6 year) (`v_hs6' `v_year')
        tempfile mrl
        save `mrl'
    restore
    merge m:1 `v_hs6' `v_year' using `mrl', keep(master match) nogen
    local v_mrl "eu_mrl_m1"
}

* 3c. treatment = EU_MRL × eu_dummy
gen double treatment = `v_mrl' * `v_eudum'
label var treatment "EU_MRL_M1 × eu_dummy"
summarize treatment, detail

*===============================================================
* [4] TẠO ID HIỆU ỨNG CỐ ĐỊNH (FE)
*===============================================================
egen fe_ikt = group(`v_exp' `v_hs6' `v_year')   // exporter×product×year  (αᵢₖₜ)
egen fe_jt  = group(`v_dest' `v_year')          // destination×year       (γᵈₜ)
egen fe_ijk = group(`v_exp' `v_dest' `v_hs6')   // exporter×dest×product  (δᵢᵈₖ)
egen fe_j   = group(`v_dest')                   // destination only
egen cl_ij  = group(`v_exp' `v_dest')           // cluster exporter×dest

di _n ">> Số nhóm FE (so với panel cũ: fe_ikt=9.250, fe_jt=430, fe_ijk=38.850):"
foreach g in fe_ikt fe_jt fe_ijk fe_j cl_ij {
    qui tab `g'
    di "   `g' = " r(r)
}

*===============================================================
* [5] ƯỚC LƯỢNG 3 ĐẶC TẢ FE (đối chiếu S1/S2/S3 panel cũ)
*     DV = giá trị xuất khẩu (level), PPML
*===============================================================
* S1 — Preferred:     fe_ikt + fe_jt
ppmlhdfe `v_value' treatment, absorb(fe_ikt fe_jt) cluster(cl_ij)
est store S1
scalar b_S1 = _b[treatment]

* S2 — Conservative:  fe_ikt + fe_jt + fe_ijk  (= Mô hình chính 3 chiều)
ppmlhdfe `v_value' treatment, absorb(fe_ikt fe_jt fe_ijk) cluster(cl_ij)
est store S2
scalar b_S2 = _b[treatment]

* S3 — Minimum:       fe_ikt + fe_j + year
ppmlhdfe `v_value' treatment, absorb(fe_ikt fe_j `v_year') cluster(cl_ij)
est store S3
scalar b_S3 = _b[treatment]

*===============================================================
* [6] SO SÁNH VỚI β CŨ   (SỬA b_old nếu headline của bạn khác)
*===============================================================
scalar b_old = -2.077
di _n "================ SO SÁNH β (treatment) ================"
di "  Panel cũ (388.500), headline       : " b_old
di "  Panel mới (292.500) S1 Preferred    : " b_S1
di "  Panel mới (292.500) S2 Conservative : " b_S2
di "  Panel mới (292.500) S3 Minimum      : " b_S3
di "======================================================="

esttab S1 S2 S3, b(4) se(4) star(* 0.10 ** 0.05 *** 0.01) ///
    keep(treatment) mtitles("S1 pref" "S2 cons" "S3 min") ///
    title("β treatment trên panel MỚI — đối chiếu β_cũ = -2,077")

* (TUỲ CHỌN) kiểm M1-quantity: đổi `v_value' -> `v_qty' và chạy lại [5]-[6].

log close
*=== HẾT =======================================================
