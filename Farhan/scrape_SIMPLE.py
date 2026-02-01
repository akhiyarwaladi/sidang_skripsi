# ===================================================================
# SCRAPING REVIEW DUOLINGO - VERSI SUPER SIMPEL (3 BARIS KODE!)
# Library: google-play-scraper (PALING POPULER 2025/2026)
# ===================================================================

# INSTALL DULU (jalankan di terminal/cmd):
# pip install google-play-scraper pandas

# ===================================================================
# IMPORT
# ===================================================================
from google_play_scraper import app, Sort, reviews
import pandas as pd
from datetime import datetime

# ===================================================================
# KONFIGURASI - TINGGAL GANTI INI SAJA!
# ===================================================================
APP_ID = 'com.duolingo'  # ID aplikasi (bisa dicek dari URL Play Store)
JUMLAH_REVIEW = 1000     # Target review (sesuai proposal Farhan)
BAHASA = 'id'            # Bahasa Indonesia
NEGARA = 'id'            # Region Indonesia

print("🚀 Mulai scraping...")
print(f"App: {APP_ID}")
print(f"Target: {JUMLAH_REVIEW} review\n")

# ===================================================================
# SCRAPING - TINGGAL 3 BARIS!
# ===================================================================

# Baris 1: Ambil semua review
result, continuation_token = reviews(
    APP_ID,
    lang=BAHASA,
    country=NEGARA,
    sort=Sort.NEWEST,     # Urutkan dari terbaru
    count=JUMLAH_REVIEW   # Jumlah yang diambil
)

# Baris 2: Konversi ke DataFrame
df = pd.DataFrame(result)

# Baris 3: Simpan ke CSV
filename = f'duolingo_reviews_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
df.to_csv(filename, index=False, encoding='utf-8-sig')

# ===================================================================
# HASIL
# ===================================================================
print(f"✅ SELESAI!")
print(f"📊 Berhasil ambil {len(df)} review")
print(f"💾 File tersimpan: {filename}")

# Preview data
print(f"\n📋 KOLOM DATA YANG DIDAPAT:")
print(df.columns.tolist())

print(f"\n👀 PREVIEW 3 REVIEW PERTAMA:")
print(df[['userName', 'score', 'at', 'content']].head(3))

# Statistik
print(f"\n📊 STATISTIK:")
print(f"Rating rata-rata: {df['score'].mean():.2f}")
print(f"Review terpanjang: {df['content'].str.len().max()} karakter")
print(f"Review terpendek: {df['content'].str.len().min()} karakter")

print(f"\n🎉 DATA SIAP DIPROSES!")

# ===================================================================
# INFORMASI KOLOM DATA
# ===================================================================
"""
KOLOM YANG DIDAPAT (10+ fields):

1. reviewId         - ID unik review
2. userName         - Nama user
3. userImage        - Foto profil user
4. content          - ISI ULASAN (DATA UTAMA) ⭐⭐⭐
5. score            - Rating (1-5 bintang)
6. thumbsUpCount    - Jumlah like
7. reviewCreatedVersion - Versi app saat review
8. at               - Tanggal review
9. replyContent     - Balasan developer
10. repliedAt       - Tanggal balasan developer
11. appVersion      - Versi aplikasi
"""
