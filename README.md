# MCP Accounting

An **AI-ready accounting anomaly detection API** built with **Python, FastAPI, and PostgreSQL**.

This project demonstrates how financial analysis can be exposed as **callable API tools**, enabling automation and integration with AI agents.

---

# Overview

The system processes accounting transactions and provides:

* anomaly detection
* structured reporting
* AI-generated explanations

It follows a modern backend architecture with **data ingestion, persistence, analytics, and AI layers**.

---

# Features

✔ Upload accounting datasets via API
✔ Persistent storage using PostgreSQL
✔ Detect unusually large transactions
✔ Detect duplicate vendor payments
✔ Generate anomaly reports
✔ AI-generated explanations for anomalies
✔ Modular FastAPI architecture (API / services / data layers)
✔ MCP-style tool endpoints for automation and AI agents

---

# Architecture

```id="6mrm5n"
Client
   ↓
FastAPI API
   ↓
Service Layer
   ↓
PostgreSQL Database
   ↓
Analytics + AI Explanation
```

Project structure:

```id="qcyweq"
mcp-accounting
│
├── app
│   ├── api
│   ├── core
│   ├── data
│   ├── mcp
│   ├── models
│   ├── services
│   └── main.py
│
├── data
├── requirements.txt
└── README.md
```

---

# Installation

```bash id="c04xv6"
git clone https://github.com/<your-username>/mcp-accounting.git
cd mcp-accounting
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```id="8p8k7b"
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=postgresql://postgres:postgres@127.0.0.1:5432/mcp_accounting
```

---

# Running the Application

Start the API:

```bash id="h1bx68"
uvicorn app.main:app --reload
```

Access:

```id="qhlc2y"
http://127.0.0.1:8000/docs
```

---

# Database Setup

Ensure PostgreSQL is running and create the database:

```sql id="h4d1y3"
CREATE DATABASE mcp_accounting;
```

Tables are created automatically on startup.

---

# API Endpoints

## Health

```id="7r0fgi"
GET /health
```

---

## Upload Transactions (Ingestion)

```id="zkc4tm"
POST /upload-transactions
```

```bash id="8f0e4o"
curl -F "file=@data/transactions.csv" \
http://127.0.0.1:8000/upload-transactions | jq
```

---

## Detect Large Transactions

```id="s7vlxm"
POST /tools/detect_large_expenses
```

---

## Detect Duplicate Payments

```id="3rt0in"
POST /tools/find_duplicate_payments
```

---

## Generate Anomaly Report

```id="ujg3m9"
POST /report/anomalies
```

---

## Generate AI-Explained Report

```id="yijbof"
POST /report/anomalies/explain
```

```bash id="lf3o1g"
curl -X POST http://127.0.0.1:8000/report/anomalies/explain | jq
```

---

# Example Workflow

```id="x2ydny"
Upload CSV
→ Data ingested into PostgreSQL
→ Run anomaly detection
→ Generate report
→ Get AI explanations
```

---

# Technology Stack

* Python
* FastAPI
* Pandas
* PostgreSQL
* SQLAlchemy
* OpenAI API
* python-dotenv

---

# Development Status

This project is an **evolving MVP** focused on AI-assisted accounting analysis.

Recent improvements:

* PostgreSQL persistence layer
* Data ingestion pipeline (CSV → DB)
* AI explanation service

Planned improvements:

* Dockerized environment (API + DB)
* Vendor spending anomaly detection
* Time-based anomaly detection
* Batch AI explanations
* Dashboard UI

---

# License

MIT License

---

# Author

Edu
Senior Python Developer
