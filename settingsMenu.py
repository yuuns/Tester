from PyQt5.QtWidgets import QMessageBox,QInputDialog
from numpy import true_divide
import jsonhandler


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
    text, ok = QInputDialog.getText(self, 'Kayıt Adı girin', 'Kayıt Adı')
    if ok:
        jsonhandler.saveJson(text,data,"./settings.json")
        return True


    