import yfinance as yf
import matplotlib.pyplot as plt
import PyQt6 as pyqt
import display



class ploting:
    def createPlot(sel,stock_text):
        sc = display.MplCanvas(width=3, height=3, dpi=60)
        stock = stock_text.split(",")
        manystocks = yf.download(stock).Close
        sc.axes.plot(manystocks)
        sc.axes.set_xlabel("Zeit")
        sc.axes.set_ylabel("USD")
        sc.axes.set_title(stock_text)
        sc.axes.legend(stock)
        sel.createCanvas(sc)