from PyQt5 import QtCore, QtGui, QtWidgets,QtWidgets
from ui_form import (Ui_mainWindow)
import sys



def init_loginMenu():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    
    USERNAME = StringVar()
    PASSWORD = StringVar()

