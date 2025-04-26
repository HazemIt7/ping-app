# Utiliser une image officielle Python
FROM python:3.9-slim


# Install ping utility
RUN apt-get update && apt-get install -y iputils-ping && apt-get clean

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port sur lequel Flask va tourner
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]
