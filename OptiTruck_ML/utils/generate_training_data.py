import random
import datetime
import csv
from utils.preprocessing import preprocess_input, CITY_COORDINATES, TRUCK_CAPACITY


#  As the name suggests, I have made this script to generate csv file in order to train models for price and demand prediction


# Number of samples to generate
NUM_SAMPLES = 5000

# Output CSV file
OUTPUT_FILE = "../data/training_data.csv"

# Get all city names
cities = list(CITY_COORDINATES.keys())
truck_types = list(TRUCK_CAPACITY.keys())

def generate_random_date(start_year=2023, end_year=2025):
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    delta = end - start
    random_day = start + datetime.timedelta(days=random.randint(0, delta.days))
    return random_day.strftime("%Y-%m-%d")

# Price formula (tweak if you want)
def simulate_price(capacity, distance, season):
    base_price = distance * 8 + capacity * 300
    seasonal_factor = 1.1 if season == 2 else (0.95 if season == 0 else 1.0)
    noise = random.uniform(-500, 500)
    return round(base_price * seasonal_factor + noise, 2)

# Demand formula (influenced by distance, capacity, season)
def simulate_demand(capacity, distance, season):
    base = 1000 + capacity * 15 - distance * 0.2
    seasonal_boost = 200 if season == 2 else (-100 if season == 0 else 50)
    noise = random.uniform(-100, 100)
    return max(0, round(base + seasonal_boost + noise, 2))

def generate_dataset():
    rows = []

    for _ in range(NUM_SAMPLES):
        from_city, to_city = random.sample(cities, 2)
        truck_type = random.choice(truck_types)
        departure_date = generate_random_date()

        # Get features
        try:
            features = preprocess_input(truck_type, departure_date, from_city, to_city)
            capacity, distance, season = features

            price = simulate_price(capacity, distance, season)
            demand = simulate_demand(capacity, distance, season)

            rows.append([
                truck_type,
                departure_date,
                from_city,
                to_city,
                capacity,
                round(distance, 2),
                season,
                price,
                demand
            ])

        except Exception as e:
            print(f"Error generating row: {e}")

    # Write to CSV
    with open(OUTPUT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["truck_type", "departure_date", "from_city", "to_city",
                         "capacity", "distance_km", "season", "price", "demand"])
        writer.writerows(rows)

    print(f"✅ Generated {len(rows)} samples and saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_dataset()
