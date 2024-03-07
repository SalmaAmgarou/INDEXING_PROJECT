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
        layout_aux_input.addWidget(QLabel("Key:"))
        layout_aux_input.addWidget(self.key_input)
        layout_aux_input.addWidget(QLabel("Element:"))
        layout_aux_input.addWidget(self.element_input)

        layout_aux_button = QHBoxLayout()
        layout_aux_button.addWidget(self.insert_button)
        layout_aux_button.addWidget(self.search_button)
        layout_aux_button.addWidget(self.delete_button)

        layout_aux_available = QHBoxLayout()
        layout_aux_button.addWidget(self.available_button)
        layout_aux_button.addWidget(self.delete_available_button)

        layout.addItem(layout_aux_input)
        layout.addItem(layout_aux_button)
        layout.addItem(layout_aux_available)
        layout.addWidget(self.return_label)
        layout.addWidget(self.tableWidget)

        self.setLayout(layout)
