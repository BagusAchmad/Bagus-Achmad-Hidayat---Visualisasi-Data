import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Column Navigasi")
st.caption("Bagian 7: Empty Containers")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

st.title("Empty Containers")
import time
import streamlit as st # Asumsi import ini ada di bagian atas file

# Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    
    st.write("✔️ Times up!")