# CATATAN REVISI PROPOSAL SKRIPSI

**Nama:** MUHAMMAD RIZKI
**NIM:** F1E122140
**Judul:** Pengembangan Model Federated Learning dengan Autoencoder untuk Deteksi Anomali Data Sensor IoT Pertanian Tomat
**Tanggal Review:** 4 Februari 2026

---

## A. DAFTAR KESALAHAN KETIK (TYPOS)

### 1. Typo "Pyhton" (hal. 20)

| Halaman | Kesalahan | Seharusnya |
|---------|-----------|------------|
| 20 | "Bahasa Pemrograman **Pyhton** 3.10.0" | "Bahasa Pemrograman **Python** 3.10.0" |

---

### 2. Typo "milliar" (hal. 1)

| Halaman | Kesalahan | Seharusnya |
|---------|-----------|------------|
| 1 | "...mencapai hingga 40 **milliar** unit..." | "...mencapai hingga 40 **miliar** unit..." |

**Catatan:** Dalam Bahasa Indonesia, kata yang benar adalah "miliar" (bukan "milliar" atau "milyar").

---

### 3. Typo "meberkan" (hal. 3)

| Halaman | Kesalahan | Seharusnya |
|---------|-----------|------------|
| 3 | "...federated learning mampu **meberkan** hasil..." | "...federated learning mampu **memberikan** hasil..." |

---

### 4. Typo "Pendekatanini" - Spasi Hilang (hal. 8)

| Halaman | Kesalahan | Seharusnya |
|---------|-----------|------------|
| 8 | "...**Pendekatanini** tidak hanya..." | "...**Pendekatan ini** tidak hanya..." |

---

### 5. Typo "Temprature" (BANYAK LOKASI)

Kata "Temperature" salah ketik menjadi "Temprature" di banyak tempat:

| Halaman | Lokasi |
|---------|--------|
| 30 | Tabel 6 - Pembagian data |
| 33 | Tabel Model Summary |
| 41 | Tabel 8 - Threshold Final Parameter |
| 42 | Tabel 9 - Threshold Anomaly |

**Perbaikan:** Gunakan **Find & Replace** untuk mengganti semua "Temprature" menjadi "Temperature".

---

### 6. Typo "terseut" (hal. 29)

| Halaman | Kesalahan | Seharusnya |
|---------|-----------|------------|
| 29 | "standar deviasi fitur **terseut**" | "standar deviasi fitur **tersebut**" |

---

### 7. Typo "Recontrucstion" dan "Recontruction"

Kata "Reconstruction" salah ketik di beberapa tempat:

| Halaman | Kesalahan | Seharusnya |
|---------|-----------|------------|
| 23 (Tabel 3) | "**Recontrucstion** error model" | "**Reconstruction** error model" |
| 38 (3.8.1) | "Threshold **Recontruction** Error" | "Threshold **Reconstruction** Error" |
| 44 (3.9.1) | "Predict **Recontruction**" | "Predict **Reconstruction**" |
| 45 (3.9.2) | "**Recontruction** Error" | "**Reconstruction** Error" |

---

### 8. Typo "degan" (hal. 3)

| Halaman | Kesalahan | Seharusnya |
|---------|-----------|------------|
| 3 | "penggabungan autoencoder **degan** federated learning" | "penggabungan autoencoder **dengan** federated learning" |

---

### 9. Penulisan "di gunakan" Terpisah

Dalam Bahasa Indonesia, "digunakan" sebagai kata kerja pasif ditulis menyatu:

| Halaman | Kesalahan | Seharusnya |
|---------|-----------|------------|
| 20 | "Alat yang **di gunakan** dalam penelitian" | "Alat yang **digunakan** dalam penelitian" |
| 29 | "Fitur yang **di gunakan** yaitu" | "Fitur yang **digunakan** yaitu" |
| 46 | "rumus MSE yang **di gunakan** pada penelitian" | "rumus MSE yang **digunakan** pada penelitian" |

---

## B. KESALAHAN FORMAT DAN REFERENSI

### 10. Format Referensi FedAvg Tidak Standar

| Halaman | Kesalahan | Seharusnya |
|---------|-----------|------------|
| 14 | "(Brendan McMahan Eider Moore Daniel Ramage Seth Hampson Blaise AgüeraAg & Arcas, 2017)" | "(McMahan et al., 2017)" |

**Catatan:** Referensi asli adalah:
> McMahan, H. B., Moore, E., Ramage, D., Hampson, S., & Arcas, B. A. (2017). Communication-Efficient Learning of Deep Networks from Decentralized Data. *AISTATS 2017*.

