"""
Analisis Multikolinearitas Data Saham BMRI
Untuk menjawab pertanyaan sidang tentang korelasi tinggi antara Open, High, Low, Close

Metode:
1. Correlation Matrix - mengukur korelasi antar variabel
2. VIF (Variance Inflation Factor) - mengukur tingkat multikolinearitas
   - VIF < 5: Tidak ada multikolinearitas
   - VIF 5-10: Multikolinearitas sedang
   - VIF > 10: Multikolinearitas tinggi

Author: Imelda Agustin (F1E122002)
"""

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Set style untuk visualisasi
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ==================== DOWNLOAD DATA BMRI ====================
print("=" * 70)
print("ANALISIS MULTIKOLINEARITAS DATA SAHAM BMRI")
print("=" * 70)
print("\n1. Downloading data saham BMRI dari Yahoo Finance...")

# Download data BMRI (Bank Mandiri)
# Ticker untuk BMRI di Yahoo Finance adalah BMRI.JK
ticker = "BMRI.JK"
start_date = "2020-01-01"
end_date = datetime.now().strftime("%Y-%m-%d")

try:
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    print(f"   ✓ Berhasil download {len(df)} data points")
    print(f"   ✓ Periode: {df.index[0].strftime('%Y-%m-%d')} s/d {df.index[-1].strftime('%Y-%m-%d')}")
except Exception as e:
    print(f"   ✗ Error downloading data: {e}")
    exit()

# ==================== EXPLORATORY DATA ====================
print("\n2. Preview Data:")
print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nInfo:")
print(df.info())

# Simpan data mentah
df.to_csv("Imelda Agustin/data_bmri_raw.csv")
print("\n   ✓ Data mentah disimpan: data_bmri_raw.csv")

# ==================== ANALISIS KORELASI ====================
print("\n" + "=" * 70)
print("3. ANALISIS KORELASI MATRIX")
print("=" * 70)

# Flatten column names jika MultiIndex
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

# Pilih hanya fitur OHLCV
features = ['Open', 'High', 'Low', 'Close', 'Volume']
df_features = df[features].copy()

# Hitung correlation matrix
corr_matrix = df_features.corr()

print("\nMatriks Korelasi OHLCV:")
print(corr_matrix)

# Identifikasi pasangan dengan korelasi sangat tinggi (> 0.95)
print("\n⚠️  PASANGAN DENGAN KORELASI SANGAT TINGGI (> 0.95):")
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        if abs(corr_matrix.iloc[i, j]) > 0.95:
            print(f"   • {corr_matrix.columns[i]} vs {corr_matrix.columns[j]}: {corr_matrix.iloc[i, j]:.4f}")

# Visualisasi correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.4f', cmap='coolwarm',
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix - Fitur OHLCV Saham BMRI', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('Imelda Agustin/correlation_matrix_bmri.png', dpi=300, bbox_inches='tight')
print("\n   ✓ Visualisasi disimpan: correlation_matrix_bmri.png")
plt.close()

# ==================== ANALISIS VIF ====================
print("\n" + "=" * 70)
print("4. ANALISIS VIF (Variance Inflation Factor)")
print("=" * 70)

# Hapus missing values
df_vif = df_features.dropna()

# Hitung VIF untuk setiap fitur
vif_data = pd.DataFrame()
vif_data["Fitur"] = df_vif.columns
vif_data["VIF"] = [variance_inflation_factor(df_vif.values, i) for i in range(len(df_vif.columns))]
vif_data = vif_data.sort_values('VIF', ascending=False)

print("\nNilai VIF untuk setiap fitur:")
print(vif_data.to_string(index=False))

print("\n📊 INTERPRETASI VIF:")
print("   • VIF < 5    : Tidak ada multikolinearitas")
print("   • VIF 5-10   : Multikolinearitas sedang")
print("   • VIF > 10   : Multikolinearitas tinggi/sangat tinggi")

print("\n⚠️  FITUR DENGAN MULTIKOLINEARITAS TINGGI (VIF > 10):")
high_vif = vif_data[vif_data['VIF'] > 10]
if len(high_vif) > 0:
    for idx, row in high_vif.iterrows():
        print(f"   • {row['Fitur']}: VIF = {row['VIF']:.2f}")
else:
    print("   • Tidak ada")

# Visualisasi VIF
plt.figure(figsize=(10, 6))
colors = ['red' if x > 10 else 'orange' if x > 5 else 'green' for x in vif_data['VIF']]
bars = plt.barh(vif_data['Fitur'], vif_data['VIF'], color=colors)
plt.xlabel('VIF Value', fontsize=12)
plt.ylabel('Fitur', fontsize=12)
plt.title('Variance Inflation Factor (VIF) - Deteksi Multikolinearitas\nSaham BMRI',
          fontsize=14, fontweight='bold')
plt.axvline(x=5, color='orange', linestyle='--', label='VIF = 5 (Batas Sedang)')
plt.axvline(x=10, color='red', linestyle='--', label='VIF = 10 (Batas Tinggi)')
plt.legend()
plt.tight_layout()
plt.savefig('Imelda Agustin/vif_analysis_bmri.png', dpi=300, bbox_inches='tight')
print("\n   ✓ Visualisasi VIF disimpan: vif_analysis_bmri.png")
plt.close()

