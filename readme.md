# Distributed Data Reporting System

## Repository Structure
distributed-data-reporting-system/
│
├── app.py
├── config.py
├── db.py
├── models.py
├── data_ingestion.py
├── distributed_processor.py
├── reports.py
├── fault_tolerance.py
├── requirements.txt
├── README.md
└── .gitignore

## Overview
This project is a backend-focused distributed data reporting system designed to simulate
large-scale data processing and analytical reporting.

It demonstrates core Software Development Engineer fundamentals including:
- Distributed workload processing
- SQL optimization
- Fault-tolerant system design
- RESTful API development

## Tech Stack
- Python
- PostgreSQL
- SQL
- Flask (REST API)
- Git

## System Design
1. Large datasets are ingested into a relational database in batches.
2. Workloads are split into independent batches to simulate distributed processing.
3. Fault tolerance is handled using retry mechanisms.
4. Optimized SQL queries generate analytical reports.
5. REST APIs expose processing and reporting functionality.

## Key Features
- Batch-based distributed processing
- Retry-based fault tolerance
- Indexed SQL queries for performance
- Aggregated analytical reporting
- Modular and scalable design

## How to Run
1. Set up PostgreSQL and update `config.py`.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
