from PyQt6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hash Table")
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("Size of Hash Table"))
        self.table_size = QLineEdit()
        self.layout.addWidget(self.table_size)

        self.layout.addWidget(QLabel("Select Collision Resolution Technique"))
        self.probing_method = QComboBox()
        self.probing_method.addItems(["Linear Probing", "Quadratic Probing", "Double Hashing"])
        self.layout.addWidget(self.probing_method)

        self.create_button = QPushButton("Create")
        self.layout.addWidget(self.create_button)

        self.setLayout(self.layout)
