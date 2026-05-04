# 🌦️ Weather Data Analytics API (FastAPI)

## 📌 Overview
This project is a **Weather Data Analytics API** built using **FastAPI**, designed to handle end-to-end weather data operations, including:

- 📥 Data ingestion (CSV upload)  
- 🔄 CRUD operations  
- 📊 Statistical analysis  
- 📈 Data visualization  
- 🌐 External API integration  

The system uses **Pandas & NumPy** for data processing and **Matplotlib** for generating visual insights.

---

## 🚀 Tech Stack

- **Backend:** FastAPI  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib  
- **API Integration:** Requests  
- **Data Storage:** CSV file  

---

## 📂 Project Structure

```
REVIEW-5/
│
├── routes/
│   ├── upload_routes.py
│   ├── weather_routes.py
│   ├── analysis.py
│   ├── visualisation.py
│
├── services/
│   ├── data_services.py
│   ├── api_services.py
│
├── weather_data.csv
├── weather_schemas.py
├── main.py
```

---

## ⚙️ How to Run

### 1️⃣ Install Dependencies
```bash
pip install fastapi uvicorn pandas matplotlib requests
```

### 2️⃣ Start Server
```bash
uvicorn main:app --reload
```

### 3️⃣ Open Swagger UI
```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

### 📥 1. Upload Dataset
**POST** `/api/upload`

Upload a CSV file containing weather data.

**Request:**
- Form Data → File (CSV)

**Response:**
```json
{
  "msg": "Uploaded successfully",
  "rows": 100
}
```

---

## 🌍 2. Weather CRUD Operations

### 🔹 Get All Records
**GET** `/api/weather`  
Returns all weather records.

### 🔹 Add Record
**POST** `/api/weather`

**Request Body:**
```json
{
  "date": "2024-01-01",
  "city": "Chennai",
  "temperature_c": 30,
  "humidity": 65,
  "wind_speed_kmph": 12,
  "rainfall_mm": 2
}
```

### 🔹 Update Record
**PUT** `/api/weather/{index}`  
Updates record at given index.

### 🔹 Delete Record
**DELETE** `/api/weather/{index}`  
Deletes record at given index.

---

## 🌐 3. External API Integration

**POST** `/api/weather/fetch/{city}`  

Fetches real-time weather data and appends it to dataset.

**Example:**
```
/api/weather/fetch/Delhi
```

---

## 📊 4. Data Analysis APIs

### 🔹 Average Temperature Per City  
**GET** `/api/analysis/avg-temp`

### 🔹 Max & Min Temperature  
**GET** `/api/analysis/max-min`

### 🔹 Total Rainfall  
**GET** `/api/analysis/rainfall`

### 🔹 Humidity Analysis  
**GET** `/api/analysis/humidity`

### 🔹 Moving Average & Summary  
**GET** `/api/analysis/moving_averages_and_stats_summary`

Includes:
- 7-day moving average  
- Mean, median, standard deviation  

---

## 📈 5. Data Visualization APIs

### 🔹 Temperature Trend  
**GET** `/api/temperature-trend`

### 🔹 Rainfall Comparison  
**GET** `/api/rainfall`

### 🔹 Humidity Distribution  
**GET** `/api/humidity`

---

## 📊 Dataset Format

Expected CSV structure:

```
date,city,temperature_c,humidity,wind_speed_kmph,rainfall_mm
```

---

## 🧠 Features

- ✅ Dynamic CSV upload  
- ✅ Data cleaning and normalization  
- ✅ Modular architecture (routes + services)  
- ✅ Real-time API integration  
- ✅ Statistical analysis endpoints  
- ✅ Visualization as image responses  
- ✅ Efficient data handling using caching  

---

## 📌 Key Highlights

- Uses **Pandas** for data manipulation  
- Uses **Matplotlib** for generating plots  
- Supports **real-time weather fetching**  
- Ensures **structured API design**  
- Fully compatible with **Swagger UI documentation**  

---

## ✅ Status

- ✔ Fully Functional  
- ✔ API Tested  
- ✔ Ready for Submission  
