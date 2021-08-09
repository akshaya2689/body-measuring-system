import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication, QLabel, QCheckBox, QRadioButton, QGroupBox, \
    QGridLayout, QVBoxLayout, QHBoxLayout


class userview(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1500,920)
        self.setWindowTitle("VIEW ALL USERS")

        topwidget=QWidget()
        topwidget.resize(100,100)
        topwidget.setStyleSheet("background-image : url(viewbackground.jpg)")



        # ibl_icon = QLabel("SEARCH",topwidget )
        # ibl_icon.move(100, 0)
        # ibl_icon.resize(100, 60)
        # x = "search.jpg"
        # ibl_icon.setPixmap(QPixmap(x))

        #
        # led_search = QLineEdit(topwidget)
        # led_search.move(300, 0)
        #
        pbn_new= QPushButton("New",topwidget)
        pbn_new.setStyleSheet("color: white;"

                       "font: bold 48px;"
                     
                       "border-color: #FA8072;"
                       "border-radius: 3px")
        pbn_new.move(10,360)


        pbn_new.clicked.connect(self.newreg)
        # #
        # ibl_back = QPushButton("Back",topwidget)
        # ibl_back.move(600, 0)
        # ibl_back.clicked.connect(self.gotologin)
        #




        from DBConnection import Db
        self.r="SELECT * FROM customer"
        db=Db()
        s=db.select(self.r)
        print("---",s)
        # self.horizontalGroupBox = QGroupBox("Grid",parent=self)
        # self.horizontalGroupBox.move(100,100)
        self.a=QWidget(self)


        layout = QGridLayout()



        # self.layout.setColumnStretch(0,5)
        # layout.setColumnStretch(2, len(s))
        self.k=0
        for i in range(1,int(len(s)/5)+1):

            for j in range(0,5):

                    k=s[(i-1)*5+j]

                    central_widget = QWidget()  # Create a central widget
                    central_widget.setStyleSheet("background:white")
                    central_widget.resize(200,200)
                    ibl_image = QLabel("IMAGE", central_widget)
                    ibl_image.move(10, 50)
                    ibl_image.resize(150, 150)
                    y =k["image"]
                    ibl_image.setPixmap(QPixmap(y).scaled(150,150))
                    lb1 = QPushButton("...", central_widget)
                    lb1.move(200,10)

                    lb1.setStyleSheet("color: red;"
                                  
                                   "font: bold 24px;"
                                "background-color : yellow;"
                                   "border-color: #FA8072;"
                                   "border-radius: 3px")



                    # lb1.move(100,10)

                    lblsname= QLabel(k["name"],central_widget)
                    lblsname.move(10,10)

                    lblsemail = QLabel(k["emailid"], central_widget)
                    lblsemail.move(10, 30)

                    # lb1.clicked.connect(lambda: self.new(str(k['cid'])))
                    lb1.clicked.connect(lambda ch, i=str(k['cid']): self.new(i))
                    layout.addWidget(central_widget, i, j)
        m=0
        m=int(len(s)/5)*5

        i=(len(s)/5)
        i=i+1


        print(len(s),m,"hooy")

        for j in range(0,len(s)-(int(len(s)/5)*5)):
            # for j in range(0, 5):
                k = s[m+j]
                central_widget = QWidget()  # Create a central widget
                central_widget.setStyleSheet("background:white")
                central_widget.resize(150, 150)
                ibl_image = QLabel("IMAGE", central_widget)
                ibl_image.move(10, 40)
                ibl_image.resize(150, 150)
                y = k["image"]
                ibl_image.setPixmap(QPixmap(y).scaled(150, 150))

                lb1 = QPushButton("...", central_widget)
                lb1.move(200, 10)
                lb1.setStyleSheet("color: red;"
                          "font: bold 24px;"
                          "background-color : yellow;"
                          "border-color: #FA8072;"
                          "border-radius: 3px")
                lblsname = QLabel(k["name"], central_widget)
                lblsname.move(10, 10)

                lblsemail = QLabel(k["emailid"], central_widget)
                lblsemail.move(10, 30)

                # lb1.clicked.connect(lambda: self.new(str(k['cid'])))
                lb1.clicked.connect(lambda ch, i=str(k['cid']): self.new(i))
                layout.addWidget(central_widget, i, j)

        layouts = QVBoxLayout()
        # Add widgets to the layout




        w=QWidget()
        w.setLayout(layout)
        layouts.addWidget(topwidget)
        layouts.addWidget(w)
        self.setLayout(layouts)
        self.show()
    def new(self,i):
        print(i)
        from MEASURE import usermeasure
        self.w=usermeasure(i)
        self.hide()

    def newreg(self,i):
        print(i)
        from DETAILS import userdetails
        self.w=userdetails(i)
        self.hide()


    def gotomeasure(self):
        from MEASURE import usermeasure
        self.u=usermeasure()
        self.hide()
    def gotologin(self):
            from LOGIN import loginpage
            self.r=loginpage()
            self.hide()
if __name__=="__main__" :
    app=QApplication(sys.argv)
    a=userview()
    sys.exit(app.exec())