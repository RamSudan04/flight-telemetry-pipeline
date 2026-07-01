# Flight Telemetry Data Pipeline

An end-to-end data engineering pipeline designed to simulate, broker, store, and visualize real-time flight telemetry data. This project demonstrates the integration of message brokering and time-series data storage for live monitoring applications.

## 🏗️ Architecture & Tech Stack

This pipeline consists of four main components working seamlessly together:

1. **Data Generation (Python):** A producer script simulates real-time aircraft telemetry (Speed, Altitude, and Roll) and publishes it as JSON payloads.
2. **Message Broker (Apache ActiveMQ):** Receives the streaming data via the STOMP protocol, ensuring decoupled and reliable message delivery.
3. **Time-Series Database (InfluxDB):** A consumer script listens to the ActiveMQ queue and writes the structured data points into an InfluxDB bucket for highly efficient time-based querying.
4. **Data Visualization (Grafana):** Connects directly to InfluxDB using Flux queries to render live, updating dashboards of the flight metrics.

**Infrastructure:** The entire backend (ActiveMQ, InfluxDB, Grafana) is containerized and orchestrated using **Docker Compose**.

## 🚀 Features
* **Real-time Data Streaming:** Continuous data flow with synthetic flight metrics.
* **Asynchronous Processing:** Producer and consumer scripts operate independently through the ActiveMQ message queue.
* **Containerized Environment:** One-click infrastructure setup using `docker-compose.yml`.
* **Live Dashboards:** Grafana panels visualizing Speed, Altitude, and Roll over time.

## 🛠️ Setup and Installation

1. Start the Infrastructure: `docker compose up -d`
2. Install Python Dependencies: `pip install stomp.py influxdb-client`
3. Run `python flight_consumer.py` in one terminal.
4. Run `python flight_producer.py` in a second terminal.
5. Open `http://localhost:3000` to view the live dashboard.