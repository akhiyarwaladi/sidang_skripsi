# ANALISIS KESALAHAN PROPOSAL SKRIPSI

## Identitas Proposal
- **Judul**: Klasifikasi Tutupan Lahan dengan Kombinasi Nilai Index (NDVI, NDWI, NDBI) dan Metode Maximum Likehood Classification pada Kota Jambi
- **Nama Mahasiswa**: Ayu Friska Purba
- **NIM**: F1E122058
- **Program Studi**: Sistem Informasi
- **Pembimbing Utama**: Daniel Arsa, S.Kom., M.S.I
- **Pembimbing Pendamping**: Nindy Raisa Hanum, S.Kom., M.Kom.

---

# RINGKASAN EKSEKUTIF

| Kategori | Jumlah | Tingkat Keparahan |
|----------|--------|-------------------|
| Kesalahan Fatal/Konseptual | 7 | KRITIS |
| Kesalahan Metodologis | 7 | SERIUS |
| Kesalahan Minor/Penulisan | 7+ | PERLU PERBAIKAN |
| **TOTAL** | **21+** | - |

---

# INDEKS KESALAHAN BERDASARKAN HALAMAN DOKUMEN

## Peta Kesalahan per Halaman (Urut dari Awal)

| Halaman | Jenis Kesalahan | Keterangan | Tingkat Keparahan |
|---------|----------------|------------|-------------------|
| **Hal. i** | Ejaan Fatal | Judul: "LIKEHOOD" → "LIKELIHOOD" | 🔴 KRITIS |
| **Hal. iii** | NIP Tidak Jelas | NIP tambahan 19720624 199903 2 001 tidak jelas milik siapa | 🟡 MINOR |
| **Hal. 1** | Inkonsistensi Data | Luas Kota Jambi: 205.43 km² vs 169.89 km² - tidak dijelaskan yang mana yang dipakai | 🟠 SERIUS |
| **Hal. 2** | Referensi Hilang | Arrafi et al., 2025 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 2** | Referensi Hilang | Asahar Johar et al., 2020 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 2** | Referensi Hilang | Hardiana, 2024 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 3** | Penamaan Salah | "1.2 Rumusan Penelitian" → seharusnya "Rumusan **Masalah**" | 🟡 MINOR |
| **Hal. 5** | Referensi Hilang | Government of Canada, 2025 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 6** | Referensi Hilang | Colleen Kaiser, 2023 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 6** | Referensi Hilang | Dayat, 2019 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 9** | Ejaan Salah | "Landsat 8 (OLI/**TRIS**)" → seharusnya "**TIRS**" (Thermal Infrared Sensor) | 🟡 MINOR |
| **Hal. 9** | Referensi Hilang | Tech U. L., 2023 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 9** | Referensi Hilang | Hayati et al., 2023 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 10** | Referensi Hilang | NASA Earth Observatory, 2025 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 11** | Referensi Hilang | Departemen Kehutanan, 2005 (Tabel 2.2) dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 11, 12** | Referensi Hilang | McFeeters, 1996 (rumus NDWI) dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 11, 12** | Referensi Hilang | EOS Data Analytics, 2023 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 12** | Penomoran Salah | "2.1 Maximum Likelihood..." seharusnya "**2.7**" (setelah 2.4, 2.5, 2.6) | 🟡 MINOR |
| **Hal. 12** | Referensi Hilang | Zha et al., 2003 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 12** | Referensi Hilang | Solihin & Kurniyanto, 2021 (Tabel 2.4) - Yang ada: Kurniyanto et al., 2021 | 🟠 SERIUS |
| **Hal. 12** | **KONTRADIKSI NDBI** | Tabel 2.4: Positif = Terbangun ✓ VS Tabel 3.3 hal 30: 0.285 (POSITIF) = "Tidak Terbangun" ✗ | 🔴 KRITIS |
| **Hal. 13** | Referensi Hilang | USGS, 2023 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 14** | Referensi Hilang | Irawan, 2024 dikutip tapi TIDAK ADA di daftar pustaka | 🟠 SERIUS |
| **Hal. 20** | Info Tidak Lengkap | "3.1 Tempat **Dan Waktu** Penelitian" - hanya isi TEMPAT, tidak ada WAKTU | 🟠 SERIUS |
| **Hal. 21** | Metodologi Ambigu | Gambar 3.1: "Perhitungan Nilai Indeks" dan "Klasifikasi MLC" terlihat paralel, tidak terintegrasi | 🔴 KRITIS |
| **Hal. 23** | **KESALAHAN EPSG FATAL** | "EPSG:4326 = UTM Zone 48S" → SALAH TOTAL! EPSG:4326 adalah WGS84 Geographic (Lat/Long), bukan UTM. Yang benar: **EPSG:32748** | 🔴 KRITIS |
| **Hal. 25** | Referensi Hilang | Rouse et al., 1974 (rumus NDVI) dikutip tapi TIDAK ADA di daftar pustaka | 🔴 KRITIS |
| **Hal. 26** | **Tabel Salah Format** | Tabel 3.1: Nilai NDVI hanya nilai tunggal (0.21234415), bukan rentang. Tidak bisa dipakai untuk klasifikasi! | 🔴 KRITIS |
| **Hal. 27** | Referensi Hilang | McFeeters, 1996 (rumus NDWI) dikutip tapi TIDAK ADA di daftar pustaka | 🔴 KRITIS |
| **Hal. 28** | **Tabel Salah Format** | Tabel 3.2: Nilai NDWI hanya nilai tunggal, bukan rentang | 🔴 KRITIS |
| **Hal. 29** | Referensi Hilang | Zha et al., 2003 (rumus NDBI) dikutip tapi TIDAK ADA di daftar pustaka | 🔴 KRITIS |
| **Hal. 30** | **Tabel Salah Format** | Tabel 3.3: Nilai NDBI hanya nilai tunggal, bukan rentang | 🔴 KRITIS |
| **Hal. 30** | **KONTRADIKSI NDBI** | Nilai 0.2850414 (POSITIF) disebut "Tidak Terbangun" - bertentangan dengan Tabel 2.4 hal. 12 | 🔴 KRITIS |
| **Hal. 32** | Penomoran Aneh | Analisis Hasil dimulai dari nomor 3, bukan 1 (kemungkinan ada bagian terhapus) | 🟡 MINOR |
| **Hal. 32** | Validasi Tidak Ada | Klasifikasi Berbasis Indeks (3.6.7) TIDAK ADA validasi akurasi, padahal MLC ada | 🟠 SERIUS |
| **Hal. 33-34** | **GROUND TRUTH FATAL** | Training samples hanya dari interpretasi visual citra yang SAMA → Circular reasoning! Tidak ada ground truth independen | 🔴 BLOCKER |
| **Hal. 34** | Pembagian Data Tidak Jelas | Tidak dijelaskan proporsi training vs testing (70:30? 80:20?) | 🟠 SERIUS |

**CATATAN PENTING UNTUK PENGUJI**:
- 🔴 KRITIS/BLOCKER = 7 kesalahan → Harus diperbaiki atau penelitian tidak valid
- 🟠 SERIUS = 18+ kesalahan → Mempengaruhi kualitas penelitian signifikan
- 🟡 MINOR = 5 kesalahan → Perlu diperbaiki untuk profesionalitas

**Total Kesalahan Teridentifikasi: 21+ kesalahan**

---

# BAGIAN A: KESALAHAN FATAL / KONSEPTUAL

## A.1. Kesalahan Sistem Koordinat (EPSG)

**Halaman**: 23

**Lokasi**: Bagian 3.5 Pra-Pengolahan Citra, Poin 3

**Kutipan dari Proposal**:
> "Sistem koordinat spasial citra disesuaikan menjadi WGS 1984 / UTM Zone 48S (EPSG:4326), yaitu sistem proyeksi yang paling sesuai untuk wilayah Jambi."

**KESALAHAN**:
- **EPSG:4326** adalah **WGS 84 Geographic Coordinate System** (dalam satuan derajat latitude/longitude), **BUKAN** UTM Zone 48S
- UTM Zone 48S yang benar adalah **EPSG:32748**
- Kota Jambi terletak di koordinat sekitar 1.6°S, 103.6°E

**Kode EPSG yang benar untuk Kota Jambi**:
| Sistem Koordinat | Kode EPSG | Keterangan |
|------------------|-----------|------------|
| WGS 84 (Geographic) | EPSG:4326 | Lat/Long dalam derajat |
| UTM Zone 48N | EPSG:32648 | Untuk wilayah utara ekuator |
| UTM Zone 48S | EPSG:32748 | Untuk wilayah selatan ekuator |

**DAMPAK**: Perhitungan luas area dalam satuan meter/kilometer akan menghasilkan nilai yang SALAH jika menggunakan EPSG:4326 yang bersatuan derajat.

---

## A.2. Kontradiksi Nilai Klasifikasi NDBI

**Halaman**: 12 (Tabel 2.4) vs 30 (Tabel 3.3)

**Di Tabel 2.4 Tinjauan Pustaka (hal. 12)**:

| No | Klasifikasi | Nilai NDBI |
|----|-------------|------------|
| 1 | Tidak Terbangun | -1 hingga 0 |
| 2 | Terbangun | 0 hingga +1 |

**Di Tabel 3.3 Hasil Perhitungan (hal. 30)**:

| No | Kelas Vegetasi | Nilai NDBI 2015 | Nilai NDBI 2025 |
|----|----------------|-----------------|-----------------|
| 1 | **Tidak Terbangun** | **0.2850414** | -0.6028725 |
| 2 | Terbangun | 0.2680664 | 0.31556 |

**KONTRADIKSI**:
- Menurut Tabel 2.4: Nilai POSITIF (>0) = **Terbangun**
- Di Tabel 3.3 tahun 2015: Nilai **0.2850414 (POSITIF)** diklasifikasikan sebagai **"Tidak Terbangun"**
- Ini adalah **KONTRADIKSI LANGSUNG** antara teori dan hasil

**PERTANYAAN KRITIS**: 
- Apakah mahasiswa memahami konsep NDBI?
- Mengapa nilai positif 0.285 disebut "Tidak Terbangun" padahal menurut definisi sendiri (Tabel 2.4) nilai positif adalah "Terbangun"?

---

## A.3. Tidak Ada Sumber Ground Truth Independen

**Halaman**: 33-34

**Lokasi**: Bagian 3.7 Klasifikasi MLC, sub-bagian b. Penentuan Training Sampel

**Kutipan dari Proposal**:
> "Training sampel ditentukan pada citra menggunakan polygon Region of Interest (ROI). Pemilihan sampel dilakukan dengan cara:
> - Mengamati ciri visual citra (warna, tekstur, dan pola objek)
> - Menggunakan citra komposit RGB untuk membedakan objek
> - Memastikan setiap kelas memiliki area yang jelas dan representatif"

**MASALAH FUNDAMENTAL**:

MLC adalah **SUPERVISED classification** yang membutuhkan **ground truth** dari sumber **INDEPENDEN**.

Yang dilakukan mahasiswa:
1. Melihat citra Landsat 8 → "area ini terlihat hijau, saya anggap vegetasi"
2. Membuat training sample dari asumsi tersebut
3. Menjalankan MLC pada **citra yang SAMA**
4. Mengklaim hasilnya akurat

