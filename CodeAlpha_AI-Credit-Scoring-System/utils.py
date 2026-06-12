import pandas as pd

# ==========================
# Feature Engineering
# ==========================

def calculate_debt_income_ratio(debt, income):

    if income == 0:
        return 0

    return debt / income


# ==========================
# Convert Payment History
# ==========================

def encode_payment_history(history):

    if history == "Good":
        return 1
    else:
        return 0


# ==========================
# Create Input DataFrame
# ==========================

def create_input_dataframe(
    income,
    debt,
    payment_history,
    credit_utilization,
    age,
    loan_amount
):

    debt_income_ratio = calculate_debt_income_ratio(
        debt,
        income
    )

    payment_value = encode_payment_history(
        payment_history
    )

    input_df = pd.DataFrame({
        'Income': [income],
        'Debt': [debt],
        'Payment_History': [payment_value],
        'Credit_Utilization': [credit_utilization],
        'Age': [age],
        'Loan_Amount': [loan_amount],
        'Debt_Income_Ratio': [debt_income_ratio]
    })

    return input_df