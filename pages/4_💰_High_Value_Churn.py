import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# ----------------------------
# LOAD DATA
# ----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/bank.csv")

df = load_data()

# ----------------------------
# PAGE HEADER
# ----------------------------
st.markdown("""
<h1 style="text-align:center; color:#a78bfa;">
💰 High-Value Customer Churn Explorer
</h1>

<p style="text-align:center; font-size:18px; color:#e0e0ff;">
This module identifies churn patterns among financially valuable customers.
High-value customers contribute significantly to bank revenue, making their retention critical.
</p>
""", unsafe_allow_html=True)

st.write("")

# ----------------------------
# SIDEBAR FILTERS
# ----------------------------
st.sidebar.header("🔎 High-Value Customer Filters")

credit_min = st.sidebar.slider(
    "Minimum Credit Score",
    300,
    900,
    650
)

balance_min = st.sidebar.slider(
    "Minimum Balance",
    0,
    int(df["Balance"].max()),
    50000
)

products_min = st.sidebar.slider(
    "Minimum Products Owned",
    1,
    4,
    2
)

# ----------------------------
# APPLY FILTERS
# ----------------------------
filtered = df[
    (df["CreditScore"] >= credit_min) &
    (df["Balance"] >= balance_min) &
    (df["NumOfProducts"] >= products_min)
]

# ----------------------------
# KPI METRICS
# ----------------------------
st.subheader("📊 High-Value Customer Metrics")

col1, col2, col3 = st.columns(3)

total_high_value = len(filtered)

churn_rate = round(filtered["Exited"].mean() * 100, 2) if len(filtered) > 0 else 0

avg_balance = round(filtered["Balance"].mean(), 2) if len(filtered) > 0 else 0

col1.metric("Matching High-Value Customers", total_high_value)
col2.metric("Churn Rate", f"{churn_rate}%")
col3.metric("Average Balance", f"${avg_balance:,.0f}")

st.caption(
    "Key indicators summarizing churn risk among filtered high-value customer segments."
)

st.write("---")

# ----------------------------
# BALANCE VS CREDIT SCORE SCATTER
# ----------------------------
st.subheader("📊 Balance vs Credit Score (Churn Risk Visualization)")

fig = px.scatter(
    filtered,
    x="Balance",
    y="CreditScore",
    color="Exited",
    color_discrete_map={0: "#7dd3fc", 1: "#f472b6"},
    labels={"Exited": "Churn Status"},
    title="High-Value Customers: Balance vs Credit Score"
)

fig.update_layout(title_x=0.25)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "Each point represents a customer. Pink points indicate churned customers. "
    "This visualization helps identify patterns among high-balance customers "
    "who leave the bank."
)

st.write("---")

# ----------------------------
# CHURN DISTRIBUTION FOR HIGH VALUE CUSTOMERS
# ----------------------------
st.subheader("📊 Churn Distribution for High-Value Customers")

churn_dist = filtered["Exited"].value_counts().reset_index()
churn_dist.columns = ["Churn Status", "Customers"]

churn_dist["Churn Status"] = churn_dist["Churn Status"].map({
    0: "Retained",
    1: "Churned"
})

fig2 = px.pie(
    churn_dist,
    names="Churn Status",
    values="Customers",
    hole=0.4,
    color="Churn Status",
    color_discrete_map={"Retained": "#7dd3fc", "Churned": "#f472b6"},
    title="Retention vs Churn Among High-Value Customers"
)

fig2.update_layout(title_x=0.25)

st.plotly_chart(fig2, use_container_width=True)

st.caption(
    "This chart highlights how many high-value customers remain with the bank "
    "versus those who have churned."
)

st.write("---")

# ----------------------------
# KEY INSIGHTS
# ----------------------------
st.markdown("### 📌 Key Insights")

st.info("""
• High-balance customers represent **significant revenue potential**, making their churn particularly costly.

• Customers with **high balances but lower engagement levels** may still leave the bank.

• Monitoring high-value customers using filters helps identify **segments requiring proactive retention strategies**.

• Banks can use such insights to implement **loyalty programs, personalized financial advisory services, and premium support channels**.
""")
