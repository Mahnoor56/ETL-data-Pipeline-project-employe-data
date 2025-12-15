import os
import csv
from faker import Faker
import random
import string
from google.cloud import storage

# Set the path to your service account JSON key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\LENOVO\Downloads\dataform-460508-8560b3c0cddc.json"

# Config
project_name = 'dataform-460508'
bucket_name = 'employe_data1'
source_file_name = 'employee_data.csv'
destination_blob_name = 'employee_data.csv'
num_employees = 100

# Create Faker instance
fake = Faker()

# Define password character set (exclude comma to avoid CSV parsing issues)
password_characters = string.ascii_letters + string.digits + "!@#$%^&*()_+=-"

# Generate employee data and save to CSV
with open(source_file_name, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['first_name', 'last_name', 'job_title', 'department', 'email',
                  'address', 'phone_number', 'salary', 'password']
    writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

    writer.writeheader()
    for _ in range(num_employees):
        writer.writerow({
            "first_name": fake.first_name().replace(',', ''),  # remove any commas if present
            "last_name": fake.last_name().replace(',', ''),
            "job_title": fake.job().replace(',', ''),
            "department": fake.job().replace(',', ''),
            "email": fake.email(),
            "address": fake.city().replace(',', ''),
            "phone_number": fake.phone_number().replace(',', ''),
            "salary": int(fake.random_number(digits=5)),  # ensure salary is an int
            "password": ''.join(random.choices(password_characters, k=8))
        })

print(f"✅ {num_employees} fake employee records created in {source_file_name}")

# upload files in gcs bucket
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name, project):
    storage_client = storage.Client(project=project)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f'✅ File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.')

# execute  uploaded functions
upload_to_gcs(bucket_name, source_file_name, destination_blob_name, project_name)