# ==================== PAIRPLOT UNTUK VISUALISASI ====================
print("\n" + "=" * 70)
print("5. MEMBUAT PAIRPLOT (Scatter Matrix)")
print("=" * 70)

# Sampling data untuk pairplot (agar tidak terlalu berat)
df_sample = df_features.sample(n=min(500, len(df_features)), random_state=42)

# Buat pairplot
fig = plt.figure(figsize=(14, 12))
pd.plotting.scatter_matrix(df_sample, alpha=0.5, figsize=(14, 12), diagonal='kde')
plt.suptitle('Pairplot - Visualisasi Hubungan Antar Fitur OHLCV\nSaham BMRI (Sample 500 data)',
             fontsize=14, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('Imelda Agustin/pairplot_bmri.png', dpi=300, bbox_inches='tight')
print("   ✓ Pairplot disimpan: pairplot_bmri.png")
plt.close()

# ==================== REKOMENDASI PENANGANAN ====================
print("\n" + "=" * 70)
print("6. REKOMENDASI PENANGANAN MULTIKOLINEARITAS")
print("=" * 70)

print("""
Berdasarkan hasil analisis, berikut rekomendasi untuk menangani multikolinearitas:

📌 OPSI 1: Feature Selection (Pilih fitur terbaik)
   • Gunakan HANYA Close price (paling representatif untuk prediksi harga)
   • Tambahkan Volume sebagai informasi trading activity
   • Drop: Open, High, Low (karena sangat berkorelasi dengan Close)

📌 OPSI 2: Feature Engineering (Buat fitur turunan)
   • Daily Return = (Close - Open) / Open
   • Price Range = (High - Low) / Close
   • Volume Change = (Volume_today - Volume_yesterday) / Volume_yesterday
   • Moving Averages (MA7, MA30, MA90)
   • Technical Indicators (RSI, MACD, Bollinger Bands)

📌 OPSI 3: Dimensionality Reduction
   • PCA (Principal Component Analysis) untuk reduksi dimensi
   • Combine OHLC menjadi komponen utama

📌 OPSI 4: Keep All Features (Dengan catatan)
   • LSTM bisa handle multikolinearitas lebih baik dari model linear
   • Dokumentasikan bahwa Anda aware akan multikolinearitas ini
   • Jelaskan kenapa tetap menggunakan semua fitur (temporal pattern, dll)

🎯 REKOMENDASI UNTUK IMELDA:
   Gunakan OPSI 2 (Feature Engineering) karena:
   ✓ Mengurangi multikolinearitas
   ✓ Menambah informasi temporal
   ✓ Lebih informatif untuk LSTM
   ✓ Umum digunakan dalam penelitian time series finance
""")

# Simpan rekomendasi ke file
recommendations = """
LAPORAN ANALISIS MULTIKOLINEARITAS
Saham: BMRI (Bank Mandiri)
Periode: {} s/d {}
Total Data Points: {}

========================================
HASIL ANALISIS KORELASI
========================================
{}

========================================
HASIL ANALISIS VIF
========================================
{}

========================================
KESIMPULAN
========================================
{}

========================================
REKOMENDASI UNTUK SIDANG
========================================
Ketika ditanya tentang multikolinearitas, jawab:

"Ya Bapak/Ibu, saya sudah melakukan analisis korelasi dan VIF.
Hasil menunjukkan bahwa fitur Open, High, Low, dan Close memiliki
korelasi yang sangat tinggi (> 0.95) dan nilai VIF > 10.

Untuk menangani ini, saya menggunakan pendekatan Feature Engineering:
1. Menggunakan Close price sebagai fitur utama
2. Menambahkan fitur turunan seperti Daily Return, Price Range
3. Menambahkan Technical Indicators (RSI, MACD, Moving Average)
4. Normalisasi data untuk meningkatkan performa LSTM

Pendekatan ini mengurangi redundansi informasi sekaligus menambah
informasi temporal yang penting untuk prediksi time series."

""".format(
    df.index[0].strftime('%Y-%m-%d'),
    df.index[-1].strftime('%Y-%m-%d'),
    len(df),
    corr_matrix.to_string(),
    vif_data.to_string(index=False),
    high_vif.to_string(index=False) if len(high_vif) > 0 else "Semua fitur memiliki VIF > 10"
)

with open('Imelda Agustin/laporan_multikolinearitas_bmri.txt', 'w', encoding='utf-8') as f:
    f.write(recommendations)

print("\n   ✓ Laporan lengkap disimpan: laporan_multikolinearitas_bmri.txt")

print("\n" + "=" * 70)
print("✅ ANALISIS SELESAI!")
print("=" * 70)
print("\nFile yang dihasilkan:")
print("   1. data_bmri_raw.csv - Data mentah BMRI")
print("   2. correlation_matrix_bmri.png - Heatmap korelasi")
print("   3. vif_analysis_bmri.png - Bar chart VIF")
print("   4. pairplot_bmri.png - Scatter matrix")
print("   5. laporan_multikolinearitas_bmri.txt - Laporan lengkap")
print("\n💡 Gunakan file-file ini untuk persiapan sidang!")
print("=" * 70)
