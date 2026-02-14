🏦 Bank Customer Segmentation & Churn Analysis – Streamlit Web Application

An interactive Streamlit analytics application built to explore customer churn patterns, identify high-risk customer segments, and help financial institutions improve retention strategies.

This project delivers dynamic dashboards, drill-down analysis, and segment-wise churn exploration, meeting the typical workflow of a BI Analyst / Data Analyst in the banking domain.

🔍 1. Project Overview

Customer churn is one of the biggest concerns for banks. Losing high-value customers impacts:

Profitability

Long-term customer lifetime value

Cross-selling opportunities

This project uses real banking data to analyze why customers leave and provides actionable churn insights using a Streamlit web application.

The dashboards allow users to:

Monitor churn

Compare churn across age, tenure, geography

Filter and examine high-value customers

Analyze customer behavior dynamically

🎯 2. Business Problem

Banks struggle to identify:

Which customers are at the highest risk of churn?

How churn varies across age groups, tenure, and geography?

What defines a high-value customer, and why are they leaving?

Which segments require urgent retention efforts?

This project solves these questions through a visual and interactive analytics tool.

🧠 3. Project Objectives

✔ Build an interactive customer churn analytics dashboard
✔ Provide segment filters for deep-dive exploration
✔ Deliver dynamic KPIs updating with filters
✔ Compare churn across demographics and geographies
✔ Identify high-value customers and analyze their churn patterns
✔ Enable drill-down visualizations for business decisions

🖥️ 4. Application Features
### 📊 A. Overall Churn Summary

Total customers

Churned vs Active customers

Automated churn rate calculation

Churn distribution chart

🗺️ B. Geography-wise Churn Analysis

Churn percentage by country

Interactive geographic bar charts

📈 C. Age & Tenure Comparative Analysis

Age vs Churn % line visualization

Tenure vs Churn % trendline

Identifies high-risk age ranges

💰 D. High-Value Customer Churn Explorer

Dynamic filters for:

Minimum Credit Score

Minimum Account Balance

Number of Products Owned

Includes:

High-value churn rate KPI

Scatter plot: Balance vs Credit Score vs Churn

Drill-down customer segmentation

🎛️ E. User Capabilities

✔ Segment filters
✔ Dynamic KPI updates
✔ Interactive charts
✔ Drill-down segmentation views
✔ Clean and simple navigation

🏗️ 5. Application Architecture
                       ┌──────────────┐
                       │   Dataset     │
                       │  bank.csv     │
                       └──────┬───────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  Data Processing │
                    └──────────────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │    Streamlit Web Application   │
              └────────────────────────────────┘
                 │         │          │
                 ▼         ▼          ▼
        Overall Churn   Geo-Churn   High-Value
          Summary        Analysis      Explorer

🧰 6. Tech Stack
Component	Technology
Dashboard Framework	Streamlit
Data Manipulation	Pandas, NumPy
Visualizations	Altair, Matplotlib
ML-ready Structure	Scikit-Learn
Deployment	Streamlit Cloud

📁 7. Folder Structure
customer-churn-app/
│── app.py
│── pages/
│     ├── 1_📊_Churn_Summary.py
│     ├── 2_🗺️_Geography_Wise_Churn.py
│     ├── 3_📈_Age_Tenure_Analysis.py
│     ├── 4_💰_High_Value_Churn.py
│── data/
│     └── bank.csv
│── requirements.txt
│── README.md

🔧 8. Installation & Setup
Step 1: Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Run the Streamlit application
streamlit run app.py

📈 9. Screenshots

(You can add images later)

Dashboard Home

Geography-wise Churn

High-Value Customer Explorer

📊 10. Key Insights from the Data

✔ Customers aged 45–60 show significantly higher churn
✔ Low-tenure customers show a sudden churn spike
✔ Germany exhibits the highest churn rate
✔ Customers with:

High balance

High credit score

Multiple products

still churn — indicating dissatisfaction despite financial value.

✔ High-value churn analysis shows product ownership influences churn more than balance.

🚀 11. Future Enhancements

🔹 Add machine learning models (Logistic Regression, Random Forest, XGBoost)
🔹 Predict churn likelihood for each customer
🔹 Build LTV (Lifetime Value) estimation
🔹 Add Power BI style theme
🔹 Include cohort retention analysis
🔹 Add customer segmentation using K-Means

👩‍💻 12. Author

Rutuja Kamble
📍 Mumbai, India
💼 Aspiring BI Analyst | Data Analyst
💡 Passionate about analytics, dashboards & business intelligence
