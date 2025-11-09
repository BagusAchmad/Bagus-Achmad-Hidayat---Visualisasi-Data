import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Column Navigasi")
st.caption("Bagian 8: Sidebars")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0, 10)