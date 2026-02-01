# 📘 PANDUAN LENGKAP SCRAPING REVIEW DUOLINGO
## Untuk Penelitian: Muhammad Farhan Hadrawi (F1E122149)

---

## 🚀 METODE 1: GOOGLE COLAB (PALING MUDAH - 5 MENIT)

### Langkah 1: Buka Google Colab
1. Buka browser (Chrome/Firefox/Edge)
2. Ketik di address bar: https://colab.research.google.com
3. Login dengan akun Google Anda
4. Klik **"New Notebook"** (tombol biru)

### Langkah 2: Copy-Paste Kode
1. Buka file: `scrape_duolingo_reviews.py`
2. Copy SEMUA isi file (Ctrl+A → Ctrl+C)
3. Paste di Colab (Ctrl+V)

### Langkah 3: Jalankan
1. Klik tombol **Play** ▶️ di sebelah kiri code cell
2. Tunggu muncul output seperti ini:
   ```
   ===================================================================
   SCRAPING REVIEW APLIKASI DUOLINGO
   ===================================================================
   🔄 Sedang mengambil data review...
   ⏳ Proses ini membutuhkan waktu 2-5 menit...
   ```

### Langkah 4: Tunggu Proses Selesai
- Jangan tutup browser
- Jangan refresh halaman
- Tunggu sampai muncul:
  ```
  ✅ PROSES SELESAI!
  📁 File tersimpan: duolingo_reviews_20250106_XXXXXX.csv
  ⬇️ File sedang di-download ke komputer Anda...
  ```

### Langkah 5: File CSV Otomatis Ter-Download
- Cek folder **Downloads** di komputer Anda
- File bernama: `duolingo_reviews_[tanggal]_[waktu].csv`
- **SELESAI!** 🎉

---

## 🖥️ METODE 2: PYTHON DI LAPTOP (Perlu Install Python)

### Prasyarat:
- Python 3.7+ sudah terinstall
- Koneksi internet stabil

### Langkah-Langkah:

#### 1. Buka Command Prompt/Terminal
- Windows: Tekan `Win+R` → ketik `cmd` → Enter
- Atau buka PowerShell

#### 2. Install Library
```bash
pip install google-play-scraper pandas
```

Tunggu sampai selesai (muncul "Successfully installed...")

#### 3. Jalankan Script
```bash
cd "C:\Users\MyPC PRO\Documents\sidang_skripsi\Farhan"
python scrape_duolingo_reviews.py
```

#### 4. Tunggu Proses (2-5 menit)
Output akan muncul di terminal

#### 5. File CSV Tersimpan
Lokasi: `C:\Users\MyPC PRO\Documents\sidang_skripsi\Farhan\duolingo_reviews_[timestamp].csv`

---

## 📊 HASIL YANG DIDAPAT

File CSV berisi **1.000 review** dengan kolom:

| Kolom | Deskripsi | Contoh |
|-------|-----------|--------|
| `username` | Nama pengguna | "Ahmad Rizki" |
| `review_text` | **ISI ULASAN** (DATA UTAMA) | "Bagus banget aplikasinya..." |
| `rating` | Rating bintang | 5 |
| `review_date` | Tanggal review | 2025-03-15 |
| `app_version` | Versi aplikasi saat review | 5.140.0 |
| `thumbs_up` | Jumlah like | 12 |
| `developer_reply` | Balasan developer | "Terima kasih atas..." |

---

## ⚠️ TROUBLESHOOTING (Jika Ada Error)

### Error 1: "ModuleNotFoundError: No module named 'google_play_scraper'"
**Solusi:**
```bash
pip install google-play-scraper
```

### Error 2: "Too many requests" atau "Rate limit exceeded"
**Penyebab:** Google Play Store membatasi request terlalu banyak dalam waktu singkat

**Solusi:**
1. Tunggu 15-30 menit
2. Coba lagi
3. Atau kurangi `MAX_REVIEWS` dari 1000 menjadi 500

### Error 3: Script jalan tapi dapat review sedikit (< 1000)
**Penyebab:** Review bahasa Indonesia memang terbatas dalam periode Jan-Nov 2025

