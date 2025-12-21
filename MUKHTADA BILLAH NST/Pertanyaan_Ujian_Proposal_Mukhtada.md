# DAFTAR PERTANYAAN UJIAN PROPOSAL SKRIPSI
## Mahasiswa: MUKHTADA BILLAH NST (F1E122037)
## Judul: Optimasi Algoritma Genetika Menggunakan Fuzzy Logic pada Penjadwalan Praktikum

---

# BAGIAN A: KESALAHAN PENULISAN DAN FORMAT DOKUMEN

## Pertanyaan A.1
**Pertanyaan:** Pada halaman 2, terdapat kata "menyelsaikan". Apa penulisan yang benar dan mengapa ketelitian dalam penulisan dokumen akademik sangat penting?

**TEMUAN KESALAHAN:**
- Halaman 2: "Diajukan sebagai salah satu syarat untuk **menyelsaikan** studi pada Program Studi Sistem Informasi"

**KOREKSI YANG SEHARUSNYA:**
- Penulisan yang benar adalah "**menyelesaikan**"
- Kesalahan ejaan (typo) seperti ini menunjukkan kurangnya proofreading dan dapat mempengaruhi kredibilitas dokumen akademik.

---

## Pertanyaan A.2
**Pertanyaan:** Dalam Daftar Tabel (halaman 8), terdapat "Tabel 3.12...Error! Bookmark not defined". Apa yang menyebabkan error ini dan bagaimana cara memperbaikinya?

**TEMUAN KESALAHAN:**
- Halaman 8 Daftar Tabel menunjukkan: "Tabel 3.12 Fuzzy logic pada tahap Mutation....... **Error! Bookmark not defined.**"

**KOREKSI YANG SEHARUSNYA:**
- Error ini terjadi karena Microsoft Word tidak dapat menemukan referensi silang (cross-reference) ke tabel tersebut
- Penyebab umum: tabel dihapus/dipindah tanpa memperbarui daftar tabel, atau field reference rusak
- Solusi: Update seluruh field (Ctrl+A, F9) atau buat ulang daftar tabel secara otomatis

---

## Pertanyaan A.3
**Pertanyaan:** Pada Daftar Gambar (halaman 9), terdapat dua gambar dengan nomor yang sama yaitu "Gambar 3.12". Bagaimana sistem penomoran gambar yang benar dalam penulisan ilmiah?

**TEMUAN KESALAHAN:**
Halaman 9 (Daftar Gambar) menunjukkan:
```
Gambar 3. 12 Alur proses mutation setelah penerapan fuzzy logic.............. 49
Gambar 3. 12 Contoh penerapan AG berbasis website............................... 53
```

**KOREKSI YANG SEHARUSNYA:**
- Gambar kedua (halaman 53) seharusnya bernomor **Gambar 3.13**
- Penomoran gambar harus berurutan dan unik
- Format: Gambar X.Y dimana X = nomor bab, Y = nomor urut gambar dalam bab

---

## Pertanyaan A.4
**Pertanyaan:** Pada Daftar Tabel (halaman 8), terdapat penomoran tabel yang tidak konsisten. Ada "Tabel 3.2" yang muncul di Bab 2 (halaman 23). Bagaimana seharusnya penomoran tabel dilakukan?

**TEMUAN KESALAHAN:**
Halaman 8 (Daftar Tabel) menunjukkan:
```
Tabel 2.1 Konflik yang terjadi pada perhitungan skor fitness.................. 12
Tabel 3.2 Metode perbandingan pada penelitian terdahulu tentang HGA ... 23
Tabel 2.3 Penelitian terdahulu terkait penerapan AG ............................. 26
```
- "Tabel 3.2" berada di halaman 23 yang merupakan bagian Bab 2 (Tinjauan Pustaka)
- Seharusnya bernomor **Tabel 2.2** bukan Tabel 3.2

**KOREKSI YANG SEHARUSNYA:**
- Penomoran tabel mengikuti format X.Y:
  - X = Nomor Bab
  - Y = Nomor urut tabel dalam bab tersebut
