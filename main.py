# PyQT5 Intro
import sys
from PyQt5.QtGui import QIcon, QFontDatabase, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QWidget, QVBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Manager")
        self.setWindowIcon(QIcon("assets/antique.png"))
        self.screen_width = QApplication.primaryScreen().availableGeometry().width()
        self.screen_height = QApplication.primaryScreen().availableGeometry().height()
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.buttonFontSize = 25
        self.fixedButtonHeight = 65
        # Custom Font Setup
        self.customFonts = ["fonts/DancingScript-VariableFont_wght.ttf",]
        for font in self.customFonts:
            if QFontDatabase.addApplicationFont(font) == -1: print("Error")
            else: self.fonts = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(font))
        self.currentFont = self.fonts[0]
        self.centralWidget = QWidget()
        self.mainMenu = QLabel("Main Menu", self)
        self.addInventory = QPushButton("Add Inventory", self)
        self.currentInventory = QPushButton("Current Inventory", self)
        self.soldInventory = QPushButton("Sold Inventory", self)
        self.incomeView = QPushButton("Income", self)
        self.buttons = [self.addInventory, self.currentInventory, self.soldInventory, self.incomeView]
        self.widgets = [self.mainMenu, self.addInventory, self.currentInventory, self.soldInventory, self.incomeView]
        self.init()

    def init(self):
        self.centralWidget.setContentsMargins(10, 10, 40, 40)
        self.setCentralWidget(self.centralWidget)
        self.mainMenu.setFont(QFont(self.currentFont, 60, QFont.ExtraBold))
        self.mainMenu.setAlignment(Qt.AlignHCenter)
        for button in self.buttons:
            button.setFont(QFont(self.currentFont, self.buttonFontSize, QFont.Bold))
            button.setStyleSheet("background-color: pink;")
        self.addInventory.clicked.connect(self.addInventoryClicked)
        self.currentInventory.clicked.connect(self.currentInventoryClicked)
        self.soldInventory.clicked.connect(self.soldInventoryClicked)
        self.incomeView.clicked.connect(self.incomeViewClicked)
        # Vertical Layout

        vbox = QVBoxLayout()
        for widget in self.widgets:
            vbox.addWidget(widget)
        self.centralWidget.setLayout(vbox)

    def addInventoryClicked(self):
        print("Clicked Add Inventory")

    def currentInventoryClicked(self):
        print("Clicked Current Inventory")

    def soldInventoryClicked(self):
        print("Clicked Sold Inventory")

    def incomeViewClicked(self):
        print("Clicked Income")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()