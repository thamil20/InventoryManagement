import sys
from email.policy import default

from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
                             QPushButton, QLabel, QMainWindow,
                             QLineEdit, QComboBox, QFileDialog, QSizePolicy, QPlainTextEdit)

class AddInventory(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Manager")
        self.setWindowIcon(QIcon("assets/antique.png"))
        self.screen_width = QApplication.primaryScreen().availableGeometry().width()
        self.screen_height = QApplication.primaryScreen().availableGeometry().height()
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.buttonFontSize = 25
        self.fixedHeight = 65
        # Custom Font Setup
        self.customFonts = ["../fonts/DancingScript-VariableFont_wght.ttf",]
        for font in self.customFonts:
            if QFontDatabase.addApplicationFont(font) == -1: print("Error")
            else: self.fonts = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(font))
        self.currentFont = self.fonts[0]
        self.centralWidget = QWidget(self)
        self.grid = QGridLayout()
        self.itemName = QLineEdit("Please enter the name of the item", self)
        self.itemDescription = QPlainTextEdit("Please enter the description of the item", self)
        self.itemType = QComboBox(self)
        self.itemAge = QLineEdit("Please enter the age of the item", self)
        self.itemPurchasePrice = QLineEdit("Please enter the purchase price of the item", self)
        self.itemImageUpload = QPushButton("Upload Image(s)", self)
        self.showItemImage = QLabel(self)
        self.addInventoryButton = QPushButton("Add Item", self)
        self.buttons = [self.itemImageUpload, self.addInventoryButton]
        self.widgets = [self.itemName, self.itemDescription, self.itemType,
                        self.itemAge, self.itemPurchasePrice, self.itemImageUpload,
                        self.showItemImage, self.addInventoryButton]
        self.itemTypes = ["Please select an item type",
                          "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        self.init()

    def init(self):
        self.setCentralWidget(self.centralWidget)

        row_counter = 0
        for widget in self.widgets:
            self.grid.addWidget(widget, row_counter, 0)
            widget.setFont(QFont(self.currentFont, self.buttonFontSize))
            if widget == self.itemDescription:
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            else: widget.setMinimumSize(100, 100)
            row_counter += 1

        for button in self.buttons:
            button.setFont(QFont(self.currentFont, self.buttonFontSize, QFont.Bold))
            button.setStyleSheet("background-color: pink;")

        self.itemImageUpload.clicked.connect(self.itemImageClicked)
        self.centralWidget.setLayout(self.grid)
        self.grid.setContentsMargins(10, 10, 20, 20)

        for i in self.itemTypes:
            self.itemType.addItem(i)

    def itemImageClicked(self):
        img, _ = QFileDialog.getOpenFileName(self,
                                             "Open File",
                                             "C://",
                                             "Image files (*.jpg *.png *.jpeg)")

        if img:
            pixmap = QPixmap(img).scaled(128,128,Qt.KeepAspectRatio,Qt.SmoothTransformation)
            self.showItemImage.setPixmap(pixmap)
            #self.showItemImage.setScaledContents(True)
        else:
            self.showItemImage.setText("Could not load image.")

    def addItemClicked(self):
        # TODO
        # Complete the backend implementation for the Add Item button.
        pass


def main():
    app = QApplication(sys.argv)
    window = AddInventory()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()