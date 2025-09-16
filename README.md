# Docker Frontend-Backend Project

This project demonstrates a containerized application with separate frontend and backend services using Docker. The frontend is built with Streamlit, and the backend uses MongoDB.

## Prerequisites

- Docker

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kpandit15/docker-frontend-backend.git
cd docker-frontend-backend
```

### 2. Start the containers

```bash
docker compose up --build -d
```

This command will build and start both the frontend and backend services in detached mode.

## Accessing the Services

### Frontend (Streamlit)

- Open your browser and navigate to: [http://localhost:8501](http://localhost:8501)

### MongoDB (Backend)

- MongoDB runs on port `27017`.
### MongoDB Express UI

- The project includes a Mongo Express UI service for easy MongoDB management.
- Access the Mongo Express UI at: [http://localhost:8081](http://localhost:8081)
- Alternatively, you can use [MongoDB Compass](https://www.mongodb.com/products/compass) or any MongoDB client.
- Connect to: `mongodb://admin:password@localhost:27017/`

**Database Login Credentials:**
- **Username:** `admin`
- **Password:** `pass`

## Stopping the Services

To stop the containers, run:

```bash
docker compose down
```

## License

This project is licensed under the MIT License.