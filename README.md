# 🏦 Credit Risk Assessment Model

## 📌 Project Overview
This project performs **end-to-end Credit Risk Analysis and Loan Default Prediction** using **Machine Learning and Power BI**.

The objective is to analyze borrower data, identify risk patterns, and predict the probability of loan default to support better financial decision-making.

---

## 🔗 Project Resources
📂 **GitHub Repository:**  
https://github.com/mangeshnersekar44-web/credit-risk-prediction  

💻 **Python Code:**  
`credit_risk_model.py` / Notebook  

📁 **Dataset:**  
`credit_risk_dataset.csv`  

---

## 🎯 Business Objectives
- Predict loan default probability  
- Identify high-risk borrowers  
- Analyze default trends by loan grade, intent, and income  
- Understand customer risk behavior  
- Support data-driven lending decisions  

---

## 🛠 Tools & Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn (Logistic Regression)  
- MySQL  
- Power BI  
- Streamlit  

---

## 📂 Project Workflow

### 1️⃣ Data Cleaning & Preprocessing
- Handled missing values  
- Removed null records  
- Standardized data types  
- Prepared dataset for modeling  

### 2️⃣ Feature Engineering
- Encoded categorical variables using One-Hot Encoding  
- Created model-ready dataset  
- Generated input features for ML model  

### 3️⃣ Exploratory Data Analysis (EDA)
- Loan Status Distribution (Default vs Non-Default)  
- Loan Amount Distribution  
- Correlation Heatmap  
- Identified key risk-driving factors  

### 4️⃣ Predictive Modeling (Machine Learning)
- Implemented **Logistic Regression Model**  
- Train-Test Split: **80% Training / 20% Testing**  
- Predicted default probability  

---

## 📈 Model Evaluation
The model performance is evaluated using:

- **Accuracy Score:** 78%  
- **ROC-AUC Score:** 0.85  
- **Confusion Matrix**  
- **Classification Report**  

These metrics indicate strong performance in identifying high-risk customers.

---

## 🔮 Risk Segmentation
Customers are classified into:

- 🟢 **Low Risk** (0 – 30%)  
- 🟡 **Medium Risk** (30 – 70%)  
- 🔴 **High Risk** (70%+)  

This helps financial institutions prioritize risk-based decisions.

---

## 🗄️ SQL Analysis
Performed advanced analysis using MySQL:

- Default rate by loan grade  
- Default rate by loan intent  
- Income vs default comparison  
- Credit history risk analysis  
- Created dashboard-ready views  

---

## 📊 Power BI Dashboard
The dashboard includes:

- KPI Cards (Total Customers, Total Defaults, Default Rate)  
- Default Rate by Loan Grade  
- Risk Category Distribution  
- Loan Intent Analysis  
- Age vs Default Trend  
- Home Ownership Analysis  

📸 **Dashboard Preview:**  
![Dashboard](assets/dashboard.png)

---

## 🌐 Streamlit Web App
- Interactive user input system  
- Predict default probability in real-time  
- Displays risk category instantly  

---

## 🚀 How to Run the Project

### Step 1: Clone Repository
```bash
git clone https://github.com/mangeshnersekar44-web/credit-risk-prediction.git
```
###Step 2: Navigate to Project Folder
```bash
cd credit-risk-prediction
```
###Step 3: Install Required Libraries
```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```
###Step 4: Run Python Script
```bash
python credit_risk_model.py
```
▶️ Run Streamlit App
streamlit run app.py
💡 Key Insights

High loan_percent_income → Higher default risk

Lower loan grades (D, E, F, G) → More defaults

High interest rates → Increased risk

Customers with short credit history → Higher defaults

🌐 Connect With Me

👨‍💻 Mangesh Nersekar
Aspiring Data Analyst | Python | Power BI | Machine Learning

🔗 LinkedIn:
https://www.linkedin.com/in/mangesh-nersekar-350750315/

💻 GitHub:
https://github.com/mangeshnersekar44-web
