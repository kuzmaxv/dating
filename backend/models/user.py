from datetime import datetime
from backend.db import get_db_connection

class User:
    def __init__(self, user_id, username, first_name, registered_at=None):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.registered_at = registered_at or datetime.now()

    def save(self):
        """Сохраняет пользователя в базу данных."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (user_id, username, first_name, registered_at)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE username = %s, first_name = %s
        """, (self.user_id, self.username, self.first_name, self.registered_at, self.username, self.first_name))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(user_id):
        """Возвращает пользователя по ID."""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        user_data = cursor.fetchone()
        conn.close()
        if user_data:
            return User(**user_data)
        return None