# 🌡️ Weather-Based Disease Predictor

A machine learning web application that predicts the most probable disease based on a user's symptoms and real-time weather conditions (temperature, humidity, wind speed) using the OpenWeather API and a trained Random Forest model.

![Disease Predictor UI](static/preview.png) <!-- Add a preview screenshot if available -->

---

## 📦 Dataset

**Source:** [Kaggle – Weather-Related Disease Prediction Dataset](https://www.kaggle.com/datasets/orvile/weather-related-disease-prediction-dataset)

### 📜 About the Dataset
This dataset combines patient symptoms and pre-existing conditions with daily local weather data (temperature, humidity, wind speed). It provides a valuable base for exploring how weather influences disease symptoms and spread. All personally identifiable information has been removed.

### 📊 Key Features:
- `Age`: Patient's age
- `Gender`: Encoded as `0` (Female) and `1` (Male)
- `Temperature (C)`: Daily average in Celsius 🌡️
- `Humidity`: Daily average in percentage 💧
- `Wind Speed (km/h)`: Daily average in km/h 🍃
- `Symptoms`: Binary (1 = Present, 0 = Absent), e.g., nausea, fever, fatigue
- `Pre-existing Conditions`: Binary indicators, e.g., asthma, diabetes, hypertension
- `Prognosis`: The disease label to predict (target variable)

---

## 🚀 Features

- ✅ Dynamic symptom selection and search
- ✅ Real-time weather integration via city input (OpenWeather API)
- ✅ Editable temperature, humidity, and wind speed fields
- ✅ Intelligent UI that displays selected symptoms
- ✅ Predicts the most likely disease using trained ML model
- ✅ Tailwind CSS + Bootstrap styled UI

---

## 🧠 Machine Learning Model

- **Model Type**: Random Forest Classifier
- **Trained on**: 5200 records
- **Features used**: 45 binary symptoms, weather data, age, gender
- **Target**: Prognosis (Disease)

Model files:
- `model/model.pkl`: Trained RandomForestClassifier
- `model/label_encoder.pkl`: Label encoder for disease names

---

## 🖥️ Tech Stack

- **Frontend**: HTML, Tailwind CSS, Bootstrap, JavaScript
- **Backend**: Python, Flask
- **ML Model**: Scikit-learn
- **Weather API**: OpenWeatherMap API
- **Deployment-ready**: Structure supports hosting on Render, Railway, or Vercel with Flask adapter.

---

## 📷 Screenshots

> _Add images of your UI flow here (form, prediction screen, etc.)_

---

## ⚙️ Installation

### 1. Clone this repository

```bash
git clone https://github.com/chethan722003/DiseasePredictor.git
cd DiseasePredictor
