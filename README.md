# Docker Frontend-Backend Project

This project demonstrates a containerized application with separate frontend and backend services using Docker.

## Prerequisites

- Docker
- Docker Compose


## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/kpandit15/docker-frontend-backend.git
```

2. Navigate to the project directory:
```bash
cd docker-frontend-backend
```

3. Start the containers:
```bash
docker-compose up
```

## Services

### Frontend
- Built with streamlit
- Runs on port 8501

### Backend
- Built with mongo-db]
- Runs on port 27017

## Development

To build and run the containers in development mode:
```bash
docker compose up --build
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License