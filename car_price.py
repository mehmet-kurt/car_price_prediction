import joblib
import pandas as pd
from PySide6.QtWidgets import QLabel, QMainWindow, QApplication, QVBoxLayout, QWidget, QPushButton, QLineEdit, QGridLayout, QMessageBox
from PySide6.QtCore import Qt

model = joblib.load('car_price_model.pkl')
columns = joblib.load('car_columns.pkl')

print('Successful')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Car Price Prediction")
        self.setGeometry(100, 100, 800, 600)
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #f0f0f0; padding: 0px; margin: 0px;")
        central_layout = QGridLayout(central_widget)

        label = QLabel('Enter the features of the car that you are interested in (Give the correct inputs for better results)')
        label.setStyleSheet("font-size: 22px; font-weight: bold; color: darkblue; margin-bottom: 0px; padding: 0px; min-height: 48px; max-height: 48px;")
        label.setAlignment(Qt.AlignCenter)

        self.line1 = QLineEdit()
        self.line1.setPlaceholderText("Enter car brand here... (e.g., Toyota, Honda)")
        self.line1.setStyleSheet("font-size: 14px; padding: 10px;")

        self.line2 = QLineEdit()
        self.line2.setPlaceholderText("Enter car year here... (YYYY)")
        self.line2.setStyleSheet("font-size: 14px; padding: 10px;")

        self.line3 = QLineEdit()
        self.line3.setPlaceholderText("Enter car engine size here... (in CC)")
        self.line3.setStyleSheet("font-size: 14px; padding: 10px;")

        self.line4 = QLineEdit()
        self.line4.setPlaceholderText("Enter car km driven here... (in km)")
        self.line4.setStyleSheet("font-size: 14px; padding: 10px;")

        self.line5 = QLineEdit()
        self.line5.setPlaceholderText("Enter car fuel type here... (Diesel, Petrol, LPG)")
        self.line5.setStyleSheet("font-size: 14px; padding: 10px;")

        self.line6 = QLineEdit()
        self.line6.setPlaceholderText("Enter car transmission here... (Manual, Automatic)")
        self.line6.setStyleSheet("font-size: 14px; padding: 10px;")

        self.line7 = QLineEdit()
        self.line7.setPlaceholderText("Enter car owner type here... (First, Second, Third, Fourth & Above, Test Drive)")
        self.line7.setStyleSheet("font-size: 14px; padding: 10px;")

        self.line8 = QLineEdit()
        self.line8.setPlaceholderText("Enter car mileage here... (km/ltr/kg)")
        self.line8.setStyleSheet("font-size: 14px; padding: 10px;")

        self.line9 = QLineEdit()
        self.line9.setPlaceholderText("Enter seller type here... (Individual, Dealer)")
        self.line9.setStyleSheet("font-size: 14px; padding: 10px;")

        button = QPushButton("Predict Price")
        button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;")
        button.clicked.connect(self.predict_price)

        central_layout.addWidget(label, 0, 1, 1, 3)
        central_layout.addWidget(self.line1,1,0,1,5)
        central_layout.addWidget(self.line2,2,0,1,5)
        central_layout.addWidget(self.line3,3,0,1,5)
        central_layout.addWidget(self.line4,4,0,1,5)
        central_layout.addWidget(self.line5,5,0,1,5)
        central_layout.addWidget(self.line6,6,0,1,5)
        central_layout.addWidget(self.line7,7,0,1,5)
        central_layout.addWidget(self.line8,8,0,1,5)
        central_layout.addWidget(self.line9,9,0,1,5)
        central_layout.addWidget(button,10,1,1,3)
        self.setCentralWidget(central_widget)

    def predict_price(self):
        # This method will be implemented to predict the price based on user input
        new_car = pd.DataFrame(0, index=[0], columns=columns)

        new_car['year'] = self.line2.text()
        new_car['mileage(km/ltr/kg)'] = self.line8.text()
        new_car['engine'] = self.line3.text()
        new_car['km_driven'] = self.line4.text()
        new_car['fuel_Diesel'] = self.line5.text().lower() == 'diesel'
        new_car['fuel_Petrol'] = self.line5.text().lower() == 'petrol'
        new_car['fuel_LPG'] = self.line5.text().lower() == 'lpg'
        new_car['transmission_Manual'] = self.line6.text().lower() == 'manual'
        new_car['owner_Second Owner'] = self.line7.text().lower() == 'second'
        new_car['owner_Third Owner'] = self.line7.text().lower() == 'third'
        new_car['owner_Fourth & Above Owner'] = self.line7.text().lower() == 'fourth & above'
        new_car['owner_Test Drive Car'] = self.line7.text().lower() == 'test drive'
        new_car['seller_type_Individual'] = self.line9.text().lower() == 'individual'
        new_car['seller_type_Trustmark Dealer'] = self.line9.text().lower() == 'dealer'

        brand = self.line1.text().lower()

    
        if f'brand_{brand.capitalize()}' in new_car.columns or f'brand_{brand.upper()}' in new_car.columns:
            if brand == 'bmw':
                brand = 'BMW'
            else:
                brand = brand.capitalize()
            new_car[f'brand_{brand}'] = 1
            predicted_price = model.predict(new_car)
            message_box = QMessageBox()
            message_box.setText(f'The predicted price of the car is: {predicted_price[0]}')
            message_box.exec()
        else:
            message_box = QMessageBox()
            message_box.setText(f"Brand '{brand}' not found in the current brands.")
            message_box.exec()


app = QApplication([])
window = MainWindow()

window.show()
app.exec()
