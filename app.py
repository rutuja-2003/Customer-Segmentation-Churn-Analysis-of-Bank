import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Bank Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# LOAD DATA
# ----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/bank.csv")

df = load_data()

# ----------------------------
# SIDEBAR TITLE
# ----------------------------
st.sidebar.markdown("## 🏦 Bank Churn Dashboard")

# ----------------------------
# GLOBAL FILTERS
# ----------------------------
st.sidebar.header("🔎 Global Filters")

geo_filter = st.sidebar.multiselect(
    "Select Geography",
    options=df["Geography"].unique(),
    default=df["Geography"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# Apply filters
df = df[
    (df["Geography"].isin(geo_filter)) &
    (df["Gender"].isin(gender_filter))
]

# ----------------------------
# PAGE HEADER
# ----------------------------
st.markdown("""
    <h1 style="text-align:center; color:#a78bfa;">
        📊 Customer Churn – Executive Summary
    </h1>
    <p style="text-align:center; font-size:18px; color:#e0e0ff;">
        A high-level overview of churn patterns across the bank’s customer base.
    </p>
""", unsafe_allow_html=True)

st.write("")

# ----------------------------
# KPI CARDS
# ----------------------------
total_customers = len(df)
churned = df["Exited"].sum()
retained = total_customers - churned
churn_rate = round((churned / total_customers) * 100, 2)

active_rate = round((df["IsActiveMember"].mean()) * 100, 2)
avg_balance = int(df["Balance"].mean())

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    label="👥 Total Customers",
    value=f"{total_customers:,}"
)

kpi2.metric(
    label="❌ Customers Churned",
    value=f"{churned:,}",
    delta=f"{churn_rate}% churn rate"
)

kpi3.metric(
    label="✅ Customers Retained",
    value=f"{retained:,}"
)

kpi4.metric(
    label="⚡ Active Customer %",
    value=f"{active_rate}%"
)

st.write("---")

# ----------------------------
# CHURN DISTRIBUTION
# ----------------------------
col1, col2 = st.columns([1.2, 1])

with col1:
    churn_df = df["Exited"].value_counts().reset_index()
    churn_df.columns = ["Churn", "Count"]
    churn_df["Churn"] = churn_df["Churn"].map({0: "Retained", 1: "Churned"})

    fig = px.pie(
        churn_df,
        names="Churn",
        values="Count",
        color="Churn",
        color_discrete_map={
            "Retained": "#7dd3fc",
            "Churned": "#f472b6"
        },
        title="Customer Churn Distribution",
        hole=0.45
    )

    fig.update_layout(title_x=0.25)

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("""
        ### 📌 Key Insights
        
        • The overall churn rate indicates a measurable loss of customers.  
        
        • Customer retention remains relatively strong, but targeted strategies are required to reduce churn.  
        
        • Demographic and behavioral patterns such as **age, tenure, and geography** play a significant role in customer attrition.  
        
        • Identifying high-risk segments helps banks implement **proactive retention strategies**.
    """)

st.write("---")

# ----------------------------
# DATA SUMMARY TABLE
# ----------------------------
summary_df = pd.DataFrame({
    "Metric": [
        "Total Customers",
        "Customers Churned",
        "Customers Retained",
        "Churn Rate (%)",
        "Active Customer (%)",
        "Average Balance"
    ],
    "Value": [
        total_customers,
        churned,
        retained,
        churn_rate,
        active_rate,
        avg_balance
    ]
})

st.subheader("📋 Data Summary")

st.dataframe(summary_df, use_container_width=True)
