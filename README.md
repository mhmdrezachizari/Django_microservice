# 🚀 Django Microservices with Docker

A simple microservices project using **Django**, **PostgreSQL**, **RabbitMQ**, and **Docker Compose**.

---

## 🧩 Architecture

# Microservices Docker Setup

A simple Docker Compose setup with two Django services, PostgreSQL databases, RabbitMQ, and a product worker.

## Services

- **User Service**: `http://localhost:8000`
- **Product Service**: `http://localhost:8001`
- **User DB**: PostgreSQL on port `5433`
- **Product DB**: PostgreSQL on port `5434`
- **RabbitMQ**
  - AMQP: `5672`
  - Management UI: `http://localhost:15672`
  - Username: `admin`
  - Password: `admin`

## Requirements

- Docker
- Docker Compose

## Run
```bash
docker compose up --build

## Stop

bash
docker compose down

## Remove volumes

bash
docker compose down -v

## Notes

- Migrations run automatically when services start.
- Databases use persistent Docker volumes.

