
from PyQt6.QtWidgets import *

from src.domain.utils import get_dictionary_key, get_dictionary_element


class TableWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hash Table")
        self.layout = QVBoxLayout()
        self.key_input = QLineEdit()
        self.element_input = QLineEdit()

        self.insert_button = QPushButton("Insert")
        self.search_button = QPushButton("Search")
        self.delete_button = QPushButton("Delete")
        self.available_button = QPushButton("Set Element Available")
        self.delete_available_button = QPushButton("Delete Elements Available")

        self.return_label = QLabel("Your hash table:")
        self.return_label.setStyleSheet("margin-top: 90px;")

        self.tableWidget = QTableWidget()

        self.set_up_layout()

    def create_table(self, list_):
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setRowCount(len(list_))
        self.tableWidget.setColumnCount(3)

        self.tableWidget.setHorizontalHeaderLabels(["Index", "Key", "Element"])

        for i, dictionary in enumerate(list_):
            self.tableWidget.setCellWidget(i, 0, QLabel(str(i)))
            self.tableWidget.setCellWidget(i, 1, QLabel(str(get_dictionary_key(dictionary))))
            self.tableWidget.setCellWidget(i, 2, QLabel(str(get_dictionary_element(dictionary))))

        self.tableWidget.horizontalHeader().setDisabled(True)
        self.tableWidget.horizontalHeader().setStyleSheet("color: black; background-color: gray")
        self.tableWidget.setStyleSheet("background-color: #DCDCDC; color: black;")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)

    def set_up_layout(self):
        self.setMinimumSize(1000, 500)

        self.return_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.return_label.setMaximumWidth(750)

        layout = QVBoxLayout()

        layout_aux_input = QHBoxLayout()
        label_key = QLabel("Key :")
        label_key.setStyleSheet("font-size: 18px;")  # Increase font size of label
        self.key_input.setPlaceholderText("Enter Key")  # Set placeholder text for key input
        self.key_input.setMinimumWidth(100)  # Set the minimum width
        self.key_input.setMaximumWidth(150)  # Set the maximum width
        self.key_input.setStyleSheet("font-size: 14px;")  # Increase font size of placeholder text
        layout_aux_input.addWidget(label_key)
        layout_aux_input.addWidget(self.key_input)
        label_element = QLabel("Element :")
        label_element.setStyleSheet("font-size: 18px;")  # Increase font size of label
        self.element_input.setPlaceholderText("Enter Element")  # Set placeholder text for element input
        self.key_input.setMinimumWidth(100)  # Set the minimum width
        self.key_input.setMaximumWidth(150)  # Set the maximum width
        self.element_input.setStyleSheet("font-size: 14px;")  # Increase font size of placeholder text
        layout_aux_input.addWidget(label_element)
        layout_aux_input.addWidget(self.element_input)
        layout_aux_input.setSpacing(30)  # Add spacing between buttons


        layout_aux_button = QHBoxLayout()
        layout_aux_button.addWidget(self.insert_button)
        layout_aux_button.addWidget(self.search_button)
        layout_aux_button.addWidget(self.delete_button)
        layout_aux_button.setSpacing(15)  # Add spacing between buttons

        layout_aux_available = QHBoxLayout()
        layout_aux_available.addWidget(self.available_button)
        layout_aux_available.addWidget(self.delete_available_button)
        layout_aux_available.setSpacing(10)  # Add spacing between buttons

        layout.addItem(layout_aux_input)
        layout.addItem(layout_aux_button)
        layout.addItem(layout_aux_available)
        layout.addWidget(self.return_label)
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)

        self.setStyleSheet("""
                    background-color: #f0f0f0;
                    color: #333;
                """)

        self.return_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #005a8d;")
        self.setMinimumSize(1200, 600)

        # Apply styles to buttons
        self.apply_button_styles(self.insert_button)
        self.apply_button_styles(self.search_button)
        self.apply_button_styles(self.delete_button)
        self.apply_button_styles(self.available_button)
        self.apply_button_styles(self.delete_available_button)

    def apply_button_styles(self, button):
        button.setStyleSheet("""
                    QPushButton {
                        background-color: navy;
                        color: white;
                        padding: 8px 16px;
                        border-radius: 4px;
                    }
                    QPushButton:hover {
                        background-color: #005a8d;
                    }
                    QPushButton:pressed {
                        background-color: #003e5f;
                    }
                """)


        # Set font
        font = button.font()
        font.setPointSize(12)
        button.setFont(font)

    def insert_button_clicked(self):
        key_text = self.key_input.text()
        element_text = self.element_input.text()

        if not key_text and not element_text:
            QMessageBox.warning(self, "Missing Fields", "Please enter both Key and Element.")
            return

        try:
            key = int(key_text)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer for Key.")
            return

        # Insert functionality here

    def search_button_clicked(self):
        key_text = self.key_input.text()

        if not key_text:
            QMessageBox.warning(self, "Missing Key", "Please enter the Key to search.")
            return

        try:
            key = int(key_text)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer for Key.")
            return

        # Search functionality here

    def delete_button_clicked(self):
        key_text = self.key_input.text()

        if not key_text:
            QMessageBox.warning(self, "Missing Key", "Please enter the Key to delete.")
            return

        try:
            key = int(key_text)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer for Key.")
            return

        # Delete functionality here

    def available_button_clicked(self):
        key_text = self.key_input.text()

        if not key_text:
            QMessageBox.warning(self, "Missing Key", "Please enter the Key to set as available.")
            return

        try:
            key = int(key_text)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer for Key.")
            return

        # Set available functionality here

    def delete_available_button_clicked(self):
        # Delete available functionality here
        pass