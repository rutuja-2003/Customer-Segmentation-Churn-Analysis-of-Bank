import streamlit as st
import pandas as pd

st.title("📊 Churn Summary Overview")

df = pd.read_csv("data/bank.csv")

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric-value'>{len(df)}</div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-label'>Total Customers</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    churn_rate = df['Exited'].mean() * 100
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric-value'>{churn_rate:.2f}%</div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-label'>Overall Churn Rate</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    active = len(df[df['Exited'] == 0])
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric-value'>{active}</div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-label'>Active Customers</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
