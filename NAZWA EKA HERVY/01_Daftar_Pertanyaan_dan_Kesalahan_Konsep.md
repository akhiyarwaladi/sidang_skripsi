# DAFTAR PERTANYAAN PENGUJI & KESALAHAN KONSEP
## Proposal: Pemodelan K-Means Clustering untuk Eksplorasi Pola Distribusi Kinerja Tri Dharma Dosen Berdasarkan Data BKD di Universitas Jambi
## Nazwa Eka Hervy - F1E122096

**Catatan untuk penguji:**
Dokumen ini disusun sebagai panduan pertanyaan sidang dan daftar kesalahan konseptual dalam proposal. Setiap temuan telah diverifikasi melalui pengecekan regulasi BKD (Kepdirjendikti 12/E/KPT/2021), referensi asli CRISP-DM (Chapman et al., 2000), literatur *compositional data analysis*, dan metadata jurnal terkait.

Dokumen terbagi dua bagian utama:
- **Bagian A** berisi pertanyaan-pertanyaan yang disarankan untuk diajukan saat sidang, lengkap dengan catatan konteks agar penguji dapat menggali lebih dalam.
- **Bagian B** berisi daftar kesalahan konsep yang ditemukan dalam proposal, disertai bukti verifikasi.

---

## A. PERTANYAAN UNTUK SIDANG

### 1. Pertanyaan Seputar Judul & Rumusan Masalah

**Pertanyaan 1 -- Kontradiksi kata "Pemodelan" dan "Eksplorasi" di judul**

Judul proposal berbunyi: *"**Pemodelan** K-Means Clustering untuk **Eksplorasi** Pola Distribusi..."*

Kedua kata kunci ini saling bertentangan secara konseptual. "Pemodelan" mengimplikasikan pembangunan model prediktif yang bisa digunakan ulang untuk mengklasifikasi data baru (*supervised learning*). Sementara "Eksplorasi" mengimplikasikan pencarian pola tersembunyi tanpa target prediksi (*unsupervised learning*). K-Means sendiri adalah algoritma *clustering* (unsupervised), bukan model prediktif.

Pertanyaan yang diajukan:
> *"Apa yang dimaksud dengan 'pemodelan' di sini? Jelaskan perbedaan antara pemodelan (modeling) dan penerapan algoritma clustering."*

**Strategi bertanya:** Mulai dengan pertanyaan terbuka -- *"Apa definisi pemodelan menurut Anda?"* Lalu arahkan ke kontradiksi dengan kata "Eksplorasi" di judul yang sama. Jika mahasiswa tidak bisa menjelaskan model apa yang dihasilkan dan bagaimana model tersebut akan digunakan kembali, maka penggunaan kata "Pemodelan" tidak tepat.

**Kata yang lebih tepat untuk judul:**
- *"**Penerapan** K-Means Clustering untuk Eksplorasi Pola Distribusi Kinerja Tri Dharma..."*
- *"**Analisis** Pola Distribusi Kinerja Tri Dharma Dosen Menggunakan K-Means Clustering..."*

---

**Pertanyaan 2 -- Makna "dioptimalkan" dalam rumusan masalah**

Rumusan masalah nomor 1 menyebutkan kata "dioptimalkan." Pertanyaan ini menguji apakah mahasiswa memahami perbedaan antara optimasi parameter K-Means (misalnya inisialisasi centroid, jumlah iterasi) dan penentuan jumlah cluster optimal. Keduanya adalah hal yang berbeda secara metodologis.

> *"Optimasi apa yang dimaksud dalam rumusan masalah? Apakah optimasi parameter algoritma, atau penentuan jumlah cluster terbaik?"*

---

**Pertanyaan 3 -- Kecukupan data untuk perbandingan semester**

Rumusan masalah nomor 3 membahas perbandingan pola antara semester ganjil dan genap. Namun, batasan masalah hanya mencakup data TA 2024/2025, yang berarti hanya ada 2 titik data waktu (1 semester ganjil + 1 semester genap).

> *"Dengan hanya 2 semester sebagai data, apakah cukup untuk menarik kesimpulan tentang 'perbedaan pola'? Bukankah ini hanya perbandingan deskriptif satu kali, bukan analisis pola yang dapat digeneralisasi?"*

---

### 2. Pertanyaan Seputar Tinjauan Pustaka & Konsep

