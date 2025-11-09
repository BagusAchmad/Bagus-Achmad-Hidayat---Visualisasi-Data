import streamlit as st
import pandas as pd
import numpy as np

st.title("Praktikum 2 - Column Navigasi")
st.caption("Bagian 6: Containers")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

st.title("Container")

with st.container():
    st.write("Element Inside Contianer")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))

st.write("Element Outside Container")

st.title("Out of Order Container")

# Defining Contianers
container_one = st.container()
container_one.write("Element One Inside Contianer")

st.write("Element Outside Contianer")

# Now insert few more elements in the container_one
container_one.write("Element Two Inside Contianer")
container_one.line_chart(np.random.randn(40, 4))