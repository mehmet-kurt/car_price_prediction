# 🚗 Car Price Predictor (PySide6 & scikit-learn)

A desktop application designed to estimate used car prices based on user-provided vehicle features (brand, model year, engine size, mileage, transmission type, owner history, etc.). The predictive engine is powered by a **Random Forest Regressor** trained via **scikit-learn**, wrapped in a clean desktop interface built with **PySide6 (Qt for Python)**.

---

## ✨ Features

- **Intuitive Desktop GUI:** Native and responsive desktop interface built with PySide6.
- **Machine Learning Powered:** Regression predictions generated via an ensemble `RandomForestRegressor` pipeline.
- **One-Hot Encoding Compatibility:** Form input values are dynamically mapped into a one-hot encoded feature matrix aligned with the model's training columns.
- **Model Persistence:** Fast loading of pre-trained estimators and column schemas using `joblib`.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.10+
- **GUI Framework:** [PySide6](https://pypi.org/project/PySide6/)
- **Machine Learning:** [scikit-learn](https://scikit-learn.org/)
- **Data Handling:** [pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **Model Serialization:** [joblib](https://joblib.readthedocs.io/)

---

## 📁 Repository Structure

```text
.
├── car_price.py           # Main GUI application and prediction pipeline
├── car_price_model.pkl    # Serialized scikit-learn RandomForestRegressor model
├── car_columns.pkl        # Serialized feature column names list
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
```

### 2. Create and Activate a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python car_price.py
```

---

## 📋 Input Parameters Guide

To ensure reliable predictions, provide inputs matching the standard format expected by the model:

| Field | Type | Description | Example Values |
| :--- | :--- | :--- | :--- |
| **Brand** | Categorical | Manufacturer name | `Toyota`, `BMW`, `Hyundai`, `Ford`, `Maruti` |
| **Year** | Numeric | Year of manufacture | `2018` |
| **Engine** | Numeric | Engine displacement in cubic centimeters (CC) | `1498` |
| **KM Driven** | Numeric | Total distance driven | `65000` |
| **Fuel Type** | Categorical | Primary fuel type | `Diesel`, `Petrol`, `LPG`, `CNG` |
| **Transmission** | Categorical | Gearbox type | `Manual`, `Automatic` |
| **Owner Type** | Categorical | Vehicle ownership status | `First`, `Second`, `Third`, `Fourth & Above`, `Test Drive` |
| **Mileage** | Numeric | Fuel economy rating (km/ltr or km/kg) | `18.5` |
| **Seller Type** | Categorical | Seller category | `Individual`, `Dealer`, `Trustmark Dealer` |

---

## 🧠 Model Architecture

- **Algorithm:** `RandomForestRegressor(n_estimators=100, criterion='squared_error')`
- **Feature Space:** Approximately 43 columns incorporating continuous numeric indicators alongside one-hot encoded categorical indicators (brands, fuel variants, ownership brackets).
- **Inference Flow:** Inputs $\to$ Categorical matching & zero-filled template DataFrame $\to$ Model inference $\to$ Price display in GUI.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).