**Pertanyaan 4 -- Inkonsistensi jumlah variabel dengan batasan masalah [TERVERIFIKASI]**

Batasan masalah (hal. 5) secara eksplisit menyatakan bahwa variabel dibatasi pada "tiga pilar utama Tri Dharma." Namun di Tabel 3 (hal. 30), tercantum 4 variabel termasuk X4 (Kegiatan Penunjang). Kegiatan penunjang secara regulasi bukan bagian dari Tri Dharma Perguruan Tinggi (UU 12/2012 Pasal 1 ayat 9).

> *"Mengapa kegiatan penunjang dimasukkan sebagai variabel clustering padahal batasan masalah menyatakan hanya 3 pilar Tri Dharma?"*

---

**Pertanyaan 5 -- Ambiguitas satuan variabel: proporsi vs SKS absolut [TERVERIFIKASI]**

Batasan masalah menyebutkan "proporsi persentase SKS riil", tetapi Tabel 3 menuliskan satuan "SKS" (absolut). Dua satuan ini menghasilkan implikasi metodologis yang sangat berbeda:

- **Jika proporsi/persentase:** Data bersifat *compositional* (semua variabel berjumlah 100%) dan memerlukan perlakuan statistik khusus.
- **Jika SKS absolut:** Dosen dengan total 20 SKS dan dosen dengan 12 SKS akan terlihat berbeda meski pola distribusi antar komponen Tri Dharma-nya identik.

> *"Mana yang benar digunakan -- proporsi atau SKS absolut? Jelaskan dampaknya terhadap hasil clustering."*

---

**Pertanyaan 6 -- Masalah compositional data dalam K-Means [TERVERIFIKASI]**

Pertanyaan ini relevan jika mahasiswa menggunakan proporsi/persentase. Literatur ilmiah (Aitchison, 1986; van den Boogaart & Tolosana-Delgado, 2013) menunjukkan bahwa K-Means dengan Euclidean distance pada data compositional di *simplex space* dapat menghasilkan cluster yang *misleading*. Pendekatan yang direkomendasikan adalah transformasi ILR (*Isometric Log-Ratio*) atau Aitchison distance.

> *"Jika data yang digunakan berupa proporsi, apakah Anda mengetahui masalah compositional data? Bagaimana menanganinya?"*

---

**Pertanyaan 7 -- Justifikasi pemilihan K-Means**

Mahasiswa menyebutkan data BKD "tidak mengandung noise signifikan karena telah melalui verifikasi asesor." Namun pada kenyataannya, data BKD kemungkinan besar memiliki banyak nilai 0 pada komponen penelitian atau pengabdian -- khususnya untuk dosen yang memang tidak melakukan kegiatan tersebut di semester tertentu.

> *"Mengapa K-Means dipilih dibandingkan metode lain? Bagaimana K-Means menangani data dengan banyak nilai nol?"*

---

**Pertanyaan 8 -- Tahap Deployment dalam CRISP-DM**

Di halaman 28, mahasiswa menyamakan tahap *Deployment* CRISP-DM dengan "Visualisasi & Interpretasi Data." Menurut dokumen resmi CRISP-DM (Chapman et al., 2000), *deployment* mengacu pada implementasi hasil ke proses bisnis/operasional organisasi -- bukan sekadar membuat visualisasi untuk laporan skripsi.

> *"Apa rencana deployment konkret dari penelitian ini? Apakah membuat visualisasi untuk laporan sudah termasuk deployment menurut CRISP-DM?"*

**Catatan:** Mahasiswa sebenarnya menyebutkan opsi "*Dashboard interaktif menggunakan Streamlit atau Google Data Studio*" di halaman 28. Jika ini benar-benar diimplementasikan, bisa dikategorikan sebagai *deployment*. Namun ini ditulis sebagai opsi ("dapat dibuat"), bukan komitmen.

---

### 3. Pertanyaan Seputar Metodologi

**Pertanyaan 9 -- Klaim SLR vs narrative review**

Di bagian kerangka penelitian, mahasiswa menyebutkan menggunakan *Systematic Literature Review* (SLR). SLR formal memerlukan protokol PRISMA (diagram alir, kriteria inklusi/eksklusi, jumlah artikel di tiap tahap). Yang dilakukan dalam proposal hanya pencarian di database akademik dengan kata kunci tertentu -- ini lebih mendekati *narrative review*.

