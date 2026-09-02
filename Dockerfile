FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
COPY app/ ./app/
CMD ["python", "-m", "app.config"]
