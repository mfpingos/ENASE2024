# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:46:54 2023

@author: mpingos
"""

import random
from faker import Faker
from datetime import datetime, timedelta
import time

fake = Faker()

def generate_data(source_id, location, variety, velocity):
    start_date = fake.date_between_dates(date_start=datetime(2019, 1, 1), date_end=datetime(2023, 12, 31))
    
    # Ensure a maximum 4-month difference for feedcycle
    max_end_date = start_date + timedelta(days=120)
    end_date = fake.date_between_dates(date_start=start_date, date_end=max_end_date)

    # Add the number of birds
    num_birds = random.randint(10000, 20000)

    # Extract the year from feedcycle_end
    year = end_date.year

    # Determine flock_size based on the number of birds
    if num_birds < 13000:
        flock_size = "low"
    elif 13000 <= num_birds <= 17000:
        flock_size = "Medium"
    else:
        flock_size = "High"

    # Add sensors_accuracy property
    sensors_accuracy = random.choice(["Medium", "High"])

    data = {
        "ex:source_name": f"{source_id}_FLOCK_{velocity}_EXPORT-{start_date.strftime('%d-%m-%Y')}",
        "ex:flockid": source_id,
        "ex:location": location,
        "ex:feedcycle_start": start_date.strftime('%Y-%m-%d'),
        "ex:feedcycle_end": end_date.strftime('%Y-%m-%d'),
        "ex:keywords": "growDay, hour, requiredTemperature, coldTemperatureAlarm, hotTemperatureAlarm, sensor1, sensor2, sensor3, sensor4, sensor5, outsideTemp, currentAverageTemp, humidity, staticPressure, currentCO2, CO2HourMax, CO2HourMin",
        "ex:variety": variety,
        "ex:velocity": velocity,
        "ex:source_path": f"hdfs://your-hadoop-namenode:9000/user/sources/daily_flock_{source_id}_data",
        "ex:owner": "Paradisiotis Group Of Companies",
        "ex:num_birds": num_birds,
        "ex:year": year,
        "ex:flock_size": flock_size,
        "ex:sensors_accuracy": sensors_accuracy
    }

    return data

def generate_volume():
    size = random.randint(1, 100)
    return f"{size} KB"

def save_to_ttl(data, filename):
    with open(filename, 'a') as file:
        file.write("@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.\n")
        file.write("@prefix ex: <http://example.org/>.\n\n")

        for source_id, details in data.items():
            file.write(f"ex:source{source_id}\n")
            file.write("  rdf:type ex:Description ;\n")
            for key, value in details.items():
                file.write(f"  {key} \"{value}\" ;\n")
            file.write("  .\n\n")

if __name__ == "__main__":
    start_time = time.time()

    data_size = int(input("Enter the number of sources to generate: "))

    data = {}

    for source_id in range(1, data_size + 1):
        location = random.choice(["Larnaca", "Famagusta", "Nicosia", "Pafos", "Limassol"])
        variety = random.choice(["structured", "unstructured", "semi-structured"])
        velocity = random.choice(["Hourly", "Daily", "Monthly", "Yearly"])

        data[source_id] = generate_data(source_id, location, variety, velocity)

    for source_id, details in data.items():
        volume = generate_volume()
        details["ex:volume"] = volume

    ttl_filename = input("Enter the TTL file name to save the data (e.g., output.ttl): ")
    save_to_ttl(data, ttl_filename)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Random data has been generated and saved to {ttl_filename}.")
    print(f"Execution time: {execution_time} seconds.")
