import requests
from backend.utils.notification_utils import notify_match

@match_bp.route('/api/match', methods=['POST'])
def create_match():
    data = request.json
    user1_id = data['user1_id']
    user2_id = data['user2_id']

    # Сохраняем мэтч в базу данных
    match = Match(user1_id=user1_id, user2_id=user2_id)
    match.save()

    # Уведомляем пользователей
    bot_token = "YOUR_BOT_TOKEN"
    notify_match(user1_id, user2_id, bot_token)

    return jsonify({"status": "success"})

def send_telegram_message(chat_id, text, bot_token):
    """Отправляет сообщение в Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    return response.status_code == 200

def notify_match(user1_id, user2_id, bot_token):
    """Уведомляет пользователей о мэтче."""
    message = "У вас новый мэтч! Напишите своему новому знакомому."
    send_telegram_message(user1_id, message, bot_token)
    send_telegram_message(user2_id, message, bot_token)