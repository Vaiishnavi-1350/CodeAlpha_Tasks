import streamlit as st

from auth.login import login_user
from auth.register import register_user

from dashboard.dashboard import dashboard_page

from dashboard.admin_dashboard import (
    admin_dashboard
)

st.set_page_config(
    page_title="EmotionSense AI",
    page_icon="🎙️",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ----------------------------------
# LOGIN PAGE
# ----------------------------------

if not st.session_state.logged_in:

    tab1, tab2 = st.tabs([
        "Login",
        "Register"
    ])

    with tab1:

        st.title("🎙️ EmotionSense AI")

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if login_user(
                username,
                password
            ):

                st.session_state.logged_in = True

                st.session_state.username = username

                st.rerun()

            else:

                st.error(
                    "Invalid Credentials"
                )

    with tab2:

        st.title("Create Account")

        new_user = st.text_input(
            "New Username"
        )

        new_pass = st.text_input(
            "New Password",
            type="password"
        )

        if st.button("Register"):

            success = register_user(
                new_user,
                new_pass
            )

            if success:

                st.success(
                    "Account Created"
                )

            else:

                st.error(
                    "Username Exists"
                )

else:

    dashboard_page(
        st.session_state.username
    )