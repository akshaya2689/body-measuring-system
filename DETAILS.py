import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication, QLabel, QCheckBox, QRadioButton, QFileDialog

from DBConnection import Db


class userdetails(QWidget):
    def __init__(self, i=0):
        super().__init__()
        self.setGeometry(0, 0, 1500, 920)
        self.setWindowTitle("DETAIL")

        self.a = QLabel("CUSTOMER DETAILS", self)
        self.a.move(600, 50)
        self.a.setStyleSheet("color: red;"

                             "font: bold 25px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px")

        self.ibl_image = QLabel("IMAGE", self)
        self.ibl_image.move(900, 150)
        self.ibl_image.resize(300, 300)
        self.y = "pic.jpg"
        self.ibl_image.setPixmap(QPixmap(self.y))

        self.ibl_name = QLabel("Name", self)
        self.ibl_name.move(100, 150)
        self.led_name = QLineEdit(self)
        self.led_name.move(100, 175)
        self.led_name.resize(400, 30)

        self.ibl_age = QLabel("Age", self)
        self.ibl_age.move(100, 225)
        self.led_age = QLineEdit(self)
        self.led_age.move(100, 250)
        self.led_age.resize(400, 30)

        self.ibl_gender = QLabel("Gender", self)
        self.ibl_gender.move(100, 300)
        self.rbn_male = QRadioButton("Male", self)
        self.rbn_male.move(100, 325)
        self.rbn_female = QRadioButton("Female", self)
        self.rbn_female.move(300, 325)

        self.ibl_place = QLabel("Place", self)
        self.ibl_place.move(100, 375)
        self.led_place = QLineEdit(self)
        self.led_place.move(100, 400)
        self.led_place.resize(400, 30)

        self.ibl_district = QLabel("District", self)
        self.ibl_district.move(100, 450)
        self.led_district = QLineEdit(self)
        self.led_district.move(100, 475)
        self.led_district.resize(400, 30)

        self.ibl_pincode = QLabel("Pincode", self)
        self.ibl_pincode.move(100, 525)
        self.led_pincode = QLineEdit(self)
        self.led_pincode.move(100, 550)
        self.led_pincode.resize(400, 30)

        self.ibl_email = QLabel("Email ID", self)
        self.ibl_email.move(100, 600)
        self.led_email = QLineEdit(self)
        self.led_email.move(100, 625)
        self.led_email.resize(400, 30)

        self.ibl_phone = QLabel("Phone number", self)
        self.ibl_phone.move(100, 675)
        self.led_phone = QLineEdit(self)
        self.led_phone.move(100, 700)
        self.led_phone.resize(400, 30)

        self.ibl_height = QLabel("Height", self)
        self.ibl_height.move(100, 750)
        self.led_height = QLineEdit(self)
        self.led_height.move(100, 775)
        self.led_height.resize(400, 30)

        self.pbn_save = QPushButton("Save", self)
        self.pbn_save.move(100, 850)
        self.pbn_save.resize(145, 50)
        self.pbn_save.setStyleSheet("color: red;"
                                          "border-style: solid;"
                                          "border-width: 2px;"
                                          "font: bold 14px;"
                                          "border-color: #FA8072;"
                                          "border-radius: 3px")

        self.pbn_save.clicked.connect(self.gotoview)

        self.pbn_cancel = QPushButton("Cancel", self)
        self.pbn_cancel.move(250, 850)
        self.pbn_cancel.resize(145, 50)
        self.pbn_cancel.setStyleSheet("color: red;"
                                          "border-style: solid;"
                                          "border-width: 2px;"
                                          "font: bold 14px;"
                                          "border-color: #FA8072;"
                                          "border-radius: 3px")

        self.pbn_cancel.clicked.connect(self.gotoview)

        self.pbn_capture = QPushButton("Capture", self)
        self.pbn_capture.move(900, 500)
        self.pbn_capture.resize(300, 50)
        self.pbn_capture.setStyleSheet("color: red;"
                                          "border-style: solid;"
                                          "border-width: 2px;"
                                          "font: bold 14px;"
                                          "border-color: #FA8072;"
                                          "border-radius: 3px")

        self.pbn_capture.clicked.connect(self.imagebrowse)

        print(i)

        db = Db()

        qry = "SELECT * FROM `customer` WHERE `cid`='" + str(i) + "'"
        res = db.selectOne(qry)
        if res is not None:
            pass
            self.led_name.setText(res["name"])
        self.show()

    def gotoview(self):
        from DBConnection import Db
        name = self.led_name.text()
        age = self.led_age.text()
        place = self.led_place.text()
        district = self.led_district.text()
        pincode = self.led_pincode.text()
        email = self.led_email.text()
        phonenumber = self.led_phone.text()
        height = self.led_height.text()
        gender = ""
        if self.rbn_male.isChecked():
            gender = "male"
        else:
            gender = "female"

        self.d = "INSERT INTO customer(NAME,age,gender,place,district,pincode,emailid,phonenumber,height,image) VALUES('" + name + "','" + age + "','" + gender + "','" + place + "','" + district + "','" + pincode + "','" + email + "','" + phonenumber + "','" + height + "','" + self.timestr + ".jpg" + "')"
        self.g = Db()
        self.g.insert(self.d)
        from VIEW import userview
        self.s = userview()
        self.hide()

    def imagebrowse(self):
        import cv2

        # define a video capture object
        vid = cv2.VideoCapture(0)

        while (True):

            # Capture the video frame
            # by frame
            ret, frame = vid.read()

            # Display the resulting frame
            cv2.imshow('frame', frame)

            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice

            import time
            self.timestr = time.strftime("%Y%m%d-%H%M%S")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite(self.timestr + ".jpg", frame)

                break

        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        self.ibl_image.setPixmap(QPixmap(self.timestr + ".jpg").scaled(400, 400))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = userdetails()
    sys.exit(app.exec())