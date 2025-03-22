from flask import Flask, request, jsonify
import mysql.connector
import json
from backend.models.user import User
from backend.models.profile import Profile
from backend.models.match import Match
from backend.routes.auth import auth_bp
from backend.routes.profile import profile_bp
from backend.routes.search import search_bp
from backend.routes.match import match_bp
from backend.routes.report import report_bp
from backend.routes.block import block_bp
from backend.routes.admin import admin_bp
from backend.routes.feedback import feedback_bp

app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(search_bp)
app.register_blueprint(match_bp)
app.register_blueprint(report_bp)
app.register_blueprint(block_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(feedback_bp)

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ваш_пароль",
        database="dating_app"
    )

@app.route('/api/save_profile', methods=['POST'])
def save_profile():
    data = request.json
    user_id = data['user_id']
    city = data['city']
    age = data['age']
    gender = data['gender']
    height = data['height']
    eye_color = data['eye_color']
    hair_color = data['hair_color']
    bio = data['bio']
    interests = data['interests']
    hobbies = data['hobbies']
    goals = data['goals']
    photo_urls = json.dumps(data['photo_urls'])

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO profiles (user_id, city, age, gender, height, eye_color, hair_color, bio, interests, hobbies, goals, photo_urls)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (user_id, city, age, gender, height, eye_color, hair_color, bio, interests, hobbies, goals, photo_urls))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)