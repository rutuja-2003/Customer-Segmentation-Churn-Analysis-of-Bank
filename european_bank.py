# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

import streamlit as st
import pandas as pd

# File Upload
uploaded_file = st.file_uploader("Upload the Bank Dataset (CSV file)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Dataset:")
    st.dataframe(df)
else:
    st.warning("Please upload a CSV file to continue.")

df.head()

"""Basic Info & Check Null Values"""

df.info()
df.isnull().sum()
df.describe()

# remove duplicates
df.drop_duplicates(inplace=True)

"""EDA – Univariate Analysis"""

# Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], kde=True)
plt.title("Age Distribution")
plt.show()

# Credit Score Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['CreditScore'], kde=True)
plt.title("Credit Score Distribution")
plt.show()

# Balance Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Balance'], kde=True)
plt.title("Balance Distribution")
plt.show()

"""Bivariate EDA"""

# Churn count
sns.countplot(data=df, x='Exited')
plt.title("Churn vs Non-Churn")
plt.show()

# Age vs Churn
plt.figure(figsize=(7,5))
sns.boxplot(data=df, x='Exited', y='Age')
plt.title("Age vs Churn")
plt.show()

# Credit Score vs Churn
plt.figure(figsize=(7,5))
sns.boxplot(data=df, x='Exited', y='CreditScore')
plt.title("Credit Score vs Churn")
plt.show()

# Select numeric columns only
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Correlation Heatmap
plt.figure(figsize=(12,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Numeric Features Only)")
plt.show()

"""Feature Engineering"""

# Age Groups
df['Age_Group'] = pd.cut(df['Age'],
                         bins=[0, 30, 50, 100],
                         labels=['Young', 'Middle-Aged', 'Senior'])

# Credit Score Band
df['CreditScore_Band'] = pd.cut(df['CreditScore'],
                                bins=[300, 580, 670, 740, 850],
                                labels=['Poor', 'Fair', 'Good', 'Excellent'])

#Customer Segment (Example Logic)
df['Customer_Segment'] = np.where(df['Balance'] > 100000, 'High Value',
                           np.where(df['Balance'] > 50000, 'Mid Value', 'Low Value'))

df.head()

#Encode Categorical Variables
df_encoded = pd.get_dummies(df, drop_first=True)
df_encoded.head()

# Split Data (X, y)
X = df_encoded.drop('Exited', axis=1)
y = df_encoded['Exited']

#Train–Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Logistic Regression Model
log_model = LogisticRegression(max_iter=500)
log_model.fit(X_train, y_train)

y_pred_log = log_model.predict(X_test)

print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred_log))
print(classification_report(y_test, y_pred_log))

# Random Forest Classifier
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)

#Evaluation
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

#ROC-AUC Curve
y_probs = rf.predict_proba(X_test)[:,1]
fpr, tpr, thresh = roc_curve(y_test, y_probs)

plt.figure(figsize=(6,5))
plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve (Random Forest)")
plt.show()

roc_auc_score(y_test, y_probs)

#Feature Importance (Random Forest)
importances = pd.Series(rf.feature_importances_, index=X.columns)
importances.nlargest(15).plot(kind='barh', figsize=(8,6))
plt.title("Top 15 Feature Importances")
plt.show()

#Export Cleaned Dataset
df.to_csv("cleaned_bank_churn.csv", index=False)
files.download("cleaned_bank_churn.csv")
