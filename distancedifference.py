
import math

def haversine(lat1, lon1, lat2, lon2):

    """

    Calculate the great-circle distance between two points 

    on the Earth specified by their latitude and longitude using the Haversine formula.

    Returns distance in miles.

    """

    # Earth radius in miles

    R = 3958.8

    

    # Convert degrees to radians

    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)

    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)

    

    # Differences

    dlat = lat2_rad - lat1_rad

    dlon = lon2_rad - lon1_rad

    

    # Haversine formula

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    

    return R * c



def filter_restaurants(restaurants, center_lat, center_lon, radius_miles):

    """

    Filter and return restaurants within a given radius (in miles) of a center point.

    

    restaurants: List of dictionaries, each with 'name', 'lat', and 'lon' keys

    center_lat, center_lon: Latitude and longitude of the center point

    radius_miles: Radius in miles within which to include restaurants

    """

    nearby = []

    for restaurant in restaurants:

        distance = haversine(center_lat, center_lon, restaurant['lat'], restaurant['lon'])

        if distance <= radius_miles:

            nearby.append(restaurant)

    return nearby



# Example usage:

restaurants = [

    {'name': 'Pizza Palace', 'lat': 40.730610, 'lon': -73.935242},

    {'name': 'Sushi Spot', 'lat': 40.650002, 'lon': -73.949997},

    {'name': 'Burger Barn', 'lat': 40.700292, 'lon': -73.987495},

    {'name': 'Taco Town', 'lat': 40.758896, 'lon': -73.985130},

]



# Center point: Times Square, NY

center_lat = 40.7580

center_lon = -73.9855

radius_miles = 5



nearby_restaurants = filter_restaurants(restaurants, center_lat, center_lon, radius_miles)

print("Restaurants within", radius_miles, "miles of center point:")

for r in nearby_restaurants:

    print(f"- {r['name']} (Latitude: {r['lat']}, Longitude: {r['lon']})")
