# 🗃️ WhisperWave Persistence Microservice

This microservice is part of the **WhisperWave system** and is responsible for **persisting messages and user status** into a local **SQLite database**. It operates by consuming messages from RabbitMQ queues and processes them accordingly, following Clean Architecture principles.

---

## 📦 Project Overview

- **Language**: Python 3.11+
- **Package Manager**: [Poetry](https://python-poetry.org/)
- **Broker**: RabbitMQ
- **Database**: SQLite (via SQLAlchemy)
- **Architecture**: Clean Architecture (Entities, Use Cases, Interfaces)

---

## 🧰 Features

- ✅ Consumes messages from a RabbitMQ queue named `persistence`
- 🔁 Handles RPC-style requests via a `rpc_persistence` queue
- 💾 Stores messages and TTS (text-to-speech) status per user
- 🧵 Uses multi-threading to handle consumers concurrently
- 🧼 Clean separation between domain logic and infrastructure

---

## 📁 Directory Structure
- whisperwave
- ├── data/ # SQLAlchemy models and database config
- ├── domain/ # Domain entities (User, Message, etc.)
- ├── messaging/ # RabbitMQ consumers
- ├── usecases/ # Business logic / action dispatcher
- ├── main.py # Entry point for the microservice
- └── config.toml # Configuration file

---

## ⚙️ Configuration

Edit the `config.toml` file at the root of the project:

```toml
[rabbit]
host = "localhost"

[database]
engine = "sqlite:///persistence.db"
```

- host: The RabbitMQ server hostname or IP.
- engine: SQLAlchemy connection string for SQLite or any supported DB.
