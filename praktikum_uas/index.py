import streamlit as st
import pandas as pd

from charts import (
    line_price_trend,
    area_volume_trend,
    bar_avg_volume,
    box_volatility,
    scatter_price_volume,
    heatmap_corr
)

st.set_page_config(page_title="Dashboard Cryptocurrency", layout="wide")

# ======================= LOAD DATA =======================
df = pd.read_csv("Output/crypto_merged.csv")
df["date"] = pd.to_datetime(df["date"])

# ======================= STYLE (CSS) =======================
st.markdown("""
<style>
.block-container {padding-top: 1.2rem; padding-bottom: 1.2rem;}

.center {text-align:center;}

.kpi-card{
  background: linear-gradient(135deg, #111827, #1f2937);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px;
  padding: 16px 18px;
  height: 130px;
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items:center;
  color: #fff;
  box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}
.kpi-title{font-size:13px; opacity:0.75; text-align:center;}
.kpi-value{font-size:22px; font-weight:800; margin-top:6px; text-align:center; word-break:break-word;}
.kpi-sub{font-size:12px; opacity:0.65; margin-top:4px; text-align:center;}

.info {
  display:inline-flex;
  align-items:center;
  justify-content:center;
  width:18px; height:18px;
  border-radius:999px;
  margin-left:8px;
  color:#111827;
  background:#F9C74F;
  cursor:pointer;
  position:relative;
  font-weight:800;
  font-size:12px;
}
.info:hover::after{
  content: attr(data-tip);
  position:absolute;
  bottom:135%;
  left:50%;
  transform:translateX(-50%);
  background:#111827;
  color:white;
  padding:10px 12px;
  border-radius:12px;
  width:280px;
  font-size:12px;
  box-shadow:0 10px 30px rgba(0,0,0,0.45);
  z-index:999;
  line-height:1.35;
}
</style>
""", unsafe_allow_html=True)

# ======================= HEADER =======================
st.markdown("""
<h1 class="center">Analisis Visual Pergerakan Harga Cryptocurrency</h1>
<p class="center" style="opacity:0.72; margin-top:-6px;">
Perbandingan Tren, Volatilitas, dan Volume Perdagangan Bitcoin, Ethereum, dan Binance Coin
</p>
""", unsafe_allow_html=True)

# ======================= FILTER GLOBAL =======================
with st.expander("🔎 Filter Data (Global)", expanded=True):
    cA, cB = st.columns([1,2])

    with cA:
        coin_sel = st.multiselect(
            "Pilih Cryptocurrency",
            sorted(df["coin"].unique().tolist()),
            default=sorted(df["coin"].unique().tolist())
        )

    with cB:
        min_d = df["date"].min().date()
        max_d = df["date"].max().date()
        date_range = st.date_input("Rentang Tanggal", (min_d, max_d))

# Apply global filter
dff = df.copy()
if coin_sel:
    dff = dff[dff["coin"].isin(coin_sel)]

if isinstance(date_range, tuple) and len(date_range) == 2:
    start, end = date_range
    dff = dff[(dff["date"].dt.date >= start) & (dff["date"].dt.date <= end)]

# ======================= KPI SECTION =======================
def fmt_big(x):
    if pd.isna(x): return "-"
    x = float(x)
    if abs(x) >= 1e12: return f"{x/1e12:.2f}T"
    if abs(x) >= 1e9:  return f"{x/1e9:.2f}B"
    if abs(x) >= 1e6:  return f"{x/1e6:.2f}M"
    if abs(x) >= 1e3:  return f"{x/1e3:.2f}K"
    return f"{x:.2f}"

def kpi(col, title, value, sub=""):
    col.markdown(f"""
    <div class="kpi-card">
      <div class="kpi-title">{title}</div>
      <div class="kpi-value">{value}</div>
      <div class="kpi-sub">{sub}</div>
    </div>
    """, unsafe_allow_html=True)

# KPI calculations
if len(dff) > 0:
    top_close = dff.loc[dff["close"].idxmax()]
    top_vol = dff.loc[dff["volume"].idxmax()]

    vol_std = dff.groupby("coin")["daily_return"].std().sort_values(ascending=False)
    most_vol_coin = vol_std.index[0]
    most_vol_val = f"{vol_std.iloc[0]:.2f}%"

    avg_ret = dff.groupby("coin")["daily_return"].mean().sort_values(ascending=False)
    best_coin = avg_ret.index[0]
    best_val = f"{avg_ret.iloc[0]:.3f}%"
else:
    top_close = top_vol = None
    most_vol_coin = best_coin = "-"
    most_vol_val = best_val = "-"

