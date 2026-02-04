# DAFTAR PERTANYAAN SIDANG AKHIR SKRIPSI
## Fachrul Sukmadinata (F1E121159)
### Implementasi dan Pengujian Sistem Pencatatan dan Monitoring Kekeruhan Air Berbasis Internet of Things (Studi Kasus: PAMTIRTA Tempino)

**Total Kesalahan Teridentifikasi:** 25+ kesalahan (termasuk 4 kesalahan fatal, 8 kesalahan serius, dan 13+ kesalahan minor)

---

# BAGIAN A: PERTANYAAN BERDASARKAN KESALAHAN FATAL

---

## Q1. KESALAHAN PERHITUNGAN TOTAL TEST CASE BLACKBOX

**📍 Lokasi:** BAB IV, Halaman 200, Sub-bab 4.4 Pengujian Blackbox

**📝 Kutipan Asli (Halaman 200):**
> "Dari pengujian yang telah dilakukan, didapatkan hasil dan diperoleh fungsi yang berjalan dengan baik **19+8+4 = 31** fungsi."

**📝 Fakta dari Tabel:**
- **Tabel 59 (Admin):** Terdapat 22 baris test case (Login sampai Menghapus tarif)
- **Tabel 60 (Petugas):** Terdapat 8 baris test case
- **Tabel 61 (Pelanggan):** Terdapat 4 baris test case

**❌ Kesalahan GANDA:**
1. Angka **19** salah - seharusnya **22** (dari Tabel 59)
2. Total **31** salah - seharusnya **22 + 8 + 4 = 34**

**❓ Pertanyaan untuk Mahasiswa:**
> "Saya sudah menghitung dengan teliti Tabel 59 di halaman 197-198. Ada **22 fungsi** yang diuji untuk Admin. Bahkan di perhitungan per-role Anda sendiri di halaman 199, Anda tulis 'Presentase Skor = 22'. **Jadi dari mana angka 19 di halaman 200?** Bagaimana kesalahan matematika SD seperti **19+8+4=31** (yang seharusnya 22+8+4=34) bisa lolos sampai sidang?"

**✅ Jawaban yang Seharusnya:**
- Mahasiswa HARUS mengakui ini adalah kesalahan fatal
- Total yang benar: **22 + 8 + 4 = 34 test case**
- Angka 19 kemungkinan sisa dari draft lama yang tidak diperbarui

---

## Q2. DUPLIKASI PENOMORAN SUB-BAB DI BAB II

**📍 Lokasi:** BAB II Tinjauan Pustaka, Halaman 13-24 dan Daftar Isi (Halaman viii)

**📝 Fakta dari Daftar Isi:**
```
2.7 SDLC ................................................................... 13
2.8 Rapid Application Development (RAD) ..................... 19
2.7 Framework Laravel ........................................... 21 ← DUPLIKAT!
2.8 MySQL ........................................................... 21 ← DUPLIKAT!
2.9 Sensor Turbidity .................................................. 22
```

**❌ Kesalahan:**
Penomoran sub-bab **RESET** setelah RAD - ada DUA sub-bab 2.7 dan DUA sub-bab 2.8!

**❓ Pertanyaan untuk Mahasiswa:**
> "Coba buka BAB II skripsi Anda. Di halaman 13 ada 2.7 SDLC. Di halaman 19 ada 2.8 RAD. Lalu di halaman 21, tiba-tiba muncul lagi **2.7 Framework Laravel** dan **2.8 MySQL**. **Bagaimana bisa ada DUA sub-bab 2.7? DUA sub-bab 2.8?** Seharusnya Framework Laravel itu nomor berapa?"

**✅ Jawaban yang Seharusnya:**
- Framework Laravel seharusnya **2.9** (bukan 2.7)
- MySQL seharusnya **2.10** (bukan 2.8)
- Dan seterusnya sampai 2.14 Penelitian Terdahulu

