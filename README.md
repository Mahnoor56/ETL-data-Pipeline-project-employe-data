📊 ETL Data Pipeline with GCP & Data Fusion
This project demonstrates a full end-to-end ETL (Extract, Transform, Load) pipeline on Google Cloud Platform, starting from synthetic data generation using Python, to automated transformation using Cloud Data Fusion, and finally loading into a data warehouse for analytics.

🚀 Project Overview
Objective:
Build a scalable and modular ETL pipeline that:

Generates fake data using the Python faker library.

Exports the data to a .csv file.

Uploads the CSV to Google Cloud Storage (GCS).

Triggers a Cloud Data Fusion pipeline for:

Data ingestion from GCS

Transformation steps (e.g., cleaning, formatting)

Loading the clean data into BigQuery

🔁 ETL Workflow Breakdown
1. Extract (Fake Data Generation)
Use Python with the faker library to create synthetic user/customer/transaction data.

Export the generated data to a .csv file.

2. Load to Cloud Storage
Upload the generated CSV to a specified GCS bucket using the google-cloud-storage Python client.

3. Transform & Load (Cloud Data Fusion)
Design an ETL pipeline in Cloud Data Fusion (UI-based).

Configure a source plugin (GCS), transformation logic (Wrangler, Wrangler Directives), and a sink plugin (BigQuery).

Deploy the pipeline to perform the full ETL process.

🧰 Tools & Technologies
Google Cloud Platform

Google Cloud Storage (GCS)

Cloud Data Fusion

BigQuery

Python

faker (for data generation)

pandas (for DataFrame handling)

google-cloud-storage (for GCS upload)

Cloud Data Fusion

Source: GCS

Transform: Wrangler, JavaScript, Schema changes

Sink: BigQuery
