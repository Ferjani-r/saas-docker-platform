# 🐳 Docker Container Manager — Python SaaS Platform

## 📌 Overview

**Docker Container Manager** is a Python-based SaaS web application that provides a clean and professional web interface for managing Docker containers.

The platform allows users to create and manage **Nginx containers running a custom landing page**, while offering real-time operational visibility such as **status, uptime, logs, and direct service access**.

This project demonstrates strong knowledge of **backend development**, **Docker API integration**, and **DevOps best practices**.

---

## 🎯 Project Objectives

- Build a **SaaS-style web interface** for Docker container management
- Interact with Docker using the **Docker Engine API** (not shell commands)
- Replace the default Nginx page with a **custom professional landing page**
- Provide **container lifecycle management and observability**
- Follow **clean, modular, production-aware architecture**
- Run on **Linux-based systems only**

---

## 🧱 Architecture Overview

```text
User Browser
     │
     ▼
Flask Web Application (SaaS UI)
     │
     ▼
Docker Engine API
     │
     ▼
Nginx Containers (Custom HTML Page)
...

## Architectural Principles

    Separation of Concerns: Routes, services, and utilities are clearly separated

    API-Driven Design: Docker logic isolated in a service layer

    Security-Oriented: No shell execution and read-only volume mounts

## ✨ Features
## 🔧 Container Lifecycle Management

    Create Nginx containers

    Start containers

    Stop containers

    Restart containers

    Delete containers

## 📊 Observability & Monitoring

    Container status (Running / Stopped)

    Dynamic port mapping

    Container uptime calculated from Docker metadata

    Container logs viewer

    Automatic dashboard refresh

## 🌐 User Experience

    Clean Bootstrap-based dashboard

    Flash messages for success and error feedback

    Confirmation dialogs for destructive actions

    Open button to directly access Nginx containers

    Custom professional Nginx landing page

## 🗂️ Project Structure
```text
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
├── README.md
└── .gitignore
...

## 🧠 Technical Highlights
## 🐳 Docker Integration

    Uses Docker SDK for Python

    Communicates directly with Docker Engine API

    Dynamic port allocation

    Safe container lifecycle handling

## ⏱️ Uptime Calculation

    Derived from Docker StartedAt metadata

    Handles nanosecond timestamps safely

    Accurate across restarts

    Updated automatically via page refresh

## 🧩 Clean Backend Architecture

    Flask application factory pattern

    Blueprint-based routing

    Dedicated service layer for Docker operations

    Utility helpers for validation and time handling

## 🔐 Security Considerations

    Docker socket access limited to host

    No user input passed to shell

    No command execution inside containers

    Read-only HTML volume mounts

    Default Nginx page disabled

## ⚠️ Note: Authentication is not implemented (single-admin demo context).
## 🚀 Installation & Usage
## 1️⃣ Requirements

    Linux OS (Ubuntu, Debian, Rocky Linux, etc.)

    Docker installed and running

    Python 3.9+

## ⚠️ Docker on Windows is NOT supported
## 2️⃣ Clone Repository

- git clone https://github.com/Ferjani-r/saas-docker-platform.git
- cd saas-docker-platform

## 3️⃣ Create Virtual Environment

- python3 -m venv venv
- source venv/bin/activate

## 4️⃣ Install Dependencies

- pip install -r requirements.txt

## 5️⃣ Run Application (Development Mode)

- python app.py

Access the application at:
- http://<VM-IP>:5000

## 🧪 Example Workflow

    Create a container from the dashboard

    Container starts automatically

    Click Open to access the Nginx page

    View logs and uptime in real time

    Restart or stop the container

    Uptime updates accordingly

## 🏁 Conclusion

This project demonstrates:

    Backend engineering fundamentals

    Docker and DevOps operational thinking

    Clean and maintainable architecture

    Secure container management

    Professional documentation and UI design
