# 🐳 Docker Container Manager — Python SaaS Platform

## 📖 Description

**Docker Container Manager** is a Python-based SaaS web application that provides a clean and professional web interface for managing Docker containers.

The platform allows users to **create, start, stop, restart, delete containers**, inspect **container logs**, monitor **uptime**, and **open running Nginx services directly** from the dashboard.

Each container runs **Nginx with a fully customized landing page**, replacing the default Nginx configuration.

This project demonstrates **backend engineering**, **Docker Engine API integration**, and **DevOps operational awareness**.

---

## 🎯 Project Objectives

- Provide a **SaaS-style web interface** for Docker container management
- Use the **Docker Engine API** safely via Python
- Replace default Nginx pages with **custom professional content**
- Offer **operational visibility** (status, logs, uptime)
- Follow **clean and modular backend architecture**
- Run on **Linux-based systems only**

---

## 🧱 Architecture Overview


Browser
│
▼
Flask Web Interface (SaaS UI)
│
▼
Docker Engine API
│
▼
Nginx Containers (Custom Landing Page)



### Design Principles
- Clear separation between **routes**, **services**, and **utilities**
- Docker logic isolated in a dedicated service layer
- No shell execution inside containers
- Read-only volume mounts for Nginx HTML

---

## ✨ Features

### 🔧 Container Lifecycle Management
- Create Nginx containers
- Start containers
- Stop containers
- Restart containers (atomic operation)
- Delete containers

### 📊 Observability & Monitoring
- Container status (Running / Stopped)
- Dynamic port mapping
- Container uptime (calculated from Docker metadata)
- Container logs viewer
- Automatic dashboard refresh

### 🌐 User Experience
- Clean Bootstrap-based interface
- Flash messages for user feedback
- Direct **Open** button to access Nginx containers
- Confirmation dialogs for destructive actions
- Professional custom Nginx landing page

---

## 🗂️ Project Structure




saas-docker-platform/
├── app/
│ ├── init.py # Flask app factory
│ ├── routes.py # Application routes
│ ├── services/
│ │ └── docker_service.py
│ └── utils/
│ └── validators.py # Validation & uptime helpers
│
├── templates/
│ └── index.html # Web UI
├── static/
│ └── style.css
├── nginx/
│ └── index.html # Custom Nginx landing page
│
├── app.py # Application entry point
├── requirements.txt
└── README.md



---

## 🧠 Technical Highlights

### 🐳 Docker Integration
- Uses **Docker SDK for Python**
- Communicates directly with Docker Engine API
- Dynamic port assignment
- No default Nginx configuration exposed

### ⏱️ Uptime Calculation
- Based on Docker `StartedAt` metadata
- Handles nanosecond timestamps safely
- Accurate across restarts
- Automatically updated via dashboard refresh

### 🧩 Clean Architecture
- Flask application factory pattern
- Blueprint-based routing
- Service layer for Docker operations
- Utility helpers for validation and time handling

---

## 🔐 Security Considerations

- Docker socket access restricted to the host
- No command execution inside containers
- No user input passed to shell
- Read-only volume mounts for Nginx HTML
- Default Nginx page disabled

⚠️ **Note**: Authentication is not implemented (single-admin demo context).

---

## 🚀 Installation & Usage

### 1️⃣ Requirements

- Linux OS (Ubuntu, Debian, Rocky Linux, etc.)
- Docker installed and running
- Python 3.9 or higher

⚠️ **Docker on Windows is NOT supported**

---

### 2️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/saas-docker-platform.git
cd saas-docker-platform



### 3️⃣  Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

## 4️⃣  Install Dependencies

pip install -r requirements.txt



## 5️⃣  Run Application (Development Mode)

python app.py
