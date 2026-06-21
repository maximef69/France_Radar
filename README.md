
# ✈️ Radar aérien Francais

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-Exporter-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-F46800?style=for-the-badge&logo=grafana&logoColor=white)

Ce projet est une preuve de concept (PoC) d'une architecture d'observabilité complète déployée sur un VPS Linux. 
Il s'agit d'un **Custom Exporter Prometheus** développé en Python, qui interroge l'API publique OpenSky Network pour extraire le trafic aérien en temps réel au-dessus de la France, et l'afficher sur un tableau de bord dynamique.

## 🏗️ Architecture Technique

L'ensemble du projet est conteneurisé et géré avec Docker Compose.

1. **Collecteur (Python) :** Script interrogeant l'API OpenSky toutes les 15 secondes.
2. **Exposition des Métriques :** Utilisation de `prometheus_client` pour formater les données au standard Cloud Native (ex: `flights_over_france_total 1018`).
3. **Time Series Database :** **Prometheus** configuré pour scraper le conteneur Python en réseau interne.
4. **Visualisation :** **Grafana** branché sur Prometheus pour l'affichage en temps réel.

## 🚀 La Stack Déployée

- **Langage :** Python 3.11 (requests, prometheus-client)
- **Conteneurisation :** Docker, Docker Compose
- **Supervision :** Prometheus, Grafana
- **Système (Serveur de Prod) :** Debian 12

## 📊 Tableau de bord (Grafana)

<img width="1554" height="541" alt="image" src="https://github.com/user-attachments/assets/f3ee8927-7d0e-4327-a6d2-d1e8e19a3bb9" />


## 🛠️ Comment lancer ce projet 

Grâce à Docker, le projet peut être déployé sur n'importe quelle machine en moins de 2 minutes.

1. Cloner le dépôt :
   ```bash
   git clone [https://github.com/maximef69/France_Radar.git](https://github.com/maximef69/France_Radar.git)
   cd France_Radar
