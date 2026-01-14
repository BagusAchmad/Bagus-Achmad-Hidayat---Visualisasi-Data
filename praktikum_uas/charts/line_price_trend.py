import streamlit as st
import plotly.express as px

def show(df):

    coin = st.multiselect("Pilih Coin", df["coin"].unique(), default=df["coin"].unique(), key="price_coin")
    d = df[df["coin"].isin(coin)]

    fig = px.line(d, x="date", y="close", color="coin")
    fig.update_layout(xaxis_title="Date", yaxis_title="Close Price")
    st.plotly_chart(fig, use_container_width=True)