Paper ini tersedia di: https://arxiv.org/abs/1602.05629

---

### 11. Inkonsistensi Tahun Dataset Belli et al.

| Lokasi | Tahun yang Ditulis |
|--------|-------------------|
| hal. 5 (Batasan Masalah) | Belli et al., **2024** |
| hal. 20-21 (Jenis dan Sumber Data) | Belli et al., **2025** |
| Daftar Pustaka | Belli et al., **2025** |

**Verifikasi:** Dataset Mendeley "IoT-based Dataset of a Tomato Cultivation Under Different Irrigation Regimes" dipublikasikan November 2024 (Version 2), dan paper Data in Brief dipublikasikan 2025.

**Rekomendasi:** Konsistenkan menjadi Belli et al. (2025) sesuai publikasi Data in Brief, atau Belli et al. (2024) jika merujuk versi dataset.

---

### 12. Daftar Pustaka - Format DOI Tidak Konsisten

Beberapa entri menggunakan format DOI berbeda:

| Format | Contoh |
|--------|--------|
| `https://doi.org/...` | Sebagian besar entri |
| URL langsung tanpa DOI | Beberapa entri arXiv |

**Rekomendasi:** Konsistenkan semua referensi dengan format standar APA 7th Edition.

---

## C. KESALAHAN KONSEPTUAL DAN PERTANYAAN SIDANG

### PERTANYAAN 1: Federated Rounds

**Konteks (hal. 5):**
> "Model Federated Learning pada penelitian ini dibatasi pada penggunaan 3 klien, **1 federated rounds**, dan metode agregasi FedAvg"

**Pertanyaan:**
"Mengapa hanya menggunakan 1 federated round? Bagaimana Anda memastikan model sudah konvergen dengan hanya 1 round agregasi?"

**Jawaban Ideal:**
- Dalam FL standar, diperlukan beberapa rounds (biasanya 10-100+) untuk mencapai konvergensi
- Dengan 1 round, model global hanya merupakan rata-rata bobot awal setelah 1x pelatihan lokal
- Justifikasi yang dapat diterima: eksperimen awal, keterbatasan waktu/sumber daya
- Sebaiknya tambahkan eksperimen dengan variasi rounds (1, 5, 10, 20) untuk melihat efek konvergensi

**Referensi:** McMahan et al. (2017) menggunakan 100-1000 rounds dalam eksperimen mereka.

---

### PERTANYAAN 2: Three-Sigma Rule dan Asumsi Normalitas

**Konteks (hal. 39-40):**
> "Pada penelitian ini digunakan nilai konstanta k = 3 dalam penentuan threshold reconstruction error. Pemilihan nilai tersebut didasarkan pada prinsip **three-sigma rule**..."

**Pertanyaan:**
"Three-sigma rule mengasumsikan data berdistribusi normal. Apakah Anda sudah memverifikasi bahwa reconstruction error mengikuti distribusi normal? Bagaimana jika distribusinya skewed?"

**Jawaban Ideal:**
- Perlu dilakukan uji normalitas (Shapiro-Wilk, Kolmogorov-Smirnov) pada reconstruction error
- Jika tidak normal, alternatif threshold:
  - Persentil (95th atau 99th percentile)
  - IQR method: Q3 + 1.5*IQR
  - MAD (Median Absolute Deviation): median + 3*MAD
- Visualisasi distribusi error dengan histogram/Q-Q plot

---

### PERTANYAAN 3: Non-IID Data Handling

**Konteks (hal. 4):**
> "...model ini diharapkan mampu beradaptasi dengan karakteristik data sensor irigasi tomat yang bersifat **tidak terpusat (non-IID)**, dinamis, dan heterogen..."

**Pertanyaan:**
"Anda menyebutkan data bersifat non-IID, tetapi dalam metodologi tidak ada penanganan khusus untuk non-IID. Bagaimana FedAvg menangani ketika distribusi data antar klien sangat berbeda?"

**Jawaban Ideal:**
- FedAvg standar memang memiliki kelemahan pada data non-IID yang ekstrem
- Alternatif yang lebih robust:
  - **FedProx**: Menambahkan proximal term untuk regularisasi
  - **SCAFFOLD**: Menggunakan control variates untuk koreksi drift
  - **FedNova**: Normalisasi berdasarkan jumlah local steps
- Dalam penelitian ini, non-IID terjadi karena perbedaan level irigasi (100%, 60%, 30%)
- Rekomendasi: Bandingkan performa FedAvg vs FedProx

