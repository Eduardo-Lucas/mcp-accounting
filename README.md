# MCP Accounting

An **AI-powered accounting anomaly detection platform** built with  
**FastAPI, PostgreSQL, React, Tailwind, and Docker**.

This project exposes financial analytics as **callable API tools (MCP-style)** and delivers a **full-stack user experience** with authentication and data ingestion.

---

# Overview

The system processes accounting transactions and provides:

- anomaly detection
- structured reporting
- AI-generated explanations

It combines:

- backend analytics engine
- AI enrichment layer
- authenticated frontend interface

---

# Features

## Backend

✔ Upload accounting datasets via API  
✔ Persistent storage using PostgreSQL  
✔ Detect unusually large transactions  
✔ Detect duplicate vendor payments  
✔ Generate anomaly reports  
✔ AI-generated explanations for anomalies  
✔ Modular architecture (API / services / data layers)  
✔ MCP-style tool endpoints for automation and AI agents  

---

## Frontend

✔ React + TypeScript UI  
✔ Tailwind CSS styling  
✔ Email/password authentication (JWT)  
✔ Protected routes (dashboard)  
✔ File upload interface (CSV ingestion)  

---

## Infrastructure

✔ Fully containerized (Docker + Docker Compose)  
✔ PostgreSQL with healthcheck  
✔ Backend startup synchronization (wait-for-db)  
✔ Reproducible local environment  

---

# Architecture

Frontend (React + Tailwind)  
↓  
FastAPI (API Layer)  
↓  
Service Layer (Business Logic)  
↓  
Data Layer (SQLAlchemy + PostgreSQL)  
↓  
AI Layer (OpenAI)  

---

# Project Structure

mcp-accounting  
│  
├── app/                # FastAPI backend  
├── frontend/           # React + Tailwind frontend  
├── data/  
├── scripts/  
├── Dockerfile  
├── docker-compose.yml  
├── requirements.txt  
├── README.md  
└── .env  

---

# Run with Docker (Recommended)

Start the full system:

```bash
docker compose up --build
```

---

## Services

- Frontend → http://localhost:5173  
- Backend → http://localhost:8000/docs  

---

# Authentication Flow

- Login with email + password  
- Backend returns JWT token  
- Token stored in frontend  
- All protected endpoints require authentication  

---

# API Endpoints

## Auth

POST /auth/login

---

## Upload Transactions

POST /upload-transactions

---

## Anomaly Detection

POST /tools/detect_large_expenses  
POST /tools/find_duplicate_payments  

---

## Reports

POST /report/anomalies  
POST /report/anomalies/explain  

---

# Example Workflow

Login  
→ Upload CSV  
→ Data stored in PostgreSQL  
→ Run anomaly detection  
→ Generate report  
→ AI explanation  

---

# Technology Stack

## Backend
- FastAPI  
- SQLAlchemy  
- PostgreSQL  
- Pandas  

## Frontend
- React  
- TypeScript  
- Tailwind CSS  

## AI
- OpenAI API  

## Infrastructure
- Docker  
- Docker Compose  

---

# Environment Variables

OPENAI_API_KEY=your_api_key_here  
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/postgres  
SECRET_KEY=your-secret-key  

---

# Development Status

This project has evolved into a **full-stack AI-powered financial analysis tool**.

### Recent Improvements

- React + Tailwind frontend  
- JWT authentication (email-based login)  
- Protected routes and dashboard structure  
- Improved Docker setup (healthcheck + wait-for-db)  
- Structured API + service + data layers  

---

### Planned Improvements

- Upload history per user  
- Anomaly dashboard (UI)  
- Background processing (Celery)  
- Role-based access control  
- Audit logging  
- Alembic migrations  

---

# Positioning

> **AI-powered financial audit assistant** focused on anomaly detection, explainability, and automation readiness.

---

# License

MIT License

---

# Author

Edu  
Senior Python Developer
