from PyQt5.QtWidgets import QMessageBox
from numpy import true_divide
import jsonhandler


def init_loginMenu():
      print("")



def login(self,username,password):
    print(username)
    print(password)
    status = jsonhandler.Login("./users.json",username,password)
    print(status)
    if status == True:
        print("doğru şifre")
        reply = QMessageBox.information(self, 'Kullanıcı girişi', 'Giriş başarılı', QMessageBox.Ok)
        return reply
    else:
        reply = QMessageBox.warning(self, 'Kullanıcı girişi', 'Yalnış Kullanıcı adı veya şifre', QMessageBox.Ok)
        print("yanlış şifre")
