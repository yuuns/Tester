from PyQt5.QtWidgets import QMessageBox,QInputDialog,QLineEdit,QDialog
from numpy import true_divide
import jsonhandler
from PyQt5 import QtCore

def popup(self):
    settings= jsonhandler.readJson("./settings.json","settings")
    name, ok = QInputDialog.getItem(self, "Kayıtlar", "Kayıt seçiniz",
                                    settings, editable=False)
    if ok:
        # print(settings[name])        
        return settings[name]
    else:
        return []
def savePopup(self,data):

    text, ok = opendialog(self)
    print(ok)

    if ok == QMessageBox.Ok:
        jsonhandler.saveJson(text,data,"./settings.json")
        print("kaydedildi")
        return True


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
        return [inp.textValue(),QMessageBox.Ok]
    else:
        print('cancel')
        return ["",QMessageBox.Cancel]
    inp.deleteLater()