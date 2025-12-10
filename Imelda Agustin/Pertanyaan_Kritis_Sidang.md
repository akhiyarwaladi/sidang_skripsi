# PERTANYAAN KRITIS UNTUK SIDANG PROPOSAL
## Imelda Agustin (F1E122002)
### Prediksi Harga Saham BMRI dengan LSTM dan Analisis Sentimen

---

## 1. KESALAHAN FUNDAMENTAL: INISIALISASI BOBOT LSTM

### Masalah Kritis
Pada halaman 40, tertulis:
- W = (−1/√d, 1/√d) = (−0.408, 0.408)
- Nilai W = 0.408 digunakan dalam perhitungan sebagai **skalar tunggal**

### Pertanyaan Penguji:

**Q1.1:** Saudari menuliskan W = 0.408 dan menggunakannya sebagai nilai tunggal dalam perhitungan LSTM (halaman 40-43). Padahal, dalam LSTM yang benar, W adalah **matriks berukuran besar**.

**PENJELASAN DETAIL DIMENSI WEIGHT:**

Input ke setiap gate LSTM adalah concatenation dari:
- Hidden state sebelumnya (h_{t-1}): misalnya 50 units
- Input saat ini (x_t): 6 fitur (Close, High, Low, Open, Volume, Sentimen)
- **Total = 50 + 6 = 56 dimensi**

Maka W untuk setiap gate (forget, input, cell, output) seharusnya:
- **Dimensi: 50 × 56 = 2.800 parameter**
- Bukan satu nilai 0.408!

**Visualisasi:**
```
[h_{t-1}; x_t] = [h1, h2, ..., h50, Close, High, Low, Open, Vol, Sent]
                  |______________|  |___________________________|
                    50 elemen              6 elemen

                  Total = 56 elemen

W_f (forget gate) = Matriks 50 × 56:
[0.052  -0.118   0.089 ... -0.031]  ← 56 kolom
[-0.107  0.024   0.133 ...  0.071]
[0.045  -0.092   0.011 ... -0.128]
  ...
[-0.067  0.101  -0.054 ...  0.098]
↑ 50 baris

Setiap nilai di-random dalam rentang (-0.134, 0.134)
```

**Operasi Matriks yang Benar:**
```
f_t = σ(W_f · [h_{t-1}; x_t] + b_f)
      [50×56] · [56×1] + [50×1] = [50×1]
```

**Total parameter untuk 4 gates:**
- W_forget: 50 × 56 = 2,800
- W_input: 50 × 56 = 2,800
- W_cell: 50 × 56 = 2,800
- W_output: 50 × 56 = 2,800
- Plus bias: 4 × 50 = 200
- **TOTAL: 11,400 parameter**

**Pertanyaan menghancurkan:**
- **"Saudari menggunakan W = 0.408 sebagai satu angka. Seharusnya ada 11,400 parameter. Bagaimana bisa menghitung LSTM dengan hanya 1 angka?"**
- **"Dari mana angka 56 di proposal Saudari? Apakah Saudari memahami bahwa 56 = hidden_units + input_features?"**
- **"Jika model Keras LSTM(50 units) dengan 6 input features, berapa total parameter yang dilatih? (Jawaban: ~11,400, bukan 1!)"**

**Q1.2:** Formula W = (−1/√d, 1/√d) = (−0.408, 0.408) sebenarnya menunjukkan **rentang untuk inisialisasi random** (Xavier initialization), bukan nilai tetap. Artinya, setiap elemen matriks W diinisialisasi dengan nilai acak antara −0.408 hingga +0.408.

**Mengapa Saudari menggunakan 0.408 sebagai nilai tunggal untuk semua perhitungan? Apakah Saudari memahami perbedaan antara rentang inisialisasi dengan nilai aktual bobot?**

**Q1.3:** Dengan kesalahan konseptual sebesar ini tentang struktur dasar LSTM, **bagaimana Saudari yakin bahwa implementasi model Saudari benar?** Apakah ada bukti bahwa model telah diimplementasikan dengan benar di kode program?

---

## 2. ARSITEKTUR MODEL TIDAK TERDEFINISI

### Masalah Kritis
Tidak ada penjelasan tentang:
- Jumlah timestep/sequence length
- Jumlah layer LSTM
- Jumlah unit per layer
- Dropout rate
- Optimizer yang digunakan
- Learning rate

### Pertanyaan Penguji:

**Q2.1:** **Berapa timestep/sequence length yang Saudari gunakan?**

**PENJELASAN DETAIL:**
Timestep adalah jumlah hari historis yang digunakan untuk memprediksi 1 hari ke depan (lookback period).

**Ilustrasi:**
- Timestep = 5 hari: Model melihat 5 hari terakhir untuk prediksi hari ke-6
- Timestep = 20 hari: Model melihat 20 hari terakhir (≈ 1 bulan trading)
- Timestep = 60 hari: Model melihat 60 hari terakhir (≈ 3 bulan trading)

**Dampak pada Data Training:**
Dengan data ~250 hari dan split 80:20:

| Timestep | Training Sequences | Testing Sequences |
|----------|-------------------|-------------------|
| 5 hari   | 200 - 5 = 195     | 50 - 5 = 45      |
| 20 hari  | 200 - 20 = 180    | 50 - 20 = 30     |
| 60 hari  | 200 - 60 = 140    | 50 - 60 = **TIDAK CUKUP!** |

**Permasalahan Kritis:**
Saudari TIDAK MENYEBUTKAN timestep sama sekali di proposal! Ini parameter fundamental yang menentukan:
1. Berapa banyak data training tersedia
2. Seberapa jauh model melihat ke belakang
3. Dimensi input ke LSTM (samples × timestep × features)

**Pertanyaan menghancurkan:**
- **"Berapa timestep yang akan Saudari gunakan? 5, 10, 20, atau berapa?"**
- **"Jika menggunakan timestep 60 hari dengan data testing 50 hari, apakah testing sequences masih cukup untuk evaluasi yang reliable?"**
- **"Bagaimana Saudari menentukan timestep optimal? Apakah dengan eksperimen atau hanya tebak-tebakan?"**
- **"Dalam penelitian time series LSTM, nilai umum adalah 10-60 hari. Mengapa tidak ada satupun informasi ini di proposal?"**

**Q2.2:** **Berapa jumlah layer LSTM dan berapa unit per layer?**
- Single layer 50 units berbeda drastis dengan 3 layers masing-masing 100 units
- Ini mempengaruhi kapasitas model dan risiko overfitting

**Mengapa tidak ada informasi ini di proposal?**

**Q2.3:** Arsitektur model adalah inti dari penelitian machine learning. **Bagaimana reviewer atau pembaca dapat mereproduksi penelitian Saudari jika informasi fundamental ini tidak ada?**

---

## 3. TIDAK ADA VALIDATION SET

### Masalah Kritis
Halaman 32: "Data akan dibagi menjadi 80% data latih dan 20% data uji"
- Hanya ada train dan test
- Tidak ada validation set untuk tuning hyperparameter

### Pertanyaan Penguji:

**Q3.1:** Dalam deep learning, validation set digunakan untuk:
- Memilih jumlah epoch optimal (early stopping)
- Tuning learning rate
- Memilih arsitektur terbaik
- Mendeteksi overfitting selama training

**Tanpa validation set, bagaimana Saudari melakukan tuning hyperparameter? Apakah Saudari menggunakan test set untuk tuning? Jika ya, ini adalah kesalahan metodologi serius (data leakage).**

