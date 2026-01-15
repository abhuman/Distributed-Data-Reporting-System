# Distributed Data Reporting System

## Overview
This project is a backend-focused distributed data reporting system designed to simulate
large-scale data processing and analytical reporting.

It demonstrates core Software Development Engineer fundamentals, including:
- Distributed workload processing
- SQL query optimization
- Fault-tolerant system design
- RESTful API development

---

## Repository Structure
```
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
```

---

## Tech Stack
- **Programming Language:** Python
- **Database:** PostgreSQL
- **Query Language:** SQL
- **API Framework:** Flask (REST APIs)
- **Version Control:** Git

---

## System Design
1. Large datasets are ingested into a relational database in batches.
2. Workloads are split into independent batches to simulate distributed processing.
3. Fault tolerance is achieved using retry-based error handling.
4. Optimized SQL queries generate aggregated analytical reports.
5. REST APIs expose data processing and reporting functionality.

---

## Key Features
- Batch-based distributed workload simulation
- Retry-based fault tolerance for failure handling
- Indexed SQL queries for performance optimization
- Aggregated analytical reporting
- Modular, scalable backend design

---

## How to Run

### 1. Configure Database
Set up PostgreSQL and update database credentials in `config.py`.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create Database Tables
```bash
python -c "import models; models.create_tables()"
```

### 4. Start the Application
```bash
python app.py
```

### 5. Available API Endpoints
- **POST** `/process-data`  
  Simulates distributed batch processing and data ingestion.

- **POST** `/generate-report`  
  Generates aggregated analytical reports using optimized SQL queries.

---

## Interview Talking Points
- Simulated distributed systems using batch-based processing
- Implemented fault-tolerant retry mechanisms
- Optimized SQL queries using indexing and aggregation
- Designed scalable REST APIs
- Owned the system end-to-end, from design to implementation

---

## Author
**Abir Roy**
