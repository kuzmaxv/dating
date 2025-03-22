from geopy.distance import geodesic
from backend.utils.geo_utils import calculate_distance

@search_bp.route('/api/search_nearby', methods=['POST'])
def search_nearby():
    data = request.json
    user_lat = data['latitude']
    user_lon = data['longitude']
    max_distance = data.get('max_distance', 10)  # По умолчанию 10 км

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM profiles")
    profiles = cursor.fetchall()
    conn.close()

    nearby_profiles = []
    for profile in profiles:
        profile_lat, profile_lon = profile['latitude'], profile['longitude']
        distance = calculate_distance(user_lat, user_lon, profile_lat, profile_lon)
        if distance <= max_distance:
            nearby_profiles.append(profile)

    return jsonify(nearby_profiles)

def calculate_distance(lat1, lon1, lat2, lon2):
    """Вычисляет расстояние между двумя точками в километрах."""
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    return geodesic(coords_1, coords_2).km

def get_city_coordinates(city_name):
    """Возвращает координаты города по его названию."""
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="dating_app")
    location = geolocator.geocode(city_name)
    if location:
        return (location.latitude, location.longitude)
    return None