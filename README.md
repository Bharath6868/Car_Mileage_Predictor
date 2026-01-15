# 🚗 Car Mileage Prediction System (City, Average & Highway)

🔗 Live App:
👉 https://car-mileage-predictor.streamlit.app/

A complete end-to-end **Machine Learning regression project** that predicts a car’s **City**, **Average**, and **Highway mileage (MPG)** based on user-provided vehicle specifications.

The project covers:
- Exploratory Data Analysis (EDA)
- Feature engineering
- Training multiple regression models
- Handling different feature spaces per target
- Production-ready deployment using **Streamlit**

---

## 📌 Problem Statement

Fuel efficiency is a critical factor for vehicle buyers and manufacturers.  
This project aims to predict:
- 🏙 **City Mileage**
- ⚖ **Average Mileage**
- 🛣 **Highway Mileage**

using vehicle attributes such as engine specifications, drivetrain, transmission type, and engineered features.

---

## 🧠 Key Highlights

- ✅ **Three independent regression models**
  - City mileage model
  - Average mileage model
  - Highway mileage model
- ✅ **Separate feature pipelines per model**
- ✅ **Backend feature engineering**
- ✅ **Robust inference without feature mismatch**
- ✅ **Interactive Streamlit web application**
- ✅ **Production-safe design (no data leakage)**

---

## 🧪 Feature Engineering

The following features are engineered dynamically during inference:

- **Car Volume**
# 🚗 Car Mileage Prediction System (City, Average & Highway)

A complete end-to-end **Machine Learning regression project** that predicts a car’s **City**, **Average**, and **Highway mileage (MPG)** based on user-provided vehicle specifications.

The project covers:
- Exploratory Data Analysis (EDA)
- Feature engineering
- Training multiple regression models
- Handling different feature spaces per target
- Production-ready deployment using **Streamlit**

---

## 📌 Problem Statement

Fuel efficiency is a critical factor for vehicle buyers and manufacturers.  
This project aims to predict:
- 🏙 **City Mileage**
- ⚖ **Average Mileage**
- 🛣 **Highway Mileage**

using vehicle attributes such as engine specifications, drivetrain, transmission type, and engineered features.

---

## 🧠 Key Highlights

- ✅ **Three independent regression models**
  - City mileage model
  - Average mileage model
  - Highway mileage model
- ✅ **Separate feature pipelines per model**
- ✅ **Backend feature engineering**
- ✅ **Robust inference without feature mismatch**
- ✅ **Interactive Streamlit web application**
- ✅ **Production-safe design (no data leakage)**

---

## 🧪 Feature Engineering

The following features are engineered dynamically during inference:

- **Car Volume**
# 🚗 Car Mileage Prediction System (City, Average & Highway)

A complete end-to-end **Machine Learning regression project** that predicts a car’s **City**, **Average**, and **Highway mileage (MPG)** based on user-provided vehicle specifications.

The project covers:
- Exploratory Data Analysis (EDA)
- Feature engineering
- Training multiple regression models
- Handling different feature spaces per target
- Production-ready deployment using **Streamlit**

---

## 📌 Problem Statement

Fuel efficiency is a critical factor for vehicle buyers and manufacturers.  
This project aims to predict:
- 🏙 **City Mileage**
- ⚖ **Average Mileage**
- 🛣 **Highway Mileage**

using vehicle attributes such as engine specifications, drivetrain, transmission type, and engineered features.

---

## 🧠 Key Highlights

- ✅ **Three independent regression models**
  - City mileage model
  - Average mileage model
  - Highway mileage model
- ✅ **Separate feature pipelines per model**
- ✅ **Backend feature engineering**
- ✅ **Robust inference without feature mismatch**
- ✅ **Interactive Streamlit web application**
- ✅ **Production-safe design (no data leakage)**

---

## 🧪 Feature Engineering

The following features are engineered dynamically during inference:

- **Car Volume**

- **Power Index**

These engineered features are calculated **only in the backend**, ensuring consistency with training.

---

## 📊 Input Features

### Numerical Inputs
- Engine displacement
- Cylinders
- Horsepower (HP)
- Torque
- Number of gears
- Car age
- Vehicle dimensions (length, width, height)

### Categorical Inputs (Dropdowns)
- Fuel type
- Transmission type
- Driveline style
- Car body type
- Market segment

All categorical inputs are converted to one-hot encoded features **internally**, aligned exactly with the training feature space.

---

## 🏗 Model Architecture

| Model Target | Feature Strategy |
|-------------|------------------|
| City MPG | Full feature set |
| Avg MPG | Selected feature subset |
| Highway MPG | Full feature set |

Each model uses its **own saved feature list**, ensuring:
- Correct feature order
- No missing columns
- No runtime errors

---

## 🛠 Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **Joblib / Pickle**
- **Git & GitHub**

---

## 🚀 Application Flow

1. User enters car specifications
2. Backend performs feature engineering
3. Model-specific feature pipeline is built
4. Predictions are generated for:
 - City MPG
 - Average MPG
 - Highway MPG
5. Results are displayed in a clean UI

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/Car_Mileage_Prediction.git
cd Car_Mileage_Prediction
pip install -r requirements.txt
streamlit run app.py