**Solusi:**
1. Ubah filter tanggal di script:
   ```python
   # Ganti ini:
   (df_clean['review_date'] >= '2025-01-01') &
   (df_clean['review_date'] <= '2025-11-30')

   # Jadi ini (ambil semua tahun):
   (df_clean['review_date'] >= '2024-01-01')
   ```

### Error 4: Koneksi internet terputus
**Solusi:**
- Pastikan WiFi/data aktif
- Coba lagi dengan koneksi lebih stabil

---

## 📋 CHECKLIST SEBELUM SCRAPING

- [ ] Koneksi internet stabil
- [ ] Google Colab sudah dibuka ATAU Python sudah terinstall
- [ ] Library sudah diinstall (jika pakai laptop)
- [ ] Folder tujuan sudah siap
- [ ] Siap tunggu 2-5 menit

---

## 🎯 LANGKAH SETELAH DAPAT DATA

### 1. Verifikasi Data ✅
Buka file CSV, pastikan:
- Ada 1000 baris (atau mendekati)
- Kolom `review_text` terisi semua
- Tanggal sesuai periode penelitian

### 2. Preprocessing Data 🔧
Lakukan tahapan sesuai proposal:
- [ ] **Cleaning**: Hapus URL, mention, spasi berlebih
- [ ] **Case folding**: Ubah ke lowercase
- [ ] **Normalization**: Kata tidak baku → baku (gk → tidak, dll)

### 3. Pelabelan Sentimen 🏷️
- [ ] Baca setiap review
- [ ] Beri label: `positif` atau `negatif`
- [ ] Simpan hasil pelabelan

### 4. Split Data 📊
- [ ] 80% untuk training
- [ ] 20% untuk testing

### 5. Training Model 🤖
- [ ] Fine-tuning IndoBERTweet
- [ ] Evaluasi dengan metrik: accuracy, precision, recall, F1-score

### 6. Analisis Topik 📈
- [ ] Jalankan BERTopic
- [ ] Identifikasi topik utama
- [ ] Visualisasi hasil

---

## 📞 BANTUAN TAMBAHAN

Jika masih ada masalah, dokumentasikan:
1. Screenshot error message
2. Versi Python yang digunakan (`python --version`)
3. Library yang terinstall (`pip list`)

---

## 🎓 TIPS UNTUK SEMINAR BESOK

### Pertanyaan yang Mungkin Ditanya:

**Q1: "Kenapa pilih 1.000 data?"**
**A:** Berdasarkan penelitian IndoBERTweet original (Koto et al., 2021), model dapat mencapai performa tinggi dengan dataset 499-11.000 data. Jumlah 1.000 dipilih sebagai keseimbangan antara kecukupan data dan efisiensi pelabelan manual.

**Q2: "Bagaimana menangani data tidak seimbang (positif >> negatif)?"**
**A:** Opsi:
- Oversampling kelas minoritas
- Undersampling kelas mayoritas
- Gunakan class weights saat training
- Evaluasi dengan F1-score (lebih robust untuk imbalanced data)

**Q3: "Kenapa tidak pakai stemming?"**
**A:** Berdasarkan penelitian Khairani et al. (2024), IndoBERTweet mencapai akurasi lebih tinggi TANPA stemming dan stopword removal karena model sudah dilatih memahami konteks bahasa informal.

**Q4: "Bagaimana validasi hasil pelabelan?"**
**A:**
- Pelabelan dilakukan 2x oleh peneliti
- Hitung inter-rater reliability (Cohen's Kappa)
- Review ulang data yang ambigu

**Q5: "Apa yang dilakukan jika akurasi < 75%?"**
**A:**
- Hyperparameter tuning (learning rate, batch size, epoch)
- Tambah data berlabel
- Review kualitas pelabelan
- Coba teknik augmentasi data

---

## ✅ KESIMPULAN

1. **Scraping MUDAH** - Pakai Google Colab, 5 menit selesai
2. **Data LENGKAP** - 1.000 review dengan 7 kolom informasi
3. **Siap PREPROCESSING** - Tinggal lanjut ke tahap cleaning
4. **Metodologi SOLID** - Sesuai penelitian terdahulu

**SEMANGAT SEMINAR BESOK!** 🚀📊🎓

---

*Dibuat: 6 Januari 2026*
*Untuk: Muhammad Farhan Hadrawi (F1E122149)*
*Penelitian: Analisis Sentimen Aplikasi Duolingo*