---

### PERTANYAAN 4: Hyperparameter Autoencoder

**Konteks (hal. 33):**
Model autoencoder hanya menampilkan arsitektur (3→8→4→8→3), tanpa detail hyperparameter training.

**Pertanyaan:**
"Hyperparameter apa yang digunakan untuk melatih autoencoder? Berapa learning rate, jumlah epoch, batch size, dan optimizer yang digunakan?"

**Jawaban Ideal:**
Hyperparameter standar untuk autoencoder anomaly detection:

```python
# Contoh konfigurasi
model.compile(
    optimizer=Adam(learning_rate=1e-3),  # atau 1e-4
    loss='mse'
)

model.fit(
    X_train,
    X_train,  # autoencoder: input = output
    epochs=50-100,
    batch_size=32-64,
    validation_split=0.1,
    callbacks=[EarlyStopping(patience=10)]
)
```

**Rekomendasi:** Tambahkan tabel hyperparameter dan justifikasi pemilihannya.

---

### PERTANYAAN 5: Evaluasi dengan Ground Truth

**Konteks (hal. 48):**
> "Meskipun model dikembangkan dengan pendekatan **unsupervised learning**, proses evaluasi dilakukan secara **supervised** dengan memanfaatkan label fisiologis sebagai ground truth..."

**Pertanyaan:**
"Bagaimana Anda menghasilkan ground truth label fisiologis? Apakah label ini dibuat secara manual berdasarkan threshold yang Anda tentukan sendiri? Bukankah ini berarti Anda mengevaluasi model dengan kriteria yang Anda buat sendiri?"

**Jawaban Ideal:**
- Ground truth berbasis threshold fisiologis memang bersifat **semi-synthetic**
- Untuk validasi yang lebih kuat:
  1. Bandingkan dengan dataset anomaly detection benchmark yang sudah memiliki label
  2. Injeksi anomali sintetis (synthetic anomaly injection) dengan jenis yang diketahui
  3. Validasi oleh domain expert (agronomist)
- Alternatif evaluasi unsupervised:
  - Silhouette score untuk clustering quality
  - Reconstruction error distribution analysis

---

### PERTANYAAN 6: Skalabilitas 3 Klien

**Konteks (hal. 5):**
> "Model Federated Learning pada penelitian ini dibatasi pada penggunaan **3 klien**..."

**Pertanyaan:**
"Dengan hanya 3 klien, apakah hasil penelitian ini dapat digeneralisasi untuk skenario FL yang lebih besar? Apa tantangan yang mungkin muncul jika jumlah klien ditingkatkan menjadi 10, 50, atau 100?"

**Jawaban Ideal:**
- Tantangan skalabilitas:
  - **Communication overhead**: Lebih banyak klien = lebih banyak parameter yang dikirim
  - **Stragglers**: Klien lambat dapat menghambat keseluruhan proses
  - **Heterogeneity**: Lebih beragam kemampuan komputasi
  - **Non-IID severity**: Distribusi data makin beragam
- Flower framework mendukung simulasi hingga jutaan klien
- Rekomendasi: Tambahkan eksperimen dengan variasi jumlah klien

---

### PERTANYAAN 7: Metrik Evaluasi

**Konteks (hal. 49-50):**
Evaluasi hanya menggunakan Precision, Recall, F1-Score.

**Pertanyaan:**
"Mengapa tidak menggunakan metrik seperti AUC-ROC atau Average Precision yang lebih cocok untuk masalah deteksi anomali dengan class imbalance?"

**Jawaban Ideal:**
- Deteksi anomali biasanya memiliki class imbalance (anomali << normal)
- Metrik tambahan yang disarankan:
  - **AUC-ROC**: Area Under ROC Curve
  - **AUC-PR**: Area Under Precision-Recall Curve (lebih informatif untuk imbalanced data)
  - **Matthews Correlation Coefficient (MCC)**
- Visualisasi threshold trade-off dengan ROC curve

---

### PERTANYAAN 8: Perbandingan dengan Baseline

**Konteks:** Tidak ada perbandingan dengan metode deteksi anomali lain.

**Pertanyaan:**
"Bagaimana performa model FL-Autoencoder Anda dibandingkan dengan metode deteksi anomali lain seperti Isolation Forest, One-Class SVM, atau LSTM-Autoencoder tanpa FL?"

**Jawaban Ideal:**
Baseline yang sebaiknya dibandingkan:
1. **Centralized Autoencoder**: Semua data digabung, dilatih di satu tempat
2. **Isolation Forest**: Tree-based anomaly detection
3. **One-Class SVM**: Support vector approach
4. **Local-only model**: Setiap klien hanya pakai model lokalnya