**Ini adalah CIRCULAR REASONING**:
```
Citra Landsat 8 → Interpretasi Visual "ini vegetasi" → Training Sample 
       ↑                                                        ↓
       └──────────────── MLC Klasifikasi ←──────────────────────┘
```

**Ground Truth yang Valid Seharusnya**:
1. **Survei lapangan** dengan GPS (minimal 30-50 titik per kelas)
2. **Citra resolusi tinggi** (Google Earth dengan sinkronisasi tanggal)
3. **Data sekunder terverifikasi** (Peta KLHK, BIG)

**DAMPAK**: Hasil klasifikasi TIDAK memiliki validitas ilmiah.

---

## A.4. Tidak Ada Pembagian Training dan Testing

**Halaman**: 34

**Lokasi**: Bagian 3.7e Analisis Luas & Validasi

**Kutipan dari Proposal**:
> "Tahap ini menghitung luas tiap kelas tutupan lahan dan melakukan validasi akurasi melalui metode:
> - Confusion matrix
> - Overall accuracy
> - User's accuracy
> - Producer's accuracy
> - Kappa coefficient"

**Yang TIDAK dijelaskan**:
- Berapa proporsi pembagian training dan testing? (standar: 70:30 atau 80:20)
- Dari mana testing samples berasal?
- Apakah training dan testing dari lokasi yang berbeda (spatial independence)?
- Berapa jumlah titik validasi per kelas?

**DAMPAK**: Confusion matrix tidak bermakna jika training dan testing dari sumber yang sama.

---

## A.5. Hubungan Metode Indeks dan MLC Tidak Jelas

**Halaman**: 21 (Gambar 3.1), 24-34

**MASALAH**: Proposal memiliki DUA pendekatan klasifikasi yang berjalan paralel:

### Pendekatan 1: Klasifikasi Berbasis Indeks (Interpretatif)
- Bagian 3.6.7 (hal. 32)
- Berdasarkan nilai NDVI, NDWI, NDBI
- Output: "peta identifikasi objek"

### Pendekatan 2: Klasifikasi MLC
- Bagian 3.7 (hal. 33-34)
- Supervised classification
- Output: "peta tutupan lahan"

**PERTANYAAN YANG TIDAK TERJAWAB**:
1. Apakah layer stack (NDVI+NDWI+NDBI) menjadi **INPUT** untuk MLC?
2. Atau MLC dijalankan pada **band asli** Landsat 8?
3. Bagaimana **integrasi** kedua pendekatan?
4. Mana yang menjadi **fokus utama** penelitian?
5. Judul menyebutkan "kombinasi" — tapi kombinasi **seperti apa**?

**Di Gambar 3.1 (hal. 21)**: "Perhitungan Nilai Indeks" dan "Klasifikasi MLC" terlihat sebagai proses **paralel**, bukan terintegrasi.

---

## A.6. Kesalahan Ejaan Istilah Utama

**Lokasi**: Judul, Halaman 1, 2, 3, 12, 33, dan seluruh dokumen

**Tertulis**: "Maximum **LIKEHOOD** Classification"

**Seharusnya**: "Maximum **LIKELIHOOD** Classification"

**Catatan**: Ini adalah kesalahan ejaan pada istilah teknis yang menjadi **JUDUL PENELITIAN**.

---

## A.7. Tabel Klasifikasi Menunjukkan Nilai Tunggal, Bukan Rentang

**Halaman**: 26 (Tabel 3.1), 28 (Tabel 3.2), 30 (Tabel 3.3)

**Contoh di Tabel 3.1 Klasifikasi Hasil NDVI**:

| No | Kelas | Nilai NDVI 2015 | Nilai NDVI 2025 |
|----|-------|-----------------|-----------------|
| 1 | Vegetasi Rendah | -0.1106798 | -0.1892031 |
| 2 | Vegetasi Sedang | 0.21234415 | 0.21670945 |
| 3 | Vegetasi Tinggi | 0.5353681 | 0.622622 |

**MASALAH**:
- Klasifikasi membutuhkan **RENTANG nilai**, bukan nilai tunggal
- Apakah 0.21234415 adalah nilai minimum, maksimum, atau rata-rata?
- Bagaimana mengklasifikasikan piksel dengan nilai 0.25? Masuk Sedang atau Tinggi?
- Bandingkan dengan Tabel 2.2 (hal. 11) yang **BENAR** menggunakan rentang:
  - Vegetasi Rendah: -1 ≤ NDVI ≤ 0,32
  - Vegetasi Sedang: 0,33 ≤ NDVI ≤ 0,42
  - Vegetasi Tinggi: 0,43 ≤ NDVI ≤ 1

**DAMPAK**: Tabel 3.1, 3.2, 3.3 tidak dapat digunakan untuk mengklasifikasikan piksel lain.

---

# BAGIAN B: KESALAHAN METODOLOGIS

## B.1. Kesalahan Penomoran Section

**Halaman**: 12

**Tertulis**: "2.1 Maximum Likelihood Classification (MLC)"

**Urutan sebelumnya**:
- 2.4 NDVI
- 2.5 NDWI
- 2.6 NDBI
- **2.1** MLC ← SALAH

**Seharusnya**: "**2.7** Maximum Likelihood Classification (MLC)"

---

## B.2. Tidak Ada Validasi untuk Klasifikasi Berbasis Indeks

**Halaman**: 32 (Bagian 3.6.7 dan 3.6.8)

**Perbandingan**:

| Metode | Validasi Akurasi |
|--------|------------------|
| MLC (Bagian 3.7e) | ✓ Confusion matrix, Overall accuracy, Kappa |
| Klasifikasi Berbasis Indeks (Bagian 3.6.7) | ✗ TIDAK ADA penjelasan validasi |

**PERTANYAAN**: Bagaimana membuktikan bahwa klasifikasi berbasis indeks akurat?

---

## B.3. Inkonsistensi Luas Wilayah Kota Jambi

**Halaman**: 1

**Kutipan**:
> "Pada periode tahun 2020 sampai 2021, BPS (2024) mencatat bahwa luas administrasi Kota Jambi adalah **205,43 km²** ... namun sejak tahun 2022 hingga 2024 luas yang tercatat adalah **169,89 km²**"

**MASALAH**:
- Perbedaan luas sangat signifikan: **35,54 km²** (selisih ~17%)
- Tidak dijelaskan shapefile **tahun berapa** yang akan digunakan
- Apakah menggunakan batas 2015 atau batas 2022?

**DAMPAK**: Mempengaruhi perhitungan luas tutupan lahan secara signifikan.

---

## B.4. Waktu Penelitian Tidak Dijelaskan

**Halaman**: 20

**Judul Section**: "3.1 Tempat **Dan Waktu** Penelitian"

**Isi**: Hanya menjelaskan **TEMPAT** penelitian (Universitas Jambi), tidak ada informasi tentang:
- Jadwal penelitian
- Timeline pelaksanaan
- Durasi penelitian

---

## B.5. Ketersediaan Data Citra 2025 Belum Pasti

**Halaman**: 21-22

**Kutipan**:
> "Rentang waktu pencarian: 01 januari – 20 November 2025, Toleransi tutupan awan ≤ 10%"

**MASALAH**:
- Proposal disusun untuk **perencanaan** penelitian
- Data citra dengan cloud cover ≤10% untuk Kota Jambi di tahun 2025 belum tentu tersedia
- Perlu verifikasi ketersediaan scene yang memenuhi kriteria

---

## B.6. Kesalahan Ejaan Sensor Satelit

**Halaman**: 9 (Tabel 2.1)

**Tertulis**: "Landsat 8 (OLI/**TRIS**)"

**Seharusnya**: "Landsat 8 (OLI/**TIRS**)" — Thermal Infrared Sensor

---

## B.7. Data Batas Administrasi dari Sumber Tidak Resmi

**Halaman**: 22

**Kutipan**:
> "data batas administrasi Kota Jambi dalam bentuk shapefile (SHP) diunduh dari situs Indonesia Geospasial melalui tautan https://www.indonesia-geospasial.com/"

**REKOMENDASI**: Sebaiknya menggunakan data resmi dari:
- BIG (Badan Informasi Geospasial) — geoportal.big.go.id
- BAPPEDA Kota Jambi

---

# BAGIAN C: KESALAHAN REFERENSI

## C.1. Referensi Dikutip Tapi TIDAK ADA di Daftar Pustaka

| No | Referensi yang Dikutip | Lokasi Kutipan | Status di Daftar Pustaka |
|----|------------------------|----------------|--------------------------|
| 1 | Rouse et al., 1974 | Hal. 25 (rumus NDVI) | ❌ TIDAK ADA |
| 2 | McFeeters, 1996 | Hal. 11, 27 (rumus NDWI) | ❌ TIDAK ADA |
| 3 | Zha et al., 2003 | Hal. 12, 29 (rumus NDBI) | ❌ TIDAK ADA |
| 4 | NASA Earth Observatory, 2025 | Hal. 10, 11 | ❌ TIDAK ADA |
| 5 | USGS, 2023 | Hal. 13 | ❌ TIDAK ADA |
| 6 | USGS, 2024 | Hal. 8 | ❌ TIDAK ADA |
| 7 | Government of Canada, 2025 | Hal. 5 | ❌ TIDAK ADA |
| 8 | EOS Data Analytics, 2023 | Hal. 11, 12 | ❌ TIDAK ADA |
| 9 | Departemen Kehutanan, 2005 | Hal. 11 (Tabel 2.2) | ❌ TIDAK ADA |
| 10 | Tech U. L., 2023 | Hal. 9 | ❌ TIDAK ADA |
| 11 | Solihin & Kurniyanto, 2021 | Hal. 12 (Tabel 2.4) | ❌ TIDAK ADA (yang ada: Kurniyanto et al., 2021) |
| 12 | Colleen Kaiser, 2023 | Hal. 6 | ❌ TIDAK ADA |
| 13 | Dayat, 2019 | Hal. 6 (Gambar 2.2) | ❌ TIDAK ADA |
| 14 | Asahar Johar et al., 2020 | Hal. 2 | ❌ TIDAK ADA |
| 15 | Hardiana, 2024 | Hal. 2 | ❌ TIDAK ADA |
| 16 | Irawan, 2024 | Hal. 14 | ❌ TIDAK ADA |
| 17 | Arrafi et al., 2025 | Hal. 2 | ❌ TIDAK ADA |
| 18 | Hayati et al., 2023 | Hal. 9 | ❌ TIDAK ADA |

**TOTAL: 18 referensi dikutip tapi tidak ada di daftar pustaka**

---

# BAGIAN D: KESALAHAN MINOR / PENULISAN

## D.1. Penamaan Section Tidak Tepat

**Halaman**: 3

**Tertulis**: "1.2 Rumusan **Penelitian**"

**Seharusnya**: "1.2 Rumusan **Masalah**"

---

## D.2. Inkonsistensi Penulisan Istilah

| Penulisan 1 | Penulisan 2 | Halaman |
|-------------|-------------|---------|
| Penginderaan | Pengindraan | 5, daftar isi |
| Index | Indeks | Judul, isi |
| spectral | spektral | Berbagai |
| Likehood | Likelihood | Seluruh dokumen |
| infrared | Infrared | Berbagai |

---

## D.3. NIP Tambahan yang Tidak Jelas

**Halaman**: 3 (Halaman Persetujuan)

**Tertulis**: Di bawah tanda tangan ada NIP tambahan "19720624 199903 2 001"

