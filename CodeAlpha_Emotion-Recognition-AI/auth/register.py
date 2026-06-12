import sqlite3
import bcrypt
from utils.logger import logger
def register_user(username,password):

    conn = sqlite3.connect("database/emotions.db")

    cursor = conn.cursor()

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:

        cursor.execute(
            """
            INSERT INTO users(username,password)
            VALUES(?,?)
            """,
            (
                username,
                hashed
            )
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()