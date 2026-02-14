import streamlit as st
import pandas as pd

st.title("📊 Overall Churn Summary")

df = pd.read_csv("data/bank.csv")

# KPIs
total_customers = len(df)
churned = df[df["Exited"] == 1].shape[0]
active = df[df["Exited"] == 0].shape[0]
churn_rate = churned / total_customers * 100

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", total_customers)
col2.metric("Churned Customers", churned)
col3.metric("Churn Rate (%)", f"{churn_rate:.2f}%")

st.subheader("Churn Distribution")
st.bar_chart(df["Exited"].value_counts())
