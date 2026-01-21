# Projet Examen Docker Compose

**Auteur :** Mohammed MOSLEH


## Description
Ce dépôt contient les 4 exercices de l'examen Docker Compose. Chaque exercice est isolé dans son propre dossier et respecte les consignes d'orchestration et de structure.

## Structure du projet
Le projet est divisé en 4 dossiers :

* **Exo 1 : Architecture Simple**
    * Backend Flask (Port 5000) + Frontend Nginx (Port 3000).
    * Communication basique via API.

* **Exo 2 : Base de données & Volumes**
    * Ajout d'une base de données SQLite persistante.
    * Opérations CRUD (Create, Read, Update, Delete).
    * Règle Makefile `purge` pour nettoyer les données.

* **Exo 3 : Réseau Tor**
    * Le Backend passe par un proxy Tor (SOCKS5) pour contacter l'extérieur.
    * Récupération anonyme de profils utilisateurs via `randomuser.me`.

* **Exo 4 : Stack Complète (PostgreSQL)**
    * Architecture complexe avec Backend, Frontend, PostgreSQL et PgAdmin.
    * Configuration stricte via fichiers `.env` dans le dossier `docker/`.
    * Configuration automatique du serveur dans PgAdmin.

## Comment lancer les exercices

Chaque dossier contient un `Makefile` pour faciliter le lancement.

### Prérequis
* Docker & Docker Compose
* Make (optionnel, sinon utiliser `docker-compose up`)

### Commandes
Pour chaque exercice, aller dans le dossier correspondant (`cd exoX`) et utiliser :

* `make` ou `make all` : Lance l'exercice.
* `make clean` : Arrête les conteneurs.
* `make fclean` : Nettoie conteneurs et images.
* `make purge` (Exo 2) : Supprime le volume de données.
* `make purge_bdd` (Exo 4) : Supprime la base de données.
* `make purge_all` (Exo 4) : Réinitialisation totale.