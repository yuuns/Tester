# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/emre.akgul/AppData/Local/Temp/formmeybOy.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1024, 600)
        mainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        mainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        mainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        mainWindow.setTabletTracking(True)
        self.stackedWidget = QtWidgets.QStackedWidget(mainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.userButton = QtWidgets.QPushButton(self.homePage)
        self.userButton.setGeometry(QtCore.QRect(0, 0, 512, 300))
        self.userButton.setMinimumSize(QtCore.QSize(512, 300))
        self.userButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.userButton.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background: rgb(15, 188, 249);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgb(75, 207, 250);\n"
"}")
        self.userButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userButton.setIcon(icon)
        self.userButton.setIconSize(QtCore.QSize(100, 100))
        self.userButton.setObjectName("userButton")
        self.graphButton = QtWidgets.QPushButton(self.homePage)
        self.graphButton.setGeometry(QtCore.QRect(512, 300, 512, 300))
        self.graphButton.setMinimumSize(QtCore.QSize(512, 300))
        self.graphButton.setMaximumSize(QtCore.QSize(512, 300))
        self.graphButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.graphButton.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background: rgb(128, 142, 155);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgb(210, 218, 226);\n"
"\n"
"}")
        self.graphButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/chart-histogram.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.graphButton.setIcon(icon1)
        self.graphButton.setIconSize(QtCore.QSize(100, 100))
        self.graphButton.setObjectName("graphButton")
        self.listButton = QtWidgets.QPushButton(self.homePage)
        self.listButton.setGeometry(QtCore.QRect(0, 300, 512, 300))
        self.listButton.setMinimumSize(QtCore.QSize(512, 300))
        self.listButton.setMaximumSize(QtCore.QSize(512, 300))
        self.listButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listButton.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background: rgb(255, 63, 52);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgb(255, 94, 87);\n"
"\n"
"}")
        self.listButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/document.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listButton.setIcon(icon2)
        self.listButton.setIconSize(QtCore.QSize(100, 100))
        self.listButton.setObjectName("listButton")
        self.settingsButton = QtWidgets.QPushButton(self.homePage)
        self.settingsButton.setGeometry(QtCore.QRect(512, 0, 512, 300))
        self.settingsButton.setMinimumSize(QtCore.QSize(512, 300))
        self.settingsButton.setMaximumSize(QtCore.QSize(512, 300))
        self.settingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.settingsButton.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background: rgb(0, 216, 214);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgb(52, 231, 228);\n"
"}")
        self.settingsButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon3)
        self.settingsButton.setIconSize(QtCore.QSize(100, 100))
        self.settingsButton.setObjectName("settingsButton")
        self.stackedWidget.addWidget(self.homePage)
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setStyleSheet("QWidget{\n"
"background: rgb(15, 188, 249);\n"
"}")
        self.loginPage.setObjectName("loginPage")
        self.usernameText = QtWidgets.QLineEdit(self.loginPage)
        self.usernameText.setGeometry(QtCore.QRect(312, 300, 400, 45))
        self.usernameText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.usernameText.setInputMask("")
        self.usernameText.setText("")
        self.usernameText.setFrame(False)
        self.usernameText.setObjectName("usernameText")
        self.userpasswordText = QtWidgets.QLineEdit(self.loginPage)
        self.userpasswordText.setGeometry(QtCore.QRect(312, 350, 400, 45))
        self.userpasswordText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userpasswordText.setFrame(False)
        self.userpasswordText.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.userpasswordText.setObjectName("userpasswordText")
        self.loginButton = QtWidgets.QPushButton(self.loginPage)
        self.loginButton.setGeometry(QtCore.QRect(312, 400, 195, 45))
        self.loginButton.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background: rgb(52, 231, 228);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgb(0, 216, 214);\n"
"}")
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")
        self.newUserButton = QtWidgets.QPushButton(self.loginPage)
        self.newUserButton.setGeometry(QtCore.QRect(517, 400, 195, 45))
        self.newUserButton.setStyleSheet("QPushButton {\n"
"border: none;\n"
"background: rgb(11, 232, 129);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: rgb(5, 196, 107);\n"
"}")
        self.newUserButton.setObjectName("newUserButton")
        self.logoQgraph = QtWidgets.QGraphicsView(self.loginPage)
        self.logoQgraph.setGeometry(QtCore.QRect(412, 75, 200, 200))
        self.logoQgraph.setStyleSheet("border: none;\n"
"")
        self.logoQgraph.setObjectName("logoQgraph")
        self.stackedWidget.addWidget(self.loginPage)
        self.settingPage = QtWidgets.QWidget()
        self.settingPage.setStyleSheet("\n"
"background: rgb(0, 216, 214);\n"
"\n"
"")
        self.settingPage.setObjectName("settingPage")
        self.stackedWidget.addWidget(self.settingPage)
        self.listPage = QtWidgets.QWidget()
        self.listPage.setStyleSheet("background: rgb(255, 63, 52);\n"
"")
        self.listPage.setObjectName("listPage")
        self.stackedWidget.addWidget(self.listPage)
        self.graphPage = QtWidgets.QWidget()
        self.graphPage.setStyleSheet("background: rgb(128, 142, 155);\n"
"")
        self.graphPage.setObjectName("graphPage")
        self.stackedWidget.addWidget(self.graphPage)
        self.homeButton = QtWidgets.QPushButton(mainWindow)
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.homeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon4)
        self.homeButton.setIconSize(QtCore.QSize(40, 40))
        self.homeButton.setFlat(True)
        self.homeButton.setObjectName("homeButton")

        self.retranslateUi(mainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Data Logger"))
        self.usernameText.setPlaceholderText(_translate("mainWindow", "Kullanıcı Adı"))
        self.userpasswordText.setPlaceholderText(_translate("mainWindow", "Şifre"))
        self.loginButton.setText(_translate("mainWindow", "Giriş"))
        self.newUserButton.setText(_translate("mainWindow", "Şifremi unuttum"))
import icon_rc