Perbandingan ini penting untuk membuktikan added value dari pendekatan FL.

---

### PERTANYAAN 9: Privacy Guarantee

**Konteks (hal. 3):**
> "...menjaga privasi data petani serta efisiensi komunikasi..."

**Pertanyaan:**
"FL memang tidak mengirim data mentah, tetapi penelitian terbaru menunjukkan bahwa gradient/weight juga bisa di-reverse engineer untuk mengekstrak data asli (gradient inversion attack). Apakah Anda mempertimbangkan mekanisme privasi tambahan seperti Differential Privacy?"

**Jawaban Ideal:**
- Gradient inversion attack memang menjadi concern di FL
- Mekanisme tambahan untuk privasi:
  - **Differential Privacy (DP)**: Menambahkan noise pada gradient
  - **Secure Aggregation**: Enkripsi gradient sebelum dikirim
  - **Gradient Compression**: Mengurangi informasi yang dikirim
- Untuk penelitian ini, bisa ditambahkan sebagai future work

---

### PERTANYAAN 10: Interpretasi Reconstruction Error

**Konteks (hal. 45-46):**
MSE dihitung per baris dengan 3 fitur (EC, Humidity, Temperature).

**Pertanyaan:**
"Ketika model mendeteksi anomali berdasarkan MSE tinggi, bagaimana Anda mengetahui fitur mana yang menyebabkan anomali? Apakah EC, Humidity, atau Temperature?"

**Jawaban Ideal:**
- MSE agregat memang tidak menunjukkan fitur penyebab
- Solusi untuk interpretability:
  1. Hitung error per fitur: `error_ec`, `error_humidity`, `error_temp`
  2. Feature contribution analysis
  3. Visualisasi dengan radar chart per observasi
- Ini penting untuk actionable insights bagi petani

---

## D. CHECKLIST REVISI

### Kesalahan Ketik:
- [ ] Perbaiki "Pyhton" → "Python" (hal. 20)
- [ ] Perbaiki "milliar" → "miliar" (hal. 1)
- [ ] Perbaiki "meberkan" → "memberikan" (hal. 3)
- [ ] Perbaiki "Pendekatanini" → "Pendekatan ini" (hal. 8)
- [ ] Perbaiki semua "Temprature" → "Temperature" (4+ lokasi)
- [ ] Perbaiki "terseut" → "tersebut" (hal. 29)
- [ ] Perbaiki semua "Recontruction/Recontrucstion" → "Reconstruction" (4+ lokasi)
- [ ] Perbaiki "degan" → "dengan" (hal. 3)
- [ ] Perbaiki "di gunakan" → "digunakan" (3+ lokasi)

### Format dan Referensi:
- [ ] Perbaiki format referensi McMahan et al. (2017)
- [ ] Konsistenkan tahun dataset Belli et al. (2024 atau 2025)
- [ ] Konsistenkan format DOI di daftar pustaka

### Metodologi (Opsional - Untuk Perbaikan):
- [ ] Tambahkan justifikasi penggunaan 1 federated round
- [ ] Tambahkan uji normalitas untuk reconstruction error
- [ ] Tambahkan tabel hyperparameter autoencoder
- [ ] Pertimbangkan penambahan metrik AUC-ROC/AUC-PR

---

## E. RINGKASAN TEMUAN

| Kategori | Jumlah |
|----------|--------|
| Kesalahan ketik unik | 9 jenis |
| Total lokasi typo | 15+ lokasi |
| Inkonsistensi referensi | 2 |
| Pertanyaan konseptual | 10 |

---

## F. REFERENSI TERVERIFIKASI

| Referensi | Status | Sumber Verifikasi |
|-----------|--------|-------------------|
| McMahan et al. (2017) - FedAvg | VALID | [arXiv](https://arxiv.org/abs/1602.05629), [AISTATS 2017](https://proceedings.mlr.press/v54/mcmahan17a.html) |
| Belli et al. (2024/2025) - Dataset | VALID | [Mendeley Data](https://data.mendeley.com/datasets/35wh56287y/2), [Data in Brief](https://www.sciencedirect.com/science/article/pii/S2352340925002537) |
| Flower Framework | VALID | [flower.ai](https://flower.ai/), [arXiv](https://arxiv.org/abs/2007.14390) |

---

**Catatan:** Dokumen ini dibuat untuk membantu mahasiswa dalam proses revisi proposal skripsi.
