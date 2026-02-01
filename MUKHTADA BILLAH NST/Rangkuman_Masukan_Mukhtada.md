# RANGKUMAN MASUKAN UNTUK MUKHTADA BILLAH NST

Mahasiswa: MUKHTADA BILLAH NST (F1E122037)
Judul: Optimasi Algoritma Genetika Menggunakan Fuzzy Logic pada Penjadwalan Praktikum
File Sumber: MUKHTADA BILLAH NST\Pertanyaan_Ujian_Proposal_Mukhtada.md

---

## Masukan Utama

1) Kesalahan Penulisan dan Format Dokumen - Dokumen proposal mengandung beberapa kesalahan seperti kesalahan ejaan "menyelsaikan" pada halaman 2 yang seharusnya "menyelesaikan", error bookmark "Tabel 3.12...Error! Bookmark not defined" pada Daftar Tabel halaman 8 yang menunjukkan referensi silang rusak, duplikasi penomoran Gambar 3.12 yang muncul dua kali (halaman 49 dan 53) serta Tabel 3.3 yang juga muncul dua kali (halaman 40 dan 52), serta inkonsistensi penomoran tabel seperti Tabel 3.2 yang berada di Bab 2 seharusnya bernomor Tabel 2.2 dan Tabel 4.12 yang muncul di halaman 49 padahal masih bagian Bab 3. 2) Justifikasi Parameter dan Metodologi Fuzzy Logic - Perlu memperkuat justifikasi pemilihan parameter fuzzy logic yang digunakan, terutama nilai bobot penalti alpha=3.0, beta=1.0, dan gamma=2.0 pada fitness function yang harus didukung dengan studi literatur, eksperimen pendahuluan, dan domain knowledge dari pihak FST. Selain itu, perlu dijelaskan secara eksplisit metode defuzzifikasi yang digunakan (COG, MOM, atau weighted average), alasan pemilihan fungsi keanggotaan segitiga dan trapesium beserta kelebihan dan kekurangannya, serta justifikasi range nilai untuk kategori LOW-MEDIUM-HIGH pada standar deviasi fitness dan lonjakan fitness. Perlu juga mengklarifikasi mengapa menggunakan "lonjakan fitness" sebagai input untuk mutation rate dibandingkan "stagnation counter" yang lebih umum dalam literatur, serta mempertimbangkan apakah range mutation rate 0.01-0.10 sudah cukup untuk keluar dari local optimum, karena pemahaman mendalam tentang parameter-parameter ini sangat krusial untuk membuktikan kontribusi penelitian. 3) Metrik Evaluasi dan Gap Penelitian - Terdapat kesalahan konseptual serius pada metrik evaluasi di halaman 52, dimana disebutkan akan menggunakan "makespan", "flow time", dan "average lateness" yang sebenarnya lebih cocok untuk Job Shop Scheduling Problem (JSSP) bukan Course Timetabling Problem (CTP), sehingga perlu diganti dengan metrik yang tepat seperti Hard Constraint Violations (bentrok ruangan, dosen, mahasiswa), Soft Constraint Violations (preferensi waktu), Fitness Value Convergence, dan Computational Performance (waktu eksekusi, jumlah generasi). Perlu juga memperjelas gap analysis yang membedakan penelitian ini dengan penelitian sebelumnya seperti Ghaffar et al. (2022) untuk menunjukkan novelty dan kontribusi penelitian secara lebih jelas, serta menjelaskan mengapa pendekatan dari penelitian terdahulu tidak cukup untuk kasus di FST Universitas Jambi.

---

Tanggal: 23 Desember 2025
