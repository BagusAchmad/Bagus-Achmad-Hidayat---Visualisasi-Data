import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Column Navigasi")
st.caption("Bagian 1: column")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

st.title("Column")
col1, col2 = st.columns(2)

col1.write("Ini  adalah kolom pertama")
col1.image("https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQQvuSIPCorih_h23Ir4JtYHoslDa9HzAY4nzAtg-HzbjMiByZS")
col2.write("Ini adalah kolom kedua")
col2.image("https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRxq_QUcxmIeUju09y9nrormC8w6MTIeB-5wDDFQ6DDcajHMQ4T")
