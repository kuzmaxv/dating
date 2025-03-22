from flask import Blueprint, request, jsonify
from backend.db import get_db_connection
from backend.models.user import User

block_bp = Blueprint('block', __name__)

@block_bp.route('/api/block', methods=['POST'])
def block_user():
    data = request.json
    blocker_id = data['blocker_id']
    blocked_user_id = data['blocked_user_id']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO blocks (blocker_id, blocked_user_id)
        VALUES (%s, %s)
    """, (blocker_id, blocked_user_id))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})