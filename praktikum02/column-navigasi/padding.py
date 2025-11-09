import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Column Navigasi")
st.caption("Bagian 3: Columns with Padding")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")


from PIL import Image

img = Image.open("../../praktikum01/assets/kucing1.jpg")
st.title("Padding")

# Defining Padding with columns
col1, padding, col2 = st.columns((10, 2, 10))

with col1:
    col1.image("../../praktikum01/assets/kucing3.jpg")

with col2:
    col2.image("../../praktikum01/assets/kucing4.jpg")