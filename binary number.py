import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class DecimalToBinaryConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Decimal to Binary Converter")
        self.setGeometry(100, 100, 400, 200)

        self.decimal_label = QLabel("Enter your number")
        self.decimal_entry = QLineEdit()
        self.convert_button = QPushButton("Convert")
        self.binary_result_label = QLabel("")

        self.convert_button.clicked.connect(self.convert)

        layout = QVBoxLayout()
        layout.addWidget(self.decimal_label)
        layout.addWidget(self.decimal_entry)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.binary_result_label)

        self.setLayout(layout)

    def convert(self):
        decimal_number = self.decimal_entry.text()
        try:
            decimal_number = int(decimal_number)
            binary_number = bin(decimal_number)[2:]
            self.binary_result_label.setText(f"binary number :[{ binary_number}]\n  ")
        except ValueError:
            self.binary_result_label.setText("Please enter a valid decimal number.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DecimalToBinaryConverter()
    window.show()
    sys.exit(app.exec_())
