# MCP Accounting Platform

An **AI-powered accounting anomaly detection platform** built with **FastAPI, PostgreSQL, React, and OpenAI**, featuring a complete **production-ready authentication system**.

---

## 🚀 Overview

MCP Accounting is a full-stack system designed to:

* Ingest financial transaction data
* Detect anomalies (large transactions, duplicates)
* Generate AI-powered explanations
* Expose functionality as **MCP-style callable APIs**

---

## 🧱 Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Passlib (bcrypt)
* JWT (authentication)
* Docker

### Frontend

* React (TypeScript)
* Tailwind CSS

### AI Layer

* OpenAI API (explanations)

---

## 🔐 Authentication System (Production-Ready)

### Features Implemented

* ✅ User registration
* ✅ Email verification (token-based)
* ✅ Secure password hashing (bcrypt)
* ✅ Login with JWT (stateless auth)
* ✅ Password reset flow
* ✅ Protected routes (JWT-ready)

---

### Auth Flow

#### Registration

1. User registers
2. User is created as **inactive/unverified**
3. Verification token generated (DB)
4. Email sent with verification link

#### Email Verification

* Token validated
* User marked as:

  * `is_active = True`
  * `is_verified = True`
* Token invalidated after use

#### Login

* Validates:

  * Email exists
  * Password matches (bcrypt)
  * User is verified
* Returns JWT:

```json
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```

#### Password Reset

1. Request reset
2. Token generated and emailed
3. User submits new password
4. Token invalidated

---

## 🏗️ Architecture

```
Frontend (React)
        ↓
FastAPI (API Layer)
        ↓
Service Layer (Business Logic)
        ↓
SQLAlchemy ORM
        ↓
PostgreSQL
        ↓
AI Layer (OpenAI)
```

---

## 🔄 Data Flow

```
Register → Verify Email → Login → Upload CSV
        ↓
Store Transactions → Detect Anomalies
        ↓
Generate Report → AI Explanation
```

---

## 🧩 API Endpoints

### Auth

* `POST /auth/register`
* `POST /auth/login`
* `GET /verify-email`
* `POST /forgot-password`
* `POST /reset-password`

### Core Features

* `POST /upload-transactions`
* `POST /tools/get_transactions`
* `POST /tools/detect_large_expenses`
* `POST /tools/find_duplicate_payments`
* `POST /report/anomalies`
* `POST /report/anomalies/explain`

---

## 🐳 Running with Docker

```bash
docker compose up --build
```

### Access:

* API Docs: http://localhost:8000/docs
* Frontend: http://localhost:3000

---

## ⚙️ Environment Variables

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/mcp_accounting
SECRET_KEY=your-secret-key
FRONTEND_URL=http://localhost:3000
```

---

## 🧠 Key Technical Decisions

### 1. Separation of Token Types

| Use Case           | Mechanism |
| ------------------ | --------- |
| Email verification | DB token  |
| Password reset     | DB token  |
| Authentication     | JWT       |

---

### 2. Security Practices

* Password hashing via bcrypt
* No plaintext password storage
* Token invalidation after use
* Generic login errors (no user enumeration)

---

### 3. SQLAlchemy Best Practices

* Single `Base` instance
* Proper model registration
* Dependency-injected DB sessions

---

### 4. Dockerized Environment

* Service-based networking (`db`)
* Environment-driven configuration
* Clean container rebuilds

---

## 🧪 Current Status

* ✅ End-to-end functional
* ✅ Authentication fully implemented
* ✅ Stable Docker environment
* ✅ Clean API contracts
* ✅ AI integration working

---

## 📌 Next Steps

* [ ] Alembic migrations (schema versioning)
* [ ] JWT-protected endpoints
* [ ] Role-based access control (RBAC)
* [ ] Background jobs (email queue)
* [ ] Token hashing (security hardening)
* [ ] Observability (logs + metrics)

---

## 💡 Project Purpose

This project demonstrates:

* Real-world backend architecture
* Secure authentication design
* AI integration into financial workflows
* MCP-style API exposure for automation

---

## 👨‍💻 Author

Developed as a **production-style backend system** to showcase:

* Python / FastAPI expertise
* System design & architecture
* Secure authentication flows
* AI-driven application design

---

## 📄 License

MIT License
