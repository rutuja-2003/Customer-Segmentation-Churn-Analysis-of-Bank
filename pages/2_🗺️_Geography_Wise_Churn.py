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
🗺️ Geography-wise Customer Churn Analysis
</h1>

<p style="text-align:center; font-size:18px; color:#e0e0ff;">
This section analyzes how customer churn varies across different geographic regions.
Understanding regional churn patterns helps banks identify areas requiring targeted retention strategies.
</p>
""", unsafe_allow_html=True)

st.write("")

# ----------------------------
# GEOGRAPHY KPI METRICS
# ----------------------------
geo_summary = df.groupby("Geography")["Exited"].mean().reset_index()
geo_summary["Churn %"] = (geo_summary["Exited"] * 100).round(2)

col1, col2, col3 = st.columns(3)

france_rate = geo_summary[geo_summary["Geography"] == "France"]["Churn %"].values[0]
germany_rate = geo_summary[geo_summary["Geography"] == "Germany"]["Churn %"].values[0]
spain_rate = geo_summary[geo_summary["Geography"] == "Spain"]["Churn %"].values[0]

col1.metric("🇫🇷 France Churn Rate", f"{france_rate}%")
col2.metric("🇩🇪 Germany Churn Rate", f"{germany_rate}%")
col3.metric("🇪🇸 Spain Churn Rate", f"{spain_rate}%")

st.caption("Key churn percentages across the bank’s primary geographic markets.")

st.write("---")

# ----------------------------
# CHURN RATE BY GEOGRAPHY
# ----------------------------
st.subheader("📊 Churn Rate by Geography")

fig = px.bar(
    geo_summary,
    x="Geography",
    y="Churn %",
    color="Geography",
    color_discrete_sequence=["#7dd3fc", "#a78bfa", "#f472b6"],
    title="Customer Churn Percentage Across Geographic Regions"
)

fig.update_layout(title_x=0.25)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "This chart compares churn rates across the three primary geographic markets. "
    "Regions with higher churn rates may indicate lower customer satisfaction "
    "or stronger competition from other banks."
)

st.write("---")

# ----------------------------
# CUSTOMER DISTRIBUTION BY REGION
# ----------------------------
st.subheader("📊 Customer Distribution by Geography")

geo_counts = df["Geography"].value_counts().reset_index()
geo_counts.columns = ["Geography", "Customers"]

fig2 = px.pie(
    geo_counts,
    names="Geography",
    values="Customers",
    color="Geography",
    color_discrete_sequence=["#7dd3fc", "#a78bfa", "#f472b6"],
    hole=0.4,
    title="Customer Base Distribution Across Regions"
)

fig2.update_layout(title_x=0.25)

st.plotly_chart(fig2, use_container_width=True)

st.caption(
    "This visualization shows how the bank’s customer base is distributed across "
    "different regions. Regions with larger customer bases contribute more "
    "significantly to overall churn risk."
)

st.write("---")

# ----------------------------
# KEY INSIGHTS
# ----------------------------
st.markdown("### 📌 Key Regional Insights")

st.info("""
• **Germany shows the highest churn risk**, indicating potential customer dissatisfaction or strong market competition.

• **France has the largest customer base**, making retention efforts in this region especially important.

• **Spain demonstrates moderate churn levels**, suggesting relatively stable customer relationships.

• Geographic insights help banks develop **region-specific retention strategies** and improve customer satisfaction.
""")
