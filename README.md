# MCP Accounting

An **AI-ready accounting anomaly detection API** built with **Python and FastAPI**.
This project demonstrates how financial analysis capabilities can be exposed as **callable tools**, making them usable by automation systems or AI agents.

The system analyzes accounting transactions, detects suspicious patterns, and generates **AI explanations for flagged anomalies**.

---

# Overview

Traditional accounting analysis is often manual and time-consuming.
This project explores a different architecture:

**Expose accounting analytics as API tools that can be called by software or AI agents.**

The service:

1. Accepts accounting datasets (CSV)
2. Detects potential anomalies
3. Generates a structured report
4. Uses AI to explain suspicious transactions

---

# Current Features

✔ Upload accounting datasets via API
✔ Detect unusually large transactions
✔ Detect duplicate vendor payments
✔ Generate anomaly reports
✔ AI-generated explanations for suspicious transactions
✔ Clean modular FastAPI architecture
✔ CLI testing with `curl` and `jq`
✔ Upload accounting datasets via API  
✔ Detect unusually large transactions  
✔ Detect duplicate vendor payments  
✔ Generate anomaly reports  
✔ AI-generated explanations for suspicious transactions  
✔ Modular FastAPI architecture (API / services / data layers)
✔ MCP-style tool endpoints for automation or AI agents

---

# Architecture

The backend follows a **layered architecture**:

```
HTTP API
   ↓
API Routes
   ↓
Service Layer
   ↓
Data Layer
```

Project structure:

```
mcp-accounting
│
├── app
│   ├── api
│   │   └── routes.py
│   │
│   ├── core
│   │   └── config.py
│   │
│   ├── data
│   │   └── loader.py
│   │
│   ├── mcp
│   │   └── tools.py
│   │
│   ├── models
│   │   └── schemas.py
│   │
│   ├── services
│   │   ├── anomaly_detection.py
│   │   ├── report_service.py
│   │   └── explanation_service.py
│   │
│   └── main.py
│
├── data
│   └── transactions.csv
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/<your-username>/mcp-accounting.git
cd mcp-accounting
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

The application loads this automatically using `python-dotenv`.

---

# Running the Server

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

# API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check

```
GET /health
```

Example:

```
curl http://127.0.0.1:8000/health
```

---

## Upload Transactions Dataset

```
POST /upload-transactions
```

Example:

```
curl -F "file=@data/transactions.csv" \
http://127.0.0.1:8000/upload-transactions
```

---

## Detect Large Transactions

```
POST /tools/detect_large_expenses
```

Example:

```
curl -X POST http://127.0.0.1:8000/tools/detect_large_expenses | jq
```

---

## Detect Duplicate Payments

```
POST /tools/find_duplicate_payments
```

Example:

```
curl -X POST http://127.0.0.1:8000/tools/find_duplicate_payments | jq
```

---

## Generate Anomaly Report

```
POST /report/anomalies
```

Example:

```
curl -X POST http://127.0.0.1:8000/report/anomalies | jq
```

Example response:

```json
{
  "summary": {
    "transactions_analyzed": 5,
    "anomalies_detected": 3
  },
  "anomalies": [...]
}
```

---

## Generate AI-Explained Anomaly Report

```
POST /report/anomalies/explain
```

Example:

```
curl -X POST http://127.0.0.1:8000/report/anomalies/explain | jq
```

Example output:

```json
{
  "vendor": "Dell",
  "amount": "8200.00",
  "anomaly_type": "large_transaction",
  "ai_explanation": "This transaction is significantly higher than the vendor's typical payments and may require further review."
}
```

---

# Example Dataset

```
date,description,vendor,amount
2025-01-01,Office Supplies,Staples,120
2025-01-05,Consulting Fee,ABC Consulting,1500
2025-01-10,Consulting Fee,ABC Consulting,1500
2025-01-15,Equipment,Dell,8200
2025-01-20,Software License,Microsoft,300
```

---

# Technology Stack

* Python
* FastAPI
* Pandas
* Uvicorn
* OpenAI API
* python-dotenv

---

# Development Status

This project is an **early MVP exploring AI-assisted accounting analysis**.

Planned improvements include:

* Vendor spending anomaly detection
* Time-based financial behavior analysis
* Batch AI explanations
* PostgreSQL persistence
* MCP-compatible tool schemas
* Simple analytics dashboard

---

# License

MIT License

---

# Author

Edu
Senior Python Developer
