# TODO
from PyQt5 import Qt
from PyQt5.QtCore import pyqtSignal, QByteArray
from PyQt5.QtWidgets import QWidget, QListWidget, QPushButton, QListView, QLayout, QVBoxLayout
from PyQt5.QtSql import QSqlTableModel, QSqlQueryModel
from PyQt5.QtGui import QPixmap, QImageReader, QImage, QFontDatabase, QFont
from logs.logger import Logger
from logic.databaseLogic import connectToDB, getInfo

# Fetches and prints results
conn = connectToDB("postgres")
results = getInfo(conn)
for tup in results:
    for item in tup:
        print(item)

class CurrentInventory(QWidget):
    pageChangeRequest = pyqtSignal(str)


