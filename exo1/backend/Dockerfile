# On part sur une version légère de python
FROM python:3.9-slim

# On se place dans le dossier de travail
WORKDIR /app

# On copie les dépendances et on installe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie le code
COPY . .

# On lance l'app
CMD ["python", "app.py"]