from matplotlib.backends.backend_qt5 import ConfigureSubplotsQt
import matplotlib.pyplot as plt;
from datetime import date
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from datetime import datetime;
from matplotlib.figure import Figure;
import yfinance as yf
import ploting
from config import config

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setWindowState(QtCore.Qt.WindowMaximized)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.widget = QtWidgets.QWidget(self.centralwidget)

        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 141, 571))
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 139, 600))

        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 141, 571))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 580, 141, 21))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setText("")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.clicked.connect(lambda: self.newStock())
        self.horizontalLayout.addWidget(self.pushButton)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(140, 0, 860, 601))
        self.canvasLayout = QtWidgets.QHBoxLayout(self.widget_2)

        self.label = QtWidgets.QLabel()
        self.label.setText("""Hallo und Willkommen zu Stock Visualizer.\n\nDu kannst hier Aktien anschauen. Links siehst du deine Aktien und unten kannst du welche hinzufügen.""")
        self.label.setFont(QFont('Arial', 10))

        self.canvasLayout.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)
    
        MainWindow.setWindowTitle("Stock Visualizer")
        self.pushButton.setText("Add Stock")
        self.init_stocks()
        MainWindow.show()
    def init_stocks(self):
        for stock in config.getstocks():
            self.btn = QtWidgets.QPushButton('{}'.format(stock), self.scrollAreaWidgetContents)
            text = self.btn.text()
            self.btn.clicked.connect(lambda ch, text=text : self.newStockView("{}".format(text)))
            self.verticalLayout.addWidget(self.btn)
            
    def createCanvas(self,sc):
        try:
            self.clearLayout(self.canvasLayout)
        except Exception as err:
            print(err)
        self.canvasLayout.addWidget(sc)

    def newStockView(self,stock):
        print(stock)
        ploting.ploting.createPlot(self,stock)

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def newStock(self):
        stock = self.lineEdit.text()
        config.addstock(stock)
        self.lineEdit.setText("")
        self.btn = QtWidgets.QPushButton('{}'.format(stock), self.scrollAreaWidgetContents)
        text = self.btn.text()
        self.btn.clicked.connect(lambda ch, text=text : self.newStockView("{}".format(text)))
        self.verticalLayout.addWidget(self.btn)
