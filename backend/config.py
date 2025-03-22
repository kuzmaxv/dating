import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

class Config:
    # Секретный ключ для Flask (для защиты сессий)
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

    # Настройки базы данных
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "yourpassword")
    DB_NAME = os.getenv("DB_NAME", "dating_app")

    # Telegram Bot Token
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "your-telegram-bot-token")

    # Настройки для загрузки файлов
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Настройки для геолокации
    GEOCODING_API_KEY = os.getenv("GEOCODING_API_KEY", "your-geocoding-api-key")

# Экземпляр конфигурации
config = Config()