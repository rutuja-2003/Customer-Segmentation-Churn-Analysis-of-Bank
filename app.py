import streamlit as st
from streamlit_option_menu import option_menu

# ----------- PAGE CONFIG -----------
st.set_page_config(
    page_title="Bank Customer Churn Dashboard",
    layout="wide",
    page_icon="🏦"
)

# ----------- CUSTOM CSS FOR MODERN UI -----------

def load_css():
    st.markdown("""
    <style>

    /* Main background */
    .main {
        background-color: #F7F9FC;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        padding: 20px;
    }

    /* Titles */
    h1, h2, h3 {
        font-family: 'Segoe UI', sans-serif;
        color: #0A3D62;
    }

    /* Cards */
    .metric-card {
        padding: 20px;
        border-radius: 12px;
        background-color: white;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
        text-align: center;
        border-left: 5px solid #1B98F5;
        margin-bottom: 10px;
    }

    /* KPI Value */
    .metric-value {
        font-size: 28px;
        color: #1B98F5;
        font-weight: bold;
    }

    /* KPI Label */
    .metric-label {
        font-size: 16px;
        color: #333;
        margin-top: -5px;
    }

    /* Option menu text */
    .nav-item {
        font-size: 18px !important;
    }

    </style>
    """, unsafe_allow_html=True)

load_css()

# ---------- SIDEBAR NAVIGATION ----------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1048/1048953.png", width=70)
    st.markdown("## **Bank Churn Dashboard**")
    st.markdown("---")

    selected = option_menu(
        menu_title="Navigation",
        options=[
            "🏠 Home",
            "📊 Churn Summary",
            "🗺️ Geography-wise Churn",
            "📈 Age & Tenure Analysis",
            "💎 High-Value Customers"
        ],
        icons=["house", "bar-chart", "map", "graph-up", "gem"],
        menu_icon="grid-3x3-gap-fill",
    )

# ---------- HOME PAGE ----------
if selected == "🏠 Home":
    st.title("🏦 Bank Customer Churn Analysis")
    st.write("A modern & interactive dashboard to explore customer churn patterns.")

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("### ✔️ Explore churn behavior")
        st.markdown("### ✔️ Understand customer segments")
        st.markdown("### ✔️ Improve retention strategy")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2332/2332044.png")

    st.markdown("---")
    st.info("Use the left menu to navigate through dashboard modules.")
