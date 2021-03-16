import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from join import *
from reg import *
import sqlite3


class Reg(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Reg()
        self.ui.setupUi(self)

        self.ui.label_error.hide()

        self.ui.pushButton.clicked.connect(self.go_back)
        self.ui.btn_reg.clicked.connect(self.register)

        # self.con = sqlite3.connect("DATABASE.db")
        # self.curs = self.con.cursor()

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

        # self.curs.execute(
        #     """INSRET INTO UserForm(name, surname, otchestvo, login, password) VALUES("{}", "{}", "{}", "{}", "{}") """)
        # self.con.commit()
        # self.con.close()


class Join(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Join()
        self.ui.setupUi(self)

        self.ui.btn_join.clicked.connect(self.go_join)
        self.ui.btn_reg.clicked.connect(self.go_reg)

    def go_join(self):
        pass

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