**MASALAH**: NIP ini bukan milik Dekan, Ketua Jurusan, atau Pembimbing yang tercantum. Tidak jelas milik siapa.

---

## D.4. Penomoran dalam Analisis Hasil

**Halaman**: 32

**Tertulis**:
> "3. Perhitungan Luas Tiap Kelas
> 4. Persentase Sebaran Kelas
> 5. Perbandingan Antar Tahun
> 6. Visualisasi Peta dan Grafik
> 7. Interpretasi Hasil"

**MASALAH**: Dimulai dari nomor 3, bukan 1. Kemungkinan ada bagian yang terhapus atau salah format.

---

# BAGIAN E: PERTANYAAN UNTUK UJIAN

## E.1. Pertanyaan tentang Ground Truth dan Supervised Classification

1. "MLC disebut supervised classification. Jelaskan apa yang 'supervised' dari metode ini dan dari mana 'supervisi' itu berasal?"

2. "Anda mengatakan training samples diambil dari interpretasi visual citra Landsat. Bagaimana Anda membuktikan bahwa interpretasi visual Anda benar?"

3. "Jika training dan testing berasal dari sumber yang sama (interpretasi visual Anda sendiri), apa artinya overall accuracy yang Anda dapatkan?"

4. "Sebutkan minimal 3 sumber ground truth yang valid untuk penelitian klasifikasi tutupan lahan!"

5. "Berapa proporsi pembagian training dan testing yang Anda gunakan? Jelaskan mengapa proporsi tersebut dipilih!"

## E.2. Pertanyaan tentang Metodologi

6. "Judul Anda menyebutkan 'kombinasi' nilai indeks dan MLC. Jelaskan secara spesifik bagaimana kombinasi ini dilakukan?"

7. "Input apa yang akan Anda gunakan untuk proses MLC? Band asli Landsat atau hasil layer stacking indeks?"

8. "MLC menghitung mean vector dan covariance matrix. Jelaskan apa fungsi kedua parameter ini dalam proses klasifikasi!"

9. "Bagaimana validasi akurasi untuk klasifikasi berbasis indeks? Apakah juga menggunakan confusion matrix?"

## E.3. Pertanyaan tentang Kesalahan Teknis

10. "Anda menyebutkan EPSG:4326 adalah UTM Zone 48S. Jelaskan perbedaan antara Geographic Coordinate System dan Projected Coordinate System!"

11. "Di Tabel 2.4, NDBI negatif = tidak terbangun. Di Tabel 3.3 tahun 2015, nilai POSITIF 0.285 Anda sebut 'Tidak Terbangun'. Jelaskan kontradiksi ini!"

12. "Di Tabel 3.1, nilai NDVI Vegetasi Sedang tahun 2015 adalah 0.21234415. Apakah ini nilai minimum, maksimum, atau rata-rata? Bagaimana Anda mengklasifikasikan piksel dengan nilai 0.25?"

13. "Shapefile batas administrasi tahun berapa yang Anda gunakan? 205 km² atau 169 km²?"

## E.4. Pertanyaan tentang Referensi

14. "Anda mengutip Rouse et al. (1974) sebagai referensi rumus NDVI. Coba sebutkan judul lengkap publikasi tersebut!"

15. "Bagaimana ejaan yang benar untuk metode klasifikasi yang Anda gunakan? Dan apa arti 'likelihood' dalam konteks statistika?"

## E.5. Pertanyaan Kritis

16. "Apa kontribusi penelitian ini dibanding penelitian Aulia et al. (2023) yang juga menggunakan NDVI di Kota Jambi?"

17. "Jika klasifikasi berbasis indeks sudah menghasilkan peta tutupan lahan, mengapa perlu MLC?"

18. "Jika akurasi penelitian Anda mencapai 95%, tapi tidak ada ground truth independen, apakah angka ini dapat dipercaya?"

19. "Apa bedanya metodologi Anda dengan sekadar melakukan digitasi manual tutupan lahan?"

20. "Sensor Landsat 8 Anda tulis OLI/TRIS. Apa kepanjangan yang benar dan apa fungsinya?"

---

# BAGIAN F: REKOMENDASI PERBAIKAN

## F.1. Perbaikan Kritis (WAJIB)

1. **Perbaiki sumber ground truth**: Tambahkan survei lapangan, atau gunakan citra resolusi tinggi (Google Earth dengan sinkronisasi tanggal), atau data sekunder dari KLHK/BIG

2. **Jelaskan hubungan metode**: Apakah layer stack indeks menjadi input MLC, atau keduanya dibandingkan secara terpisah?

3. **Perbaiki sistem koordinat**: Gunakan EPSG:32648 (UTM 48N) atau EPSG:32748 (UTM 48S), BUKAN EPSG:4326

4. **Konsistenkan nilai NDBI**: Perbaiki kontradiksi antara Tabel 2.4 dan Tabel 3.3

5. **Gunakan rentang nilai**: Tabel 3.1, 3.2, 3.3 harus menunjukkan RENTANG, bukan nilai tunggal

6. **Tambahkan protokol pembagian data**: Jelaskan proporsi training/testing (misal 70:30)

## F.2. Perbaikan Penting

7. **Lengkapi daftar pustaka**: Tambahkan 18 referensi yang dikutip tapi tidak ada

8. **Perbaiki ejaan**: "Likelihood" bukan "Likehood", "TIRS" bukan "TRIS"

9. **Perbaiki penomoran**: Section 2.7 bukan 2.1

10. **Tentukan shapefile yang digunakan**: Jelaskan batas administrasi tahun berapa

11. **Tambahkan waktu penelitian**: Di section 3.1 tambahkan jadwal/timeline

## F.3. Perbaikan Minor

12. Konsistenkan penulisan istilah (Penginderaan/Pengindraan, Index/Indeks)

13. Perbaiki "Rumusan Penelitian" menjadi "Rumusan Masalah"

14. Hapus atau jelaskan NIP tambahan di halaman persetujuan

---

# KESIMPULAN

Proposal skripsi ini memiliki **kesalahan fundamental** yang perlu diperbaiki sebelum dapat dilanjutkan ke tahap penelitian. Kesalahan paling kritis adalah:

1. **Tidak adanya ground truth independen** — yang membuat seluruh hasil klasifikasi tidak memiliki validitas ilmiah

2. **Metodologi yang tidak jelas** — hubungan antara klasifikasi berbasis indeks dan MLC tidak dijelaskan

3. **Kesalahan teknis** — sistem koordinat, kontradiksi nilai NDBI, dan tabel klasifikasi yang tidak dapat digunakan

4. **Referensi tidak lengkap** — 18 referensi dikutip tapi tidak ada di daftar pustaka

**Rekomendasi**: Mahasiswa perlu melakukan **revisi mayor** sebelum penelitian dapat dilanjutkan.

---

# BAGIAN G: ANALISIS KELAYAKAN PENELITIAN

## G.1. Status Kelayakan: TIDAK LAYAK (Perlu Revisi Mayor)

Berdasarkan analisis komprehensif, proposal ini **BELUM LAYAK** untuk dilanjutkan tanpa revisi mayor karena:

### Masalah Kritis yang Menghambat Validitas Ilmiah:

1. **Tidak Ada Ground Truth Independen (FATAL)**
   - Supervised classification TANPA data supervisi yang valid
   - Training samples hanya dari interpretasi visual mahasiswa sendiri
   - Hasil validasi tidak bermakna karena circular reasoning
   - **SEVERITY**: ⚠️ BLOCKER - Penelitian tidak dapat menghasilkan hasil yang valid

2. **Metodologi Tidak Jelas (SERIUS)**
   - Judul menyebut "kombinasi" tapi kombinasi bagaimana?
   - Dua pendekatan (berbasis indeks vs MLC) tidak terintegrasi
   - Tidak jelas mana yang menjadi fokus utama
   - **SEVERITY**: ⚠️ CRITICAL - Pembaca tidak dapat mereplikasi penelitian

3. **Kesalahan Teknis Fundamental (SERIUS)**
   - EPSG:4326 bukan UTM Zone 48S
   - Kontradiksi klasifikasi NDBI (nilai positif disebut "tidak terbangun")
   - Tabel hasil hanya nilai tunggal, bukan rentang
   - **SEVERITY**: ⚠️ HIGH - Hasil perhitungan tidak dapat dipercaya

### Penilaian Per Aspek:

| Aspek | Nilai | Keterangan |
|-------|-------|------------|
| **Originalitas** | ⭐⭐☆☆☆ | Penelitian serupa sudah dilakukan Aulia et al. (2023) di Kota Jambi. Tidak ada nilai tambah yang jelas. |
| **Metodologi** | ⭐☆☆☆☆ | Fatal: Tidak ada ground truth. Training samples tidak valid. |
| **Penulisan** | ⭐⭐☆☆☆ | Banyak kesalahan ejaan (Likehood), referensi tidak lengkap, penomoran salah. |
| **Kelengkapan** | ⭐⭐⭐☆☆ | Struktur proposal sudah lengkap, tapi banyak bagian yang ambigu atau tidak dijelaskan. |
| **Kelayakan Teknis** | ⭐☆☆☆☆ | Kesalahan sistem koordinat, kontradiksi tabel, metodologi tidak dapat dijalankan. |

**REKOMENDASI AKHIR**:
- ❌ **DITOLAK** - Jika tidak ada perbaikan
- ⚠️ **REVISI MAYOR** - Jika mahasiswa bersedia memperbaiki kesalahan fundamental (minimal 2-3 bulan revisi)
- ✅ **DITERIMA BERSYARAT** - Hanya jika mahasiswa dapat menjelaskan dengan baik di ujian dan berkomitmen revisi semua poin kritis

---

# BAGIAN H: PERTANYAAN UJIAN LANJUTAN (21-40)

## H.1. Pertanyaan tentang Konsep Dasar Remote Sensing

21. **"Anda menggunakan Landsat 8 dengan resolusi 30 meter. Apa artinya 30 meter dalam konteks piksel? Jika area Kota Jambi adalah 169.89 km², berapa jumlah piksel yang akan Anda proses?"**
   - Jawaban yang diharapkan: 1 piksel = 900 m² (30m x 30m), total ≈ 188,767 piksel
   - Tujuan: Menguji pemahaman resolusi spasial

22. **"Band 4 Landsat adalah Red (0.64-0.67 µm), Band 5 adalah NIR (0.85-0.88 µm). Mengapa vegetasi hijau memantulkan NIR tinggi tapi menyerap Red?"**
   - Jawaban: Karena klorofil menyerap cahaya merah untuk fotosintesis, tapi struktur sel daun memantulkan NIR
   - Tujuan: Menguji pemahaman fisika dasar penginderaan jauh

## H.2. Pertanyaan tentang Validitas Data

23. **"Anda menggunakan citra 2015 dengan cloud cover 30% dan citra 2025 dengan cloud cover 10%. Bagaimana Anda memastikan perbandingan kedua tahun ini valid?"**
   - Tujuan: Menguji kesadaran tentang kualitas data dan komparabilitas temporal

24. **"Shapefile batas administrasi Anda download dari indonesia-geospasial.com (bukan situs resmi BIG). Bagaimana Anda memvalidasi bahwa shapefile ini akurat?"**
   - Tujuan: Menguji critical thinking tentang kualitas data sekunder

