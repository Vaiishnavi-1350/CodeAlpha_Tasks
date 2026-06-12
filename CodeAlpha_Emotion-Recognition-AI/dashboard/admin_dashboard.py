import streamlit as st
import sqlite3
import pandas as pd

from reports.excel_report import (
    generate_excel_report
)

DB = "database/emotions.db"


def admin_dashboard():

    st.title(
        "Admin Analytics"
    )

    conn = sqlite3.connect(DB)

    history = pd.read_sql_query(
        """
        SELECT *
        FROM emotion_history
        """,
        conn
    )

    users = pd.read_sql_query(
        """
        SELECT *
        FROM users
        """,
        conn
    )

    conn.close()

    # ------------------
    # KPIs
    # ------------------

    total_users = len(users)

    total_predictions = len(
        history
    )

    avg_confidence = 0

    if total_predictions > 0:

        avg_confidence = round(
            history[
                "confidence"
            ].mean(),
            2
        )

    col1,col2,col3 = st.columns(3)

    col1.metric(
        "Users",
        total_users
    )

    col2.metric(
        "Predictions",
        total_predictions
    )

    col3.metric(
        "Avg Confidence",
        avg_confidence
    )

    st.divider()

    # ------------------
    # Users
    # ------------------

    st.subheader(
        "Registered Users"
    )

    st.dataframe(users)

    # ------------------
    # Predictions
    # ------------------

    st.subheader(
        "Emotion History"
    )

    st.dataframe(history)

    # ------------------
    # Export
    # ------------------

    if st.button(
        "Generate Excel Report"
    ):

        file_path = (
            generate_excel_report(
                history
            )
        )

        with open(
            file_path,
            "rb"
        ) as f:

            st.download_button(
                label=
                "Download Report",
                data=f,
                file_name=
                file_path
            )