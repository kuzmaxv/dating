from flask import Blueprint, request, jsonify
from backend.models.match import Match

match_bp = Blueprint('match', __name__)

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