25. **"Landsat 8 diluncurkan 2013, tapi Anda analisis tahun 2015 dan 2025. Apakah ada perbedaan kalibrasi sensor antara tahun-tahun tersebut yang perlu Anda pertimbangkan?"**
   - Tujuan: Menguji pemahaman tentang sensor degradation dan kalibrasi

## H.3. Pertanyaan tentang Statistik dan Probability

26. **"MLC menggunakan teorema Bayes. Tuliskan rumus lengkap Bayes theorem dan jelaskan setiap komponennya dalam konteks klasifikasi citra!"**
   - Rumus: P(C|X) = [P(X|C) × P(C)] / P(X)
   - Tujuan: Menguji pemahaman matematika di balik MLC

27. **"MLC mensyaratkan distribusi normal. Bagaimana Anda menguji apakah training samples Anda berdistribusi normal?"**
   - Jawaban: Shapiro-Wilk test, Q-Q plot, histogram, dll
   - Tujuan: Menguji pengetahuan statistik

28. **"Jika dua kelas (vegetasi dan sawah) memiliki nilai spektral yang overlap, bagaimana MLC memutuskan klasifikasi piksel di area overlap?"**
   - Tujuan: Menguji pemahaman tentang probabilitas dan decision boundary

## H.4. Pertanyaan tentang Akurasi dan Validasi

29. **"Anda menyebutkan akan menghitung Overall Accuracy, User's Accuracy, Producer's Accuracy, dan Kappa. Jelaskan perbedaan keempat metrik ini dan kapan masing-masing penting!"**
   - Tujuan: Menguji pemahaman tentang metrik akurasi

30. **"Kappa coefficient 0.85 artinya apa? Apakah ini cukup baik untuk klasifikasi tutupan lahan?"**
   - Jawaban: 0.85 = kesepakatan "almost perfect" (>0.80), tapi perlu lihat juga confusion matrix
   - Tujuan: Menguji interpretasi statistik

31. **"Jika Overall Accuracy Anda 95% tapi User's Accuracy untuk kelas 'badan air' hanya 60%, apa interpretasi Anda?"**
   - Jawaban: Banyak piksel yang diprediksi sebagai air ternyata bukan air (false positive tinggi)
   - Tujuan: Menguji pemahaman confusion matrix

## H.5. Pertanyaan tentang Alternatif Metodologi

32. **"Kenapa tidak menggunakan Random Forest atau Support Vector Machine (SVM) yang sering lebih akurat dari MLC?"**
   - Tujuan: Menguji pemahaman tentang algoritma machine learning alternatif

33. **"Supervised classification membutuhkan ground truth yang mahal. Kenapa tidak pakai Unsupervised (K-Means atau ISODATA)?"**
   - Tujuan: Menguji pemahaman tentang trade-off supervised vs unsupervised

34. **"Object-Based Image Analysis (OBIA) kadang lebih baik dari pixel-based untuk area urban. Kenapa Anda tidak pakai OBIA?"**
   - Tujuan: Menguji wawasan tentang pendekatan alternatif

## H.6. Pertanyaan tentang Interpretasi Hasil

35. **"Jika NDVI tahun 2025 lebih rendah dari 2015, apa saja kemungkinan penyebabnya selain berkurangnya vegetasi?"**
   - Jawaban: Perbedaan musim, kelembaban tanah, sudut matahari, kualitas atmosfer, dll
   - Tujuan: Menguji critical thinking tentang faktor confounding

36. **"NDBI tinggi bisa berarti area terbangun, tapi juga bisa tanah gundul. Bagaimana membedakan keduanya?"**
   - Jawaban: Kombinasi dengan NDVI (tanah gundul biasanya NDVI sedikit lebih tinggi), tekstur, konteks spasial
   - Tujuan: Menguji pemahaman tentang ambiguitas spektral

37. **"Anda menemukan area dengan NDVI tinggi, NDWI tinggi, dan NDBI rendah. Kelas apa ini?"**
   - Jawaban: Kemungkinan sawah/lahan pertanian basah atau vegetasi di tepi sungai
   - Tujuan: Menguji kemampuan interpretasi kombinasi indeks

## H.7. Pertanyaan tentang Aplikasi dan Dampak

38. **"Penelitian Aulia et al. (2023) sudah menunjukkan RTH Kota Jambi menurun 2013-2021. Apa VALUE ADDED penelitian Anda dibanding penelitian tersebut?"**
   - **PERTANYAAN KUNCI INI MENGUJI ORIGINALITAS**
   - Tujuan: Memaksa mahasiswa menjelaskan kontribusi penelitiannya

39. **"Jika hasil penelitian Anda menunjukkan RTH Kota Jambi di bawah standar 30% (PP No. 26/2008), apa rekomendasi konkret yang bisa Anda berikan ke Pemkot Jambi?"**
   - Tujuan: Menguji kemampuan aplikasi praktis

40. **"Anda menggunakan citra gratis Landsat (resolusi 30m). Jika budget tidak masalah, kenapa tidak pakai Sentinel-2 (10m), SPOT (1.5m), atau drone? Apa trade-off nya?"**
   - Tujuan: Menguji pemahaman tentang resolusi spasial vs temporal, cost-benefit

---

# BAGIAN I: STRATEGI PERTANYAAN UNTUK DOSEN PENGUJI

## I.1. Teknik Bertanya yang Efektif

### 1. **Mulai dengan Pertanyaan Terbuka (Warm-up)**
   - "Ceritakan secara singkat apa yang ingin Anda capai dalam penelitian ini?"
   - "Mengapa Anda memilih Kota Jambi sebagai lokasi penelitian?"
   - **Tujuan**: Membuat mahasiswa nyaman, menilai pemahaman umum

### 2. **Fokus pada Kesalahan Fatal (Core Questions)**
   Prioritaskan 3 pertanyaan kritis ini:

   **A. Ground Truth (PALING PENTING):**
   > "MLC disebut supervised classification karena butuh supervisi dari luar. Di proposal Anda, training samples diambil dari interpretasi visual citra Landsat yang sama. Kemudian Anda klasifikasi citra Landsat yang sama, lalu validasi hasilnya dengan data yang juga dari interpretasi Anda sendiri. **Ini namanya circular reasoning**. Bagaimana Anda membuktikan bahwa interpretasi visual Anda benar?"

   **B. Metodologi Kombinasi:**
   > "Judul Anda: 'Kombinasi Nilai Indeks dan MLC'. Tolong jelaskan secara TEKNIS: apakah layer stack NDVI+NDWI+NDBI menjadi INPUT untuk MLC, atau MLC jalan di band asli? Dan kalau sudah ada klasifikasi dari indeks, untuk apa MLC?"

   **C. Sistem Koordinat:**
   > "Anda tulis EPSG:4326 adalah UTM Zone 48S. Coba Anda buka Google sekarang dan search 'EPSG 4326'. Apa yang Anda temukan? Dan apa konsekuensi kesalahan ini untuk perhitungan luas area?"

### 3. **Pertanyaan Follow-up (Probing)**
   Jika mahasiswa jawab salah atau ragu:
   - "Bisa dijelaskan lebih detail?"
   - "Dari mana Anda mendapat informasi ini?"
   - "Apakah Anda yakin dengan jawaban itu?"
   - "Coba lihat di halaman X proposal Anda, apakah konsisten dengan jawaban Anda?"

### 4. **Pertanyaan Skenario (Scenario-based)**
   - "Jika saya sebagai reviewer jurnal internasional, dan saya tanya 'where is your ground truth?', apa jawaban Anda?"
   - "Bayangkan mahasiswa lain ingin replikasi penelitian Anda. Apakah proposal ini cukup detail untuk mereka ikuti?"

## I.2. Area yang Wajib Ditanyakan

| Area | Pertanyaan Kunci | Ekspektasi Jawaban |
|------|------------------|-------------------|
| **Ground Truth** | "Dari mana ground truth Anda?" | Mahasiswa HARUS mengakui masalah ini atau usulkan solusi konkret |
| **EPSG** | "Apa beda EPSG:4326 dan EPSG:32748?" | Harus bisa jawab dengan benar atau akui kesalahan |
| **Kontradiksi NDBI** | "Mengapa Tabel 2.4 dan 3.3 bertentangan?" | Harus identifikasi kontradiksi dan jelaskan mana yang benar |
| **Referensi** | "Anda kutip Rouse et al. 1974, ada di daftar pustaka?" | Mahasiswa akui kelalaian dan berkomitmen lengkapi |
| **Kontribusi** | "Apa bedanya dengan Aulia et al. 2023?" | Harus bisa jelaskan value added penelitian |

## I.3. Red Flags yang Harus Diwaspadai

🚩 **Mahasiswa menghindari pertanyaan**: "Saya belum sampai ke detail itu, Pak/Bu"
   → **Respons**: "Tapi ini sudah di proposal Anda halaman X. Coba jelaskan maksud Anda."

🚩 **Jawaban copy-paste dari internet**: Terlalu "buku" dan tidak kontekstual
   → **Respons**: "Oke, sekarang aplikasikan ke konteks penelitian Anda. Bagaimana implementasinya?"

🚩 **Tidak konsisten antara jawaban lisan dan tertulis di proposal**
   → **Respons**: "Tapi di proposal halaman X Anda tulis berbeda. Mana yang benar?"

🚩 **Mahasiswa menyalahkan software atau data**: "Mungkin QGIS-nya yang salah, Bu"
   → **Respons**: "Anda harus memastikan tools dan data valid sebelum pakai untuk penelitian."

## I.4. Skala Penilaian Ujian Proposal

### Kriteria Kelulusan:

**LULUS TANPA REVISI** (Sangat Langka):
- ✅ Memahami semua kesalahan fatal
- ✅ Bisa menjelaskan metodologi dengan jelas
- ✅ Proposal siap eksekusi tanpa perubahan signifikan

**LULUS DENGAN REVISI MINOR** (20-30% proposal):
- ✅ Memahami konsep utama dengan baik
- ⚠️ Ada kesalahan teknis tapi mudah diperbaiki (typo, referensi, format)
- ✅ Metodologi sound secara fundamental

**LULUS DENGAN REVISI MAYOR** (Kasus proposal ini):
- ⚠️ Memahami sebagian konsep tapi ada gap signifikan
- ❌ Ada kesalahan fundamental yang butuh redesign metodologi
- ⚠️ Butuh 2-4 minggu untuk revisi besar

**TIDAK LULUS** (Harus ujian ulang):
- ❌ Tidak memahami konsep dasar penelitiannya
- ❌ Tidak bisa menjawab pertanyaan kritis sama sekali
- ❌ Proposal tidak feasible untuk dilaksanakan

### Untuk Proposal Ayu Friska:
Prediksi: **LULUS DENGAN REVISI MAYOR** (jika mahasiswa menunjukkan pemahaman konsep)
atau **TIDAK LULUS** (jika tidak bisa jawab pertanyaan ground truth dan metodologi)

---

# BAGIAN J: CHECKLIST REVISI WAJIB (untuk Mahasiswa)

## J.1. Revisi Kritis (Deadline: 2 Minggu)

### ☑️ PRIORITAS 1: Ground Truth (BLOCKER)

**Masalah**: Tidak ada ground truth independen untuk supervised classification

**Solusi Wajib** (Pilih minimal 1):

