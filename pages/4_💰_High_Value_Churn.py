import streamlit as st
import pandas as pd
import altair as alt

st.title("💰 High-Value Customer Churn Explorer")

df = pd.read_csv("data/bank.csv")

st.sidebar.header("Filters")

credit_min = st.sidebar.slider("Minimum Credit Score:", 300, 900, 650)
balance_min = st.sidebar.slider("Minimum Balance:", 0, int(df["Balance"].max()), 50000)
products_min = st.sidebar.slider("Min Products Owned:", 1, 4, 2)

filtered = df[
    (df["CreditScore"] >= credit_min) &
    (df["Balance"] >= balance_min) &
    (df["NumOfProducts"] >= products_min)
]

st.write(f"### Matching Customers: {len(filtered)}")

churn_rate = filtered["Exited"].mean() * 100
st.metric("Churn Rate for High-Value Customers", f"{churn_rate:.2f}%")

st.subheader("Balance vs Churn")

chart = alt.Chart(filtered).mark_circle().encode(
    x="Balance",
    y="CreditScore",
    color="Exited:N",
    tooltip=["Balance", "CreditScore", "Exited"]
).properties(width=700, height=400)

st.altair_chart(chart)
