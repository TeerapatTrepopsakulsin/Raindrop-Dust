# Raindrop-Dust
This project explores the connection between PM 2.5 and environmental variables like temperature, light intensity, humidity, and weather conditions. By analyzing these data, we provide insights into patterns affecting PM 2.5 levels and predict future levels using historical relationships.

# ENV
```
.env
```

## HOW TO RUN

### Backend
```
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload --workers 1
```
```
http://localhost:8000/
```
**Swagger UI**
```
http://localhost:8000/docs
```

### Frontend
```
streamlit run frontend/app.py
```
```
http://localhost:8501/
```

