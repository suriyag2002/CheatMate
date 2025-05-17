import random
import time
import csv
from datetime import datetime, timedelta

# Sample vehicle numbers and locations
vehicle_numbers = ['KA01AB1234', 'DL3EF9876', 'MH12CD5678']
locations = ['Out for Delivery', 'Sorting Center - Delhi', 'Distribution Hub - Mumbai', 'Transit Point - Hyderabad']

# Create a function to generate random IoT data
def generate_iot_data():
    vehicle_number = random.choice(vehicle_numbers)
    temperature = round(random.uniform(15.0, 35.0), 2)  # Random temperature between 15 and 35
    humidity = round(random.uniform(30.0, 80.0), 2)  # Random humidity between 30 and 80
    location = random.choice(locations)
    timestamp = (datetime.now() - timedelta(seconds=random.randint(0, 100))).strftime('%Y-%m-%d %H:%M:%S')  # Dynamic timestamp

    # Create a dictionary to hold the generated data
    data = {
        'vehicle_number': vehicle_number,
        'temperature': temperature,
        'humidity': humidity,
        'location': location,
        'timestamp': timestamp
    }

    return data

# Path for the CSV file
csv_file = 'iot_parcel_data.csv'

# Write headers to CSV if the file doesn't exist
def write_headers_if_not_exists():
    try:
        with open(csv_file, mode='r', newline='') as file:
            pass  # File exists, no need to write headers
    except FileNotFoundError:
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["vehicle_number", "temperature", "humidity", "location", "timestamp"])
            writer.writeheader()  # Write headers if file is not found

# Write data to CSV
def write_data_to_csv(data):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["vehicle_number", "temperature", "humidity", "location", "timestamp"])
        writer.writerow(data)

# Generate and write data
def generate_and_write_data():
    write_headers_if_not_exists()  # Ensure headers are written
    data = generate_iot_data()
    write_data_to_csv(data)
    print(f"New data recorded: {data}")

# Run the function every 10 seconds to simulate real-time data generation
if __name__ == "__main__":
    while True:
        generate_and_write_data()
        time.sleep(10)  # Wait for 10 seconds before generating the next data point