---

## Q3. TYPO NAMA PENULIS SENDIRI DI PRAKATA

**📍 Lokasi:** Halaman vii (Prakata), bagian tanda tangan

**📝 Kutipan Asli:**
> "Fachrul **Sukmdinata**"

**❌ Kesalahan:**
Nama penulis sendiri **SALAH TULIS**! Huruf "**a**" hilang di "Sukm**a**dinata".

**❓ Pertanyaan untuk Mahasiswa:**
> "Di halaman Prakata, tempat Anda menandatangani karya ilmiah Anda, nama Anda tertulis '**Sukmdinata**' - tanpa huruf 'a'. **Bagaimana bisa nama sendiri salah tulis di dokumen yang Anda tandatangani?** Apakah Anda membaca skripsi ini sebelum disubmit?"

**✅ Jawaban yang Seharusnya:**
- Nama yang benar: **Fachrul Sukmadinata**
- Ini adalah kesalahan fatal yang sangat memalukan

---

## Q4. HEADER TABEL 7 SALAH - KONTRADIKSI DALAM SATU TABEL

**📍 Lokasi:** BAB III, Halaman 35, Tabel 7

**📝 Fakta:**
- **Judul tabel:** "Tabel 7. Kebutuhan **Non-Fungsional**"
- **Header kolom dalam tabel:** "Kebutuhan **Fungsional**"

**❌ Kesalahan:**
Kontradiksi dalam satu tabel yang sama! Judul bilang Non-Fungsional, header kolom bilang Fungsional.

**❓ Pertanyaan untuk Mahasiswa:**
> "Lihat Tabel 7 di halaman 35. Judulnya '**Kebutuhan Non-Fungsional**', tapi header kolom di dalamnya tertulis '**Kebutuhan Fungsional**'. **Mana yang benar?** Isinya tentang kompatibilitas browser dan koneksi internet - itu kebutuhan apa? Coba jelaskan perbedaan kebutuhan fungsional dan non-fungsional!"

**✅ Jawaban yang Seharusnya:**
- Header kolom seharusnya "**Kebutuhan Non-Fungsional**"
- **Fungsional**: APA yang dilakukan sistem (fitur)
- **Non-Fungsional**: BAGAIMANA sistem bekerja (kualitas)

---

# BAGIAN B: PERTANYAAN BERDASARKAN KESALAHAN SERIUS

---

## Q5. KALIBRASI SENSOR TIDAK MENGGUNAKAN ALAT STANDAR

**📍 Lokasi:** BAB IV, Halaman 165, Sub-bab Pengujian Sensor

**📝 Kutipan Asli:**
> "Dalam penelitian ini, **nilai acuan NTU untuk setiap sampel tidak diperoleh dari pengukuran langsung menggunakan turbidity meter**, tetapi diambil dari studi terdahulu dalam jurnal yang menggunakan sampel dan karakteristik larutan serupa."

**📝 Tabel 51 - Hasil Pengujian Sensor:**
| Sampel Air | Alat uji (dari jurnal) | Sensor | Akurasi |
|-----------|----------------------|--------|---------|
| Air Mineral | 0 | 0 | 100% |
| Kopi | 89 | 91.30 | 97.5% |
| Detergen | 91 | 93.54 | 97.3% |

**❌ Kesalahan Metodologi:**
Nilai pembanding BUKAN dari pengukuran langsung, tapi dari jurnal. Konsentrasi larutan tidak distandarisasi.

**❓ Pertanyaan untuk Mahasiswa:**
> "Anda mengklaim sensor memiliki akurasi 97.5%. Tapi nilai pembandingnya bukan dari alat ukur standar, melainkan dari **jurnal**. **Berapa gram kopi yang Anda larutkan per liter air?** Apakah sama persis dengan jurnal referensi? **Mengapa tidak menggunakan turbidimeter standar?** Apakah klaim akurasi 97% ini valid secara ilmiah?"

**✅ Jawaban yang Seharusnya:**
- Ini adalah **KETERBATASAN SERIUS** dalam penelitian
- Kalibrasi valid harus menggunakan turbidimeter standar atau larutan formazin
- Nilai akurasi 97% tidak dapat diklaim secara absolut

---

## Q6. STANDAR KEKERUHAN AIR TIDAK DISEBUTKAN

**📍 Lokasi:** Seluruh dokumen skripsi

**📝 Fakta:**
- Sistem memonitor kekeruhan dalam satuan NTU
- **TIDAK ADA** penjelasan tentang standar NTU
- Menurut **PERMENKES No. 492/2010**: Air minum maksimal **5 NTU**, Air bersih maksimal **25 NTU**
- Sistem tidak memberikan alert jika kekeruhan melewati batas

**❓ Pertanyaan untuk Mahasiswa:**
> "Sistem Anda memonitor kekeruhan air dalam satuan NTU. **Berapa batas NTU untuk air yang layak konsumsi menurut PERMENKES?** Apakah sistem Anda memberikan peringatan otomatis jika kekeruhan melewati batas aman? **Di mana standar ini disebutkan dalam skripsi Anda?**"

**✅ Jawaban yang Seharusnya:**
- PERMENKES No. 492/2010: Air minum maksimal **5 NTU**, Air bersih maksimal **25 NTU**
- Sistem BELUM memiliki fitur alert (disebutkan di Saran halaman 202)

---

## Q7. INKONSISTENSI TERMINOLOGI "WARGA" VS "PELANGGAN"

**📍 Lokasi:** 
- Tabel 9 (halaman 38): Aktor = "Ketua, Petugas, **Warga**"
- Tabel 10 (halaman 39): Aktor = "Ketua, Petugas, **Pelanggan**"

**❓ Pertanyaan untuk Mahasiswa:**
> "Di Tabel 9 Anda sebut aktornya '**Warga**', di Tabel 10 Anda sebut '**Pelanggan**'. **Mana yang benar?** Dalam penulisan ilmiah, konsistensi terminologi sangat penting. Mengapa bisa berbeda?"

**✅ Jawaban yang Seharusnya:**
- Istilah yang konsisten adalah **Pelanggan**
- "Warga" adalah kesalahan yang harus diperbaiki

---

## Q8. KESALAHAN REFERENSI NOMOR GAMBAR (6 KESALAHAN)

**📍 Lokasi:** BAB IV, beberapa halaman

| Halaman | Tertulis | Seharusnya |
|---------|----------|------------|
| 135 | "gambar 57" | Gambar 69 |
| 137 | "gambar 58" | Gambar 70 |
| 138 | "gambar 59" | Gambar 71 |
| 139 | "Gambar 23" | Gambar 72 |
| 186 | "Gambar 72 dan 73" | Gambar 108 dan 109 |
| 187 | "gambar 18" | Gambar 110 |

**❓ Pertanyaan untuk Mahasiswa:**
> "Di halaman 139, Anda menyebutkan 'Gambar 23' tapi gambar yang ada adalah Gambar 72. Di halaman 187, Anda menyebutkan 'gambar 18' tapi gambar yang ada adalah Gambar 110. **Berapa banyak kesalahan referensi gambar yang ada di skripsi Anda?** Mengapa bisa terjadi?"

**✅ Jawaban yang Seharusnya:**
- Minimal 6 kesalahan referensi gambar
- Terjadi karena perubahan urutan gambar tanpa update referensi teks
- Seharusnya menggunakan fitur cross-reference di Word

---

## Q9. DUPLIKASI JUDUL GAMBAR (Gambar 38 dan 39)

**📍 Lokasi:** Daftar Gambar, halaman xii

**📝 Fakta:**
- Gambar 38: "Sequence Diagram **Melihat Pemakaian Air**"
- Gambar 39: "Sequence Diagram **Melihat Pemakaian Air**"

**❌ Kesalahan:**
Dua gambar berurutan dengan judul yang **SAMA PERSIS**!

**❓ Pertanyaan untuk Mahasiswa:**
> "Di Daftar Gambar, Gambar 38 dan Gambar 39 judulnya **sama persis**: 'Sequence Diagram Melihat Pemakaian Air'. **Apa bedanya kedua gambar ini?** Mengapa judulnya sama? Apakah ini duplikasi atau kesalahan penamaan?"

**✅ Jawaban yang Seharusnya:**
- Salah satu gambar seharusnya memiliki judul berbeda
- Mungkin Gambar 39 untuk use case yang berbeda (misal: Monitoring Kekeruhan)

---

## Q10. TIDAK ADA PERBANDINGAN KUANTITATIF EFISIENSI

**📍 Lokasi:** BAB I (Tujuan) dan BAB V (Kesimpulan)

**📝 Kutipan Tujuan (Halaman 4):**
> "Menguji **efisiensi dan efektivitas** sistem menggunakan metode black box."

**📝 Fakta:**
- Tidak ada data perbandingan waktu pencatatan manual vs digital
- Tidak ada pengukuran pengurangan error rate
- Tidak ada metrik efisiensi yang terukur

**❓ Pertanyaan untuk Mahasiswa:**
> "Di tujuan penelitian, Anda menyebutkan ingin menguji **efisiensi dan efektivitas** sistem. **Berapa lama waktu pencatatan dengan metode manual?** Berapa lama dengan sistem digital Anda? **Berapa persentase pengurangan kesalahan?** Tanpa data pembanding, bagaimana Anda bisa mengklaim sistem efisien?"

**✅ Jawaban yang Seharusnya:**
- Mengakui tidak ada pengukuran kuantitatif efisiensi
- Idealnya ada data seperti: Waktu manual X menit vs Digital Y menit

---

## Q11. INTERVAL PENGIRIMAN DATA MQTT 10 DETIK TANPA ERROR HANDLING

**📍 Lokasi:** BAB IV, Halaman 168, Kode Program Sensor

**📝 Kutipan Kode:**
```c
// Kirim data setiap 10 detik
if (millis() - lastMillis > 10000) {
    lastMillis = millis();
    publishMessage();
}
```

**❓ Pertanyaan untuk Mahasiswa:**
> "Pada kode sensor, data dikirim setiap **10 detik**. **Mengapa dipilih 10 detik?** Apakah ada analisis trade-off frekuensi vs bandwidth? **Bagaimana jika koneksi WiFi terputus?** Apakah ada mekanisme retry atau buffer data? Saya tidak melihat error handling di kode Anda."

**✅ Jawaban yang Seharusnya:**
- Harus ada justifikasi pemilihan interval 10 detik
- Harus ada error handling jika koneksi terputus (reconnect logic)
- Buffer data penting untuk menghindari kehilangan data

---

## Q12. JUMLAH RESPONDEN PENGUJIAN HANYA 5 ORANG

**📍 Lokasi:** BAB IV, Halaman 197

**📝 Kutipan:**
> "Pengujian ini melibatkan **5 orang** yang memiliki peran berbeda, yaitu ketua, petugas, dan pelanggan."

**❓ Pertanyaan untuk Mahasiswa:**
> "Anda melakukan pengujian dengan hanya **5 orang** (1 ketua, 2 petugas, 2 pelanggan). Untuk sistem yang akan digunakan oleh puluhan pelanggan, **apakah 5 responden cukup representatif?** Apa justifikasi ilmiah untuk jumlah responden ini?"

**✅ Jawaban yang Seharusnya:**
- Mengakui ini adalah keterbatasan penelitian
- Bisa mengacu pada Nielsen (2000) bahwa 5 responden cukup untuk usability testing
- Tapi untuk functional testing, idealnya lebih banyak

