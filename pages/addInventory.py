import sys
from email.policy import default

from PyQt5.QtGui import QIcon, QFont, QFontDatabase, QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
                             QPushButton, QLabel, QLineEdit,
                             QComboBox, QFileDialog, QSizePolicy, QPlainTextEdit)


class AddInventory(QWidget):
    def __init__(self, cancelCallback):
        super().__init__()
        self.cancelCallback = cancelCallback

        self.setContentsMargins(40, 10, 40, 10)
        self.buttonFontSize = 25
        self.fixedHeight = 65

        # Custom Font Setup
        # self.customFonts = ["../fonts/DancingScript-VariableFont_wght.ttf", ]
        # for font in self.customFonts:
        #    if QFontDatabase.addApplicationFont(font) == -1:
        #        print("Error")
        #    else:
        #        self.fonts = QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFont(font))[0]
        # self.currentFont = self.fonts
        self.currentFont = "Times"

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setContentsMargins(10, 10, 20, 20)

        self.itemName = QLineEdit("Please enter the name of the item", self)
        self.itemDescription = QPlainTextEdit("Please enter the description of the item", self)
        self.itemType = QComboBox(self)
        self.itemAge = QLineEdit("Please enter the age of the item", self)
        self.itemPurchasePrice = QLineEdit("Please enter the purchase price of the item", self)
        self.itemImageUpload = QPushButton("Upload Image(s)", self)
        self.showItemImage = QLabel(self)
        self.addItem = QPushButton("Add Item", self)
        self.cancel = QPushButton("Cancel", self)
        self.buttons = [self.itemImageUpload, self.addItem, self.cancel]
        self.widgets = [self.itemName, self.itemDescription, self.itemType,
                        self.itemAge, self.itemPurchasePrice, self.itemImageUpload,
                        self.showItemImage, self.addItem, self.cancel]
        self.itemTypes = ["Please select an item type",
                          "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        self.init()

    def init(self):
        # Set any differing policies for widgets
        for widget in self.widgets:
            self.grid.addWidget(widget)
            widget.setFont(QFont(self.currentFont, self.buttonFontSize))
            if widget == self.itemDescription:
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            elif widget == self.showItemImage:
                widget.setMinimumSize(125,125)
            else: widget.setMinimumSize(75, 75)

        # Set styles for buttons
        for button in self.buttons:
            button.setFont(QFont(self.currentFont, self.buttonFontSize, QFont.Bold))
            button.setStyleSheet("background-color: pink;")

        # Action taken when each button is pressed
        self.itemImageUpload.clicked.connect(self.itemImageClicked)
        # self.addItem.clicked.connect(self.addItemClicked)
        self.cancel.clicked.connect(self.cancelCallback)

        # Add all item types to the item types drop down menu
        for i in self.itemTypes:
            self.itemType.addItem(i)

    # Opens file dialog and allows user to select an image
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

    # Will hold the logic to store any added inventory in the database
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