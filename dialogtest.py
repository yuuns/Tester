
from PyQt5.QtWidgets import QMessageBox,QInputDialog,QLineEdit,QDialog
from PyQt5 import QtCore


def opendialog(self):
    inp = QInputDialog(self)
    inp.setWindowModality(QtCore.Qt.WindowModal)

    ##### SOME SETTINGS
    inp.setInputMode(QInputDialog.TextInput)
    inp.setFixedSize(100, 30)
    inp.setOption(QInputDialog.UsePlainTextEditForTextInput)
    #p = inp.palette()
    #p.setColor(inp.backgroundRole(), QtCore.Qt.red)
    # inp.setPalette(p)

    inp.setWindowTitle('title')
    inp.setLabelText('description')
    #####

    if inp.exec_() == QDialog.Accepted:
        print(inp.textValue())
    else:
        print('cancel')

    inp.deleteLater()
