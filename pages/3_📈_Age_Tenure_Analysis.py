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
📈 Age & Tenure Churn Analysis
</h1>

<p style="text-align:center; font-size:18px; color:#e0e0ff;">
This section explores how customer age and account tenure influence churn behavior.
Understanding these patterns helps identify vulnerable customer segments.
</p>
""", unsafe_allow_html=True)

st.write("")

# ----------------------------
# AGE VS CHURN
# ----------------------------
st.subheader("📊 Customer Churn by Age")

age_churn = df.groupby("Age")["Exited"].mean().reset_index()
age_churn["Churn %"] = age_churn["Exited"] * 100

fig_age = px.line(
    age_churn,
    x="Age",
    y="Churn %",
    title="Customer Churn Percentage by Age",
    markers=True,
    color_discrete_sequence=["#a78bfa"]
)

fig_age.update_layout(title_x=0.25)

st.plotly_chart(fig_age, use_container_width=True)

st.caption(
    "The chart illustrates how churn probability varies across different age groups. "
    "Older customers often demonstrate higher churn tendencies."
)

st.write("---")

# ----------------------------
# TENURE VS CHURN
# ----------------------------
st.subheader("📊 Customer Churn by Tenure")

tenure_churn = df.groupby("Tenure")["Exited"].mean().reset_index()
tenure_churn["Churn %"] = tenure_churn["Exited"] * 100

fig_tenure = px.line(
    tenure_churn,
    x="Tenure",
    y="Churn %",
    title="Customer Churn Percentage by Account Tenure",
    markers=True,
    color_discrete_sequence=["#f472b6"]
)

fig_tenure.update_layout(title_x=0.25)

st.plotly_chart(fig_tenure, use_container_width=True)

st.caption(
    "This visualization highlights churn trends based on the length of time a customer "
    "has been with the bank. Early-tenure customers often display higher churn risk."
)

st.write("---")

# ----------------------------
# AGE GROUP SEGMENTATION
# ----------------------------
st.subheader("📊 Churn by Age Segment")

df["Age Group"] = pd.cut(
    df["Age"],
    bins=[18, 30, 45, 60, 100],
    labels=["<30", "30–45", "46–60", "60+"]
)

age_group_churn = df.groupby("Age Group")["Exited"].mean().reset_index()
age_group_churn["Churn %"] = age_group_churn["Exited"] * 100

fig_age_group = px.bar(
    age_group_churn,
    x="Age Group",
    y="Churn %",
    color="Age Group",
    color_discrete_sequence=["#7dd3fc", "#a78bfa", "#f472b6", "#fbbf24"],
    title="Customer Churn Rate by Age Segment"
)

fig_age_group.update_layout(title_x=0.25)

st.plotly_chart(fig_age_group, use_container_width=True)

st.caption(
    "Segmenting customers by age group helps identify which demographic segments "
    "contribute most significantly to churn risk."
)

st.write("---")

# ----------------------------
# KEY INSIGHTS
# ----------------------------
st.markdown("### 📌 Key Insights")

st.info("""
• Churn tends to increase gradually as customers grow older.

• Customers aged **45 years and above** demonstrate higher churn risk compared to younger segments.

• **New customers with shorter tenure** show a greater likelihood of leaving the bank.

• These insights highlight the importance of **strong onboarding programs** and **personalized services for senior customers**.
""")
