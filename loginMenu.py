from PyQt5.QtWidgets import QMessageBox


def init_loginMenu():
      print("")



def login(self,username,password):
    print(username)
    print(password)
    if username == "emre" and password == "1234":
        print("doğru şifre")
        reply = QMessageBox.information(self, 'Kullanıcı girişi', 'Giriş başarılı', QMessageBox.Ok)
        return reply
    else:
        reply = QMessageBox.warning(self, 'Kullanıcı girişi', 'Yalnış Kullanıcı adı veya şifre', QMessageBox.Ok)
        print("yanlış şifre")