> *"Apakah ini benar-benar SLR atau narrative review? Di mana protokol PRISMA-nya?"*

**Catatan:** Penggunaan istilah "SLR" secara longgar memang umum di skripsi Indonesia, sehingga ini lebih merupakan isu presisi terminologi daripada kesalahan fatal. Namun tetap layak diklarifikasi untuk menguji pemahaman mahasiswa.

---

**Pertanyaan 10 -- Hubungan antara 2 tahap clustering**

Mahasiswa menyebutkan ada 2 tahap clustering: Tahap 1 (clustering global semua variabel) dan Tahap 2 (clustering per aspek Tri Dharma).

> *"Bagaimana menghubungkan hasil Tahap 1 dan Tahap 2? Apakah ada metode formal untuk membandingkan keanggotaan cluster, atau hanya analisis deskriptif?"*

---

**Pertanyaan 11 -- Jumlah populasi**

> *"Berapa jumlah dosen tetap UNJA yang menjadi populasi penelitian? Apakah jumlahnya sudah dipastikan memadai untuk K-Means clustering?"*

---

**Pertanyaan 12 -- Pemilihan metode normalisasi**

> *"Anda menyebutkan menggunakan StandardScaler atau MinMaxScaler. Mana yang akan digunakan dan mengapa? Keduanya memberikan hasil berbeda dan dapat mempengaruhi hasil clustering."*

---

**Pertanyaan 13 -- Kontradiksi argumen noise vs outlier detection [TERVERIFIKASI]**

Di halaman 21, mahasiswa berargumen data BKD "tidak mengandung noise signifikan" untuk menjustifikasi pemilihan K-Means daripada DBSCAN. Namun di Data Preparation (hal. 32), masih merencanakan "outlier detection menggunakan IQR atau Z-score."

> *"Jika data sudah bersih tanpa noise, mengapa masih merencanakan outlier detection? Dan sebaliknya, jika ternyata ada outlier, mengapa mengklaim noise minimal untuk menjustifikasi K-Means?"*

Ini adalah kontradiksi logis yang menunjukkan mahasiswa mungkin belum sepenuhnya memahami hubungan antara noise, outlier, dan pemilihan algoritma clustering.

---

**Pertanyaan 14 -- Penanganan dosen struktural [TERVERIFIKASI - Isu Regulasi]**

Menurut Kepdirjendikti 12/E/KPT/2021, dosen struktural (pimpinan PT sampai ketua program studi) hanya wajib minimal 3 SKS pendidikan. Ini berbeda dari dosen biasa yang wajib 9 SKS gabungan pendidikan dan penelitian.

> *"Jika dosen struktural dan dosen biasa di-cluster bersama, perbedaan pola yang ditemukan bisa jadi hanya mencerminkan perbedaan regulasi, bukan perbedaan 'kinerja.' Bagaimana Anda menangani hal ini?"*

---

### 4. Pertanyaan Seputar Evaluasi & Kontribusi

**Pertanyaan 15 -- Penanganan konflik antar metrik evaluasi**

> *"Anda menggunakan 3 metrik evaluasi (Elbow, Silhouette, DBI). Bagaimana jika ketiganya memberikan rekomendasi jumlah cluster (k) yang berbeda? Metrik mana yang diprioritaskan dan mengapa?"*

---

**Pertanyaan 16 -- Relevansi dengan bidang Sistem Informasi**

> *"Penelitian ini secara teknis lebih condong ke data science/data mining. Sebagai mahasiswa Sistem Informasi, di mana aspek 'sistem informasi'-nya? Apa kontribusi spesifik terhadap bidang SI?"*

---

**Pertanyaan 17 -- Pembeda dari penelitian Pratama et al. (2026)**

Pratama et al. (2026) sudah melakukan K-Means pada data BKD di universitas lain.

> *"Apa yang membedakan penelitian Anda secara fundamental dari Pratama et al. selain perbedaan lokasi? Jelaskan mengapa penambahan aspek Tri Dharma lengkap dan perbandingan dosen struktural/fungsional signifikan sebagai kontribusi baru."*

---

**Pertanyaan 18 -- Rencana pemanfaatan hasil**

> *"Bagaimana hasil clustering akan digunakan secara praktis oleh UNJA? Apakah pihak UNJA sudah dilibatkan dalam merumuskan kebutuhan ini?"*

