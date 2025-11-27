End-to-End ETL Pipeline on Google Cloud

This project is a fully automated ETL data pipeline built using Google Cloud services. It generates synthetic employee data, transforms it, loads it into BigQuery, visualizes it, and automates the entire workflow via Airflow.

🚀 Tech Stack

Python (Faker) – Data generation

Google Cloud Storage – Raw data storage

Cloud Data Fusion – Data transformation & masking

BigQuery – Data warehouse

Looker Studio – Dashboard & reporting

Cloud Composer (Airflow) – Automation & scheduling

🔄 Pipeline Flow
Python → Cloud Storage → Data Fusion → BigQuery → Looker Studio
                        ↑
                    Cloud Composer

📁 Files

extract.py — Generates & uploads employee data

dag.py — Airflow DAG to automate ETL

employee_data.csv — Sample generated data

⚙️ How It Works

Generate synthetic employee data using Python

Upload CSV to Cloud Storage

Use Data Fusion Wrangler to join names, mask salary, encode password

Data Fusion pipeline loads processed data into BigQuery

Looker Studio visualizes the employee dataset

Cloud Composer runs the entire ETL daily using Airflow
