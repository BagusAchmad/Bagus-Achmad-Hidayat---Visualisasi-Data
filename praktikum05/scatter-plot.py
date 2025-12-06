import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================
# Bagian Header
# ============================
st.title("Praktikum 5 - Scatter Plot")
st.caption("Bagian 2: Scatter Plot")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076  
2. **BAGUS ACHMAD HIDAYAT** - 0110222002  
3. AZRIL PUTRA SYAHRI - 0110222197
""")

# ============================
# DATASET
# ============================
suhu =  [20,22,24,26,28,30,32,34,36]
penjualan = [50,60,70,90,100,130,110,150,180]

penjualan_weekdays = [50,60,70,80,90,100,110,120,130]
penjualan_weekend = [60,70,80,100,110,120,140,160,200]

data = {
    'Suhu': suhu,
    'Penjualan Coklat': [40,45,50,55,60,65,70,75,80],
    'Penjualan Vanila': [82,80,78,76,77,80,82,85,88],
    'Penjualan Stroberi': [55,50,55,60,65,60,65,70,72],
    'Kelembapan': [50,65,70,75,80,85,90,95,100]
}

df = pd.DataFrame(data)

# ============================
# SIDEBAR MENU
# ============================
st.sidebar.header("Pengaturan Visualisasi")
option = st.sidebar.selectbox(
    "Pilih Jenis Visualisasi:",
    [
        "Basic Scatter Plot",
        "Kostumisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    ]
)

# ============================
# 1. Basic Scatter Plot
# ============================
def basic_scatter_plot():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title("Hubungan Penjualan Es Krim dengan Suhu")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan Es Krim")
    st.pyplot(fig)

# ============================
# 2. Custom Scatter Plot
# ============================
def custom_scatter():
    st.subheader("2. Kostumisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', s=100, alpha=0.7, edgecolors='black')
    ax.set_title("Hubungan Penjualan Es Krim dengan Suhu")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan Es Krim")
    ax.grid(True)
    st.pyplot(fig)

# ============================
# 3. Multiple Scatter Plot
# ============================
def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color="green", label="Hari Kerja", s=80)
    ax.scatter(suhu, penjualan_weekend, color="purple", label="Akhir Pekan", s=80)
    ax.set_title("Perbandingan Penjualan pada Hari Kerja vs Akhir Pekan")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan Es Krim")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# ============================
# 4. Analisis 3 Variabel
# ============================
def scatter_3_variabel():
    st.subheader("4. Analisis Scatter Plot dengan 3 Variabel")

    jenis_eskrim = st.selectbox("Pilih Jenis Es Krim:", ["Coklat", "Vanila", "Stroberi"])

    if jenis_eskrim == "Coklat":
        penjualan_es = df["Penjualan Coklat"]
    elif jenis_eskrim == "Vanila":
        penjualan_es = df["Penjualan Vanila"]
    else:
        penjualan_es = df["Penjualan Stroberi"]

    fig, ax = plt.subplots()
    scatter = ax.scatter(df["Suhu"], penjualan_es, c=df["Kelembapan"], cmap="coolwarm", s=100, alpha=0.7)

    ax.set_title(f"Penjualan Es Krim {jenis_eskrim} vs Suhu dan Kelembapan")
    ax.set_xlabel("Suhu")
    ax.set_ylabel(f"Penjualan {jenis_eskrim}")

    fig.colorbar(scatter, label="Kelembapan (%)")

    st.pyplot(fig)

    st.subheader("Analisis Hubungan")
    st.write(
        f"Grafik menunjukkan hubungan antara **Suhu**, **Kelembapan**, "
        f"dan **Penjualan Es Krim {jenis_eskrim}**."
    )

# ============================
# ROUTING MENU
# ============================
if option == "Basic Scatter Plot":
    basic_scatter_plot()
elif option == "Kostumisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter()
elif option == "Analisis Scatter Plot":
    scatter_3_variabel()
