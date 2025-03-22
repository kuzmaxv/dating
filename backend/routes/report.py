from flask import Blueprint, request, jsonify
from backend.db import get_db_connection
from backend.models.user import User

report_bp = Blueprint('report', __name__)

@report_bp.route('/api/report', methods=['POST'])
def report_user():
    data = request.json
    reporter_id = data['reporter_id']
    reported_user_id = data['reported_user_id']
    reason = data['reason']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reports (reporter_id, reported_user_id, reason)
        VALUES (%s, %s, %s)
    """, (reporter_id, reported_user_id, reason))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})