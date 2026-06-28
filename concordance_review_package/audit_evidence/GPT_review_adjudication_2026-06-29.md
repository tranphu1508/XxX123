# Đối chiếu review GPT độc lập — adjudication (2026-06-29)

GPT soi 381 mã: ĐÚNG 100 · SAI 85 · NGỜ 196. Cowork đối chiếu từng ca với HS2012 universe.

## KẾT QUẢ: GPT bắt ~70 lỗi THẬT mà certification của Cowork (token-match) đã SÓT.
Nguyên nhân sót: token-matcher mù với lỗi semantic cùng-chương (head cabbage↔headed broccoli chung từ "head"; fungi↔capsicum), và Cowork giữ nhầm nhiều ca dưới nhãn "lumping".

### Đã ÁP (70 sửa, note GPTFIX trong concordance):
- **Lỗi semantic cụ thể (36):** wild/cultivated fungi→070959/070951 (KHÔNG phải ớt 070960); head cabbage/kale/kohlrabi/chinese cabbage→070490 brassica (KHÔNG phải súp lơ 070410); beans Phaseolus→071333; lupins→071390; kumquat→080590 citrus; dewberry/cane→081020 Rubus; **mã chuyên dụng bỏ sót**: chicory root→121294, ginseng→121120, mate→090300, celery→070940, buckwheat→100810; **mã THIẾU**: hops→121010, cocoa→180100, algae→121221, carob→121292; olives-for-oil→070992; escarole→070529; parsnip/celeriac/parsley-root/swede→070690.
- **Re-anchor về nec (34):** "Others(2)" + lumping-sai-họ (purslane/cress/mustard/rocket→070999; loquat/medlar→081090; Sichuan pepper Zanthoxylum→091099...) — đổi từ mã-cụ-thể-sai về nec đúng nhóm.

### GIỮ (không theo GPT):
- 402030 oil palm FRUIT = 120799 (GPT đề 120710 nhưng 120710=palm KERNEL=mã của 0402020, khác fruit).

### CHƯA xử (cấu trúc, để bước panel-build, không phải lỗi đơn):
- Multi-code "explode": rice 1006xx, tea 0902xx, coffee 0901xx, wheat/barley — tách khi merge trade.
- Cereal seed-vs-grain: rye/oat/maize/sorghum hiện map mã "seed" (100210...), GPT đề thêm mã "other/grain" (100290...) — MRL áp lên hạt thương phẩm → cân nhắc đổi/bổ sung khi build.
- Mã NHÓM-CHA Annex (Tree nuts/Stone fruits/Citrus...): trải nhiều HS6; con của chúng đã map riêng → để aggregate.

## BÀI HỌC: certification tự-động (token) KHÔNG đủ; review semantic độc lập (GPT) bắt được lỗi Cowork mù. Khuyến nghị chạy thêm vòng Claude trên bản ĐÃ SỬA để kiểm hội tụ.
