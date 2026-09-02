FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
COPY app/ ./app/

ADD https://secure.eicar.org/eicar.com /tmp/eicar.com

CMD ["python", "-m", "app.config"]
