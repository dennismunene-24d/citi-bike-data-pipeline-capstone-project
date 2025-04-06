# Citi Bike NYC: A Cloud-Native Data Pipeline to Analyze Urban Mobility Patterns

![Citi Bike Logo](https://citibikenyc.com/assets/images/citi-bike-logo.png)

End-to-end data pipeline for analyzing NYC Citi Bike trip data, including ingestion, transformation, and visualization using various cloud technologies.

## Objective
To design and implement an end-to-end cloud data pipeline on GCP for ingesting, transforming, and visualizing Citi Bike trip data from Jan 2024 to Mar 2025.

## Project Architecture Overview

1. **Infrastructure Provisioning**: Use Terraform to set up GCP resources
2. **Data Ingestion**: Download and process monthly Citi Bike trip data
3. **Orchestration**: Use Airflow to schedule and manage the pipeline
4. **Data Warehouse**: Store and optimize data in BigQuery
5. **Transformations**: Implement data transformations
6. **Visualization**: Create dashboards in Looker Studio

---

## Problem Description

### Problem Statement
New York City's Citi Bike system generates vast amounts of trip data that can reveal valuable insights about urban mobility, but this data remains underutilized because:

- **Data is fragmented** across monthly files in different formats
- **No centralized system** exists to analyze long-term trends
- **Manual analysis is time-consuming** and doesn't scale
- **Key sustainability insights remain hidden** in unstructured data

### Business Questions We'll Solve
Our pipeline will enable data-driven answers to critical questions that impact operations, planning, and sustainability goals:

#### Temporal Patterns
- When are bikes most heavily used? (Peak hours/days/seasons)
- How does usage differ between members and casual riders?
- How many car trips are being replaced by bike share? (emissions impact)

#### Geospatial Analysis
- Which stations are most popular and why?
- What are the most common routes between stations?
- Where do bike shortages/surpluses typically occur?

#### Operational Efficiency
- What's the average trip duration/distance?
- How does weather affect ridership?
- Which stations need rebalancing most frequently?

### The Bigger Picture: Why This Matters

#### Environmental Benefits
- **Carbon Emission Reduction**: Each bike trip replaces 0.5-2 kg of CO₂ compared to car trips
- **Fossil Fuel Transition**: Supports NYC's 30x30 climate goal by providing zero-emission transport
- **Last-Mile Solution**: Reduces congestion by connecting transit hubs to final destinations

#### Public Health Impact
- **Chronic Disease Prevention**: Regular cycling reduces risks of obesity (+17% lower BMI), diabetes (-20% risk), and cardiovascular disease (-24% risk)
- **Mental Health Benefits**: Active commuters report 40% lower stress levels
- **Equitable Access**: Bike share provides affordable transport in transit deserts

---

## Technical Implementation

### Infrastructure Diagram
```mermaid
graph TD
    A[Terraform] --> B[GCP Resources]
    B --> C[GCS Buckets]
    B --> D[BigQuery]
    B --> E[Compute Engine]
    C --> F[Raw Data]
    F --> G[Airflow]
    G --> H[Processed Data]
    H --> D
    D --> I[dbt/pyspark Transformations]
    I --> J[Looker Studio] 

