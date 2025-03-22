from backend.db import get_db_connection
from backend.utils.analytics_utils import get_user_activity

@profile_bp.route('/api/stats/<int:user_id>', methods=['GET'])
def get_stats(user_id):
    activity = get_user_activity(user_id)
    return jsonify(activity)

def get_user_activity(user_id):
    """Возвращает активность пользователя (лайки, мэтчи и т.д.)."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) as likes_given FROM reactions WHERE from_user_id = %s", (user_id,))
    likes_given = cursor.fetchone()['likes_given']
    cursor.execute("SELECT COUNT(*) as likes_received FROM reactions WHERE to_user_id = %s", (user_id,))
    likes_received = cursor.fetchone()['likes_received']
    cursor.execute("SELECT COUNT(*) as matches FROM matches WHERE user1_id = %s OR user2_id = %s", (user_id, user_id))
    matches = cursor.fetchone()['matches']
    conn.close()
    return {
        "likes_given": likes_given,
        "likes_received": likes_received,
        "matches": matches
    }