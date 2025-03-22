from flask import Blueprint, request, jsonify
from backend.models.profile import Profile

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/api/save_profile', methods=['POST'])
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
    photo_urls = data['photo_urls']

    profile = Profile(
        user_id=user_id,
        city=city,
        age=age,
        gender=gender,
        height=height,
        eye_color=eye_color,
        hair_color=hair_color,
        bio=bio,
        interests=interests,
        hobbies=hobbies,
        goals=goals,
        photo_urls=photo_urls
    )
    profile.save()

    return jsonify({"status": "success"})

@profile_bp.route('/api/get_profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    profile = Profile.get_by_user_id(user_id)
    if profile:
        return jsonify({
            "city": profile.city,
            "age": profile.age,
            "gender": profile.gender,
            "height": profile.height,
            "eye_color": profile.eye_color,
            "hair_color": profile.hair_color,
            "bio": profile.bio,
            "interests": profile.interests,
            "hobbies": profile.hobbies,
            "goals": profile.goals,
            "photo_urls": profile.photo_urls
        })
    return jsonify({"error": "Profile not found"}), 404