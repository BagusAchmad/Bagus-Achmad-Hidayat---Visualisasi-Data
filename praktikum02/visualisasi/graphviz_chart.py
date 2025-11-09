import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

st.title("Praktikum 2 - Visualisasi Data")
st.caption("Bagian 5: Graphviz Chart")
st.write("Kelompok 16")
st.subheader("Praktikum 2 - Anggota Kelompok:")
st.markdown("""
1. ARIA KRISTALLINACHT SUNDANIS - 0110222076
2. BAGUS ACHMAD HIDAYAT - 0110222002
3. AZRIL PUTRA SYAHRI - 0110222197
""")

st.title("Graphviz Chart")
st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
    }
""")


