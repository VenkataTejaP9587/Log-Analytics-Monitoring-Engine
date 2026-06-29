# Log Analytics and Monitoring Engine

A Python-based log analytics platform with real-time ingestion, anomaly detection, and an interactive Streamlit dashboard.

## Features

- FastAPI backend for log ingestion and search
- Streamlit dashboard for visualization and alert monitoring
- SQLite storage with SQLAlchemy ORM
- Dask-based log parsing and processing
- WebSocket support for live dashboard updates
- Sample log ingestion simulator included

## Prerequisites

- Python 3.9+ (Python 3.11 recommended)
- `pip` package manager

## Installation

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install required packages:

```powershell
pip install dask[complete] fastapi uvicorn streamlit sqlalchemy pandas plotly pydeck requests
```

> If you use a different shell, adjust activation accordingly: `source .venv/bin/activate` on macOS/Linux.

## Run the application

The project includes a top-level launcher that starts the FastAPI backend and the Streamlit dashboard together.

```powershell
python main.py
```

Then open the Streamlit dashboard when it launches, or go to `http://localhost:8501`.

## Components

- `main.py` — orchestrates database setup and starts the backend + dashboard
- `backend/api_server.py` — FastAPI server with ingestion endpoint and WebSocket manager
- `dashboard/app.py` — Streamlit dashboard for log analytics, ingest, anomaly monitoring, and threat intelligence
- `backend/pipeline/processing.py` — parses CSV or raw web server logs into structured data using Dask
- `backend/simulate_stream.py` — sends sample log events to the ingestion API to simulate a live stream
- `backend/config/db_config.py` — SQLite database configuration
- `backend/schema/models.py` — SQLAlchemy data models

## Usage

### Start the app

```powershell
python main.py
```

### Simulate log ingestion

Run the simulator once the backend is available:

```powershell
python backend/simulate_stream.py
```

### Use the ingestion API directly

POST to:

```
http://localhost:8000/ingest/logs
```

Payload format:

```json
{
  "timestamp": "2026-04-22T08:15:00Z",
  "service": "auth",
  "level": "ERROR",
  "message": "User login failed"
}
```

### Search logs

GET:

```
http://localhost:8000/api/logs/search?query=error&limit=100
```

## Sample data

- `backend/sample_data/sample_logs.txt` — CSV-style sample log stream
- `backend/sample_data/generate_nginx.py` — generator for Nginx-style log data

## Notes

- The dashboard loads logs from SQLite and supports CSV or Nginx/Apache style log parsing.
- The backend automatically creates the database schema on start.
- If you want to work with Dask directly, explore `backend/config/dask_config.py` and `backend/pipeline/processing.py`.

## License

This project is released under the terms of the included `LICENCE` file.
