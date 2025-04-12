# 🚲 Citi Bike NYC: Cloud-Native Data Pipeline for Urban Mobility Insights

This project presents an end-to-end cloud-native data pipeline for analyzing **Citi Bike NYC** trip data from **January 2024 to March 2025**, powered by **Google Cloud Platform (GCP)**. The solution ingests, processes, and visualizes bike-sharing data to uncover patterns in urban mobility and support data-driven transportation planning.

---

## 🎯 Objective

To design and implement a scalable data pipeline for:

- Ingesting monthly Citi Bike trip datasets
- Performing transformations for analytical readiness
- Visualizing key metrics and trends in **Looker Studio**

---

## 📦 Data Sources

- 🗃️ [Citi Bike S3 Archive](https://s3.amazonaws.com/tripdata/index.html)  
- 📊 [Citi Bike NYC System Data](https://citibikenyc.com/system-data)

---

## 🏗️ Project Architecture
- Each different part of the project architecture will be found in the following folders airflow datapipelines and terraform

| Layer                | Tool/Technology             |
|---------------------|-----------------------------|
| Infrastructure      | Terraform (GCP provisioning)|
| Data Ingestion      | Python, Cloud Storage       |
| Orchestration       | Apache Airflow              |
| Data Warehouse      | BigQuery                    |
| Transformation      | SQL (BigQuery Views)        |
| Visualization       | Looker Studio               |

---

## 🏗️ Architecture Overview
```mermaid
graph LR
    A[Raw CSVs] --> B(Airflow DAG)
    B --> C[GCS Bucket]
    C --> D[BigQuery]
    D --> E[Looker Studio]
    style B fill:#f9f,stroke:#333

---
## ❓ Problem Statement

Citi Bike NYC generates massive datasets monthly, but:

- Data is fragmented across multiple CSVs
- Long-term analysis is difficult without centralization
- Manual insights are time-consuming and don’t scale
- Sustainability and planning insights remain hidden

---
## 🚀 Quick Start

Get up and running with the Citi Bike data pipeline quickly!

### ✅ Prerequisites

Before you begin, ensure you have the following installed and configured:

-   **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
-   **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
-   **Google Cloud Platform Account**: You'll need a GCP account with billing enabled.
-   **GCS Bucket**: Create a Google Cloud Storage bucket (e.g., `citibike-data-*`) in your GCP project.
-   **BigQuery Dataset**: Create a BigQuery dataset within your GCP project to store the processed data.
-   **GCP Service Account Credentials**: Generate a service account key file with necessary permissions for GCS and BigQuery.

### 🔧 Setup & Deployment

Follow these steps to set up and deploy the pipeline:

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/your-repo/citibike-pipeline.git](https://github.com/your-repo/citibike-pipeline.git)
    cd citibike-pipeline
    ```

2.  **Prepare Credentials Directory:**

    ```bash
    mkdir -p /home/denis/auth_keys
    cp path/to/service-account.json /home/denis/auth_keys/keys.json
    ```

    **Note:** Replace `path/to/service-account.json` with the actual path to your downloaded GCP service account key file.

3.  **Start the Services:**

    ```bash
    docker-compose up -d --build
    ```

    This command will build the Docker images and start the Airflow webserver and scheduler in detached mode.

### Access the Applications:

-   **Airflow UI**: Open your web browser and navigate to `http://localhost:8080`. Use `admin` for both the username and password for the initial login.
-   **Jupyter Notebook**: Open your web browser and navigate to `http://localhost:8888`. You may need to find the token from the container logs if prompted.

## 🔄 Pipeline DAGs

The Airflow pipeline consists of the following Directed Acyclic Graphs (DAGs):

| DAG File                     | Description                                 | Output                                    |
| ---------------------------- | ------------------------------------------- | ----------------------------------------- |
| `citibike_data_pipeline.py`  | Downloads and verifies the raw data files. | `/home/denis/data/*.csv`                  |
| `merge_citibike_data.py`     | Merges multiple monthly data files.       | `/opt/notebooks/merged_data.csv`          |
| `process_citibike_data.py`   | Cleans, transforms, and uploads data to GCS. | `gs://your-bucket/processed_data/`       |

---
## 🧠 Business Questions Answered

- **Temporal Trends**: When are bikes most used (peak hours/days/seasons)?
- **User Segmentation**: How do member and casual rider patterns differ?
- **Geospatial Insights**: Which stations/routes are most popular?
- **Efficiency Metrics**: What is the average trip duration and usage by time of day?
- **Sustainability Impact**: How many car trips are replaced, and what’s the CO₂ reduction?

---

##### 📈 Dashboard (Looker Studio)

#### Explore the interactive dashboard here:  
🔗 [Looker Studio Report](https://lookerstudio.google.com/reporting/7020aeb2-cede-4b96-b1c3-3354c403f2b5/page/FJoGF)

### 📌 Highlights

- Peak usage by hour, day, and season
- Breakdown by membership type
- Top station pairings and trip volumes
- Weekend vs weekday behavior
- Duration distribution and trip category

### ⚙️ How It Works

- A BigQuery view `vw_citibike_looker_ready` is created to prepare data for reporting
- The view is connected to **Looker Studio** as the data source
- Custom fields, aggregations, and filters are applied for visualization
- Distance and speed calculations are temporarily removed to ensure compatibility

---
