import sys
from math import sqrt

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication, QLabel, QCheckBox, QRadioButton, QFileDialog, \
    QTableWidget, QTableWidgetItem, QHBoxLayout

from measure_Sample import poseestimation


class usercapture(QWidget):
    def __init__(self,cid=15):
        super().__init__()



        from DBConnection import  Db
        db=Db()
        qry="SELECT `height` FROM `customer` WHERE `cid`='"+str(cid)+"'"
        ress=db.selectOne(qry)
        self.heightofperson=int(ress['height'])




        self.cid=cid
        self.setGeometry(0,0,1500,1000)
        self.setWindowTitle("CAPTURE")

        self.la = QHBoxLayout()

        self.ibl_image = QLabel("capture", self)
        self.ibl_image.move(50,50)
        self.ibl_image.resize(400,400)
        self.z = "capture.jpg"
        self.ibl_image.setPixmap(QPixmap(self.z).scaled(400,400))

        self.ibl_image2 = QLabel("capture", self)
        self.ibl_image2.move(50, 550)
        self.ibl_image2.resize(400, 400)
        self.z = "capture.jpg"
        self.ibl_image2.setPixmap(QPixmap(self.z).scaled(400, 400))




        self.ibl_label= QLabel("POSE POINTS", self)
        self.ibl_label.move(500, 50)
        self.ibl_label.setStyleSheet("color: red;"
                      "border-style: solid;"
                      "border-width: 2px;"
                      "font: bold 14px;"
                      "border-color: #FA8072;"
                      "border-radius: 3px")




        self.tableWidget = QTableWidget(self)

        self.tableWidget.setHorizontalHeaderLabels(["Header-1", "Header-2", "Header-3"])
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)

        self.tableWidget.move(500, 100)
        self.tableWidget.resize(400,800)



        self.tableWidget2 = QTableWidget(self)

        self.tableWidget2.setHorizontalHeaderLabels(["Header-1", "Header-2"])
        self.tableWidget2.setRowCount(4)
        self.tableWidget2.setColumnCount(2)

        self.tableWidget2.move(925, 100)
        self.tableWidget2.resize(280, 800)

        self.ibl_label2 = QLabel("MEASUREMENTS(in cm)", self)
        self.ibl_label2.move(925, 50)
        self.ibl_label2.setStyleSheet("color: red;"
                                     "border-style: solid;"
                                     "border-width: 2px;"
                                     "font: bold 14px;"
                                     "border-color: #FA8072;"
                                     "border-radius: 3px")

        self.ibl_label2back = QPushButton("Back", self)
        self.ibl_label2back.move(1170, 50)
        self.ibl_label2back.setStyleSheet("color: red;"
                                      "border-style: solid;"
                                      "border-width: 2px;"
                                      "font: bold 14px;"
                                      "border-color: #FA8072;"
                                      "border-radius: 3px")

        self.ibl_label2back.clicked.connect(self.back)








        self.ibl_size= QLabel("Precise Size:", self)
        self.ibl_size.move(800, 935)
        self.ibl_size.setStyleSheet("color: red;"
                                      "border-style: solid;"
                                      "border-width: 2px;"
                                      "font: bold 14px;"
                                      "border-color: #FA8072;"
                                      "border-radius: 3px")

        self.ibl_small = QLabel("Small", self)
        self.ibl_small.move(900, 935)
        self.ibl_small.resize(100, 20)
        self.ibl_small.setStyleSheet("color: green;"
                                      "border-style: solid;"
                                      "border-width: 2px;"
                                      "font: bold 14px;"
                                      "border-color: green;"
                                      "border-radius: 3px")

        self.pbn_save=QPushButton("Save",self)
        self.pbn_save.move(1500,90)
        self.pbn_save.resize(145,30)
        self.pbn_save.clicked.connect(self.gotomeasure)

        self.pbn_cancel=QPushButton("Cancel",self)
        self.pbn_cancel.move(1650,90)
        self.pbn_cancel.resize(145,30)
        self.pbn_cancel.clicked.connect(self.gotomeasure)

        self.pbn_capture = QPushButton("Capture", self)
        self.pbn_capture.move(50, 470)
        self.pbn_capture.resize(150, 50)
        self.pbn_capture.setStyleSheet("color: red;"
                       "border-style: solid;"
                       "border-width: 2px;"
                       "font: bold 14px;"
                       "border-color: #FA8072;"
                       "background-color:#000000"
                       "border-radius: 3px")
        self.pbn_capture.clicked.connect(self.captures)


        self.pbn_browse = QPushButton("Browse", self)
        self.pbn_browse.move(200, 470)
        self.pbn_browse.resize(150, 50)
        self.pbn_browse.clicked.connect(self.browse)
        self.pbn_browse.setStyleSheet("color: red;"
                                       "border-style: solid;"
                                       "border-width: 2px;"
                                       "font: bold 14px;"
                                       "border-color: #FA8072;"
                                       "background-color:#000000"
                                       "border-radius: 3px")

        self.show()

    def back(self):
        from MEASURE import usermeasure
        self.l=usermeasure(self.cid)
        self.l.show()
        self.hide()

    def poseestimate(self,q):
        totalpoints, w, h = poseestimation(q)

        m = 0

        self.tableWidget.setRowCount(len(totalpoints))
        for i in totalpoints:
            self.tableWidget.setItem(m, 0, QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(m, 1, QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(m, 2, QTableWidgetItem(str(i[2])))

            m = m + 1

        self.z = "as_coco.jpg"
        self.ibl_image2.setPixmap(QPixmap(self.z).scaled(400, 400))


        try:  # 0-13
            zeropoint = totalpoints[0]
            levenpoint = totalpoints[13]
            x1 = int(zeropoint[1])
            x2 = int(levenpoint[1])
            y1 = int(zeropoint[2])
            y2 = int(levenpoint[2])
            self.zerothirteen = self.getdistance(x1, x2, y1, y2)
            print("eightpoint", self.zerothirteen)
            self.tableWidget2.setItem(10, 0, QTableWidgetItem("zero-thirteen"))
            self.tableWidget2.setItem(10, 1, QTableWidgetItem(str(self.zerothirteen)))
            self.onepixelratio= self.zerothirteen/ self.heightofperson

            print(self.onepixelratio,"totals",self.zerothirteen,self.heightofperson)

            # shouldersize
        except Exception as aa:
            print("errrrrr",aa)
            pass

        self.tableWidget2.setRowCount(10)
        try:
            twopoint = totalpoints[2]
            fivepoint = totalpoints[5]
            x1 = int(twopoint[1])
            x2 = int(fivepoint[1])
            y1 = int(twopoint[2])
            y2 = int(fivepoint[2])
            self.two_five = self.getdistance(x1, x2, y1, y2)
            # print("two five", two_five)

            self.tableWidget2.setItem(0, 0, QTableWidgetItem("Shoulder"))
            self.tableWidget2.setItem(0, 1, QTableWidgetItem(str(self.two_five/self.onepixelratio)))





                    # shouldersize
        except:
            pass

        try:
            twopoint = totalpoints[2]
            threepoint = totalpoints[3]
            x1 = int(twopoint[1])
            x2 = int(threepoint[1])
            y1 = int(twopoint[2])
            y2 = int(threepoint[2])
            self.two_three = self.getdistance(x1, x2, y1, y2)
            # print("twothree", two_three)
            self.tableWidget2.setItem(1, 0, QTableWidgetItem("Right UpperArm"))
            self.tableWidget2.setItem(1, 1, QTableWidgetItem(str(self.two_three/self.onepixelratio)))
            # shouldersize
        except:
            pass

        try:  # 3-4
            threepoint = totalpoints[3]
            fourpoint = totalpoints[4]
            x1 = int(threepoint[1])
            x2 = int(fourpoint[1])
            y1 = int(threepoint[2])
            y2 = int(fourpoint[2])
            self.threefour = self.getdistance(x1, x2, y1, y2)
            print("Right LowerArm", self.threefour)

            self.tableWidget2.setItem(2, 0, QTableWidgetItem("Right LowerArm"))
            self.tableWidget2.setItem(2, 1, QTableWidgetItem(str(self.threefour/self.onepixelratio)))
            # shouldersize
        except:
            pass

        try:  # 5-6
            fivepoint = totalpoints[5]
            sixpoint = totalpoints[6]
            x1 = int(fivepoint[1])
            x2 = int(sixpoint[1])
            y1 = int(fivepoint[2])
            y2 = int(sixpoint[2])
            self.fivesix = self.getdistance(x1, x2, y1, y2)
            print("Left UpperArm", self.fivesix)

            self.tableWidget2.setItem(3, 0, QTableWidgetItem("Left UpperArm"))
            self.tableWidget2.setItem(3, 1, QTableWidgetItem(str(self.fivesix/self.onepixelratio)))


            # shouldersize
        except:
            pass

        try:  # 6-7
            sixpoint = totalpoints[6]
            sevenpoint = totalpoints[7]
            x1 = int(sixpoint[1])
            x2 = int(sevenpoint[1])
            y1 = int(sixpoint[2])
            y2 = int(sevenpoint[2])
            self.six_seven = self.getdistance(x1, x2, y1, y2)
            print("Left LowerArm", self.six_seven)

            self.tableWidget2.setItem(4, 0, QTableWidgetItem("Left LowerArm"))
            self.tableWidget2.setItem(4, 1, QTableWidgetItem(str(self.six_seven/self.onepixelratio)))


            # shouldersize
        except:
            pass

        try:  # 8-11
            eightpoint = totalpoints[8]
            levenpoint = totalpoints[11]
            x1 = int(eightpoint[1])
            x2 = int(levenpoint[1])
            y1 = int(eightpoint[2])
            y2 = int(levenpoint[2])
            self.eightlevenpoint = self.getdistance(x1, x2, y1, y2)

            self.tableWidget2.setItem(5, 0, QTableWidgetItem("Hip"))
            self.tableWidget2.setItem(5, 1, QTableWidgetItem(str(self.eightlevenpoint/self.onepixelratio)))


            # shouldersize
        except:
            pass

        try:  # 8-9
            eightpoint = totalpoints[8]
            levenpoint = totalpoints[9]
            x1 = int(eightpoint[1])
            x2 = int(levenpoint[1])
            y1 = int(eightpoint[2])
            y2 = int(levenpoint[2])
            self.eightnine = self.getdistance(x1, x2, y1, y2)
            print("Right UpperLeg", self.eightnine)
            self.tableWidget2.setItem(6, 0, QTableWidgetItem("Right UpperLeg"))
            self.tableWidget2.setItem(6, 1, QTableWidgetItem(str(self.eightnine/self.onepixelratio)))


            # shouldersize
        except:
            pass

        try:  # 9-10
            eightpoint = totalpoints[9]
            levenpoint = totalpoints[10]
            x1 = int(eightpoint[1])
            x2 = int(levenpoint[1])
            y1 = int(eightpoint[2])
            y2 = int(levenpoint[2])
            self.nineleven = self.getdistance(x1, x2, y1, y2)
            print("Right LowerLeg", self.nineleven)
            self.tableWidget2.setItem(7, 0, QTableWidgetItem("Right LowerLeg"))
            self.tableWidget2.setItem(7, 1, QTableWidgetItem(str(self.nineleven/self.onepixelratio)))


            # shouldersize
        except:
            pass

        try:  # 11-12
            eightpoint = totalpoints[11]
            levenpoint = totalpoints[12]
            x1 = int(eightpoint[1])
            x2 = int(levenpoint[1])
            y1 = int(eightpoint[2])
            y2 = int(levenpoint[2])
            self.leventwelve = self.getdistance(x1, x2, y1, y2)
            print("Left UpperLeg", self.leventwelve)
            self.tableWidget2.setItem(8, 0, QTableWidgetItem("Left UpperLeg"))
            self.tableWidget2.setItem(8, 1, QTableWidgetItem(str(self.leventwelve/self.onepixelratio)))


            # shouldersize
        except:
            pass

        try:  # 12-13
            twelvepoint = totalpoints[12]
            thirteenpoint = totalpoints[13]
            x1 = int(twelvepoint[1])
            x2 = int(thirteenpoint[1])
            y1 = int(twelvepoint[2])
            y2 = int(thirteenpoint[2])
            self.twelvethirteen = self.getdistance(x1, x2, y1, y2)
            self.tableWidget2.setItem(9, 0, QTableWidgetItem("Left LowerLeg"))
            self.tableWidget2.setItem(9, 1, QTableWidgetItem(str(self.twelvethirteen/self.onepixelratio)))


            # shouldersize
        except:
            pass





        print("done")


        try:
            qry="INSERT INTO `measurement` (`m1`,`m2`,`m3`,`m4`,`m5`,`m6`,`m7`,`m8`,`m9`,`m10`,`mdate`,`cid`) VALUES ('"+str(self.two_five/self.onepixelratio)+"','"+str(self.two_three/self.onepixelratio)+"','"+str(self.threefour/self.onepixelratio)+"','"+str(self.fivesix/self.onepixelratio)+"','"+str(self.six_seven/self.onepixelratio)+"','"+str(self.eightlevenpoint/self.onepixelratio)+"','"+str(self.eightnine/self.onepixelratio)+"','"+str(self.nineleven/self.onepixelratio)+"','"+str(self.leventwelve/self.onepixelratio)+"','"+str(self.twelvethirteen/self.onepixelratio)+"',NOW(),'"+str(self.cid)+"')"
            from DBConnection import Db
            db = Db()
            db.insert(qry)


            if self.two_five/self.onepixelratio <=36:
                self.ibl_small.setText("Small")
            elif self.two_five/self.onepixelratio >36 and self.two_five/self.onepixelratio <=40 :
                self.ibl_small.setText("Medium")
            elif self.two_five/self.onepixelratio >40 and self.two_five/self.onepixelratio <=42 :
                self.ibl_small.setText("Large")
            elif self.two_five/self.onepixelratio >42 and self.two_five/self.onepixelratio <=44 :
                self.ibl_small.setText("Extra Large")




        except Exception as e0:
            print(e0)

        print(qry)



    def gotomeasure(self):
        from MEASURE import usermeasure
        self.u=usermeasure()
        self.hide()

    def browse(self):

        from measure_Sample import poseestimation
        self.q=QFileDialog.getOpenFileName(self,"SELECT","SELECT FILE")
        print(self.q[0])

        self.ibl_image.setPixmap(QPixmap(self.q[0]).scaled(400,400))
        self.poseestimate(self.q[0])



    def getdistance(self,x1,x2,y1,y2):

        a= max([x2,x1])- min([x2,x1])
        b= max([y2,y1])- min([y2,y1])

        d =sqrt((a*a)+(b*b))

        return d


    def captures(self):
        # import the opencv library
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
            if cv2.waitKey(1) & 0xFF == ord('q'):

                cv2.imwrite("ks.jpg",frame)

                break

        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        self.ibl_image.setPixmap(QPixmap("ks.jpg").scaled(400, 400))

        print("started")
        self.poseestimate("ks.jpg")

        print("Stoped")


if __name__=="__main__" :
    app=QApplication(sys.argv)
    a=usercapture()
    sys.exit(app.exec())