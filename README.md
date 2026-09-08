# 🚗 Car Price Predictor (PySide6 & Machine Learning)

An end-to-end used car price estimation desktop application combining exploratory data analysis, machine learning model training, and a native graphical interface built with **PySide6 (Qt for Python)**.

The prediction engine is driven by a scikit-learn **Random Forest Regressor** trained on historical vehicle market data, achieving an **$R^2$ score of ~0.955** on unseen test data.

---

## ✨ Features

- **Native Desktop GUI:** Fast, responsive interface built with PySide6 for local inference without needing an active internet connection.
- **Machine Learning Powered:** High-precision regression predictions powered by an ensemble `RandomForestRegressor`.
- **Dynamic One-Hot Encoding:** User input values are automatically aligned with the 45-column feature matrix used during model training.
- **Model Persistence:** Instant inference startup leveraging serialized estimators and column metadata via `joblib`.
- **Comprehensive Pipeline:** Includes raw data ingestion, brand extraction, feature cleaning, model fitting, and evaluation inside an exploratory Jupyter notebook.

---

## 📁 Repository Structure

```text
.
├── car_data.csv          # Raw vehicle dataset (8,000+ entries)
├── car_price.ipynb       # Data exploration, feature engineering & model training
├── car_price.py          # PySide6 desktop application & inference engine
├── car_price_model.pkl   # Serialized RandomForestRegressor model
├── car_columns.pkl       # Serialized feature column matrix (45 columns)
├── requirements.txt      # Project dependencies
├── .gitignore            # Git exclusion rules (.DS_Store, venv, cache)
└── README.md             # Project documentation
```

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.10+
- **GUI Framework:** [PySide6](https://pypi.org/project/PySide6/) (Qt for Python)
- **Machine Learning:** [scikit-learn](https://scikit-learn.org/) (`RandomForestRegressor`, `train_test_split`, `metrics`)
- **Data Manipulation:** [pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **Model Serialization:** [joblib](https://joblib.readthedocs.io/)
- **Notebook Environment:** [Jupyter Notebook](https://jupyter.org/)

---

## 📊 Model Architecture & Performance

The predictive model was trained on the `car_data.csv` dataset containing 8,128 vehicle sales records:

- **Algorithm:** `RandomForestRegressor()`
- **Train / Test Split:** 80% training, 20% testing
- **Train $R^2$ Score:** $\approx 0.992$
- **Test $R^2$ Score:** $\approx 0.955$
- **Root Mean Squared Error (RMSE):** $\approx 161,974$

### Feature Importance (Top 5 Drivers)

The model identified the following parameters as having the highest relative influence on vehicle price:

1. **`transmission_Manual`**: ~35.5%
2. **`engine` (Displacement in CC)**: ~29.9%
3. **`year` (Manufacture Year)**: ~24.8%
4. **`mileage(km/ltr/kg)`**: ~3.0%
5. **`km_driven`**: ~2.7%

---

## ⚙️ Installation & Setup

### 1. Clone or Download the Repository

```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
```

### 2. Create and Activate a Virtual Environment (Recommended)

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Launch the desktop interface:
```bash
python car_price.py
```

To review the training pipeline or re-train the model, open the notebook:
```bash
jupyter notebook car_price.ipynb
```

---

## 📋 Input Parameters Guide

When using the desktop application, format your vehicle values as follows:

| Field | Type | Description | Example Values |
| :--- | :--- | :--- | :--- |
| **Brand** | Categorical | Manufacturer name | `Toyota`, `BMW`, `Hyundai`, `Ford`, `Maruti` |
| **Year** | Numeric | Year of manufacture | `2018` |
| **Engine** | Numeric | Engine displacement in cubic centimeters (CC) | `1498` |
| **KM Driven** | Numeric | Total distance driven in kilometers | `65000` |
| **Fuel Type** | Categorical | Fuel configuration | `Diesel`, `Petrol`, `LPG` |
| **Transmission** | Categorical | Gearbox type | `Manual`, `Automatic` |
| **Owner Type** | Categorical | Registered ownership history | `First`, `Second`, `Third`, `Fourth & Above`, `Test Drive` |
| **Mileage** | Numeric | Fuel economy rating (km/ltr or km/kg) | `19.4` |
| **Seller Type** | Categorical | Seller category | `Individual`, `Dealer`, `Trustmark Dealer` |

---

## 📄 License

This project is licensed under the MIT License - see below for details:

```text
MIT License

Copyright (c) 2026 Mehmet Kurt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```