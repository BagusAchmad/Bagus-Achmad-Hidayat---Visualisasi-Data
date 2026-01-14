import streamlit as st
import plotly.express as px

def show(df):

    year = st.selectbox("Tahun", ["All"] + sorted(df["date"].dt.year.unique()), key="box_year")
    d = df.copy()
    if year != "All":
        d = d[d["date"].dt.year == year]

    fig = px.box(d, x="coin", y="daily_return", color="coin")
    fig.update_layout(xaxis_title="Coin", yaxis_title="Daily Return (%)")
    st.plotly_chart(fig, use_container_width=True)