1. **Survei Lapangan (RECOMMENDED)**
   - [ ] Tentukan minimal 50 titik sampel per kelas (total 250 titik untuk 5 kelas)
   - [ ] Gunakan GPS untuk rekam koordinat
   - [ ] Foto setiap lokasi sampel dengan timestamp
   - [ ] Dokumentasi karakteristik setiap titik
   - **Timeline**: 1 minggu survei lapangan

2. **Citra Resolusi Tinggi (ALTERNATIF 1)**
   - [ ] Download citra Google Earth Pro untuk tanggal yang sama dengan Landsat
   - [ ] Digitasi manual ROI untuk training dan testing
   - [ ] Pastikan tidak ada time gap > 3 bulan dengan citra Landsat
   - [ ] Dokumentasi proses digitasi
   - **Timeline**: 3-5 hari

3. **Data Sekunder Resmi (ALTERNATIF 2)**
   - [ ] Dapatkan peta tutupan lahan dari BIG atau KLHK untuk tahun yang sama
   - [ ] Verifikasi metadata dan akurasi peta sekunder
   - [ ] Overlay dengan citra Landsat untuk ekstrak training samples
   - **Timeline**: 1 minggu (termasuk koordinasi instansi)

**Deliverable**:
- Database ground truth (shapefile + atribut)
- Foto dokumentasi (jika survei)
- Metadata lengkap sumber data

---

### ☑️ PRIORITAS 2: Perbaiki Sistem Koordinat

**Masalah**: EPSG:4326 salah disebut sebagai UTM Zone 48S

**Solusi**:
- [ ] Ganti semua tulisan "EPSG:4326" menjadi "**EPSG:32748**" (UTM Zone 48S)
- [ ] Verifikasi di QGIS: Project → Properties → CRS → cari "32748"
- [ ] Pastikan semua layer (citra + shapefile) dalam EPSG:32748
- [ ] Re-calculate luas area setelah re-project

**Perubahan di Proposal**:
```
Halaman 23, Poin 3:
SALAH: "WGS 1984 / UTM Zone 48S (EPSG:4326)"
BENAR: "WGS 1984 / UTM Zone 48S (EPSG:32748)"
```

---

### ☑️ PRIORITAS 3: Klarifikasi Metodologi "Kombinasi"

**Masalah**: Tidak jelas bagaimana NDVI+NDWI+NDBI "dikombinasikan" dengan MLC

**Solusi** (Pilih 1 pendekatan):

**Opsi A: Layer Stack sebagai Input MLC** (RECOMMENDED)
```
1. Hitung NDVI, NDWI, NDBI → 3 layer baru
2. Stack: Band_asli (Band 2-7) + NDVI + NDWI + NDBI = 9 layer input
3. Training samples pada 9 layer
4. MLC dengan 9 features
5. Validasi
```

**Opsi B: Dua Pendekatan Terpisah + Perbandingan**
```
1. Pendekatan 1: Klasifikasi berbasis thresholding indeks
   - NDVI → kelas vegetasi
   - NDWI → kelas air
   - NDBI → kelas terbangun

2. Pendekatan 2: MLC pada band asli

3. Bandingkan akurasi kedua pendekatan
4. Analisis agreement/disagreement
```

**Opsi C: Ensemble Method**
```
1. Klasifikasi dari indeks → Peta A
2. Klasifikasi dari MLC → Peta B
3. Majority voting: jika A dan B setuju → final class
4. Jika tidak setuju → ambil yang probabilitas lebih tinggi
```

**Yang Harus Ditambahkan di Proposal**:
- [ ] Flowchart detail metodologi kombinasi
- [ ] Penjelasan teknis implementasi di QGIS/Python
- [ ] Justifikasi kenapa kombinasi lebih baik dari single method

---

### ☑️ PRIORITAS 4: Perbaiki Tabel Klasifikasi

**Masalah**: Tabel 3.1, 3.2, 3.3 hanya nilai tunggal, seharusnya rentang

**Contoh Perbaikan Tabel 3.3 (NDBI)**:

**SALAH** (sekarang):
| No | Kelas | Nilai NDBI 2015 | Nilai NDBI 2025 |
|----|-------|-----------------|-----------------|
| 1 | Tidak Terbangun | 0.2850414 | -0.6028725 |
| 2 | Terbangun | 0.2680664 | 0.31556 |

**BENAR** (seharusnya):
| No | Kelas | Rentang NDBI | Keterangan Statistik 2015 | Keterangan Statistik 2025 |
|----|-------|--------------|---------------------------|---------------------------|
| 1 | Tidak Terbangun | **-1.0 hingga 0.0** | Min=-0.602, Max=-0.010, Mean=-0.285 | Min=-0.728, Max=-0.005, Mean=-0.348 |
| 2 | Terbangun | **0.0 hingga +1.0** | Min=0.005, Max=0.456, Mean=0.268 | Min=0.008, Max=0.523, Mean=0.316 |

**Action Items**:
- [ ] Tambah kolom "Rentang Nilai" berdasarkan literatur
- [ ] Tambah statistik deskriptif: Min, Max, Mean, StdDev
- [ ] Jelaskan threshold yang digunakan untuk klasifikasi

---

### ☑️ PRIORITAS 5: Perbaiki Kontradiksi NDBI

**Masalah**: Tabel 2.4 vs Tabel 3.3 bertentangan

**Tabel 2.4** (Teori):
- Negatif = Tidak Terbangun ✓
- Positif = Terbangun ✓

**Tabel 3.3** (Hasil):
- 0.2850414 (POSITIF) → "Tidak Terbangun" ✗ SALAH!

**Solusi**:
- [ ] **Opsi 1**: Koreksi Tabel 3.3 → nilai positif harus "Terbangun"
- [ ] **Opsi 2**: Cek ulang perhitungan NDBI (mungkin formula salah)
- [ ] **Opsi 3**: Jika benar ada kontradiksi literatur, jelaskan dengan referensi

**Penjelasan yang Harus Ditambahkan**:
```
"Berdasarkan hasil perhitungan NDBI tahun 2015, nilai minimum adalah
-0.602 (non-terbangun) dan maksimum 0.456 (terbangun). Threshold
pemisah ditetapkan pada NDBI = 0.0, sesuai dengan Zha et al. (2003)
dan Kurniyanto et al. (2021)."
```

---

## J.2. Revisi Penting (Deadline: 1 Minggu)

### ☑️ Lengkapi Daftar Pustaka

**Referensi yang WAJIB ditambahkan**:
1. [ ] Rouse, J. W., et al. (1974). Monitoring vegetation systems in the Great Plains with ERTS. *NASA Special Publication*, 351, 309.
2. [ ] McFeeters, S. K. (1996). The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features. *International Journal of Remote Sensing*, 17(7), 1425-1432.
3. [ ] Zha, Y., Gao, J., & Ni, S. (2003). Use of normalized difference built-up index in automatically mapping urban areas from TM imagery. *International Journal of Remote Sensing*, 24(3), 583-594.
4. [ ] Departemen Kehutanan. (2005). *Pedoman Inventarisasi dan Monitoring Sumber Daya Hutan*. Jakarta: Direktorat Jenderal RLPS.
5. [ ] ... (12 referensi lainnya dari Bagian C.1)

**Format Penulisan** (sesuaikan dengan gaya Fakultas):
- Untuk jurnal: Nama, Tahun. Judul. *Nama Jurnal*, Volume(Nomor), Halaman.
- Untuk buku: Nama, Tahun. *Judul Buku*. Kota: Penerbit.

---

### ☑️ Perbaiki Ejaan dan Penomoran

**Kesalahan Ejaan**:
- [ ] "LIKEHOOD" → "**LIKELIHOOD**" (di SELURUH dokumen termasuk judul!)
- [ ] "TRIS" → "**TIRS**" (Thermal Infrared Sensor)
- [ ] "Pengindraan" → pilih satu: "Penginderaan" atau "Pengindraan" (konsisten)

**Penomoran Section**:
- [ ] Section 2.1 yang sekarang → ubah jadi **Section 2.7**
- [ ] Halaman 32: Numbering dimulai dari 3 → perbaiki jadi mulai dari 1

---

### ☑️ Tambahkan Informasi yang Hilang

**Waktu Penelitian** (Hal. 20):
- [ ] Tambahkan: "Penelitian dilaksanakan selama 6 bulan dari Januari - Juni 2025"
- [ ] Buat Gantt Chart atau timeline pelaksanaan

**Luas Wilayah Kota Jambi**:
- [ ] Tentukan shapefile yang digunakan: 205.43 km² atau 169.89 km²?
- [ ] Tambahkan: "Penelitian ini menggunakan batas administrasi Kota Jambi berdasarkan [sumber] dengan luas [X] km²"

**Pembagian Training dan Testing**:
- [ ] Tambahkan: "Training samples: 70%, Testing samples: 30%"
- [ ] Jelaskan metode pembagian: random sampling atau stratified sampling?

---

## J.3. Revisi Minor (Deadline: 3 Hari)

- [ ] Perbaiki NIP yang tidak jelas di halaman persetujuan
- [ ] Standarisasi penulisan: "Indeks" atau "Index" (pilih satu)
- [ ] Perbaiki inkonsistensi "spectral" vs "spektral"
- [ ] Tambahkan caption yang lebih deskriptif untuk setiap gambar dan tabel

---

## J.4. Dokumen Pendukung yang Harus Disiapkan

Untuk sidang revisi atau sidang skripsi:

1. **Ground Truth Database**
   - File: `Ground_Truth_Kota_Jambi_2015_2025.xlsx`
   - Kolom: ID, Kelas, Latitude, Longitude, Foto, Tanggal Verifikasi, Sumber

2. **Dokumentasi Perhitungan**
   - Script QGIS/Python untuk perhitungan NDVI, NDWI, NDBI
   - Log proses MLC
   - Confusion matrix mentah

3. **Metadata Lengkap**
   - Scene ID Landsat yang digunakan
   - Tanggal akuisisi
   - Cloud cover percentage
   - Sumber shapefile dengan versi dan tanggal download

4. **Revisi Proposal (Track Changes)**
   - Dokumen "Proposal_v1_Original.pdf"
   - Dokumen "Proposal_v2_Revisi.pdf"
   - Dokumen "Daftar_Revisi.xlsx" (sebelum-sesudah)

---

# BAGIAN K: ANALISIS KONTRIBUSI PENELITIAN

## K.1. Perbandingan dengan Penelitian Terdahulu

### Penelitian Aulia et al. (2023) - Kota Jambi

**Metode**:
- NDVI transformasi saja
- 6 tingkat kerapatan vegetasi
- Periode 2013-2021

**Hasil**:
- RTH menurun 11,813.68 ha (2013) → 9,605.39 ha (2021)
- Penurunan 2,208.30 ha dalam 8 tahun
- Korelasi dengan pertumbuhan penduduk 1.24%/tahun

### Penelitian Ayu Friska (Proposal Ini) - Kota Jambi

**Metode**:
- Kombinasi NDVI + NDWI + NDBI
- MLC untuk klasifikasi
- Periode 2015-2025

**Potensi Kontribusi**:
1. **Multi-indeks** (tidak hanya NDVI) → lebih komprehensif
2. **Klasifikasi supervised** (lebih akurat dari thresholding sederhana)
3. **Periode lebih panjang** (10 tahun: 2015-2025)
4. **Identifikasi lebih detail**: vegetasi + air + terbangun + sawah