- Urutan yang benar di Bab 2 seharusnya: Tabel 2.1, Tabel 2.2, Tabel 2.3, dst.

---

## Pertanyaan A.5
**Pertanyaan:** Pada halaman 49, terdapat "Tabel 4.12" padahal halaman tersebut masih bagian dari Bab 3 (Metodologi Penelitian). Mengapa ini merupakan kesalahan?

**TEMUAN KESALAHAN:**
- Halaman 49 menampilkan "Tabel 4.12 Kategori Lonjakan pada"
- Halaman 49 masih merupakan bagian dari Bab 3 (Metodologi Penelitian)
- Nomor tabel tidak sesuai dengan nomor bab

**KOREKSI YANG SEHARUSNYA:**
- Tabel tersebut seharusnya bernomor **Tabel 3.12** atau sesuai urutan di Bab 3
- Nomor "4" menunjukkan Bab 4 yang belum ada dalam proposal ini

---

## Pertanyaan A.6
**Pertanyaan:** Pada Daftar Tabel (halaman 8), terdapat dua tabel dengan nomor "Tabel 3.3" (halaman 40 dan 52). Apa dampak duplikasi nomor tabel terhadap kualitas dokumen?

**TEMUAN KESALAHAN:**
Halaman 8 (Daftar Tabel):
```
Tabel 3.3 Rule Base Fuzzy Berdasarkan Total Konflik .............................. 40
...
Tabel 3.3 Tabel statistik untuk evaluasi optimasi algoritma ..................... 52
```

**KOREKSI YANG SEHARUSNYA:**
- Tabel di halaman 52 seharusnya memiliki nomor yang berbeda (misalnya Tabel 3.14 atau sesuai urutan)
- Duplikasi nomor menyulitkan pembaca untuk merujuk tabel yang dimaksud

---

# BAGIAN B: METODOLOGI FUZZY LOGIC - FITNESS FUNCTION

## Pertanyaan B.1
**Pertanyaan:** Mengapa Anda menggunakan nilai bobot penalti alpha = 3.0, beta = 1.0, dan gamma = 2.0 pada rumus fitness function (halaman 12)? Apa dasar pemilihan nilai-nilai ini?

**CATATAN:** Pertanyaan ini menguji justifikasi parameter.

Halaman 12 menyebutkan:
```
Penalty = alpha(Room Conflicts) + beta(Group Conflicts) + gamma(Assistant Conflicts)
dengan alpha = 3.0, beta = 1.0, gamma = 2.0
```

**JAWABAN IDEAL:**
Pemilihan bobot penalti harus berdasarkan:
1. **Prioritas constraint**: Hard constraint (konflik ruangan) lebih penting dari soft constraint
2. **Studi literatur**: Sebutkan referensi yang menggunakan nilai serupa
3. **Eksperimen pendahuluan**: Lakukan sensitivity analysis
4. **Domain knowledge**: Konsultasi dengan pihak FST tentang prioritas

---

## Pertanyaan B.2
**Pertanyaan:** Dalam fuzzy inference untuk fitness (Tabel 3.3 halaman 40), Anda menggunakan output crisp melalui defuzzifikasi. Apa metode defuzzifikasi yang digunakan? Center of Gravity (COG), Mean of Maximum (MOM), atau metode lain?

**CATATAN:**
- Dokumen menyebutkan penggunaan weighted average pada halaman 43
- Mahasiswa harus bisa menjelaskan alasan pemilihan metode

---

## Pertanyaan B.3
**Pertanyaan:** Pada Tabel 3.2 (halaman 39), Anda mendefinisikan fuzzy membership function untuk konflik. Mengapa Anda memilih fungsi segitiga dan trapesium? Apa kelebihan dan kekurangan masing-masing?

**CATATAN:** Pertanyaan untuk menguji pemahaman fungsi keanggotaan fuzzy.

---

# BAGIAN C: METODOLOGI FUZZY LOGIC - CROSSOVER RATE

