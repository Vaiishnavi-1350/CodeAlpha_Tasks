import pandas as pd
import joblib
import os

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)

# =====================================================
# CREATE FOLDERS
# =====================================================

os.makedirs("models", exist_ok=True)
os.makedirs("graphs", exist_ok=True)

print("=" * 60)
print("AI CREDIT SCORING SYSTEM")
print("=" * 60)

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("data/credit_data.csv")

print("\nDataset Loaded Successfully")
print("Dataset Shape:", df.shape)

# =====================================================
# MISSING VALUES
# =====================================================

print("\nMissing Values:")
print(df.isnull().sum())

df["person_emp_length"] = df["person_emp_length"].fillna(
    df["person_emp_length"].median()
)

df["loan_int_rate"] = df["loan_int_rate"].fillna(
    df["loan_int_rate"].median()
)

# =====================================================
# FEATURE ENGINEERING
# =====================================================

print("\nPerforming Feature Engineering...")

df["loan_income_ratio"] = (
    df["loan_amnt"] /
    (df["person_income"] + 1)
)

df["employment_credit_ratio"] = (
    df["person_emp_length"] /
    (df["cb_person_cred_hist_length"] + 1)
)

print("Feature Engineering Completed")

# =====================================================
# GRAPHS - BEFORE ENCODING
# =====================================================

# Loan Status Distribution
plt.figure(figsize=(6,4))
sns.countplot(x="loan_status", data=df)
plt.title("Loan Status Distribution")
plt.savefig("graphs/loan_status_distribution.png")
plt.close()

# Income Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["person_income"], bins=30, kde=True)
plt.title("Income Distribution")
plt.savefig("graphs/income_distribution.png")
plt.close()

# Loan Amount Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["loan_amnt"], bins=30, kde=True)
plt.title("Loan Amount Distribution")
plt.savefig("graphs/loan_amount_distribution.png")
plt.close()

# =====================================================
# LABEL ENCODING
# =====================================================

encoders = {}

categorical_cols = [
    "person_home_ownership",
    "loan_intent",
    "loan_grade",
    "cb_person_default_on_file"
]

for col in categorical_cols:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(df[col])

    encoders[col] = encoder

# =====================================================
# CORRELATION HEATMAP
# =====================================================

plt.figure(figsize=(12,8))

sns.heatmap(
    df.corr(),
    annot=False,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig(
    "graphs/correlation_heatmap.png"
)

plt.close()

# =====================================================
# FEATURES & TARGET
# =====================================================

X = df.drop("loan_status", axis=1)

y = df["loan_status"]

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =====================================================
# SCALING
# =====================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

# =====================================================
# TRAIN MODEL
# =====================================================

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42
)

model.fit(
    X_train_scaled,
    y_train
)

# =====================================================
# PREDICTIONS
# =====================================================

y_pred = model.predict(
    X_test_scaled
)

y_prob = model.predict_proba(
    X_test_scaled
)[:,1]

# =====================================================
# EVALUATION
# =====================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

roc_auc = roc_auc_score(
    y_test,
    y_prob
)

print("\nModel Accuracy:")
print(round(accuracy,4))

print("\nROC-AUC Score:")
print(round(roc_auc,4))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred
    )
)

# =====================================================
# CONFUSION MATRIX
# =====================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d"
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig(
    "graphs/confusion_matrix.png"
)

plt.close()

# =====================================================
# ROC CURVE
# =====================================================

fpr, tpr, _ = roc_curve(
    y_test,
    y_prob
)

plt.figure(figsize=(7,5))

plt.plot(
    fpr,
    tpr,
    label=f"AUC = {roc_auc:.3f}"
)

plt.plot(
    [0,1],
    [0,1],
    linestyle="--"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.legend()

plt.savefig(
    "graphs/roc_curve.png"
)

plt.close()

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

importance_df = pd.DataFrame({

    "Feature": X.columns,

    "Importance":
    model.feature_importances_

})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Features:")
print(
    importance_df.head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x="Importance",
    y="Feature",
    data=importance_df.head(10)
)

plt.title("Top 10 Feature Importance")

plt.savefig(
    "graphs/feature_importance.png"
)

plt.close()

# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(
    model,
    "models/credit_model.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

joblib.dump(
    encoders,
    "models/encoders.pkl"
)

print("\nModel Saved Successfully!")

# =====================================================
# TRAINING REPORT
# =====================================================

with open(
    "training_report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "AI CREDIT SCORING SYSTEM REPORT\n"
    )

    report.write(
        "=" * 60 + "\n\n"
    )

    report.write(
        f"Dataset Shape: {df.shape}\n\n"
    )

    report.write(
        f"Accuracy: {accuracy:.4f}\n"
    )

    report.write(
        f"ROC-AUC: {roc_auc:.4f}\n\n"
    )

    report.write(
        classification_report(
            y_test,
            y_pred
        )
    )

print("\nTraining Report Generated!")

print("\nPROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)