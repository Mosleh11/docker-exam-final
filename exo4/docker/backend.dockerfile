FROM python:3.9-slim
WORKDIR /app
# On installe le driver pour PostgreSQL (psycopg2)
RUN pip install flask flask-cors psycopg2-binary
COPY ../backend/src /app
CMD ["python", "app.py"]