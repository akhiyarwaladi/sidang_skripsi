# ===================================================================
# SCRIPT UNTUK SCRAPING REVIEW APLIKASI DUOLINGO
# Untuk Penelitian: Farhan (F1E122149)
# ===================================================================

# CARA PAKAI:
# 1. Buka Google Colab: https://colab.research.google.com
# 2. Copy-paste seluruh kode ini
# 3. Jalankan (tekan tombol Play)
# 4. File CSV akan otomatis ter-download

# ===================================================================
# INSTALASI LIBRARY
# ===================================================================
!pip install google-play-scraper pandas

# ===================================================================
# IMPORT LIBRARY
# ===================================================================
from google_play_scraper import app, reviews_all
import pandas as pd
from datetime import datetime
import time

# ===================================================================
# KONFIGURASI
# ===================================================================
APP_ID = 'com.duolingo'  # ID aplikasi Duolingo di Google Play Store
LANG = 'id'              # Bahasa Indonesia
COUNTRY = 'id'           # Region Indonesia
MAX_REVIEWS = 1000       # Jumlah review yang ingin diambil (sesuai proposal)

print("=" * 70)
print("SCRAPING REVIEW APLIKASI DUOLINGO")
print("=" * 70)
print(f"App ID: {APP_ID}")
print(f"Target: {MAX_REVIEWS} review berbahasa Indonesia")
print(f"Waktu mulai: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)

# ===================================================================
# SCRAPING DATA
# ===================================================================
try:
    print("\n🔄 Sedang mengambil data review...")
    print("⏳ Proses ini membutuhkan waktu 2-5 menit...")

    # Ambil review
    result = reviews_all(
        APP_ID,
        lang=LANG,
        country=COUNTRY,
        count=MAX_REVIEWS
    )

    print(f"✅ Berhasil mengambil {len(result)} review!")

    # ===================================================================
    # KONVERSI KE DATAFRAME
    # ===================================================================
    print("\n🔄 Memproses data...")

    df = pd.DataFrame(result)

    # Pilih kolom yang relevan sesuai proposal
    df_clean = df[[
        'userName',           # Nama user
        'content',           # Isi ulasan (TEXT UTAMA untuk analisis)
        'score',             # Rating (1-5 bintang)
        'at',                # Waktu review dibuat
        'reviewCreatedVersion',  # Versi aplikasi saat review
        'thumbsUpCount',     # Jumlah thumbs up
        'replyContent'       # Balasan developer (jika ada)
    ]].copy()

    # Rename kolom agar lebih jelas
    df_clean.columns = [
        'username',
        'review_text',
        'rating',
        'review_date',
        'app_version',
        'thumbs_up',
        'developer_reply'
    ]

    # Format tanggal
    df_clean['review_date'] = pd.to_datetime(df_clean['review_date'])

    # Filter hanya review tahun 2025 (sesuai proposal: Jan-Nov 2025)
    df_clean = df_clean[
        (df_clean['review_date'] >= '2025-01-01') &
        (df_clean['review_date'] <= '2025-11-30')
    ]

    # Ambil 1000 data secara random (sesuai proposal)
    if len(df_clean) > MAX_REVIEWS:
        df_clean = df_clean.sample(n=MAX_REVIEWS, random_state=42)

    print(f"✅ Data berhasil diproses!")
    print(f"📊 Jumlah review final: {len(df_clean)}")

    # ===================================================================
    # STATISTIK DATA
    # ===================================================================
    print("\n" + "=" * 70)
    print("STATISTIK DATA")
    print("=" * 70)
    print(f"Total review: {len(df_clean)}")
    print(f"Periode: {df_clean['review_date'].min()} s/d {df_clean['review_date'].max()}")
    print(f"\nDistribusi Rating:")
    print(df_clean['rating'].value_counts().sort_index())
    print(f"\nRata-rata panjang review: {df_clean['review_text'].str.len().mean():.0f} karakter")

    # ===================================================================
    # SIMPAN KE CSV
    # ===================================================================
    filename = f'duolingo_reviews_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    df_clean.to_csv(filename, index=False, encoding='utf-8-sig')

    print("\n" + "=" * 70)
    print("✅ PROSES SELESAI!")
    print("=" * 70)
    print(f"📁 File tersimpan: {filename}")
    print(f"📊 Total data: {len(df_clean)} review")
    print(f"⏰ Waktu selesai: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # Preview data
    print("\n📋 PREVIEW DATA (5 review pertama):")
    print(df_clean.head())

    # Download file (khusus untuk Google Colab)
    try:
        from google.colab import files
        files.download(filename)
        print(f"\n⬇️ File {filename} sedang di-download ke komputer Anda...")
    except:
        print(f"\n💾 File tersimpan di: {filename}")
        print("ℹ️ Jika menggunakan Colab, file akan otomatis ter-download")

except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    print("\nKemungkinan masalah:")
    print("1. Koneksi internet tidak stabil")
    print("2. Google Play Store membatasi request")
    print("3. ID aplikasi salah")
    print("\n💡 Solusi: Tunggu beberapa menit, lalu coba lagi")

# ===================================================================
# INFORMASI TAMBAHAN
# ===================================================================
print("\n" + "=" * 70)
print("LANGKAH SELANJUTNYA (Sesuai Proposal)")
print("=" * 70)
print("1. ✅ Data sudah di-download")
print("2. 🔧 Lakukan Preprocessing:")
print("   - Cleaning (hapus URL, mention, spasi berlebih)")
print("   - Case folding (lowercase)")
print("   - Normalization (kata tidak baku → baku)")
print("3. 🏷️  Pelabelan manual sentimen (positif/negatif)")
print("4. 🤖 Training model IndoBERTweet")
print("5. 📊 Analisis topik dengan BERTopic")
print("=" * 70)
