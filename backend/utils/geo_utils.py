from geopy.distance import geodesic

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