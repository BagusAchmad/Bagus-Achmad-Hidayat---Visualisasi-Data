import streamlit as st
import plotly.express as px

def show(df):

    coin = st.selectbox("Coin", ["All"] + list(df["coin"].unique()), key="scatter_coin")
    d = df.copy()
    if coin != "All":
        d = d[d["coin"] == coin]

    fig = px.scatter(d, x="volume", y="close", color="coin")
    fig.update_layout(xaxis_title="Volume", yaxis_title="Close Price")
    st.plotly_chart(fig, use_container_width=True)
