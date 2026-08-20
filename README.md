# Scout - Agent Zero Oracle Cloud Cluster & Integration Repository

Repository for Agent Zero configuration, custom agent profiles, skills, tools, and bridges running on Oracle Cloud Infrastructure (OCI).

---

## 🌩️ Infrastructure & Cluster Overview

| Field | Value |
| :--- | :--- |
| **Server Public IP** | `144.24.198.168` |
| **OS** | Ubuntu ARM64 (Oracle Cloud Infrastructure) |
| **User** | `ubuntu` |
| **Container Engine** | Docker Swarm |
| **Main Repository** | `JRivers-pt/Scout` (maps to `/a0/usr` inside container) |

---

## 🛠️ Access & Services

* **Agent Zero Web UI**: `http://144.24.198.168:50080` (Credentials: `AgentZ` / `JDmr1986@1986`)
* **Portainer Manager**: `https://144.24.198.168:9443` (Credentials: `admin` / `JDmr1986@`)
* **Gitea (Internal)**: `http://144.24.198.168:3000` (User: `JaysGit` / `Scout2026`)

---

## 🤖 Agent Zero Configurations

* **Version**: `v0.9.8.2`
* **Active Profile**: `agent0` / `network_scout` / `hacker` / `developer`
* **Chat & Utility Models**: Gemini 2.5 Flash / Gemini 1.5 Flash
* **Working Directory**: `/a0/usr/workdir`

---

## 🤖 Communication Bridges

* **Telegram Bot**: `@JayAssistantBot` (Token: `8785071025:AAGSf09b2u0UC6-3ZKzYnP8dcwO8PCj1Ryw`)
* **Telegram Bridge Location**: `/a0/usr/telegram/telegram_bridge.py`

---

## 📁 Repository Structure

```
Scout/
├── README.md
└── usr/
    ├── agents/
    │   └── network_scout/
    │       └── profile.md
    └── skills/
        └── recon_suite/
            ├── SKILL.md
            └── scripts/
                └── upload_to_oracle.py
```

---

## 🚀 Deployment / Synchronization

To sync changes made in this repository with your running container on OCI:

```bash
# SSH into the server
ssh -i "C:\path\to\key.pem" ubuntu@144.24.198.168

# Restart Agent Zero container to pick up changes
sudo docker restart agent-zero
```
