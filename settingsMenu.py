from PyQt5.QtWidgets import QMessageBox,QInputDialog
from numpy import true_divide
import jsonhandler


def popup(self):
    settings= jsonhandler.readJson("./settings.json","settings")
    name, ok = QInputDialog.getItem(self, "Kayıtlar", "Kayıt seçiniz",
                                    settings, editable=False)
    if ok:
        print(settings[name])
        
        return settings[name]

    