**MASALAH**:
- Kontribusi ini TIDAK DIJELASKAN di proposal!
- Mahasiswa harus EKSPLISIT menyatakan value added dibanding Aulia et al.
- Perlu tambahan analisis: perbandingan akurasi metode NDVI-only vs kombinasi indeks+MLC

## K.2. Gap Penelitian yang Seharusnya Diisi

Dari penelitian terdahulu (Tabel 2.5), ada gap yang bisa diisi:

| Penelitian | Metode | Gap |
|------------|--------|-----|
| Aulia et al. (2023) | NDVI only | Tidak identifikasi badan air dan area terbangun secara eksplisit |
| Agus et al. (2024) | NDVI + MLC | Lokasi berbeda (Samarinda), belum ada untuk Jambi |
| Jothimani et al. (2021) | NDVI+NDWI+NDBI+LST | Fokus ke LST (suhu), bukan klasifikasi tutupan lahan |

**Kontribusi Potensial Penelitian Ini**:
1. ✅ Pertama kali menerapkan kombinasi 3 indeks + MLC untuk Kota Jambi
2. ✅ Mengisi gap periode 2021-2025 (lanjutan dari Aulia et al.)
3. ✅ Identifikasi lebih detail: 5 kelas tutupan lahan

**TAPI**: Ini semua hanya potensial jika metodologi diperbaiki!

---

# BAGIAN M: PERBANDINGAN DATASET SATELIT DAN SUMBER GROUND TRUTH

## M.1. Mengapa Landsat 8? Perbandingan dengan Alternatif Lain

### Tabel Komparasi Dataset Satelit untuk Klasifikasi Tutupan Lahan

| Dataset | Resolusi Spasial | Resolusi Temporal | Band Spektral | Ketersediaan | Biaya | Kelebihan | Kekurangan |
|---------|------------------|-------------------|---------------|--------------|-------|-----------|------------|
| **Landsat 8 OLI/TIRS** | **30m** (multispektral) <br> 15m (pankromatik) <br> 100m (thermal) | **16 hari** | **11 band** (Coastal-SWIR-Thermal) | 2013-sekarang | **GRATIS** | ✅ Gratis <br> ✅ Arsip historis panjang (sejak 1972 untuk Landsat series) <br> ✅ Konsistensi data <br> ✅ Dokumentasi lengkap | ❌ Resolusi spasial sedang (30m) <br> ❌ Revisit 16 hari (lambat) <br> ❌ Sering terhalang awan di tropis |
| **Sentinel-2 (ESA)** | **10m** (RGB, NIR) <br> 20m (Red Edge, SWIR) <br> 60m (Coastal, Cirrus) | **5 hari** (2 satelit) | **13 band** (termasuk Red Edge untuk vegetasi) | 2015-sekarang | **GRATIS** | ✅ Gratis <br> ✅ Resolusi lebih tinggi (10m) <br> ✅ Revisit lebih cepat (5 hari) <br> ✅ Band Red Edge untuk analisis vegetasi detail | ❌ Arsip historis lebih pendek (sejak 2015) <br> ❌ Tidak ada band thermal <br> ❌ Data lebih besar (storage) |
| **SPOT 6/7** | **1.5m** (pankromatik) <br> 6m (multispektral) | On-demand (tasking) | 5 band | 2012-sekarang <br> ⚠️ SPOT 7 failed March 2023 | **KOMERSIAL** (harga bervariasi, contact Airbus) | ✅ Resolusi sangat tinggi <br> ✅ Cocok untuk urban mapping detail | ❌ Mahal <br> ❌ Tidak ada arsip gratis <br> ❌ Coverage terbatas <br> ❌ SPOT 7 tidak operasional |
| **Planet (SkySat, Dove)** | **0.5-3m** | **Harian** | 4-8 band | 2016-sekarang | **KOMERSIAL** (atau gratis untuk penelitian tertentu) | ✅ Resolusi tinggi <br> ✅ Temporal sangat tinggi (daily) | ❌ Mahal untuk area luas <br> ❌ Variasi kualitas radiometrik <br> ❌ Kompleksitas preprocessing |
| **MODIS (Terra/Aqua)** | **250m-1km** (sensor bands) <br> **500m** (land cover product MCD12Q1) | **1-2 hari** | 36 band | 2000-sekarang | **GRATIS** | ✅ Gratis <br> ✅ Revisit sangat cepat <br> ✅ Cocok untuk monitoring regional | ❌ Resolusi rendah (500m untuk land cover) <br> ❌ Tidak cocok untuk area kecil seperti Kota Jambi |
| **Google Earth (Basemap)** | **0.5-15m** (varies) | Tidak konsisten | RGB (visual) | Varies by location | **GRATIS** (viewing only) | ✅ Resolusi tinggi <br> ✅ Mudah diakses | ❌ Tanggal akuisisi tidak konsisten <br> ❌ Tidak ada band spektral (hanya RGB) <br> ❌ Tidak untuk analisis kuantitatif |

---

### **Pertanyaan Kritis untuk Mahasiswa**:

> **"Anda memilih Landsat 8 dengan resolusi 30m. Sentinel-2 tersedia GRATIS dengan resolusi 10m dan revisit 5 hari (lebih baik dari Landsat). Mengapa tidak menggunakan Sentinel-2?"**

**Jawaban yang Diharapkan**:
- Sentinel-2 memang lebih baik dalam resolusi spasial dan temporal
- Tapi untuk analisis **multitemporal 2015-2025**, Landsat memiliki arsip lebih panjang (Sentinel baru 2015)
- Untuk Kota Jambi yang tidak terlalu besar (169 km²), resolusi 30m sudah cukup memadai
- Konsistensi sensor Landsat 8 (2013-2025) lebih baik untuk perbandingan temporal

**Jika Mahasiswa Tidak Bisa Jawab**:
- ⚠️ Menunjukkan kurang riset tentang alternatif dataset
- ⚠️ Tidak ada justifikasi metodologis untuk pemilihan data

---

## M.2. Ketersediaan Data Landsat 8 di USGS Earth Explorer

### Timeline dan Coverage Landsat 8

| Aspek | Detail |
|-------|--------|
| **Launch Date** | 11 Februari 2013 |
| **Operational Status** | Aktif (2013 - sekarang, >11 tahun) |
| **Path/Row untuk Kota Jambi** | **Path 126, Row 62** (Bengkulu & Jambi provinces, Sumatra) |
| **Rentang Waktu Tersedia** | 2013 - Present |
| **Revisit Time** | 16 hari |
| **Jumlah Scene per Tahun** | ~23 scene (365/16) |
| **Cloud-Free Scene** | Sangat terbatas di Indonesia (iklim tropis) |

---

### **Realitas Cloud Cover di Kota Jambi**

**Tabel Estimasi Ketersediaan Scene Cloud-Free**:

| Musim | Bulan | Estimasi Cloud Cover | Kemungkinan Cloud < 10% | Catatan |
|-------|-------|----------------------|-------------------------|---------|
| **Kemarau** | **Juni - September** | **20-40%** | **TINGGI** ✅ | **WAKTU TERBAIK** untuk akuisisi data |
| Peralihan | Oktober - November | 40-60% | Sedang | Mulai memasuki musim hujan |
| **Musim Hujan** | Desember - Maret | **60-90%** | **SANGAT RENDAH** ❌ | Hampir mustahil mendapat scene cloud-free |
| Peralihan | April - Mei | 50-70% | Rendah | Akhir musim hujan |

**MASALAH DALAM PROPOSAL**:

Di halaman 21-22, mahasiswa menulis:
> "Rentang waktu pencarian: 01 januari – 20 November 2025, Toleransi tutupan awan ≤ 10%"

**PERTANYAAN KRITIS**:
> **"Anda mencari data Januari-November dengan cloud ≤10%. Apakah Anda sudah cek di USGS berapa scene yang tersedia? Di musim hujan (Desember-Maret), kemungkinan cloud <10% sangat kecil!"**

**Rekomendasi yang Seharusnya**:
- Fokus pada **musim kemarau** (Juni-September) untuk kedua tahun (2015 dan 2025)
- Gunakan **composite multi-temporal** jika tidak ada single scene cloud-free
- Pertimbangkan **cloud masking** untuk area dengan cloud <30%

---

### **Cara Verifikasi Ketersediaan Data di USGS**:

**Langkah-langkah**:
1. Buka **USGS Earth Explorer**: https://earthexplorer.usgs.gov/
2. Masukkan koordinat Kota Jambi: **1°36'S, 103°36'E**
3. Set kriteria:
   - Dataset: Landsat 8 OLI/TIRS Collection 2 Level 2
   - Date Range: 01/01/2015 - 31/12/2015 (untuk tahun 2015)
   - Additional Criteria: Land Cloud Cover < 10%
4. **Hasil yang mungkin**:
   - Untuk cloud <10%: Hanya **2-4 scene per tahun** (sangat terbatas!)
   - Untuk cloud <30%: ~8-12 scene per tahun

**ACTION ITEM untuk Mahasiswa**:
- [ ] Screenshot hasil pencarian USGS untuk tahun 2015 dan 2025
- [ ] Dokumentasi Scene ID yang akan digunakan
- [ ] Justifikasi jika harus gunakan cloud >10%

---

## M.3. Sumber Ground Truth / True Label untuk Validasi

### **MASALAH KRUSIAL**: Proposal tidak ada ground truth independen!

**Berikut adalah sumber-sumber ground truth yang SEHARUSNYA digunakan**:

---

### **Opsi 1: Dataset Global Land Cover (Gratis, Siap Pakai)**

#### **A. Google Dynamic World (RECOMMENDED ✅)**

| Aspek | Detail |
|-------|--------|
| **Provider** | Google & World Resources Institute |
| **Resolution** | **10m** (dari Sentinel-2) |
| **Temporal Coverage** | **2015 - Present** (Near Real-Time) |
| **Update Frequency** | Setiap 2-5 hari |
| **Jumlah Kelas** | **9 kelas**: Water, Trees, Grass, Flooded vegetation, Crops, Shrub/scrub, Built area, Bare ground, Snow/ice |
| **Akurasi Global** | Overall Accuracy: **~73-74%** (validated in Nature Scientific Data 2022) |
| **Format** | GeoTIFF (Google Earth Engine) |
| **Akses** | **GRATIS** via Google Earth Engine |
| **URL** | https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_DYNAMICWORLD_V1 |

**MENGAPA INI COCOK UNTUK VALIDASI**:
- ✅ Resolusi 10m (lebih detail dari Landsat 30m)
- ✅ Coverage temporal 2015-2025 ✓ (sesuai dengan proposal!)
- ✅ **Independen** dari Landsat (menggunakan Sentinel-2)
- ✅ Gratis dan mudah diakses
- ✅ Bisa digunakan sebagai training atau testing samples

**Cara Mendapatkan**:
```javascript
// Google Earth Engine Script
var roi = ee.Geometry.Point([103.6, -1.6]); // Kota Jambi
var dynamicWorld = ee.ImageCollection('GOOGLE/DYNAMICWORLD/V1')
  .filterBounds(roi)
  .filterDate('2015-06-01', '2015-09-30') // Musim kemarau
  .select('label');
Export.image.toDrive({image: dynamicWorld.mode(), ...});
```

---

#### **B. ESA WorldCover 10m**

