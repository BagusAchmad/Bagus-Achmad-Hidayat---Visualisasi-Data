import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Column Navigasi")
st.caption("Bagian 4: Grids")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

from PIL import Image

img = Image.open("../../praktikum01/assets/kucingpembuka.jpg")
st.title("Grid")

# Defining no of Rows
for a in range(4):
    # Defining no. of columns with size
    cols = st.columns((1, 1, 1, 1))
    cols[0].image("../../praktikum01/assets/kucingpembuka.jpg")
    cols[1].image("../../praktikum01/assets/kucing1.jpg")
    cols[2].image("../../praktikum01/assets/kucing2.jpg")
    cols[3].image("../../praktikum01/assets/kucing3.jpg")