## Pertanyaan C.1
**Pertanyaan:** Pada Tabel 3.7 (halaman 45), Anda menggunakan standar deviasi fitness sebagai input untuk menentukan crossover rate. Bagaimana Anda menentukan range nilai untuk kategori LOW (0.00-0.05), MEDIUM (0.02-0.08), dan HIGH (>0.05)?

**CATATAN:** Pertanyaan untuk menguji justifikasi parameter fuzzy.

---

## Pertanyaan C.2
**Pertanyaan:** Tabel 3.9 (halaman 46) menunjukkan aturan fuzzy untuk crossover rate. Mengapa ketika diversity LOW, crossover rate menjadi HIGH? Bukankah ini bertentangan dengan prinsip eksploitasi?

**JAWABAN IDEAL:**
Logika yang digunakan: "diversity rendah = populasi konvergen = perlu eksplorasi tinggi (crossover tinggi)". Ini adalah mekanisme untuk mencegah premature convergence.

---

## Pertanyaan C.3
**Pertanyaan:** Berapa jumlah total aturan fuzzy yang Anda gunakan untuk crossover rate? Dengan 1 input (diversity/SD fitness) dan 3 kategori, seharusnya ada 3 aturan. Apakah ini cukup untuk mengontrol crossover secara adaptif?

**CATATAN:** Verifikasi kelengkapan rule base.

---

# BAGIAN D: METODOLOGI FUZZY LOGIC - MUTATION RATE

## Pertanyaan D.1
**Pertanyaan:** Pada implementasi fuzzy untuk mutation (halaman 48-51), Anda menggunakan "lonjakan fitness dari iterasi sebelumnya" sebagai input. Mengapa tidak menggunakan "stagnation counter" yang lebih umum digunakan dalam literatur?

**CATATAN:** Pertanyaan untuk menguji alternatif desain.

---

## Pertanyaan D.2
**Pertanyaan:** Range mutation rate yang Anda gunakan adalah 0.01 - 0.10 (Tabel 3.13 halaman 51). Mengapa nilai maksimum hanya 0.10? Apakah nilai ini cukup untuk keluar dari local optimum?

**CATATAN:** Pertanyaan tentang parameter mutation.

---

## Pertanyaan D.3
**Pertanyaan:** Pada Tabel 3.13 (halaman 50), ketika improvement HIGH, mutation rate menjadi LOW. Bukankah seharusnya jika sudah ada peningkatan yang baik, kita tetap perlu eksplorasi untuk mencari solusi yang lebih baik?

**JAWABAN IDEAL:**
Logika yang digunakan: "improvement tinggi = populasi berkembang baik = perlu menjaga stabilitas (mutation rendah)". Ini mencegah kerusakan struktur individu yang sudah baik.

---

# BAGIAN E: STRUKTUR KROMOSOM DAN REPRESENTASI

## Pertanyaan E.1
**Pertanyaan:** Pada Gambar 3.3 (halaman 32), Anda mendefinisikan struktur kromosom dengan berbagai atribut. Bagaimana jika ada praktikum yang membutuhkan lebih dari 1 slot waktu berturut-turut? Apakah representasi ini bisa mengakomodasi?

**CATATAN:** Menguji fleksibilitas representasi kromosom.

---

## Pertanyaan E.2
**Pertanyaan:** Berapa ukuran kromosom (jumlah gen) dalam penelitian Anda? Bagaimana hubungannya dengan jumlah mata kuliah praktikum yang dijadwalkan?

**CATATAN:** Pertanyaan teknis implementasi.

---

## Pertanyaan E.3
**Pertanyaan:** Anda menggunakan Roulette Wheel Selection (Gambar 3.6 halaman 35). Mengapa tidak menggunakan Tournament Selection yang lebih robust terhadap scaling fitness?

**JAWABAN IDEAL:**
```
Tournament Selection kelebihan:
- Tidak sensitif terhadap fitness scaling
- Mudah mengontrol selection pressure via tournament size
- Lebih efisien secara komputasi

Roulette Wheel kelebihan:
- Memberikan kesempatan proporsional ke semua individu
- Klasik dan banyak digunakan di literatur
```

---

