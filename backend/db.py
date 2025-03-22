from backend.models.user import User
from backend.models.profile import Profile
from backend.models.match import Match
import mysql.connector
from backend.config import config

def get_db_connection():
    """Возвращает соединение с базой данных."""
    return mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )

def init_db():
    """Инициализирует базу данных (создает таблицы, если их нет)."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Создание таблиц
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id BIGINT UNIQUE,
            username VARCHAR(255),
            first_name VARCHAR(255),
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profiles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id BIGINT,
            city VARCHAR(255),
            age INT,
            gender ENUM('male', 'female', 'other'),
            height INT,
            eye_color VARCHAR(50),
            hair_color VARCHAR(50),
            bio TEXT,
            interests TEXT,
            hobbies TEXT,
            goals TEXT,
            photo_urls JSON,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            from_user_id BIGINT,
            to_user_id BIGINT,
            reaction ENUM('like', 'dislike'),
            reacted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (from_user_id) REFERENCES users(user_id),
            FOREIGN KEY (to_user_id) REFERENCES users(user_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user1_id BIGINT,
            user2_id BIGINT,
            matched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user1_id) REFERENCES users(user_id),
            FOREIGN KEY (user2_id) REFERENCES users(user_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INT AUTO_INCREMENT PRIMARY KEY,
            reporter_id BIGINT,
            reported_user_id BIGINT,
            reason TEXT,
            reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (reporter_id) REFERENCES users(user_id),
            FOREIGN KEY (reported_user_id) REFERENCES users(user_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS blocks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            blocker_id BIGINT,
            blocked_user_id BIGINT,
            blocked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (blocker_id) REFERENCES users(user_id),
            FOREIGN KEY (blocked_user_id) REFERENCES users(user_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id BIGINT,
            message TEXT,
            sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()