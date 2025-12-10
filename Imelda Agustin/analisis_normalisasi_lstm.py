"""
ANALISIS MENDALAM: Apakah Normalisasi Min-Max Benar-Benar Diperlukan untuk LSTM?

Pertanyaan kritis untuk sidang:
"Mengapa menggunakan normalisasi Min-Max? Apakah ada alternatif yang lebih baik?"

Analisis ini akan menguji:
1. Min-Max Normalization (0-1)
2. Standardization (Z-score)
3. Robust Scaler (resistant to outliers)
4. No Normalization (menggunakan Returns)
5. Log Transformation

Author: Imelda Agustin (F1E122002)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
import yfinance as yf
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 80)
print("ANALISIS NORMALISASI UNTUK LSTM - PREDIKSI SAHAM BMRI")
print("=" * 80)

# ==================== DOWNLOAD DATA ====================
print("\n1. Download data BMRI...")
ticker = "BMRI.JK"
start_date = "2020-01-01"
end_date = datetime.now().strftime("%Y-%m-%d")

df = yf.download(ticker, start=start_date, end=end_date, progress=False)

# Flatten MultiIndex columns
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

print(f"   ✓ Data downloaded: {len(df)} data points")
print(f"   ✓ Periode: {df.index[0].date()} s/d {df.index[-1].date()}")

# Fokus pada Close price
close_prices = df['Close'].values.reshape(-1, 1)

# ==================== ANALISIS DISTRIBUSI DATA ====================
print("\n" + "=" * 80)
print("2. ANALISIS DISTRIBUSI DATA")
print("=" * 80)

print(f"\nStatistik Close Price BMRI:")
print(f"   Mean (μ):     Rp {df['Close'].mean():.2f}")
print(f"   Std Dev (σ):  Rp {df['Close'].std():.2f}")
print(f"   Min:          Rp {df['Close'].min():.2f}")
print(f"   Max:          Rp {df['Close'].max():.2f}")
print(f"   Range:        Rp {df['Close'].max() - df['Close'].min():.2f}")
print(f"   Median:       Rp {df['Close'].median():.2f}")
print(f"   Q1 (25%):     Rp {df['Close'].quantile(0.25):.2f}")
print(f"   Q3 (75%):     Rp {df['Close'].quantile(0.75):.2f}")
print(f"   IQR:          Rp {df['Close'].quantile(0.75) - df['Close'].quantile(0.25):.2f}")

# Cek stationarity dengan visual
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1: Time series original
axes[0, 0].plot(df.index, df['Close'], linewidth=1)
axes[0, 0].set_title('Close Price - Time Series Original', fontweight='bold')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Price (Rp)')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Histogram
axes[0, 1].hist(df['Close'], bins=50, edgecolor='black', alpha=0.7)
axes[0, 1].set_title('Distribusi Close Price', fontweight='bold')
axes[0, 1].set_xlabel('Price (Rp)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].axvline(df['Close'].mean(), color='red', linestyle='--', label='Mean')
axes[0, 1].axvline(df['Close'].median(), color='green', linestyle='--', label='Median')
axes[0, 1].legend()

# Plot 3: Returns distribution
returns = df['Close'].pct_change().dropna()
axes[1, 0].hist(returns, bins=50, edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Distribusi Daily Returns', fontweight='bold')
axes[1, 0].set_xlabel('Returns (%)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].axvline(returns.mean(), color='red', linestyle='--', label=f'Mean: {returns.mean():.4f}')
axes[1, 0].legend()

# Plot 4: Box plot
axes[1, 1].boxplot([df['Close']], labels=['Close Price'])
axes[1, 1].set_title('Box Plot - Deteksi Outliers', fontweight='bold')
axes[1, 1].set_ylabel('Price (Rp)')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Imelda Agustin/distribusi_data_bmri.png', dpi=300, bbox_inches='tight')
print("\n   ✓ Visualisasi distribusi disimpan: distribusi_data_bmri.png")
plt.close()

# ==================== UJI BERBAGAI METODE NORMALISASI ====================
print("\n" + "=" * 80)
print("3. PERBANDINGAN METODE NORMALISASI")
print("=" * 80)

# Prepare data untuk perbandingan
methods = {}

# Method 1: Min-Max Normalization (0-1)
print("\n📌 METHOD 1: Min-Max Normalization")
minmax_scaler = MinMaxScaler(feature_range=(0, 1))
minmax_normalized = minmax_scaler.fit_transform(close_prices)
methods['Min-Max (0-1)'] = minmax_normalized.flatten()
print(f"   Range: [{minmax_normalized.min():.4f}, {minmax_normalized.max():.4f}]")
print(f"   Mean: {minmax_normalized.mean():.4f}")
print(f"   Std: {minmax_normalized.std():.4f}")
print("   ✓ Kelebihan: Output dalam range [0,1], mudah diinterpretasi")
print("   ✗ Kekurangan: Sensitif terhadap outliers, tidak robust untuk data baru di luar range")

# Method 2: Standardization (Z-score)
print("\n📌 METHOD 2: Standardization (Z-score)")
standard_scaler = StandardScaler()
standardized = standard_scaler.fit_transform(close_prices)
methods['Standardization'] = standardized.flatten()
print(f"   Range: [{standardized.min():.4f}, {standardized.max():.4f}]")
print(f"   Mean: {standardized.mean():.4f}")
print(f"   Std: {standardized.std():.4f}")
print("   ✓ Kelebihan: Tidak terbatas pada range tertentu, robust untuk data baru")
print("   ✓ Kelebihan: Preserve outliers (penting untuk deteksi anomali)")
print("   ✗ Kekurangan: Output tidak bounded")

# Method 3: Robust Scaler
print("\n📌 METHOD 3: Robust Scaler (Median + IQR)")
robust_scaler = RobustScaler()
robust_scaled = robust_scaler.fit_transform(close_prices)
methods['Robust Scaler'] = robust_scaled.flatten()
print(f"   Range: [{robust_scaled.min():.4f}, {robust_scaled.max():.4f}]")
print(f"   Median: {np.median(robust_scaled):.4f}")
print(f"   IQR: {np.percentile(robust_scaled, 75) - np.percentile(robust_scaled, 25):.4f}")
print("   ✓ Kelebihan: SANGAT robust terhadap outliers")
print("   ✓ Kelebihan: Menggunakan median (bukan mean)")
print("   ✗ Kekurangan: Kurang umum digunakan dalam literatur")

# Method 4: Log Transformation
print("\n📌 METHOD 4: Log Transformation")
log_transformed = np.log(close_prices)
log_normalized = (log_transformed - log_transformed.mean()) / log_transformed.std()
methods['Log Transform'] = log_normalized.flatten()
print(f"   Range: [{log_normalized.min():.4f}, {log_normalized.max():.4f}]")
print(f"   Mean: {log_normalized.mean():.4f}")
print(f"   Std: {log_normalized.std():.4f}")
print("   ✓ Kelebihan: Bagus untuk data dengan pertumbuhan eksponensial")
print("   ✓ Kelebihan: Mengurangi skewness")
print("   ✗ Kekurangan: Tidak bisa handle nilai negatif atau nol")

# Method 5: No Normalization - Using Returns
print("\n📌 METHOD 5: No Normalization - Direct Returns")
returns_data = df['Close'].pct_change().fillna(0).values
methods['Returns (No Norm)'] = returns_data
print(f"   Range: [{returns_data.min():.4f}, {returns_data.max():.4f}]")
print(f"   Mean: {returns_data.mean():.4f}")
print(f"   Std: {returns_data.std():.4f}")
print("   ✓ Kelebihan: TERBAIK - Scale-free, stationary")
print("   ✓ Kelebihan: Tidak perlu normalisasi, langsung meaningful")
print("   ✓ Kelebihan: Umum digunakan dalam finance time series")
print("   ✗ Kekurangan: Harus convert kembali ke harga untuk prediksi")

# Visualisasi perbandingan
fig, axes = plt.subplots(3, 2, figsize=(16, 12))
axes = axes.flatten()

for idx, (method_name, data) in enumerate(methods.items()):
    axes[idx].plot(data, linewidth=0.8, alpha=0.8)
    axes[idx].set_title(f'{method_name}', fontweight='bold', fontsize=11)
    axes[idx].set_xlabel('Time Index')
    axes[idx].set_ylabel('Normalized Value')
    axes[idx].grid(True, alpha=0.3)
    axes[idx].axhline(y=0, color='red', linestyle='--', alpha=0.5, linewidth=1)

    # Add statistics box
    stats_text = f'Mean: {data.mean():.3f}\nStd: {data.std():.3f}\nMin: {data.min():.3f}\nMax: {data.max():.3f}'
    axes[idx].text(0.02, 0.98, stats_text, transform=axes[idx].transAxes,
                   verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
                   fontsize=8)

# Original data
axes[5].plot(df['Close'], linewidth=0.8, alpha=0.8, color='black')
axes[5].set_title('Original Close Price', fontweight='bold', fontsize=11)
axes[5].set_xlabel('Date')
axes[5].set_ylabel('Price (Rp)')
axes[5].grid(True, alpha=0.3)

plt.suptitle('Perbandingan Metode Normalisasi untuk LSTM', fontsize=14, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('Imelda Agustin/perbandingan_normalisasi.png', dpi=300, bbox_inches='tight')
print("\n   ✓ Visualisasi perbandingan disimpan: perbandingan_normalisasi.png")
plt.close()

# ==================== ANALISIS MASALAH MIN-MAX ====================
print("\n" + "=" * 80)
print("4. MASALAH KHUSUS DENGAN MIN-MAX NORMALIZATION")
print("=" * 80)

print("\n⚠️  MASALAH 1: Data Baru di Luar Range Training")
print("-" * 80)
# Simulasi: training pada 80% pertama, testing pada 20% terakhir
split_idx = int(len(close_prices) * 0.8)
train_data = close_prices[:split_idx]
test_data = close_prices[split_idx:]

# Fit scaler hanya pada training data
minmax_train = MinMaxScaler()
train_normalized = minmax_train.fit_transform(train_data)
test_normalized = minmax_train.transform(test_data)

print(f"Training data range: Rp {train_data.min():.2f} - Rp {train_data.max():.2f}")
print(f"Testing data range:  Rp {test_data.min():.2f} - Rp {test_data.max():.2f}")
print(f"\nSetelah normalisasi:")
print(f"Training normalized: [{train_normalized.min():.4f}, {train_normalized.max():.4f}]")
print(f"Testing normalized:  [{test_normalized.min():.4f}, {test_normalized.max():.4f}]")

if test_normalized.max() > 1.0 or test_normalized.min() < 0.0:
    print(f"\n❌ MASALAH: Testing data keluar dari range [0,1]!")
    print(f"   Nilai maksimum: {test_normalized.max():.4f} (seharusnya ≤ 1.0)")
    print(f"   Model LSTM yang dilatih dengan range [0,1] akan bingung!")
else:
    print(f"\n✓ Testing data masih dalam range [0,1]")

print("\n⚠️  MASALAH 2: Outliers")
print("-" * 80)
# Detect outliers menggunakan IQR method
Q1 = df['Close'].quantile(0.25)
Q3 = df['Close'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Close'] < lower_bound) | (df['Close'] > upper_bound)]
print(f"Jumlah outliers detected: {len(outliers)} dari {len(df)} data ({len(outliers)/len(df)*100:.2f}%)")
if len(outliers) > 0:
    print(f"Outlier range: Rp {outliers['Close'].min():.2f} - Rp {outliers['Close'].max():.2f}")
    print("❌ Min-Max sangat dipengaruhi oleh outliers ini!")
    print("✓ Robust Scaler atau Standardization lebih baik handle outliers")

print("\n⚠️  MASALAH 3: Non-Stationary Time Series")
print("-" * 80)
print("Harga saham adalah non-stationary (memiliki trend naik/turun)")
print("❌ Min-Max tidak mengatasi non-stationarity")
print("✓ Returns/log-returns membuat data menjadi stationary")

# ==================== REKOMENDASI ====================
print("\n" + "=" * 80)
print("5. REKOMENDASI UNTUK IMELDA")
print("=" * 80)

recommendations = """
🎯 REKOMENDASI TERBAIK: GUNAKAN RETURNS TANPA NORMALISASI TAMBAHAN