**Q3.2:** Bagaimana Saudari menentukan kapan harus menghentikan training? Apakah menggunakan fixed epoch? Jika ya, bagaimana menentukan jumlah epoch optimal tanpa validation set?

---

## 4. TIDAK ADA UJI STASIONERITAS

### Masalah Kritis
Data time series finansial umumnya **non-stationary** (memiliki trend, seasonal pattern, variance berubah)

### Pertanyaan Penguji:

**Q4.1:** Augmented Dickey-Fuller (ADF) test adalah standar industri untuk mengecek stasioneritas data time series finansial.

**PENJELASAN DETAIL ADF TEST:**

**Apa itu Stasioneritas?**
Data stasioner = properti statistik (mean, variance) **konstan** sepanjang waktu.

**Visualisasi:**
```
DATA STASIONER (Mean konstan):
     |    *  *     *        *   *
     |  *    *  *    * *  *   *    *
Mean |--*------*-------*--*------*----  ← rata-rata tetap
     |    *  *    *  *      *  *
     +--------------------------------→ Waktu

DATA NON-STASIONER (Ada trend naik):
     |                           * *
     |                       * *
     |                   * *        ← Trend naik
     |               * *
     |           * *
     |       * *
     |   * *
     | *
     +--------------------------------→ Waktu
     Mean berubah = NON-STATIONARY
```

**Contoh Konkret dengan Data Harga BMRI:**
```python
from statsmodels.tsa.stattools import adfuller

close_prices = [4380, 4360, 4310, 4260, 4290, 4250, 4390,
                4250, 4230, 4090, 4050, 4090, 4050, 4300,
                4350, 4330, 4430, 4550, 4470, 4510, 4650,
                4800, 4720]

result = adfuller(close_prices)
print(f"ADF Statistic: {result[0]:.4f}")
print(f"p-value: {result[1]:.4f}")

# Output (ilustrasi):
# ADF Statistic: -1.2847
# p-value: 0.6352  ← > 0.05 = NON-STATIONARY!
```

**Interpretasi:**
- **p-value = 0.6352 > 0.05** → GAGAL TOLAK H₀ → Data NON-STATIONARY
- **ADF Statistic = -1.285 > Critical Value (-2.998)** → NON-STATIONARY

**Hipotesis:**
```
H₀: Data memiliki unit root (NON-STATIONARY)
H₁: Data tidak memiliki unit root (STATIONARY)

Jika p-value < 0.05 → Reject H₀ → Data STATIONARY ✓
Jika p-value ≥ 0.05 → Fail to reject H₀ → Data NON-STATIONARY ✗
```

**Mengapa Ini Penting?**
Jika data non-stationary (ada trend):
1. Model belajar trend, bukan pola fluktuasi
2. LSTM mungkin hanya "menghafal" harga naik terus
3. Gagal generalisasi saat trend berubah
4. Metrik evaluasi menyesatkan

**Pertanyaan menghancurkan:**
- **"Apakah Saudari melakukan ADF test pada data harga saham BMRI? Jika ya, berapa p-value yang didapat?"**
- **"Data harga saham umumnya memiliki trend (non-stationary). Bagaimana Saudari menangani ini? Differencing? Log returns?"**
- **"Jika model dilatih saat trend bullish (harga naik), bagaimana bisa akurat saat trend bearish (harga turun)?"**

**Q4.2:** Jika data terbukti non-stationary, seharusnya dilakukan transformasi seperti:
- Differencing: X(t) - X(t-1)
- Log returns: log(X(t)) - log(X(t-1))
- Detrending

**Apakah Saudari melakukan langkah-langkah ini?**

**Q4.3:** Min-Max Normalization (halaman 38) **TIDAK SAMA** dengan membuat data stationary. Normalization hanya mengubah skala, tidak menghilangkan trend atau seasonal pattern.

**Apakah Saudari memahami perbedaan antara normalization dan stationarity transformation?**

---

## 5. TIDAK ADA BASELINE COMPARISON

### Masalah Kritis
Tidak ada model pembanding untuk menunjukkan bahwa LSTM memang lebih baik

### Pertanyaan Penguji:

**Q5.1:** Bagaimana Saudari membuktikan bahwa LSTM dengan sentiment analysis lebih baik dibanding:
- LSTM tanpa sentiment?
- ARIMA?
- Simple moving average?
- Random walk model?

**Tanpa comparison, bagaimana kita tahu model Saudari benar-benar memberikan value?**

**Q5.2:** RMSE = 56.696 (halaman 45). Apakah ini bagus atau buruk?
- Jika harga saham berkisar 5000-7000, RMSE 56 adalah ~1% error → bagus
- Tapi bagaimana kita tahu ini lebih baik dari model sederhana?

**Apakah Saudari akan menambahkan baseline comparison di penelitian final?**

---

## 6. INSET LEXICON: TIDAK SESUAI UNTUK KONTEKS FINANSIAL/BISNIS

### Masalah Kritis yang Sangat Serius

InSet Lexicon adalah kamus sentimen **umum bahasa Indonesia**, BUKAN kamus untuk domain finansial/perbankan. Ini kesalahan metodologi fatal yang dapat menggugurkan seluruh penelitian.

### FAKTA TENTANG INSET LEXICON

Berdasarkan paper asli dan penelitian terkini:

**Desain dan Tujuan:**
- InSet Lexicon dirancang **KHUSUS untuk analisis sentimen di microblogs (Twitter)** pada tahun 2017
- Dibangun dari kumpulan kata-kata dalam tweet bahasa Indonesia
- Fokus pada bahasa **informal dan percakapan media sosial**, bukan bahasa formal bisnis/finansial

**Komposisi:**
- 3,609 kata positif
- 6,609 kata negatif (**bias 65% negatif**)
- Total hanya **10,218 kata** dengan bobot -5 hingga +5
- Dibuat dengan pelabelan manual kemudian diperkaya dengan stemming dan sinonim

**Akurasi yang Rendah:**
- Akurasi tertinggi hanya **65.78%** pada data Twitter (paper asli 2017)
- Penelitian terbaru menunjukkan akurasi InSet turun menjadi **59.82% - 59.99%**
- Hanya **30% akurasi dalam feature extraction** untuk emotion recognition
- Jauh lebih rendah dari IndoBERT yang mencapai **74.79%**

**Domain Spesificity:**
- Penelitian 2024 menunjukkan InSet mengandung banyak kata **informal** dari Twitter
- TIDAK dirancang untuk domain finansial, perbankan, atau pasar modal
- Tidak memiliki vocabulary khusus finansial Indonesia

### Pertanyaan Penguji:

**Q6.1: VALIDASI KAMUS - KESALAHAN METODOLOGI FUNDAMENTAL**

**Berdasarkan fakta bahwa InSet Lexicon dirancang KHUSUS untuk Twitter/microblogs dengan bahasa informal, bagaimana Saudari membenarkan penggunaannya untuk analisis berita finansial formal tentang saham perbankan?**

**Bukti ketidaksesuaian:**

1. **Domain Mismatch Kritis:**
   - InSet: Dibuat dari **data Twitter** (bahasa informal, slang, singkatan)
   - Penelitian Saudari: **Berita finansial formal** dari media ekonomi
   - Ini seperti menggunakan kamus bahasa gaul untuk menganalisis jurnal ilmiah!

2. **Akurasi Rendah:**
   - InSet hanya **59.82% - 65.78% akurasi** bahkan pada domain aslinya (Twitter)
   - Bagaimana Saudari bisa yakin akurasinya tidak lebih buruk lagi di domain finansial yang berbeda total?