# BAGIAN F: METRIK EVALUASI

## Pertanyaan F.1
**Pertanyaan:** Pada bagian Evaluasi (halaman 52), Anda menyebutkan akan menggunakan metrik "Makespan", "flow time", dan "average lateness". Apakah metrik-metrik ini tepat untuk Course/Lab Timetabling Problem? Apa perbedaannya dengan Job Shop Scheduling?

**CATATAN PENTING:**
Metrik yang disebutkan lebih cocok untuk Job Shop Scheduling Problem (JSSP), bukan Course Timetabling Problem (CTP).

**KOREKSI YANG SEHARUSNYA:**
Metrik yang lebih tepat untuk Course Timetabling:
1. **Hard Constraint Violations (HCV)**
   - Bentrok jadwal dosen
   - Bentrok jadwal ruangan
   - Bentrok jadwal mahasiswa

2. **Soft Constraint Violations (SCV)**
   - Preferensi waktu dosen
   - Distribusi beban mengajar

3. **Fitness Value Convergence**
   - Rata-rata fitness per generasi
   - Best fitness per generasi

4. **Computational Performance**
   - Waktu eksekusi
   - Jumlah generasi sampai konvergen

---

## Pertanyaan F.2
**Pertanyaan:** Bagaimana Anda akan membandingkan hasil GA+Fuzzy dengan GA standar? Apa baseline yang digunakan?

**JAWABAN IDEAL:**
Perbandingan yang fair memerlukan:
1. Parameter GA standar yang sama (ukuran populasi, max generasi)
2. Crossover dan mutation rate tetap untuk GA standar
3. Jumlah run yang sama (minimal 30 independent runs)
4. Statistical test untuk signifikansi
5. Seed random yang sama untuk reproducibility

---

# BAGIAN G: NOVELTY DAN GAP PENELITIAN

## Pertanyaan G.1
**Pertanyaan:** Apa yang membedakan penelitian Anda dengan penelitian sebelumnya seperti Ghaffar et al. (2022) yang juga menggunakan Fuzzy-based Adaptive GA untuk course timetabling?

**CATATAN:** Pertanyaan untuk menguji kontribusi penelitian.

---

## Pertanyaan G.2
**Pertanyaan:** Anda menyebutkan beberapa penelitian terdahulu (Tabel 2.3 halaman 26) menggunakan GA untuk penjadwalan. Mengapa pendekatan mereka tidak cukup untuk kasus di FST Universitas Jambi?

**CATATAN:** Menguji gap analysis.

---

# BAGIAN H: ASPEK TEKNIS IMPLEMENTASI

## Pertanyaan H.1
**Pertanyaan:** Berapa ukuran populasi yang akan Anda gunakan? Bagaimana menentukan ukuran populasi yang optimal untuk kasus penjadwalan praktikum ini?

**CATATAN:** Pertanyaan parameter setting.

---

## Pertanyaan H.2
**Pertanyaan:** Apa kriteria berhenti (stopping criteria) yang digunakan? Apakah hanya maksimum generasi, atau ada kriteria konvergensi?

**JAWABAN IDEAL:**
Stopping criteria yang baik:
1. Maximum generation
2. Convergence: tidak ada perbaikan selama N generasi
3. Target fitness achieved (fitness = 1.0)
4. Time limit

---

## Pertanyaan H.3
**Pertanyaan:** Bagaimana Anda memastikan solusi yang dihasilkan valid (tidak ada hard constraint yang dilanggar)? Apakah repair function (Gambar 3.7 halaman 35) sudah cukup?

**CATATAN:** Pertanyaan constraint handling.

---

# BAGIAN I: REFERENSI DAN KEABSAHAN SUMBER

## Pertanyaan I.1
**Pertanyaan:** Berapa persen referensi Anda yang berasal dari jurnal terindeks (Scopus/WoS) dalam 5 tahun terakhir?

**CATATAN:** Pertanyaan standar tentang kualitas referensi.

---

