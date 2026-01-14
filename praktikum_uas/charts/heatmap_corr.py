import streamlit as st
import plotly.express as px

def show(df):

    coin = st.selectbox("Coin", df["coin"].unique(), key="corr_coin")
    d = df[df["coin"] == coin]

    corr = d[["close", "volume", "marketcap", "daily_return"]].corr()

    fig = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r")
    st.plotly_chart(fig, use_container_width=True)
