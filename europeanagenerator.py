import random
from faker import Faker
from datetime import datetime, timedelta
import time

fake = Faker()

def generate_data(source_id):
    languages = ["en", "fr", "de", "es", "it"]
    themes = ["Archeology", "Art", "Fashion", "Industrial Heritage", "Manuscript", "Music", "Maps and Geography", "Migration", "Natural History", "Newspapers", "Photography", "Sport", "World War I"]

    rights = ["http://creativecommons.org/publicdomain/zero/1.0/", 
              "http://creativecommons.org/publicdomain/mark/1.0/",
              "http://creativecommons.org/licenses/by/3.0/",
              "http://creativecommons.org/licenses/by-sa/3.0/",
              "http://creativecommons.org/licenses/by-nc/3.0/",
              "All rights reserved"]

    start_date = fake.date_between_dates(date_start=datetime(1000, 1, 1), date_end=datetime(2023, 12, 31))
    max_end_date = start_date + timedelta(days=120)
    end_date = fake.date_between_dates(date_start=start_date, date_end=max_end_date)
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.min.time())

    data = {
        "ex:providing_institution": fake.company(),
        "ex:theme": random.choice(themes),
        "ex:contributors": f"{fake.name()}, {fake.name()}",
        "ex:creator": fake.name(),
        "ex:type_of_object": random.choice(["Text", "Image", "Sound", "Video", "3D"]),
        "ex:subject": f"{fake.word()}, {fake.word()}",
        "ex:date": start_date.strftime('%Y-%m-%d'),
        "ex:title": fake.sentence(),
        "ex:provider_collection_name": fake.company(),
        "ex:rights": random.choice(rights),
        "ex:identifier": f"Identifier-{source_id}",
        "ex:places": f"{fake.city()}, {fake.city()}",
        "ex:format": random.choice(["text/plain", "image/jpeg", "audio/mp3", "video/mp4"]),
        "ex:providing_country": fake.country(),
        "ex:language": random.choice(languages),
        "ex:timestamp_created": start_datetime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "ex:timestamp_updated": end_datetime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "ex:variety": random.choice(["structured", "unstructured", "semi-structured"]),
        "ex:velocity": random.choice(["Hourly", "Daily", "Monthly", "Yearly"]),
        "ex:source_path": f"hdfs://your-hadoop-namenode:9000/user/sources/daily_flock_{source_id}_data"
    }

    return data

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

    num_sources = int(input("Enter the number of sources to generate: "))
    ttl_filename = input("Enter the TTL file name to save the data (e.g., output.ttl): ")

    data = {}
    for source_id in range(1, num_sources + 1):
        data[source_id] = generate_data(source_id)

    save_to_ttl(data, ttl_filename)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{num_sources} sources have been generated and saved to {ttl_filename}.")
    print(f"Execution time: {execution_time} seconds.")
