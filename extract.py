from faker import Faker
import csv
import random
from google.cloud import storage
import os
import hashlib  # Only needed if using hashed passwords option

# -----------------------------
# CONFIGURATION
# -----------------------------

NUM_EMPLOYEES = 150
OUTPUT_FILE = "employee_data.csv"
GCS_BUCKET_NAME = "bucket-employee-datas"
GCS_DESTINATION_BLOB = "employee_data.csv"

fake = Faker()

DEPARTMENTS = ["HR", "Finance", "Engineering", "Sales", "Marketing", "IT Support"]

def generate_employee():
    # Simple Faker Password
    password = fake.password(
        length=12,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )

    # Clean address to prevent CSV & BigQuery issues
    address = fake.address().replace('\n', ', ').replace('"', "'")

    return {
        "employee_id": fake.unique.random_number(digits=6),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "date_of_birth": fake.date_of_birth(minimum_age=20, maximum_age=65).isoformat(),
        "ssn": fake.ssn(),
        "address": address,
        "department": random.choice(DEPARTMENTS),
        "salary": random.randint(35000, 150000),
        "password": password
    }

def generate_employee_data(num_records):
    return [generate_employee() for _ in range(num_records)]

def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, 
            fieldnames=data[0].keys(),
            quoting=csv.QUOTE_ALL  # <-- CRITICAL FIX
        )
        writer.writeheader()
        writer.writerows(data)

# -----------------------------
# UPLOAD TO GCS
# -----------------------------

def upload_to_gcs(bucket_name, source_file, destination_blob):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(source_file)
    print(f"File uploaded to gs://{bucket_name}/{destination_blob}")

# -----------------------------
# MAIN EXECUTION
# -----------------------------

if __name__ == "__main__":
    employees = generate_employee_data(NUM_EMPLOYEES)
    save_to_csv(employees, OUTPUT_FILE)
    print(f"Generated {NUM_EMPLOYEES} employee records")
    print(f"CSV saved locally as: {OUTPUT_FILE}")

    upload_to_gcs(GCS_BUCKET_NAME, OUTPUT_FILE, GCS_DESTINATION_BLOB)
