import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication, QLabel, QCheckBox, QRadioButton


class loginpage(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,2000,1000)
        self.setWindowTitle("LOGIN")
        self.d=QPushButton("Login",self)
        self.d.move(500,600)
        self.d.resize(185, 50)
        self.lbl=QLabel("", self)
        self.lbl.move(450, 675)
        self.lbl.resize(350, 40)
        self.d.clicked.connect(self.click)

        self.b=QLabel("ADMIN LOGIN",self)
        self.b.setStyleSheet("color: red;"
                                     
                                      "font: bold 25px;"
                                      "border-color: #FA8072;"
                                      "border-radius: 3px")


        self.b.move(400,200)
        self.b.resize(350, 40)
        self.ibl_image = QLabel("IMAGE", self)
        self.ibl_image.move(900,0)
        self.ibl_image.resize(975,1000)
        self.y="backgd.jpg"
        self.ibl_image.setPixmap(QPixmap(self.y).scaled(975,1000))
        self.a = QLabel("USERNAME", self)
        self.a.setStyleSheet("color: red;"

                       "font: bold 25px;"
                       "border-color: #FA8072;"
                       "border-radius: 3px")


        self.a.move(280, 300)
        self.f = QLabel("PASSWORD", self)
        self.f.setStyleSheet("color: red;"

                       "font: bold 25px;"
                       "border-color: #FA8072;"
                       "border-radius: 3px")
        self.f.move(280, 450)
        self.i = QLineEdit(self)
        self.i.move(280, 350)
        self.i.resize(400, 40)
        self.e = QLineEdit(self)
        self.e.move(280, 500)
        self.e.resize(400, 40)
        self.show()
    def click(self):
        from VIEW import userview
        from DBConnection import Db
        username=self.i.text()
        password=self.e.text()
        self.a="SELECT * FROM login WHERE uname='"+username+"' AND PASSWORD='"+password+"'"
        self.r=Db()
        rvs=self.r.selectOne(self.a)
        if rvs is None:
            print('invalid')
            self.lbl.setText("invalid user")
        else:
            self.v=userview()
            self.hide()

if __name__=="__main__" :
    app=QApplication(sys.argv)
    a=loginpage()
    sys.exit(app.exec())