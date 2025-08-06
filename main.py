# PyQT5 Intro
import sys
from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QPushButton, QWidget, QVBoxLayout, QStackedWidget, QMessageBox)
from pages.currentInventory import CurrentInventory
from pages.mainMenu import MainMenu
from pages.addInventory import AddInventory
# from pages.currentInventory import CurrentInventory
#from pages.soldInventory import SoldInventory
#from pages.income import Income

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window Setup
        self.setWindowTitle("Inventory Manager")
        self.setWindowIcon(QIcon("assets/antique.png"))
        self.screen_width = QApplication.primaryScreen().availableGeometry().width()
        self.screen_height = QApplication.primaryScreen().availableGeometry().height()
        self.setGeometry(0, 0, self.screen_width, self.screen_height)

        # Custom Font Setup
        try:
            self.customFonts = ["fonts/DancingScript-VariableFont_wght.ttf", ]
            for font in self.customFonts:
                if QFontDatabase.addApplicationFont(font) == -1:
                    self.logger.debugLog("Font Failed To Load.")
                else:
                    self.fonts = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(font))
            self.currentFont = self.fonts[0]
        except Exception as e:
            self.currentFont = "Times"
            self.logger.debugLog(e)

        # Setup pagination
        self.mainMenu = MainMenu()
        self.addInventory = AddInventory()
        self.currentInventory = CurrentInventory()

        self.pages = {
            "mainMenu": self.mainMenu,
            "addInventory": self.addInventory,
            "currentInventory": self.currentInventory,
        }

        # Create the stack
        self.stackedWidget = QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        # Add all page widgets to the stack
        self.stackedWidget.addWidget(self.mainMenu) # index 0
        self.stackedWidget.addWidget(self.addInventory) # index 1
        self.stackedWidget.addWidget(self.currentInventory) # index 2
        # self.stackedWidget.addWidget(SoldInventory()) # index 3
        # self.stackedWidget.addWidget(Income()) # index 4
        self.mainMenu.pageChangeRequest.connect(self.changePage)
        self.addInventory.pageChangeRequest.connect(self.changePage)
        self.currentInventory.pageChangeRequest.connect(self.changePage)

        # Go to main menu index
        self.stackedWidget.setCurrentIndex(0)


    def changePage(self, pageName):
        if pageName in self.pages:
            self.stackedWidget.setCurrentWidget(self.pages[pageName])
        else: self.stackedWidget.setCurrentWidget(self.pages['mainMenu'])


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()