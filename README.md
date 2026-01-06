# 🐳 Docker Container Manager — Python SaaS Platform

## 📌 Overview
**Docker Container Manager** is a Python-based SaaS web application that provides a clean and professional web interface for managing Docker containers. 

The platform allows users to create and manage **Nginx containers running a custom landing page**, while offering real-time operational visibility such as **status, uptime, logs, and direct service access**.

This project demonstrates strong knowledge of **backend development, Docker API integration, and DevOps best practices**.

---

## 🎯 Project Objectives
* Build a **SaaS-style web interface** for Docker container management.
* Interact with Docker using the **Docker Engine API** (not shell commands).
* Replace the default Nginx page with a **custom professional landing page**.
* Provide **container lifecycle management and observability**.
* Follow **clean, modular, production-aware architecture**.
* Run on **Linux-based systems only**.

---

## 🧱 Architecture Overview
* **User Browser** → **Flask Web Application** (SaaS UI)
* **Flask Web Application** → **Docker Engine API** (Python SDK)
* **Docker Engine API** → **Nginx Containers** (Custom HTML Page)

### Architectural Principles
* **Separation of Concerns:** Distinct layers for routes, services, and utilities.
* **API-Driven:** Docker logic is isolated in a dedicated service layer.
* **Security:** No direct shell execution; uses read-only volume mounts.

---

## ✨ Features

### 🔧 Container Lifecycle Management
* **Create:** Provision new Nginx containers instantly.
* **Control:** Start, Stop, and Restart containers from the UI.
* **Cleanup:** Delete containers and free up system resources.

### 📊 Observability & Monitoring
* **Live Status:** Real-time visibility (Running / Stopped).
* **Dynamic Mapping:** View assigned host ports for each container.
* **Uptime Tracking:** Precise uptime calculated from Docker metadata.
* **Logs Viewer:** Access container output for troubleshooting.

### 🌐 User Experience
* **Clean UI:** Responsive Bootstrap-based dashboard.
* **Direct Access:** "Open" button to jump straight to the container's web service.
* **Feedback:** Flash messages for success/error notifications.

---

## 🗂️ Project Structure

saas-docker-platform/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── services/
│   │   └── docker_service.py
│   └── utils/
│       └── validators.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── nginx/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md



## 🚀 Installation & Usage

### 1️⃣ Requirements

- Linux OS (Ubuntu, Debian, Rocky Linux, etc.)
- Docker installed and running
- Python 3.9 or higher

⚠️ **Docker on Windows is NOT supported**

---

### 2️⃣ Clone Repository

```bash
git clone https://github.com/Ferjani-r/saas-docker-platform.git
cd saas-docker-platform


### 3️⃣ Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

### 4️⃣ Install Dependencies

pip install -r requirements.txt

### 5️⃣ Run Application (Development Mode)

python app.py
