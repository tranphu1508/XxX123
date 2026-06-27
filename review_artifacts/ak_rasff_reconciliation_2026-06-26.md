# Bảng đối chiếu A_k × RASFF T5 — 2026-06-26

(Bản .md sinh từ CSV gốc — chỉ để Claude rà.)

| substance | snapshot_id | snapshot_name | in_A_k | in_snapshot | has_inwindow_binding | n_VN_products_with_MRL | n_VN_pending_null | n_VN_not_yet_set | MRL_min_mg_kg | MRL_typical_mg_kg | n_at_LOD | rejection_n_T5 | flag | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| carbendazim | 38 | Carbendazim and benomyl (sum of benomyl and carbendazim expressed as carbendazim) (R) | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.1 | 11 | 37 |  |  |
| permethrin | 467 | Permethrin (sum of isomers) (F) | yes | yes | yes | 17 | 0 | 0 | 0.05 | 0.05 | 17 | 32 |  |  |
| chlorfenapyr | 48 | Chlorfenapyr | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 16 | 30 |  |  |
| chlorpyrifos | 56 | Chlorpyrifos  (F) | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 17 | 28 |  |  |
| tricyclazole | 394 | Tricyclazole | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 17 | 23 |  |  |
| hexaconazole | 126 | Hexaconazole | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 17 | 21 |  |  |
| acetamiprid | 10 | Acetamiprid  (R) | NO | yes | no | 0 | 0 | 17 |  |  | 0 | 21 | MISSING_FROM_A_k | snapshot CHỈ có định nghĩa dư lượng REVISED 'Acetamiprid (R)' id=10; record sớm nhất 20/08/2025 + 12/05/2026 (SAU cửa sổ) -> 0 MRL ràng buộc in-window 2015-2024; định nghĩa CŨ không còn trong snapshot -> cần khôi phục CELEX/định nghĩa cũ |
| propiconazole | 188 | Propiconazole (sum of isomers) (F) | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 17 | 20 |  |  |
| dithiocarbamates | 83 | Dithiocarbamates (dithiocarbamates expressed as CS2, including maneb, mancozeb, metiram, propineb, thiram and ziram) | yes | yes | yes | 17 | 0 | 0 | 0.05 | 5.0 | 8 | 16 |  |  |
| imidacloprid | 326 | Imidacloprid | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 10 | 15 |  |  |
| carbofuran | 39 | Carbofuran (sum of carbofuran (including any carbofuran generated from carbosulfan, benfuracarb or furathiocarb) and 3-OH carbofuran expressed as carbofuran) (R) | yes | yes | yes | 17 | 0 | 0 | 0.002 | 0.01 | 17 | 15 |  |  |
| dinotefuran | 2322 | Dinotefuran | yes | yes | yes | 1 | 16 | 0 | 8.0 | 8.0 | 0 | 13 |  | id=2322 trong A_k nhưng record 05/06/2014 value=None (NULL) cho hầu hết mã -> pending_celex_recovery; chỉ 1 mã VN có giá trị số |
| profenofos | 186 | Profenofos  (F) | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 14 | 12 |  |  |
| cypermethrin | 65 | Cypermethrin (cypermethrin including other mixtures of constituent isomers (sum of isomers)) (F) | yes | yes | yes | 17 | 0 | 0 | 0.05 | 2.0 | 4 | 11 |  |  |
| acephate | 9 | Acephate | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 17 | 10 |  |  |
| methamidophos | 154 | Methamidophos | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 17 | 10 |  |  |
| dimethoate | 76 | Dimethoate | yes | yes | yes | 17 | 0 | 0 | 0.01 | 0.01 | 17 | 8 |  |  |
| fipronil | 302 | Fipronil (sum fipronil + sulfone metabolite (MB46136) expressed as fipronil) (F) | yes | yes | yes | 17 | 0 | 0 | 0.005 | 0.005 | 17 | 8 |  |  |
