from PyQt5 import QtCore, QtGui, QtWidgets,QtWidgets
from PyQt5.QtWidgets import QMessageBox,QLineEdit
from PyQt5.QtGui import QPixmap

from ui_form import Ui_mainWindow
import os
import loginMenu
import settingsMenu
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
    ui.settingsButton.setEnabled(1)
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
    ui.getButton.clicked.connect(lambda: getButton())
    ## List page event ###############################################################################

    ui.listBackButton.clicked.connect(lambda: goPage(ui.homePage))

    ## graph page event ##############################################################################
    ui.graphBackButton.clicked.connect(lambda: goPage(ui.homePage))




    ## Main Functions  ####################################################################################
    def goPage(page):
        print (str(page) + "    Gecildi")
        ui.stackedWidget.setCurrentWidget(page)

    def userStatus():
        status = loginMenu.login(MainWindow,ui.usernameText.text(),ui.userpasswordText.text())
        if status == QMessageBox.Ok:
            ui.settingsButton.setEnabled(1)
            ui.listButton.setEnabled(1)
            ui.graphButton.setEnabled(1)
            goPage(ui.homePage)

    def getButton():
        data = settingsMenu.popup(MainWindow)
        voltage = data[0]["voltage"]
        current = data[0]["current"]
        voltageDescription = data[0]["voltageDescription"]
        temp = data[0]["temp"]
        tempDescription = data[0]["tempDescription"]

        ui.voltageDescription1.setText(voltageDescription[0])
        ui.voltageDescription2.setText(voltageDescription[1])
        ui.voltageDescription3.setText(voltageDescription[2])
        ui.voltageDescription4.setText(voltageDescription[3])
        ui.voltageDescription5.setText(voltageDescription[4])
        ui.voltageDescription6.setText(voltageDescription[5])
        ui.voltageDescription7.setText(voltageDescription[6])
        ui.voltageDescription8.setText(voltageDescription[7])
        ui.voltageDescription9.setText(voltageDescription[8])
        ui.voltageDescription10.setText(voltageDescription[9])
        ui.voltageDescription11.setText(voltageDescription[10])
      
        ui.tempDescription1.setText(tempDescription[0])
        ui.tempDescription2.setText(tempDescription[1])
        ui.tempDescription3.setText(tempDescription[2])
        ui.tempDescription4.setText(tempDescription[3])
        ui.tempDescription5.setText(tempDescription[4])
        ui.tempDescription6.setText(tempDescription[5])
        ui.tempDescription7.setText(tempDescription[6])
        ui.tempDescription8.setText(tempDescription[7])
        ui.tempDescription9.setText(tempDescription[8])
        ui.tempDescription10.setText(tempDescription[9])
        ui.tempDescription11.setText(tempDescription[10])

        ui.voltageProbe1Cb.setChecked(voltage[0])
        ui.voltageProbe2Cb.setChecked(voltage[1])
        ui.voltageProbe3Cb.setChecked(voltage[2])
        ui.voltageProbe4Cb.setChecked(voltage[3])
        ui.voltageProbe5Cb.setChecked(voltage[4])
        ui.voltageProbe6Cb.setChecked(voltage[5])
        ui.voltageProbe7Cb.setChecked(voltage[6])
        ui.voltageProbe8Cb.setChecked(voltage[7])
        ui.voltageProbe9Cb.setChecked(voltage[8])
        ui.voltageProbe10Cb.setChecked(voltage[9])
        ui.voltageProbe11Cb.setChecked(voltage[10])
        
        ui.currentProbe1Cb.setChecked(current[0])
        ui.currentProbe2Cb.setChecked(current[1])
        ui.currentProbe3Cb.setChecked(current[2])
        ui.currentProbe4Cb.setChecked(current[3])
        ui.currentProbe5Cb.setChecked(current[4])
        ui.currentProbe6Cb.setChecked(current[5])
        ui.currentProbe7Cb.setChecked(current[6])
        ui.currentProbe8Cb.setChecked(current[7])
        ui.currentProbe9Cb.setChecked(current[8])
        ui.currentProbe10Cb.setChecked(current[9])
        ui.currentProbe11Cb.setChecked(current[10])

        ui.tempProbe1Cb.setChecked(temp[0])
        ui.tempProbe2Cb.setChecked(temp[1])
        ui.tempProbe3Cb.setChecked(temp[2])
        ui.tempProbe4Cb.setChecked(temp[3])
        ui.tempProbe5Cb.setChecked(temp[4])
        ui.tempProbe6Cb.setChecked(temp[5])
        ui.tempProbe7Cb.setChecked(temp[6])
        ui.tempProbe8Cb.setChecked(temp[7])
        ui.tempProbe9Cb.setChecked(temp[8])
        ui.tempProbe10Cb.setChecked(temp[9])
        ui.tempProbe11Cb.setChecked(temp[10])

       

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


