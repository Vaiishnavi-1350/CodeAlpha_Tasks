[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://codealpha-ai-credit-scoring-system-2026.streamlit.app/)

# 💳 AI-Based Credit Scoring System using Machine Learning

---

#  Abstract

The AI-Based Credit Scoring System is a Machine Learning-powered financial analytics application developed to predict an individual's creditworthiness using historical financial data. Traditional credit approval systems are often time-consuming and may involve manual analysis, leading to inefficiencies and increased financial risk.

This project automates the credit evaluation process by using Machine Learning algorithms to analyze customer financial behavior such as income, debt, loan amount, payment history, and credit utilization. The system predicts whether a customer is creditworthy or non-creditworthy, helping financial institutions make faster and smarter lending decisions.

The project also includes a professional Streamlit-based web application with login authentication and real-time prediction functionality.

---

# 🎯 Problem Statement

Financial institutions face challenges in accurately assessing customer creditworthiness due to:

* Increasing loan applications
* Manual evaluation processes
* Human errors
* High risk of loan defaults

This project aims to develop an intelligent automated system capable of predicting customer credit risk using Machine Learning techniques.

---

# 🎯 Objectives

* Predict customer creditworthiness using Machine Learning
* Reduce loan default risk
* Automate credit approval analysis
* Improve financial decision-making
* Develop a real-time AI-powered web application
* Provide a scalable and user-friendly financial system

---

# 🧠 Machine Learning Algorithm Used

| Algorithm                | Purpose                |
| ------------------------ | ---------------------- |
| Random Forest Classifier | Credit Risk Prediction |

---

# 🏗️ System Architecture

```text id="nql1lo"
Customer Financial Data
            ↓
     Data Preprocessing
            ↓
    Feature Engineering
            ↓
   Machine Learning Model
            ↓
 Creditworthiness Prediction
            ↓
    Streamlit Web Interface
```

---

#  Project Structure

```bash id="4zw5rr"
credit_scoring_project/
│
├── data/
│   └── credit_data.csv
│
├── models/
│   ├── credit_model.pkl
│   └── scaler.pkl
│
├── screenshots/
│   └── app_ui.png
│
├── app.py
├── main.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Technologies Used

## Programming Language

* Python

## Libraries & Frameworks

* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib
* Matplotlib
* Seaborn

## Development Tools

* VS Code
* GitHub
* Streamlit Cloud

---

#  Dataset Features

| Feature            | Description                  |
| ------------------ | ---------------------------- |
| Income             | Annual customer income       |
| Debt               | Existing debt amount         |
| Payment_History    | Previous repayment history   |
| Credit_Utilization | Credit card usage percentage |
| Age                | Customer age                 |
| Loan_Amount        | Requested loan amount        |

---

#  Key Features

1. AI-Based Credit Risk Prediction
2. Machine Learning Integration
3. Feature Engineering
4. Streamlit Web Application
5. Secure Login Authentication
6. Real-Time Prediction
7. Financial Data Analysis
8. Model Serialization using Joblib
9. User-Friendly Dashboard

---

# Authentication Module

The system includes a secure login page to restrict unauthorized access.

## Default Credentials

```text id="e8z0ro"
Username: admin
Password: admin123
```

---

#  Working Methodology

## Step 1 — Data Collection

Financial customer data is collected and stored in CSV format.

## Step 2 — Data Preprocessing

The dataset is cleaned and transformed for Machine Learning.

## Step 3 — Feature Engineering

Additional features such as Debt-Income Ratio are created.

Example:

```python id="5w97f0"
df["Debt_Income_Ratio"] = df["Debt"] / df["Income"]
```

## Step 4 — Model Training

The Random Forest Classifier is trained using financial data.

## Step 5 — Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

## Step 6 — Model Deployment

The trained model is deployed using Streamlit Cloud.

---

#  Performance Metrics

The project evaluates model performance using:

| Metric    | Purpose                        |
| --------- | ------------------------------ |
| Accuracy  | Overall prediction correctness |
| Precision | Positive prediction quality    |
| Recall    | Detection capability           |
| F1-Score  | Balanced performance           |
| ROC-AUC   | Classification performance     |

---

#  Installation Guide

## 1️⃣ Clone Repository

```bash id="09kpxw"
git clone https://github.com/your-username/credit-scoring-system.git
```

---

## 2️⃣ Install Dependencies

```bash id="jlwm4d"
pip install -r requirements.txt
```

---

## 3️⃣ Train Machine Learning Model

```bash id="n6mjlwm"
python main.py
```

This creates:

* `credit_model.pkl`
* `scaler.pkl`

inside the `models/` folder.

---

## 4️⃣ Run Streamlit Application

```bash id="h0c7y5"
streamlit run app.py
```

---

# 🌐 Deployment

The project is deployed using Streamlit Cloud.

Platform:
https://share.streamlit.io

Deployment Steps:

1. Push project to GitHub
2. Login to Streamlit Cloud
3. Select repository
4. Deploy `app.py`

---

#  Application Screenshots

Add screenshots of:

* Login Page
* Dashboard
* Prediction Results
* Financial Summary


---
## Live Demo

Streamlit App:
https://codealpha-ai-credit-scoring-system-2026.streamlit.app/

## Features
- Credit Risk Prediction
- Random Forest Classifier
- Interactive Dashboard
- Data Visualization
- Secure Login System

---

#  Real-World Applications

* Banking Systems
* Loan Approval Systems
* Financial Analytics Platforms
* Credit Card Approval Systems
* FinTech Applications
* Risk Management Systems

---

# Future Scope

* Integration with real banking datasets
* Deep Learning implementation
* Multi-user authentication
* Database connectivity
* REST API integration
* Explainable AI (XAI)
* Cloud database deployment

---

#  Learning Outcomes

This project helped in understanding:

* Machine Learning Classification
* Financial Data Analysis
* Feature Engineering
* Web Application Development
* Model Deployment
* Authentication Systems
* Cloud Deployment

---

# Author

## Vaishnavi Jadhav

B.Tech CSE (AI & ML)

Areas of Interest:

* Machine Learning
* Artificial Intelligence
* Data Analytics
* Financial AI Solutions

---

# License

This project is licensed under the MIT License.

---

#  Conclusion

The AI-Based Credit Scoring System demonstrates how Machine Learning can be effectively applied in the financial domain to automate and improve credit risk assessment. The project combines AI, financial analytics, and web technologies to build a practical and scalable intelligent financial solution.

---



