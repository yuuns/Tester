from PyQt5 import QtCore, QtGui, QtWidgets,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap

from ui_form import (Ui_mainWindow)
import os
import loginMenu
import sys
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"


def handleVisibleChanged():
    if not QtGui.QGuiApplication.inputMethod().isVisible():
        return
    for w in QtGui.QGuiApplication.allWindows():
        if w.metaObject().className() == "QtVirtualKeyboard::InputView":
            keyboard = w.findChild(QtCore.QObject, "keyboard")
            if keyboard is not None:
                r = w.geometry()
                r.moveTop(keyboard.property("y"))
                w.setMask(QtGui.QRegion(r))
                return


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)

    ## Set disable other menu before login
    ui.settingsButton.setEnabled(0)
    ui.listButton.setEnabled(0)
    ui.graphButton.setEnabled(0)


    ## Global Functions connections #########################################################################
    QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)


    ## Home Page event ###############################################################################
    ui.homeButton.clicked.connect(lambda: goPage(ui.homePage))
    ui.homeButton.setVisible(0)
    ui.userButton.clicked.connect(lambda: goPage(ui.loginPage))
    ui.settingsButton.clicked.connect(lambda: goPage(ui.settingPage))
    ui.listButton.clicked.connect(lambda: goPage(ui.listPage))
    ui.graphButton.clicked.connect(lambda: goPage(ui.graphPage))


    ## Login page event ##############################################################################
    ui.loginButton.clicked.connect(lambda: userStatus())


    # ui.newUserButton.clicked.connect(lambda: goPage(ui.homePage))
    ui.loginBackButton.clicked.connect(lambda: goPage(ui.homePage))

    ## Settings page event ###########################################################################
    ui.settingsBackButton.clicked.connect(lambda: goPage(ui.homePage))

    ## List page event ###############################################################################

    ui.listBackButton.clicked.connect(lambda: goPage(ui.homePage))

    ## graph page event ##############################################################################
    ui.graphBackButton.clicked.connect(lambda: goPage(ui.homePage))




    ## Main Functions  ####################################################################################
    def goPage(page):
        print (str(page) + "Gecildi")
        ui.stackedWidget.setCurrentWidget(page)

    def userStatus():
        status = loginMenu.login(MainWindow,ui.usernameText.text(),ui.userpasswordText.text())
        if status == QMessageBox.Ok:
            ui.settingsButton.setEnabled(1)
            ui.listButton.setEnabled(1)
            ui.graphButton.setEnabled(1)
            goPage(ui.homePage)



    ##################################################################################################

    pix = QPixmap(":/icons/svg/logo.jpg")
    item = QtWidgets.QGraphicsPixmapItem(pix)
    scene = QtWidgets.QGraphicsScene()
    scene.addItem(item)
    ui.logoQgraph.setScene(scene)

    MainWindow.showFullScreen() 
    #MainWindow.show() 
    sys.exit(app.exec_())


if __name__ == "__main__":
    os.system('export DISPLAY=:0.0') # for vscode ssh connection
    main()


