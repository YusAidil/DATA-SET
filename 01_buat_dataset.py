# -*- coding: utf-8 -*-
"""
Membuat dataset "Kerentanan Sosial-Ekonomi Kabupaten/Kota di Indonesia".
Sumber data: Badan Pusat Statistik (BPS) - komponen IPM Metode Baru.
  - UHH  = Umur Harapan Hidup Saat Lahir (Tahun), 2024        [bps id 414]
  - HLS  = Harapan Lama Sekolah (Tahun), 2025                 [bps id 417]
  - RLS  = Rata-rata Lama Sekolah (Tahun), 2025               [bps id 415]
  - Pengeluaran = Pengeluaran per Kapita Disesuaikan (Ribu Rupiah/Orang/Tahun), 2025 [bps id 416]
Data nyata, diambil dari www.bps.go.id (bukan Kaggle/GitHub).
"""
import pandas as pd

# Format tiap baris: Provinsi | Kabupaten/Kota | UHH | HLS | RLS | Pengeluaran(ribu Rp)
DATA = """
Aceh|Simeulue|65.73|14.59|10.09|8555
Aceh|Aceh Singkil|67.89|14.37|9.05|10227
Aceh|Aceh Selatan|64.97|14.72|9.25|9573
Aceh|Aceh Tenggara|68.78|14.52|10.39|9097
Aceh|Aceh Timur|69.18|13.09|8.80|10284
Aceh|Aceh Tengah|69.30|15.04|10.35|12175
Aceh|Aceh Barat|68.48|14.94|10.27|10937
Aceh|Aceh Besar|70.29|14.92|10.69|11072
Aceh|Pidie|67.41|14.53|9.37|11607
Aceh|Bireuen|71.83|14.98|9.92|10418
Aceh|Aceh Utara|69.28|14.76|9.38|9813
Aceh|Aceh Barat Daya|65.65|13.70|9.11|9922
Aceh|Gayo Lues|66.03|14.73|8.75|10237
Aceh|Aceh Tamiang|70.21|14.52|9.42|9959
Aceh|Nagan Raya|69.75|14.19|9.57|9759
Aceh|Aceh Jaya|67.69|14.07|9.34|11324
Aceh|Bener Meriah|69.79|13.93|10.41|12657
Aceh|Pidie Jaya|70.77|15.02|9.80|11543
Aceh|Kota Banda Aceh|72.17|17.95|13.37|18356
Aceh|Kota Sabang|71.17|14.98|11.23|13040
Aceh|Kota Langsa|69.92|15.72|11.60|13510
Aceh|Kota Lhokseumawe|72.25|15.56|11.64|13071
Aceh|Kota Subulussalam|64.51|15.32|8.75|8910
Sumatera Utara|Nias|70.52|13.32|6.41|8115
Sumatera Utara|Mandailing Natal|63.65|14.10|9.17|11100
Sumatera Utara|Tapanuli Selatan|65.74|13.90|9.60|12557
Sumatera Utara|Tapanuli Tengah|68.18|13.51|8.93|11687
Sumatera Utara|Tapanuli Utara|69.77|13.75|10.50|12643
Sumatera Utara|Toba Samosir|71.42|13.82|10.78|13333
Sumatera Utara|Labuhan Batu|70.99|13.30|9.53|12537
Sumatera Utara|Asahan|69.27|12.84|9.06|12760
Sumatera Utara|Simalungun|72.38|13.16|9.74|12585
Sumatera Utara|Dairi|70.27|13.54|10.09|11794
Sumatera Utara|Karo|72.44|13.27|10.30|13583
Sumatera Utara|Deli Serdang|72.48|13.46|10.50|13697
Sumatera Utara|Langkat|69.90|13.29|8.95|12452
Sumatera Utara|Nias Selatan|69.80|13.12|6.61|8082
Sumatera Utara|Humbang Hasundutan|70.49|13.47|10.26|9097
Sumatera Utara|Pakpak Bharat|67.24|13.92|9.94|9462
Sumatera Utara|Samosir|72.41|13.53|9.81|10057
Sumatera Utara|Serdang Bedagai|69.83|12.66|9.13|12429
Sumatera Utara|Batu Bara|68.11|13.13|8.71|11747
Sumatera Utara|Padang Lawas Utara|67.99|13.73|10.05|11371
Sumatera Utara|Padang Lawas|67.87|14.11|9.64|10258
Sumatera Utara|Labuhan Batu Selatan|69.73|13.54|9.29|12797
Sumatera Utara|Labuhan Batu Utara|70.47|13.59|9.15|13347
Sumatera Utara|Nias Utara|70.44|13.38|7.25|7606
Sumatera Utara|Nias Barat|70.20|13.17|7.43|7032
Sumatera Utara|Kota Sibolga|70.38|13.44|10.46|13317
Sumatera Utara|Kota Tanjung Balai|64.44|13.16|9.90|12726
Sumatera Utara|Kota Pematang Siantar|75.05|14.62|11.83|13783
Sumatera Utara|Kota Tebing Tinggi|71.78|13.14|10.88|14499
Sumatera Utara|Kota Medan|74.16|14.80|11.80|16489
Sumatera Utara|Kota Binjai|73.28|14.19|11.21|12409
Sumatera Utara|Kota Padangsidimpuan|70.43|14.72|11.22|12274
Sumatera Utara|Kota Gunungsitoli|72.25|13.95|8.95|9477
Sumatera Barat|Kepulauan Mentawai|65.27|13.17|8.21|7451
Sumatera Barat|Pesisir Selatan|71.59|13.38|9.06|10633
Sumatera Barat|Solok|69.80|13.66|8.25|11318
Sumatera Barat|Sijunjung|67.32|12.99|8.66|11829
Sumatera Barat|Tanah Datar|70.96|15.06|9.46|11552
Sumatera Barat|Padang Pariaman|70.10|14.21|8.78|12089
Sumatera Barat|Agam|73.47|14.26|9.57|11034
Sumatera Barat|Lima Puluh Kota|70.46|13.53|8.49|10917
Sumatera Barat|Pasaman|68.61|13.65|8.49|9418
Sumatera Barat|Solok Selatan|68.99|13.08|9.20|11542
Sumatera Barat|Dharmasraya|72.60|13.02|9.31|12604
Sumatera Barat|Pasaman Barat|68.81|13.73|9.28|10231
Sumatera Barat|Kota Padang|74.42|16.58|11.64|15957
Sumatera Barat|Kota Solok|74.73|14.59|11.38|13504
Sumatera Barat|Kota Sawah Lunto|70.92|13.89|10.54|11501
Sumatera Barat|Kota Padang Panjang|73.61|15.74|12.01|12148
Sumatera Barat|Kota Bukittinggi|75.42|15.29|11.66|14579
Sumatera Barat|Kota Payakumbuh|74.77|14.79|11.08|14536
Sumatera Barat|Kota Pariaman|71.17|14.81|11.32|14261
Riau|Kuantan Singingi|69.44|13.39|9.33|11400
Riau|Indragiri Hulu|70.86|12.78|8.62|11495
Riau|Indragiri Hilir|68.70|12.39|7.49|11248
Riau|Pelalawan|72.13|12.92|8.97|13052
Riau|Siak|71.75|13.02|9.93|13546
Riau|Kampar|71.56|13.70|9.78|12200
Riau|Rokan Hulu|70.95|13.03|9.11|10769
Riau|Bengkalis|71.92|13.47|9.93|12521
Riau|Rokan Hilir|71.11|12.90|8.55|10895
Riau|Kepulauan Meranti|68.48|12.90|8.13|9380
Riau|Kota Pekanbaru|73.21|15.85|12.08|15610
Riau|Kota Dumai|71.78|13.36|10.30|13369
Jambi|Kerinci|70.80|14.18|8.76|11650
Jambi|Merangin|71.95|12.50|8.41|11847
Jambi|Sarolangun|69.92|12.82|8.60|13030
Jambi|Batang Hari|71.55|13.20|8.41|11219
Jambi|Muaro Jambi|72.09|13.38|8.72|10579
Jambi|Tanjung Jabung Timur|67.26|12.22|7.71|10626
Jambi|Tanjung Jabung Barat|68.91|12.71|8.54|11266
Jambi|Tebo|70.69|13.20|8.05|11791
Jambi|Bungo|68.71|12.92|8.61|13182
Jambi|Kota Jambi|73.66|15.56|11.59|13706
Jambi|Kota Sungai Penuh|73.20|14.85|10.75|11994
Sumatera Selatan|Ogan Komering Ulu|69.02|13.01|9.07|11700
Sumatera Selatan|Ogan Komering Ilir|69.48|11.99|7.49|12547
Sumatera Selatan|Muara Enim|69.93|12.03|8.45|12646
Sumatera Selatan|Lahat|67.11|12.46|9.03|11620
Sumatera Selatan|Musi Rawas|69.15|12.43|7.61|11407
Sumatera Selatan|Musi Banyuasin|69.72|12.34|8.29|11790
Sumatera Selatan|Banyu Asin|69.96|12.54|7.65|11638
Sumatera Selatan|Ogan Komering Ulu Selatan|68.25|12.02|8.48|10010
Sumatera Selatan|Ogan Komering Ulu Timur|70.00|12.66|8.13|13154
Sumatera Selatan|Ogan Ilir|66.54|12.43|8.16|12445
Sumatera Selatan|Empat Lawang|65.87|12.12|8.02|11315
Sumatera Selatan|Penukal Abab Lematang Ilir|69.17|12.69|7.42|9965
Sumatera Selatan|Musi Rawas Utara|66.56|12.07|7.80|11460
Sumatera Selatan|Kota Palembang|72.35|14.47|11.25|16725
Sumatera Selatan|Kota Prabumulih|71.59|13.42|10.37|14342
Sumatera Selatan|Kota Pagar Alam|67.98|13.51|9.78|10610
Sumatera Selatan|Kota Lubuklinggau|70.59|13.88|10.15|15090
Bengkulu|Bengkulu Selatan|68.53|13.67|9.60|11518
Bengkulu|Rejang Lebong|69.42|14.21|9.05|11824
Bengkulu|Bengkulu Utara|68.99|12.93|8.35|12045
Bengkulu|Kaur|67.51|13.16|8.71|10180
Bengkulu|Seluma|68.53|13.34|8.34|9919
Bengkulu|Mukomuko|67.57|13.06|8.65|12055
Bengkulu|Lebong|64.13|12.92|8.48|12776
Bengkulu|Kepahiang|68.61|13.31|8.61|11010
Bengkulu|Bengkulu Tengah|68.64|13.64|7.94|10973
Bengkulu|Kota Bengkulu|71.03|16.08|11.95|15971
Lampung|Lampung Barat|68.40|12.31|8.57|11612
Lampung|Tanggamus|69.56|12.34|7.63|10888
Lampung|Lampung Selatan|70.32|12.79|7.98|11540
Lampung|Lampung Timur|71.53|13.00|8.46|11670
Lampung|Lampung Tengah|70.55|13.18|8.17|12975
Lampung|Lampung Utara|70.13|12.64|8.63|10160
Lampung|Way Kanan|70.16|12.53|7.91|10831
Lampung|Tulangbawang|70.56|12.39|7.90|12513
Lampung|Pesawaran|70.13|12.64|8.01|9638
Lampung|Pringsewu|71.21|13.09|8.72|11950
Lampung|Mesuji|69.04|11.97|7.30|9843
Lampung|Tulang Bawang Barat|70.64|12.13|7.81|10032
Lampung|Pesisir Barat|64.69|12.31|8.76|9879
Lampung|Kota Bandar Lampung|72.24|14.74|11.11|14270
Lampung|Kota Metro|72.44|14.97|11.19|13380
Kep. Bangka Belitung|Bangka|71.80|13.13|8.77|13411
Kep. Bangka Belitung|Belitung|71.75|12.10|9.11|14559
Kep. Bangka Belitung|Bangka Barat|70.59|11.95|7.80|13380
Kep. Bangka Belitung|Bangka Tengah|72.36|12.34|7.33|13768
Kep. Bangka Belitung|Bangka Selatan|69.24|11.78|7.25|12920
Kep. Bangka Belitung|Belitung Timur|72.85|11.78|9.03|12694
Kep. Bangka Belitung|Kota Pangkal Pinang|74.24|13.50|10.90|16856
Kepulauan Riau|Karimun|72.20|12.63|9.06|13649
Kepulauan Riau|Bintan|71.21|13.46|9.45|15303
Kepulauan Riau|Natuna|66.41|13.95|9.25|15683
Kepulauan Riau|Lingga|63.73|12.77|7.87|13108
Kepulauan Riau|Kepulauan Anambas|68.37|13.07|7.79|13141
Kepulauan Riau|Kota Batam|74.28|13.57|11.34|19944
Kepulauan Riau|Kota Tanjung Pinang|73.02|14.19|10.80|16838
DKI Jakarta|Kepulauan Seribu|69.78|12.97|9.27|14691
DKI Jakarta|Kota Jakarta Selatan|75.02|14.28|12.06|26387
DKI Jakarta|Kota Jakarta Timur|75.38|14.32|12.01|19824
DKI Jakarta|Kota Jakarta Pusat|75.09|13.50|11.62|19309
DKI Jakarta|Kota Jakarta Barat|74.48|13.47|11.25|22831
DKI Jakarta|Kota Jakarta Utara|73.69|13.05|11.08|20584
Banten|Pandeglang|65.79|13.75|7.50|9923
Banten|Lebak|68.34|12.12|6.78|10165
Banten|Tangerang|70.88|12.89|9.16|13625
Banten|Serang|65.90|13.02|8.03|12065
Banten|Kota Tangerang|72.46|13.96|11.46|16058
Banten|Kota Cilegon|67.66|13.41|10.40|14759
Banten|Kota Serang|69.27|12.85|8.94|15250
Banten|Kota Tangerang Selatan|73.31|14.71|12.10|17396
DI Yogyakarta|Kulon Progo|75.41|14.55|9.33|11499
DI Yogyakarta|Bantul|74.17|15.91|10.11|17240
DI Yogyakarta|Gunung Kidul|74.35|13.56|7.64|11006
DI Yogyakarta|Sleman|75.29|16.80|11.42|18231
DI Yogyakarta|Kota Yogyakarta|75.11|17.67|12.13|21104
Bali|Jembrana|73.51|13.13|8.71|13113
Bali|Tabanan|74.80|13.37|9.81|15752
Bali|Badung|76.18|14.26|11.26|19004
Bali|Gianyar|74.86|14.12|9.93|16244
Bali|Klungkung|72.50|13.14|8.75|13023
Bali|Bangli|71.63|12.54|7.80|12447
Bali|Karangasem|71.53|12.92|6.98|11676
Bali|Buleleng|72.92|13.31|7.94|14827
Bali|Kota Denpasar|76.01|14.14|11.64|21185
Nusa Tenggara Barat|Lombok Barat|68.35|14.17|7.15|12544
Nusa Tenggara Barat|Lombok Tengah|67.32|13.90|7.08|11870
Nusa Tenggara Barat|Lombok Timur|67.20|14.08|7.71|10851
Nusa Tenggara Barat|Sumbawa|68.81|13.35|8.88|10716
Nusa Tenggara Barat|Dompu|67.99|14.01|9.38|10230
Nusa Tenggara Barat|Bima|67.52|13.67|8.61|9821
Nusa Tenggara Barat|Sumbawa Barat|69.54|13.84|9.35|12983
Nusa Tenggara Barat|Lombok Utara|68.43|13.16|6.75|10502
Nusa Tenggara Barat|Kota Mataram|72.75|15.69|9.89|16851
Nusa Tenggara Barat|Kota Bima|71.41|15.21|10.97|12623
Kalimantan Selatan|Tanah Laut|70.31|12.70|8.09|12986
Kalimantan Selatan|Kotabaru|69.93|12.23|7.71|13163
Kalimantan Selatan|Banjar|68.26|13.05|8.15|14101
Kalimantan Selatan|Barito Kuala|67.07|12.69|7.99|11469
Kalimantan Selatan|Tapin|71.35|12.60|8.38|13381
Kalimantan Selatan|Hulu Sungai Selatan|67.17|12.78|8.18|14453
Kalimantan Selatan|Hulu Sungai Tengah|67.12|12.58|8.45|13608
Kalimantan Selatan|Hulu Sungai Utara|65.26|13.47|8.00|11168
Kalimantan Selatan|Tabalong|71.46|13.18|9.37|13541
Kalimantan Selatan|Tanah Bumbu|71.11|12.80|8.44|13380
Kalimantan Selatan|Balangan|68.59|13.35|8.34|12675
Kalimantan Selatan|Kota Banjarmasin|72.10|14.02|10.36|16013
Kalimantan Selatan|Kota Banjar Baru|72.82|14.87|11.07|15361
"""


def main():
    rows = []
    for line in DATA.strip().splitlines():
        prov, nama, uhh, hls, rls, peng = line.split("|")
        rows.append({
            "Provinsi": prov,
            "Kabupaten/Kota": nama,
            "Umur Harapan Hidup (Tahun)": float(uhh),
            "Harapan Lama Sekolah (Tahun)": float(hls),
            "Rata-rata Lama Sekolah (Tahun)": float(rls),
            "Pengeluaran per Kapita (Ribu Rupiah)": int(peng),
        })
    df = pd.DataFrame(rows)
    df.to_excel("Kesejahteraan_Daerah.xlsx", index=False)
    print("Jumlah baris :", len(df))
    print("Jumlah kolom :", df.shape[1])
    print(df.head(10).to_string(index=False))
    print("\nFile disimpan: Kesejahteraan_Daerah.xlsx")


if __name__ == "__main__":
    main()
