import sys
from PyQt5 import QtWidgets

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication, QLabel, QCheckBox, QRadioButton, \
    QTableWidget, QTableWidgetItem


class usermeasure(QWidget):
    def __init__(self,i=14):
        super().__init__()

        self.cid=i

        print("ok")
        self.setGeometry(0,0,1500,800)
        self.setWindowTitle("VIEWING MEASUREMENTS")

        self.a=QLabel("Previous Measurements",self)
        self.a.setStyleSheet("color: red;"

                             "font: bold 25px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px")
        self.a.move(600,50)

        self.ibl_image = QLabel("IMAGE", self)
        self.ibl_image.move(100,50)
        self.ibl_image.resize(250,250)
        self.y = "pic.jpg"
        self.ibl_image.setPixmap(QPixmap(self.y))

        self.ibl_namelabel= QLabel("Name", self)
        self.ibl_namelabel.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")

        self.ibl_namelabel.move(100, 350)
        self.ibl_name = QLabel("ABCD", self)
        self.ibl_name.setStyleSheet("color: red;"

                                     "font: bold 25px;"
                                     "border-color: #FA8072;"
                                     "border-radius: 3px")
        self.ibl_name.move(300, 350)
        self.ibl_name.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")


        self.ibl_agelabel= QLabel("Age", self)
        self.ibl_agelabel.setStyleSheet("color: red;"

                                     "font: bold 25px;"
                                     "border-color: #FA8072;"
                                     "border-radius: 3px")
        self.ibl_agelabel.move(100, 400)
        self.ibl_age = QLabel("15", self)
        self.ibl_age.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")

        self.ibl_age.move(300, 400)

        self.ibl_genderlabel= QLabel("Gender", self)
        self.ibl_genderlabel.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_genderlabel.move(100, 450)
        self.ibl_agelabel.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_gender = QLabel("Female", self)
        self.ibl_gender.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_gender.move(300, 450)

        self.ibl_placelabel = QLabel("Place", self)
        self.ibl_placelabel.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_placelabel.move(100, 500)
        self.ibl_place = QLabel("Ferok", self)
        self.ibl_place.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_place.move(300, 500)


        self.ibl_districtlabel = QLabel("District", self)
        self.ibl_districtlabel.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_districtlabel.move(100, 550)
        self.ibl_district = QLabel("Kozhikode", self)
        self.ibl_district.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_district.move(300, 550)

        self.ibl_pincodelabel = QLabel("Pincode", self)
        self.ibl_pincodelabel.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_pincodelabel.move(100, 600)
        self.ibl_pincode = QLabel("673655", self)
        self.ibl_pincode.move(300, 600)
        self.ibl_pincode.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")

        self.ibl_emaillabel= QLabel("Email ID", self)
        self.ibl_emaillabel.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_emaillabel.move(100, 650)
        self.ibl_email = QLabel("abcd@gmail.com", self)
        self.ibl_email.move(300, 650)
        self.ibl_email.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")


        self.ibl_phonelabel = QLabel("Phone number", self)
        self.ibl_phonelabel.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_phonelabel.move(100, 700)
        self.ibl_phone = QLabel("8624592451", self)
        self.ibl_phone.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_phone.move(300, 700)

        self.ibl_heightlabel = QLabel("Height", self)
        self.ibl_heightlabel.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_heightlabel.move(100, 750)
        self.ibl_height = QLabel("155", self)
        self.ibl_height.setStyleSheet("color: red;"

                                        "font: bold 25px;"
                                        "border-color: #FA8072;"
                                        "border-radius: 3px")
        self.ibl_height.move(300, 750)

        self.pbn_take = QPushButton("Take new measurement ", self)
        self.pbn_take.move(980, 50)
        self.pbn_take.resize(200, 30)
        self.pbn_take.clicked.connect(self.gotocapture)

        self.pbn_logout = QPushButton("Log out ", self)
        self.pbn_logout.move(1295,50)
        self.pbn_logout.resize(100, 30)
        self.pbn_logout.clicked.connect(self.gotologin)

        self.pbn_back = QPushButton("Back ", self)
        self.pbn_back.move(1190, 50)
        self.pbn_back.resize(100, 30)
        self.pbn_back.clicked.connect(self.click)



        print("ok2")

        from DBConnection import Db
        db=Db()

        qry="SELECT * FROM `customer` WHERE `cid`='"+str(i)+"'"
        print(qry)
        res=db.selectOne(qry)
        if res is not None:

            self.ibl_name.setText(res['name'])
            self.ibl_age.setText(str(res['age']))
            self.ibl_district.setText(res['district'])
            self.ibl_email.setText(res['emailid'])
            self.ibl_gender.setText(res['gender'])
            self.ibl_height.setText(str(res['height']))
            self.ibl_phone.setText(res['phonenumber'])
            self.ibl_pincode.setText(str(res['pincode']))
            self.ibl_place.setText(res['place'])

            y = res["image"]
            self.ibl_image.setPixmap(QPixmap(y).scaled(250, 250))


        qry="select * from measurement where cid='"+str(self.cid)+"'"
        res=db.select(qry)

        self.tableWidget2 = QTableWidget(self)

        self.tableWidget2.setHorizontalHeaderLabels(["Header-1", "Header-2"])
        self.tableWidget2.setRowCount(len(res))
        self.tableWidget2.setColumnCount(11)
        self.tableWidget2.move(600,100)
        self.tableWidget2.resize(800,600)

        self.tableWidget2.setHorizontalHeaderLabels(['Date', 'Shoulder', 'RightUpperArm', 'RighLlowerArm', 'LeftUpperArm','LeftLowerArm','Hip','RightUpperLeg ','RightLowerLeg','LeftUpperLeg','LeftLowerLeg'])

        k=0
        for i in res:
            self.tableWidget2.setItem(k, 0, QTableWidgetItem(str(i['mdate'])))
            self.tableWidget2.setItem(k, 1, QTableWidgetItem(str(i['m1'])))
            self.tableWidget2.setItem(k, 2, QTableWidgetItem(str(i['m2'])))
            self.tableWidget2.setItem(k, 3, QTableWidgetItem(str(i['m3'])))
            self.tableWidget2.setItem(k, 4, QTableWidgetItem(str(i['m4'])))
            self.tableWidget2.setItem(k, 5, QTableWidgetItem(str(i['m5'])))
            self.tableWidget2.setItem(k, 6, QTableWidgetItem(str(i['m6'])))
            self.tableWidget2.setItem(k, 7, QTableWidgetItem(str(i['m7'])))
            self.tableWidget2.setItem(k, 8, QTableWidgetItem(str(i['m8'])))
            self.tableWidget2.setItem(k, 9, QTableWidgetItem(str(i['m9'])))
            self.tableWidget2.setItem(k, 10, QTableWidgetItem(str(i['m10'])))
            k=k+1

        header = self.tableWidget2.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(10, QtWidgets.QHeaderView.ResizeToContents)
        self.show()

    def gotocapture(self):
        from CAPTURE import usercapture
        self.h=usercapture(self.cid)
        # self.hide()

    def gotologin(self):
            from LOGIN import loginpage
            self.r=loginpage()
            self.hide()

    def click(self):
        from VIEW import userview
        self.v=userview()
        self.hide()

if __name__=="__main__" :
    app=QApplication(sys.argv)
    a=usermeasure()
    sys.exit(app.exec())