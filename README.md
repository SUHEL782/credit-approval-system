# Credit Approval System

A backend system for evaluating customer loan eligibility and managing loans.
Built using **Django, PostgreSQL, Docker**, and deployed on **AWS EC2**.

## Features

* Register a new customer
* Check loan eligibility based on credit score rules
* Create a loan for eligible customers
* View individual loan details
* View all loans for a specific customer

## Tech Stack

* Python
* Django REST Framework
* PostgreSQL
* Docker
* AWS EC2

## API Endpoints

| Method | Endpoint                        | Description             |
| ------ | ------------------------------- | ----------------------- |
| POST   | `/api/register`                 | Register a new customer |
| POST   | `/api/check-eligibility`        | Check loan eligibility  |
| POST   | `/api/create-loan`              | Create a loan           |
| GET    | `/api/view-loan/<loan_id>`      | View loan details       |
| GET    | `/api/view-loans/<customer_id>` | View customer loans     |

## Deployment

The application is containerized using Docker and deployed on AWS EC2.

Base URL:

http://51.20.154.217:8000/

## Author

Suhel Khan
