from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from camera import Ui_camera
from rapport import Ui_rapport

class Ui_Dash(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 575)
        # add
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 802, 501))
        self.widget.setStyleSheet("background:rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"")
        self.widget.setObjectName("widget")
        self.menubar_2 = QtWidgets.QLabel(self.widget)
        self.menubar_2.setGeometry(QtCore.QRect(0, 0, 191, 501))
        self.menubar_2.setStyleSheet("background-color: rgb(165, 165, 189);\n"
"border-rabius: none; ")
        self.menubar_2.setText("")
        self.menubar_2.setObjectName("menubar_2")
        self.dashboard = QtWidgets.QPushButton(self.widget)
        # add
        self.dashboard.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\dashboard.png'))

        self.dashboard.setGeometry(QtCore.QRect(0, 151, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dashboard.setFont(font)
        self.dashboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dashboard.setStyleSheet("QPushButton#dashboard{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#dashboard:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#dashboard:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")
        
        self.dashboard.setObjectName("dashboard")
        self.employee = QtWidgets.QPushButton(self.widget)
        # add
        self.employee.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\group.png'))

        self.employee.setGeometry(QtCore.QRect(0, 187, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.employee.setFont(font)
        self.employee.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.employee.setStyleSheet("QPushButton#employee{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#employee:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#employee:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")
        
        self.employee.setObjectName("employee")
        self.rapport = QtWidgets.QPushButton(self.widget)
        # add
        self.rapport.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\rapport.png'))

        self.rapport.setGeometry(QtCore.QRect(0, 223, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rapport.setFont(font)
        self.rapport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rapport.setStyleSheet("QPushButton#rapport{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#rapport:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#rapport:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")
        
        self.rapport.setObjectName("rapport")
        self.chat = QtWidgets.QPushButton(self.widget)
        # chat
        self.chat.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\messenger.png'))

        self.chat.setGeometry(QtCore.QRect(0, 260, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chat.setFont(font)
        self.chat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chat.setStyleSheet("QPushButton#chat{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#chat:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#chat:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")

        self.chat.setObjectName("chat")
        self.terminer = QtWidgets.QPushButton(self.widget)
        # add
        self.terminer.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\exit.png'))

        self.terminer.setGeometry(QtCore.QRect(0, 450, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.terminer.setFont(font)
        self.terminer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.terminer.setStyleSheet("QPushButton#terminer{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#terminer:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#terminer:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")

        self.terminer.setObjectName("terminer")
        self.logo = QtWidgets.QLabel(self.widget)
        # add
        # self.logo.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\face.png'))

        self.logo.setGeometry(QtCore.QRect(60, 5, 61, 61))
        self.logo.setStyleSheet("\n"
"    background-image: url(:/logo/face-detection.png);\n"
"   background-color:none;\n"
" ")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 70, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;\n"
"background-color: none;\n"
"color: #887575;")
        self.label.setObjectName("label")
        self.recherche = QtWidgets.QLineEdit(self.widget)
        self.recherche.setGeometry(QtCore.QRect(270, 30, 311, 20))
        self.recherche.setStyleSheet("                max-width: 300px;\n"
"                padding: 0px 12px; \n"
"                border-radius: 8px;\n"
"                border: 1px solid #000000;\n"
"                outline: none;\n"
"                box-shadow: 0px 0px 20px -18px; ")
        self.recherche.setObjectName("recherche")
        self.user_pic = QtWidgets.QLabel(self.widget)
        self.user_pic.setGeometry(QtCore.QRect(740, 20, 40, 40))
        self.user_pic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_pic.setStyleSheet("\n"
"    width: 40px; \n"
"    height: 40px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius: 20px;\n"
"\n"
"")
        self.user_pic.setText("")
        self.user_pic.setObjectName("user_pic")
        self.userName = QtWidgets.QLabel(self.widget)
        self.userName.setGeometry(QtCore.QRect(672, 30, 51, 16))
        self.userName.setObjectName("userName")
        self.notification_btn = QtWidgets.QPushButton(self.widget)

        self.notification_btn.setGeometry(QtCore.QRect(620, 30, 21, 21))
        self.notification_btn.setStyleSheet("        QPushButton{ \n"
"        border: none;\n"
"        }\n"
"        QPushButton:hover{\n"
"         border: #B3D9E4;                           \n"
"        }  ")
        self.notification_btn.setText("")
        # add
        self.notification_btn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\not.png'))

        self.notification_btn.setObjectName("notification_btn")
        self.recherche_btn = QtWidgets.QPushButton(self.widget)
        self.recherche_btn.setGeometry(QtCore.QRect(550, 31, 15, 15))
        self.recherche_btn.setStyleSheet("        QPushButton{ \n"
"        border: none;\n"
"        }\n"
"        QPushButton:hover{\n"
"         border: #B3D9E4;                           \n"
"        }  ")
        self.recherche_btn.setText("")
        self.recherche_btn.setObjectName("recherche_btn")
         # add
        self.recherche_btn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\glass.png'))
        self.close_btn = QtWidgets.QPushButton(self.widget)
        # add
        self.close_btn.clicked.connect(exit)
        self.close_btn.setGeometry(QtCore.QRect(784, 10, 10, 10))
        self.close_btn.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 60, 63);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgb(255, 90, 93);\n"
"}")
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        # add
        def reduir():
            MainWindow.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.widget)
        self.reduit.clicked.connect(reduir)
        self.reduit.setGeometry(QtCore.QRect(770, 10, 10, 10))
        self.reduit.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 255, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(84, 255, 90);\n"
"}")
        self.reduit.setText("")
        self.reduit.setObjectName("reduit")
        self.cam = QtWidgets.QPushButton(self.widget)
        self.cam.setGeometry(QtCore.QRect(0, 300, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cam.setFont(font)
        self.cam.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cam.setStyleSheet("QPushButton#cam{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton#cam:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton#cam:pressed { \n"
" background:#A5A5BD ;\n"
"}\n"
"")     
         # add
        self.cam.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\camera.png'))

        self.cam.setObjectName("cam")
        self.themr = QtWidgets.QPushButton(self.widget)
        self.themr.setGeometry(QtCore.QRect(0, 414, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.themr.setFont(font)
        self.themr.setStyleSheet("QPushButton{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}")

        self.themr.setObjectName("themr")
         # add
        self.themr.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\theme.png'))

        self.profil = QtWidgets.QPushButton(self.widget)
        self.profil.setGeometry(QtCore.QRect(0, 377, 191, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.profil.setFont(font)
        self.profil.setStyleSheet("QPushButton{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}")
         # add
        self.profil.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\user.png'))

        self.profil.setObjectName("profil")
        self.hide_btn = QtWidgets.QPushButton(self.widget)
        # add
        self.hide_btn.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\SmartFace\\icon\\menu.png'))

        self.hide_btn.setGeometry(QtCore.QRect(150, 10, 31, 23))
        self.hide_btn.setStyleSheet("QPushButton{\n"
"background-color:#A5A5BD;\n"
"border:none;\n"
"color:#000000;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#D9D9D9;\n"
"border-radius: 5px;\n"
"text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"}\n"
"QPushButton:pressed { \n"
" background:#A5A5BD ;\n"
"}")
        self.hide_btn.setText("")
        self.hide_btn.setObjectName("hide_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.widget.mousePressEvent = self.mouseclick
        self.widget.mouseMoveEvent = self.mousemove

        self.cam.clicked.connect(self.open_cam)
        self.rapport.clicked.connect(self.open_rapport)



    def open_rapport(self):
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_rapport()
        self.work.setupUi(self.work_window)
        self.work_window.show()
        MainWindow.hide()        

    def open_cam(self):
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_camera()
        self.work.setupUi(self.work_window)
        self.work_window.show()
        MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dashboard.setText(_translate("MainWindow", "Tableau de bord"))
        self.employee.setText(_translate("MainWindow", "Employée           "))
        self.rapport.setText(_translate("MainWindow", "Rapport               "))
        self.chat.setText(_translate("MainWindow", "Chat                     "))
        self.terminer.setText(_translate("MainWindow", "Quitter                 "))
        self.label.setText(_translate("MainWindow", "Face smart project"))
        self.recherche.setPlaceholderText(_translate("MainWindow", "Rechercher ici ..."))
        self.userName.setText(_translate("MainWindow", "user name"))
        self.cam.setText(_translate("MainWindow", "Camera               "))
        self.themr.setText(_translate("MainWindow", "Théme                 "))
        self.profil.setText(_translate("MainWindow", "Profil                    "))

    def mouseclick(self, event):
        if event.button() == Qt.LeftButton:
            self.mouseclick = event.globalPos()
            self.mousemove = event.globalPos() - MainWindow.pos()
    
    def mousemove(self, event):
        if event.buttons() == Qt.LeftButton:
                position = event.globalPos()
                diff = position - self.mouseclick
                MainWindow.move(diff)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dash()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
