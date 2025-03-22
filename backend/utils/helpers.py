import json
from datetime import datetime
from backend.models.user import User
from backend.models.profile import Profile
from backend.models.match import Match
from backend.utils.helpers import json_dumps, format_user_profile

@profile_bp.route('/api/get_profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    profile = Profile.get_by_user_id(user_id)
    if profile:
        formatted_profile = format_user_profile(profile)
        return json_dumps(formatted_profile)  # Сериализация в JSON
    return jsonify({"error": "Профиль не найден"}), 404


def serialize_datetime(obj):
    """Преобразует объект datetime в строку."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def json_dumps(data):
    """Сериализует данные в JSON с поддержкой datetime."""
    return json.dumps(data, default=serialize_datetime)

def calculate_age(birthdate):
    """Вычисляет возраст по дате рождения."""
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def generate_random_string(length=8):
    """Генерирует случайную строку заданной длины."""
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def format_user_profile(profile):
    """Форматирует профиль пользователя для отображения."""
    return {
        "name": profile.first_name,
        "age": profile.age,
        "city": profile.city,
        "bio": profile.bio,
        "interests": profile.interests,
        "photo_urls": profile.photo_urls
    }