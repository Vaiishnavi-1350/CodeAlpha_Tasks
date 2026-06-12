import sqlite3
import bcrypt
from utils.logger import logger
def login_user(username,password):

    conn = sqlite3.connect(
        "database/emotions.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT password
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        return bcrypt.checkpw(
            password.encode(),
            user[0]
        )

    return False