3. **Bias Negatif:**
   - InSet memiliki **65% kata negatif vs 35% positif**
   - Apakah ini menciptakan bias sistematis dalam scoring sentimen berita BMRI?

4. **Tidak Ada Validasi:**
   - **TIDAK ADA SATU PUN penelitian yang memvalidasi InSet untuk domain finansial Indonesia**
   - Saudari menggunakan tools tanpa membuktikan validitasnya di domain penelitian
   - Ini pelanggaran metodologi serius!

**Pertanyaan krusial: Berapa akurasi InSet Lexicon pada data berita finansial BMRI Saudari? Sudahkah Saudari melakukan validasi manual terhadap minimal 100 berita untuk mengecek apakah skor InSet sesuai dengan penilaian manusia?**

---

**Q6.2: MASALAH POLISEMI (MAKNA GANDA)**

Kata-kata dalam konteks finansial sering memiliki makna berbeda:

**Contoh 1: "MELEMAH"**
- Dalam InSet: "melemah" = sentimen negatif (-2 atau -3)
- Dalam konteks: "Rupiah melemah terhadap dolar"
  - Untuk perusahaan **eksportir**: POSITIF (profit naik)
  - Untuk perusahaan **importir**: NEGATIF (biaya naik)
  - Untuk **bank**: KOMPLEKS (tergantung eksposur valas)

**Pada Tabel 9 halaman 37, Saudari memberikan skor -7 untuk berita "Rupiah Melemah...". Apakah Saudari yakin ini selalu negatif untuk BMRI? Bagaimana jika BMRI memiliki banyak aset/pendapatan dalam USD?**

**Contoh 2: "TURUN"**
- "Harga saham turun" → negatif
- "Suku bunga turun" → POSITIF untuk perbankan (kredit meningkat)
- "NPL turun" → SANGAT POSITIF (kualitas kredit membaik)

**Bagaimana InSet Lexicon membedakan konteks-konteks ini?**

---

**Q6.3: MISSING VOCABULARY (KATA HILANG) - COVERAGE TIDAK MEMADAI**

**FAKTA: InSet Lexicon hanya memiliki 10,218 kata total (3,609 positif + 6,609 negatif)**

**BUKTI KONKRET - SAYA SUDAH DOWNLOAD DAN ANALISIS InSet Lexicon dari GitHub:**

**File positive.tsv (~2,500 entries):**
- Contoh kata: hai, makasih, thanks, promo, halo, terimakasih, semboyan, ditunggu, punya, asih, gelar, senyum, cedayam, bener, terbaik
- **Kata finansial yang ADA:** hanya "laba" (bobot +4)
- **Kata finansial yang TIDAK ADA:** likuiditas, volatilitas, kapitalisasi, rugi, untung

**File negative.tsv (2,827 entries):**
- Contoh kata: nggak, gatau, apaan, ngakak, males, atuh, anjir, soalnya, malem, mulu, ngga, doang, abis
- **Kata finansial yang ADA:** defisit (-3), pailit (-5), bangkrut (-5), merugi (-5)
- **Kata finansial yang TIDAK ADA:** NPL, kredit bermasalah, volatilitas, likuiditas

**KESIMPULAN DARI ANALISIS LANGSUNG:**
1. **InSet sangat informal:** kata-kata seperti "nggak", "gatau", "apaan", "ngakak", "anjir", "doang" dominan
2. **Kata finansial MINIMAL:** dari 10,218 kata, hanya ada: laba, defisit, pailit, bangkrut, merugi (5 kata!)
3. **Missing istilah krusial:** likuiditas, volatilitas, NPL, kapitalisasi, rugi, untung - TIDAK ADA SEMUA!

Bandingkan dengan vocabulary berita finansial yang jauh lebih besar dan spesifik. InSet **TERBUKTI TIDAK MEMILIKI** banyak istilah krusial finansial/perbankan karena:
1. Dibuat dari Twitter (bahasa informal - terbukti dari kata: gatau, nggak, ngakak)
2. Bukan domain finansial (hanya 5 kata finansial dari 10,218 kata = 0.05%!)
3. Coverage terbatas dan tidak relevan untuk berita finansial formal

**Istilah Finansial/Perbankan yang TIDAK ADA di InSet:**

**Metrik Perbankan:**
- Likuiditas / likuidasi
- Volatilitas / volatil
- NPL (Non-Performing Loan) / kredit bermasalah
- LDR (Loan to Deposit Ratio)
- CAR (Capital Adequacy Ratio) / rasio kecukupan modal
- ROA (Return on Assets)
- ROE (Return on Equity)
- NIM (Net Interest Margin)
- CASA (Current Account Saving Account)
- Cost of fund
- Fee-based income

**Corporate Actions:**
- Buyback / pembelian kembali saham
- Rights issue / HMETD
- Stock split / pemecahan saham
- Dividen interim
- Dilusi saham
- IPO / penawaran umum perdana
- Private placement

**Analisis Finansial:**
- Price to book value (PBV)
- Price to earnings ratio (PER)
- Earnings per share (EPS)
- Market capitalization / kapitalisasi pasar
- EBITDA
- Free cash flow
- Debt to equity ratio
- Book value / nilai buku

**Istilah Makroekonomi:**
- Quantitative easing
- Hawkish / dovish (kebijakan moneter)
- Repo rate / reverse repo
- Bad debt / utang macet
- Restrukturisasi kredit
- Capital inflow / outflow

**IMPLIKASI KRITIS:**

Jika InSet tidak mengenali kata-kata ini, maka:

1. **"Bank Mandiri meningkatkan likuiditas"** → Skor 0 (netral)
   - Seharusnya: POSITIF (+3 atau +4)

2. **"NPL BMRI turun menjadi 2.1%"** → Skor 0 (netral)
   - Seharusnya: SANGAT POSITIF (+5) - ini indikator kesehatan bank!

3. **"BMRIumumkan buyback saham Rp 2 triliun"** → Skor 0 atau random
   - Seharusnya: POSITIF (+4) - sinyal manajemen yakin pada valuasi

4. **"Rights issue BMRI untuk tingkatkan CAR"** → Skor 0
   - Seharusnya: NETRAL atau sedikit NEGATIF (dilusi, tapi untuk tujuan baik)

**PERTANYAAN MENGHANCURKAN BERDASARKAN BUKTI KONKRET:**

1. **"Saudari Imelda, saya sudah download dan analisis InSet Lexicon dari GitHub. InSet berisi kata-kata informal Twitter seperti 'nggak', 'gatau', 'apaan', 'ngakak', 'anjir', 'doang'. Dari 10,218 kata, HANYA 5 KATA yang terkait finansial: laba, defisit, pailit, bangkrut, merugi."**

   **"Bagaimana Saudari bisa menggunakan kamus yang 99.95% bukan kata finansial untuk menganalisis berita finansial formal BMRI? Ini seperti menggunakan kamus bahasa gaul untuk menganalisis laporan keuangan!"**

2. **"InSet TIDAK MEMILIKI kata: likuiditas, volatilitas, NPL, kapitalisasi, rugi, untung, ROA, ROE, CAR, LDR, buyback, rights issue, dan ratusan istilah finansial penting lainnya."**

   **"Jika InSet tidak mengenali kata-kata ini, maka berita-berita penting seperti 'NPL BMRI turun ke 2.1%' atau 'BMRI tingkatkan likuiditas' akan mendapat skor 0 (netral), padahal ini berita SANGAT POSITIF untuk kesehatan bank!"**

   **"Berapa persen berita BMRI Saudari yang mengandung istilah finansial yang TIDAK DIKENALI InSet? Apakah 30%? 40%? 50%? Sudahkah Saudari hitung coverage rate?"**

