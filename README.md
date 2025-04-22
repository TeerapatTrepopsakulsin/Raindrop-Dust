# Raindrop-Dust 🌧️💨

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0-green)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.22.0-red)](https://streamlit.io/)
[![MicroPython](https://img.shields.io/badge/MicroPython-1.19-yellow)](https://micropython.org/)
[![Node-RED](https://img.shields.io/badge/Node--RED-3.0.2-orange)](https://nodered.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

## Overview

Raindrop-Dust is an environmental monitoring system that explores the connection between PM 2.5 particulate matter and various environmental variables such as temperature, light intensity, humidity, and weather conditions. The project leverages IoT devices, data analytics, and machine learning to provide insights into patterns affecting PM 2.5 levels and predict future air quality.

## Collaborators and Affiliations
| Name             | Department          | Faculty             | University                  |
|------------------|---------------------|---------------------|-----------------------------|
| Teerapat Trepopsakulsin    | Software and Knowledge Engineering    | Engineering  | Kasetsart University       |
| Pattharamon Dumrongkittikule| Software and Knowledge Engineering    | Engineering  | Kasetsart University       |

## Key Features

- **Real-time data monitoring** using sensors and MQTT
- **Predictive modeling** for future AQI & PM levels
- **Data Sharing API** for user to call API
- **Interactive visualization dashboard** for data exploration
- **Environmental data correlation** with temperature, humidity, and light intensity

## Project Structure

```
raindrop-dust/
├── backend/              # FastAPI backend
│   ├── main.py           # Main backend application
│   ├── routes/           # API endpoints
│   ├── crud.py           # Database operation and query
│   ├── database.py       # Database connection
│   ├── models.py         # Data models
│   ├── predictor.py      # SVR models
│   ├── schemas.py        # Response model schemas
│   └── utils.py          # Helper functions
├── frontend/             # Streamlit frontend
│   ├── app.py            # Main frontend application
│   ├── components/       # UI components
│   ├── pages/            # Pages of dashboard
│   └── utils/            # Frontend utilities
├── static/               # Documentation
├── .env                  # Environment variables
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Data Acquisition an Integration Flow

```
Sensors (MicroPython) → MQTT → Node-RED → Database
```
```
Weather API → MQTT → Node-RED → Database
```
```
Primary+Secondary → hourly → Database
```
```
Database → FastAPI → Streamlit Dashboard
```

### 1. Data Collection

The project uses KidBright with attached sensors to collect PM and environmental Primary data, and Weather API to collect weather Secondary data:

- **PM 2.5 Particulate Matter**: Using PMS7003 sensors
- **Temperature & Humidity**: Using DHT22 sensors
- **Light Intensity**: Using Kidbrught
- **Weather Conditions**: Call [OpenWeather API](https://openweathermap.org/current)

#### MicroPython Code
See [the code](static/micropython.py)

#### Weather API Call
See [OpenWeather API Call](https://openweathermap.org/current)

### 2. Data Insertion with Node-RED

See Node-Red JSON of [Primary data](static/node-red_raindropdust) and [Secondary data](static/node-red_openweather)

Overall flow: connect MQTT input → JSON parsing → Insert statement → Database storage

### 3. Backend Data Sharing API (FastAPI)

The backend provides RESTful API endpoints for data sharing and analytics


### 4. Frontend Dashboard (Streamlit)

The Streamlit dashboard visualizes the data and provides interactive analytics

## Installation and Setup

### Prerequisites

- Python 3.8+

### Installation

See [the Installation Guide](https://github.com/TeerapatTrepopsakulsin/Raindrop-Dust/wiki/Installation)

## How to Run
1. Activate the virtual environment:
> On Windows:
```bash
venv\Scripts\activate
```
> On macOS/Linux:
```bash
source venv/bin/activate
```
2. Start the backend and frontend server:
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload --workers 1
```
```bash
streamlit run frontend/app.py
```
3. Access the web application

Access the API at:
```
http://localhost:8000/
```

**Swagger UI Documentation**:
```
http://localhost:8000/docs
```

Access the dashboard at:
```
http://localhost:8501/
```

## Data Analysis

The project analyses relationships between PM 2.5 levels and environmental factors:

- **Predictive Models**: Using SVR model to forecast future AQI, PM 2.5, and PM 10 levels

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [Streamlit](https://streamlit.io/) for the frontend framework
- [MicroPython](https://micropython.org/) for sensor programming
- [Node-RED](https://nodered.org/) for flow-based programming
