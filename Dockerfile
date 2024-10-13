# backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ /app/

EXPOSE 5000

CMD ["python", "app.py"]
