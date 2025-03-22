from datetime import datetime
from backend.db import get_db_connection

class Profile:
    def __init__(self, user_id, city, age, gender, height, eye_color, hair_color, bio, interests, hobbies, goals, photo_urls, created_at=None):
        self.user_id = user_id
        self.city = city
        self.age = age
        self.gender = gender
        self.height = height
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.bio = bio
        self.interests = interests
        self.hobbies = hobbies
        self.goals = goals
        self.photo_urls = photo_urls
        self.created_at = created_at or datetime.now()

    def save(self):
        """Сохраняет профиль в базу данных."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO profiles (user_id, city, age, gender, height, eye_color, hair_color, bio, interests, hobbies, goals, photo_urls, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            city = %s, age = %s, gender = %s, height = %s, eye_color = %s, hair_color = %s, bio = %s, interests = %s, hobbies = %s, goals = %s, photo_urls = %s
        """, (
            self.user_id, self.city, self.age, self.gender, self.height, self.eye_color, self.hair_color, self.bio, self.interests, self.hobbies, self.goals, self.photo_urls, self.created_at,
            self.city, self.age, self.gender, self.height, self.eye_color, self.hair_color, self.bio, self.interests, self.hobbies, self.goals, self.photo_urls
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_user_id(user_id):
        """Возвращает профиль по ID пользователя."""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM profiles WHERE user_id = %s", (user_id,))
        profile_data = cursor.fetchone()
        conn.close()
        if profile_data:
            return Profile(**profile_data)
        return None