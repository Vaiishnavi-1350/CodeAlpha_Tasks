import streamlit as st
import pandas as pd
import joblib

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Credit Scoring System",
    page_icon="💳",
    layout="wide"
)

# =====================================================
# LOAD MODELS
# =====================================================

model = joblib.load("models/credit_model.pkl")
scaler = joblib.load("models/scaler.pkl")
encoders = joblib.load("models/encoders.pkl")

# =====================================================
# LOGIN CREDENTIALS
# =====================================================

USERNAME = "admin"
PASSWORD = "admin123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #2563eb
    );
}

.main-title{
    text-align:center;
    font-size:55px;
    font-weight:800;
    color:white;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    font-size:20px;
    margin-bottom:30px;
}

.glass-card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    padding:25px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.15);
}

[data-testid="stSidebar"]{
    background:#0f172a;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:15px;
    border:none;
    font-size:18px;
    font-weight:bold;
}

.metric-card{
    background:white;
    padding:15px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOGIN PAGE
# =====================================================

if not st.session_state.logged_in:

    st.markdown("""
    <div class="main-title">
        💳 AI Credit Scoring System
    </div>

    <div class="sub-title">
        Machine Learning Powered Credit Risk Assessment Platform
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1,2,1])

    with c2:

        st.markdown(
            '<div class="glass-card">',
            unsafe_allow_html=True
        )

        st.subheader("🔐 Secure Login")

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("🚀 Login"):

            if username == USERNAME and password == PASSWORD:

                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error("Invalid Credentials")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

# =====================================================
# DASHBOARD
# =====================================================

else:

    st.sidebar.title("💳 Dashboard")
    st.sidebar.success("Admin Logged In")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("""
    <div class="main-title">
        AI Credit Scoring Dashboard
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # =================================================
    # TOP METRICS
    # =================================================

    m1,m2,m3,m4 = st.columns(4)

    m1.metric("Model", "Random Forest")
    m2.metric("Accuracy", "94%+")
    m3.metric("Dataset", "32K+")
    m4.metric("Features", "13")

    st.markdown("---")

    st.subheader("Customer Information")

    col1, col2 = st.columns(2)

    with col1:

        person_age = st.number_input(
            "Age",
            18,
            100,
            30
        )

        person_income = st.number_input(
            "Annual Income",
            1000,
            1000000,
            50000
        )

        person_emp_length = st.number_input(
            "Employment Length",
            0,
            50,
            5
        )

        loan_amnt = st.number_input(
            "Loan Amount",
            500,
            500000,
            10000
        )

        loan_int_rate = st.number_input(
            "Interest Rate",
            1.0,
            40.0,
            10.0
        )

    with col2:

        person_home_ownership = st.selectbox(
            "Home Ownership",
            encoders["person_home_ownership"].classes_
        )

        loan_intent = st.selectbox(
            "Loan Purpose",
            encoders["loan_intent"].classes_
        )

        loan_grade = st.selectbox(
            "Loan Grade",
            encoders["loan_grade"].classes_
        )

        cb_person_default_on_file = st.selectbox(
            "Previous Default",
            encoders["cb_person_default_on_file"].classes_
        )

        cb_person_cred_hist_length = st.number_input(
            "Credit History Length",
            1,
            50,
            5
        )

        loan_percent_income = st.slider(
            "Loan Percent Income",
            0.0,
            1.0,
            0.20
        )

    st.markdown("---")

    if st.button("🔍 Predict Credit Risk"):

        home_encoded = encoders[
            "person_home_ownership"
        ].transform(
            [person_home_ownership]
        )[0]

        intent_encoded = encoders[
            "loan_intent"
        ].transform(
            [loan_intent]
        )[0]

        grade_encoded = encoders[
            "loan_grade"
        ].transform(
            [loan_grade]
        )[0]

        default_encoded = encoders[
            "cb_person_default_on_file"
        ].transform(
            [cb_person_default_on_file]
        )[0]

        loan_income_ratio = (
            loan_amnt /
            (person_income + 1)
        )

        employment_credit_ratio = (
            person_emp_length /
            (cb_person_cred_hist_length + 1)
        )

        input_df = pd.DataFrame({

            "person_age":[person_age],

            "person_income":[person_income],

            "person_home_ownership":[home_encoded],

            "person_emp_length":[person_emp_length],

            "loan_intent":[intent_encoded],

            "loan_grade":[grade_encoded],

            "loan_amnt":[loan_amnt],

            "loan_int_rate":[loan_int_rate],

            "loan_percent_income":[loan_percent_income],

            "cb_person_default_on_file":[default_encoded],

            "cb_person_cred_hist_length":[
                cb_person_cred_hist_length
            ],

            "loan_income_ratio":[
                loan_income_ratio
            ],

            "employment_credit_ratio":[
                employment_credit_ratio
            ]

        })

        scaled_data = scaler.transform(
            input_df
        )

        prediction = model.predict(
            scaled_data
        )[0]

        probability = model.predict_proba(
            scaled_data
        )[0]

        confidence = max(probability) * 100

        st.markdown("---")

        st.subheader("Prediction Result")

        if prediction == 0:

            st.markdown("""
            <div style="
                background:#10b981;
                padding:20px;
                border-radius:15px;
                color:white;
                text-align:center;
                font-size:24px;
                font-weight:bold;">
                ✅ LOW CREDIT RISK
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div style="
                background:#ef4444;
                padding:20px;
                border-radius:15px;
                color:white;
                text-align:center;
                font-size:24px;
                font-weight:bold;">
                ⚠ HIGH CREDIT RISK
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.subheader("Prediction Confidence")

        st.progress(int(confidence))

        st.write(
            f"Confidence Score: {confidence:.2f}%"
        )

        st.subheader("Customer Summary")

        st.dataframe(
            input_df,
            use_container_width=True
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Income",
            f"₹{person_income:,}"
        )

        c2.metric(
            "Loan Amount",
            f"₹{loan_amnt:,}"
        )

        c3.metric(
            "Interest Rate",
            f"{loan_int_rate}%"
        )