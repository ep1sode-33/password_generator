import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QCheckBox
from PyQt5.QtCore import pyqtSlot
import string
import random

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Strong Password Generator')
        self.setGeometry(100, 100, 400, 300)
        self.setMinimumSize(400, 300)

        layout = QVBoxLayout()

        self.label = QLabel('Enter the desired password length (6-100):')
        self.lineEdit = QLineEdit(self)
        self.generateButton = QPushButton('Generate Password')
        self.configModeCheckbox = QCheckBox('Configuration File / Command Line Mode')
        self.resultText = QTextEdit(self)
        self.resultText.setReadOnly(True)

        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.configModeCheckbox)
        layout.addWidget(self.generateButton)
        layout.addWidget(self.resultText)

        self.setLayout(layout)

        self.generateButton.clicked.connect(self.on_generate)
        self.lineEdit.returnPressed.connect(self.on_generate)

    @pyqtSlot()
    def on_generate(self):
        input_text = self.lineEdit.text()
        if not input_text.isdigit() or not 6 <= int(input_text) <= 100:
            QMessageBox.warning(self, "Input Error", "Please enter a valid integer, length between 6 and 100.", QMessageBox.Ok, QMessageBox.Ok)
            return
        length = int(input_text)
        password = self.generate_password(length, self.configModeCheckbox.isChecked())
        self.resultText.setText(password)

    def generate_password(self, length, configMode):
        if configMode:
            # For configuration files, avoid characters that often require escaping
            characters = string.ascii_letters + string.digits + "-_"
        else:
            # Include all characters for command line use
            characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    ex.show()
    sys.exit(app.exec_())
