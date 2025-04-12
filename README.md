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

## ❓ Problem Statement

Citi Bike NYC generates massive datasets monthly, but:

- Data is fragmented across multiple CSVs
- Long-term analysis is difficult without centralization
- Manual insights are time-consuming and don’t scale
- Sustainability and planning insights remain hidden

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

## 🛠️ View Definition (BigQuery)

A cleaned-up version of the analytical view omitting unsupported geographic calculations can be found in:
