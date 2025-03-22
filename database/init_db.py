from backend.db import get_db_connection

def add_test_data():
    """Добавляет тестовые данные в базу данных."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Добавление тестовых пользователей
    cursor.execute("""
        INSERT INTO users (user_id, username, first_name)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE username = VALUES(username), first_name = VALUES(first_name)
    """, (123, "test_user", "Test User"))

    # Добавление тестового профиля
    cursor.execute("""
        INSERT INTO profiles (user_id, city, age, gender, height, eye_color, hair_color, bio, interests, hobbies, goals, photo_urls)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        city = VALUES(city), age = VALUES(age), gender = VALUES(gender), height = VALUES(height),
        eye_color = VALUES(eye_color), hair_color = VALUES(hair_color), bio = VALUES(bio),
        interests = VALUES(interests), hobbies = VALUES(hobbies), goals = VALUES(goals), photo_urls = VALUES(photo_urls)
    """, (
        123, "Москва", 25, "male", 180, "голубые", "русые", "Люблю путешествия и спорт.",
        "путешествия, спорт", "фотография, бег", "дружба, отношения", '["photo1.jpg", "photo2.jpg"]'
    ))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    print("Инициализация базы данных...")
    init_db()
    print("База данных успешно инициализирована!")

    print("Добавление тестовых данных...")
    add_test_data()
    print("Тестовые данные успешно добавлены!")