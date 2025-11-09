import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Column Navigasi")
st.caption("Bagian 2: Spaced-Out Columns")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

st.title("Spaced-Out Columns")

from PIL import Image

img = Image.open("../../praktikum01/assets/kucingpembuka.jpg")

# Defining two Rows
for _ in range(2):
    # Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image("../../praktikum01/assets/kucingpembuka.jpg")
    cols[1].image("../../praktikum01/assets/kucing1.jpg")
    cols[2].image("../../praktikum01/assets/kucing2.jpg")
    cols[3].image("../../praktikum01/assets/kucing3.jpg")