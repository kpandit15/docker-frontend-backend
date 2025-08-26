# stremlit-app Project

## Prerequisites

- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/)
- (Optional) [Docker](https://www.docker.com/)

## Setup

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd fast-api
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

```bash
streamlit run app.py
```
- The API will be available at `http://127.0.0.1:8000`.

## Building with Docker

1. **Build the Docker image:**
    ```bash
    docker compose build
    ```

2. **Run the container:**
    ```bash
    docker compose up
    ```
3. **Tear down the docker images**
    ```
    docker compose down
    ```

## License

MIT  