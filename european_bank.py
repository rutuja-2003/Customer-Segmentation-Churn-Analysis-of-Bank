# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------------------------------------------------
# 🎯 PAGE CONFIG
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Bank Customer Churn Analysis",
    layout="wide"
)

st.title("🏦 Bank Customer Churn Dashboard (Customer Segmentation + Churn Analysis)")

# -------------------------------------------------------------------
# 📥 FILE UPLOADER
# -------------------------------------------------------------------
st.sidebar.header("📂 Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your bank churn CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # -------------------------------------------------------------------
    # 🎯 FILTER SIDEBAR (Segment Filters)
    # -------------------------------------------------------------------
    st.sidebar.header("🔍 Filters")

    geography_filter = st.sidebar.multiselect(
        "Select Geography",
        options=df["Geography"].unique(),
        default=df["Geography"].unique()
    )

    gender_filter = st.sidebar.multiselect(
        "Select Gender",
        options=df["Gender"].unique(),
        default=df["Gender"].unique()
    )

    # Apply Filters
    df_filtered = df[
        (df["Geography"].isin(geography_filter)) &
        (df["Gender"].isin(gender_filter))
    ]

    # -------------------------------------------------------------------
    # 📊 KPI SUMMARY
    # -------------------------------------------------------------------
    st.subheader("📌 Overall Churn Summary")

    total_customers = len(df_filtered)
    churned_customers = df_filtered["Exited"].sum()
    churn_rate = round((churned_customers / total_customers) * 100, 2)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", total_customers)
    col2.metric("Churned Customers", churned_customers)
    col3.metric("Churn Rate (%)", churn_rate)

    st.markdown("---")

    # -------------------------------------------------------------------
    # 🌍 GEOGRAPHY-WISE CHURN
    # -------------------------------------------------------------------
    st.subheader("🌍 Geography-wise Churn")

    geo_churn = df_filtered.groupby("Geography")["Exited"].mean().reset_index()
    geo_churn["Exited"] = geo_churn["Exited"] * 100

    fig_geo = px.bar(
        geo_churn,
        x="Geography",
        y="Exited",
        title="Churn Rate by Geography (%)",
        color="Exited",
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig_geo, use_container_width=True)

    # -------------------------------------------------------------------
    # 👴 AGE & TENURE BASED CHURN
    # -------------------------------------------------------------------
    st.subheader("📈 Age & Tenure Impact on Churn")

    colA, colB = st.columns(2)

    with colA:
        fig_age = px.histogram(
            df_filtered,
            x="Age",
            color="Exited",
            nbins=20,
            title="Churn by Age",
            barmode="overlay"
        )
        st.plotly_chart(fig_age, use_container_width=True)

    with colB:
        fig_tenure = px.histogram(
            df_filtered,
            x="Tenure",
            color="Exited",
            title="Churn by Tenure",
            barmode="overlay"
        )
        st.plotly_chart(fig_tenure, use_container_width=True)

    # -------------------------------------------------------------------
    # 💰 HIGH-VALUE CUSTOMER CHURN
    # -------------------------------------------------------------------
    st.subheader("💰 High-Value Customer Churn Explorer")

    high_value = df_filtered[df_filtered["Balance"] > df_filtered["Balance"].median()]

    fig_high_value = px.scatter(
        high_value,
        x="Balance",
        y="EstimatedSalary",
        color="Exited",
        size="Balance",
        title="High Value Customer Churn",
        hover_data=["CustomerId", "Age", "Geography"]
    )
    st.plotly_chart(fig_high_value, use_container_width=True)

    # -------------------------------------------------------------------
    # 🔍 DRILL DOWN SECTION
    # -------------------------------------------------------------------
    st.subheader("🔍 Drill-Down Customer View")

    customer_id = st.text_input("Enter Customer ID to Drill Down")

    if customer_id:
        customer_data = df_filtered[df_filtered["CustomerId"] == int(customer_id)]

        if not customer_data.empty:
            st.write("### Customer Details")
            st.dataframe(customer_data)
        else:
            st.warning("Customer ID not found in filtered dataset!")

else:
    st.info("👈 Upload a CSV file from the sidebar to begin analysis.")
