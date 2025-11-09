import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Alert Box")
st.caption("Bagian 10: Alert Box")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

st.success("Successful")
st.warning("Warning")
st.info("Info")
st.error("Error")
st.exception(Exception("It is an exception"))