k1,k2,k3,k4 = st.columns(4)
kpi(k1, "🏆 Harga Penutupan Tertinggi", f"{top_close['coin']} ({fmt_big(top_close['close'])})" if top_close is not None else "-", "Dalam rentang terpilih")
kpi(k2, "📊 Volume Tertinggi", f"{top_vol['coin']} ({fmt_big(top_vol['volume'])})" if top_vol is not None else "-", "Dalam rentang terpilih")
kpi(k3, "⚡ Cryptocurrency Paling Volatil", most_vol_coin, f"Std Return: {most_vol_val}")
kpi(k4, "📈 Return Harian Rata-rata Terbaik", best_coin, f"Avg Return: {best_val}")

st.divider()

# ======================= DASHBOARD CHARTS =======================

# Row 1: Line, Area, Bar
r1 = st.columns(3)

with r1[0]:
    st.markdown("""
    <h3 style="display:flex;align-items:center;gap:8px">
      <span>Perbandingan Tren Harga Penutupan</span>
      <span class="info" data-tip="Membandingkan tren harga penutupan (close) untuk melihat pergerakan jangka panjang tiap cryptocurrency.">ⓘ</span>
    </h3>
    """, unsafe_allow_html=True)
    line_price_trend.show(dff)

with r1[1]:
    st.markdown("""
    <h3 style="display:flex;align-items:center;gap:8px">
      <span>Tren Volume Perdagangan Harian</span>
      <span class="info" data-tip="Menampilkan aktivitas perdagangan harian. Lonjakan volume sering terjadi saat pasar sedang sangat aktif.">ⓘ</span>
    </h3>
    """, unsafe_allow_html=True)
    area_volume_trend.show(dff)

with r1[2]:
    st.markdown("""
    <h3 style="display:flex;align-items:center;gap:8px">
      <span>Perbandingan Rata-rata Volume</span>
      <span class="info" data-tip="Membandingkan rata-rata volume untuk melihat coin mana yang paling aktif diperdagangkan dalam periode tertentu.">ⓘ</span>
    </h3>
    """, unsafe_allow_html=True)
    bar_avg_volume.show(dff)

# Row 2: Box, Scatter, Heatmap
r2 = st.columns(3)

with r2[0]:
    st.markdown("""
    <h3 style="display:flex;align-items:center;gap:8px">
      <span>Distribusi Volatilitas Harian</span>
      <span class="info" data-tip="Boxplot daily return menunjukkan risiko fluktuasi harga. Semakin lebar sebarannya, semakin volatil.">ⓘ</span>
    </h3>
    """, unsafe_allow_html=True)
    box_volatility.show(dff)

with r2[1]:
    st.markdown("""
    <h3 style="display:flex;align-items:center;gap:8px">
      <span>Hubungan Harga vs Volume</span>
      <span class="info" data-tip="Scatter plot membantu melihat apakah volume perdagangan tinggi cenderung terjadi pada harga tertentu atau saat lonjakan harga.">ⓘ</span>
    </h3>
    """, unsafe_allow_html=True)
    scatter_price_volume.show(dff)

with r2[2]:
    st.markdown("""
    <h3 style="display:flex;align-items:center;gap:8px">
      <span>Korelasi Faktor Keberhasilan</span>
      <span class="info" data-tip="Heatmap korelasi menunjukkan hubungan antara close, volume, marketcap dan return. Membantu memahami faktor yang paling saling berkaitan.">ⓘ</span>
    </h3>
    """, unsafe_allow_html=True)
    heatmap_corr.show(dff)

# ======================= KESIMPULAN =======================
st.markdown("## Kesimpulan Analisis")

st.write("""
Berdasarkan visualisasi yang ditampilkan:

1. **Tren harga penutupan** menunjukkan perbedaan pola pertumbuhan antara Bitcoin, Ethereum, dan Binance Coin pada periode tertentu.
2. **Volume perdagangan** menggambarkan aktivitas pasar dan dapat menjadi indikator momentum ketika terjadi lonjakan drastis.
3. **Volatilitas harian (daily return)** membantu mengidentifikasi cryptocurrency dengan risiko fluktuasi paling tinggi.
4. **Hubungan harga dan volume** menunjukkan bahwa volume besar sering terjadi pada saat harga mengalami perubahan signifikan.
5. **Korelasi variabel** membantu memahami keterkaitan antara harga, marketcap, volume, dan return, sebagai dasar analisis lebih lanjut.
""")

# ======================= FOOTER =======================
st.markdown("""
<hr>
<div style="text-align:center; opacity:0.75; font-size:13px; line-height:1.5">
<b>Final Project Mata Kuliah Visualisasi Data</b><br>
Disusun untuk memenuhi Ujian Akhir Semester (UAS)<br><br>
<b>Kelompok 16</b><br>
BAGUS ACHMAD HIDAYAT (Membuat Visualisasi Data)<br>
ARIA KRISTALLINACHT SUNDARIS (Menyusun Laporan & Presentasi)<br>
AZRIL PUTRA SYAHRI (Menyusun Laporan & Presentasi)
</div>
""", unsafe_allow_html=True)
