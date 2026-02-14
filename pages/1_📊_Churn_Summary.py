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

kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric(
    label="👥 Total Customers",
    value=f"{total_customers:,}",
)

kpi2.metric(
    label="❌ Customers Churned",
    value=f"{churned:,}",
    delta=f"{churn_rate}% churn rate",
)

kpi3.metric(
    label="✅ Customers Retained",
    value=f"{retained:,}",
)

st.write("---")

# ----------------------------
# CHURN DISTRIBUTION CHART
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
        color_discrete_map={"Retained": "#7dd3fc", "Churned": "#f472b6"},
        title="Churn Distribution",
        hole=0.45,
    )
    fig.update_layout(title_x=0.3)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("""
        ### 📌 Key Insights
        - **Churn Rate:** Customers leaving the bank represent a significant business risk.
        - **Retention:** Majority customers remain loyal, but churn needs deeper analysis.
        - **Action Required:** Investigate high-risk age groups, tenure segments, and geography.
    """)

st.write("---")

# ----------------------------
# NUMERIC SUMMARIES (CLEAN TABLE)
# ----------------------------
summary_df = pd.DataFrame({
    "Metric": ["Total Customers", "Churned", "Retained", "Churn Rate (%)"],
    "Value": [total_customers, churned, retained, churn_rate]
})

st.subheader("📋 Data Summary")
st.dataframe(summary_df, use_container_width=True)
