import sys
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap
from PyQt5.QtCore import Qt, QByteArray, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
                             QPushButton, QLabel, QLineEdit,
                             QComboBox, QFileDialog, QSizePolicy, QPlainTextEdit)

from configs.databaseInfo import databaseName
from logs.logger import Logger
from logic.databaseLogic import modifyDB, connectToDB # getInfo


class AddInventory(QWidget):
    pageChangeRequest = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setContentsMargins(40, 10, 40, 10)
        self.buttonFontSize = 25
        self.fixedHeight = 65
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

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setContentsMargins(10, 10, 20, 20)

        self.itemName = QLineEdit("Please enter the name of the item", self)
        self.itemDescription = QPlainTextEdit("Please enter the description of the item", self)
        self.itemType = QComboBox(self)
        self.itemAge = QLineEdit("Please enter the age of the item", self)
        self.itemPrice = QLineEdit("Please enter the price of the item", self)
        self.itemImageUpload = QPushButton("Upload Image(s)", self)
        self.showItemImage = QLabel(self)
        self.addItem = QPushButton("Add Item", self)
        self.cancel = QPushButton("Cancel", self)
        self.selectedImagePath = None
        self.buttons = [self.itemImageUpload, self.addItem, self.cancel]
        self.widgets = [self.itemName, self.itemDescription, self.itemType,
                        self.itemAge, self.itemPrice, self.itemImageUpload,
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
        self.addItem.clicked.connect(self.addItemClicked)
        self.cancel.clicked.connect(self.emitMainMenuRequest)

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
            self.selectedImagePath = img
        else:
            self.showItemImage.setText("Could not load image.")
            self.selectedImagePath = None

    # Will hold the logic to store any added inventory in the database
    def addItemClicked(self):
        # Transform objects into text for the database.
        itemName = self.itemName.text()
        itemDescription = self.itemDescription.toPlainText()
        itemType = self.itemType.currentText()
        itemAge = self.itemAge.text()
        itemPrice = self.itemPrice.text()
        # Read image bytes to transform image
        imageBytes = None
        if hasattr(self, "selectedImagePath") and self.selectedImagePath:
            try:
                with open(self.selectedImagePath, 'rb') as img_file:
                    imageBytes = img_file.read()
                    imageBytes = QByteArray(imageBytes)
            except Exception as e:
                print("Image read error:", e)
                imageBytes = None
        else:
            print("No selected image.")

        try:
            con = connectToDB("postgres")
            modifyDB(con, itemName, itemDescription, itemType, itemAge, itemPrice, imageBytes)
            self.emitMainMenuRequest()
        except Exception as e:
            Logger.debugLog(self, e)

    def emitMainMenuRequest(self):
        self.pageChangeRequest.emit("mainMenu")

def main():
    app = QApplication(sys.argv)
    window = AddInventory()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()