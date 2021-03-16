import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from join import *
from reg import *
from Zap_Step1 import *
from Zap_Step2 import *
from menu import *
import sqlite3


class Reg(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Reg()
        self.ui.setupUi(self)

        self.ui.label_error.hide()

        self.ui.pushButton.clicked.connect(self.go_back)
        self.ui.btn_reg.clicked.connect(self.register)

    def go_back(self):
        try:
            self.win = Join(self)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)

    def register(self):
        Name = None
        Surname = None
        Otch = None
        Sex = None
        Login = None
        Password = None

        if len(self.ui.edit_name.text()) > 0:
            Name = self.ui.edit_name.text()
        else:
            self.ui.label_error.show()
            return

        if len(self.ui.edit_surname.text()) > 0:
            Surname = self.ui.edit_surname.text()
        else:
            self.ui.label_error.show()
            return

        if len(self.ui.edit_dad.text()) > 0:
            Otch = self.ui.edit_dad.text()
        else:
            self.ui.label_error.show()
            return

        if len(self.ui.edit_mail.text()) > 0:
            Login = self.ui.edit_mail.text()
        else:
            self.ui.label_error.show()
            return

        if len(self.ui.edit_password.text()) > 0:
            Password = self.ui.edit_password.text()
        else:
            self.ui.label_error.show()
            return

        radio_base = [self.ui.radioButton_female, self.ui.radioButton_male]
        for rad in radio_base:
            if rad.isChecked():
                Sex = rad.text()

        if not Sex:
            self.ui.label_error.show()
            return

        try:
            con = sqlite3.connect("../DATABASE.db")
            curs = con.cursor()
            curs.execute(
                f"""INSERT INTO UserForm(name, surname, otchestvo, password, email, sex) VALUES("{Name}", "{Surname}", "{Otch}", "{Password}", "{Login}", "{Sex}") """)
            con.commit()
            con.close()
        except sqlite3.IntegrityError:
            print("Этот email уже используется")

        try:
            self.win = Join(self)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class Zap_Step1(QtWidgets.QMainWindow):
    def __init__(self, parent=None, person=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Zap_Step1()
        self.ui.setupUi(self)

        self.person = person

        self.ui.btn_next.clicked.connect(self.go_next)

        self.ui.btn_load_photo.clicked.connect(self.load_photo)

    def load_photo(self):
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'headers', 'filename')

    def go_next(self):
        radio_base_sex = [self.ui.radioButton_female, self.ui.radioButton_male]
        Surname = self.ui.edit_surname.text()
        Name = self.ui.edit_name.text()
        Otch = self.ui.edit_dad.text()
        Sex = None
        for i in radio_base_sex:
            if i.isChecked():
                Sex = i.text()
        Login = self.ui.edit_mail.text()
        Date = self.ui.edit_date.text()
        Phone = self.ui.edit_phone.text()
        Birth_place = self.ui.edit_birth_place.text()
        Life = None
        Photo = self.file_path
        radio_base_life = [self.ui.radioButton_yes, self.ui.radioButton_no]
        for i in radio_base_life:
            if i.isChecked():
                Life = i.text()

        id = self.person[0][0]

        con = sqlite3.connect("DATABASE.db")
        curs = con.cursor()
        curs.execute(
            f"""UPDATE UserForm SET name = "{Name}", surname = "{Surname}", otchestvo = "{Otch}", sex = "{Sex}", email = "{Login}", birthday = "{Date}", place_of_birth = "{Birth_place}", phone_number = "{Phone}", photo_path = "{Photo}", campus = "{Life}" WHERE id = "{id}" """)  # если не будет работать, убери кавычки на id
        con.commit()
        con.close()

        try:
            self.win = Zap_Step2(self, person=self.person)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class Zap_Step2(QtWidgets.QMainWindow):
    def __init__(self, parent=None, person=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Zap_Step2()
        self.ui.setupUi(self)

        self.person = person

        self.ui.btn_next.clicked.connect(self.go_next)

    def go_next(self):
        try:
            self.win = Zap_Step3(self, person=self.person)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class Menu(QtWidgets.QMainWindow):
    def __init__(self, parent=None, person=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Menu()
        self.ui.setupUi(self)

        self.person = person

        self.ui.pushButton.clicked.connect(self.go_zap)
        self.ui.pushButton_2.clicked.connect(self.go_watch)
        self.ui.pushButton_3.clicked.connect(self.go_change)

    def go_zap(self):
        try:
            self.win = Zap_Step1(self, person=self.person)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)

    def go_watch(self):
        pass

    def go_change(self):
        pass


class Join(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Join()
        self.ui.setupUi(self)

        self.ui.label_error.hide()

        self.ui.btn_join.clicked.connect(self.go_join)
        self.ui.btn_reg.clicked.connect(self.go_reg)

    def go_join(self):
        Login = None
        Password = None

        if len(self.ui.edit_login.text()) > 0:
            Login = self.ui.edit_login.text()
        else:
            self.ui.label_error.setText("Введите логин и пароль")
            self.ui.label_error.show()
            return

        if len(self.ui.edit_password.text()) > 0:
            Password = self.ui.edit_password.text()
        else:
            self.ui.label_error.setText("Введите логин и пароль")
            self.ui.label_error.show()
            return

        con = sqlite3.connect("DATABASE.db")
        curs = con.cursor()
        ex = curs.execute(
            """SELECT * FROM UserForm WHERE email = "{}" and password = "{}" """.format(Login, Password)).fetchall()
        con.commit()
        con.close()
        if not ex:
            self.ui.label_error.setText("Неверный логин или пароль")
            self.ui.label_error.show()
            return
        else:
            try:
                self.win = Menu(self, person=ex)
                self.close()
                self.win.show()

            except Exception as er:
                print(er)

    def go_reg(self):
        try:
            self.win = Reg(self)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = Join()
        myapp.show()
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex)
