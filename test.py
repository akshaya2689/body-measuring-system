import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, \
    QGroupBox, QGridLayout, QLabel, QScrollArea
from typing import List

class AccountWidget(QWidget):
    def __init__(self, data: dict, parent=None):
        super().__init__(parent)
        self.group_box_layout = QGridLayout()
        for i, (key, value) in enumerate(data.items()):
            self.group_box_layout.addWidget(QLabel(key), i+1, 1)
            self.group_box_layout.addWidget(QLabel(value), i+1, 2)
        self.group_box = QGroupBox()
        self.group_box.setLayout(self.group_box_layout)
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.group_box)
        self.setLayout(self.main_layout)

class AccountListWidget(QWidget):
    def __init__(self, data: List[dict], parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout()
        for account_data in data:
            self.main_layout.addWidget(AccountWidget(account_data))
        self.setLayout(self.main_layout)

class MainWidget(QWidget):
    def __init__(self, data: List[dict], parent=None):
        super().__init__(parent)




        self.account_list_widget = AccountListWidget(data)
        self.account_list_widget.move(200,200)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.account_list_widget)
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.scroll_area)
        self.setLayout(self.main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    data = [{"created":"2019","balance":"100","deposits":"50","type":"Chq"},
            {"created":"2020","balance":"80","deposits":"45","type":"Chq"},
            {"created":"2020","balance":"70","deposits":"55","type":"Sav"}]
    mainWidget = MainWidget(data)
    mainWindow = QMainWindow()
    mainWindow.setCentralWidget(mainWidget)
    mainWindow.setWindowTitle("Demo App")
    mainWindow.resize(300, 300)
    mainWindow.show()
    app.exec()