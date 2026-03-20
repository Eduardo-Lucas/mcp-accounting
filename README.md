# MCP Accounting

An **AI-ready accounting anomaly detection API** built with **Python, FastAPI, PostgreSQL, and Docker**.

This project demonstrates how financial analysis can be exposed as **callable API tools**, enabling integration with automation systems and AI agents.

---

# Overview

The system processes accounting transactions and provides:

* anomaly detection
* structured reporting
* AI-generated explanations

It follows a modern backend architecture with **data ingestion, persistence, analytics, and AI layers**, fully containerized with Docker.

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
✔ Fully containerized environment (Docker + Docker Compose)

---

# Architecture

```id="6jqqc6"
Client
   ↓
FastAPI API (Docker)
   ↓
Service Layer
   ↓
PostgreSQL (Docker)
   ↓
Analytics + AI Explanation
```

Project structure:

```id="3pq4u0"
mcp-accounting
│
├── app/
├── data/
├── scripts/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env
```

---

# Run with Docker (Recommended)

Start the entire system:

```bash id="9tx1x0"
docker compose up --build
```

This will start:

* FastAPI application
* PostgreSQL database

API available at:

```id="r6typo"
http://localhost:8000/docs
```

---

# Manual Setup (Without Docker)

```bash id="b7s0ey"
git clone https://github.com/<your-username>/mcp-accounting.git
cd mcp-accounting

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```id="6c9dlh"
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=postgresql://postgres:postgres@127.0.0.1:5432/mcp_accounting
```

---

# Database Setup (Manual)

```sql id="6qg17q"
CREATE DATABASE mcp_accounting;
```

Tables are created automatically on startup.

---

# API Endpoints

## Health

```id="7y2jqn"
GET /health
```

---

## Upload Transactions (Ingestion)

```id="8cfu6l"
POST /upload-transactions
```

```bash id="h2j32b"
curl -F "file=@data/transactions.csv" \
http://localhost:8000/upload-transactions
```

---

## Detect Large Transactions

```id="w1w0sk"
POST /tools/detect_large_expenses
```

---

## Detect Duplicate Payments

```id="bn04bt"
POST /tools/find_duplicate_payments
```

---

## Generate Anomaly Report

```id="ub2p4c"
POST /report/anomalies
```

---

## Generate AI-Explained Report

```id="m7i1lq"
POST /report/anomalies/explain
```

```bash id="qhr2gl"
curl -X POST http://localhost:8000/report/anomalies/explain
```

---

# Example Workflow

```id="xztij1"
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
* Docker
* Docker Compose

---

# Development Status

This project is an **evolving MVP focused on AI-assisted accounting analysis**.

Recent improvements:

* PostgreSQL persistence layer
* Data ingestion pipeline (CSV → DB)
* AI explanation service
* Dockerized environment with healthcheck and startup synchronization

Planned improvements:

* Vendor spending anomaly detection
* Time-based anomaly detection
* Alembic migrations
* Authentication (API keys)
* Dashboard UI

---

# License

MIT License

---

# Author

Edu
Senior Python Developer