---

## B. KESALAHAN KONSEP (TERVERIFIKASI)

Bagian ini memuat kesalahan-kesalahan konseptual yang ditemukan dalam proposal. Setiap temuan dilengkapi dengan bukti verifikasi dan sumber rujukan. Urutan disusun dari yang paling serius.

---

### 1. [CONFIRMED] Inkonsistensi Variabel dengan Batasan Masalah

**Inti masalah:** Batasan masalah menyatakan 3 variabel (Tri Dharma), tetapi variabel penelitian menambahkan variabel ke-4 (Kegiatan Penunjang) yang bukan bagian dari Tri Dharma.

**Bukti:**
- **Halaman 5 (Batasan Masalah no. 1):** Menyatakan variabel dibatasi pada *"proporsi persentase SKS riil dari **tiga pilar utama** Tri Dharma Perguruan Tinggi (Pendidikan/Pengajaran, Penelitian, dan Pengabdian kepada Masyarakat)"*
- **Halaman 29-30 (Variabel Penelitian & Tabel 3):** Menampilkan **empat variabel** termasuk X4 (Kegiatan Penunjang), dan secara eksplisit menyatakan *"Keempat variabel tersebut akan digunakan sebagai fitur dalam model K-Means Clustering"*

**Verifikasi:** Kegiatan penunjang secara regulasi memang bukan bagian Tri Dharma. Tri Dharma hanya terdiri dari Pendidikan, Penelitian, dan Pengabdian (UU 12/2012 Pasal 1 ayat 9). Ini adalah inkonsistensi nyata antara batasan masalah dan variabel penelitian yang harus diklarifikasi.

---

### 2. [CONFIRMED] Inkonsistensi Satuan Variabel

**Inti masalah:** Batasan masalah dan Tabel 3 menyebutkan satuan yang berbeda.

- **Batasan masalah** menyatakan *"proporsi persentase SKS riil"*
- **Tabel 3** menyatakan satuan *"SKS"* (nilai absolut)

**Catatan:** Ada kemungkinan mahasiswa bermaksud menggunakan SKS mentah yang kemudian dikonversi ke proporsi pada tahap Data Preparation. Namun hal ini tidak dijelaskan secara eksplisit di mana pun dalam proposal, sehingga menimbulkan ambiguitas metodologis yang perlu diklarifikasi.

---

### 3. [CONFIRMED] Masalah Compositional Data (Jika Menggunakan Proporsi)

**Inti masalah:** Jika menggunakan proporsi/persentase, K-Means dengan Euclidean distance secara matematis tidak tepat.

**Penjelasan:** Data yang berbentuk proporsi terletak di *simplex space* (semua komponen berjumlah 100%), bukan ruang Euclidean. Euclidean distance pada data seperti ini dapat menghasilkan cluster yang *misleading*. Literatur merekomendasikan transformasi ILR (*Isometric Log-Ratio*) atau menggunakan Aitchison distance.

**Relevansi:** Isu ini **hanya berlaku** jika mahasiswa benar-benar menggunakan proporsi/persentase. Jika menggunakan SKS absolut, masalah ini tidak muncul. Namun karena batasan masalah secara eksplisit menyebut "proporsi persentase," isu ini perlu dibahas.

**Sumber:** Aitchison (1986); van den Boogaart & Tolosana-Delgado (2013); Filzmoser et al. (2009).

---

### 4. [CONFIRMED] Referensi CRISP-DM dengan Nama Penulis Salah

**Inti masalah:** Nama afiliasi perusahaan ditulis sebagai nama penulis di daftar pustaka.

**Bukti:**
- **Halaman 13:** Mengutip "Ncr et al., 2000"
- **Halaman 27:** Mengutip "Chapman et al., 2000" (ini yang benar)
- **Daftar Pustaka (hal. 36):** Menulis *"Ncr, P. C., Spss, J. C., Ncr, R. K., Spss, T. K., Daimlerchrysler, T. R., Spss, C. S., & Daimlerchrysler, R. W. (2000)"*

**Verifikasi:** Penulis sebenarnya adalah Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). "NCR", "SPSS", dan "DaimlerChrysler" adalah **afiliasi perusahaan** tempat masing-masing penulis bekerja, bukan nama penulis. Inisial "P. C." dan "J. C." adalah singkatan nama depan penulis asli (Pete Chapman, Julian Clinton, dst.) yang keliru dipasangkan dengan nama perusahaan.