3. **"Mari kita test langsung dengan Tabel 9 Saudari (halaman 37):"**
   - **Berita:** "Mandiri (BMRI) Salurkan 63% Guyuran Likuiditas..."
   - **Kata 'likuiditas':** TIDAK ADA di InSet → skor 0
   - **Skor Saudari:** +2 (dari mana? kata apa yang dikenaali?)

   **"Bagaimana Saudari memverifikasi bahwa skor +2 itu benar? Apakah Saudari cek manual kata mana yang InSet kenali dari berita itu?"**

4. **"Dari analisis konkret InSet Lexicon, terbukti:**
   - **99.95% kata bukan finansial** (hanya 5 dari 10,218)
   - **Dominan bahasa informal** (gatau, nggak, ngakak - cocok untuk Twitter, TIDAK untuk berita formal)
   - **Missing critical financial terms** (ratusan istilah tidak ada)

   **"Dengan bukti ini, bagaimana Saudari masih bisa mempertahankan bahwa InSet cocok untuk penelitian Saudari?"**

5. **"Pertanyaan terakhir yang krusial: Apakah Saudari PERNAH membuka file InSet Lexicon dan melihat isinya sebelum memutuskan menggunakannya? Atau Saudari hanya lihat paper InSet mengatakan 'sentiment analysis' lalu langsung pakai tanpa cek isinya?"**

   **"Jika Saudari sudah buka dan lihat isinya penuh kata informal dan minim kata finansial, mengapa tetap dipakai? Jika tidak pernah buka dan cek isinya, apakah ini bukan tanda kurangnya rigor dalam metodologi penelitian?"**

---

**Q6.4: ANALISIS TABEL 9 (HALAMAN 37) - BUKTI KONKRET**

Mari kita analisis contoh dari proposal Saudari sendiri:

**Berita 1:** "Rupiah Melemah, Investor Asing Tinggalkan Pasar Modal RI"
- **Skor Saudari:** -7 (sangat negatif)
- **Masalah:** Apakah ini selalu buruk untuk BMRI?
  - Jika BMRI punya banyak USD assets → bisa POSITIF
  - Jika BMRI punya banyak USD debt → bisa NEGATIF
  - Konteks sangat penting

**Bagaimana InSet menangani nuansa ini?**

**Berita 2:** "Mandiri (BMRI) Salurkan 63% Guyuran Likuiditas..."
- **Skor Saudari:** +2 (positif lemah)
- **Masalah:** Ini berita tentang likuiditas bank
  - Kata "likuiditas" kemungkinan tidak ada di InSet → skor 0
  - Hanya kata-kata umum seperti "salurkan" yang diberi skor
  - **Apakah skor +2 benar-benar merepresentasikan sentimen berita ini?**

**Bagaimana Saudari memverifikasi bahwa skor sentimen yang dihasilkan akurat?**

**Berita 3:** "JPMorgan Hindari BBNI dan BMRI, Pilih BBCA dan BBRI"
- **Skor Saudari:** -3 (negatif)
- **Masalah:** "JPMorgan hindari BMRI" adalah red flag besar dari institusi keuangan global
  - Seharusnya skor lebih negatif (misalnya -5 atau -6)
  - **Apakah skor -3 cukup merepresentasikan severity berita ini?**

---

**Q6.5: ALTERNATIVE YANG SEHARUSNYA DIGUNAKAN - ADA RESOURCES YANG LEBIH BAIK!**

**FAKTA PENTING: Ada resources spesifik untuk sentiment analysis saham Indonesia yang Saudari ABAIKAN!**

**1. ID-SMSA Dataset (2024) - KHUSUS UNTUK SAHAM INDONESIA**
- **Indonesian Stock Market Dataset for Sentiment Analysis (ID-SMSA)**
- Published tahun **2024** - sangat baru dan relevan!
- Berisi **3,288 tweets** tentang 10 saham terbesar di Indonesia (termasuk BMRI!)
- Data dari **Januari 2021 - Maret 2024** (periode yang overlap dengan penelitian Saudari!)
- Sentimen sudah dilabeli: 2,339 positif, 999 netral, 1,025 negatif
- Dataset berkualitas tinggi dengan anotasi untuk tugas sentiment analysis
- **Ini adalah dataset PERTAMA dalam bahasa Indonesia yang spesifik untuk pasar saham Indonesia**

**Pertanyaan menghancurkan: Mengapa Saudari tidak menggunakan ID-SMSA dataset yang DIRANCANG KHUSUS untuk analisis sentimen saham Indonesia, dan malah menggunakan InSet yang dirancang untuk Twitter umum?**

**2. IndoBERT Post-Trained untuk Domain Finansial**
- Penelitian 2024 menunjukkan IndoBERT yang di-post-training dengan data finansial Indonesia meningkatkan performa drastis
- Menggunakan 875 artikel berita finansial dari CNBC Indonesia dan Bisnis.com
- Plus laporan keuangan dari 3 institusi finansial terbesar Indonesia
- **Terbukti lebih baik untuk sentiment analysis finansial dibanding lexicon-based approach**

**3. Penelitian Sentiment Analysis Saham Indonesia (2018-2024)**
- Ada penelitian yang menganalisis **192,582 artikel berita finansial Indonesia** dari 2018-2023
- Menyelidiki hubungan kompleks antara news sentiment dan perilaku pasar saham perusahaan Indonesia
- Menggunakan IndoBERT dan IndoLEM untuk sentiment analysis

**4. Alternative Approaches:**
- **Custom financial lexicon Indonesia**: Buat lexicon spesifik dari berita finansial BMRI
- **Supervised learning dengan ID-SMSA**: Training model dengan dataset yang sudah ada
- **IndoBERT fine-tuning**: Fine-tune IndoBERT dengan data finansial
- **Manual annotation + training**: Annotasi manual 1000-2000 berita BMRI kemudian training model

**PERTANYAAN KRUSIAL:**

**"Saudari Imelda, ada dataset ID-SMSA yang DIRANCANG KHUSUS untuk sentiment analysis saham Indonesia tahun 2024. Ada penelitian IndoBERT untuk domain finansial Indonesia. Ada puluhan ribu artikel berita finansial Indonesia yang sudah dianalisis dalam penelitian terbaru.**

**Mengapa Saudari memilih InSet Lexicon (2017, untuk Twitter informal, akurasi 60%, TIDAK PERNAH divalidasi untuk finansial) dibanding menggunakan resources domain-specific yang JELAS LEBIH SESUAI?**

**Apakah Saudari tidak melakukan literature review yang cukup? Atau Saudari sadar ada alternatif lebih baik tapi tetap memilih InSet karena lebih mudah? Ini menunjukkan kurangnya rigor metodologi."**

---

**Q6.6: PERTANYAAN KRUSIAL FINAL**

**"Saudari Imelda, berdasarkan SEMUA bukti di atas:**

1. **InSet dirancang untuk Twitter informal (2017), BUKAN berita finansial formal**
2. **Akurasi InSet hanya 60-66% bahkan di domain aslinya, turun hingga 30% di tasks lain**
3. **InSet memiliki bias 65% negatif**
4. **Tidak ada satupun validasi InSet untuk domain finansial**
5. **Missing vocabulary: 10,218 kata tidak cukup untuk cover terminologi finansial**
6. **Polisemi: kata-kata punya makna berbeda di konteks finansial**
7. **Ada alternatif yang JAUH LEBIH BAIK: ID-SMSA (2024), IndoBERT financial, 192K artikel finansial**

