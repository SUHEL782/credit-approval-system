# Credit Approval System

A backend system for evaluating customer loan eligibility and managing loans.  
Built using **Django, Django REST Framework, PostgreSQL, Docker**, and deployed on **AWS EC2**.

---

## Features

- Register a new customer
- Check loan eligibility based on credit score rules
- Create a loan for eligible customers
- View individual loan details
- View all loans for a specific customer
- Excel data ingestion using background tasks

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- AWS EC2
- Pandas

---

## API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| POST | `/api/register` | Register a new customer |
| POST | `/api/check-eligibility` | Check loan eligibility |
| POST | `/api/create-loan` | Create a loan |
| GET | `/api/view-loan/<loan_id>` | View loan details |
| GET | `/api/view-loans/<customer_id>` | View all loans of a customer |

---

## Live API

Base URL


http://51.20.154.217:8000


Example endpoints


http://51.20.154.217:8000/api/register

http://51.20.154.217:8000/api/check-eligibility

http://51.20.154.217:8000/api/create-loan

http://51.20.154.217:8000/api/view-loan/1

http://51.20.154.217:8000/api/view-loans/1


---

## Run Locally (Docker)

```bash
docker-compose up --build

The API will be available at:

http://localhost:8000
Author

Suhel Khan
AWS Certified Developer – Associate
