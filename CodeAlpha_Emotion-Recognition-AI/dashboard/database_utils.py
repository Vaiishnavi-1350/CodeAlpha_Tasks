import sqlite3
import pandas as pd

DB = "database/emotions.db"


def save_prediction(
    username,
    emotion,
    confidence
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO emotion_history
        (
            username,
            emotion,
            confidence
        )
        VALUES (?, ?, ?)
        """,
        (
            username,
            emotion,
            confidence
        )
    )

    conn.commit()
    conn.close()


def get_user_history(
    username
):

    conn = sqlite3.connect(DB)

    df = pd.read_sql_query(
        """
        SELECT *
        FROM emotion_history
        WHERE username=?
        ORDER BY timestamp DESC
        """,
        conn,
        params=(username,)
    )

    conn.close()

    return df


def latest_predictions(
    username
):

    conn = sqlite3.connect(DB)

    df = pd.read_sql_query(
        """
        SELECT timestamp,
               confidence
        FROM emotion_history
        WHERE username=?
        ORDER BY timestamp
        """,
        conn,
        params=(username,)
    )

    conn.close()

    return df