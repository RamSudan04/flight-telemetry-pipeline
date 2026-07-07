<img width="1916" height="879" alt="1 project Third" src="https://github.com/user-attachments/assets/ec1a69a3-b0d5-432c-bce7-8d9e27d3dda2" />
<img width="1920" height="871" alt="1 project second" src="https://github.com/user-attachments/assets/74f6eacd-14fc-43cd-9c4c-30d6ab4f1009" />
<img width="1914" height="879" alt="1 project one" src="https://github.com/user-attachments/assets/4e6e9e3b-9656-44d2-80ba-8cac62767687" />
<img width="1918" height="875" alt="1 project fourth" src="https://github.com/user-attachments/assets/61c380d3-eebd-485e-9d5c-63892f54a0e8" />
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