## Pertanyaan I.2
**Pertanyaan:** Dalam daftar pustaka, Anda banyak mengutip penelitian tahun 2021-2025. Apakah ada paper foundational yang harus dikutip seperti Srinivas & Patnaik (1994) untuk adaptive GA atau Zadeh (1965) untuk fuzzy logic?

**CATATAN:** Pertanyaan tentang referensi klasik yang wajib ada.

---

# BAGIAN J: PEMAHAMAN KONSEPTUAL

## Pertanyaan J.1
**Pertanyaan:** Jelaskan dengan bahasa Anda sendiri, apa perbedaan antara hard constraint dan soft constraint dalam konteks penjadwalan praktikum?

**JAWABAN IDEAL:**
```
Hard Constraint: Kendala yang HARUS dipenuhi, jika dilanggar solusi tidak valid
- Contoh: Satu ruangan tidak boleh digunakan 2 kelas bersamaan
- Contoh: Satu asisten tidak boleh mengajar 2 kelas di waktu yang sama

Soft Constraint: Kendala yang SEBAIKNYA dipenuhi, untuk meningkatkan kualitas
- Contoh: Asisten X lebih suka mengajar pagi hari
- Contoh: Distribusi jadwal merata sepanjang minggu
```

---

## Pertanyaan J.2
**Pertanyaan:** Dalam Algoritma Genetika, apa yang dimaksud dengan "premature convergence"? Bagaimana fuzzy logic dalam penelitian Anda membantu mencegah hal ini?

**CATATAN:** Pertanyaan inti dari kontribusi penelitian.

---

## Pertanyaan J.3
**Pertanyaan:** Apa perbedaan antara fuzzifikasi, inferensi fuzzy, dan defuzzifikasi? Berikan contoh dari penelitian Anda.

**JAWABAN IDEAL:**
```
1. Fuzzifikasi: Mengubah nilai crisp menjadi derajat keanggotaan fuzzy
   Contoh: Konflik = 3 -> mu_LOW = 0.33, mu_MED = 0.67, mu_HIGH = 0

2. Inferensi: Menjalankan aturan IF-THEN fuzzy
   Contoh: IF Konflik = LOW THEN Quality = EXCELLENT

3. Defuzzifikasi: Mengubah hasil fuzzy menjadi nilai crisp
   Contoh: Quality = (0.2*90 + 0.8*60 + 0.1*30) / 1.1 = 62.7
```

---

## Pertanyaan J.4
**Pertanyaan:** Mengapa Anda memilih menggunakan fuzzy logic dibandingkan metode adaptive lainnya seperti self-adaptive GA atau reinforcement learning untuk parameter control?

**CATATAN:** Menguji justifikasi pemilihan metode.

---

# BAGIAN K: PERTANYAAN PENUTUP

## Pertanyaan K.1
**Pertanyaan:** Apa keterbatasan (limitation) dari pendekatan yang Anda usulkan?

**CATATAN:** Pertanyaan reflektif.

---

## Pertanyaan K.2
**Pertanyaan:** Jika waktu dan resource tidak terbatas, apa improvement yang akan Anda lakukan terhadap penelitian ini?

**CATATAN:** Pertanyaan untuk mengukur visi mahasiswa.

---

# RINGKASAN TEMUAN KESALAHAN DOKUMEN

| No | Lokasi | Jenis Kesalahan | Tingkat Keparahan |
|----|--------|-----------------|-------------------|
| 1 | Halaman 2 | Typo "menyelsaikan" seharusnya "menyelesaikan" | Medium |
| 2 | Daftar Tabel (hal 8) | "Tabel 3.2" di Bab 2 seharusnya "Tabel 2.2" | Medium |
| 3 | Daftar Tabel (hal 8) | "Tabel 3.12...Error! Bookmark not defined" | Tinggi |
| 4 | Daftar Gambar (hal 9) | Duplikat "Gambar 3.12" (hal 49 & 53) | Medium |
| 5 | Halaman 49 | "Tabel 4.12" di Bab 3 seharusnya "Tabel 3.x" | Medium |
| 6 | Daftar Tabel (hal 8) | Duplikat "Tabel 3.3" (hal 40 & 52) | Medium |
| 7 | Halaman 52 | Metrik evaluasi (makespan, flow time) kurang tepat untuk Course Timetabling | Perlu Klarifikasi |

