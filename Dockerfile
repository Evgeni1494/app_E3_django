# Utiliser une image de base Python 3.10
FROM python:3.10-slim as builder

# Définir le répertoire de travail
WORKDIR /app

# Installer les packages nécessaires pour la compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Utiliser pip pour installer les dépendances en deux étapes pour améliorer la réutilisation du cache
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

###################
# Stage de production
FROM python:3.10-slim

WORKDIR /app

# Copier les wheels compilés et les installer pour éviter de recompiler
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copier le reste de l'application
COPY . .

# Exposer le port utilisé par Streamlit
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
