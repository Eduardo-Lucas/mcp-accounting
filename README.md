# MCP Accounting

A minimal **Model Context Protocol (MCP)-style accounting analysis API** built with **Python and FastAPI**.
This project demonstrates how an AI agent or external service can interact with accounting data through structured API tools to detect financial anomalies.

The current MVP focuses on **detecting unusually large transactions** from accounting datasets.

---

## Overview

This project provides a lightweight backend service that:

* Loads accounting transactions from a CSV file
* Detects unusually large transactions
* Detects potential duplicate payments
* Exposes the analysis through REST endpoints that can be used by:

  * AI agents
  * automation workflows
  * external applications

The API is designed to resemble **MCP-style tool endpoints**, which makes it suitable for integration with LLM-based agents.

---

## Current Features

* Transaction ingestion from CSV
* Anomaly detection based on statistical thresholds
* Duplicate payment detection
* REST API with FastAPI
* Interactive API documentation via Swagger
* Command-line testing using `curl` and `jq`

---

## Project Structure

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
│   │   └── anomaly_detection.py
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

## Installation

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

## Running the Server

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

OpenAPI schema:

```
http://127.0.0.1:8000/openapi.json
```

---

## Available Endpoints

### Health Check

```
GET /health
```

Example:

```
curl http://127.0.0.1:8000/health
```

---

### List Available Tools

```
GET /tools
```

Example:

```
curl http://127.0.0.1:8000/tools
```

---

### Detect Large Transactions

```
POST /tools/detect_large_expenses
```

Example:

```
curl -X POST http://127.0.0.1:8000/tools/detect_large_expenses | jq
```

Example response:

```
{
  "results": [
    {
      "date": "2025-01-15",
      "vendor": "Dell",
      "amount": 8200,
      "description": "Equipment",
      "threshold": 6860.00,
      "reason": "Transaction above 95th percentile of amounts"
    }
  ]
}
```

---

### Detect Duplicate Payments

```
POST /tools/find_duplicate_payments
```

Example:

```
curl -X POST http://127.0.0.1:8000/tools/find_duplicate_payments | jq
```

---

## Sample Dataset

Example `transactions.csv`:

```
date,description,vendor,amount
2025-01-01,Office Supplies,Staples,120
2025-01-05,Consulting Fee,ABC Consulting,1500
2025-01-10,Consulting Fee,ABC Consulting,1500
2025-01-15,Equipment,Dell,8200
2025-01-20,Software License,Microsoft,300
```

---

## Technology Stack

* Python
* FastAPI
* Pandas
* Uvicorn

Optional developer tools:

* `curl`
* `jq`

---

## Development Status

Current version is an **early MVP** focused on core accounting anomaly detection.

Planned improvements include:

* CSV upload endpoint
* AI-generated explanations for anomalies
* Vendor spending analysis
* PostgreSQL support
* MCP-compatible tool schema definitions
* Accounting reports API

---

## License

MIT License

---

## Author

Edu
Senior Python Developer
