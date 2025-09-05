FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN pip install uv

RUN uv pip install --no-cache-dir -r requirements.txt --system

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]