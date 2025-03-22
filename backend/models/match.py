from datetime import datetime
from backend.db import get_db_connection

class Match:
    def __init__(self, user1_id, user2_id, matched_at=None):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.matched_at = matched_at or datetime.now()

    def save(self):
        """Сохраняет мэтч в базу данных."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO matches (user1_id, user2_id, matched_at)
            VALUES (%s, %s, %s)
        """, (self.user1_id, self.user2_id, self.matched_at))
        conn.commit()
        conn.close()

    @staticmethod
    def get_matches_for_user(user_id):
        """Возвращает все мэтчи для пользователя."""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT * FROM matches
            WHERE user1_id = %s OR user2_id = %s
        """, (user_id, user_id))
        matches = cursor.fetchall()
        conn.close()
        return [Match(**match) for match in matches]