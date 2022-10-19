from token import ENCODING
from PyQt5 import QtCore, QtGui, QtWidgets,QtWidgets
from PyQt5.QtWidgets import QMessageBox,QLineEdit,QCheckBox,QInputDialog
from PyQt5.QtGui import QPixmap

from ui_form import Ui_mainWindow
import os
import loginMenu
import settingsMenu
import sys

import dialogtest


os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
os.system('export DISPLAY=:0.0') # for vscode ssh connection


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
    MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)

    
    ## Set disable other menu before login
    ui.settingsButton.setEnabled(True)
    ui.listButton.setEnabled(False)
    ui.graphButton.setEnabled(False)


    ## Global Functions connections #########################################################################
    QtGui.QGuiApplication.inputMethod().visibleChanged.connect(handleVisibleChanged)


    ## Home Page event ###############################################################################
    ui.homeButton.clicked.connect(lambda: goPage(ui.homePage))
    ui.homeButton.setVisible(False)
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
    ui.intervalSlider.valueChanged.connect(lambda: ui.interval_lbl.setText(str(ui.intervalSlider.value())))
    ui.saveButton.clicked.connect(lambda: saveButton())
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
            ui.settingsButton.setEnabled(True)
            ui.listButton.setEnabled(True)
            ui.graphButton.setEnabled(True)
            goPage(ui.homePage)

    def getButton():
        data = settingsMenu.popup(MainWindow)
        if data == []:
            return 0
        else:
            dataDict = dict(data)
            voltage = dataDict["voltage"]
            current = dataDict["current"]
            voltageDescription = dataDict["voltageDescription"]
            temp = dataDict["temp"]
            tempDescription = dataDict["tempDescription"]
            time = dataDict["time"]
            def fill(self,data,type):
                if type == QLineEdit:
                    for i in range(self.count()-1):
                        self.itemAt(i+1).widget().setText(data[i])
                elif type == QCheckBox:
                    for i in range(self.count()-1):
                        self.itemAt(i+1).widget().setChecked(data[i]) 
                else: 
                    print("wrong type")
                    return False 

            fill(ui.voltageProbeLayout,voltage,QCheckBox)
            fill(ui.tempProbeLayout,temp,QCheckBox)
            fill(ui.voltageDescriptionLayout,voltageDescription,QLineEdit)
            fill(ui.currentProbeLayout,current,QCheckBox)
            fill(ui.tempDescriptionLayout,tempDescription,QLineEdit)
            ui.intervalSlider.setValue(time)

    def saveButton():
        def pull(self,type):
            data = list()
            if type == QLineEdit:
                for i in range(self.count()-1):
                    data.append(self.itemAt(i+1).widget().text())
            elif type == QCheckBox:
                for i in range(self.count()-1):
                    data.append(int(self.itemAt(i+1).widget().isChecked()))
            else: 
                print("wrong type")
            return data 
        data = dict()
        data["voltage"] = pull(ui.voltageProbeLayout,QCheckBox)
        data["current"] = pull(ui.currentProbeLayout,QCheckBox)
        data["voltageDescription"] = pull(ui.voltageDescriptionLayout,QLineEdit)
        data["temp"] = pull(ui.tempProbeLayout,QCheckBox)
        data["tempDescription"] = pull(ui.tempDescriptionLayout,QLineEdit)
        data["time"] = ui.intervalSlider.value()
        #dialogtest.opendialog(MainWindow)

        settingsMenu.savePopup(MainWindow,data)


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