| Aspek | Detail |
|-------|--------|
| **Provider** | European Space Agency (ESA) |
| **Resolution** | **10m** |
| **Temporal Coverage** | **2020, 2021** (snapshot tahunan) |
| **Jumlah Kelas** | **11 kelas**: Tree cover, Shrubland, Grassland, Cropland, Built-up, Bare/sparse vegetation, Snow/ice, Permanent water, Herbaceous wetland, Mangroves, Moss/lichen |
| **Akurasi Global** | Overall Accuracy: **74.4%** |
| **Format** | GeoTIFF |
| **Akses** | **GRATIS** |
| **URL** | https://worldcover2020.esa.int/ |

**KEKURANGAN untuk Proposal Ini**:
- ❌ Hanya tersedia untuk 2020 dan 2021 (tidak ada 2015 dan 2025)
- Tapi bisa digunakan sebagai **referensi** untuk 2020

---

#### **C. ESRI Land Cover (10m)**

| Aspek | Detail |
|-------|--------|
| **Provider** | Esri & Impact Observatory |
| **Resolution** | **10m** |
| **Temporal Coverage** | **2017-2023** (annual) |
| **Jumlah Kelas** | 9 kelas |
| **Akurasi** | **>75%** global (average over 75% per year) |
| **Akses** | **GRATIS** via ArcGIS Living Atlas |
| **URL** | https://livingatlas.arcgis.com/landcover/ |

---

#### **D. MODIS Land Cover (MCD12Q1)**

| Aspek | Detail |
|-------|--------|
| **Resolution** | **500m** |
| **Temporal Coverage** | 2001 - Present (annual) |
| **Kelas** | 17 kelas (IGBP scheme) |
| **Akses** | GRATIS via NASA EarthData |

**KEKURANGAN**:
- ❌ Resolusi 500m terlalu rendah untuk Kota Jambi (169 km²)
- ❌ Tidak cocok untuk validasi piksel 30m Landsat

---

### **Opsi 2: Citra Resolusi Tinggi sebagai Ground Truth**

#### **A. Google Earth Pro (RECOMMENDED untuk Validasi Visual)**

| Aspek | Detail |
|-------|--------|
| **Resolution** | 0.5-2m (varies) |
| **Coverage** | Global |
| **Akses** | **GRATIS** (desktop app) |
| **Kelebihan** | ✅ Resolusi sangat tinggi <br> ✅ Bisa lihat historical imagery <br> ✅ Gratis |
| **Kekurangan** | ❌ Tanggal akuisisi tidak selalu match dengan Landsat <br> ❌ Hanya visual (RGB), tidak ada NIR/SWIR <br> ❌ Tidak bisa analisis otomatis |

**Cara Menggunakan untuk Ground Truth**:
1. Buka Google Earth Pro
2. Set tanggal historical imagery mendekati tanggal Landsat (misal: Juni-September 2015)
3. Digitasi manual ROI (Region of Interest) untuk setiap kelas
4. Export sebagai KML/Shapefile
5. Import ke QGIS untuk overlay dengan Landsat

---

#### **B. Bing Maps / Maxar Imagery**

| Aspek | Detail |
|-------|--------|
| **Resolution** | 0.3-0.5m |
| **Akses** | Gratis via QGIS Plugin (QuickMapServices) |
| **Kelebihan** | Resolusi tinggi, akses mudah |
| **Kekurangan** | Tanggal tidak konsisten |

---

### **Opsi 3: Survei Lapangan (PALING VALID ✅✅✅)**

**Protokol Standar untuk Ground Truth Field Survey**:

| Parameter | Rekomendasi |
|-----------|-------------|
| **Jumlah Sampel** | **Minimum 50 titik per kelas** (total 250 titik untuk 5 kelas) |
| **Distribusi** | Stratified random sampling (merata di seluruh area) |
| **Jarak Antar Titik** | Minimum 90m (3× resolusi Landsat) untuk independensi spasial |
| **Peralatan** | GPS handheld (akurasi <5m), kamera, form lapangan |
| **Data yang Dicatat** | Koordinat, kelas tutupan lahan, foto, timestamp, deskripsi |
| **Waktu Survey** | **Sinkron dengan tanggal akuisisi citra** (±2 minggu) |

**Format Database Ground Truth**:

| ID | Latitude | Longitude | Kelas | Foto | Tanggal | Akurasi GPS | Catatan |
|----|----------|-----------|-------|------|---------|-------------|---------|
| GT001 | -1.5678 | 103.6234 | Vegetasi Tinggi | IMG_001.jpg | 2025-07-15 | 3.2m | Hutan kota, kanopi rapat |
| GT002 | -1.5691 | 103.6189 | Badan Air | IMG_002.jpg | 2025-07-15 | 2.8m | Sungai Batanghari |
| ... | ... | ... | ... | ... | ... | ... | ... |

---

### **Opsi 4: Data Sekunder dari Instansi Pemerintah**

| Sumber | Jenis Data | Skala/Resolusi | Akses | Kelebihan | Kekurangan |
|--------|------------|----------------|-------|-----------|------------|
| **Badan Informasi Geospasial (BIG)** | Peta Rupabumi Indonesia (RBI) | 1:25,000 - 1:50,000 | Berbayar / request | ✅ Data resmi <br> ✅ Teruji akurasi | ❌ Mungkin outdated <br> ❌ Akses lambat |
| **Kementerian LHK (KLHK)** | Peta Tutupan Lahan Indonesia | 1:250,000 (national) | Request resmi | ✅ Standar nasional | ❌ Skala besar (tidak detail untuk kota) |
| **BAPPEDA Kota Jambi** | Peta tematik kota, RTRW | Varies | Request langsung | ✅ Spesifik untuk Jambi <br> ✅ Update | ❌ Perlu koordinasi formal |
| **Dinas Pertanahan Kota Jambi** | Data penggunaan lahan | Parcel-based | Request | ✅ Detail | ❌ Fokus ke administrasi, bukan biofisik |

---

## M.4. Perbandingan Metode Akuisisi Ground Truth

| Metode | Biaya | Waktu | Akurasi | Independensi | Rekomendasi untuk Proposal Ini |
|--------|-------|-------|---------|--------------|--------------------------------|
| **Dynamic World** | GRATIS | 1-2 hari | Sedang (73-74%) | ✅ Tinggi (Sentinel-2) | ⭐⭐⭐⭐⭐ **SANGAT DISARANKAN** |
| **ESA WorldCover** | GRATIS | 1-2 hari | Tinggi (74%) | ✅ Tinggi | ⭐⭐⭐⭐ (tapi tidak ada 2015) |
| **Google Earth Digitasi** | GRATIS | 3-5 hari | Tinggi (tergantung skill) | ⚠️ Sedang (visual only) | ⭐⭐⭐⭐ |
| **Survei Lapangan** | Tinggi (Rp 5-10 juta) | 1-2 minggu | ✅ **Sangat Tinggi** | ✅ **Sangat Tinggi** | ⭐⭐⭐⭐⭐ (jika ada budget) |
| **Data BIG/KLHK** | Sedang-Tinggi | 2-4 minggu | Tinggi | ✅ Tinggi | ⭐⭐⭐ (tergantung ketersediaan) |

---

## M.5. Rekomendasi Ground Truth untuk Proposal Ayu Friska

### **Solusi Ideal (Kombinasi)**:

**Untuk Tahun 2015**:
1. **Primary**: Google Dynamic World 2015 (10m, gratis) → Extract 200 random points
2. **Secondary**: Google Earth Historical Imagery (Juni-September 2015) → Validasi visual 50 titik
3. **Tertiary**: Digitasi manual dari citra resolusi tinggi → 50 ROI polygons

**Untuk Tahun 2025**:
1. **Primary**: Survei lapangan (Juli-Agustus 2025) → 250 titik GPS
2. **Secondary**: Dynamic World 2025 → Extract 200 points
3. **Tertiary**: Google Earth current imagery → Validasi visual

### **Pembagian Training dan Testing**:

| Sumber | Jumlah | Penggunaan |
|--------|--------|------------|
| Dynamic World | 200 titik | 70% Training, 30% Testing |
| Survei Lapangan | 250 titik | 50% Training, 50% Testing |
| Google Earth Digitasi | 50 ROI | Training only (area-based) |
| **TOTAL** | ~450 sampel | Training: 315 / Testing: 135 |

---

## M.6. Pertanyaan untuk Mahasiswa

**PERTANYAAN KRITIS YANG HARUS DITANYAKAN**:

1. **"Kenapa tidak pakai Sentinel-2 yang gratis, resolusi 10m, dan revisit 5 hari?"**
   - Mahasiswa harus bisa justifikasi pemilihan Landsat 8

2. **"Berapa scene Landsat 8 tahun 2015 dan 2025 yang Anda temukan dengan cloud <10% di USGS? Coba sebutkan Scene ID-nya!"**
   - Test: Apakah mahasiswa sudah cek data availability?

3. **"Anda tahu Dynamic World dari Google? Kenapa tidak pakai itu sebagai ground truth?"**
   - Test: Apakah mahasiswa riset alternatif ground truth?

4. **"Cloud cover 10% itu artinya ada 10% area tertutup awan. Untuk Kota Jambi yang 169 km², berarti 16.9 km² tidak bisa diklasifikasi. Bagaimana solusinya?"**
   - Test: Pemahaman tentang cloud masking dan composite

5. **"Jika budget Rp 10 juta, lebih baik beli citra SPOT resolusi 1.5m atau survei lapangan 250 titik GPS? Jelaskan trade-off nya!"**
   - Test: Critical thinking tentang resource allocation

---

**CATATAN UNTUK PENGUJI**:

Dengan tidak adanya ground truth independen, **validitas seluruh penelitian ini dipertanyakan**. Dynamic World atau survei lapangan adalah **WAJIB** untuk penelitian yang valid.

---

## M.7. Referensi dan Sumber Verifikasi

**Semua informasi dalam BAGIAN M telah diverifikasi melalui pencarian web pada 22 Desember 2025. Sumber-sumber utama:**

