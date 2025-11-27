# End-to-End ETL Pipeline on Google Cloud

This project is an **automated ETL pipeline** built using Google Cloud Platform (GCP).  
It generates synthetic employee data, uploads it to Cloud Storage, transforms and masks the data using Cloud Data Fusion, loads the processed data into BigQuery, and visualizes it in Looker Studio—all automated with Cloud Composer (Airflow).

---

## Features

- **Synthetic Data Generation**  
  Python and the Faker library are used to generate realistic employee records.

- **Cloud Storage Integration**  
  The generated CSV file is uploaded directly into a Google Cloud Storage bucket.

- **Data Transformation and Masking**  
  Cloud Data Fusion Wrangler is used to clean data, join columns, mask salary values, and encode passwords.

- **BigQuery Data Warehouse**  
  The transformed dataset is loaded into BigQuery for analytics and reporting.

- **Interactive Dashboard**  
  Looker Studio provides visual reporting by connecting directly to BigQuery.

- **Automated ETL Workflow**  
  Cloud Composer (Airflow) orchestrates the full ETL flow on a scheduled basis.

---

## Technologies Used

- **Python (Faker)** – Data generation  
- **Google Cloud Storage** – Raw data storage  
- **Cloud Data Fusion** – ETL and transformation  
- **BigQuery** – Data warehouse  
- **Looker Studio** – Dashboard & reporting  
- **Cloud Composer (Airflow)** – Workflow automation  

---

## ETL Pipeline Flow

```

```

---

## Project Files

- `extract.py` – Generates & uploads employee data  
- `dag.py` – Airflow DAG to automate ETL  
- `employee_data.csv` – Sample generated dataset  

---

## How It Works

1. **Generate Data**  
   The Python script creates synthetic employee records with fields such as name, department, salary, SSN, and password.

2. **Upload to Cloud Storage**  
   The CSV file is uploaded to the Google Cloud Storage bucket.

3. **Transform Data in Data Fusion**  
   Wrangler performs the following:  
   - Join first and last name  
   - Mask salary  
   - Encode passwords  
   - Clean address fields  

4. **Load into BigQuery**  
   A Data Fusion batch pipeline loads the cleaned data into the BigQuery table `employee.emp_data`.

5. **Visualize Using Looker Studio**  
   Looker Studio connects to BigQuery to create real-time reports and dashboard views.

6. **Automate with Cloud Composer**  
   The Airflow DAG automates extraction and triggers the Data Fusion pipeline daily.

---

## Running the Extraction Script

```bash
python extract.py
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/end-to-end-etl.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Authenticate Google Cloud credentials.

---

## License

This project is open source and free to use.