---

# BAGIAN C: PERTANYAAN TEKNIS IoT DAN SISTEM

---

## Q13. KEAMANAN SISTEM MQTT DAN WEB

**📍 Lokasi:** BAB II (Protokol MQTT) dan BAB IV (Implementasi)

**📝 Kutipan BAB II:**
> "MQTT biasanya berjalan di atas TCP/IP dan menggunakan port default 1883, serta **mendukung keamanan dengan protokol SSL/TLS**."

**❓ Pertanyaan untuk Mahasiswa:**
> "Di BAB II, Anda menyebutkan MQTT mendukung SSL/TLS. **Apakah implementasi Anda menggunakan enkripsi?** Bagaimana dengan keamanan web? **Apakah password di-hash?** Data pelanggan dan tagihan perlu dilindungi dari manipulasi."

**✅ Jawaban yang Seharusnya:**
- AWS IoT menggunakan TLS by default untuk semua koneksi
- Laravel memiliki hashing password bawaan (bcrypt)
- Cloudflare menyediakan HTTPS untuk web

---

## Q14. MEKANISME BACKUP DAN DISASTER RECOVERY

**📍 Lokasi:** BAB IV, Halaman 201 (Deployment)

**📝 Kutipan:**
> "Proses deployment dilakukan menggunakan server berbasis **AWS EC2**..."

**❓ Pertanyaan untuk Mahasiswa:**
> "Data pemakaian air pelanggan penting untuk penagihan. **Bagaimana mekanisme backup data?** Jika server AWS bermasalah, **apakah ada disaster recovery plan?** Berapa lama data bisa dipulihkan?"

**✅ Jawaban yang Seharusnya:**
- AWS menyediakan fitur snapshot dan backup untuk EC2
- Idealnya ada backup database harian/mingguan
- Jika belum dikonfigurasi, ini adalah kelemahan yang perlu diatasi

---

## Q15. SKALABILITAS DAN VALIDASI SISTEM DI PRODUCTION

**📍 Lokasi:** BAB I Batasan Penelitian dan BAB IV Implementasi

**📝 Kutipan:**
> "Implementasi sistem hanya diterapkan pada lingkup PAMTIRTA Tempino dan **belum dirancang untuk skala besar**..."

**❓ Pertanyaan untuk Mahasiswa:**
> "PAMTIRTA Tempino saat ini memiliki **berapa pelanggan aktif?** Sistem sudah di-deploy di sipamtino.site. **Berapa lama sistem sudah digunakan secara real?** Apakah ada feedback dari pengguna sesungguhnya? Pernahkah terjadi bug atau error di production?"

**✅ Jawaban yang Seharusnya:**
- Mahasiswa harus menyebutkan:
  - Jumlah pelanggan aktual yang terdaftar
  - Durasi sistem sudah live
  - Feedback real dari pengguna
  - Kendala atau bug yang ditemukan

---

# BAGIAN D: TABEL KESALAHAN PENULISAN DAN TYPO

---

| No | Lokasi | Halaman | Kesalahan | Seharusnya |
|----|--------|---------|-----------|------------|
| 1 | Prakata | vii | "Fachrul **Sukmdinata**" | "Fachrul **Sukmadinata**" |
| 2 | BAB III | 27 | "bulan **mei** 2025" | "bulan **Mei** 2025" |
| 3 | BAB II | 22 | "membantu **menilapakah**" | "membantu **menilai apakah**" |
| 4 | Tabel 7 | 35 | Header "Kebutuhan **Fungsional**" | "Kebutuhan **Non-Fungsional**" |
| 5 | Tabel 9 | 38 | Aktor: "**Warga**" | Aktor: "**Pelanggan**" |
| 6 | Tabel 11 | 40 | "**mencatatat** angka meteran" | "**mencatat** angka meteran" |
| 7 | Daftar Gambar | xii | "**Monitoing** Kekeruhan" | "**Monitoring** Kekeruhan" |
| 8 | Daftar Gambar | xiii | "Melihat **Pata** Pemakaian" | "Melihat **Data** Pemakaian" |
| 9 | Daftar Gambar | xii-xiii | "**Acitivity** diagram" (banyak) | "**Activity** diagram" |
| 10 | BAB IV | 164 | "Sensor **Kekekeruhan**" | "Sensor **Kekeruhan**" |
| 11 | BAB IV | 200 | "**19**+8+4 = 31" | "**22**+8+4 = 34" |
| 12 | Daftar Isi | viii | "**2.7** Framework Laravel" | "**2.9** Framework Laravel" |
| 13 | Daftar Isi | viii | "**2.8** MySQL" | "**2.10** MySQL" |

