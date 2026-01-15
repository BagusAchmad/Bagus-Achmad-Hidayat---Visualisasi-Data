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

/* --- KPI NEW STYLE --- */
.kpi-card{
  background: linear-gradient(135deg, #0b1220, #111827);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px;
  padding: 16px 16px;
  min-height: 120px;
  box-shadow: 0 10px 28px rgba(0,0,0,0.28);
  position: relative;
  overflow: hidden;
}
.kpi-card:before{
  content:"";
  position:absolute;
  left:-40px; top:-40px;
  width:110px; height:110px;
  background: radial-gradient(circle, rgba(249,199,79,0.30), transparent 60%);
  filter: blur(2px);
}
.kpi-top{display:flex; align-items:center; justify-content:space-between; gap:12px;}
.kpi-left{display:flex; align-items:center; gap:12px;}
.kpi-ico{
  width:38px; height:38px;
  border-radius:12px;
  display:flex; align-items:center; justify-content:center;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.10);
  font-size:18px;
}
.kpi-title{font-size:13px; opacity:0.78; color:#e5e7eb; margin-bottom:2px;}
.kpi-value{font-size:20px; font-weight:900; color:#ffffff; line-height:1.15;}
.kpi-sub{font-size:12px; opacity:0.70; color:#cbd5e1; margin-top:8px; line-height:1.35;}
.kpi-chip{
  font-size:11px;
  padding: 5px 10px;
  border-radius: 999px;
  background: rgba(249,199,79,0.16);
  border: 1px solid rgba(249,199,79,0.30);
  color:#fde68a;
  white-space:nowrap;
}

/* --- CHART ROW CARD --- */
.row-card{
  background: linear-gradient(135deg, #0b1220, #111827);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px;
  padding: 16px;
  box-shadow: 0 10px 28px rgba(0,0,0,0.28);
  margin-bottom: 14px;
}
.row-title{
  font-size:18px;
  font-weight:900;
  color:#fff;
  margin: 0 0 8px 0;
}
.row-sub{
  color:#cbd5e1;
  opacity:0.78;
  margin-top:-4px;
  margin-bottom: 12px;
  font-size: 13px;
}
/* === PENJELASAN CHART  === */
.explain-box{
  background: #ffffff;                 
  border: 1px solid #e5e7eb;           
  border-radius: 12px;
  padding: 16px;
}

.explain-title{
  font-weight: 700;
  color: #111827;                      
  margin-bottom: 8px;
  font-size: 14px;
}

.explain-text{
  color: #1f2937;                      
  font-size: 14px;
  line-height: 1.6;
}

.bullet{
  margin-top: 8px;
  padding-left: 18px;
  color: #1f2937;                      
  font-size: 14px;
  line-height: 1.6;
}

.bullet li{
  margin-bottom: 6px;
}

/* tooltip info */
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
  font-weight:900;
  font-size:12px;
}
.info:hover::after{
  content: attr(data-tip);
  position:absolute;
  bottom:135%;
  left:50%;
  transform:translateX(-50%);
  background:#0b1220;
  color:white;
  padding:10px 12px;
  border-radius:12px;
  width:300px;
  font-size:12px;
  box-shadow:0 10px 30px rgba(0,0,0,0.45);
  z-index:999;
  line-height:1.35;
  border: 1px solid rgba(255,255,255,0.08);
}

/* footer */
.footer{
  background: linear-gradient(135deg, #0b1220, #111827);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px;
  padding: 16px;
  box-shadow: 0 10px 28px rgba(0,0,0,0.28);
  color:#e5e7eb;
}

/* === KESIMPULAN  === */
.summary-text{
  color: rgba(255,255,255,0.92);
  font-size: 14px;
  line-height: 1.65;
  font-weight: 500;
}

.footer small{opacity:0.75;}
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

# ======================= KPI SECTION (NEW LAYOUT 2x2) =======================
def fmt_big(x):
    if pd.isna(x): return "-"
    x = float(x)
    if abs(x) >= 1e12: return f"{x/1e12:.2f}T"
    if abs(x) >= 1e9:  return f"{x/1e9:.2f}B"
    if abs(x) >= 1e6:  return f"{x/1e6:.2f}M"
    if abs(x) >= 1e3:  return f"{x/1e3:.2f}K"
    return f"{x:.2f}"

def kpi(col, icon, title, value, sub="", chip=""):
    col.markdown(f"""
    <div class="kpi-card">
      <div class="kpi-top">
        <div class="kpi-left">
          <div class="kpi-ico">{icon}</div>
          <div>
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
          </div>
        </div>
        <div class="kpi-chip">{chip}</div>
      </div>
      <div class="kpi-sub">{sub}</div>
    </div>
    """, unsafe_allow_html=True)

# KPI calculations
if len(dff) > 0:
    top_close = dff.loc[dff["close"].idxmax()]
    top_vol = dff.loc[dff["volume"].idxmax()]

    vol_std = dff.groupby("coin")["daily_return"].std().sort_values(ascending=False)
    most_vol_coin = vol_std.index[0]
    most_vol_val = vol_std.iloc[0]

    avg_ret = dff.groupby("coin")["daily_return"].mean().sort_values(ascending=False)
    best_coin = avg_ret.index[0]
    best_val = avg_ret.iloc[0]

    total_trx = dff["volume"].sum()
else:
    top_close = top_vol = None
    most_vol_coin = best_coin = "-"
    most_vol_val = best_val = None
    total_trx = None

rK1 = st.columns(2)
rK2 = st.columns(2)

kpi(
    rK1[0],
    "🏆",
    "Harga Penutupan Tertinggi",
    f"{top_close['coin']} • {fmt_big(top_close['close'])}" if top_close is not None else "-",
    "Nilai close terbesar pada rentang tanggal terpilih.",
    chip="Peak Close"
)
kpi(
    rK1[1],
    "📊",
    "Total Volume Perdagangan",
    fmt_big(total_trx) if total_trx is not None else "-",
    "Akumulasi volume trading semua coin pada periode terpilih.",
    chip="Total Volume"
)
kpi(
    rK2[0],
    "⚡",
    "Coin Paling Volatil",
    most_vol_coin,
    f"Standar deviasi daily return: {most_vol_val:.2f}%" if most_vol_val is not None else "-",
    chip="Risk Level"
)
kpi(
    rK2[1],
    "📈",
    "Return Harian Rata-rata Terbaik",
    best_coin,
    f"Rata-rata daily return: {best_val:.3f}%" if best_val is not None else "-",
    chip="Best Avg"
)

st.divider()

# ======================= CHARTS (1 ROW = 1 CHART + EXPLANATION) =======================
def chart_row(title, subtitle, tip, show_func, explain_paragraph, bullets):
    st.markdown(f"""
    <div class="row-card">
      <div class="row-title">{title}
        <span class="info" data-tip="{tip}">ⓘ</span>
      </div>
      <div class="row-sub">{subtitle}</div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.55, 1])
    with left:
        show_func(dff)
    with right:
        st.markdown(f"""
        <div class="explain-box">
          <div class="explain-title">Penjelasan</div>
          <div class="explain-text">{explain_paragraph}</div>
          <ul class="bullet">
            {''.join([f'<li>{b}</li>' for b in bullets])}
          </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

chart_row(
    "Perbandingan Tren Harga Penutupan",
    "Membaca arah pergerakan harga (close) dari waktu ke waktu.",
    "Bandingkan tren close antar coin untuk melihat pertumbuhan dan momen lonjakan.",
    line_price_trend.show,
    "Visualisasi ini menampilkan perubahan harga penutupan (close) untuk setiap cryptocurrency pada periode terpilih.",
    [
        "Garis naik konsisten → indikasi tren kenaikan jangka panjang.",
        "Perubahan tajam → menandakan fase pasar yang agresif/reaktif.",
        "Cocok untuk membandingkan performa antar coin dalam periode yang sama."
    ]
)

chart_row(
    "Tren Volume Perdagangan Harian",
    "Melihat intensitas aktivitas trading berdasarkan volume.",
    "Lonjakan volume sering muncul saat market sedang ramai (news, panic, euforia).",
    area_volume_trend.show,
    "Visualisasi ini menggambarkan volume perdagangan harian untuk memahami seberapa aktif pasar pada waktu tertentu.",
    [
        "Volume tinggi → aktivitas transaksi meningkat.",
        "Lonjakan volume + kenaikan harga → sinyal penguatan tren.",
        "Volume turun terus → pasar cenderung sepi/menunggu."
    ]
)

chart_row(
    "Perbandingan Rata-rata Volume",
    "Membandingkan coin yang paling aktif diperdagangkan.",
    "Rata-rata volume membantu melihat likuiditas relatif antar coin.",
    bar_avg_volume.show,
    "Visualisasi ini membandingkan rata-rata volume perdagangan tiap coin selama periode terpilih.",
    [
        "Volume rata-rata tertinggi → coin lebih likuid dan ramai.",
        "Volume rendah → aktivitas lebih kecil, potensi pergerakan bisa sporadis.",
        "Bagus untuk menilai dominasi aktivitas pasar."
    ]
)

chart_row(
    "Distribusi Volatilitas Harian",
    "Mengukur risiko fluktuasi menggunakan daily return.",
    "Boxplot memperlihatkan sebaran return dan outlier (lonjakan ekstrem).",
    box_volatility.show,
    "Visualisasi ini memperlihatkan distribusi daily return yang merepresentasikan tingkat volatilitas (risiko naik-turun).",
    [
        "Box lebih lebar → volatilitas lebih tinggi.",
        "Banyak outlier → sering terjadi perubahan ekstrem.",
        "Cocok untuk membandingkan coin yang stabil vs agresif."
    ]
)

chart_row(
    "Hubungan Harga vs Volume",
    "Menilai apakah volume besar muncul pada level harga tertentu.",
    "Scatter membantu membaca pola: volume tinggi saat harga naik/turun tajam.",
    scatter_price_volume.show,
    "Visualisasi ini menampilkan keterkaitan antara harga dan volume untuk melihat pola transaksi pada level harga tertentu.",
    [
        "Titik menyebar luas → volume aktif di banyak kondisi harga.",
        "Titik mengelompok → aktivitas besar terjadi di rentang harga tertentu.",
        "Bisa dipakai untuk membaca fase akumulasi vs distribusi."
    ]
)

chart_row(
    "Korelasi Faktor Keberhasilan",
    "Melihat hubungan antar variabel (close, volume, marketcap, return).",
    "Korelasi tinggi menandakan variabel cenderung bergerak bersama.",
    heatmap_corr.show,
    "Heatmap korelasi membantu memahami variabel mana yang paling berhubungan dengan perubahan harga dan aktivitas pasar.",
    [
        "Korelasi positif tinggi → dua variabel cenderung naik bersama.",
        "Korelasi negatif → satu naik, yang lain cenderung turun.",
        "Membantu menentukan variabel mana yang relevan untuk analisis lanjutan."
    ]
)

# ======================= KESIMPULAN (lebih enak dibaca) =======================
st.markdown("## Kesimpulan Analisis")
st.markdown("""
<div class="row-card">
  <div class="summary-text">
    Dari keseluruhan visualisasi, dashboard ini membantu membandingkan performa harga, aktivitas perdagangan, serta tingkat risiko
    antara Bitcoin, Ethereum, dan Binance Coin pada rentang waktu yang dipilih.
    KPI memberikan ringkasan cepat, sedangkan tiap chart menjawab pertanyaan spesifik: bagaimana tren harga, seberapa aktif volumenya,
    seberapa tinggi volatilitasnya, bagaimana hubungan harga-volume, dan variabel mana yang saling berkaitan.
  </div>
</div>
""", unsafe_allow_html=True)


# ======================= FOOTER (rapi, ga norak) =======================
st.markdown("""
<div class="footer">
  <div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap;">
    <div>
      <b>Final Project Mata Kuliah Visualisasi Data</b><br>
      <small>Disusun untuk memenuhi Ujian Akhir Semester (UAS)</small>
    </div>
    <div>
      <b>Kelompok 16</b><br>
      <small>
      Bagus Achmad Hidayat — Visualisasi & Dashboard<br>
      Aria Kristallinacht Sundaris — Laporan & Presentasi<br>
      Azril Putra Syahri — Laporan & Presentasi
      </small>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
