import streamlit as st
import pandas as pd
import altair as alt

st.title("📈 Age & Tenure Comparison")

df = pd.read_csv("data/bank.csv")

age_churn = df.groupby("Age")["Exited"].mean().reset_index()
tenure_churn = df.groupby("Tenure")["Exited"].mean().reset_index()

st.subheader("Age vs Churn %")
chart_age = alt.Chart(age_churn).mark_line().encode(
    x="Age",
    y="Exited",
).properties(width=700, height=300)
st.altair_chart(chart_age)

st.subheader("Tenure vs Churn %")
chart_tenure = alt.Chart(tenure_churn).mark_line(color="orange").encode(
    x="Tenure",
    y="Exited",
).properties(width=700, height=300)
st.altair_chart(chart_tenure)