---

# BAGIAN E: KESALAHAN REFERENSI GAMBAR

| No | Halaman | Tertulis dalam Teks | Gambar yang Sebenarnya Ditampilkan |
|----|---------|---------------------|-----------------------------------|
| 1 | 135 | "gambar **57**" | Gambar **69** |
| 2 | 137 | "gambar **58**" | Gambar **70** |
| 3 | 138 | "gambar **59**" | Gambar **71** |
| 4 | 139 | "Gambar **23**" | Gambar **72** |
| 5 | 186 | "Gambar **72 dan 73**" | Gambar **108 dan 109** |
| 6 | 187 | "gambar **18**" | Gambar **110** |

---

# BAGIAN F: RINGKASAN UNTUK PENGUJI

## ❌ Kesalahan FATAL (4 item - WAJIB DITANYAKAN):
1. **Kesalahan perhitungan test case** → 22+8+4=34, BUKAN 19+8+4=31
2. **Duplikasi penomoran sub-bab** → 2.7 dan 2.8 muncul DUA KALI
3. **Typo nama penulis sendiri** → "Sukmdinata" tanpa huruf 'a'
4. **Header Tabel 7 kontradiktif** → Judul Non-Fungsional, header Fungsional

## ⚠️ Kesalahan SERIUS (8 item):
5. **Kalibrasi sensor tidak valid** → Pakai referensi jurnal, bukan alat standar
6. **Tidak ada standar NTU** → PERMENKES 492/2010 tidak disebutkan
7. **Inkonsistensi terminologi** → Warga vs Pelanggan
8. **6 kesalahan referensi gambar** → Gambar 23, 57, 58, 59, 72-73, 18
9. **Duplikasi judul gambar** → Gambar 38 dan 39 sama
10. **Tidak ada perbandingan kuantitatif** → Efisiensi tidak terukur
11. **Tidak ada error handling** → Koneksi MQTT bisa gagal
12. **Responden hanya 5 orang** → Kurang representatif

## 📝 Kesalahan MINOR/Typo (13+ item):
- "Acitivity" → "Activity" (banyak tempat)
- "Monitoing" → "Monitoring"
- "Pata" → "Data"
- "menilapakah" → "menilai apakah"
- "mencatatat" → "mencatat"
- "Kekekeruhan" → "Kekeruhan"
- "mei" → "Mei"
- Dan lainnya...

## ❓ Yang TIDAK ADA tetapi SEHARUSNYA ADA:
1. Standar NTU menurut PERMENKES (5 NTU air minum, 25 NTU air bersih)
2. Fitur alert/notifikasi jika kekeruhan melewati batas
3. Perbandingan kuantitatif efisiensi (waktu pencatatan, error rate)
4. Mekanisme backup dan disaster recovery
5. Error handling untuk koneksi sensor
6. Pengujian keamanan sistem
7. Dokumentasi prosedur kalibrasi yang valid

---

*Dokumen ini disiapkan untuk sidang akhir*
*Tanggal: 6 Januari 2026*
*Total: 15 pertanyaan tajam + 25+ kesalahan teridentifikasi*