---

# REKOMENDASI UNTUK PENGUJI

1. **Pertanyaan Prioritas Tinggi**: A.2 (Error Bookmark), A.3-A.6 (Penomoran), F.1 (Metrik Evaluasi)
2. **Pertanyaan untuk Menguji Pemahaman**: J.1, J.2, J.3
3. **Pertanyaan untuk Menguji Novelty**: G.1, G.2
4. **Pertanyaan Teknis**: E.1, E.3, H.1, H.2

---

*Dokumen ini disusun untuk keperluan ujian proposal skripsi*
*Tanggal: 19 Desember 2025*
*Revisi: Telah diperbaiki berdasarkan verifikasi ulang dokumen PDF*

---

# LAMPIRAN: REFERENSI AKADEMIK YANG VALID

## 1. ADAPTIVE GENETIC ALGORITHM - FOUNDATIONAL PAPERS

### Referensi Klasik (Wajib Dikutip)

**[R1] Srinivas, M., & Patnaik, L.M. (1994)**
"Adaptive Probabilities of Crossover and Mutation in Genetic Algorithms"
*IEEE Transactions on Systems, Man, and Cybernetics*, 24(4), 656-667.
- **Relevansi**: Paper foundational yang pertama kali memperkenalkan konsep adaptive crossover dan mutation rate berdasarkan fitness. WAJIB dikutip untuk penelitian tentang adaptive GA.

---

### Fuzzy Logic untuk Parameter Control GA

**[R2] Vannucci, M., & Colla, V. (2015)**
"Fuzzy adaptation of crossover and mutation rates in genetic algorithms based on population performance"
*Journal of Intelligent & Fuzzy Systems*
- **Relevansi**: Pendekatan serupa dengan proposal - menggunakan fuzzy inference untuk menyesuaikan crossover dan mutation rate.

**[R3] Herrera, F., & Lozano, M. (2003)**
"Fuzzy adaptive genetic algorithms: design, taxonomy, and future directions"
*Soft Computing*, 7(8), 545-562.
- **Relevansi**: Review komprehensif tentang Fuzzy Genetic Algorithms.

---

## 2. CONSTRAINT HANDLING & PENALTY FUNCTION

**[R4] Deb, K. (2000)**
"An efficient constraint handling method for genetic algorithms"
*Computer Methods in Applied Mechanics and Engineering*, 186(2-4), 311-338.
- **Relevansi**: Paper KLASIK tentang constraint handling di GA. Membahas penalty function.
- **PENTING**: Mahasiswa HARUS mengutip paper ini jika membahas penalty-based fitness function.

---

## 3. UNIVERSITY COURSE TIMETABLING PROBLEM (UCTP)

**[R5] ITC 2019 - International Timetabling Competition**
- **Website Resmi**: https://www.itc2019.org/
- **Relevansi**: Dataset benchmark standar untuk university course timetabling.

**[R6] Lewis, R. (2008)**
"A survey of metaheuristic-based techniques for University Timetabling Problems"
*OR Spectrum*, 30(1), 167-190.
- **Relevansi**: Survey komprehensif tentang metrik dan metode untuk course timetabling.

---

## 4. BUKU TEKS STANDAR

**[B1] Goldberg, D.E. (1989)**
"Genetic Algorithms in Search, Optimization, and Machine Learning"
*Addison-Wesley* - Buku klasik GA

**[B2] Zadeh, L.A. (1965)**
"Fuzzy Sets"
*Information and Control*, 8(3), 338-353 - Paper foundational fuzzy logic

**[B3] Mamdani, E.H., & Assilian, S. (1975)**
"An Experiment in Linguistic Synthesis with a Fuzzy Logic Controller"
*International Journal of Man-Machine Studies*, 7(1), 1-13 - Mamdani fuzzy inference

---

*Referensi dikumpulkan dari database akademik: IEEE Xplore, Springer, ScienceDirect*
