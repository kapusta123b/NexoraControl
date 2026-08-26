# NexoraControl

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Django](https://img.shields.io/badge/django-5.0-green.svg)
![PySide6](https://img.shields.io/badge/PySide6-GUI-41CD52.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-16-336791.svg)
![Docker](https://img.shields.io/badge/docker-supported-2496ED.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

NexoraControl is a distributed server monitoring and control system built with Django, Python, and PySide6.

## Components

### Backend
* Django REST Framework
* PostgreSQL
* Agent management
* Monitoring
* Command lifecycle

### Agent
* Python
* System monitoring
* Command execution
* Docker support
* systemd deployment

### Desktop
* PySide6
* Agent monitoring
* Command management
* REST API client
* Background processing

## Features
* Agent registration and authentication
* CPU and RAM monitoring
* Online / offline detection
* Remote command execution
* Docker and system commands
* Command validation
* Command result handling
* Agent recovery
* Automated Agent installation
* Docker Compose deployment

## System Architecture

```mermaid
sequenceDiagram
    autonumber

    participant GUI as Desktop Client
    participant API as Django API
    participant DB as PostgreSQL
    participant Agent as Nexora Agent

    Note over GUI,DB: Agent registration
    GUI->>API: POST /agents/
    API->>DB: Create Agent
    DB-->>API: Agent data
    API-->>GUI: Agent ID + token

    Note over Agent,DB: Monitoring
    loop Every 5 seconds
        Agent->>API: POST /agents/{id}/heartbeat/
        API->>DB: Update status and metrics
        DB-->>API: Updated state
        API-->>Agent: 200 OK
    end

    Note over GUI,Agent: Command execution
    GUI->>API: POST /agents/{id}/commands/
    API->>DB: Create pending command
    DB-->>API: Command created
    API-->>GUI: 201 Created

    loop Command polling
        Agent->>API: GET /agents/{id}/commands/pending
        API->>DB: Query pending commands
        DB-->>API: Pending commands
        API-->>Agent: Commands
    end

    Agent->>Agent: Validate command
    Agent->>Agent: Execute command
    Agent->>API: PATCH /agents/{id}/commands/results/
    API->>DB: Update command result
    DB-->>API: Updated command
    API-->>Agent: 200 OK

    GUI->>API: GET /agents/
    API->>DB: Query agents
    DB-->>API: Agent state
    API-->>GUI: Agents data
```

## Installation

### 1. Backend
Clone the repository on the server:

```bash
git clone [https://github.com/kapusta123b/NexoraControl.git](https://github.com/kapusta123b/NexoraControl.git)
cd NexoraControl
```

Configure the environment and start the backend:

```bash
docker compose up -d --build
```

Apply migrations:

```bash
docker compose exec web python manage.py migrate
```

### 2. Agent
On the VPS you want to monitor:

```bash
curl -fsSL [https://raw.githubusercontent.com/kapusta123b/NexoraControl/main/agent/install.sh](https://raw.githubusercontent.com/kapusta123b/NexoraControl/main/agent/install.sh) | sudo bash
```

The installer downloads the Agent, creates its virtual environment, installs dependencies, configures systemd, and starts the initial setup. During setup, provide the API URL and machine name. 

Check the Agent status:

```bash
sudo systemctl status nexora-agent
```

View logs:

```bash
sudo journalctl -u nexora-agent -f
```

### 3. Desktop
Run the Desktop Client:

```bash
cd desktop
python main.py
```

The Desktop Client connects to the Django API and provides monitoring and control of registered Agents.

## Project Structure

```text
NexoraControl/
├── agent/
├── backend/
├── desktop/
├── conf.d/
├── docker-compose.yml
└── README.md
```

## License
MIT
