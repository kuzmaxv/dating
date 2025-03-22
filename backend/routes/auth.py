from flask import Blueprint, request, jsonify
from backend.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/telegram_auth', methods=['POST'])
def telegram_auth():
    data = request.json
    user_id = data['id']
    username = data.get('username', '')
    first_name = data.get('first_name', '')

    user = User(user_id=user_id, username=username, first_name=first_name)
    user.save()

    return jsonify({"status": "success", "user_id": user_id})