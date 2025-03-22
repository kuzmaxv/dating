from flask import Blueprint, request, jsonify
from backend.db import get_db_connection
from backend.models.match import Match  # Импортируйте модель Match, если она у вас есть

match_bp = Blueprint('match', __name__)

@match_bp.route('/api/like', methods=['POST'])
def like_profile():
    data = request.json
    from_user_id = data.get('from_user_id')  # ID пользователя, который ставит лайк
    to_user_id = data.get('to_user_id')      # ID пользователя, которому ставят лайк

    if not from_user_id or not to_user_id:
        return jsonify({"error": "Missing user IDs"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Сохраняем лайк в базе данных
        cursor.execute("""
            INSERT INTO reactions (from_user_id, to_user_id, reaction)
            VALUES (%s, %s, 'like')
        """, (from_user_id, to_user_id))
        conn.commit()

        # Проверяем, есть ли взаимный лайк
        cursor.execute("""
            SELECT * FROM reactions
            WHERE from_user_id = %s AND to_user_id = %s AND reaction = 'like'
        """, (to_user_id, from_user_id))
        mutual_like = cursor.fetchone()

        if mutual_like:
            # Если есть взаимный лайк, создаем мэтч
            match = Match(user1_id=from_user_id, user2_id=to_user_id)
            match.save()
            return jsonify({"status": "success", "match": True})

        return jsonify({"status": "success", "match": False})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@match_bp.route('/api/match', methods=['POST'])
def create_match():
    data = request.json
    user1_id = data['user1_id']
    user2_id = data['user2_id']

    match = Match(user1_id=user1_id, user2_id=user2_id)
    match.save()

    return jsonify({"status": "success"})

@match_bp.route('/api/get_matches/<int:user_id>', methods=['GET'])
def get_matches(user_id):
    matches = Match.get_matches_for_user(user_id)
    return jsonify([{"user1_id": m.user1_id, "user2_id": m.user2_id} for m in matches])