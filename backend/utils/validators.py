import re
from datetime import datetime
from backend.utils.validators import validate_email, validate_phone

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    phone = data.get('phone')

    if email and not validate_email(email):
        return jsonify({"error": "Некорректный email"}), 400

    if phone and not validate_phone(phone):
        return jsonify({"error": "Некорректный номер телефона"}), 400

    # Продолжаем регистрацию
    ...

def validate_email(email):
    """Проверяет корректность email."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Проверяет корректность номера телефона."""
    pattern = r"^\+?[1-9]\d{1,14}$"
    return re.match(pattern, phone) is not None

def validate_age(age):
    """Проверяет, что возраст находится в допустимом диапазоне."""
    return 18 <= age <= 100

def validate_date(date_str, format="%Y-%m-%d"):
    """Проверяет, что строка является корректной датой."""
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False

