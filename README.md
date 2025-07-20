
# 🌐 MikroSDN

**MikroSDN** is an open-source Software-Defined Networking (SDN) platform designed to **manage, automate, and monitor MikroTik devices** (routers and switches running RouterOS) through a modern web interface.

---

## 🇬🇧 English Version

### 🎯 Objectives

- ✅ Centralized web UI for MikroTik routers and switches  
- ✅ Remote configuration using RouterOS API  
- ✅ Real-time monitoring (CPU, ports, uptime, etc.)  
- ✅ Reusable configuration templates  
- ✅ Change logging and auditing  
- ✅ Dockerized deployment with CI/CD pipelines

### 🧱 Project Architecture

```
MikroSDN/
├── controller/     → FastAPI backend (Python)
├── frontend/       → React + Tailwind CSS
├── db/             → PostgreSQL scripts & migrations
├── docs/           → Technical documentation
├── deploy/         → Docker & CI/CD configurations
└── README.md       → Project overview
```

### 🔌 Tech Stack

- FastAPI (Python)  
- PostgreSQL  
- React + Tailwind CSS  
- Docker & Docker Compose  
- GitHub Actions (CI/CD)  
- RouterOS API (port 8729)

### 🚀 Quickstart

```bash
git clone https://github.com/oti-genasis/mikrosdn.git
cd mikrosdn
docker-compose up --build
```

Access frontend at http://localhost:3000  
API available at http://localhost:8000/docs

### 🔐 MikroTik Requirements

- RouterOS enabled (not SwOS)  
- API port 8729 opened  
- User with `api`, `read`, `write` permissions

### 📜 License

MIT License

---

## 🇫🇷 Version Française

### 🎯 Objectifs

- ✅ Interface web centralisée pour routeurs et switches MikroTik  
- ✅ Configuration à distance via l’API RouterOS  
- ✅ Monitoring en temps réel (CPU, ports, uptime, etc.)  
- ✅ Modèles de configuration réutilisables  
- ✅ Journalisation des modifications  
- ✅ Déploiement Dockerisé avec pipelines CI/CD

### 🧱 Architecture du Projet

```
MikroSDN/
├── controller/     → Backend FastAPI (Python)
├── frontend/       → UI React + Tailwind CSS
├── db/             → Scripts SQL PostgreSQL
├── docs/           → Documentation technique
├── deploy/         → Docker & CI/CD
└── README.md       → Présentation du projet
```

### 🔌 Technologies utilisées

- FastAPI (Python)  
- PostgreSQL  
- React + Tailwind CSS  
- Docker & Docker Compose  
- GitHub Actions (CI/CD)  
- API RouterOS (port 8729)

### 🚀 Démarrage rapide

```bash
git clone https://github.com/votre-nom/mikrosdn.git
cd mikrosdn
docker-compose up --build
```

Interface disponible sur : http://localhost:3000  
API disponible sur : http://localhost:8000/docs

### 🔐 Prérequis MikroTik

- RouterOS activé (pas SwOS)  
- Port API 8729 ouvert  
- Utilisateur avec les permissions `api`, `read`, `write`

### 📜 Licence

Licence MIT