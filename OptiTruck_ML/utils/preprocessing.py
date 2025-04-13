
from geopy.distance import geodesic
import datetime

# This script serves as a preprocessor as the name suggests.
""" I am making sure that the user does not need to type much information which can be derived from the others
    i.e.
         Truck Capacity derived from truck_type
         Distance derived from from_city and to_city
         and Seasons from departure_date 

 """

# Truck Type -> Space Capacity ( personal note: the values are in tons, DONT CHANGE EM!!!)

TRUCK_CAPACITY = {
    "Light Commercial Vehicles": 10,
    "Medium Commercial Vehicles": 20,
    "Heavy Commercial Vehicles": 30,
    "Container trucks": 40,
    "Trailer trucks": 50
}

# Indian City Coordinates : ( personal note: there are around 50 place coordinates in here, just make sure that the request cities start with capital letter! )
CITY_COORDINATES =  { "Delhi": (28.6139, 77.2090), "Mumbai": (19.0760, 72.8777), "Bangalore": (12.9716, 77.5946),
                      "Chennai": (13.0827, 80.2707), "Kolkata": (22.5726, 88.3639), "Hyderabad": (17.3850, 78.4867),
                      "Pune": (18.5204, 73.8567), "Ahmedabad": (23.0225, 72.5714), "Jaipur": (26.9124, 75.7873),
                      "Lucknow": (26.8467, 80.9462), "Indore": (22.7196, 75.8577), "Bhopal": (23.2599, 77.4126),
                      "Nagpur": (21.1458, 79.0882), "Patna": (25.5941, 85.1376), "Visakhapatnam": (17.6868, 83.2185),
                      "Surat": (21.1702, 72.8311), "Kanpur": (26.4499, 80.3319), "Ludhiana": (30.9000, 75.8573),
                      "Agra": (27.1767, 78.0081), "Vadodara": (22.3072, 73.1812), "Nashik": (19.9975, 73.7898),
                      "Vijayawada": (16.5062, 80.6480), "Rajkot": (22.3039, 70.8022), "Amritsar": (31.6340, 74.8723),
                       "Allahabad": (25.4358, 81.8463), "Coimbatore": (11.0168, 76.9558), "Guwahati": (26.1445, 91.7362),
                      "Thiruvananthapuram": (8.5241, 76.9366), "Ranchi": (23.3441, 85.3096), "Jodhpur": (26.2389, 73.0243),
                      "Raipur": (21.2514, 81.6296), "Madurai": (9.9252, 78.1198), "Meerut": (28.9845, 77.7064),
                      "Jabalpur": (23.1815, 79.9864), "Gwalior": (26.2183, 78.1828), "Hubli": (15.3647, 75.1240),
                      "Tiruchirappalli": (10.7905, 78.7047), "Udaipur": (24.5854, 73.7125), "Dehradun": (30.3165, 78.0322),
                      "Mangalore": (12.9141, 74.8560), "Vellore": (12.9165, 79.1325), "Warangal": (17.9784, 79.5941),
                      "Solapur": (17.6599, 75.9064), "Kozhikode": (11.2588, 75.7804), "Nanded": (19.1383, 77.3210),
                      "Jhansi": (25.4484, 78.5685), "Kolhapur": (16.7050, 74.2433), "Dhanbad": (23.7957, 86.4304),
                      "Bhavnagar": (21.7645, 72.1519), "Bilaspur": (22.0797, 82.1409), "Jamshedpur": (22.8046, 86.2029) }

# To calculate the distance between the cities using the coordinates

def calculate_distance(from_city, to_city):
    """Calculate the distance between two cities."""
    if from_city in CITY_COORDINATES and to_city in CITY_COORDINATES:
        return geodesic(CITY_COORDINATES[from_city], CITY_COORDINATES[to_city]).km
    return 0  # Default distance if city is not found


# To find seasons based upon the departure date
def extract_seasonality(departure_date):
    """Extract seasonality (e.g., 0 = winter, 1 = spring, etc.) from the date."""
    month = datetime.datetime.strptime(departure_date, "%Y-%m-%d").month
    if month in [12, 1, 2]:
        return 0  # Winter
    elif month in [3, 4, 5]:
        return 1  # Spring
    elif month in [6, 7, 8]:
        return 2  # Summer
    else:
        return 3  # Fall

# Truck Capacity, Distance and Seasons are extracted from truck_type, departure_date, from_city, to_city

def preprocess_input(truck_type, departure_date, from_city, to_city):
    """Convert raw input into a feature vector."""
    truck_capacity = TRUCK_CAPACITY.get(truck_type, 0)
    distance = calculate_distance(from_city, to_city)
    season = extract_seasonality(departure_date)

    return [truck_capacity, distance, season]
