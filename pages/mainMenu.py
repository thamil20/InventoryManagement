import sys
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (QLabel, QApplication, QPushButton, QWidget, QVBoxLayout)
from logs.logger import Logger


class MainMenu(QWidget):
    pageChangeRequest = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # Page setup
        self.setContentsMargins(40, 10, 40, 10)
        self.buttonFontSize = 25
        self.fixedButtonHeight = 65
        self.logger = Logger(None)
        # Custom Font Setup
        try:
            self.customFonts = ["./fonts/DancingScript-VariableFont_wght.ttf", ]
            for font in self.customFonts:
                if QFontDatabase.addApplicationFont(font) == -1:
                    self.logger.infoLog("Custom font failed to load")
                else:
                    self.fonts = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(font))
            self.currentFont = self.fonts[0]
        except Exception as e:
            self.logger.debugLog(e)
            self.currentFont = "Times"

        # Widget Init
        self.mainMenu = QLabel("Main Menu", self)
        self.addInventory = QPushButton("Add Inventory", self)
        self.currentInventory = QPushButton("Current Inventory", self)
        self.soldInventory = QPushButton("Sold Inventory", self)
        self.incomeView = QPushButton("Income", self)
        self.buttons = [self.addInventory, self.currentInventory, self.soldInventory, self.incomeView]
        self.widgets = [self.mainMenu, self.addInventory, self.currentInventory, self.soldInventory, self.incomeView]

        # Setup UI
        self.init()


    def init(self):

        # Set font/alignment
        self.mainMenu.setFont(QFont(self.currentFont, 60, QFont.ExtraBold))
        self.mainMenu.setAlignment(Qt.AlignHCenter)

        # Set the background color of all buttons
        for button in self.buttons:
            button.setFont(QFont(self.currentFont, self.buttonFontSize, QFont.Bold))
            button.setStyleSheet("background-color: pink;")

        # Actions taken when each button is clicked (Callbacks)
        self.addInventory.clicked.connect(self.emitAddInventoryRequest)
        self.currentInventory.clicked.connect(self.emitCurrentInventoryRequest)
        #self.soldInventory.clicked.connect(self.soldInventoryCallback)
        #self.income.clicked.connect(self.incomeCallback)

        # Vertical Layout
        vbox = QVBoxLayout()
        for widget in self.widgets:
            vbox.addWidget(widget)
        self.setLayout(vbox)

    def emitAddInventoryRequest(self):
        self.pageChangeRequest.emit("addInventory")

    def emitCurrentInventoryRequest(self):
        self.pageChangeRequest.emit("currentInventory")

def main():
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()