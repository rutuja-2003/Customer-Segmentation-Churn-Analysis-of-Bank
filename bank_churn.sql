CREATE DATABASE bank;
USE bank;
select * from european_bank;

-- Churn Rate
select
  (SUM(Exited) / COUNT(*)) * 100 AS churn_rate 
FROM european_bank;

-- Churn by Geography
SELECT Geography, COUNT(*) AS total,
       SUM(Exited) AS churned,
       (SUM(Exited)/COUNT(*))*100 AS churn_rate
FROM european_bank
GROUP BY Geography;

-- Churn by Age Group
SELECT 
  CASE 
    WHEN Age < 30 THEN 'Young'
    WHEN Age BETWEEN 30 AND 50 THEN 'Middle-Age'
    ELSE 'Senior'
  END AS age_group,
  COUNT(*) AS total,
  SUM(Exited) AS churned,
  (SUM(Exited)/COUNT(*))*100 AS churn_rate
FROM european_bank
GROUP BY age_group;

-- Churn by Products
SELECT NumOfProducts,
       COUNT(*) AS total,
       SUM(Exited) AS churned
FROM european_bank
GROUP BY NumOfProducts;

-- Credit Score Summary
SELECT 
  MIN(CreditScore) AS min_score,
  MAX(CreditScore) AS max_score,
  AVG(CreditScore) AS avg_score
FROM european_bank;