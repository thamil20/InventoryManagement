import sys
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QApplication, QPushButton, QWidget, QVBoxLayout)



class MainMenu(QWidget):
    def __init__(self, addInventoryCallback):
        super().__init__()
        # Callbacks to go to all the pages via buttons
        self.addInventoryCallback = addInventoryCallback
        #self.currentInventoryCallback = currentInventoryCallback

        # Page setup
        self.setContentsMargins(40, 10, 40, 10)
        self.buttonFontSize = 25
        self.fixedButtonHeight = 65

        # Custom Font Setup
        #self.customFonts = ["../fonts/DancingScript-VariableFont_wght.ttf", ]
        #for font in self.customFonts:
        #    if QFontDatabase.addApplicationFont(font) == -1:
        #        print("Error")
        #    else:
        #        self.fonts = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(font))[0]
        #self.currentFont = self.fonts
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
        self.addInventory.clicked.connect(self.addInventoryCallback)
        #self.currentInventory.clicked.connect(self.currentInventoryCallback)
        #self.soldInventory.clicked.connect(self.soldInventoryCallback)
        #self.income.clicked.connect(self.incomeCallback)

        # Vertical Layout
        vbox = QVBoxLayout()
        for widget in self.widgets:
            vbox.addWidget(widget)
        self.setLayout(vbox)

####################################################################
    #################################
    # These will be moved to main.py#
    #################################
    def soldInventoryClicked(self):
        print("Clicked Sold Inventory")
        # TODO
        # Implement transferring from main page to Sold Inventory Page


    def incomeViewClicked(self):
        print("Clicked Income")
        # TODO
        # Implement transferring from main page to Income Page
####################################################################

def main():
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()