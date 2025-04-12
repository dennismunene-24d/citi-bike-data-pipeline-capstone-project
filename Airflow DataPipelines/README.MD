# 🚴 Citibike Data Pipeline with Apache Airflow

![Airflow](https://img.shields.io/badge/Apache_Airflow-2.6+-blue)
![Python](https://img.shields.io/badge/Python-3.8+-yellowgreen)
![GCP](https://img.shields.io/badge/Google_Cloud-Platform-orange)
![Docker](https://img.shields.io/badge/Docker-Containers-blue)

A production-grade data pipeline that processes Citibike trip data from raw CSVs to analysis-ready Parquet files in Google Cloud Storage, with optional loading to BigQuery.

## 📌 Key Features

- **End-to-end workflow**: Download → Validate → Merge → Process → Store
- **Cloud Integration**: Seamless GCS uploads with Airflow hooks
- **Data Quality**: Built-in validation checks at each stage
- **Reproducible**: Containerized with Docker
- **Extensible**: Modular DAG design for easy customization

## 🏗️ Architecture



## 🛠️ Technical Stack

| Component        | Technology Used                   |
|------------------|-----------------------------------|
| Orchestration    | Apache Airflow 2.6+               |
| Data Processing  | pandas, pyarrow, geopy            |
| Storage          | Google Cloud Storage              |
| Containerization | Docker + Docker Compose           |
| Metadata DB      | PostgreSQL                        |

---

## 🚀 Getting Started

### Prerequisites

- **Docker** & **Docker Compose**

- **Google Cloud Account** with:
  - A GCS bucket:  
    `citibike-data-stellar-mercury-455917-d9-dev`
  - A service account with **Storage Admin** permissions


git clone https://github.com/your-repo/citibike-pipeline.git
cd citibike-pipeline

mkdir -p /home/denis/auth_keys
# Place your service account JSON key here
cp path/to/your-key.json /home/denis/auth_keys/keys.json

## ⏳ Wait for Initialization

After running `docker-compose up`, wait **2–3 minutes**, then access:

- **Airflow UI**: [http://localhost:8080](http://localhost:8080)  
  *Username*: `admin` • *Password*: `admin`

- **Jupyter Notebooks**: [http://localhost:8888](http://localhost:8888)

---

## 🔄 Pipeline Execution

Trigger DAGs in the following order via the Airflow UI:

1. **`citibike_data_pipeline`**: Downloads raw Citibike trip data.
2. **`merge_citibike_data`**: Merges monthly CSV files.
3. **`process_citibike_data`**: Processes and uploads to GCS.

---

### 📤 Manual BigQuery Load

Once the `.parquet` file is in GCS, load it manually into BigQuery:

```bash
bq load --source_format=PARQUET \
  dataset.citibike_trips \
  gs://citibike-data-stellar-mercury-455917-d9-dev/processed_data/*
## 📂 Data Flow Details

| Stage          | Location                                       | Format  |
|----------------|------------------------------------------------|---------|
| Raw Input      | `/home/denis/data/`                            | CSV     |
| Merged Data    | `/opt/notebooks/merged_citibike_trips.csv`     | CSV     |
| Processed Data | `/home/denis/data/processed_citibike_data.parquet` | Parquet |
| Cloud Storage  | `gs://citibike-data.../processed_data/`        | Parquet |

## ⚙️ Configuration

### 🔑 Key Environment Variables

Set in `docker-compose.yaml`:
```yaml
GOOGLE_APPLICATION_CREDENTIALS: "/opt/airflow/auth_keys/keys.json"
GCS_BUCKET: "citibike-data-stellar-mercury-455917-d9-dev"

## 🔧 Customizing the Pipeline

- **Change Data Sources**: Edit `scripts/download.sh`
- **Modify Processing Logic**: Edit `process_citibike_data.py`
- **Adjust DAG Schedule**: Change `schedule_interval` in each DAG file

## 🚨 Troubleshooting

| Symptom               | Solution                                                                 |
|-----------------------|--------------------------------------------------------------------------|
| DAGs not appearing    | Check DAG folder volume mount in `docker-compose.yaml`                   |
| GCS permission errors | Ensure service account has `storage.objects.create` permission            |
| Dependency conflicts  | Rebuild containers: `docker-compose build --no-cache`                    |

## 🪵 Access Logs

```bash
docker-compose logs -f airflow-webserver
docker-compose logs -f airflow-scheduler