ALASAN:
✓ Returns sudah scale-free (tidak perlu normalisasi)
✓ Returns lebih stationary dibanding harga absolut
✓ Returns lebih meaningful dalam konteks finance
✓ Menghindari masalah data baru di luar range training
✓ Tidak sensitif terhadap outliers
✓ Umum digunakan dalam literatur finance time series

JIKA TETAP INGIN NORMALISASI:
Ranking metode (dari terbaik ke terburuk):

1. 🥇 STANDARDIZATION (Z-score) - REKOMENDASI TERBAIK
   ✓ Robust untuk data baru
   ✓ Preserve outliers
   ✓ Tidak terbatas pada range tertentu
   ✓ Banyak digunakan dalam deep learning
   Formula: x_norm = (x - μ) / σ

2. 🥈 ROBUST SCALER
   ✓ Paling robust terhadap outliers
   ✓ Menggunakan median dan IQR
   Formula: x_norm = (x - median) / IQR

3. 🥉 MIN-MAX NORMALIZATION
   ⚠️ HANYA jika Anda yakin data testing tidak akan keluar dari range training
   ⚠️ Sensitif terhadap outliers
   ⚠️ Bisa bermasalah untuk data time series yang trending
   Formula: x_norm = (x - min) / (max - min)

📝 UNTUK SIDANG, JAWAB SEPERTI INI:

Pertanyaan: "Mengapa menggunakan normalisasi Min-Max?"

Jawaban yang LEBIH BAIK:
"Setelah analisis mendalam, saya memutuskan menggunakan STANDARDIZATION (Z-score)
karena lebih robust untuk time series data. Standardization tidak membatasi data
dalam range tertentu, sehingga jika ada harga baru di luar range training, model
tetap bisa handle dengan baik. Selain itu, saya juga menggunakan returns sebagai
fitur tambahan yang sudah scale-free dan lebih stationary."

ATAU jika sudah terlanjur pakai Min-Max:
"Saya menggunakan Min-Max normalization untuk membatasi nilai dalam range [0,1]
sesuai dengan activation function LSTM (tanh, sigmoid). Namun saya aware bahwa
Min-Max sensitif terhadap outliers dan data baru di luar range training, sehingga
saya pastikan melakukan proper train-test split dan monitoring jika ada nilai
yang exceed range [0,1]."

🔬 EKSPERIMEN YANG BISA DILAKUKAN:
1. Train LSTM dengan berbagai metode normalisasi
2. Bandingkan MSE, RMSE, MAPE pada test set
3. Pilih metode dengan error terkecil
4. Dokumentasikan hasil eksperimen di skripsi
"""

print(recommendations)

# Save recommendations
with open('Imelda Agustin/rekomendasi_normalisasi.txt', 'w', encoding='utf-8') as f:
    f.write("ANALISIS NORMALISASI UNTUK LSTM - PREDIKSI SAHAM BMRI\n")
    f.write("=" * 80 + "\n\n")
    f.write(f"Data: BMRI.JK\n")
    f.write(f"Periode: {df.index[0].date()} s/d {df.index[-1].date()}\n")
    f.write(f"Total data: {len(df)} points\n\n")
    f.write(recommendations)

print("\n   ✓ Rekomendasi disimpan: rekomendasi_normalisasi.txt")

# ==================== CREATE COMPARISON TABLE ====================
print("\n" + "=" * 80)
print("6. TABEL PERBANDINGAN METODE NORMALISASI")
print("=" * 80)

comparison_df = pd.DataFrame({
    'Metode': ['Min-Max', 'Standardization', 'Robust Scaler', 'Log Transform', 'Returns (No Norm)'],
    'Range Output': ['[0, 1]', '[-∞, +∞]', '[-∞, +∞]', '[-∞, +∞]', 'Varies'],
    'Robust to Outliers': ['❌ Tidak', '✓ Ya', '✓✓ Sangat Ya', '✓ Ya', '✓✓ Sangat Ya'],
    'Handle New Data': ['❌ Buruk', '✓✓ Baik', '✓✓ Baik', '✓ Cukup', '✓✓✓ Excellent'],
    'Stationary': ['❌ Tidak', '❌ Tidak', '❌ Tidak', '✓ Lebih baik', '✓✓ Ya'],
    'Finance Literature': ['✓ Jarang', '✓✓ Sering', '✓ Jarang', '✓ Kadang', '✓✓✓ Sangat Sering'],
    'Rekomendasi': ['3/5', '5/5', '4/5', '3/5', '5/5']
})

print("\n" + comparison_df.to_string(index=False))

# Save to CSV
comparison_df.to_csv('Imelda Agustin/perbandingan_normalisasi.csv', index=False)
print("\n   ✓ Tabel perbandingan disimpan: perbandingan_normalisasi.csv")

# ==================== SUMMARY ====================
print("\n" + "=" * 80)
print("✅ ANALISIS SELESAI!")
print("=" * 80)
print("\nFile yang dihasilkan:")
print("   1. distribusi_data_bmri.png - Analisis distribusi data")
print("   2. perbandingan_normalisasi.png - Visual perbandingan semua metode")
print("   3. rekomendasi_normalisasi.txt - Rekomendasi detail")
print("   4. perbandingan_normalisasi.csv - Tabel perbandingan")
print("\n🎯 KESIMPULAN:")
print("   • Min-Max BUKAN pilihan terbaik untuk time series stock prediction")
print("   • Gunakan STANDARDIZATION atau RETURNS tanpa normalisasi")
print("   • Pastikan dokumentasi alasan pemilihan metode di skripsi")
print("=" * 80)
