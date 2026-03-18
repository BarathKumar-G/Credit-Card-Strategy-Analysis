# Mitron Bank Credit Card Strategy Analysis

## Overview
This project analyzes customer demographics and transaction data to design data-driven credit card strategies for Mitron Bank. The goal is to identify high-value customer segments and recommend suitable credit card products based on spending behavior.

---

## Objectives
- Understand customer demographics and financial behavior  
- Analyze spending patterns across categories and payment methods  
- Identify high-value and underserved customer segments  
- Recommend targeted credit card products  

---

## Dataset
The dataset follows a **star schema structure**:

### 1. dim_customer (Customer Data)
- customer_id  
- age_group  
- city  
- occupation  
- gender  
- marital_status  
- avg_income  

### 2. fact_sales (Transaction Data)
- customer_id  
- month  
- category  
- payment_type  
- spend  

**Relationship:**  
`dim_customer (1) → fact_sales (many)` via `customer_id`

---
## Tech Stack
- **Python (Pandas, Matplotlib)** – Exploratory Data Analysis (EDA)  
- **Power BI** – Data modeling, analysis, and dashboard creation  
- **Excel** – Data inspection  

---

## Analysis Approach
- Performed initial EDA using Python to understand data structure and distributions  
- Built data model and measures in Power BI  
- Analyzed customer segments using demographics and spending behavior  
- Evaluated income utilisation to estimate credit card usage potential  

---

## Dashboard Features
- KPI overview (Total Spend, Customers, Avg Spend)  
- Customer demographics breakdown  
- Category-wise spending insights  
- Payment method analysis  
- Customer segmentation and income utilisation  
- Credit card recommendations  

---

## Key Insights
- High-income customers show higher spending and strong credit card adoption potential  
- Spending behavior varies across age groups and occupations  
- Distinct customer segments enable targeted product design  

---

## Credit Card Recommendations
- **Premium Card** – High-income, high-spend users  
- **Cashback Card** – Mid-income, frequent spenders  
- **Travel Card** – Travel-focused users  
- **Lifestyle Card** – Young customers with entertainment-driven spending 

---

## 🚀 Outcome
This project demonstrates:
- Understanding of data modeling (star schema)  
- Ability to perform EDA and build dashboards  
- Business-driven analysis and decision-making  

---

---

## 📁 Project Structure
