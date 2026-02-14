🏦 Customer Segmentation & Churn Analysis Dashboard (Bank Dataset)

An interactive Streamlit-based analytics dashboard designed to explore customer behavior, segment profiles, and churn patterns for a European bank.
This project showcases business intelligence, customer segmentation, churn prediction insights, and data storytelling — delivered through a dark-mode purple themed UI.

🌟 Key Highlights

🔮 Fully interactive dashboard built with Streamlit

🟣 Dark mode + Purple UI theme

📊 Dynamic KPI tracking

🧩 Multi-level customer segmentation

📉 Churn behavior exploration across age, geography, tenure, and financial metrics

🎯 Designed for business decision-making & revenue risk identification

📁 Project Structure
├── app.py
├── README.md
├── requirements.txt
├── data
│   └── bank.csv
├── pages
│   ├── 1_📊_Churn_Summary.py
│   ├── 2_🗺️_Geography_Wise_Churn.py
│   ├── 3_📈_Age_Tenure_Analysis.py
│   └── 4_💰_High_Value_Churn.py
└── .streamlit
    └── config.toml


🧠 Customer Segmentation Framework

This dashboard uses multi-dimensional segmentation to analyze behaviors, churn risk, and customer value.

1️⃣ Geographic Segmentation

France

Spain

Germany

2️⃣ Age Segmentation

<30

30–45

46–60

60+

3️⃣ Credit Score Bands

Low (300–580)

Medium (581–700)

High (701–850)

4️⃣ Tenure Groups

New Customers (0–3 yrs)

Mid-term (4–7 yrs)

Long-term (8–10 yrs)

5️⃣ Balance Segments

Zero-balance

Low-balance

High-balance

📉 Churn Distribution Analysis

The dashboard provides deep churn insights including:

✔ Overall churn rate
✔ Churn rate by each segment
✔ Segment size contribution to churn
✔ Comparison of churn vs retained profiles
✔ Financial and demographic churn trends

👩‍🧑 Comparative Demographic Analysis
Gender Differences

Male vs Female churn patterns

Gender-based retention risk

Geography × Age Interaction

Young churners in Germany

Older customers in France

Mid-age churn spikes in Spain

Financial Stability vs Churn

Salary × Balance interactions

Low credit score → high churn correlation

💎 High-Value Customer Churn Analysis

This module identifies and analyzes:

High-balance churners

Salary vs balance churn patterns

Revenue-at-risk estimation

Premium customer churn behavior

📌 Key Performance Indicators (KPIs)
KPI	Description
Overall Churn Rate	% of customers who exited
Segment Churn Rate	Churn % for each segment filter
High-Value Churn Ratio	Churn rate specifically for premium customers
Geographic Risk Index	Churn risk level by region
Engagement Drop Indicator	Relationship between inactivity and churn

All KPIs update dynamically based on selected filters.

🚀 Streamlit Web Application Modules

Your app includes four complete interactive BI modules:

📊 1. Overall Churn Summary

Global churn KPIs

Churn vs retained comparative charts

Segment-wise churn highlights

Summary metrics with purple theme

🌍 2. Geography-wise Churn Analysis

Churn distribution by France, Spain, Germany

Regional KPIs

Geo-level drill-downs

Compare churn across countries

👥 3. Age & Tenure Comparison

Age group churn patterns

Tenure-based churn groups

Interaction plots

Retention risk segments

💎 4. High-Value Customer Churn Explorer

Identify high-value churners

Salary × Balance churn scatter

Revenue risk analysis

High-value customer retention insights

🎛 User Features & Capabilities
✔ Segment Filters

geography

age

credit score

tenure

balance

✔ Dynamic KPI Updates

KPIs change instantly based on filters.

✔ Drill-down Visuals

Deep-dive into:

churned customers only

retained customers only

high-value customers

✔ Responsive UI

Works on desktop & mobile

Dark purple theme

🎨 UI / Dark Mode Theme

The app uses a custom purple-dark mode:

• Background: #0C0F1A  
• Primary Purple: #7B2CBF  
• Highlight Purple: #9D4EDD  
• White Accent: #F4F6FF  

🖼 Screenshots 
📊 Dashboard Home
<img width="1919" height="830" alt="image" src="https://github.com/user-attachments/assets/e2d5fdc4-c054-4ed5-979a-5a3365e1285b" />
<img width="1919" height="823" alt="image" src="https://github.com/user-attachments/assets/8fd6fce5-68cc-4fbf-b158-58cddf08654f" />

📊 Churn Summary
<img width="1919" height="824" alt="image" src="https://github.com/user-attachments/assets/00463cd8-c7b5-453f-8d8e-4c852eca6413" />


🌍 Geography View

<img width="1916" height="826" alt="image" src="https://github.com/user-attachments/assets/2d80463c-30a0-454e-9a89-ec46b6f39c8b" />


👥 Age & Tenure Comparison

<img width="1914" height="825" alt="image" src="https://github.com/user-attachments/assets/8c932e5a-df05-4c14-9d79-9fc37f296677" />
<img width="1915" height="825" alt="image" src="https://github.com/user-attachments/assets/9c259d30-67b9-43e8-89a0-041153c6c7e2" />


💎 High-Value Customer Churn Explorer

<img width="1919" height="823" alt="image" src="https://github.com/user-attachments/assets/6171212a-2843-495a-ac4f-1a04cf9c8701" />
![Uploading image.png…]()


🧪 Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Plotly

Streamlit

streamlit-option-menu

▶️ Running the App Locally
pip install -r requirements.txt
streamlit run app.py

🔗 Live App 

👉 [https://your-streamlit-app-url.com](https://customer-segmentation-churn-analysis-of-bank-bncfdp4sbtfboqb5b.streamlit.app/)

🙌 Acknowledgements

This project demonstrates real-world Business Intelligence, segmentation strategy, and churn analytics built with a clean UI and polished dashboard experience.
