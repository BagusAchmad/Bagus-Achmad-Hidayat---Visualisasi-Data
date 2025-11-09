import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Visualisasi Data")
st.caption("Bagian 4: Map")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

st.title("Map")
df = pd.DataFrame(
    np.random.randn(50, 2) / [10, 10] + [15.4589, 75.0078],
    columns=['lat', 'lon']
)
st.map(df)
