import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# --------------------------- PAGE CONFIGURATION ---------------------------- #
st.set_page_config(
    page_title="Bank Customer Churn Dashboard",
    layout="wide",
    page_icon="📊",
)

# --------------------------- LOAD DATA ------------------------------------- #
@st.cache_data
def load_data():
    return pd.read_csv("data/bank.csv")

df = load_data()

# --------------------------- CUSTOM CSS (PURPLE THEME + DARK MODE) --------- #
st.markdown("""
    <style>

    /* Main background */
    .stApp {
        background-color: #0d0b1f;
        color: #e1e1ff;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #150f2f;
        border-right: 1px solid #5a4e88;
    }

    /* Sidebar text */
    .css-1d391kg, .css-qbe2hs {
        color: #e1e1ff !important;
    }

    /* Top title */
    h1 {
        color: #c9b6ff !important;
        font-weight: 700;
    }

    /* Subheaders */
    h2, h3 {
        color: #d8c9ff !important;
    }

    /* Cards */
    .metric-card {
        background-color: #1c163d;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #5a4e88;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Option Menu Active Item */
    .nav-link.active {
        background-color: #6a44ff !important;
        color: white !important;
        border-radius: 8px;
    }

    /* Option Menu */
    .nav-link:hover {
        background-color: #5333cc !important;
        color: #fff !important;
        border-radius: 8px;
    }

    </style>
""", unsafe_allow_html=True)

# --------------------------- SIDEBAR MENU ---------------------------------- #
with st.sidebar:
    selected = option_menu(
        menu_title="🏦 Bank Churn Dashboard",
        options=["Home", "Filters"],
        icons=["house", "filter"],
        default_index=0,
        styles={
            "nav-link": {"font-size": "15px", "color": "#e1e1ff"},
            "icon": {"color": "#c9b6ff"},
        }
    )

# --------------------------- HOME PAGE ------------------------------------- #
if selected == "Home":
    st.title("📊 Customer Churn Dashboard")
    st.write("Explore customer churn insights with a clean, dark purple theme.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Customers", f"{len(df):,}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        churn_rate = df["Exited"].mean() * 100
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Overall Churn Rate", f"{churn_rate:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        active = len(df[df["Exited"] == 0])
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Active Customers", f"{active:,}")
        st.markdown('</div>', unsafe_allow_html=True)

# --------------------------- FILTERS PAGE ---------------------------------- #
if selected == "Filters":
    st.title("🔍 Apply Filters")

    col1, col2, col3 = st.columns(3)

    with col1:
        geo = st.multiselect("🌍 Geography", df["Geography"].unique())

    with col2:
        gender = st.multiselect("🧑 Gender", df["Gender"].unique())

    with col3:
        tenure = st.slider("📆 Tenure", 0, 10, (0, 10))

    filtered_df = df.copy()

    if geo:
        filtered_df = filtered_df[filtered_df["Geography"].isin(geo)]
    if gender:
        filtered_df = filtered_df[filtered_df["Gender"].isin(gender)]

    filtered_df = filtered_df[
        (filtered_df["Tenure"] >= tenure[0]) &
        (filtered_df["Tenure"] <= tenure[1])
    ]

    st.write("### Filtered Dataset", filtered_df)
