from flask import Blueprint, request, jsonify
from backend.db import get_db_connection

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/api/feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    user_id = data['user_id']
    message = data['message']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO feedback (user_id, message)
        VALUES (%s, %s)
    """, (user_id, message))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})