Ini menunjukkan bahwa mahasiswa kemungkinan menyalin referensi dari sumber yang mencantumkan afiliasi berdampingan dengan nama, tanpa memahami perbedaannya.

---

### 5. [CONFIRMED] Inkonsistensi Referensi Pratama et al.

**Inti masalah:** Satu referensi dikutip dengan 3 kesalahan berbeda di 3 lokasi berbeda dalam proposal.

**Referensi asli (terverifikasi dari metadata jurnal):** Pratama, M. E., **Kusrini**, & Artha Agastya, I. M. (2026). JSI Universitas Suryadarma, Vol. 13(1), pp. 162-179. Terdapat **3 penulis**.

**Kesalahan yang ditemukan:**

| Lokasi | Tertulis | Seharusnya | Jenis Kesalahan |
|--------|----------|------------|-----------------|
| Hal. 1, 3 | "Pratama & Agastya, 2026" | "Pratama et al., 2026" | Jumlah penulis -- ada 3 penulis, seharusnya pakai "et al." |
| Tabel 2 (hal. 22) | Tahun "(2024)" | "(2026)" | Tahun salah |
| Daftar Pustaka (hal. 37) | "Pratama, M. E., & Agastya, I. M. A. (2026)" | "Pratama, M. E., Kusrini, & Artha Agastya, I. M. (2026)" | Penulis kedua (Kusrini) dihilangkan |

**Catatan:** Tahun 2026 sendiri **valid** -- jurnal JSI Universitas Suryadarma Vol. 13(1) memang sudah terbit.

---

### 6. [CONFIRMED] Angka Beban Minimal Dosen yang Keliru

**Inti masalah:** Angka "6 SKS" yang disebut di halaman 1 tidak sesuai regulasi manapun.

**Bukti:**
- **Halaman 1:** Menyebutkan *"wajib minimal 6 SKS pendidikan"* untuk dosen struktural, mengutip Pratama & Agastya (2026)
- **Halaman 10:** Menyebutkan *"dharma pendidikan minimal 3 SKS"* untuk dosen struktural, mengutip Dirjen Dikti 12/E/KPT/2021

**Verifikasi dari regulasi resmi (Kepdirjendikti 12/E/KPT/2021):**
- Dosen biasa: pendidikan + penelitian minimal **9 SKS**
- Dosen struktural (pimpinan PT s.d. ketua program studi): pendidikan minimal **3 SKS**
- **Tidak ada** ketentuan "minimal 6 SKS pendidikan" dalam regulasi BKD

**Kesimpulan:** Angka "6 SKS" di halaman 1 merupakan data keliru. Halaman 8 (menyebut 9 SKS) dan halaman 10 (menyebut 3 SKS) sudah benar.

---

### 7. [CONFIRMED] Deployment CRISP-DM Disalahartikan

**Inti masalah:** Tahap *Deployment* CRISP-DM disamakan dengan pembuatan visualisasi.

Di halaman 28, mahasiswa menyamakan tahap *Deployment* dengan "Visualisasi & Interpretasi Data." Menurut dokumen resmi CRISP-DM (Chapman et al., 2000), *Deployment* mengacu pada penerapan hasil analisis ke dalam proses bisnis/operasional organisasi -- misalnya mengintegrasikan model ke sistem produksi, membuat prosedur otomatis, atau menyerahkan panduan pengambilan keputusan kepada pengguna akhir.

Membuat visualisasi untuk laporan skripsi **bukan** *deployment* dalam pengertian CRISP-DM.

**Catatan:** Mahasiswa menyebutkan opsi pembuatan *"Dashboard interaktif menggunakan Streamlit atau Google Data Studio"* di halaman 28. Jika ini benar-benar diimplementasikan dan digunakan oleh pihak universitas, barulah bisa dikategorikan sebagai *deployment*. Namun dalam proposal, ini ditulis sebagai opsi ("dapat dibuat"), bukan komitmen.

---

### 8. [NUANSA - Perlu Diskusi Serius] Penggunaan Istilah "Pemodelan"

**Inti masalah:** Kata "Pemodelan" dan "Eksplorasi" dalam satu judul saling bertentangan.

