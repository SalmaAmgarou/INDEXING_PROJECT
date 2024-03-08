from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont  # Import QFont for font styling

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hash Table")
        self.layout = QVBoxLayout()

        # QLabel for "Size of Hash Table"
        label_size = QLabel("Size of Hash Table")
        label_size.setFont(QFont("Arial", 15))  # Set the font size to 14
        self.layout.addWidget(label_size)

        # QLineEdit for table size
        self.table_size = QLineEdit()
        self.table_size.setFont(QFont("Arial", 15))  # Set the font size to 12
        self.layout.addWidget(self.table_size)

        self.layout.addSpacing(20)

        # QLabel for "Select Collision Resolution Technique"
        label_method = QLabel("Select Collision Resolution Technique")
        label_method.setFont(QFont("Arial", 15))  # Set the font size to 14
        self.layout.addWidget(label_method)

        # QComboBox for collision resolution technique
        self.probing_method = QComboBox()
        self.probing_method.addItems(["Linear Probing", "Quadratic Probing", "Double Hashing"])
        self.probing_method.setFont(QFont("Arial", 15))  # Set the font size to 12
        self.layout.addWidget(self.probing_method)

        # Add some spacing between the combo box and the "Create" button
        self.layout.addSpacing(32)

        # QPushButton for "Create"
        self.create_button = QPushButton("Create")
        self.create_button.setFont(QFont("Arial", 15))  # Set the font size to 14
        self.layout.addWidget(self.create_button)

        self.setLayout(self.layout)

        # Apply style sheets to change colors
        self.setStyleSheet(
            "QWidget { background-color: lightblue; }"  # Set background color for the entire window
            "QLabel { color: navy; font-weight: bold; }"  # Set font color and style for QLabel
            "QLineEdit { background-color: white; color: navy; border: 2px solid navy; }"  # Set style for QLineEdit
            "QPushButton { background-color: navy; color: white; border: none; padding: 5px; }"  # Set style for QPushButton
            "QComboBox { background-color: white; color: navy; border: 2px solid navy; }"  # Set style for QComboBox
        )

        self.layout.addSpacing(45)

        # QLabel for "Indexing Method"
        label_method = QLabel("Indexing Method : ")
        label_method.setFont(QFont("Arial", 15))  # Set the font size to 14
        label_method.setStyleSheet("QLabel { color: #45a049; }")  # Set the font color
        self.layout.addWidget(label_method)
        self.layout.addSpacing(15)

        # QPushButton for B+ Tree
        self.b_plus_tree_button = QPushButton("B+ Tree")
        self.b_plus_tree_button.setFont(QFont("Arial", 15))
        self.layout.addWidget(self.b_plus_tree_button)

        # Apply different style for B+ Tree button
        self.b_plus_tree_button.setStyleSheet(
            "QPushButton { background-color: #4CAF50; color: white; border: none; padding: 5px; }"  # Set green color
            "QPushButton:hover { background-color: #45a049; }"  # Darker green on hover
        )
