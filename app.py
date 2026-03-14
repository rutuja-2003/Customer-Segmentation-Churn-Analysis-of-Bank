import streamlit as st
import pandas as pd

# -------------------------
# PAGE CONFIGURATION
# -------------------------
st.set_page_config(
    page_title="Bank Customer Churn Dashboard",
    layout="wide",
    page_icon="🏦"
)

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("data/bank.csv")

# -------------------------
# PAGE STYLING
# -------------------------
st.markdown("""
<style>

/* Main background */
.main {
    background-color: #0e0e1a;
    color: #ffffff;
}

/* Header bar */
.top-bar {
    background: linear-gradient(90deg, #6c42f5, #a678ff);
    padding: 18px;
    border-radius: 10px;
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 25px;
}

/* KPI Cards */
.metric-card {
    background-color: #1c1c2b;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #3d3d66;
}

.metric-title {
    font-size: 16px;
    color: #c3c3ff;
}

.metric-value {
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown(
    '<div class="top-bar">🏦 Bank Customer Churn Analysis Dashboard</div>',
    unsafe_allow_html=True
)

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------
st.sidebar.title("📌 Dashboard Navigation")

page = st.sidebar.radio(
    "Select Section",
    ["Home", "About Dashboard"]
)

# -------------------------
# HOME PAGE
# -------------------------
if page == "Home":

    st.subheader("📊 Dashboard Overview")

    st.write(
        """
        This interactive dashboard analyzes **bank customer churn patterns** 
        using demographic, geographic, and financial indicators.

        Use the filters below to explore how different customer segments 
        contribute to churn risk.
        """
    )

    # -------------------------
    # FILTERS
    # -------------------------
    st.markdown("### 🔎 Customer Filters")

    col1, col2, col3 = st.columns(3)

    geography = col1.multiselect(
        "🌍 Geography",
        df["Geography"].unique(),
        default=df["Geography"].unique()
    )

    gender = col2.multiselect(
        "👤 Gender",
        df["Gender"].unique(),
        default=df["Gender"].unique()
    )

    age_range = col3.slider(
        "🎯 Age Range",
        min_value=int(df["Age"].min()),
        max_value=int(df["Age"].max()),
        value=(18, 60)
    )

    # Apply Filters
    filtered_df = df[
        (df["Geography"].isin(geography)) &
        (df["Gender"].isin(gender)) &
        (df["Age"].between(age_range[0], age_range[1]))
    ]

    # -------------------------
    # KPI SECTION
    # -------------------------
    st.markdown("### 📈 Key Performance Indicators")

    total_customers = len(filtered_df)
    churn_rate = round(filtered_df["Exited"].mean() * 100, 2)
    avg_credit = round(filtered_df["CreditScore"].mean(), 1)
    avg_balance = round(filtered_df["Balance"].mean(), 2)

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-title">Total Customers</div>
            <div class="metric-value">{total_customers}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k2:
        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-title">Overall Churn Rate</div>
            <div class="metric-value">{churn_rate}%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k3:
        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-title">Average Credit Score</div>
            <div class="metric-value">{avg_credit}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with k4:
        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-title">Average Balance</div>
            <div class="metric-value">${avg_balance}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # -------------------------
    # BUSINESS INSIGHTS
    # -------------------------
    st.markdown("### 📌 Key Insights from Analysis")

    st.info("""
    **Major churn patterns identified from the dataset:**

    • Customers from **Germany show the highest churn rate** compared to France and Spain.  
    • **Customers above 45 years** demonstrate a higher likelihood of leaving the bank.  
    • **Inactive members** represent the most vulnerable segment for churn.  
    • Some **high-balance customers still churn**, indicating possible dissatisfaction despite strong financial value.
    """)

    # -------------------------
    # RECOMMENDATIONS
    # -------------------------
    st.markdown("### 💡 Business Recommendations")

    st.success("""
    Based on the churn analysis, banks can consider the following actions:

    • Develop **loyalty programs for high-balance customers** to reduce attrition.  
    • Improve **customer onboarding for new users** to strengthen early engagement.  
    • Launch **targeted engagement campaigns for inactive customers**.  
    • Introduce **personalized financial services for senior customers**.
    """)

    st.markdown("---")

    st.write(
        "Use the **navigation menu on the left** to explore detailed analysis pages "
        "including churn summary, geographic patterns, age-tenure insights, and high-value customer risk."
    )

# -------------------------
# ABOUT PAGE
# -------------------------
elif page == "About Dashboard":

    st.header("ℹ️ About This Project")

    st.write("""
    This Streamlit dashboard presents a **comprehensive analysis of bank customer churn**.

    The analysis focuses on identifying demographic, financial, and behavioral patterns 
    associated with customer attrition.

    ### Dashboard Modules
    • Churn Summary Overview  
    • Geography-wise Churn Analysis  
    • Age and Tenure Analysis  
    • High-Value Customer Churn Explorer  

    ### Objectives
    The goal of this project is to help financial institutions understand:
    - Which customer segments are most at risk of churn
    - How demographic and financial attributes influence churn
    - What strategies can improve customer retention
    """)

    st.markdown("---")

    st.write(
        "Developed as part of a **Customer Segmentation and Churn Analysis project** "
        "using Python, Streamlit, and data analytics techniques."
    )
