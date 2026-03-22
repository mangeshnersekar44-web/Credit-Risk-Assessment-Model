"""
==========================================================
Credit Risk Prediction System
----------------------------------------------------------
Author  : Mangesh Nersekar
Project : Loan Default Prediction using Logistic Regression
Tools   : Python, Pandas, Scikit-Learn, Matplotlib, Seaborn
==========================================================
"""

# ==========================================================
# 1. Import Libraries
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import warnings

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)

warnings.filterwarnings("ignore")


# ==========================================================
# 2. Load Dataset
# ==========================================================

print("Loading dataset...")
df = pd.read_csv("credit_risk_dataset.csv")

print("\nDataset Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Shape:", df.shape)


# ==========================================================
# 3. Data Cleaning
# ==========================================================

df.dropna(inplace=True)
print("\nMissing values after cleaning:")
print(df.isnull().sum())


# ==========================================================
# 4. Encode Categorical Variables
# ==========================================================

df = pd.get_dummies(df, drop_first=True)


# ==========================================================
# 5. Exploratory Data Analysis (EDA)
# ==========================================================

# Target Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='loan_status', data=df)
plt.title("Loan Status Distribution")
plt.show()

# Loan Amount Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['loan_amnt'], kde=True)
plt.title("Loan Amount Distribution")
plt.show()

# Correlation Heatmap
numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(),annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()


# ==========================================================
# 6. Feature & Target Split
# ==========================================================

X = df.drop("loan_status", axis=1)
y = df["loan_status"]


# ==========================================================
# 7. Train-Test Split
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ==========================================================
# 8. Model Training - Logistic Regression
# ==========================================================

model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

print("\nModel training completed.")


# ==========================================================
# 9. Model Evaluation
# ==========================================================

y_pred = model.predict(X_test)

print("\nModel Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC-AUC Score:", roc_auc_score(y_test, model.predict_proba(X_test)[:,1]))

print("\nClassification Report:\n", classification_report(y_test, y_pred))


# Confusion Matrix
plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, y_pred),
            annot=True,
            fmt='d',
            cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


# ROC Curve
fpr, tpr, thresholds = roc_curve(
    y_test, model.predict_proba(X_test)[:,1]
)

plt.figure()
plt.plot(fpr, tpr)
plt.plot([0,1], [0,1], linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()


# ==========================================================
# 10. Risk Segmentation (Business Output)
# ==========================================================

df['default_probability'] = model.predict_proba(X)[:,1]

df['risk_category'] = pd.cut(
    df['default_probability'],
    bins=[0, 0.3, 0.7, 1],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

print("\nRisk Segmentation Preview:")
print(df[['default_probability', 'risk_category']].head())


# ==========================================================
# 11. Feature Importance
# ==========================================================

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
}).sort_values(by="Coefficient", ascending=False)

print("\nTop 10 Important Features:")
print(feature_importance.head(10))

plt.figure(figsize=(10,6))
sns.barplot(
    x="Coefficient",
    y="Feature",
    data=feature_importance.head(10)
)
plt.title("Top 10 Feature Importances")
plt.show()


# ==========================================================
# 12. Save Model & Dataset
# ==========================================================

joblib.dump(model, "credit_risk_model.pkl")
df.to_csv("credit_risk_dataset_with_predictions.csv", index=False)

print("\nModel and dataset saved successfully!")
