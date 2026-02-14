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

        /* Sidebar title */
        .css-1d391kg p {
            font-size: 20px !important;
        }

        /* Cards */
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
# TOP HEADER
# -------------------------
st.markdown('<div class="top-bar">🏦 Bank Customer Churn Analysis Dashboard</div>', unsafe_allow_html=True)

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Home", "About Dashboard"]
)

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("data/bank.csv")

# -------------------------
# HOME PAGE
# -------------------------
if page == "Home":
    st.subheader("📊 Overview")
    st.write(
        "Welcome to the interactive **Bank Customer Churn Analysis Dashboard**. "
        "Use the filters below to explore churn behavior across demographics, geography, and financial indicators."
    )

    # -------------- FILTER SECTION --------------
    st.markdown("### 🔎 Filters")

    col1, col2, col3 = st.columns(3)

    geography = col1.multiselect(
        "🌍 Select Geography",
        options=df["Geography"].unique(),
        default=df["Geography"].unique()
    )

    gender = col2.multiselect(
        "👤 Select Gender",
        options=df["Gender"].unique(),
        default=df["Gender"].unique()
    )

    age_range = col3.slider(
        "🎯 Age Range",
        min_value=int(df["Age"].min()),
        max_value=int(df["Age"].max()),
        value=(18, 60)
    )

    # Apply filters
    filtered_df = df[
        (df["Geography"].isin(geography)) &
        (df["Gender"].isin(gender)) &
        (df["Age"].between(age_range[0], age_range[1]))
    ]

    # -------------- KPI CARDS --------------
    st.markdown("### 📈 Key Metrics")

    total_customers = len(filtered_df)
    churn_rate = round(filtered_df["Exited"].mean() * 100, 2)
    avg_credit = round(filtered_df["CreditScore"].mean(), 1)
    avg_balance = round(filtered_df["Balance"].mean(), 1)

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown('<div class="metric-card"><div class="metric-title">Total Customers</div>'
                    f'<div class="metric-value">{total_customers}</div></div>', unsafe_allow_html=True)

    with k2:
        st.markdown('<div class="metric-card"><div class="metric-title">Overall Churn Rate</div>'
                    f'<div class="metric-value">{churn_rate}%</div></div>', unsafe_allow_html=True)

    with k3:
        st.markdown('<div class="metric-card"><div class="metric-title">Avg Credit Score</div>'
                    f'<div class="metric-value">{avg_credit}</div></div>', unsafe_allow_html=True)

    with k4:
        st.markdown('<div class="metric-card"><div class="metric-title">Avg Balance</div>'
                    f'<div class="metric-value">${avg_balance}</div></div>', unsafe_allow_html=True)

    st.markdown("---")

    st.success("Use the left sidebar to access detailed churn analysis pages like Geography, Age, Tenure, and High-Value Churn!")

# -------------------------
# ABOUT PAGE
# -------------------------
elif page == "About Dashboard":
    st.header("ℹ️ About This Project")
    st.write("""
        This dashboard provides a full churn analysis for a European bank.  
        It includes segmentation, churn distribution, financial risk, and behavior insights.
        
        Navigate through the detailed pages:
        - **Churn Summary**
        - **Geography-wise Churn**
        - **Age & Tenure Analysis**
        - **High-Value Customer Churn**
        
        All results are dynamic and update with filters.
    """)