**Analisis:**
- **"Pemodelan"** (*modeling*) mengimplikasikan pembangunan model yang bersifat prediktif/*reusable* -- menghasilkan sesuatu yang bisa digunakan untuk memprediksi atau mengklasifikasi data baru di masa depan.
- **"Eksplorasi"** mengimplikasikan analisis deskriptif untuk menemukan pola tersembunyi -- hasilnya berupa *insight* dan label cluster, bukan model yang di-*deploy*.

Penelitian ini menghasilkan label cluster dan interpretasi pola distribusi kinerja. Tidak ada "model" yang akan digunakan ulang untuk mengklasifikasi dosen baru. Ini secara substansi merupakan **penerapan** algoritma, bukan pemodelan.

**Catatan:** Dalam konvensi skripsi Indonesia, "pemodelan" memang sering digunakan secara luas. Namun kontradiksi internal dengan kata "Eksplorasi" di judul yang sama menjadikan ini bukan sekadar isu konvensi, tetapi inkonsistensi logis yang layak dipertanyakan saat sidang.

---

### 9. [NUANSA] Klaim SLR

Di halaman 25, mahasiswa menyebutkan menggunakan *Systematic Literature Review* (SLR). Secara ketat, SLR memerlukan protokol PRISMA (diagram alir, kriteria inklusi/eksklusi, transparansi jumlah artikel di tiap tahap).

Yang dilakukan dalam proposal lebih mendekati *narrative review* yang terstruktur. Penggunaan istilah "SLR" secara longgar memang umum dalam skripsi S1 di Indonesia, sehingga ini lebih merupakan isu presisi terminologi daripada kesalahan fatal.

---

### 10. [CONFIRMED] Kontradiksi Argumen Noise vs Outlier Detection

**Inti masalah:** Argumen "tidak ada noise" digunakan untuk menjustifikasi K-Means, tetapi kemudian outlier detection tetap direncanakan.

**Bukti:**
- **Halaman 21:** Mahasiswa berargumen data BKD *"tidak mengandung noise signifikan karena telah diverifikasi asesor"* -- ini dijadikan alasan memilih K-Means daripada DBSCAN.
- **Halaman 32 (Data Preparation):** Masih merencanakan *"outlier detection menggunakan IQR atau Z-score."*

Jika data memang sudah bersih, tidak perlu deteksi outlier. Jika ternyata ada outlier, klaim "noise minimal" yang digunakan untuk menolak DBSCAN menjadi lemah. Ini menunjukkan inkonsistensi dalam pemahaman mahasiswa terhadap hubungan antara noise, outlier, dan pemilihan algoritma clustering.

---

### 11. [CONFIRMED] Daftar Pustaka Sangat Tidak Lengkap

**Inti masalah:** Lebih dari separuh referensi yang dikutip dalam teks tidak ada di daftar pustaka.

Daftar pustaka hanya memuat ~19 entri (halaman 36-37), sementara dalam teks proposal terdapat **50+ referensi** yang dikutip. Referensi yang hilang tersebar di seluruh alfabet (dari huruf A hingga X), sehingga ini **bukan** masalah PDF terpotong -- melainkan entri-entri yang memang belum dimasukkan.

Contoh: "Fransiska (2022)" yang dikutip di 4 halaman berbeda seharusnya muncul di antara entri "Dewi" dan "Gunawan" dalam daftar pustaka yang urut alfabet, tetapi tidak ada.

Daftar lengkap 40 referensi yang hilang dapat dilihat di dokumen **02_Daftar_Kesalahan_Penulisan.md** bagian C.7.

---

### 12. [DIKOREKSI] Novelty Penelitian -- Awalnya Dinilai Lemah, Ternyata Cukup Memadai

Pada analisis awal, novelty penelitian ini dinilai lemah. Setelah evaluasi ulang yang lebih cermat, penilaian ini dikoreksi. Novelty sebenarnya **cukup memadai** karena:

1. Menganalisis **semua 3 komponen Tri Dharma** secara simultan (penelitian terdahulu umumnya hanya 1-2 komponen)
2. Membandingkan pola antar semester (ganjil vs genap)
3. Berencana membandingkan pola dosen struktural vs fungsional
4. Diterapkan pada konteks Universitas Jambi yang belum pernah dianalisis sebelumnya

Meskipun demikian, pertanyaan tentang novelty tetap layak diajukan dalam sidang untuk menguji pemahaman dan argumentasi mahasiswa (lihat Pertanyaan 17).