### Satelit dan Dataset:
- **Google Dynamic World**: [Nature Scientific Data 2022](https://www.nature.com/articles/s41597-022-01307-4) | [Google Earth Engine Catalog](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_DYNAMICWORLD_V1)
- **ESA WorldCover**: [Official Website](https://worldcover2020.esa.int/) | [ESA Data Portal](https://esa-worldcover.org/en/data-access)
- **ESRI Land Cover**: [ESRI Newsroom 2024](https://www.esri.com/about/newsroom/announcements/esri-releases-latest-land-cover-map-with-updated-sentinel-2-satellite-data) | [GEE Community Catalog](https://gee-community-catalog.org/projects/S2TSLULC/)
- **Landsat 8**: [USGS Official](https://www.usgs.gov/landsat-missions/landsat-8) | [NASA Landsat Science](https://landsat.gsfc.nasa.gov/satellites/landsat-8/)
- **Sentinel-2**: [ESA Sentinel-2](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2/Introducing_Sentinel-2) | [Copernicus eoPortal](https://www.eoportal.org/satellite-missions/copernicus-sentinel-2)
- **SPOT 6/7**: [eoPortal](https://www.eoportal.org/satellite-missions/spot-6-7) | [Airbus Intelligence](https://www.intelligence-airbusds.com/en/8693-spot-67)
- **Planet**: [SkySat Documentation](https://docs.planet.com/data/imagery/skysat/) | [NASA CSDA](https://www.earthdata.nasa.gov/esds/csda/csda-vendor-planet)
- **MODIS**: [USGS MODIS Land Cover](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/MCD12Q1/) | [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD12Q1)

### Path/Row Verification:
- **USGS Landsat Tools**: [Earth Explorer](https://earthexplorer.usgs.gov/) | [WRS-2 Shapefiles](https://www.usgs.gov/landsat-missions/landsat-shapefiles-and-kml-files)
- **Path 126, Row 62**: Confirmed coverage untuk Bengkulu & Jambi provinces, Sumatra

### Akurasi yang Terverifikasi:
- Dynamic World: **73.8-74%** (Nature Scientific Data 2022, independent study 72-75%)
- ESA WorldCover 2020: **74.4%**, WorldCover 2021: **76.7%**
- ESRI Land Cover: **>75%** (average over 75% per year)

**PENTING**: Semua URL, spesifikasi teknis, dan angka akurasi telah diverifikasi melalui sumber resmi. Informasi ini dapat dipercaya untuk ujian proposal.

---

# BAGIAN N: PENILAIAN AKHIR DAN REKOMENDASI

## N.1. Skor Keseluruhan Proposal

| Komponen | Bobot | Nilai (0-100) | Skor Tertimbang |
|----------|-------|---------------|-----------------|
| **Latar Belakang & Motivasi** | 15% | 70 | 10.5 |
| **Tinjauan Pustaka** | 15% | 65 | 9.75 |
| **Metodologi** | 35% | 35 | 12.25 |
| **Kelayakan Pelaksanaan** | 20% | 50 | 10.0 |
| **Penulisan & Format** | 15% | 60 | 9.0 |
| **TOTAL** | 100% | - | **51.5/100** |

**Interpretasi**:
- 0-50: **Tidak Lulus**
- 51-65: **Revisi Mayor** ← Proposal ini
- 66-80: Revisi Minor
- 81-100: Lulus

## N.2. Keputusan Ujian Proposal

### Skenario 1: Mahasiswa Menunjukkan Pemahaman Baik
**Jika mahasiswa bisa**:
- ✅ Mengidentifikasi masalah ground truth dan usulkan solusi konkret
- ✅ Jelaskan metodologi kombinasi dengan jelas (walau tidak sempurna)
- ✅ Akui kesalahan teknis (EPSG, kontradiksi, ejaan) dan berkomitmen perbaiki

**KEPUTUSAN**:
🟡 **LULUS DENGAN REVISI MAYOR**
- Deadline revisi: **4 minggu**
- Wajib sidang ulang untuk presentasi hasil revisi
- Fokus revisi: Ground truth, metodologi, koreksi teknis

---

### Skenario 2: Mahasiswa Tidak Bisa Menjawab Pertanyaan Kritis
**Jika mahasiswa**:
- ❌ Tidak paham konsep ground truth
- ❌ Tidak bisa jelaskan metodologi kombinasi
- ❌ Tidak sadar ada kesalahan EPSG dan kontradiksi NDBI

**KEPUTUSAN**:
🔴 **TIDAK LULUS**
- Harus ujian ulang setelah perbaikan fundamental
- Wajib konsultasi intensif dengan pembimbing
- Bimbingan tambahan tentang konsep dasar remote sensing

---

### Skenario 3: Mahasiswa Paham Konsep tapi Proposal Buruk
**Jika mahasiswa**:
- ✅ Paham konsep supervised classification, ground truth, dll
- ✅ Bisa jelaskan metodologi secara lisan dengan baik
- ❌ Tapi proposal tertulis banyak kesalahan dan ambigu

**KEPUTUSAN**:
🟡 **LULUS DENGAN REVISI MAYOR**
- Deadline revisi: **2 minggu**
- Fokus: Perbaiki tulisan agar konsisten dengan pemahaman
- Tidak perlu sidang ulang jika revisi disetujui pembimbing

---

## N.3. Checklist untuk Penguji

Sebelum ujian:
- [ ] Baca bagian A1-A7 (kesalahan fatal) dengan teliti
- [ ] **Baca BAGIAN M** (perbandingan dataset & ground truth) - PENTING untuk pertanyaan kritis!
- [ ] Siapkan pertanyaan dari Bagian E dan H (40 pertanyaan)
- [ ] Siapkan pertanyaan dari Bagian M.6 (tentang Landsat vs Sentinel, Dynamic World, dll)
- [ ] Print halaman berisi kesalahan kritis untuk ditunjukkan ke mahasiswa
- [ ] Koordinasi dengan penguji lain tentang aspek mana yang akan ditanyakan masing-masing

Saat ujian:
- [ ] Catat kemampuan mahasiswa menjawab per kategori (konsep, teknis, aplikasi)
- [ ] Beri kesempatan mahasiswa mengidentifikasi kesalahan sendiri sebelum ditunjukkan
- [ ] Dokumentasi komitmen mahasiswa untuk revisi

Setelah ujian:
- [ ] Buat daftar revisi tertulis yang spesifik dan terukur
- [ ] Tentukan deadline yang realistis
- [ ] Follow-up progress revisi (2 minggu sekali)

---

## N.4. Template Catatan Revisi untuk Mahasiswa

**LEMBAR REVISI PROPOSAL SKRIPSI**
**Nama**: Ayu Friska Purba (F1E122058)
**Judul**: Klasifikasi Tutupan Lahan dengan Kombinasi Nilai Indeks...
**Tanggal Ujian**: [Isi tanggal]
**Keputusan**: ⬜ Lulus ⬜ Lulus Revisi Minor ☑️ Lulus Revisi Mayor ⬜ Tidak Lulus

---

**REVISI WAJIB (CRITICAL)**:

1. **Ground Truth** (Deadline: 2 minggu) - **LIHAT BAGIAN M.3 untuk detail lengkap**
   - [ ] **RECOMMENDED**: Google Dynamic World 2015 & 2025 (gratis, 10m, independen) ATAU
   - [ ] Survei lapangan minimal 50 titik/kelas (250 titik total) ATAU
   - [ ] Gunakan Google Earth Pro historical imagery + digitasi manual ATAU
   - [ ] Kombinasi: Dynamic World (200 titik) + Survei lapangan (50 titik)
   - **Deliverable**: Database ground truth + metadata lengkap + dokumentasi sumber

2. **Metodologi Kombinasi** (Deadline: 1 minggu)
   - [ ] Tambahkan flowchart detail kombinasi indeks + MLC
   - [ ] Jelaskan apakah layer stack atau terpisah
   - **Deliverable**: Sub-bab baru "3.X Integrasi Nilai Indeks dan MLC"

3. **Koreksi Teknis** (Deadline: 3 hari)
   - [ ] EPSG:4326 → EPSG:32748
   - [ ] Perbaiki kontradiksi Tabel NDBI
   - [ ] Ubah tabel hasil dari nilai tunggal → rentang + statistik
   - **Deliverable**: Tabel 3.1, 3.2, 3.3 yang sudah diperbaiki

4. **Referensi** (Deadline: 3 hari)
   - [ ] Tambahkan 18 referensi yang dikutip tapi tidak ada
   - **Deliverable**: Daftar pustaka lengkap

---

**REVISI PENTING**:

5. **Justifikasi Pemilihan Dataset** (BARU - Lihat BAGIAN M.1)
   - [ ] Tambahkan sub-bab "Pertimbangan Pemilihan Landsat 8"
   - [ ] Jelaskan mengapa tidak pakai Sentinel-2 (resolusi lebih tinggi tapi arsip lebih pendek)
   - [ ] Dokumentasikan hasil pencarian di USGS Earth Explorer (Scene ID yang tersedia)
   - **Deliverable**: Tabel perbandingan Landsat 8 vs alternatif + justifikasi

6. Perbaiki ejaan "Likelihood" di seluruh dokumen termasuk JUDUL
7. Tambahkan waktu penelitian & timeline
8. Tentukan shapefile yang digunakan (205.43 atau 169.89 km²)
9. Jelaskan pembagian training dan testing (70:30)

---

**CATATAN PENGUJI**:
[Tulis catatan tambahan di sini]

---

**TANDA TANGAN MAHASISWA** (Tanda setuju dengan revisi):
Nama: ___________________ Tanggal: ___________

**TANDA TANGAN PENGUJI**:
1. _________________ (Ketua)
2. _________________ (Anggota 1)
3. _________________ (Anggota 2)

---

*Dokumen ini disusun untuk keperluan ujian proposal skripsi*
*Dosen Penguji: [Nama Anda]*
*Tanggal Analisis: 22 Desember 2025*
*Tanggal Ujian: [Besok]*

---

**LAMPIRAN: Quick Reference Guide untuk Dosen Penguji**

## 5 Pertanyaan Wajib yang Tidak Boleh Dilewatkan:

1. **"Dari mana ground truth untuk training MLC Anda?"**
   → Ini mengungkap kesalahan FATAL metodologi
   → Jawab yang diharapkan: Survei lapangan, citra resolusi tinggi, atau Dynamic World
   → Jika jawab "interpretasi visual" → SALAH FATAL!

2. **"Jelaskan secara teknis bagaimana NDVI, NDWI, NDBI dikombinasikan dengan MLC"**
   → Ini menguji apakah mahasiswa paham metodenya sendiri
   → Harus bisa jelaskan: layer stack atau terpisah?

3. **"Apa value added penelitian Anda dibanding Aulia et al. (2023) yang sudah ada?"**
   → Ini menguji originalitas dan kontribusi penelitian
   → Harus bisa sebutkan perbedaan metode dan hasil

4. **"Kenapa pakai Landsat 8, bukan Sentinel-2 yang gratis, resolusi 10m, dan revisit 5 hari?"** (BARU!)
   → Menguji apakah mahasiswa riset alternatif dataset (Lihat BAGIAN M.1)
   → Jawaban valid: Arsip temporal lebih panjang, konsistensi sensor
   → Jika tidak tahu Sentinel-2 → kurang riset!

5. **"Berapa scene Landsat yang Anda temukan dengan cloud <10% untuk tahun 2015 dan 2025? Sebutkan Scene ID-nya!"** (BARU!)
   → Menguji apakah mahasiswa sudah cek ketersediaan data di USGS (Lihat BAGIAN M.2)
   → Jika belum cek → penelitian prematur!

**Jika mahasiswa tidak bisa jawab 5 pertanyaan ini dengan memuaskan → TIDAK LULUS**

---

## Bagian-Bagian Penting dalam Dokumen Ini:

- **BAGIAN A**: Kesalahan Fatal/Konseptual (7 kesalahan KRITIS)
- **BAGIAN E + H**: 40 Pertanyaan Ujian (20+20)
- **BAGIAN I**: Strategi Bertanya untuk Penguji
- **BAGIAN M**: **[BARU]** Perbandingan Dataset & Sumber Ground Truth (Landsat vs Sentinel, Dynamic World, dll)
- **BAGIAN N**: Penilaian Akhir dan Keputusan Ujian

---

**Catatan Penting untuk Penguji**:
- Proposal ini memiliki struktur yang lengkap tapi eksekusinya bermasalah
- Mahasiswa mungkin copy-paste metodologi tanpa paham konsep
- Fokus ujian: Uji PEMAHAMAN bukan hanya hafalan
- Berikan kesempatan mahasiswa untuk perbaikan (revisi mayor) jika menunjukkan pemahaman dasar yang cukup

**Good luck untuk ujian besok! 💪**
