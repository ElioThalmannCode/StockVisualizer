# Elio Thalmann
# Python Trading Trainer
# 18.05.2021

import sys
import display
from config import config

def main(): 
    config.initialize()
    app = display.QtWidgets.QApplication(sys.argv)
    Window = display.QtWidgets.QMainWindow()
    ui = display.Ui_MainWindow(Window)
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()