from flask import Blueprint, request, jsonify
from backend.models.profile import Profile

search_bp = Blueprint('search', __name__)

@search_bp.route('/api/search', methods=['POST'])
def search_profiles():
    data = request.json
    city = data.get('city')
    age_min = data.get('age_min', 18)
    age_max = data.get('age_max', 100)
    gender = data.get('gender')
    height_min = data.get('height_min', 150)
    height_max = data.get('height_max', 200)
    eye_color = data.get('eye_color')
    hair_color = data.get('hair_color')
    interests = data.get('interests')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT * FROM profiles
        WHERE city = %s
        AND age BETWEEN %s AND %s
        AND gender = %s
        AND height BETWEEN %s AND %s
        AND eye_color = %s
        AND hair_color = %s
        AND interests LIKE %s
    """
    cursor.execute(query, (city, age_min, age_max, gender, height_min, height_max, eye_color, hair_color, f"%{interests}%"))
    profiles = cursor.fetchall()
    conn.close()

    return jsonify(profiles)