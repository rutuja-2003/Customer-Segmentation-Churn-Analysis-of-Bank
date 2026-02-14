import streamlit as st
import pandas as pd
import altair as alt

st.title("🗺️ Geography-wise Churn")

df = pd.read_csv("data/bank.csv")

geo_churn = df.groupby("Geography")["Exited"].mean().reset_index()
geo_churn["Churn %"] = geo_churn["Exited"] * 100

chart = alt.Chart(geo_churn).mark_bar().encode(
    x="Geography",
    y="Churn %",
    color="Geography"
).properties(width=700, height=400)

st.altair_chart(chart)