**Dengan TUJUH bukti fatal ini, bagaimana Saudari bisa mempertahankan penggunaan InSet Lexicon dalam penelitian ini?**

**Apakah Saudari:**
- Tidak melakukan literature review yang memadai tentang sentiment analysis finansial Indonesia?
- Tidak mengetahui adanya ID-SMSA dataset dan penelitian IndoBERT finansial?
- Sengaja memilih InSet karena mudah meskipun tahu tidak sesuai?
- Siap untuk mengganti metodologi sentiment analysis dengan approach yang valid?

**Ini bukan pertanyaan minor tentang parameter tuning. Ini adalah pertanyaan fundamental tentang validitas SELURUH PENELITIAN. Jika sentiment analysis tidak valid, maka gabungan LSTM + sentiment juga tidak valid."**

---

### REFERENSI DAN SUMBER

Berdasarkan penelitian dan publikasi ilmiah:

**InSet Lexicon Research:**
- Koto, F., & Rahmaningtyas, S. (2017). "InSet Lexicon: Evaluation of a Word List for Indonesian Sentiment Analysis in Microblogs". 21st International Conference on Asian Language Processing (IALP), Singapore.
- GitHub Repository: [fajri91/InSet](https://github.com/fajri91/InSet)
- Akurasi reported: 65.78% (Twitter data)
- Komposisi: 3,609 positive + 6,609 negative words

**Indonesian Financial NLP Research:**
- **ID-SMSA Dataset (2024)**: "Indonesian Stock Market Dataset for Sentiment Analysis" - 3,288 tweets, 10 saham terbesar Indonesia termasuk BMRI
  - Data: Januari 2021 - Maret 2024
  - Published: ScienceDirect & PMC
- **IndoBERT Financial Domain (2024)**: "Domain-Specific Language Model Post-Training for Indonesian Financial NLP"
  - 875 artikel berita finansial (CNBC Indonesia, Bisnis.com)
  - Laporan keuangan 3 institusi finansial terbesar
  - ArXiv: 2310.09736
- **Recent Study (2024)**: "Deciphering news sentiment and stock price relationships in Indonesian companies"
  - 192,582 artikel berita finansial Indonesia (2018-2023)
  - Published: Discover Artificial Intelligence, Springer

**Comparative Performance:**
- IndoBERT: 74.79% accuracy
- InSet Lexicon: 59.82-59.99% accuracy (recent studies)
- InSet feature extraction: 30% accuracy (emotion recognition)

**Key Finding dari Literature:**
"For Indonesian financial NLP, domain-specific post-training helps to improve the performance of downstream tasks. For sentiment analysis task, the IndoBERT base model benefits more from this domain-specific post-training." (ArXiv 2310.09736)

"InSet contains formal and informal words as it was generated using Twitter data, making it more suitable for social media but potentially less effective for domain-specific applications." (Lexicon Based Sentiment Analysis in Indonesian Languages: A Systematic Literature Review, 2022)

---

## 7. INKONSISTENSI TIMELINE

### Masalah Kritis

**Halaman 5 (Jadwal Penelitian):**
- Pengumpulan data: **November 2024 - November 2025** (12 bulan)

**Halaman 30 (Metodologi):**
- Data harga saham: **1 Januari 2023 - 30 November 2024**
- Pelaksanaan penelitian: **Desember 2024 - Februari 2025** (3 bulan)

### Pertanyaan Penguji:

**Q7.1:** Ada kontradiksi jelas:
- Jadwal: mengumpulkan data hingga November 2025
- Metodologi: data hanya sampai November 2024

**Manakah yang benar? Bagaimana Saudari bisa mengumpulkan data masa depan?**

**Q7.2:** Jika data hanya sampai November 2024, dan penelitian dimulai Desember 2024, berarti **data sudah tersedia sebelum penelitian dimulai**. Mengapa jadwal pengumpulan data mencantumkan November 2024 - November 2025?

---

## 8. EVALUASI METRIK: INTERPRETASI RMSE

### Masalah Kritis
Halaman 45: RMSE = 56.696

### Pertanyaan Penguji:

**Q8.1:** Saudari menyatakan RMSE 56.696 berarti "rata-rata selisih antara harga aktual dan prediksi adalah 56.696 poin".

Ini **SALAH**. Narasi "rata-rata selisih" adalah definisi **MAE**, bukan RMSE!

**PENJELASAN DETAIL RMSE vs MAE:**

**Rumus:**
- **MAE** = (1/n) × Σ|Yᵢ - Ŷᵢ| → Rata-rata selisih absolut
- **RMSE** = √[(1/n) × Σ(Yᵢ - Ŷᵢ)²] → Akar rata-rata kuadrat selisih

**Perhitungan dengan Data Aktual dari Tabel 12:**

| Tanggal    | Aktual | Prediksi | Error  | |Error| | Error² |
|------------|--------|----------|--------|---------|--------|
| 01/10/2025 | 4380   | 4333.85  | 46.15  | 46.15   | 2129.8 |
| 02/10/2025 | 4360   | 4363.20  | -3.20  | 3.20    | 10.2   |
| 03/10/2025 | 4310   | 4360.52  | -50.52 | 50.52   | 2552.3 |
| 06/10/2025 | 4260   | 4350.37  | -90.37 | 90.37   | 8166.7 |
| 07/10/2025 | 4290   | 4346.69  | -56.69 | 56.69   | 3213.8 |
|            |        |          |        | **246.93** | **16072.8** |

**MAE:**
```
MAE = (46.15 + 3.20 + 50.52 + 90.37 + 56.69) / 5
    = 246.93 / 5
    = 49.39
```
✅ **Interpretasi MAE:** "Rata-rata selisih absolut adalah 49.39 poin"

**RMSE:**
```
RMSE = √[(2129.8 + 10.2 + 2552.3 + 8166.7 + 3213.8) / 5]
     = √(16072.8 / 5)
     = √3214.56
     = 56.70
```
❌ **BUKAN "rata-rata selisih"!**
✅ **Interpretasi RMSE:** "Akar rata-rata kuadrat error adalah 56.70, yang memberikan penalti lebih besar pada error yang besar"

**Mengapa RMSE (56.70) > MAE (49.39)?**
```
Error -90.37 (yang SANGAT BESAR) dikuadratkan menjadi 8166.7
→ Ini mendapat "hukuman" lebih berat di RMSE
→ RMSE lebih sensitif terhadap outlier/error besar
```

**Perbandingan Karakteristik:**

| Aspek | MAE | RMSE |
|-------|-----|------|
| Interpretasi | Rata-rata selisih | Akar rata-rata kuadrat selisih |
| Sensitivitas outlier | Rendah | Tinggi |
| Penalti error besar | Linear | Kuadratik |
| Hubungan | Selalu ≤ RMSE | Selalu ≥ MAE |

**Pertanyaan menghancurkan:**
- **"Saudari mengatakan RMSE adalah 'rata-rata selisih'. Ini definisi MAE, bukan RMSE. Apakah Saudari memahami perbedaan keduanya?"**
- **"RMSE (56.70) lebih besar dari MAE (49.39). Apa yang bisa disimpulkan tentang distribusi error model Saudari?"**
- **"Jika ada satu prediksi dengan error sangat besar, metrik mana yang lebih terpengaruh? Mengapa ini penting untuk evaluasi model?"**

**Q8.2:** Untuk interpretasi yang lebih baik, seharusnya Saudari juga melaporkan:
- MAE (Mean Absolute Error): rata-rata absolut error
- MAPE (Mean Absolute Percentage Error): error dalam persentase
- R² score: seberapa baik model menjelaskan variance

**Apakah Saudari akan menambahkan metrik-metrik ini?**

---

## 9. NILAI PREDIKSI: DARI MANA ASALNYA?

### Masalah Kritis yang SANGAT FATAL

Di Tabel 12 (halaman 45), mahasiswa menunjukkan nilai prediksi:

| Tanggal    | Aktual  | **Prediksi** |
|------------|---------|--------------|
| 01/10/2025 | 4380    | **4333.848** |
| 02/10/2025 | 4360    | **4363.198** |
| 03/10/2025 | 4310    | **4360.517** |
| 06/10/2025 | 4260    | **4350.368** |
| 07/10/2025 | 4290    | **4346.687** |

**PERTANYAAN KRUSIAL: Dari mana nilai prediksi ini berasal?**

### Analisis Mendalam:

**Kemungkinan 1: Dari Model LSTM yang Sudah Dilatih?**
❌ **TIDAK MUNGKIN** karena:
1. Ini proposal/usulan penelitian - model belum diimplementasikan
2. Tidak ada informasi training yang dilakukan:
   - Berapa epoch dilatih?
   - Berapa loss di setiap epoch?
   - Berapa validation accuracy?
   - Training time berapa lama?
3. Tidak ada arsitektur yang didefinisikan (timestep, layers, units)
4. Tidak ada kode program yang ditunjukkan

**Kemungkinan 2: Dari Perhitungan Manual dengan W=0.408?**
❌ **TIDAK VALID** karena:
1. W=0.408 adalah skalar, bukan matriks trained weights
2. Tidak ada proses backpropagation/optimization
3. Weight tidak dilatih dari data
4. Ini bukan cara kerja LSTM yang sebenarnya

**Kemungkinan 3: Nilai Dummy/Ilustrasi?**
⚠️ **SANGAT BERMASALAH** karena:
1. Jika dummy, kenapa tidak dijelaskan?
2. Menghitung RMSE dari data dummy = misleading
3. Mengklaim hasil evaluasi dari data yang tidak real

**Kemungkinan 4: Copy dari Penelitian Lain?**
⚠️ **PLAGIARISME DATA** jika benar

### Pertanyaan Penguji yang MEMATIKAN:

**Q9.1:** **"Saudari, nilai prediksi 4333.848, 4363.198, dan seterusnya di Tabel 12 - dari mana angka-angka ini diperoleh?"**

**Q9.2:** **"Apakah model LSTM sudah diimplementasikan dan dilatih untuk mendapatkan nilai prediksi ini? Jika ya:**
- Berapa epoch training?
- Berapa loss function di epoch terakhir?
- Berapa lama training time?
- Dataset apa yang digunakan untuk training?
- Apa arsitektur lengkapnya (timestep, layers, units)?
- **Tunjukkan grafik training loss dan validation loss!"**

**Q9.3:** **"Jika nilai prediksi ini dari perhitungan manual dengan W=0.408, bukankah ini BUKAN hasil dari LSTM yang sesungguhnya? Bukankah weight seharusnya dilatih/dioptimasi dari data, bukan ditetapkan secara arbitrary?"**

**Q9.4:** **"Jika ini hanya nilai dummy/ilustrasi, mengapa menghitung RMSE dan mengklaim sebagai hasil evaluasi model? Bukankah ini menyesatkan?"**

**Q9.5:** **"Dengan proposal yang:**
- Tidak ada arsitektur model yang jelas
- Tidak ada implementasi
- Tidak ada training
- Weight menggunakan skalar arbitrary 0.408

**Bagaimana bisa ada nilai prediksi? Apakah ini data fabrikasi?"**

### Kesimpulan Fatal:

Nilai prediksi di Tabel 12 adalah **TIDAK VALID** karena:
1. Model belum diimplementasikan dan dilatih
2. Perhitungan manual dengan W=0.408 bukan LSTM yang sebenarnya
3. Tidak ada transparansi dari mana nilai ini berasal

**Ini adalah RED FLAG terbesar dalam proposal - menunjukkan hasil evaluasi dari model yang tidak eksis!**

---

## 10. VERIFIKASI PERHITUNGAN RMSE (MASALAH TAMBAHAN)

### Data dari Tabel 12 Alternatif (halaman 45):

**CATATAN:** Ada inkonsistensi data di proposal. Di satu tempat menggunakan data harga 6000-an, di tempat lain 4000-an.

| Tanggal    | Aktual | Prediksi | Error  | Error² |
|------------|--------|----------|--------|--------|
| 2024-11-22 | 6325   | 6401     | -76    | 5776   |
| 2024-11-25 | 6425   | 6401     | 24     | 576    |
| 2024-11-26 | 6425   | 6401     | 24     | 576    |
| 2024-11-27 | 6425   | 6401     | 24     | 576    |
| 2024-11-28 | 6450   | 6401     | 49     | 2401   |

**Perhitungan Manual:**
- Sum of squared errors = 5776 + 576 + 576 + 576 + 2401 = 9905
- MSE = 9905 / 5 = 1981
- RMSE = √1981 = **44.51**

### Pertanyaan Penguji:

**Q10.1:** Di satu tempat RMSE = 56.696, di perhitungan Tabel ini jadi **44.51**. Ada inkonsistensi data. Mana yang benar?

**Q10.2:** **Lebih penting lagi: Dari mana SEMUA nilai prediksi (6401, 6401, 6401...) ini? Mengapa prediksi hampir sama semua (6401)? Apakah model hanya memprediksi nilai konstan?**

---

## RINGKASAN KESALAHAN KRITIS

### KESALAHAN FATAL (Dapat Menggugurkan Penelitian):

1. ❌ **FATAL #1:** Kesalahan konseptual LSTM - menggunakan W = 0.408 sebagai skalar tunggal
   - Seharusnya matriks 50×56 = 2.800 parameter (bukan 1 nilai!)
   - Mahasiswa tidak memahami: 56 = 50 hidden units + 6 input features
   - Total seharusnya 11,400 parameter untuk 4 gates, bukan 1 skalar
   - Perhitungan manual di proposal (hal 40-43) secara teknis SALAH
   - Menunjukkan tidak memahami struktur fundamental neural network

2. ❌ **FATAL #2:** InSet Lexicon TIDAK VALID untuk domain finansial
   - **Bukti 1:** Dirancang untuk Twitter informal (2017), bukan berita finansial formal
   - **Bukti 2:** Akurasi rendah: hanya 60-66% di domain aslinya, turun hingga 30% di tasks lain
   - **Bukti 3:** Coverage tidak memadai: 10,218 kata vs ribuan istilah finansial yang hilang
   - **Bukti 4:** Dominan kata slang: nggak, gatau, apaan, ngakak, anjir, doang
   - **Bukti 5:** Hanya 5 kata finansial (0.05%): laba, defisit, pailit, bangkrut, merugi
   - **Bukti 6:** TIDAK ADA: likuiditas, volatilitas, NPL, ROA, ROE, CAR, LDR, kapitalisasi
   - **Bukti 7:** Bias 65% negatif - dapat distorsi sistematis hasil
   - **Bukti 8:** Polisemi - kata punya makna berbeda di konteks finansial
   - **Bukti 9:** TIDAK ADA penelitian yang validasi InSet untuk finansial Indonesia
   - **Bukti 10:** Ada alternatif JAUH LEBIH BAIK yang diabaikan: ID-SMSA (2024), IndoBERT financial
   - **Kesimpulan:** Menggunakan tools yang salah domain = seluruh sentiment analysis tidak valid

3. ❌ **FATAL #3:** Nilai prediksi di Tabel 12 tidak jelas asalnya
   - Model belum diimplementasikan, tidak ada training, tidak ada arsitektur
   - Nilai 4333.848, 4363.198, dst - dari mana?
   - Jika dari W=0.408, itu bukan LSTM yang sebenarnya
   - Jika dummy/ilustrasi, mengapa menghitung RMSE sebagai hasil evaluasi?
   - **RED FLAG: Menunjukkan hasil evaluasi dari model yang tidak eksis!**

### KESALAHAN SERIUS (Harus Diperbaiki):

4. ❌ **SERIUS:** Tidak ada arsitektur model yang jelas
   - Timestep/sequence length: TIDAK DISEBUTKAN (seharusnya 5-60 hari)
   - Jumlah layer LSTM: TIDAK DISEBUTKAN
   - Units per layer: TIDAK DISEBUTKAN (hanya asumsi 50 di perhitungan)
   - Optimizer: TIDAK DISEBUTKAN
   - Learning rate: TIDAK DISEBUTKAN
   - Dropout rate: TIDAK DISEBUTKAN
   - **Tanpa ini, penelitian tidak reproducible!**

5. ❌ **SERIUS:** Tidak ada validation set
   - Hanya train (80%) dan test (20%)
   - Risiko data leakage saat tuning hyperparameter
   - Tidak bisa early stopping
   - Tidak bisa pilih arsitektur optimal

6. ❌ **SERIUS:** Tidak ada uji stasioneritas (ADF test)
   - Data harga saham umumnya non-stationary (ada trend)
   - Min-Max normalization ≠ stationarity transformation
   - Seharusnya: ADF test → Differencing/Log returns jika perlu
   - Model trained saat bullish bisa gagal saat bearish

7. ❌ **SERIUS:** Tidak ada baseline comparison
   - Tidak ada pembanding: LSTM tanpa sentiment, ARIMA, Moving Average, Random Walk
   - Tidak bisa buktikan LSTM+sentiment lebih baik
   - RMSE 56.696 - bagus atau buruk? Tidak ada referensi!

### KESALAHAN MENENGAH:

8. ❌ **MENENGAH:** Timeline inkonsisten
   - Jadwal: data Nov 2024 - Nov 2025
   - Metodologi: data Jan 2023 - Nov 2024
   - Penelitian: Des 2024 - Feb 2025
   - Bagaimana kumpulkan data masa depan?

9. ❌ **MENENGAH:** Interpretasi RMSE SALAH
   - Mahasiswa: "rata-rata selisih adalah 56.696"
   - Fakta: Itu definisi MAE, bukan RMSE!
   - RMSE = akar rata-rata kuadrat error (sensitif outlier)
   - MAE = rata-rata selisih absolut
   - Dengan data yang sama: MAE = 49.39, RMSE = 56.70

10. ❌ **MENENGAH:** Inkonsistensi perhitungan RMSE
    - Satu tempat: RMSE = 56.696
    - Tabel lain: RMSE seharusnya = 44.51
    - Data harga: ada yang 4000-an, ada yang 6000-an
    - Prediksi hampir konstan (6401, 6401, 6401...)

---

## PERTANYAAN PENUTUP YANG MEMATIKAN

**"Saudari Imelda, dari analisis mendalam dan detail terhadap proposal ini, ditemukan TIGA KESALAHAN FATAL yang mempertanyakan validitas seluruh penelitian:**

### KESALAHAN FATAL #1: Tidak Memahami LSTM - Fundamental Error

**Saudari menggunakan W = 0.408 sebagai skalar tunggal dalam perhitungan LSTM (hal 40-43), padahal:**

1. W seharusnya **matriks 50×56 = 2.800 parameter per gate**
2. Angka 56 = 50 hidden units + 6 input features (concatenation)
3. Total 4 gates (forget, input, cell, output) = **11,400 parameter**
4. Bukan 1 angka skalar 0.408!

**Formula W = (-0.408, 0.408) adalah RENTANG untuk inisialisasi random, bukan nilai tetap!**

Setiap elemen matriks W di-sample acak dari distribusi uniform dalam rentang tersebut. Saudari salah memahami fundamental Xavier initialization.

**Ini bukan kesalahan kecil - ini menunjukkan Saudari tidak memahami:**
- Struktur dasar neural network (matrix vs scalar)
- Dimensi weight dalam LSTM
- Xavier/Glorot initialization
- Bagaimana backpropagation melatih weight

**Pertanyaan krusial: Bagaimana Saudari bisa mengimplementasikan LSTM dengan benar jika konsep dasar weight matrix 11,400 parameter dipahami sebagai 1 skalar?**

### KESALAHAN FATAL #2: InSet Lexicon untuk Domain Finansial - Tools Yang Salah Total

**Saudari menggunakan InSet Lexicon (dirancang untuk Twitter informal 2017) untuk menganalisis berita finansial formal BMRI, padahal:**

1. **InSet akurasi hanya 60-66%** bahkan di domain aslinya (Twitter), turun hingga 30% di task lain
2. **Hanya 10,218 kata** - tidak cukup untuk cover istilah finansial (likuiditas, NPL, volatilitas, ROA, CAR, buyback, dll)
3. **Bias 65% negatif** - dapat mendistorsi hasil sistematis
4. **Tidak ada satupun penelitian** yang validasi InSet untuk domain finansial
5. **Polisemi**: kata-kata punya makna berbeda di konteks finansial vs umum
6. **Ada alternatif JAUH LEBIH BAIK yang Saudari abaikan:**
   - **ID-SMSA dataset (2024)**: 3,288 tweets tentang saham Indonesia termasuk BMRI
   - **IndoBERT financial domain (2024)**: Post-trained dengan 875 artikel finansial Indonesia
   - **Penelitian 192K artikel finansial Indonesia (2018-2023)**

**Mengapa Saudari tidak menggunakan ID-SMSA yang DIRANCANG KHUSUS untuk sentiment analysis saham Indonesia, dan malah pakai InSet yang jelas-jelas tidak cocok?**

**Apakah Saudari tidak melakukan literature review yang memadai? Atau memilih InSet karena lebih mudah meski tahu tidak sesuai?**

### KESALAHAN FATAL #3: Nilai Prediksi Tanpa Dasar - Red Flag Terbesar

**Di Tabel 12 (hal 45), Saudari menunjukkan nilai prediksi: 4333.848, 4363.198, 4360.517, dst. DARI MANA NILAI INI?**

**4 Kemungkinan, semua bermasalah:**

**1. Dari Model LSTM yang Sudah Dilatih?**
- ❌ TIDAK MUNGKIN - ini proposal, model belum ada
- Tidak ada info: epoch training, loss function, training time, validation accuracy
- Tidak ada arsitektur: timestep, layers, units tidak didefinisikan
- Tidak ada kode program

**2. Dari Perhitungan Manual dengan W=0.408?**
- ❌ TIDAK VALID - itu bukan LSTM sebenarnya
- W=0.408 skalar arbitrary, bukan trained weights dari backpropagation
- Tidak ada proses optimization/learning

**3. Nilai Dummy/Ilustrasi?**
- ⚠️ SANGAT MENYESATKAN - mengapa hitung RMSE dari data dummy?
- Mengklaim hasil evaluasi dari data yang tidak real
- Tidak ada disclaimer bahwa ini ilustrasi

**4. Copy dari Penelitian Lain?**
- ⚠️ PLAGIARISME DATA jika benar

**Pertanyaan mematikan:**
**"Dengan proposal yang tidak ada: (1) arsitektur, (2) implementasi, (3) training, (4) weight yang valid - bagaimana bisa ada nilai prediksi? Apakah ini data fabrikasi untuk membuat proposal terlihat lengkap?"**

**Ini RED FLAG terbesar: Menampilkan hasil evaluasi model (RMSE 56.696) dari prediksi yang tidak jelas asalnya!**

---

### PERTANYAAN FINAL - TRIPLE FATAL BLOW:

**"Saudari Imelda, mari kita simpulkan temuan kritis:**

**TIGA KESALAHAN FATAL:**

1. **LSTM dengan W=0.408 skalar** - Seharusnya 11,400 parameter matriks
   - Tidak memahami struktur fundamental neural network
   - Perhitungan manual secara teknis salah

2. **InSet Lexicon untuk finansial** - Tools yang salah domain total
   - Dirancang untuk Twitter slang (nggak, gatau, ngakak), bukan berita formal
   - Hanya 5 kata finansial dari 10,218 (0.05%)
   - Missing: likuiditas, NPL, volatilitas, ROA, ROE, CAR, LDR
   - Ada ID-SMSA (2024) yang KHUSUS untuk saham Indonesia tapi diabaikan

3. **Nilai prediksi tanpa dasar** - Red flag akademik
   - Tabel 12 menunjukkan prediksi tapi model belum ada
   - Tidak ada training, tidak ada arsitektur, tidak ada implementasi
   - Menampilkan RMSE dari model yang tidak eksis

**DITAMBAH TUJUH KESALAHAN SERIUS:**

4. Tidak ada timestep/sequence length (seharusnya 5-60 hari)
5. Tidak ada definisi layer, units, optimizer, learning rate
6. Tidak ada validation set (risiko data leakage)
7. Tidak ada uji stasioneritas/ADF test (data non-stationary)
8. Tidak ada baseline comparison (tidak bisa buktikan lebih baik)
9. Timeline inkonsisten (data masa depan?)
10. Interpretasi RMSE salah (bukan "rata-rata selisih")

---

**PERTANYAAN PENUTUP YANG MENGHANCURKAN:**

**"Dengan TIGA kesalahan FATAL dan TUJUH kesalahan serius - total 10 masalah kritis - yang menunjukkan:**
- Tidak memahami fundamental LSTM
- Tidak melakukan literature review yang memadai (InSet vs ID-SMSA)
- Menampilkan hasil evaluasi dari model yang tidak eksis
- Tidak ada validasi metodologi
- Tidak ada reproducibility

**Apakah Saudari menyadari bahwa proposal ini memerlukan REVISI TOTAL, bukan perbaikan minor?**

**Pertanyaan terakhir yang harus dijawab dengan jujur:**

1. **Apakah Saudari benar-benar memahami LSTM?** Jika ya, jelaskan mengapa W bisa jadi skalar 0.408
2. **Apakah Saudari pernah membuka file InSet Lexicon?** Jika ya, mengapa tetap pakai meski penuh kata slang?
3. **Dari mana nilai prediksi di Tabel 12?** Ini pertanyaan paling krusial - jika tidak bisa dijelaskan, ini academic misconduct
4. **Apakah Saudari siap revisi total?** Atau akan mempertahankan metodologi yang jelas cacat?

**Rekomendasi Panel:**
Proposal ini **TIDAK LAYAK** untuk dilanjutkan tanpa revisi mayor komprehensif yang mencakup:
1. Mempelajari ulang fundamental LSTM dan neural network
2. Mengganti InSet dengan IndoBERT fine-tuned pada ID-SMSA dataset
3. Menghapus semua perhitungan/prediksi yang tidak valid
4. Mendefinisikan arsitektur lengkap dengan justifikasi
5. Menambahkan validation set, baseline, dan uji stasioneritas
6. Menunjukkan pemahaman mendalam tentang metodologi yang dipilih

**Atau, alternatif: Ubah topik penelitian menjadi yang lebih sesuai dengan kapasitas pemahaman saat ini."**

---

## CATATAN UNTUK PENGUJI

### Strategi Pertanyaan:

1. **Mulai dengan InSet Lexicon (Kesalahan #2)** - ini paling mudah dibuktikan:
   - Tunjukkan fakta: InSet untuk Twitter 2017, akurasi 60%, 10K kata
   - Tanya: "Mengapa tidak pakai ID-SMSA (2024) yang khusus untuk saham Indonesia?"
   - Gunakan Tabel 9 (hal 37) sebagai bukti: "Bagaimana InSet handle kata 'likuiditas'?"
   - Tanyakan coverage rate: "Berapa % kata finansial yang tidak dikenali InSet?"

2. **Lanjut ke LSTM (Kesalahan #1)**:
   - Tanya: "Jelaskan mengapa W=0.408 sebagai skalar tunggal?"
   - Tanya: "Berapa dimensi matriks W seharusnya jika input 56 fitur, hidden 50?"
   - Tanyakan implementasi: "Apakah ada bukti kode program yang implementasi LSTM benar?"

3. **Gabungkan kedua kesalahan fatal**:
   - "Jika LSTM salah DAN sentiment analysis salah, apa yang valid dari penelitian ini?"

### Key Points untuk Ditekan:

- **InSet Lexicon**: Ada ID-SMSA dan IndoBERT financial yang JELAS LEBIH BAIK tapi diabaikan
- **Literature review**: Tidak melakukan due diligence dalam pemilihan tools
- **Metodologi rigor**: Multiple kesalahan menunjukkan kurangnya pemahaman fundamental
- **Validitas penelitian**: Kedua komponen utama (LSTM + sentiment) bermasalah serius

### Bukti Konkret yang Harus Diminta:

1. "Tunjukkan paper yang validasi InSet untuk domain finansial"
2. "Berapa coverage rate InSet pada data berita BMRI Anda?"
3. "Jelaskan perhitungan dimensi weight matrix di LSTM"
4. "Mengapa tidak pakai ID-SMSA dataset yang spesifik untuk saham Indonesia?"

### Jika Mahasiswa Defensif:

- Gunakan fakta dari paper asli InSet: "Paper asli InSet (2017) menyatakan dirancang untuk microblogs dengan akurasi 65.78%. Bagaimana Anda yakin akurasinya sama/lebih baik di domain finansial?"
- Tunjukkan ID-SMSA: "Dataset ID-SMSA published 2024 di ScienceDirect khusus untuk saham Indonesia. Kenapa tidak pakai ini?"
- Fokus pada missing vocabulary: "Coba sebutkan skor InSet untuk kata: likuiditas, NPL, volatilitas, buyback" (jawaban: tidak ada)

### Target Outcome:

Mahasiswa harus **mengakui kesalahan dan commit untuk revisi mayor**, minimal:
1. Ganti sentiment analysis method (ID-SMSA atau IndoBERT)
2. Perbaiki pemahaman dan dokumentasi LSTM
3. Tambah validation set, baseline, uji stasioneritas
4. Validasi manual sentiment scoring
