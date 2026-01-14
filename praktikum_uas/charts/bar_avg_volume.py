import streamlit as st
import plotly.express as px

def show(df):

    year = st.selectbox("Tahun", ["All"] + sorted(df["date"].dt.year.unique()), key="avgvol_year")
    d = df.copy()
    if year != "All":
        d = d[d["date"].dt.year == year]

    avg_vol = d.groupby("coin")["volume"].mean().reset_index()

    fig = px.bar(avg_vol, x="coin", y="volume", color="coin")
    fig.update_layout(xaxis_title="Coin", yaxis_title="Average Volume")
    st.plotly_chart(fig, use_container_width=True)
