import streamlit as st
import plotly.express as px

def show(df):

    coin = st.multiselect("Pilih Coin", df["coin"].unique(), default=df["coin"].unique(), key="vol_coin")
    d = df[df["coin"].isin(coin)]

    fig = px.area(d, x="date", y="volume", color="coin")
    fig.update_layout(xaxis_title="Date", yaxis_title="Volume")
    st.plotly_chart(fig, use_container_width=True)
