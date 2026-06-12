import sqlite3
import pandas as pd

DATABASE = "database/emotions.db"


def get_all_predictions():

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        """
        SELECT *
        FROM emotion_history
        """,
        conn
    )

    conn.close()

    return df


def get_analytics():

    df = get_all_predictions()

    if len(df) == 0:

        return {
            "total_predictions": 0,
            "average_confidence": 0
        }

    return {

        "total_predictions":
        len(df),

        "average_confidence":
        round(
            df["confidence"].mean(),
            2
        )
    }